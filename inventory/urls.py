from django.urls import path
from .views import (
    ManufacturerListCreateView, ManufacturerRetrieveUpdateDeleteView,
    WarehouseListCreateView, WarehouseRetrieveUpdateDeleteView,
    WarehouseLocationListCreateView, WarehouseLocationRetrieveUpdateDeleteView,
    ItemListCreateView, ItemRetrieveUpdateDeleteView,
    ItemStockListCreateView, ItemStockRetrieveUpdateDeleteView,
    ItemWarehouseStockListCreateView, ItemWarehouseStockRetrieveUpdateDeleteView
)

urlpatterns = [
    # Manufacturer URLs
    path('manufacturers/', ManufacturerListCreateView.as_view(), name='manufacturer-list-create'),
    path('manufacturers/<int:pk>/', ManufacturerRetrieveUpdateDeleteView.as_view(), name='manufacturer-retrieve-update-delete'),
    
    # Warehouse URLs
    path('warehouses/', WarehouseListCreateView.as_view(), name='warehouse-list-create'),
    path('warehouses/<int:pk>/', WarehouseRetrieveUpdateDeleteView.as_view(), name='warehouse-retrieve-update-delete'),
    
    # Warehouse Location URLs
    path('warehouse-locations/', WarehouseLocationListCreateView.as_view(), name='warehouse-location-list-create'),
    path('warehouse-locations/<int:pk>/', WarehouseLocationRetrieveUpdateDeleteView.as_view(), name='warehouse-location-retrieve-update-delete'),

    # Item URLs
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDeleteView.as_view(), name='item-retrieve-update-delete'),

    # ItemStock URLs
    path('item-stocks/', ItemStockListCreateView.as_view(), name='item-stock-list-create'),
    path('item-stocks/<int:pk>/', ItemStockRetrieveUpdateDeleteView.as_view(), name='item-stock-retrieve-update-delete'),

    # ItemWarehouseStock URLs
    path('item-warehouse-stocks/', ItemWarehouseStockListCreateView.as_view(), name='item-warehouse-stock-list-create'),
    path('item-warehouse-stocks/<int:pk>/', ItemWarehouseStockRetrieveUpdateDeleteView.as_view(), name='item-warehouse-stock-retrieve-update-delete'),
]
