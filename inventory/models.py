from django.db import models
from django.utils import timezone


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    account_number = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class WarehouseLocation(models.Model):
    location_description = models.TextField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.warehouse.name} - {self.location_description}"


class Item(models.Model):
    name = models.CharField(max_length=255)
    part_number = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not hasattr(self, 'itemstock'):
            ItemStock.objects.create(item=self, reserved_quantity=0, stock_in_hand=0)

    def __str__(self):
        return self.name


class ItemStock(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    reserved_quantity = models.IntegerField(default=0)
    stock_in_hand = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item.name} - Stock: {self.stock_in_hand}"


class ItemWarehouseStock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    warehouse_location = models.ForeignKey(WarehouseLocation, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    comments = models.TextField(blank=True)
    reserved_quantity = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        item_stock = ItemStock.objects.get(item=self.item)
        total_quantity = ItemWarehouseStock.objects.filter(item=self.item).aggregate(
            total_quantity=models.Sum('quantity'),
            total_reserved=models.Sum('reserved_quantity')
        )
        item_stock.stock_in_hand = total_quantity['total_quantity']
        item_stock.reserved_quantity = total_quantity['total_reserved']
        item_stock.save()

    def __str__(self):
        return f"{self.item.name} - {self.warehouse.name}"
