---
description: "Connect to Brightpearl's retail operations platform to manage orders, products, contacts, warehouse, and accounting data via the Brightpearl REST API."
---

# Brightpearl

Connect to Brightpearl's retail operations platform to manage orders, products, contacts, warehouse, and accounting data via the Brightpearl REST API.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [brightpearl.com](https://brightpearl.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Actions** | 193 |
| **Events** | 51 |
| **Slug** | `brightpearl` |

## Use it

Add Brightpearl from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.brightpearl.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Contact to Group | `addContactToGroup` | Add one or more contacts to a contact group (POST /contact-group/{id}/member with contactMemberIds array). |
| Add Product Supplier | `addProductSupplier` | Add a supplier to a product |
| Add Tag to Contact | `addTagToContact` | Add a tag (or tag set) to a contact (or contact set). POST /contact/{contactIdSet}/tag/{tagIdSet}, no body. |
| Close Purchase Credit | `closePurchaseCredit` | Starts the invoicing process for a purchase credit, setting it to invoice pending state and then closing it. |
| Close Purchase Order | `closePurchaseOrder` | Invoice and close a purchase order |
| Close Sales Credit | `closeSalesCredit` | Invoice and close a sales credit |
| Close Sales Order | `closeSalesOrder` | Invoice and close a sales order |
| Create Accounting Period | `createAccountingPeriod` | Creates a new accounting period with specified start and end dates. |
| Create Asset Value Correction | `createAssetValueCorrection` | Corrects the value of stock received in a batch from a purchase order. Only unallocated stock can be corrected. |
| Create Brightpearl Category | `createBrightpearlCategory` | Create a new Brightpearl product category |
| Create Company | `createCompany` | Creates a new company entity. |
| Create Contact | `createContact` | Create a new contact (customer, supplier, or staff) |
| Create Contact Group | `createContactGroup` | Create a new contact group |
| Create Contact Note | `createContactNote` | Create a note on a contact |
| Create Customer Payment | `createCustomerPayment` | Record a customer payment against a sales order |
| Create Drop-Ship Note | `createDropShipNote` | Create a drop-ship note for an order |
| Create Drop-Ship Note Event | `createDropShipNoteEvent` | Adds an event (e.g. shipped by supplier) to an existing Drop-Ship Note. |
| Create Exchange Rate | `createExchangeRate` | Adds a new exchange rate for a non-base currency. currencyId goes in the URI path; body carries rate and rateActiveFrom. |
| Create External Transfer | `createExternalTransfer` | Creates an external transfer to move stock between two warehouses. Creates a goods-out note for the source warehouse. |
| Create Goods-In Note | `createGoodsInNote` | Create a goods-in note to receive stock from a purchase order |
| Create Goods-In Note Correction | `createGoodsInNoteCorrection` | Creates a Goods-In Note correction, allowing removal of items received in a batch if there is sufficient on-hand quantity. |
| Create Goods-Out Note | `createGoodsOutNote` | Create a goods-out note to fulfil a sales order |
| Create Goods-Out Note Event | `createGoodsOutNoteEvent` | Adds an event (e.g. picked, packed, shipped) to an existing Goods-Out Note. |
| Create Internal Transfer | `createInternalTransfer` | Transfer goods from one location to another within the same warehouse. |
| Create Journal | `createJournal` | Create a new journal entry |
| Create Journal Entry | `createJournalEntry` | Creates a new journal entry in the Brightpearl accounting system. Debits and credits must balance. |
| Create Location | `createLocation` | Create a new location in a warehouse |
| Create Order | `createOrder` | Create a new sales order, sales credit, purchase order or purchase credit |
| Create Order Acknowledgement | `createOrderAcknowledgement` | Acknowledges or un-acknowledges an existing Brightpearl purchase order. |
| Create Order Note | `createOrderNote` | Create a note on an order |
| Create Order Row | `createOrderRow` | Add a new row to an existing order |
| Create Order Status | `createOrderStatus` | Create a new order status in Brightpearl (POST /order-service/order-status). Supply a name, the order type it belongs to (SO, SC, PO or PC) and a hex colour for its label. Names must be unique within an order type. Returns the new numeric status ID in the response field. Use this instead of asking a user to create a status by hand in the Brightpearl UI. |
| Create Pick | `createPick` | Updates a goods-out note with pick information, specifying what was actually picked from which locations and batches. |
| Create Postal Address | `createPostalAddress` | Create a new postal address |
| Create Product | `createProduct` | Create a new product in Brightpearl |
| Create Product Brand | `createProductBrand` | Create a new product brand |
| Create Product Option | `createProductOption` | Create a new product option |
| Create Product Option Value | `createProductOptionValue` | Create a new product option value |
| Create Product Type | `createProductType` | Create a new product type |
| Create Purchase Credit | `createPurchaseCredit` | Create a purchase credit journal entry. |
| Create Purchase Invoice | `createPurchaseInvoice` | Create a purchase invoice journal entry. |
| Create Purchase Payment | `createPurchasePayment` | Create a purchase payment journal entry against a purchase invoice or purchase credit of a supplier. |
| Create Quarantine Release | `createQuarantineRelease` | Releases stock from the quarantine location to another location within the warehouse. |
| Create Reservation | `createReservation` | Reserve stock for a sales order |
| Create Sales Credit | `createSalesCredit` | Create a new sales credit |
| Create Sales Invoice | `createSalesInvoice` | Create a sales invoice journal entry. |
| Create Sales Order | `createSalesOrder` | Create a new sales order atomically with all rows in a single call |
| Create Stock Correction | `createStockCorrection` | Create a stock correction to adjust stock in a warehouse location (Brightpearl POST /warehouse-service/warehouse/{warehouseId}/stock-correction). Positive quantity increments, negative decrements; cost is required when incrementing; reason is required per correction. |
| Create Stock Transfer | `createStockTransfer` | Create a stock transfer between warehouses |
| Create Supplier | `createSupplier` | Create a supplier contact in Brightpearl. Suppliers are created through the contact endpoint with relationshipToAccount.isSupplier set to true. |
| Create Warehouse | `createWarehouse` | Create a new warehouse. Returns the ID assigned to the new warehouse. A default and quarantine location will also be created automatically. |
| Create Webhook | `createWebhook` | Create a Brightpearl webhook in the Integration service. |
| Create Zone | `createZone` | Create a new zone within a warehouse. Zone name must be unique within the warehouse (case-insensitive) and max 32 characters. Returns the ID of the newly created zone. |
| Delete Customer Payment | `deleteCustomerPayment` | Deletes a customer payment by its ID. |
| Delete Goods-In Note | `deleteGoodsInNote` | Deletes a Goods-In Note for the given ID. Can only be deleted if no goods movements have been made on the associated stock. |
| Delete Goods-Out Note | `deleteGoodsOutNote` | Deletes a Goods-Out Note. Can only be deleted if the status is open and the note has not been shipped. |
| Delete Location | `deleteLocation` | Delete a warehouse location. Can only delete if no stock has ever been stored there. Cannot delete the default or quarantine location. |
| Delete Order Row | `deleteOrderRow` | Delete a row from an order |
| Delete Reservation Row | `deleteReservationRow` | Deletes the reservation against the specified order row(s), making the reserved stock available again. |
| Delete Supplier Payment | `deleteSupplierPayment` | Delete a supplier payment by payment ID. |
| Delete Warehouse | `deleteWarehouse` | Delete a warehouse by ID. Can only delete if the warehouse has not been involved in any goods movements and is not the only warehouse. |
| Delete Webhook | `deleteWebhook` | Delete a registered webhook by its numeric ID. Returns an empty body on success (200). |
| Delete Zone | `deleteZone` | Delete a warehouse zone by warehouse ID and zone ID. |
| Forget Contact | `forgetContact` | Forgets a contact and their data by scrambling personal information. Only customer contacts can be forgotten. |
| Forget Contact From Orders | `forgetContactFromOrders` | Obfuscates contact details from orders, replacing the contact's name with FORGOTTEN CONTACT and the date/time. |
| Get Account Configuration | `getAccountConfiguration` | Get account configuration including base currency and tax scheme |
| Get Accounting Period | `getAccountingPeriod` | Get accounting periods |
| Get Accounting Period Lock | `getAccountingPeriodLock` | Returns the accounting period lock details, including who locked it and the date locked until. |
| Get Brightpearl Category | `getBrightpearlCategory` | Get Brightpearl categories |
| Get Bundle Availability | `getBundleAvailability` | Returns the bundle availability for a given bundle product ID, including total availability across all warehouses and per-warehouse breakdown. |
| Get Channel Brand | `getChannelBrand` | Gets the brand associated with a specific channel. |
| Get Company | `getCompany` | Returns company details for the given company ID or ID set. |
| Get Contact | `getContact` | Retrieve contacts by ID or ID range |
| Get Contact Balance | `getContactBalance` | Returns the balance for a contact (customer or supplier) for a given currency, optionally filtered by date range. |
| Get Contact Custom Field Metadata | `getContactCustomFieldMetadata` | Get custom field metadata for contacts |
| Get Contact Custom Fields | `getContactCustomFields` | Get custom field values for contacts |
| Get Contact Group | `getContactGroup` | Get contact groups |
| Get Contact Group Member | `getContactGroupMember` | Returns the membership of a contact group. Brightpearl's member GET does not filter by contact ID; to check a single contact's membership use searchContactGroupMembers with a contactId filter. |
| Get Contact Group Members | `getContactGroupMembers` | Returns the member contacts of a contact group. |
| Get Contact Postal Address | `getContactPostalAddress` | Get postal addresses by ID |
| Get Contact Status | `getContactStatus` | Returns the current status of one or more contacts. Brightpearl's contact-service has no standalone contact-status GET, so this reads the contact(s) via Contact GET; use response[].contactStatus.current. (The catalogue of all possible statuses lives in account-service configuration, outside this contact-service connector.) |
| Get Customer Payment Totals | `getCustomerPaymentTotals` | Get payment totals for one or more sales order IDs, including amountPaid, amountAuthorized, amountCaptured, and paymentCurrency when payments exist. |
| Get Default Location | `getDefaultLocation` | Returns the ID of the default location for a specified warehouse. |
| Get Discount Contact Usage | `getDiscountContactUsage` | Gets the usage of a discount by a specific contact. |
| Get Discount Total Usage | `getDiscountTotalUsage` | Gets the total usage count for a discount across all contacts. |
| Get Drop-Ship Note | `getDropShipNote` | Get drop-ship notes by ID |
| Get Exchange Rate | `getExchangeRate` | Returns exchange rates for all non-base currencies of the account. |
| Get Fulfilment Source | `getFulfilmentSource` | Returns fulfilment source availability for a set of product IDs. |
| Get Goods-In Note | `getGoodsInNote` | Get goods-in notes by ID |
| Get Goods-Out Note | `getGoodsOutNote` | Get goods-out notes by ID |
| Get Integration Instance | `getIntegrationInstance` | Fetch the installed integration instance associated with the authenticated app/token (parameterless). |
| Get Journal | `getJournal` | Returns journal details for the given journal ID or ID set. |
| Get Landed Cost Estimate | `getLandedCostEstimate` | Gets the landed cost estimate for an order. |
| Get Lead Source | `getLeadSource` | Get lead sources |
| Get Location | `getLocation` | Get warehouse locations |
| Get Nominal Code | `getNominalCode` | Get nominal codes (chart of accounts) |
| Get Order | `getOrder` | Retrieve one or more orders by ID or ID range (e.g. 100, 100-200, 100,101,102) |
| Get Order Custom Field Metadata | `getOrderCustomFieldMetadata` | Returns the custom field definitions for sales or purchase orders. |
| Get Order Custom Fields | `getOrderCustomFields` | Returns the custom field data held against a given order. |
| Get Order Fulfilment Status | `getOrderFulfilmentStatus` | Returns fulfilment information for each row of an order, including quantity, fulfilled count, shipped count, and fulfilment locations. |
| Get Order Note | `getOrderNote` | Get notes for an order |
| Get Order Shipping Status | `getOrderShippingStatus` | Returns all order shipping status codes and their descriptions (NST, SNS, SPS, ASS). |
| Get Order Status | `getOrderStatus` | Get order statuses by ID set |
| Get Order Stock Status | `getOrderStockStatus` | Returns all order stock status codes and their descriptions (e.g. SON, SOP, SOA for sales orders; PON, POP, POA for purchase orders). |
| Get Order Types | `getOrderTypes` | Returns all order type codes used to identify the types of orders (sales orders, sales credits, purchase orders and purchase credits). Returns all four types — no filtering supported. |
| Get Payment Method | `getPaymentMethod` | Get payment methods |
| Get Price List | `getPriceList` | Get price lists |
| Get Product | `getProduct` | Retrieve products by ID or ID range |
| Get Product Availability | `getProductAvailability` | Get stock availability for products |
| Get Product Brand | `getProductBrand` | Get product brands by ID |
| Get Product Bundle | `getProductBundle` | Returns a list of the bundles that contain a given product, and recursively any bundles that contain those bundles. |
| Get Product Channels | `getProductChannels` | Get product channels (Brightpearl GET /product-service/channel/{ID-SET}). Leave idSet empty to retrieve all channels, or pass comma-separated channel IDs (e.g. 1,4). |
| Get Product Custom Field Metadata | `getProductCustomFieldMetadata` | Get custom field metadata for products |
| Get Product Custom Fields | `getProductCustomFields` | Get custom field values for products by product ID or ID set. |
| Get Product Group | `getProductGroup` | Get product groups (variant groups) |
| Get Product Groups | `searchProductGroups` | Retrieves one or more product groups by ID set. Brightpearl exposes no product-group resource-search; the only documented read is the product-group GET (product-service/product-group/{idSet}). Discover group IDs via searchProducts (productGroupId column). |
| Get Product Option | `getProductOption` | Get product options (e.g. Size, Colour) |
| Get Product Option Value | `getProductOptionValue` | Get product option values |
| Get Product Price | `getProductPrice` | Get prices for products across all price lists |
| Get Product Primary Supplier | `getProductPrimarySupplier` | Gets the supplier contact IDs associated with one or more products. Returns a map of product ID to array of supplier contact IDs. |
| Get Product Supplier | `getProductSupplier` | Get suppliers for products |
| Get Product Type | `getProductType` | Get product types |
| Get Product Type Option Association | `getProductTypeOptionAssociation` | Gets a product type by ID, including its associated options (associations.options). Brightpearl exposes the option associations through the product-type GET resource, not a dedicated association GET. |
| Get Project | `getProject` | Returns project details for the given project ID or ID set. Omit the ID to return all projects. |
| Get Purchase Invoice | `getPurchaseInvoice` | Retrieves purchase invoice journal entries by journal ID or ID set. In Brightpearl, purchase invoices are stored as journal records (journalTypeCode "PI"). Use the journal ID set (e.g. "102314" or "1-5,10") to fetch the corresponding journal entries. |
| Get Purchase Order Custom Field Metadata | `getPurchaseOrderCustomFieldMetadata` | Get the custom field definitions for purchase orders. Optionally filter by a comma-separated ID set (e.g. "5,7"). |
| Get Purchase Payment Total | `getPurchasePaymentTotal` | Returns payment totals for one or more purchase orders. |
| Get Quarantine Location | `getQuarantineLocation` | Returns the ID of the quarantine location for a specified warehouse. |
| Get Reservation | `getReservation` | Get reservations for a sales order |
| Get Sale Order Custom Field Metadata | `getSaleOrderCustomFieldMetadata` | Get the custom field definitions for sale orders. Optionally filter by a comma-separated ID set (e.g. "5,7"). |
| Get Sale Payment Total | `getSalePaymentTotal` | Returns payment totals (amount paid, authorized, captured) for one or more sales orders. |
| Get Sales Credit | `getSalesCredit` | Retrieve one or more sales credits by ID |
| Get Sales Credit Order | `getSalesCreditOrder` | Gets a sales credit order by ID set. |
| Get Sales Invoice | `getSalesInvoice` | Get sales invoice journal entries by journal ID or ID set. In Brightpearl sales invoices are stored as journals (journalTypeCode "SI"). Pass the journal ID returned by createSalesInvoice (e.g. "5291" or "1-5,10"). |
| Get Sales Order | `getSalesOrder` | Retrieve sales orders by ID |
| Get Sales Order Row | `getSalesOrderRow` | Get rows for a sales order |
| Get Season | `getSeason` | Fetches one or more Seasons by Season ID. If no ID is supplied all Seasons will be returned. |
| Get Shipping Method | `getShippingMethod` | Get shipping methods |
| Get Supplier | `getSupplier` | Get supplier/vendor contact details by Brightpearl contact ID. Suppliers are contacts with relationshipToAccount.isSupplier. |
| Get Supplier Invoice by Order ID | `getSupplierInvoiceByOrderId` | Retrieve the purchase (supplier) invoice details for a Purchase Order. Brightpearl has no accounting-service supplier-invoice GET; the order-service order GET returns the order's invoices[] (invoiceReference, taxDate, dueDate) plus supplier party and totals. |
| Get Supplier Payment Totals | `getSupplierPaymentTotals` | Get payment totals for one or more purchase order IDs, including amountPaid and paymentCurrency when payments exist. |
| Get Tag | `getTag` | Get tags |
| Get Tax Code | `getTaxCode` | Get tax codes |
| Get Warehouse | `getWarehouse` | Get warehouses by ID |
| Get Warehouse Defaults | `getWarehouseDefaults` | Returns warehouse defaults (default location, overflow location, reorder level, reorder quantity) for specified products in a warehouse. |
| Get Zone | `getZone` | Get zones for a warehouse. Optionally filter by zone ID-SET (e.g. '1-3,5'). Omit zoneIdSet to return all zones for the warehouse. |
| List Channels | `listChannels` | Returns all channels in the Brightpearl account, sorted by channel ID. |
| List Price Lists | `listPriceLists` | Lists every price list for the connected Brightpearl account, including selling and buying lists; choose a SELL list when setting Shopify variant prices. |
| List Webhooks | `listWebhooks` | Retrieve registered webhooks. Omit ID set to get all webhooks. |
| Patch Contact | `patchContact` | Updates a single contact field via a JSON Patch operation. (The fastn executor cannot expand a dynamic operations array as the JSON body root, so this action applies one op per call; call repeatedly for multiple fields.) |
| Post Sales Receipt | `postSalesReceipt` | Post a sales receipt (customer payment) against a sales invoice/order. This account's /sales-receipt endpoint uses the deprecated flat body: orderId/customerId, invoiceReference, received{currency,value}, bankAccountNominalCode, taxDate. Returns the new journal ID. |
| Post Supplier Payment | `postSupplierPayment` | Record a supplier payment against a purchase order |
| Remove Contact from Group | `removeContactFromGroup` | Remove a contact from a contact group |
| Remove Tag from Contact | `removeTagFromContact` | Remove a tag from a contact |
| Search All Transactions | `searchAllTransactions` | Searches all transaction statements with flexible filtering. |
| Search Brands | `searchBrands` | Search and list all product brands in the Brightpearl account. Supports filtering by brandId and brandName. |
| Search Collections | `searchCollections` | Searches for product collections. |
| Search Companies | `searchCompanies` | Searches companies by name or ID. |
| Search Contact Group Members | `searchContactGroupMembers` | Searches contact group members. Filterable columns: contactGroupId, contactGroupName, firstName, lastName. Sortable: contactId. |
| Search Contact Groups | `searchContactGroups` | Searches contact groups by name or ID. |
| Search Contacts | `searchContacts` | Search contacts with filters |
| Search Currency | `searchCurrency` | Search currencies configured in the account |
| Search Customer Payments | `searchCustomerPayments` | Search customer payments |
| Search Goods Movements | `searchGoodsMovements` | Searches goods movements with optional filters. |
| Search Goods-In Notes | `searchGoodsInNotes` | Search goods-in notes |
| Search Journals | `searchJournals` | Searches journals with flexible filtering by journal ID, order ID, nominal code, date, contact, etc. |
| Search Locations | `searchLocations` | Search warehouse locations by warehouse ID and optional filters (barcode, groupings, zone). |
| Search Orders | `searchOrders` | Search orders with filters |
| Search Products | `searchProducts` | Search products with filters |
| Search Sales Orders | `searchSalesOrders` | Search sales orders with filters |
| Search Supplier Invoices | `searchSupplierInvoices` | Search purchase orders (supplier invoices) via the order-service order-search. Filters to purchase orders (orderTypeId 2); optionally narrow by supplier contactId. Returns rows of [orderId, orderTypeId, contactId] per metaData.columns. |
| Search Supplier Payments | `searchSupplierPayments` | Search supplier payments. |
| Search Suppliers | `searchSuppliers` | Search supplier/vendor contacts in Brightpearl using contact search filters. Brightpearl models suppliers as contacts with isSupplier=true. |
| Search Tags | `searchTags` | Returns all contact tags. Optionally specify an ID set to get specific tags. |
| Search Warehouses | `searchWarehouses` | Search warehouses. Filterable by id, name, typeDescription, and addressId. Results sorted by name ASC. |
| Set Product Image Link | `setProductImageLink` | Save an image URL on a Brightpearl product by writing it to a product custom field. Brightpearl's API has no image endpoint, so create a Text or Text area product custom field for the link first (for example PCF_IMAGEURL) and pass its code. Find codes with Get Product Custom Field Metadata. Returns the product's custom fields after the update. |
| Update Company | `updateCompany` | Updates an existing company's name. |
| Update Contact | `updateContact` | Update a single contact field via JSON Patch. Brightpearl's contact update is RFC6902 PATCH; the fastn executor cannot expand a dynamic array body, so apply one op per call (call repeatedly for multiple fields). For multi-field convenience this mirrors patchContact. |
| Update Contact Custom Fields | `updateContactCustomFields` | Updates one custom field on a contact via a JSON Patch operation. Brightpearl expects a bare JSON Patch array body; the fastn executor cannot expand a dynamic array root, so this applies one op per call. Path uses the field code, e.g. /PCF_ACCOUNTN. |
| Update Contact Group | `updateContactGroup` | Updates an existing contact group's name and description. |
| Update Contact Status | `updateContactStatus` | Updates the status of one or more contacts (up to 200 contact IDs per request). |
| Update Exchange Rate | `updateExchangeRate` | Updates an EXISTING exchange rate for a non-base currency. rateActiveFrom must exactly match an existing rate's active-from date in the account timezone, otherwise ACCC-083 is returned. currencyId in the URI path; body carries rate and rateActiveFrom. |
| Update Location | `updateLocation` | Update a warehouse location (full replace). groupingA is required; zoneId can be supplied to assign the location to a zone. Returns an empty object on success. |
| Update Order | `updateOrder` | Update an existing order (PATCH) |
| Update Order Custom Fields | `updateOrderCustomFields` | Updates custom fields on an order using JSON Patch operations (add, replace, remove). |
| Update Order Row | `updateOrderRow` | Update an existing order row |
| Update Order Status | `updateOrderStatus` | Update the status of an order |
| Update Product | `updateProduct` | Update an existing product |
| Update Product Details | `updateProductDetails` | Update a Brightpearl product's details in one call: identifiers (SKU, EAN, UPC, ISBN, MPN, barcode), brand, collection and product type, stock tracking, weight and dimensions, tax settings, name, condition, categories, long and short descriptions, seasons, nominal codes and variant options. Send the fields you want to set. Brightpearl's docs don't say whether omitted fields are cleared, so a full sync should send every field it manages. Accounts in VAT mode must include financialDetails. Product status can't be set through this endpoint. |
| Update Product Price | `updateProductPrice` | Set a Brightpearl product's prices on one or more price lists. Each price list entry takes a map of minimum order quantity to net price (both strings), so a single price is {"1": "19.99"} and quantity breaks add more keys. Use List Price Lists to find price list IDs. Brightpearl treats supplied prices as net prices. |
| Update Sales Order Row | `updateSalesOrderRow` | Update a row on a sales order |
| Update Warehouse | `updateWarehouse` | Update one or more warehouses. Accepts an array of warehouse objects. Can update name, address, typeCode, and click-and-collect settings. |
| Update Zone | `updateZone` | Update a zone's name using JSON Patch (RFC 6902). Sends a replace operation on /name. Returns the updated zone. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Contact (Any Event) | `contact` | Fires on any lifecycle event for a contact — created, modified, or deleted. |
| Contact Created | `contact.created` | Fires when a new contact is created in Brightpearl. |
| Contact Deleted | `contact.deleted` | Fires when a contact is deleted from Brightpearl. |
| Contact Modified | `contact.modified` | Fires when a contact record is modified. |
| Drop-Ship Note (Any Event) | `drop-ship-note` | Fires on any lifecycle event for a drop-ship note — created, modified, or deleted. |
| Drop-Ship Note Created | `drop-ship-note.created` | Fires when a new drop-ship note is created. |
| Drop-Ship Note Deleted | `drop-ship-note.deleted` | Fires when a drop-ship note is deleted. |
| Drop-Ship Note Modified | `drop-ship-note.modified` | Fires when a drop-ship note is modified. |
| External Transfer (Any Event) | `external-transfer` | Fires on any lifecycle event for an external (warehouse-to-warehouse) stock transfer. |
| External Transfer Created | `external-transfer.created` | Fires when a new external (warehouse-to-warehouse) stock transfer is created. |
| External Transfer Modified | `external-transfer.modified` | Fires when an external stock transfer is modified. |
| Goods-In Note (Any Event) | `goods-in-note` | Fires on any lifecycle event for a goods-in note — created, modified, or deleted. Used when stock is received against a purchase order. |
| Goods-In Note Created | `goods-in-note.created` | Fires when a new goods-in note is created (stock received against a purchase order). |
| Goods-In Note Deleted | `goods-in-note.deleted` | Fires when a goods-in note is deleted. |
| Goods-In Note Modified | `goods-in-note.modified` | Fires when a goods-in note is modified. |
| Goods-Out Note (Any Event) | `goods-out-note` | Fires on any lifecycle event for a goods-out note — created, printed, picked, packed, or shipped. Commonly used by carrier integrations. |
| Goods-Out Note Created | `goods-out-note.created` | Fires when a new goods-out note is created. |
| Goods-Out Note Deleted | `goods-out-note.deleted` | Fires when a goods-out note is deleted. |
| Goods-Out Note Modified | `goods-out-note.modified` | Fires when a goods-out note is modified (e.g. printed, picked, packed, or shipped status changes). |
| Internal Transfer (Any Event) | `internal-transfer` | Fires on any lifecycle event for an internal stock transfer — created, modified, or deleted. |
| Internal Transfer Created | `internal-transfer.created` | Fires when a new internal stock transfer is created. |
| Internal Transfer Modified | `internal-transfer.modified` | Fires when an internal stock transfer is modified. |
| Order (Any Event) | `order` | Fires on any lifecycle event for any order type (sales order, purchase order, sales credit, purchase credit) — created, modified, or deleted. |
| Order Deleted | `order.deleted` | Fires when any order (sales order, purchase order, sales credit, or purchase credit) is deleted. |
| Order Modified | `order.modified` | Fires when any order (sales order, purchase order, sales credit, or purchase credit) is modified. |
| Order Status Modified | `order.modified.order-status` | Fires when an order status changes. Brightpearl raises this as order.modified.order-status; the previously configured sales-order.modified is not a subscribable event. |
| order.modifed.fully-shipped | `order.modifed.fully-shipped` | Fires when any order (sales order, purchase order, sales credit, or purchase credit) is created. |
| Product (Any Event) | `product` | Fires on any lifecycle event for a product — created, modified, or deleted. Also fires for stock level changes (resource-specifier: on-hand-modified). |
| Product Created | `product.created` | Fires when a new product is created in Brightpearl. |
| Product Deleted | `product.destroyed` | Fires when a product is deleted from Brightpearl. |
| Product Modified | `product.modified` | Fires when a product is modified (e.g. details, price, or stock level changed). Resource specifier may be 'on-hand-modified' for stock changes. |
| Purchase Credit (Any Event) | `purchase-credit` | Fires on any lifecycle event for a purchase credit — created, modified, or deleted. |
| Purchase Credit Created | `purchase-credit.created` | Fires when a new purchase credit is created. |
| Purchase Credit Deleted | `purchase-credit.deleted` | Fires when a purchase credit is deleted. |
| Purchase Credit Modified | `purchase-credit.modified` | Fires when a purchase credit is modified. |
| Purchase Order (Any Event) | `purchase-order` | Fires on any lifecycle event for a purchase order — created, modified, or deleted. |
| Purchase Order Created | `purchase-order.created` | Fires when a new purchase order is created in Brightpearl. |
| Purchase Order Deleted | `purchase-order.deleted` | Fires when a purchase order is deleted. |
| Purchase Order Modified | `purchase-order.modified` | Fires when a purchase order is modified. |
| Sales Credit (Any Event) | `sales-credit` | Fires on any lifecycle event for a sales credit — created, modified, or deleted. |
| Sales Credit Created | `sales-credit.created` | Fires when a new sales credit is created in Brightpearl. |
| Sales Credit Deleted | `sales-credit.deleted` | Fires when a sales credit is deleted. |
| Sales Credit Modified | `sales-credit.modified` | Fires when a sales credit is modified. |
| Sales Order (Any Event) | `sales-order` | Fires on any lifecycle event for a sales order — created, modified, or deleted. |
| Sales Order Created | `sales-order.created` | Fires when a new sales order is created in Brightpearl. |
| Sales Order Deleted | `sales-order.deleted` | Fires when a sales order is deleted from Brightpearl. |
| Stock Correction (Any Event) | `stock-correction` | Fires on any lifecycle event for a stock correction. |
| Stock Correction Created | `stock-correction.created` | Fires when a stock correction is created in Brightpearl. |
| Stock Transfer (Any Event) | `stock-transfer` | Fires on any lifecycle event for a stock transfer. |
| Stock Transfer Created | `stock-transfer.created` | Fires when a stock transfer is created. |
| Stock Transfer Modified | `stock-transfer.modified` | Fires when a stock transfer is modified. |
