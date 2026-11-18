---
description: "BoxHero inventory management."
hidden: true
---

# BoxHero

<img src="../../.gitbook/assets/connectors/lg/box-hero.png" alt="BoxHero logo">

BoxHero inventory management. Manage items, item attributes, locations, bundles, partners, purchase orders, sales orders, sales returns, price lists and inventory transactions (stock in, stock out, adjust, move) through the BoxHero Open API.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [boxhero.io](https://boxhero.io) |
| **Authentication** | Bearer token |
| **Slug** | `boxHero` |

## Use it

Add BoxHero from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.boxHero.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Bundle | `createBundle` | Creates a bundle: a sellable kit made up of one or more existing inventory items with a quantity each. A bundle SKU is required and must be unique across active bundles. Returns the new bundle id. |
| Create Item | `createItem` | Creates a new inventory item. To seed opening stock, pass both quantity and location_id; BoxHero rejects the request with "location_id is required for this operation" when quantity is supplied without location_id. Omit both to create the item with zero stock. location_id is sent as a query parameter and is dropped entirely when omitted. Returns the new item id. |
| Create Item Attribute | `createItemAttribute` | Creates a custom item attribute spec for the team. Every item can then carry a value for this attribute. Choose the value type: text, date, number or barcode. Returns the new attribute spec id. |
| Create Location | `createLocation` | Creates a new stock location (warehouse, shelf or site) in the team. Locations are the source and destination of Stock In, Stock Out and Move Stock transactions. Returns the new location id. |
| Create Partner | `createPartner` | Creates a supplier or customer partner in BoxHero. Suppliers (type 0) can be attached to Stock In transactions and purchase orders; customers (type 1) to Stock Out transactions and sales orders. Returns the new partner id. |
| Create Price List | `createPriceList` | Creates a price list of unit prices for items or bundles, tied to either purchase orders or sales orders. Identify each line by exactly one of item_id, item_sku, bundle_id or bundle_sku. Returns the new price list id. |
| Create Purchase Order | `createPurchaseOrder` | Creates a purchase order against a supplier with one or more order lines. Identify each line by exactly one of item_id, item_sku, bundle_id or bundle_sku. Set is_draft to keep the order in draft, or finalize_immediately with a location_id to receive every line and close the order at once. Returns the new order id. |
| Create Sales Order | `createSalesOrder` | Creates a sales order against a customer with one or more order lines. Identify each line by exactly one of item_id, item_sku, bundle_id or bundle_sku. Set is_draft to keep the order in draft, or finalize_immediately with a location_id to ship every line and close the order at once. Returns the new order id. |
| Create Sales Return | `createSalesReturn` | Creates a sales return against an existing sales order. Each return line references a source sales order line by its order_item_id, which you read from Get Sales Order. Set finalize_immediately with a location_id to receive the returned stock at once. Returns the new return id. |
| Create Transaction | `createTransaction` | Records an inventory transaction that changes on-hand stock. Stock In (in) and Move Stock (move) take positive quantities, Stock Out (out) negative, Adjust Stock (adjust) signed. from_location_id is required on move and rejected on every other type; partner_id is allowed only on in and out; tx_time is rejected on adjust. Returns the new transaction id. |
| Delete Bundle | `deleteBundle` | Permanently deletes a bundle by id. The component items themselves are not affected. Returns an empty object on success. |
| Delete Bundle By SKU | `deleteBundleBySku` | Permanently deletes a bundle identified by its SKU (case-sensitive) rather than by id. The component items themselves are not affected. Returns an empty object on success. |
| Delete Item | `deleteItem` | Permanently deletes an inventory item by id, together with its stock at every location. Transactions that referenced the item keep it as a deleted reference rather than disappearing. Returns an empty object on success. |
| Delete Item Attribute | `deleteItemAttribute` | Permanently deletes a custom item attribute spec and the attribute values stored on every item in the team. Returns an empty object on success. |
| Delete Item By SKU | `deleteItemBySku` | Permanently deletes an inventory item identified by its SKU (case-insensitive) rather than by id, together with its stock at every location. Returns an empty object on success. |
| Delete Location | `deleteLocation` | Permanently deletes a stock location from the team. Transactions that referenced the location keep it as a deleted reference. Returns an empty object on success. |
| Delete Partner | `deletePartner` | Permanently deletes a partner from the BoxHero team. Transactions and orders that referenced the partner keep it as a deleted reference. Returns an empty object on success. |
| Delete Price List | `deletePriceList` | Permanently deletes a price list by id. Items and bundles priced by it are not affected. Returns an empty object on success. |
| Delete Purchase Order | `deletePurchaseOrder` | Permanently deletes a purchase order by id. Receiving transactions already posted against the order are NOT deleted and the stock they added stays on hand - delete those separately with Delete Transaction if you need to reverse them. Returns an empty object on success. |
| Delete Purchase Order By Number | `deletePurchaseOrderByNumber` | Permanently deletes a purchase order identified by its order number rather than by id. Receiving transactions already posted against the order are NOT deleted and the stock they added stays on hand - delete those separately with Delete Transaction if you need to reverse them. Returns an empty object on success. |
| Delete Sales Order | `deleteSalesOrder` | Permanently deletes a sales order by id. Shipping transactions already posted against the order are NOT deleted and the stock they removed stays deducted - delete those separately with Delete Transaction if you need to reverse them. Returns an empty object on success. |
| Delete Sales Order By Number | `deleteSalesOrderByNumber` | Permanently deletes a sales order identified by its order number rather than by id. Shipping transactions already posted against the order are NOT deleted and the stock they removed stays deducted - delete those separately with Delete Transaction if you need to reverse them. Returns an empty object on success. |
| Delete Sales Return | `deleteSalesReturn` | Permanently deletes a sales return by id. Receiving transactions already posted against the return are NOT deleted and the stock they added back stays on hand - delete those separately with Delete Transaction if you need to reverse them. Returns an empty object on success. |
| Delete Sales Return By Number | `deleteSalesReturnByNumber` | Permanently deletes a sales return identified by its return number rather than by id. Receiving transactions already posted against the return are NOT deleted and the stock they added back stays on hand - delete those separately with Delete Transaction if you need to reverse them. Returns an empty object on success. |
| Delete Transaction | `deleteTransaction` | Deletes an inventory transaction by id and reverses the stock change it applied. Use this to undo a Stock In, Stock Out, Move Stock or Adjust Stock entry. Returns an empty object on success. |
| Get Bundle | `getBundle` | Returns a single bundle by id, including its SKU, barcode, cost, price, memo and the component items with their per-bundle quantities. |
| Get Bundle By SKU | `getBundleBySku` | Returns a single bundle looked up by its SKU (case-sensitive) rather than by id, including its components and pricing. |
| Get Item | `getItem` | Returns a single inventory item by id, including its SKU, barcode, photo URL, custom attribute values, cost, price, total quantity and per-location quantities. |
| Get Item Attribute | `getItemAttribute` | Returns a single custom item attribute spec by id, including its name, value type and display rank. |
| Get Item By SKU | `getItemBySku` | Returns a single inventory item looked up by its SKU (case-insensitive) rather than by id, including attribute values, cost, price and per-location quantities. |
| Get Linked Team | `getLinkedTeam` | Returns the BoxHero team that the connected API token is bound to, including its id, name, team mode, currency code and symbol, and price decimal places. Takes no input and is the cheapest call for verifying a connection. |
| Get Location | `getLocation` | Returns a single stock location by id, including its name, total on-hand quantity and memo. |
| Get Partner | `getPartner` | Returns a single partner by id, including its type, name, phone, email, address and memo. |
| Get Price List | `getPriceList` | Returns a single price list by id, including its order type, name, currency and every priced line. |
| Get Purchase Order | `getPurchaseOrder` | Returns a single purchase order by id, including its status, supplier, order lines with received quantities, additional costs, custom fields, tags, totals and current revision. |
| Get Purchase Order By Number | `getPurchaseOrderByNumber` | Returns a single purchase order looked up by its order number rather than by id, including status, supplier, lines, costs, totals and current revision. |
| Get Sales Order | `getSalesOrder` | Returns a single sales order by id, including its status, customer, order lines with shipped quantities and line ids, additional costs, custom fields, tags, totals and current revision. The line ids are what Create Sales Return needs. |
| Get Sales Order By Number | `getSalesOrderByNumber` | Returns a single sales order looked up by its order number rather than by id, including status, customer, lines, costs, totals and current revision. |
| Get Sales Return | `getSalesReturn` | Returns a single sales return by id, including its status, customer, source sales order, return lines with received quantities and current revision. |
| Get Sales Return By Number | `getSalesReturnByNumber` | Returns a single sales return looked up by its return number rather than by id, including status, customer, source sales order, return lines and current revision. |
| Get Team Member | `getMember` | Returns a single BoxHero team member by id, including the member's display name and role. Use List Team Members to discover member ids. |
| Get Transaction | `getTransaction` | Returns a single inventory transaction by id, including its type, locations, partner, line items with resulting stock levels, totals and revision. Pass a revision to read a historical version of the transaction. |
| List Bundles | `listBundles` | Lists the team's bundles (kits assembled from component items) with cursor pagination. Each row carries the bundle's SKU, barcode, cost, price, memo and component count; use Get Bundle for the full component list. |
| List Item Attributes | `listItemAttributes` | Lists every custom item attribute spec defined for the team, with each spec's id, attribute name, value type and display rank. Takes no input and is not paginated. |
| List Items | `listItems` | Lists the team's inventory items with cursor pagination. Each item carries its name, SKU, barcode, photo URL, custom attribute values, cost, price, total quantity and per-location quantities. Optionally restrict the result to specific item ids or restrict the reported quantities to specific locations. |
| List Locations | `listLocations` | Lists every stock location in the team with its id, name, total on-hand quantity and memo. Takes no input and is not paginated. |
| List Partners | `listPartners` | Lists the team's partners (suppliers and customers) with cursor pagination. Filter by type to return only suppliers (0) or only customers (1); omit it to return both. |
| List Price Lists | `listPriceLists` | Lists the team's price lists with cursor pagination. Filter by order type to return only purchase price lists or only sales price lists. |
| List Purchase Orders | `listPurchaseOrders` | Lists purchase orders with cursor pagination. Filter by status, supplier, order number, tags, order date range, estimated arrival date range and creator. |
| List Sales Orders | `listSalesOrders` | Lists sales orders with cursor pagination. Filter by status, customer, order number, tags, order date range, estimated shipping date range and creator. |
| List Sales Returns | `listSalesReturns` | Lists sales returns with cursor pagination. Filter by status, customer, return number, source sales order, tags, return date range and creator. |
| List Team Members | `listMembers` | Lists every member of the BoxHero team the API token is bound to, with each member's id, display name and role. Takes no input and is not paginated. |
| List Transactions | `listTransactions` | Lists inventory transactions (the stock ledger) with cursor pagination. Filter by transaction type: in (Stock In), out (Stock Out), move (Move Stock) or adjust (Adjust Stock). |
| Receive All Purchase Order Quantities | `receiveAllPurchaseOrderQuantities` | Receives every remaining quantity on a purchase order in one step, posting a Stock In transaction at the given location and marking the order done. Returns the ids of the transactions created. |
| Receive All Purchase Order Quantities By Number | `receiveAllPurchaseOrderQuantitiesByNumber` | Receives every remaining quantity on a purchase order identified by its order number, posting a Stock In transaction at the given location and marking the order done. Returns the ids of the transactions created. |
| Receive All Returned Quantities | `receiveAllReturnedQuantities` | Receives every remaining returned quantity on a sales return in one step, posting a Stock In transaction at the given location and marking the return done. Returns the ids of the transactions created. |
| Receive All Returned Quantities By Number | `receiveAllReturnedQuantitiesByNumber` | Receives every remaining returned quantity on a sales return identified by its return number, posting a Stock In transaction at the given location and marking the return done. Returns the ids of the transactions created. |
| Receive Purchase Order Quantities | `receivePurchaseOrderQuantities` | Receives specific quantities against a purchase order, posting a Stock In transaction at the given location and advancing the order. Returns the id of the transaction created. |
| Receive Purchase Order Quantities By Number | `receivePurchaseOrderQuantitiesByNumber` | Receives specific quantities against a purchase order identified by its order number, posting a Stock In transaction at the given location. Returns the id of the transaction created. |
| Receive Returned Quantities | `receiveReturnedQuantities` | Receives specific returned quantities against a sales return, posting a Stock In transaction at the given location and advancing the return. Returns the id of the transaction created. |
| Receive Returned Quantities By Number | `receiveReturnedQuantitiesByNumber` | Receives specific returned quantities against a sales return identified by its return number, posting a Stock In transaction at the given location. Returns the id of the transaction created. |
| Rename Item Attribute | `renameItemAttribute` | Renames an existing custom item attribute spec. Only the name can be changed; the value type is fixed once the attribute is created. Returns the attribute id. |
| Reorder Item Attributes | `reorderItemAttributes` | Reorders the team's custom item attribute specs. The request body is a top-level JSON array, so pass it as a JSON string listing every attribute id with its new zero-based rank, for example: [{"id":924685,"rank":1},{"id":924686,"rank":0}] |
| Ship All Sales Order Quantities | `shipAllSalesOrderQuantities` | Ships every remaining quantity on a sales order in one step, posting a Stock Out transaction from the given location and marking the order done. Returns the ids of the transactions created. |
| Ship All Sales Order Quantities By Number | `shipAllSalesOrderQuantitiesByNumber` | Ships every remaining quantity on a sales order identified by its order number, posting a Stock Out transaction from the given location and marking the order done. Returns the ids of the transactions created. |
| Ship Sales Order Quantities | `shipSalesOrderQuantities` | Ships specific quantities against a sales order, posting a Stock Out transaction from the given location and advancing the order. Returns the id of the transaction created. |
| Ship Sales Order Quantities By Number | `shipSalesOrderQuantitiesByNumber` | Ships specific quantities against a sales order identified by its order number, posting a Stock Out transaction from the given location. Returns the id of the transaction created. |
| Update Bundle | `updateBundle` | Updates a bundle by id. Only the fields supplied are changed. Supplying components replaces the entire component list. Returns the bundle id. |
| Update Bundle By SKU | `updateBundleBySku` | Updates a bundle identified by its SKU (case-sensitive) rather than by id. Only the fields supplied are changed. Supplying components replaces the entire component list. Returns the bundle id. |
| Update Item | `updateItem` | Updates an inventory item by id. Only the fields supplied are changed; on-hand quantity cannot be changed here, use Create Transaction instead. Returns the item id. |
| Update Item By SKU | `updateItemBySku` | Updates an inventory item identified by its SKU (case-insensitive) rather than by id. Only the fields supplied are changed. Returns the item id. |
| Update Location | `updateLocation` | Updates the name and/or memo of an existing stock location. Fields that are omitted are left unchanged. Returns the location id. |
| Update Partner | `updatePartner` | Updates an existing partner. The partner name is required on every update; omitted optional fields are left unchanged. Returns the partner id. |
| Update Price List | `updatePriceList` | Updates a price list by id. Only the fields supplied are changed; supplying items replaces the full priced line list. Returns the price list id. |
| Update Purchase Order | `updatePurchaseOrder` | Updates a purchase order by id. Only the fields supplied are changed; supplying items replaces the full line list. Pass the revision you last read to guard against a concurrent edit. Returns the order id. |
| Update Purchase Order By Number | `updatePurchaseOrderByNumber` | Updates a purchase order identified by its order number rather than by id. Only the fields supplied are changed; supplying items replaces the full line list. Returns the order id. |
| Update Purchase Order Status | `updatePurchaseOrderStatus` | Moves a purchase order to a new status: draft, confirmed, in-progress or done. Returns the order id. |
| Update Purchase Order Status By Number | `updatePurchaseOrderStatusByNumber` | Moves a purchase order identified by its order number to a new status: draft, confirmed, in-progress or done. Returns the order id. |
| Update Sales Order | `updateSalesOrder` | Updates a sales order by id. Only the fields supplied are changed; supplying items replaces the full line list. Pass the revision you last read to guard against a concurrent edit. Returns the order id. |
| Update Sales Order By Number | `updateSalesOrderByNumber` | Updates a sales order identified by its order number rather than by id. Only the fields supplied are changed; supplying items replaces the full line list. Returns the order id. |
| Update Sales Order Status | `updateSalesOrderStatus` | Moves a sales order to a new status: draft, confirmed, in-progress or done. Returns the order id. |
| Update Sales Order Status By Number | `updateSalesOrderStatusByNumber` | Moves a sales order identified by its order number to a new status: draft, confirmed, in-progress or done. Returns the order id. |
| Update Sales Return | `updateSalesReturn` | Updates a sales return by id. Only the fields supplied are changed; supplying items replaces the full return line list. Returns the return id. |
| Update Sales Return By Number | `updateSalesReturnByNumber` | Updates a sales return identified by its return number rather than by id. Only the fields supplied are changed; supplying items replaces the full return line list. Returns the return id. |
| Update Transaction | `updateTransaction` | Edits an existing inventory transaction, creating a new revision and re-applying the stock change. The transaction type itself cannot be changed. Only the fields supplied are changed; supplying items replaces the full line list. Returns the transaction id. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Inventory Transaction Created | `txs/new` | Fires when an inventory transaction is recorded in BoxHero: Stock In, Stock Out, Adjust Stock or Move Stock. SETUP (BoxHero has no webhook registration API, so this is manual and one-time): in the BoxHero desktop web app open Settings &gt; Integrations &gt; Webhook, click Add/Register webhook, paste the fastn trigger URL, save, and enable the topic. One BoxHero webhook URL receives every topic. Note: BoxHero does NOT fire this event for adjustments created through bulk edits or Excel import. |
| Inventory Transaction Deleted | `txs/delete` | Fires when an inventory transaction is deleted and its stock change reversed. The payload carries only the transaction id and its final revision. SETUP: in the BoxHero desktop web app open Settings &gt; Integrations &gt; Webhook, click Add/Register webhook, paste the fastn trigger URL, save, and enable the topic. One BoxHero webhook URL receives every topic. |
| Inventory Transaction Edited | `txs/edit` | Fires when an existing inventory transaction (Stock In, Stock Out, Move Stock or Adjust Stock) is edited. The payload carries a revision number that starts at 1 and increments on each edit. SETUP: in the BoxHero desktop web app open Settings &gt; Integrations &gt; Webhook, click Add/Register webhook, paste the fastn trigger URL, save, and enable the topic. One BoxHero webhook URL receives every topic. |
| Item Created | `item/new` | Fires when a new item is added to the team's inventory. SETUP: in the BoxHero desktop web app open Settings &gt; Integrations &gt; Webhook, click Add/Register webhook, paste the fastn trigger URL, save, and enable the topic. One BoxHero webhook URL receives every topic. Note: BoxHero does NOT fire this event for the Add Item Variants feature or for items imported from Excel. |
| Item Deleted | `item/delete` | Fires when an item is deleted from the team's inventory. The payload carries only the item id. SETUP: in the BoxHero desktop web app open Settings &gt; Integrations &gt; Webhook, click Add/Register webhook, paste the fastn trigger URL, save, and enable the topic. One BoxHero webhook URL receives every topic. Note: BoxHero does NOT fire this event for bulk deletions made through Data Center &gt; Items. |
| Item Edited | `item/edit` | Fires when an existing item is edited. The payload carries the item's full current field set. SETUP: in the BoxHero desktop web app open Settings &gt; Integrations &gt; Webhook, click Add/Register webhook, paste the fastn trigger URL, save, and enable the topic. One BoxHero webhook URL receives every topic. |
