---
description: "Inventory Planner by Sage — smart forecasting and replenishment recommendations."
hidden: true
---

# Inventory Planner

<img src="../../.gitbook/assets/connectors/lg/inventory-planner.png" alt="Inventory Planner logo">

Inventory Planner by Sage — smart forecasting and replenishment recommendations. Provides Stock Orders API (purchase orders, transfers, assembly orders) and Reports API (variants, metrics) for syncing data with ERPs, 3PLs, and custom systems.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [app.inventory-planner.com](https://app.inventory-planner.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `inventoryPlanner` |

## Use it

Add Inventory Planner from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.inventoryPlanner.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Item to Purchase Order | `addPurchaseOrderItem` | Add (or upsert) a line item to an existing purchase order by variant id. Note: Inventory Planner's POST /items endpoint returns a server error, so this merges the line via PATCH on the purchase order. Existing line items are preserved; a line with the same variant id is updated. |
| Cancel Assembly Order | `cancelAssemblyOrder` | Cancel an assembly order by setting its status to CANCELLED. |
| Cancel Transfer Order | `cancelTransferOrder` | Cancel a transfer order by setting its status to CANCELLED. |
| Create Assembly Order | `createAssemblyOrder` | Create a new assembly order (type=assembly) for building finished goods from components. |
| Create Purchase Order | `createPurchaseOrder` | Create a new purchase order, optionally seeded with replenishment quantities via variants_filter. Use type='transfer' or type='assembly' to create those order types instead. |
| Create Transfer Order | `createTransferOrder` | Create a new transfer order to move inventory between warehouses. Sets type to 'transfer' automatically. Requires source warehouse and destination warehouse. |
| Delete Assembly Order | `deleteAssemblyOrder` | Permanently delete an assembly order by ID. |
| Delete Purchase Order | `deletePurchaseOrder` | Permanently delete a purchase order by ID. Use with caution — this is irreversible. |
| Delete Purchase Order Item | `deletePurchaseOrderItem` | Remove a line item from a purchase order by zeroing its ordered quantity. Inventory Planner's DELETE on a line item returns 'Not allowed', so this sets the line's replenishment to 0 via PATCH. |
| Delete Transfer Order | `deleteTransferOrder` | Permanently delete a transfer order by ID. |
| Delete Variant | `deleteVariant` | Delete a variant from Inventory Planner by ID. |
| Delete Variant Vendor | `deleteVariantVendor` | Remove a vendor assignment from a variant. |
| Get Assembly Order | `getAssemblyOrder` | Retrieve a single assembly order by its ID. |
| Get Category | `getCategory` | Retrieve a single product category (product type) by its id. Returns the object under the 'product_type' key. |
| Get Purchase Order | `getPurchaseOrder` | Retrieve a single purchase order by its ID. |
| Get Purchase Order Stock Update | `getPurchaseOrderStockUpdate` | Retrieve computed stock update deltas for a purchase order (based on received quantities and previous stock updates). |
| Get Transfer Order | `getTransferOrder` | Retrieve a single transfer order by its ID. |
| Get Variant | `getVariant` | Retrieve a single variant by its ID. |
| Get Variant Vendor | `getVariantVendor` | Get vendor data for a specific variant-vendor pairing. Returns cost price, landing cost, vendor reference, packaging, and ordering UOM. |
| Get Vendor | `getVendor` | Retrieve a single vendor/supplier by its id (vendor name). |
| Get Warehouse | `getWarehouse` | Retrieve a single warehouse/location by its id (the warehouse 'name'). |
| List Assembly Orders | `listAssemblyOrders` | List assembly orders (purchase orders with type=assembly). Supports pagination and status filtering. |
| List Categories | `listCategories` | List product categories (product types). The /categories endpoint returns objects under the 'product_types' key. |
| List Purchase Order Connections | `listPurchaseOrderConnections` | List connection sync statuses for a purchase order. |
| List Purchase Order Items | `listPurchaseOrderItems` | List all line items for a purchase order. |
| List Purchase Orders | `listPurchaseOrders` | Returns a paginated list of purchase orders (also includes transfers and assembly orders). Filter by status, vendor, warehouse, etc. |
| List Transfer Orders | `getTransferOrders` | List transfer orders (purchase orders with type=transfer). Supports pagination and filtering by status. |
| List Variant Vendors | `listVariantVendors` | List all vendor assignments for a variant (cost price, vendor reference, MOQ, etc.) |
| List Variants | `listVariants` | List product variants with their replenishment data. Supports filtering, sorting, and field selection. Use fields parameter to specify which of 200+ metrics to return. |
| List Vendors | `listVendors` | List all vendors/suppliers. Each vendor has id, name, title. Use the vendor name when creating a purchase order. |
| List Warehouses | `listWarehouses` | List all warehouses/locations. Each warehouse has id, name, title and whether it supports assembly orders. Use the warehouse name (id) when creating purchase/transfer/assembly orders. |
| Push Stock Update | `pushStockUpdate` | Push stock update deltas to a connection for a purchase order. |
| Save Purchase Order to Connection | `savePurchaseOrderConnection` | Push a purchase order to an external connection (e.g. Brightpearl, QuickBooks). Sets save_po = true. |
| Update Assembly Order | `updateAssemblyOrder` | Partially update an assembly order (e.g. change expected_date, reference, status). |
| Update Purchase Order | `updatePurchaseOrder` | Partially update a purchase order. Only include the fields you want to change. |
| Update Purchase Order Item | `updatePurchaseOrderItem` | Update a single line item in a purchase order (e.g. update received quantity). |
| Update Purchase Order Items | `updatePurchaseOrderItems` | Update received quantities for multiple line items in a purchase order in one request. |
| Update Transfer Order | `updateTransferOrder` | Partially update a transfer order's reference, status, or expected_date. Note: warehouse/source_warehouse are not editable here because Inventory Planner applies empty values and would blank them; set those at creation time. |
| Update Variant | `updateVariant` | Partially update a variant (e.g. set lead_time, review_period). |
| Upsert Variant Vendor | `upsertVariantVendor` | Create or update vendor data for a variant (cost price, vendor reference, MOQ, etc.) |
