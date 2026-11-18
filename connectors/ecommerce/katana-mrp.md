---
description: "Katana Cloud Inventory (Katana MRP) — manufacturing resource planning and inventory management."
hidden: true
---

# Katana MRP

<img src="../../.gitbook/assets/connectors/lg/katana-mrp.png" alt="Katana MRP logo">

Katana Cloud Inventory (Katana MRP) — manufacturing resource planning and inventory management. Full coverage of the Katana v1 API: products, materials, variants, recipes/BOM, manufacturing orders, sales orders, purchase orders, customers, suppliers, inventory, stock adjustments/transfers/stocktakes, locations, bins, price lists, tax rates, serial/batch tracking, and webhook subscriptions.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [katanamrp.com](https://katanamrp.com) |
| **Authentication** | Bearer token |
| **Slug** | `katanaMrp` |

## Use it

Add Katana MRP from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.katanaMrp.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Create BOM Rows | `batchCreateBomRows` | Create a Create in Katana MRP. |
| Create Batch | `createBatch` | Create a Batche in Katana MRP. |
| Create Bin Location | `createBinLocation` | Create a Bin Location in Katana MRP. |
| Create Bin Transfer | `createBinTransfer` | Create a Bin Transfer in Katana MRP. |
| Create Bin Transfer Row | `createBinTransferRow` | Create a Bin Transfer Row in Katana MRP. |
| Create Bom Row | `createBomRow` | Create a Bom Row in Katana MRP. |
| Create Custom Field Definition | `createCustomFieldDefinition` | Create a Custom Field Definition in Katana MRP. |
| Create Customer | `createCustomer` | Create a Customer in Katana MRP. |
| Create Customer Address | `createCustomerAddress` | Create a Customer Address in Katana MRP. |
| Create Demand Forecast | `createDemandForecast` | Create a Demand Forecast in Katana MRP. |

<details>

<summary>See 213 more actions</summary>

* **Create Make To Order Manufacturing Order** `createManufacturingOrderMakeToOrder`: Create a Manufacturing Order Make To Order in Katana MRP.
* **Create Manufacturing Order** `createManufacturingOrder`: Create a Manufacturing Order in Katana MRP.
* **Create Manufacturing Order Operation Row** `createManufacturingOrderOperationRow`: Create a Manufacturing Order Operation Row in Katana MRP.
* **Create Manufacturing Order Production** `createManufacturingOrderProduction`: Create a Manufacturing Order Production in Katana MRP.
* **Create Manufacturing Order Recipe Row** `createManufacturingOrderRecipeRow`: Create a Manufacturing Order Recipe Row in Katana MRP.
* **Create Material** `createMaterial`: Create a Material in Katana MRP.
* **Create Outsourced Purchase Order Recipe Row** `createOutsourcedPurchaseOrderRecipeRow`: Create a Outsourced Purchase Order Recipe Row in Katana MRP.
* **Create Po Additional Cost Row** `createPoAdditionalCostRow`: Create a Po Additional Cost Row in Katana MRP.
* **Create Price List** `createPriceList`: Create a Price List in Katana MRP.
* **Create Price List Customer** `createPriceListCustomer`: Create a Price List Customer in Katana MRP.
* **Create Price List Row** `createPriceListRow`: Create a Price List Row in Katana MRP.
* **Create Product** `createProduct`: Create a Product in Katana MRP.
* **Create Product Operation Row** `createProductOperationRow`: Create a Product Operation Row in Katana MRP.
* **Create Purchase Order** `createPurchaseOrder`: Create a Purchase Order in Katana MRP.
* **Create Purchase Order Row** `createPurchaseOrderRow`: Create a Purchase Order Row in Katana MRP.
* **Create Recipe** `createRecipe`: Create a Recipe in Katana MRP.
* **Create Sales Order** `createSalesOrder`: Create a Sales Order in Katana MRP.
* **Create Sales Order Address** `createSalesOrderAddress`: Create a Sales Order Address in Katana MRP.
* **Create Sales Order Fulfillment** `createSalesOrderFulfillment`: Create a Sales Order Fulfillment in Katana MRP.
* **Create Sales Order Row** `createSalesOrderRow`: Create a Sales Order Row in Katana MRP.
* **Create Sales Order Shipping Fee** `createSalesOrderShippingFee`: Create a Sales Order Shipping Fee in Katana MRP.
* **Create Sales Return** `createSalesReturn`: Create a Sales Return in Katana MRP.
* **Create Sales Return Row** `createSalesReturnRow`: Create a Sales Return Row in Katana MRP.
* **Create Serial Number** `createSerialNumber`: Create a Serial Number in Katana MRP.
* **Create Service** `createService`: Create a Service in Katana MRP.
* **Create Stock Adjustment** `createStockAdjustment`: Create a Stock Adjustment in Katana MRP.
* **Create Stock Transfer** `createStockTransfer`: Create a Stock Transfer in Katana MRP.
* **Create Stocktake** `createStocktake`: Create a Stocktake in Katana MRP.
* **Create Stocktake Row** `createStocktakeRow`: Create a Stocktake Row in Katana MRP.
* **Create Supplier** `createSupplier`: Create a Supplier in Katana MRP.
* **Create Supplier Address** `createSupplierAddress`: Create a Supplier Address in Katana MRP.
* **Create Tax Rate** `createTaxRate`: Create a Tax Rate in Katana MRP.
* **Create Variant** `createVariant`: Create a Variant in Katana MRP.
* **Create Webhook** `createWebhook`: Create a Webhook in Katana MRP.
* **Delete Bin Location** `deleteBinLocation`: Delete a Bin Location in Katana MRP.
* **Delete Bin Transfer** `deleteBinTransfer`: Delete a Bin Transfer in Katana MRP.
* **Delete Bin Transfer Row** `deleteBinTransferRow`: Delete a Bin Transfer Row in Katana MRP.
* **Delete Bom Row** `deleteBomRow`: Delete a Bom Row in Katana MRP.
* **Delete Custom Field Definition** `deleteCustomFieldDefinition`: Delete a Custom Field Definition in Katana MRP.
* **Delete Customer** `deleteCustomer`: Delete a Customer in Katana MRP.
* **Delete Customer Address** `deleteCustomerAddress`: Delete a Customer Address in Katana MRP.
* **Delete Demand Forecasts** `deleteDemandForecasts`: Delete a Demand Forecast in Katana MRP.
* **Delete Manufacturing Order** `deleteManufacturingOrder`: Delete a Manufacturing Order in Katana MRP.
* **Delete Manufacturing Order Operation Row** `deleteManufacturingOrderOperationRow`: Delete a Manufacturing Order Operation Row in Katana MRP.
* **Delete Manufacturing Order Production** `deleteManufacturingOrderProduction`: Delete a Manufacturing Order Production in Katana MRP.
* **Delete Manufacturing Order Recipe Row** `deleteManufacturingOrderRecipeRow`: Delete a Manufacturing Order Recipe Row in Katana MRP.
* **Delete Material** `deleteMaterial`: Delete a Material in Katana MRP.
* **Delete Outsourced Purchase Order Recipe Row** `deleteOutsourcedPurchaseOrderRecipeRow`: Delete a Outsourced Purchase Order Recipe Row in Katana MRP.
* **Delete Po Additional Cost Row** `deletePoAdditionalCostRow`: Delete a Po Additional Cost Row in Katana MRP.
* **Delete Price List** `deletePriceList`: Delete a Price List in Katana MRP.
* **Delete Price List Customer** `deletePriceListCustomer`: Delete a Price List Customer in Katana MRP.
* **Delete Price List Row** `deletePriceListRow`: Delete a Price List Row in Katana MRP.
* **Delete Product** `deleteProduct`: Delete a Product in Katana MRP.
* **Delete Product Operation Row** `deleteProductOperationRow`: Delete a Product Operation Row in Katana MRP.
* **Delete Purchase Order** `deletePurchaseOrder`: Delete a Purchase Order in Katana MRP.
* **Delete Purchase Order Row** `deletePurchaseOrderRow`: Delete a Purchase Order Row in Katana MRP.
* **Delete Recipe** `deleteRecipe`: Delete a Recipe in Katana MRP.
* **Delete Recipe Row** `deleteRecipeRow`: Delete a Recipe Row in Katana MRP.
* **Delete Sales Order** `deleteSalesOrder`: Delete a Sales Order in Katana MRP.
* **Delete Sales Order Address** `deleteSalesOrderAddress`: Delete a Sales Order Address in Katana MRP.
* **Delete Sales Order Fulfillment** `deleteSalesOrderFulfillment`: Delete a Sales Order Fulfillment in Katana MRP.
* **Delete Sales Order Row** `deleteSalesOrderRow`: Delete a Sales Order Row in Katana MRP.
* **Delete Sales Order Shipping Fee** `deleteSalesOrderShippingFee`: Delete a Sales Order Shipping Fee in Katana MRP.
* **Delete Sales Return** `deleteSalesReturn`: Delete a Sales Return in Katana MRP.
* **Delete Sales Return Row** `deleteSalesReturnRow`: Delete a Sales Return Row in Katana MRP.
* **Delete Serial Numbers** `deleteSerialNumbers`: Delete a Serial Number in Katana MRP.
* **Delete Service** `deleteService`: Delete a Service in Katana MRP.
* **Delete Stock Adjustment** `deleteStockAdjustment`: Delete a Stock Adjustment in Katana MRP.
* **Delete Stock Transfer** `deleteStockTransfer`: Delete a Stock Transfer in Katana MRP.
* **Delete Stocktake** `deleteStocktake`: Delete a Stocktake in Katana MRP.
* **Delete Stocktake Row** `deleteStocktakeRow`: Delete a Stocktake Row in Katana MRP.
* **Delete Supplier** `deleteSupplier`: Delete a Supplier in Katana MRP.
* **Delete Supplier Address** `deleteSupplierAddress`: Delete a Supplier Address in Katana MRP.
* **Delete Variant** `deleteVariant`: Delete a Variant in Katana MRP.
* **Delete Webhook** `deleteWebhook`: Delete a Webhook in Katana MRP.
* **Export Webhook Logs** `exportWebhookLogs`: Create a Webhook Logs Export in Katana MRP.
* **Get Bin Transfer** `getBinTransfer`: Retrieve a Bin Transfer in Katana MRP.
* **Get Bin Transfer Row** `getBinTransferRow`: Retrieve a Bin Transfer Row in Katana MRP.
* **Get Current User Info** `getUserInfo`: List User Info in Katana MRP.
* **Get Custom Field Definition** `getCustomFieldDefinition`: Retrieve a Custom Field Definition in Katana MRP.
* **Get Factory Settings** `getFactory`: List Factory in Katana MRP.
* **Get Location** `getLocation`: Retrieve a Location in Katana MRP.
* **Get Manufacturing Order** `getManufacturingOrder`: Retrieve a Manufacturing Order in Katana MRP.
* **Get Manufacturing Order Operation Row** `getManufacturingOrderOperationRow`: Retrieve a Manufacturing Order Operation Row in Katana MRP.
* **Get Manufacturing Order Production** `getManufacturingOrderProduction`: Retrieve a Manufacturing Order Production in Katana MRP.
* **Get Manufacturing Order Recipe Row** `getManufacturingOrderRecipeRow`: Retrieve a Manufacturing Order Recipe Row in Katana MRP.
* **Get Material** `getMaterial`: Retrieve a Material in Katana MRP.
* **Get Outsourced Purchase Order Recipe Row** `getOutsourcedPurchaseOrderRecipeRow`: Retrieve a Outsourced Purchase Order Recipe Row in Katana MRP.
* **Get Po Additional Cost Row** `getPoAdditionalCostRow`: Retrieve a Po Additional Cost Row in Katana MRP.
* **Get Price List** `getPriceList`: Retrieve a Price List in Katana MRP.
* **Get Price List Customer** `getPriceListCustomer`: Retrieve a Price List Customer in Katana MRP.
* **Get Price List Row** `getPriceListRow`: Retrieve a Price List Row in Katana MRP.
* **Get Product** `getProduct`: Retrieve a Product in Katana MRP.
* **Get Purchase Order** `getPurchaseOrder`: Retrieve a Purchase Order in Katana MRP.
* **Get Purchase Order Row** `getPurchaseOrderRow`: Retrieve a Purchase Order Row in Katana MRP.
* **Get Sales Order** `getSalesOrder`: Retrieve a Sales Order in Katana MRP.
* **Get Sales Order Fulfillment** `getSalesOrderFulfillment`: Retrieve a Sales Order Fulfillment in Katana MRP.
* **Get Sales Order Returnable Items** `getSalesOrderReturnableItems`: Retrieve a Returnable Item in Katana MRP.
* **Get Sales Order Row** `getSalesOrderRow`: Retrieve a Sales Order Row in Katana MRP.
* **Get Sales Order Shipping Fee** `getSalesOrderShippingFee`: Retrieve a Sales Order Shipping Fee in Katana MRP.
* **Get Sales Return** `getSalesReturn`: Retrieve a Sales Return in Katana MRP.
* **Get Sales Return Row** `getSalesReturnRow`: Retrieve a Sales Return Row in Katana MRP.
* **Get Sales Return Row Unassigned Batch Transactions** `getSalesReturnRowUnassignedBatchTransactions`: Retrieve a Unassigned Batch Transaction in Katana MRP.
* **Get Service** `getService`: Retrieve a Service in Katana MRP.
* **Get Variant** `getVariant`: Retrieve a Variant in Katana MRP.
* **Get Webhook** `getWebhook`: Retrieve a Webhook in Katana MRP.
* **List Additional Costs** `listAdditionalCosts`: List Additional Costs in Katana MRP.
* **List Batch Stocks** `listBatchStocks`: List Batch Stocks in Katana MRP.
* **List Bin Inventory** `listBinInventory`: List Bin Inventory in Katana MRP.
* **List Bin Locations** `listBinLocations`: List Bin Locations in Katana MRP.
* **List Bin Transfer Rows** `listBinTransferRows`: List Bin Transfer Rows in Katana MRP.
* **List Bin Transfers** `listBinTransfers`: List Bin Transfers in Katana MRP.
* **List Bom Rows** `listBomRows`: List Bom Rows in Katana MRP.
* **List Custom Field Definitions** `listCustomFieldDefinitions`: List Custom Field Definitions in Katana MRP.
* **List Custom Fields Collections** `listCustomFieldsCollections`: List Custom Fields Collections in Katana MRP.
* **List Customer Addresses** `listCustomerAddresses`: List Customer Addresses in Katana MRP.
* **List Customers** `listCustomers`: List Customers in Katana MRP.
* **List Demand Forecasts** `listDemandForecasts`: List Demand Forecasts in Katana MRP.
* **List Inventory** `listInventory`: List Inventory in Katana MRP.
* **List Inventory Movements** `listInventoryMovements`: List Inventory Movements in Katana MRP.
* **List Locations** `listLocations`: List Locations in Katana MRP.
* **List Manufacturing Order Operation Rows** `listManufacturingOrderOperationRows`: List Manufacturing Order Operation Rows in Katana MRP.
* **List Manufacturing Order Productions** `listManufacturingOrderProductions`: List Manufacturing Order Productions in Katana MRP.
* **List Manufacturing Order Recipe Rows** `listManufacturingOrderRecipeRows`: List Manufacturing Order Recipe Rows in Katana MRP.
* **List Manufacturing Orders** `listManufacturingOrders`: List Manufacturing Orders in Katana MRP.
* **List Materials** `listMaterials`: List Materials in Katana MRP.
* **List Negative Stock** `listNegativeStock`: List Negative Stock in Katana MRP.
* **List Operators** `listOperators`: List Operators in Katana MRP.
* **List Outsourced Purchase Order Recipe Rows** `listOutsourcedPurchaseOrderRecipeRows`: List Outsourced Purchase Order Recipe Rows in Katana MRP.
* **List Po Additional Cost Rows** `listPoAdditionalCostRows`: List Po Additional Cost Rows in Katana MRP.
* **List Price List Customers** `listPriceListCustomers`: List Price List Customers in Katana MRP.
* **List Price List Rows** `listPriceListRows`: List Price List Rows in Katana MRP.
* **List Price Lists** `listPriceLists`: List Price Lists in Katana MRP.
* **List Product Operation Rows** `listProductOperationRows`: List Product Operation Rows in Katana MRP.
* **List Products** `listProducts`: List Products in Katana MRP.
* **List Purchase Order Accounting Metadata** `listPurchaseOrderAccountingMetadata`: List Purchase Order Accounting Metadata in Katana MRP.
* **List Purchase Order Rows** `listPurchaseOrderRows`: List Purchase Order Rows in Katana MRP.
* **List Purchase Orders** `listPurchaseOrders`: List Purchase Orders in Katana MRP.
* **List Recipes** `listRecipes`: List Recipes in Katana MRP.
* **List Sales Order Accounting Metadata** `listSalesOrderAccountingMetadata`: List Sales Order Accounting Metadata in Katana MRP.
* **List Sales Order Addresses** `listSalesOrderAddresses`: List Sales Order Addresses in Katana MRP.
* **List Sales Order Fulfillments** `listSalesOrderFulfillments`: List Sales Order Fulfillments in Katana MRP.
* **List Sales Order Rows** `listSalesOrderRows`: List Sales Order Rows in Katana MRP.
* **List Sales Order Shipping Fee** `listSalesOrderShippingFee`: List Sales Order Shipping Fee in Katana MRP.
* **List Sales Orders** `listSalesOrders`: List Sales Orders in Katana MRP.
* **List Sales Return Reasons** `listSalesReturnReasons`: List Return Reasons in Katana MRP.
* **List Sales Return Rows** `listSalesReturnRows`: List Sales Return Rows in Katana MRP.
* **List Sales Returns** `listSalesReturns`: List Sales Returns in Katana MRP.
* **List Serial Numbers** `listSerialNumbers`: List Serial Numbers in Katana MRP.
* **List Serial Numbers Stock** `listSerialNumbersStock`: List Serial Numbers Stock in Katana MRP.
* **List Serial Numbers Stock (Nested)** `listSerialNumbersStockNested`: List Serial Numbers Stock in Katana MRP.
* **List Services** `listServices`: List Services in Katana MRP.
* **List Stock Adjustments** `listStockAdjustments`: List Stock Adjustments in Katana MRP.
* **List Stock Transfers** `listStockTransfers`: List Stock Transfers in Katana MRP.
* **List Stocktake Rows** `listStocktakeRows`: List Stocktake Rows in Katana MRP.
* **List Stocktakes** `listStocktakes`: List Stocktakes in Katana MRP.
* **List Supplier Addresses** `listSupplierAddresses`: List Supplier Addresses in Katana MRP.
* **List Suppliers** `listSuppliers`: List Suppliers in Katana MRP.
* **List Tax Rates** `listTaxRates`: List Tax Rates in Katana MRP.
* **List Users** `listUsers`: List Users in Katana MRP.
* **List Variants** `listVariants`: List Variants in Katana MRP.
* **List Webhooks** `listWebhooks`: List Webhooks in Katana MRP.
* **Receive Purchase Order** `receivePurchaseOrder`: Create a Purchase Order Receive in Katana MRP.
* **Rerank Product Operation Rows** `rerankProductOperation`: Create a Product Operation Rerank in Katana MRP.
* **Search Sales Order Rows** `searchSalesOrderRows`: Create a Search in Katana MRP.
* **Search Sales Orders** `searchSalesOrders`: Create a Search in Katana MRP.
* **Set Inventory Reorder Point** `setInventoryReorderPoint`: Create a Inventory Reorder Point in Katana MRP.
* **Set Inventory Safety Stock Level** `setInventorySafetyStockLevel`: Create a Inventory Safety Stock Level in Katana MRP.
* **Set Variant Bin Locations** `setVariantBinLocations`: Create a Variant Bin Location in Katana MRP.
* **Unlink Manufacturing Order** `unlinkManufacturingOrder`: Create a Manufacturing Order Unlink in Katana MRP.
* **Unlink Variant Bin Locations** `unlinkVariantBinLocations`: Create a Unlink Variant Bin Location in Katana MRP.
* **Update Batch Stock** `updateBatchStock`: Update a Batch Stock in Katana MRP.
* **Update Bin Location** `updateBinLocation`: Update a Bin Location in Katana MRP.
* **Update Bin Transfer** `updateBinTransfer`: Update a Bin Transfer in Katana MRP.
* **Update Bin Transfer Row** `updateBinTransferRow`: Update a Bin Transfer Row in Katana MRP.
* **Update Bin Transfer Status** `updateBinTransferStatus`: Update a Statu in Katana MRP.
* **Update Bom Row** `updateBomRow`: Update a Bom Row in Katana MRP.
* **Update Custom Field Definition** `updateCustomFieldDefinition`: Update a Custom Field Definition in Katana MRP.
* **Update Customer** `updateCustomer`: Update a Customer in Katana MRP.
* **Update Customer Address** `updateCustomerAddress`: Update a Customer Address in Katana MRP.
* **Update Manufacturing Order** `updateManufacturingOrder`: Update a Manufacturing Order in Katana MRP.
* **Update Manufacturing Order Operation Row** `updateManufacturingOrderOperationRow`: Update a Manufacturing Order Operation Row in Katana MRP.
* **Update Manufacturing Order Production** `updateManufacturingOrderProduction`: Update a Manufacturing Order Production in Katana MRP.
* **Update Manufacturing Order Production Ingredient** `updateManufacturingOrderProductionIngredient`: Update a Manufacturing Order Production Ingredient in Katana MRP.
* **Update Manufacturing Order Recipe Row** `updateManufacturingOrderRecipeRow`: Update a Manufacturing Order Recipe Row in Katana MRP.
* **Update Material** `updateMaterial`: Update a Material in Katana MRP.
* **Update Outsourced Purchase Order Recipe Row** `updateOutsourcedPurchaseOrderRecipeRow`: Update a Outsourced Purchase Order Recipe Row in Katana MRP.
* **Update Po Additional Cost Row** `updatePoAdditionalCostRow`: Update a Po Additional Cost Row in Katana MRP.
* **Update Price List** `updatePriceList`: Update a Price List in Katana MRP.
* **Update Price List Customer** `updatePriceListCustomer`: Update a Price List Customer in Katana MRP.
* **Update Price List Row** `updatePriceListRow`: Update a Price List Row in Katana MRP.
* **Update Product** `updateProduct`: Update a Product in Katana MRP.
* **Update Product Operation Row** `updateProductOperationRow`: Update a Product Operation Row in Katana MRP.
* **Update Purchase Order** `updatePurchaseOrder`: Update a Purchase Order in Katana MRP.
* **Update Purchase Order Row** `updatePurchaseOrderRow`: Update a Purchase Order Row in Katana MRP.
* **Update Recipe Row** `updateRecipeRow`: Update a Recipe Row in Katana MRP.
* **Update Sales Order** `updateSalesOrder`: Update a Sales Order in Katana MRP.
* **Update Sales Order Address** `updateSalesOrderAddress`: Update a Sales Order Address in Katana MRP.
* **Update Sales Order Fulfillment** `updateSalesOrderFulfillment`: Update a Sales Order Fulfillment in Katana MRP.
* **Update Sales Order Row** `updateSalesOrderRow`: Update a Sales Order Row in Katana MRP.
* **Update Sales Order Shipping Fee** `updateSalesOrderShippingFee`: Update a Sales Order Shipping Fee in Katana MRP.
* **Update Sales Return** `updateSalesReturn`: Update a Sales Return in Katana MRP.
* **Update Sales Return Row** `updateSalesReturnRow`: Update a Sales Return Row in Katana MRP.
* **Update Service** `updateService`: Update a Service in Katana MRP.
* **Update Stock Adjustment** `updateStockAdjustment`: Update a Stock Adjustment in Katana MRP.
* **Update Stock Transfer** `updateStockTransfer`: Update a Stock Transfer in Katana MRP.
* **Update Stock Transfer Status** `updateStockTransferStatus`: Update a Statu in Katana MRP.
* **Update Stocktake** `updateStocktake`: Update a Stocktake in Katana MRP.
* **Update Stocktake Row** `updateStocktakeRow`: Update a Stocktake Row in Katana MRP.
* **Update Supplier** `updateSupplier`: Update a Supplier in Katana MRP.
* **Update Supplier Address** `updateSupplierAddress`: Update a Supplier Address in Katana MRP.
* **Update Variant** `updateVariant`: Update a Variant in Katana MRP.
* **Update Webhook** `updateWebhook`: Update a Webhook in Katana MRP.

</details>
