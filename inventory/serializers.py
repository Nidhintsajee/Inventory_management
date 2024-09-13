from rest_framework import serializers
from .models import Manufacturer, Warehouse, WarehouseLocation, Item,ItemStock, ItemWarehouseStock


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'


class WarehouseLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseLocation
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    manufacturer_name = serializers.CharField(source='manufacturer.name', read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
        

class ItemStockSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)

    class Meta:
        model = ItemStock
        fields = '__all__'


class ItemWarehouseStockSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)
    warehouse_name = serializers.CharField(source='warehouse.name', read_only=True)
    warehouse_location_description = serializers.CharField(source='warehouse_location.location_description', read_only=True)

    class Meta:
        model = ItemWarehouseStock
        fields = '__all__'