---
description: "Cin7 Omni (api.cin7.com) — cloud inventory, sales, purchasing, and retail management."
hidden: true
---

# Cin7 Omni

<img src="../../.gitbook/assets/connectors/lg/cin7omni.png" alt="Cin7 Omni logo">

Cin7 Omni (api.cin7.com) — cloud inventory, sales, purchasing, and retail management. Wraps the Cin7 Omni REST API v1 (https://api.cin7.com/api/v1). List endpoints use the fields/where/order/page/rows query pattern; POST/PUT bodies are JSON arrays of objects (bulk create/update). HTTP Basic auth with API Username + connection Key. Distinct from Cin7 Core.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [cin7.com](https://cin7.com) |
| **Authentication** | Basic auth |
| **Slug** | `cin7omni` |

## Use it

Add Cin7 Omni from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cin7omni.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Adjustments | `createAdjustments` | Create Adjustments (POST /api/v1/Adjustments). Creates one or more records in one call; send adjustments as a list. Returns one result per record with success, id and errors. |
| Create Branch Transfers | `createBranchTransfers` | Create Branch Transfers (POST /api/v1/BranchTransfers). Creates one or more stock transfers between branches in one call; send branchTransfers as a list. Returns one result per record with success, id and errors. |
| Create Branches | `createBranches` | Create Branches (POST /api/v1/Branches). Creates one or more branches in one call; send branches as a list. Returns one result per record with success, id and errors. |
| Create Contacts | `createContacts` | Create Contacts (POST /api/v1/Contacts). Creates one or more contacts (customers or suppliers) in one call; send contacts as a list. Returns one result per record with success, id and errors. |
| Create Credit Notes | `createCreditNotes` | Create Credit Notes (POST /api/v1/CreditNotes). Creates one or more credit notes in one call; send creditNotes as a list. Returns one result per record with success, id and errors. |
| Create Payments | `createPayments` | Create Payments (POST /api/v1/Payments). Creates one or more records in one call; send payments as a list. Returns one result per record with success, id and errors. |
| Create Product Categories | `createProductCategories` | Create Product Categories (POST /api/v1/ProductCategories). Creates one or more records in one call; send productCategories as a list. Returns one result per record with success, id and errors. |
| Create Product Options | `createProductOptions` | Create Product Options (POST /api/v1/ProductOptions). Creates one or more product options (variants) in one call; send productOptions as a list. Returns one result per record with success, id and errors. |
| Create Production Jobs | `createProductionJobs` | Create Production Jobs (POST /api/v1/ProductionJobs). Creates one or more production jobs in one call; send productionJobs as a list. Returns one result per record with success, id and errors. |
| Create Products | `createProducts` | Create Products (POST /api/v1/Products). Creates one or more products (with their options) in one call; send products as a list. Returns one result per record with success, id and errors. |
| Create Purchase Orders | `createPurchaseOrders` | Create Purchase Orders (POST /api/v1/PurchaseOrders). Creates one or more purchase orders in one call; send purchaseOrders as a list. Optional loadboms=true loads bill-of-materials lines. Returns one result per record with success, id and errors. |
| Create Quotes | `createQuotes` | Create Quotes (POST /api/v1/Quotes). Creates one or more quotes in one call; send quotes as a list. Optional loadboms=true loads bill-of-materials lines. Returns one result per record with success, id and errors. |
| Create Sales Orders | `createSalesOrders` | Create Sales Orders (POST /api/v1/SalesOrders). Creates one or more sales orders in one call; send salesOrders as a list. Optional loadboms=true loads bill-of-materials lines. Returns one result per record with success, id and errors. |
| Delete Contact | `deleteContact` | Delete a contact by its numeric Id. |
| Delete Payment | `deletePayment` | Delete a payment by its numeric Id. |
| Get Adjustment | `getAdjustment` | Get a single stock adjustment by its numeric Id. |
| Get BOM Master | `getBomMaster` | Get a single BOM master by its numeric Id (v1). |
| Get BOM Master V2 | `getBomMasterV2` | Get a single BOM master by its numeric Id (v2). |
| Get Branch | `getBranch` | Get a single branch by its numeric Id. |
| Get Branch Transfer | `getBranchTransfer` | Get a single branch transfer by its numeric Id. |
| Get Carton | `getCarton` | Get a single carton by its numeric Id. |
| Get Contact | `getContact` | Get a single contact by its numeric Id. |
| Get Credit Note | `getCreditNote` | Get a single credit note by its numeric Id. |
| Get Payment | `getPayment` | Get a single payment by its numeric Id. |
| Get Product | `getProduct` | Get a single product by its numeric Id. |
| Get Product Category | `getProductCategory` | Get a single product category by its numeric Id. |
| Get Product Option | `getProductOption` | Get a single product option by its numeric Id. |
| Get Production Job | `getProductionJob` | Get a single production job by its numeric Id. |
| Get Purchase Order | `getPurchaseOrder` | Get a single purchase order by its numeric Id. |
| Get Quote | `getQuote` | Get a single quote by its numeric Id. |
| Get Sales Order | `getSalesOrder` | Get a single sales order by its numeric Id. |
| Get Sales Order With Cartons | `getSalesOrderWithCartons` | Get a single sales order with carton/dispatch details by Id. |
| Get Serial Number | `getSerialNumber` | Get a single serial number record by its numeric Id. |
| Get Size Range | `getSizeRange` | Get a single size range by its numeric Id. |
| Get Stock By Barcode | `getStockByBarcode` | Get stock levels for a specific barcode. |
| Get User | `getUser` | Get a single user by its numeric Id. |
| Get Voucher By Code | `getVoucherByCode` | Get a gift voucher by its code. |
| List Adjustments | `listAdjustments` | Get a list of stock adjustments. Supports fields/where/order/page/rows. |
| List BOM Masters | `listBomMasters` | Get a list of Bill of Materials (BOM) masters (v1). Supports fields/where/order/page/rows. |
| List BOM Masters V2 | `listBomMastersV2` | Get a list of Bill of Materials (BOM) masters (v2). Supports fields/where/order/page/rows. |
| List Branch Transfers | `listBranchTransfers` | Get a list of branch transfers. Supports fields/where/order/page/rows. |
| List Branches | `listBranches` | Get a list of branches (locations). Supports fields/where/order/page/rows. |
| List Contacts | `listContacts` | Get a list of contacts (customers/suppliers). Supports fields/where/order/page/rows. |
| List Credit Notes | `listCreditNotes` | Get a list of credit notes. Supports fields/where/order/page/rows. |
| List Payment Fees | `listPaymentFees` | Get a list of payment fees. Supports fields/where/order/page/rows. |
| List Payment Payouts | `listPaymentPayouts` | Get a list of payment payouts. Supports fields/where/order/page/rows. |
| List Payments | `listPayments` | Get a list of payments. Supports fields/where/order/page/rows. |
| List Product Categories | `listProductCategories` | Get a list of product categories. Supports fields/where/order/page/rows. |
| List Product Options | `listProductOptions` | Get a list of product options (variants/SKUs). Supports fields/where/order/page/rows. |
| List Production Jobs | `listProductionJobs` | Get a list of production jobs. Supports fields/where/order/page/rows. |
| List Products | `listProducts` | Get a list of products. Supports the Cin7 query pattern: fields (comma-separated columns), where (SQL-like filter e.g. Status='Active'), order (sort), page (1-based), rows (page size, max 250). |
| List Purchase Orders | `listPurchaseOrders` | Get a list of purchase orders. Supports fields/where/order/page/rows. |
| List Quotes | `listQuotes` | Get a list of quotes. Supports fields/where/order/page/rows. |
| List Sales Orders | `listSalesOrders` | List Sales Orders (GET /api/v1/SalesOrders). Returns sales orders as a list, filtered with a where clause, e.g. InvoiceNumber=10234 to find one by invoice number, or Stage='New'. Use fields to pick columns (e.g. id,stage,internalComments,customFields,invoiceNumber), order to sort, page and rows (default 50, max 250) to page through results. |
| List Sales Orders With Cartons | `listSalesOrdersWithCartons` | Get a list of sales orders including their carton/dispatch details. Supports fields/where/order/page/rows. |
| List Serial Numbers | `listSerialNumbers` | Get a list of serial numbers. Supports fields/where/order/page/rows. |
| List Size Ranges | `listSizeRanges` | Get all size ranges. |
| List Stock | `listStock` | Get current stock levels per product option / branch. Supports fields/where/order/page/rows. |
| List Users | `listUsers` | Get a list of Cin7 Omni users. |
| List Vouchers | `listVouchers` | Get a list of gift vouchers. Supports fields/where/order/page/rows. |
| Update Adjustments | `updateAdjustments` | Update Adjustments (PUT /api/v1/Adjustments). Updates one or more records in one call; send adjustments as a list. Each item needs id and only the fields to change. Returns one result per record with success, id and errors. |
| Update Branch Transfers | `updateBranchTransfers` | Update Branch Transfers (PUT /api/v1/BranchTransfers). Updates one or more branch transfers in one call; send branchTransfers as a list. Each item needs id and only the fields to change. Returns one result per record with success, id and errors. |
| Update Branches | `updateBranches` | Update Branches (PUT /api/v1/Branches). Updates one or more branches in one call; send branches as a list. Each item needs id and only the fields to change. Returns one result per record with success, id and errors. |
| Update Carton | `updateCarton` | Update a single carton by Id. Body is a JSON object with the carton fields (e.g. TrackingNumber, Weight, LineItems). Pass it as a JSON-encoded string in 'payload'. |
| Update Contacts | `updateContacts` | Update Contacts (PUT /api/v1/Contacts). Updates one or more contacts in one call; send contacts as a list. Each item needs id and only the fields to change. Returns one result per record with success, id and errors. |
| Update Credit Notes | `updateCreditNotes` | Update Credit Notes (PUT /api/v1/CreditNotes). Updates one or more credit notes in one call; send creditNotes as a list. Each item needs id and only the fields to change. Returns one result per record with success, id and errors. |
| Update Payments | `updatePayments` | Update Payments (PUT /api/v1/Payments). Updates one or more records in one call; send payments as a list. Each item needs id and only the fields to change. Returns one result per record with success, id and errors. |
| Update Product Categories | `updateProductCategories` | Update Product Categories (PUT /api/v1/ProductCategories). Updates one or more records in one call; send productCategories as a list. Each item needs id; leave other fields out (or null) to keep them. Returns one result per record with success, id and errors. |
| Update Product Options | `updateProductOptions` | Update Product Options (PUT /api/v1/ProductOptions). Updates one or more product options in one call; send productOptions as a list. Each item needs id and only the fields to change. Returns one result per record with success, id and errors. |
| Update Production Jobs | `updateProductionJobs` | Update Production Jobs (PUT /api/v1/ProductionJobs). Updates one or more production jobs in one call; send productionJobs as a list. Each item needs id and only the fields to change. Returns one result per record with success, id and errors. |
| Update Products | `updateProducts` | Update Products (PUT /api/v1/Products). Updates one or more products in one call; send products as a list. Each item needs id and only the fields to change. Returns one result per record with success, id and errors. |
| Update Purchase Orders | `updatePurchaseOrders` | Update Purchase Orders (PUT /api/v1/PurchaseOrders). Updates one or more purchase orders in one call; send purchaseOrders as a list. Each item needs id and only the fields to change. Optional loadboms=true loads bill-of-materials lines. Returns one result per record with success, id and errors. |
| Update Quotes | `updateQuotes` | Update Quotes (PUT /api/v1/Quotes). Updates one or more quotes in one call; send quotes as a list. Each item needs id and only the fields to change. Optional loadboms=true loads bill-of-materials lines. Returns one result per record with success, id and errors. |
| Update Sales Orders | `updateSalesOrders` | Update Sales Orders (PUT /api/v1/SalesOrders). Updates one or more sales orders in one call. Send salesOrders as a list; each item needs id and only the fields to change, e.g. {"id": 123, "stage": "Dispatched", "internalComments": "Delivered 14 Nov", "customerOrderNo": "PO-55", "customFields": {"orders_1000": "OK"}}. Returns one result per order with success, id and errors. Setting isVoid true voids an order and cannot be undone. |
| Upload Product Image | `uploadProductImage` | Upload an image for a product at a given priority slot. POST /ProductImages with productId and imagePriority (1-based image slot). Body is the image payload as documented by Cin7 (base64 or URL object). Pass it as a JSON-encoded string in 'payload'. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Branch Transfer Created | `BranchTransfer/Created` | Fires when a new branch transfer is created. |
| Contact Created | `Contact/Created` | Fires when a new contact (customer/supplier) is created. |
| Contact Modified | `Contact/Modified` | Fires when a contact is updated. |
| Credit Note Created | `CreditNote/Created` | Fires when a new credit note is created. |
| Payment Created | `Payment/Created` | Fires when a new payment is recorded. |
| Product Created | `Product/Created` | Fires when a new product is created. |
| Product Modified | `Product/Modified` | Fires when a product is updated. |
| Purchase Order Created | `PurchaseOrder/Created` | Fires when a new purchase order is created. |
| Purchase Order Modified | `PurchaseOrder/Modified` | Fires when a purchase order is updated. |
| Sales Order Created | `SalesOrder/Created` | Fires when a new sales order is created in Cin7 Omni. |
| Sales Order Dispatched | `SalesOrder/Dispatched` | Fires when a sales order is dispatched. |
| Sales Order Modified | `SalesOrder/Modified` | Fires when an existing sales order is updated. |
| Sales Order Voided | `SalesOrder/Voided` | Fires when a sales order is voided/cancelled. |
| Stock Modified | `Stock/Modified` | Fires when stock levels change for a product option / branch. |
