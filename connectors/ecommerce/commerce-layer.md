---
description: "Commerce Layer is a headless, API-first commerce platform."
hidden: true
---

# Commerce Layer

Commerce Layer is a headless, API-first commerce platform. This connector covers the Commerce Layer Core API (JSON:API) at https://{organization}.commercelayer.io/api — markets, merchants, stores, SKUs and SKU lists, prices and price lists, inventory (stock locations, stock items, stock transfers, reserved stocks), orders, line items and line item options, customers, customer groups, customer addresses and payment sources, addresses, shipments, parcels and parcel line items, shipping methods, categories and zones, deliveries, returns and return line items, promotions and coupons, gift cards, tags, attachments, events, webhooks, imports, exports and cleanups. Authenticates with OAuth 2.0 client_credentials against https://auth.commercelayer.io/oauth/token using an Integration application's client id and secret.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [commercelayer.io](https://commercelayer.io) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 121 |
| **Events** | 43 |
| **Slug** | `commerceLayer` |

## Use it

Add Commerce Layer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.commerceLayer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Address | `createAddress` | Create a new Address. Send a JSON:API resource object with type "addresses" plus its attributes and relationships. |
| Create Customer | `createCustomer` | Create a new Customer. Requires an email address. |
| Create Customer Address | `createCustomerAddress` | Add an existing address to a customer's address book. Requires customer and address relationships; Commerce Layer clones the address so the original stays unchanged. |
| Create Customer Group | `createCustomerGroup` | Create a new Customer Group. Requires a name. |
| Create Inventory Model | `createInventoryModel` | Create a new Inventory Model. Requires a name; the shipping strategy defaults to no_split. |
| Create Line Item | `createLineItem` | Add a line item to an order. Requires a quantity and an order relationship; identify the item with sku_code, bundle_code or the item relationship. |
| Create Market | `createMarket` | Create a new Market. Requires a name plus merchant, price_list and inventory_model relationships. |
| Create Merchant | `createMerchant` | Create a new Merchant. Requires a name and an existing address relationship. |
| Create Order | `createOrder` | Create a new Order (a draft cart). A market relationship is normally required; the order is created in draft status and no money moves until it is placed. |
| Create Package | `createPackage` | Create a new Package at a stock location. Requires a name, its three dimensions, a unit of length and a stock_location relationship. |
| Create Parcel | `createParcel` | Create a Parcel for a shipment. Requires a weight, a unit of weight and shipment plus package relationships. |
| Create Price | `createPrice` | Create a new Price for a SKU in a price list. Do not send currency_code: it is inherited from the price list and Commerce Layer rejects it with 400 PARAM_NOT_ALLOWED. |
| Create Price List | `createPriceList` | Create a new Price List. Requires a name and an ISO 4217 currency code. |
| Create Shipment | `createShipment` | Create a Shipment for an order. Requires order and inventory_stock_location relationships (stock_location is rejected with 400 PARAM_NOT_ALLOWED), plus a shipping_address. IMPORTANT: Commerce Layer only allows a shipment to be created manually once the order is placed and approved and fulfilment is already in progress; on any earlier order it answers 422 "is not creatable unless fulfillment is in progress". In normal use shipments are generated automatically when line items are added to an order, so use this action only to add a manual split shipment during fulfilment. |
| Create Shipping Category | `createShippingCategory` | Create a new Shipping Category. Requires a name. |
| Create Shipping Method | `createShippingMethod` | Create a new Shipping Method. Requires a name and price_amount_cents; attach it to a market, shipping zone and shipping category to make it selectable. |
| Create Shipping Zone | `createShippingZone` | Create a new Shipping Zone. Requires a name; the regex attributes decide which shipping addresses the zone matches. |
| Create SKU | `createSku` | Create a new SKU. Requires a code, a name and a shipping_category relationship. |
| Create SKU List | `createSkuList` | Create a new SKU List. Requires a name; set manual true and add SKU list items, or supply a sku_code_regex. |
| Create SKU List Item | `createSkuListItem` | Add a SKU to a manual SKU list. Requires sku_list and sku relationships. |
| Create Stock Item | `createStockItem` | Create a new Stock Item, i.e. put a quantity of a SKU into a stock location. Requires a quantity and a stock_location relationship; identify the SKU with sku_code or the sku relationship. |
| Create Stock Location | `createStockLocation` | Create a new Stock Location. Requires a name and an existing address relationship. |
| Create Webhook | `createWebhook` | Register a Webhook subscription. Requires a topic (resource.event, e.g. orders.place) and a callback_url that Commerce Layer will POST to. The response includes the shared_secret used to sign deliveries. |
| Delete Address | `deleteAddress` | Permanently delete an Address by its Commerce Layer id. Returns 204 No Content on success. |
| Delete Customer | `deleteCustomer` | Permanently delete a Customer by its Commerce Layer id. Returns 204 No Content on success. Fails if the customer has orders; consider GDPR anonymization instead. |
| Delete Customer Address | `deleteCustomerAddress` | Remove an address from a customer's address book. Returns 204 No Content on success. |
| Delete Customer Group | `deleteCustomerGroup` | Permanently delete a Customer Group by its Commerce Layer id. Returns 204 No Content on success. |
| Delete Inventory Model | `deleteInventoryModel` | Permanently delete an Inventory Model by its Commerce Layer id. Returns 204 No Content on success. |
| Delete Line Item | `deleteLineItem` | Remove a line item from an order. Returns 204 No Content on success. Only line items on a draft or pending order can be deleted. |
| Delete Market | `deleteMarket` | Permanently delete a Market by its Commerce Layer id. Returns 204 No Content on success. Fails if the market still has orders or shipping methods. |
| Delete Merchant | `deleteMerchant` | Permanently delete a Merchant by its Commerce Layer id. Returns 204 No Content on success. Fails if the merchant is still referenced by a market. |
| Delete Order | `deleteOrder` | Permanently delete an Order by its Commerce Layer id. Returns 204 No Content on success. Only draft and pending orders can be deleted; placed orders must be cancelled instead. |
| Delete Package | `deletePackage` | Permanently delete a Package by its Commerce Layer id. Returns 204 No Content on success. |
| Delete Parcel | `deleteParcel` | Permanently delete a Parcel by its Commerce Layer id. Returns 204 No Content on success. |
| Delete Price | `deletePrice` | Permanently delete a Price by its Commerce Layer id. Returns 204 No Content on success. |
| Delete Price List | `deletePriceList` | Permanently delete a Price List by its Commerce Layer id. Returns 204 No Content on success. |
| Delete Shipment | `deleteShipment` | Permanently delete a Shipment by its Commerce Layer id. Returns 204 No Content on success. Only shipments on a draft or pending order can be deleted. |
| Delete Shipping Category | `deleteShippingCategory` | Permanently delete a Shipping Category by its Commerce Layer id. Returns 204 No Content on success. |
| Delete Shipping Method | `deleteShippingMethod` | Permanently delete a Shipping Method by its Commerce Layer id. Returns 204 No Content on success. |
| Delete Shipping Zone | `deleteShippingZone` | Permanently delete a Shipping Zone by its Commerce Layer id. Returns 204 No Content on success. |
| Delete SKU | `deleteSku` | Permanently delete a SKU by its Commerce Layer id. Returns 204 No Content on success. Fails if the SKU still has prices, stock items or line items. |
| Delete SKU List | `deleteSkuList` | Permanently delete a SKU List by its Commerce Layer id. Returns 204 No Content on success. |
| Delete SKU List Item | `deleteSkuListItem` | Remove a SKU from a manual SKU list by deleting its SKU List Item. Returns 204 No Content on success. |
| Delete Stock Item | `deleteStockItem` | Permanently delete a Stock Item by its Commerce Layer id. Returns 204 No Content on success. |
| Delete Stock Location | `deleteStockLocation` | Permanently delete a Stock Location by its Commerce Layer id. Returns 204 No Content on success. |
| Delete Webhook | `deleteWebhook` | Delete a Webhook subscription by its Commerce Layer id, stopping all future deliveries. Returns 204 No Content on success. |
| Get Address | `getAddress` | Retrieve a single Address by its Commerce Layer id. |
| Get Application | `getApplication` | Retrieve the Commerce Layer application the current access token was issued for, including its kind (integration, sales_channel, webapp) and role. Singleton endpoint at /api/application. |
| Get Customer | `getCustomer` | Retrieve a single Customer by its Commerce Layer id. |
| Get Customer Address | `getCustomerAddress` | Retrieve a single Customer Address by its Commerce Layer id. |
| Get Customer Group | `getCustomerGroup` | Retrieve a single Customer Group by its Commerce Layer id. |
| Get Event | `getEvent` | Retrieve a single recorded Event by its Commerce Layer id, with its payload and delivery callbacks. |
| Get Inventory Model | `getInventoryModel` | Retrieve a single Inventory Model by its Commerce Layer id. |
| Get Line Item | `getLineItem` | Retrieve a single Line Item by its Commerce Layer id. |
| Get Market | `getMarket` | Retrieve a single Market by its Commerce Layer id. |
| Get Merchant | `getMerchant` | Retrieve a single Merchant by its Commerce Layer id. |
| Get Order | `getOrder` | Retrieve a single Order by its Commerce Layer id, with its totals, status and payment state. |
| Get Organization | `getOrganization` | Retrieve the Commerce Layer organization this connection authenticates against, including its configuration, logo and subscription limits. This is a singleton endpoint at /api/organization with no id. |
| Get Package | `getPackage` | Retrieve a single Package by its Commerce Layer id. |
| Get Parcel | `getParcel` | Retrieve a single Parcel by its Commerce Layer id, including tracking status and label URL. |
| Get Price | `getPrice` | Retrieve a single Price by its Commerce Layer id. |
| Get Price List | `getPriceList` | Retrieve a single Price List by its Commerce Layer id. |
| Get Reserved Stock | `getReservedStock` | Retrieve a single Reserved Stock record by its Commerce Layer id. |
| Get Shipment | `getShipment` | Retrieve a single Shipment by its Commerce Layer id, with its status, rates and parcels. |
| Get Shipping Category | `getShippingCategory` | Retrieve a single Shipping Category by its Commerce Layer id. |
| Get Shipping Method | `getShippingMethod` | Retrieve a single Shipping Method by its Commerce Layer id. |
| Get Shipping Zone | `getShippingZone` | Retrieve a single Shipping Zone by its Commerce Layer id. |
| Get SKU | `getSku` | Retrieve a single SKU by its Commerce Layer id. |
| Get SKU List | `getSkuList` | Retrieve a single SKU List by its Commerce Layer id. |
| Get SKU List Item | `getSkuListItem` | Retrieve a single SKU List Item by its Commerce Layer id. |
| Get Stock Item | `getStockItem` | Retrieve a single Stock Item by its Commerce Layer id. |
| Get Stock Location | `getStockLocation` | Retrieve a single Stock Location by its Commerce Layer id. |
| Get Webhook | `getWebhook` | Retrieve a single Webhook by its Commerce Layer id. SECURITY: the response carries shared_secret, the HMAC signing secret used to verify deliveries. |
| List Addresses | `listAddresses` | List addresses in your Commerce Layer organization, with JSON:API pagination, sorting, sparse fieldsets and side-loaded relationships. |
| List Customer Addresses | `listCustomerAddresses` | List customer addresses, the entries of each customer's address book. |
| List Customer Groups | `listCustomerGroups` | List customer groups, used to segment customers and to scope private markets. |
| List Customers | `listCustomers` | List the customers of your Commerce Layer organization. |
| List Events | `listEvents` | List the events recorded by your organization. Each event records the resource type and the action that fired a webhook, and links to its delivery callbacks. |
| List Inventory Models | `listInventoryModels` | List inventory models. An inventory model defines the shipping strategy and the stock locations a market draws inventory from. |
| List Line Items | `listLineItems` | List order line items across your Commerce Layer organization. |
| List Markets | `listMarkets` | List the markets of your Commerce Layer organization. A market ties a merchant, a price list and an inventory model together. |
| List Merchants | `listMerchants` | List the merchants of your Commerce Layer organization. A merchant is the selling entity behind a market. |
| List Orders | `listOrders` | List orders (carts and placed orders) of your Commerce Layer organization. |
| List Packages | `listPackages` | List packages, the box formats available at a stock location for building parcels. |
| List Parcels | `listParcels` | List parcels, the physical boxes that make up a shipment, with their tracking numbers and label URLs. |
| List Price Lists | `listPriceLists` | List the price lists of your Commerce Layer organization. A price list groups SKU prices for one currency. |
| List Prices | `listPrices` | List SKU prices. Each price belongs to one price list and one SKU. |
| List Reserved Stocks | `listReservedStocks` | List the stock reservations currently held against your stock items by carts and orders. |
| List Shipments | `listShipments` | List shipments. Commerce Layer generates shipments automatically from an order's line items and inventory model. |
| List Shipping Categories | `listShippingCategories` | List shipping categories. Every SKU belongs to a shipping category, which shipping methods are matched against. |
| List Shipping Methods | `listShippingMethods` | List shipping methods, the delivery options offered to customers in a market. |
| List Shipping Zones | `listShippingZones` | List shipping zones, the regex-matched geographic areas a shipping method applies to. |
| List SKU List Items | `listSkuListItems` | List SKU list items, the individual SKU entries of a manual SKU list. |
| List SKU Lists | `listSkuLists` | List SKU lists. A SKU list groups SKUs manually or by regex, and backs wishlists and bundles. |
| List SKUs | `listSkus` | List the SKUs (stock keeping units) of your Commerce Layer catalogue. |
| List Stock Items | `listStockItems` | List stock items. A stock item is the quantity of one SKU held at one stock location. |
| List Stock Locations | `listStockLocations` | List stock locations (warehouses) of your Commerce Layer organization. |
| List Webhooks | `listWebhooks` | List the webhook subscriptions registered on your Commerce Layer organization. |
| Update Address | `updateAddress` | Update an existing Address. Only the attributes and relationships you send are changed. |
| Update Customer | `updateCustomer` | Update an existing Customer. _request_anonymization and _cancel_anonymization drive the GDPR anonymization flow and are irreversible once anonymization completes. |
| Update Customer Address | `updateCustomerAddress` | Update an existing Customer Address, e.g. to point it at a different address record. |
| Update Customer Group | `updateCustomerGroup` | Update an existing Customer Group. Only the attributes you send are changed. |
| Update Inventory Model | `updateInventoryModel` | Update an existing Inventory Model. Only the attributes you send are changed. |
| Update Line Item | `updateLineItem` | Update an existing Line Item, typically to change its quantity or reserve stock. |
| Update Market | `updateMarket` | Update an existing Market, including enabling or disabling it with the _enable and _disable trigger attributes. |
| Update Merchant | `updateMerchant` | Update an existing Merchant. Only the attributes and relationships you send are changed. |
| Update Order | `updateOrder` | Update an Order and drive its state machine. WARNING: the trigger attributes _place, _authorize, _capture, _approve_and_capture, _refund, _refund_invoice and _cancel move real money against the order's payment source. Send them only when you intend a real financial operation. |
| Update Package | `updatePackage` | Update an existing Package. Only the attributes and relationships you send are changed. |
| Update Parcel | `updateParcel` | Update an existing Parcel, e.g. its weight, customs information or tracking details. |
| Update Price | `updatePrice` | Update an existing Price. Only the attributes and relationships you send are changed. |
| Update Price List | `updatePriceList` | Update an existing Price List. Only the attributes you send are changed. |
| Update Shipment | `updateShipment` | Update a Shipment and drive its fulfilment state machine. WARNING: _purchase buys a real shipping label from the carrier account and charges it, and _decrement_stock permanently reduces inventory. |
| Update Shipping Category | `updateShippingCategory` | Update an existing Shipping Category. Only the attributes you send are changed. |
| Update Shipping Method | `updateShippingMethod` | Update an existing Shipping Method, including enabling or disabling it with _enable and _disable. |
| Update Shipping Zone | `updateShippingZone` | Update an existing Shipping Zone. Only the attributes you send are changed. |
| Update SKU | `updateSku` | Update an existing SKU. Use _add_tags and _remove_tags to change its tags without replacing the whole set. |
| Update SKU List | `updateSkuList` | Update an existing SKU List. Only the attributes and relationships you send are changed. |
| Update SKU List Item | `updateSkuListItem` | Update an existing SKU List Item, e.g. its quantity or position in the list. |
| Update Stock Item | `updateStockItem` | Update an existing Stock Item, typically to change its quantity. Send _validate true to validate the new quantity against reserved stock. |
| Update Stock Location | `updateStockLocation` | Update an existing Stock Location. Only the attributes and relationships you send are changed. |
| Update Webhook | `updateWebhook` | Update a Webhook subscription, including enabling or disabling it with _enable and _disable, and resetting its circuit breaker after repeated delivery failures. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Cleanup Completed | `cleanups.complete` | Fires when a bulk cleanup job finishes. |
| Customer Created | `customers.create` | Fires when a customer record is created, including the implicit customer Commerce Layer creates from an order's customer_email. |
| Export Completed | `exports.complete` | Fires when a bulk export job finishes; the payload carries the signed download URL. |
| Gift Card Activated | `gift_cards.activate` | Fires when a gift card is activated and can be redeemed. |
| Gift Card Deactivated | `gift_cards.deactivate` | Fires when a gift card is deactivated. |
| Gift Card Purchased | `gift_cards.purchase` | Fires when a gift card is purchased. |
| Gift Card Redeemed | `gift_cards.redeem` | Fires when a gift card is redeemed against an order. |
| Import Completed | `imports.complete` | Fires when a bulk import job finishes. |
| In-Stock Subscription Activated | `in_stock_subscriptions.activate` | Fires when a back-in-stock notification subscription is activated. |
| Order Approved | `orders.approve` | Fires when a placed order is approved for fulfilment. |
| Order Cancelled | `orders.cancel` | Fires when a placed order is cancelled and its payment authorization is voided. |
| Order Created | `orders.create` | Fires when a new order (cart) is created in any market. Payload is the JSON:API orders resource object. Schema modelled from the live GET /api/orders/{id} representation, which is the same body Commerce Layer posts; it was not captured from a real delivery. |
| Order Editing Started | `orders.start_editing` | Fires when a placed order is reopened for editing. |
| Order Editing Stopped | `orders.stop_editing` | Fires when editing of a placed order ends and it returns to placed status. |
| Order Fulfilled | `orders.fulfill` | Fires when every shipment on the order is delivered or cancelled and the order is marked fulfilled. |
| Order Moved To Pending | `orders.pending` | Fires when a draft order moves to pending, e.g. on refresh or at checkout. Observed live in this organization's /api/events feed. |
| Order Placed | `orders.place` | Fires when an order is placed by the customer; the orders resource arrives with status 'placed'. |
| Order Refunded | `orders.refund` | Fires when a captured order is refunded. |
| Order Subscription Activated | `order_subscriptions.activate` | Fires when an order subscription becomes active. |
| Order Subscription Cancelled | `order_subscriptions.cancel` | Fires when an order subscription is cancelled. |
| Order Subscription Created | `order_subscriptions.create` | Fires when a recurring order subscription is created. |
| Payment Authorized | `authorizations.create` | Fires when a payment authorization is created against an order. |
| Payment Captured | `captures.create` | Fires when an authorized payment is captured. |
| Payment Refunded | `refunds.create` | Fires when a refund transaction is created. |
| Payment Voided | `voids.create` | Fires when a payment authorization is voided. |
| Return Approved | `returns.approve` | Fires when a requested return is approved. |
| Return Cancelled | `returns.cancel` | Fires when a return is cancelled. |
| Return Received | `returns.receive` | Fires when a return is received at the stock location. |
| Return Rejected | `returns.reject` | Fires when a requested return is rejected. |
| Return Requested | `returns.request` | Fires when a customer requests a return. |
| Return Restocked | `returns.restock` | Fires when returned items are restocked. |
| Return Shipped | `returns.ship` | Fires when the customer ships the return back. |
| Shipment Cancelled | `shipments.cancel` | Fires when a shipment is cancelled. |
| Shipment Delivered | `shipments.deliver` | Fires when a shipment is marked delivered. |
| Shipment Marked Upcoming | `shipments.upcoming` | Fires when a shipment is marked upcoming, awaiting stock. |
| Shipment Packing Started | `shipments.packing` | Fires when packing starts for a shipment. |
| Shipment Picking Started | `shipments.picking` | Fires when picking starts for a shipment. |
| Shipment Put On Hold | `shipments.on_hold` | Fires when a shipment is put on hold. |
| Shipment Ready To Ship | `shipments.ready_to_ship` | Fires when a shipment is marked ready to ship. |
| Shipment Shipped | `shipments.ship` | Fires when a shipment is marked shipped. |
| Stock Transfer Cancelled | `stock_transfers.cancel` | Fires when a stock transfer is cancelled. |
| Stock Transfer Completed | `stock_transfers.complete` | Fires when a stock transfer between stock locations completes. |
| Transaction Created | `transactions.create` | Fires for every payment transaction recorded against an order: authorization, capture, void or refund. |
