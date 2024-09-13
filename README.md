# Inventory_management
API Endpoints
The Inventory Management API provides the following endpoints using Django REST Framework's generic views:

1. Manufacturers
* GET /api/manufacturers/: Retrieve a list of all manufacturers.
* POST /api/manufacturers/: Create a new manufacturer.
* GET /api/manufacturers/<id>/: Retrieve details of a specific manufacturer by ID.
* PUT /api/manufacturers/<id>/: Update details of a specific manufacturer.
* DELETE /api/manufacturers/<id>/: Soft delete a manufacturer.
2. Warehouses
* GET /api/warehouses/: Retrieve a list of all warehouses.
* POST /api/warehouses/: Create a new warehouse.
* GET /api/warehouses/<id>/: Retrieve details of a specific warehouse by ID.
* PUT /api/warehouses/<id>/: Update details of a specific warehouse.
* DELETE /api/warehouses/<id>/: Soft delete a warehouse.
3. Warehouse Locations
* GET /api/warehouse-locations/: Retrieve a list of all warehouse locations.
* POST /api/warehouse-locations/: Create a new warehouse location.
* GET /api/warehouse-locations/<id>/: Retrieve details of a specific warehouse location by ID.
* PUT /api/warehouse-locations/<id>/: Update details of a specific warehouse location.
* DELETE /api/warehouse-locations/<id>/: Delete a warehouse location.
4. Items
* GET /api/items/: Retrieve a list of all items, including their manufacturer details.
* POST /api/items/: Create a new item. Automatically creates an entry in the ItemStock model with initial stock levels.
* GET /api/items/<id>/: Retrieve details of a specific item by ID.
* PUT /api/items/<id>/: Update details of a specific item.
* DELETE /api/items/<id>/: Soft delete an item.
5. Item Stock
* GET /api/item-stocks/: Retrieve a list of all item stocks.
* POST /api/item-stocks/: Create a new item stock record.
* GET /api/item-stocks/<id>/: Retrieve details of a specific item stock by ID.
* PUT /api/item-stocks/<id>/: Update details of a specific item stock.
* DELETE /api/item-stocks/<id>/: Delete an item stock.
6. Item Warehouse Stock
* GET /api/item-warehouse-stocks/: Retrieve a list of all item warehouse stocks.
* POST /api/item-warehouse-stocks/: Create a new item warehouse stock record. Updates the total count of quantity and reserved_quantity in the ItemStock model.
* GET /api/item-warehouse-stocks/<id>/: Retrieve details of a specific item warehouse stock by ID.
* PUT /api/item-warehouse-stocks/<id>/: Update details of a specific item warehouse stock.
* DELETE /api/item-warehouse-stocks/<id>/: Delete an item warehouse stock.

Stock Management
The stock management functionality ensures that:

Every time an item is added, updated, or deleted, the corresponding stock levels (stock_in_hand and reserved_quantity) in the ItemStock model are adjusted accordingly.
The ItemWarehouseStock model helps in managing the stock across different warehouses and their locations. It also updates the total count of stock in the ItemStock model whenever changes occur.

Celery Task for Low Stock Notification
The project uses Celery for handling background tasks, such as monitoring stock levels and sending email alerts. A periodic task is set up to:

Check the stock levels in the ItemStock model at regular intervals.
Trigger an email notification to the relevant stakeholders when the stock_in_hand for any item drops below a predefined minimum threshold (e.g., 5 units).
