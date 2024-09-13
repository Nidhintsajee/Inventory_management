from rest_framework import generics
from .models import Manufacturer, Warehouse, WarehouseLocation, Item, ItemStock, ItemWarehouseStock
from .serializers import ManufacturerSerializer, WarehouseSerializer, WarehouseLocationSerializer, ItemSerializer, ItemStockSerializer, ItemWarehouseStockSerializer


# Manufacturer CRUD Views
class ManufacturerListCreateView(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.filter(is_delete=False)
    serializer_class = ManufacturerSerializer


class ManufacturerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.filter(is_delete=False)
    serializer_class = ManufacturerSerializer


# Warehouse CRUD Views
class WarehouseListCreateView(generics.ListCreateAPIView):
    queryset = Warehouse.objects.filter(is_delete=False)
    serializer_class = WarehouseSerializer


class WarehouseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.filter(is_delete=False)
    serializer_class = WarehouseSerializer


# WarehouseLocation CRUD Views
class WarehouseLocationListCreateView(generics.ListCreateAPIView):
    queryset = WarehouseLocation.objects.all()
    serializer_class = WarehouseLocationSerializer


class WarehouseLocationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WarehouseLocation.objects.all()
    serializer_class = WarehouseLocationSerializer


# Item CRUD Views
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.filter(is_delete=False)
    serializer_class = ItemSerializer


class ItemRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.filter(is_delete=False)
    serializer_class = ItemSerializer
    

# ItemStock CRUD Views
class ItemStockListCreateView(generics.ListCreateAPIView):
    queryset = ItemStock.objects.all()
    serializer_class = ItemStockSerializer


class ItemStockRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemStock.objects.all()
    serializer_class = ItemStockSerializer


# ItemWarehouseStock CRUD Views
class ItemWarehouseStockListCreateView(generics.ListCreateAPIView):
    queryset = ItemWarehouseStock.objects.all()
    serializer_class = ItemWarehouseStockSerializer


class ItemWarehouseStockRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemWarehouseStock.objects.all()
    serializer_class = ItemWarehouseStockSerializer