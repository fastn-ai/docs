---
description: "commercetools composable commerce HTTP API — manage products, categories, customers, carts, orders, inventory, discounts, shipping, payments, types, channels,…"
hidden: true
---

# commercetools

commercetools composable commerce HTTP API — manage products, categories, customers, carts, orders, inventory, discounts, shipping, payments, types, channels, stores, states, and subscriptions.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [commercetools.com](https://commercetools.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 144 |
| **Events** | 0 |
| **Slug** | `commercetools` |

## Use it

Add commercetools from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.commercetools.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Apply Order Edit | `applyOrderEdit` | Apply an order edit, permanently committing its staged actions to the referenced order. Requires the edit version and the current order (resource) version. |
| Change Customer Password | `changeCustomerPassword` | Change a customer's password by providing their current password and a new password. Requires the customer ID and current version. |
| Create Cart | `createCart` | Create a new cart. The currency is required. Optionally set a customer, country, line items, addresses, shipping method, and discount codes. |
| Create Cart Discount | `createCartDiscount` | Create a new cart discount. Requires a localized name, a discount value, a cart predicate, and a unique sortOrder. Set requiresDiscountCode to true if the discount is only applied via a discount code. |
| Create Category | `createCategory` | Create a new category. Name and slug are required localized strings; slug values must be unique within the project. |
| Create Channel | `createChannel` | Create a new channel. Key is required. Roles determine what the channel can be used for (e.g. InventorySupply, ProductDistribution, OrderExport, OrderImport, Primary). |
| Create Customer | `createCustomer` | Create (sign up) a new customer. Email is required; a password is required when authenticationMode is Password (the default). Returns a customer sign-in result containing the created customer. |
| Create Customer Email Token | `createCustomerEmailToken` | Create a token for verifying a customer's email address. Provide the customer ID and a time-to-live in minutes. |
| Create Customer Group | `createCustomerGroup` | Create a new customer group. The group name is required and must be unique within the project. |
| Create Customer Password Reset Token | `createCustomerPasswordResetToken` | Create a token for resetting a customer's password, identified by email address. Optionally set a time-to-live in minutes. |
| Create Discount Code | `createDiscountCode` | Create a new discount code. Requires a unique code and one or more cart discount references (which must have requiresDiscountCode set to true). |
| Create Inventory Entry | `createInventoryEntry` | Create a new inventory entry for a SKU. SKU and quantityOnStock are required. Optionally set a key, supply channel, restock days, and expected delivery. |
| Create Order Edit | `createOrderEdit` | Create an order edit that stages a set of update actions against an order. Provide the order resource reference and the staged actions; apply the edit later to make the changes permanent. |
| Create Order from Cart | `createOrderFromCart` | Create an order from an existing cart. Provide the cart reference and its current version. Optionally set an order number, key, and initial order/payment/shipment states. |
| Create Payment | `createPayment` | Create a new payment. The planned amount (amountPlanned) is required. Optionally attach a customer, payment method info, status, and transactions. |
| Create Product | `createProduct` | Create a new product. Requires a productType reference, a localized name, and a localized slug. Optionally provide a master variant, additional variants, categories, tax category, and state. |
| Create Product Discount | `createProductDiscount` | Create a new product discount. Requires a localized name, a discount value, a product predicate, a unique sortOrder, and an isActive flag. |
| Create Product Type | `createProductType` | Create a new product type that defines a set of attribute definitions shared by products. Name and description are required. |
| Create Shipping Method | `createShippingMethod` | Create a new shipping method. Requires a name, a tax category reference, an isDefault flag, and zone rates (each zone with its shipping rates and prices). |
| Create State | `createState` | Create a new state for a workflow. Requires a key and a type (OrderState, LineItemState, ProductState, ReviewState, PaymentState, QuoteRequestState, StagedQuoteState, or QuoteState). |
| Create Store | `createStore` | Create a new store. Key is required. Optionally set the store name, supported languages and countries, distribution and supply channels, and product selections. |
| Create Subscription | `createSubscription` | Create a subscription that delivers messages and/or resource change notifications to an external message queue (AWS SQS/SNS/EventBridge, Google Cloud Pub/Sub, Azure Service Bus/Event Grid, or Confluent Cloud). A key and a reachable destination are required. |
| Create Tax Category | `createTaxCategory` | Create a new tax category. Name is required. Each rate requires name, amount (0-1), includedInPrice, and country. |
| Create Type | `createType` | Create a new custom-field Type. Requires a key, a localized name, and the resource type IDs it applies to. Field definitions describe the custom fields. |
| Create Zone | `createZone` | Create a new zone. Name is required. Locations is a list of country (and optional state) objects; a location can belong to only one zone. |
| Delete Cart | `deleteCart` | Delete a cart by ID. Requires the current version. |
| Delete Cart Discount | `deleteCartDiscount` | Delete a cart discount by ID. Requires the current version. |
| Delete Category | `deleteCategory` | Delete a category by ID. Requires the current version. |
| Delete Channel | `deleteChannel` | Delete a channel by ID. Requires the current version. |
| Delete Customer | `deleteCustomer` | Delete a customer by ID. Requires the current version. |
| Delete Customer Group | `deleteCustomerGroup` | Delete a customer group by ID. Requires the current version. |
| Delete Discount Code | `deleteDiscountCode` | Delete a discount code by ID. Requires the current version. |
| Delete Inventory Entry | `deleteInventoryEntry` | Delete an inventory entry by ID. Requires the current version. |
| Delete Order | `deleteOrder` | Delete an order by ID. Requires the current version. Optionally erase personal data. |
| Delete Order Edit | `deleteOrderEdit` | Delete an order edit by ID. Requires the current version. |
| Delete Payment | `deletePayment` | Delete a payment by ID. Requires the current version. |
| Delete Product | `deleteProduct` | Delete a product by ID. Requires the current version. The product must be unpublished before it can be deleted. |
| Delete Product Discount | `deleteProductDiscount` | Delete a product discount by ID. Requires the current version. |
| Delete Product Type | `deleteProductType` | Delete a product type by ID. Requires the current version. A product type cannot be deleted while products still reference it. |
| Delete Shipping Method | `deleteShippingMethod` | Delete a shipping method by ID. Requires the current version. |
| Delete State | `deleteState` | Delete a state by ID. Requires the current version. Built-in states cannot be deleted. |
| Delete Store | `deleteStore` | Delete a store by ID. Requires the current version. |
| Delete Subscription | `deleteSubscription` | Delete a subscription by ID. Requires the current version. |
| Delete Tax Category | `deleteTaxCategory` | Delete a tax category by ID. Requires the current version. |
| Delete Type | `deleteType` | Delete a custom-field Type by ID. Requires the current version. |
| Delete Zone | `deleteZone` | Delete a zone by ID. Requires the current version. A zone cannot be deleted while shipping methods reference it. |
| Get Cart | `getCart` | Retrieve a single cart by its unique ID. |
| Get Cart by Key | `getCartByKey` | Retrieve a single cart by its user-defined key. |
| Get Cart Discount | `getCartDiscount` | Retrieve a single cart discount by its unique ID. |
| Get Cart Discount by Key | `getCartDiscountByKey` | Retrieve a single cart discount by its user-defined key. |
| Get Category | `getCategory` | Retrieve a single category by its unique ID. |
| Get Category by Key | `getCategoryByKey` | Retrieve a single category by its user-defined key. |
| Get Channel | `getChannel` | Retrieve a single channel by its unique ID. |
| Get Channel by Key | `getChannelByKey` | Retrieve a single channel by its user-defined key. |
| Get Customer | `getCustomer` | Retrieve a single customer by its unique ID. |
| Get Customer by Key | `getCustomerByKey` | Retrieve a single customer by its user-defined key. |
| Get Customer Group | `getCustomerGroup` | Retrieve a single customer group by its unique ID. |
| Get Customer Group by Key | `getCustomerGroupByKey` | Retrieve a single customer group by its user-defined key. |
| Get Discount Code | `getDiscountCode` | Retrieve a single discount code by its unique ID. |
| Get Discount Code by Key | `getDiscountCodeByKey` | Retrieve a single discount code by its user-defined key. |
| Get Inventory Entry | `getInventoryEntry` | Retrieve a single inventory entry by its unique ID. |
| Get Inventory Entry by Key | `getInventoryEntryByKey` | Retrieve a single inventory entry by its user-defined key. |
| Get Message | `getMessage` | Retrieve a single message by its unique ID. |
| Get Order | `getOrder` | Retrieve a single order by its unique ID. |
| Get Order by Key | `getOrderByKey` | Retrieve a single order by its user-defined key. |
| Get Order by Order Number | `getOrderByOrderNumber` | Retrieve a single order by its order number. |
| Get Order Edit | `getOrderEdit` | Retrieve a single order edit by its unique ID. |
| Get Order Edit by Key | `getOrderEditByKey` | Retrieve a single order edit by its user-defined key. |
| Get Payment | `getPayment` | Retrieve a single payment by its unique ID. |
| Get Payment by Key | `getPaymentByKey` | Retrieve a single payment by its user-defined key. |
| Get Product | `getProduct` | Retrieve a single product by its unique ID, including its current and staged master data. |
| Get Product by Key | `getProductByKey` | Retrieve a single product by its user-defined key. |
| Get Product Discount | `getProductDiscount` | Retrieve a single product discount by its unique ID. |
| Get Product Discount by Key | `getProductDiscountByKey` | Retrieve a single product discount by its user-defined key. |
| Get Product Projection | `getProductProjection` | Retrieve the projected representation of a single product by its ID. Use the staged flag to select current or staged data. |
| Get Product Projection by Key | `getProductProjectionByKey` | Retrieve the projected representation of a single product by its user-defined key. Use the staged flag to select current or staged data. |
| Get Product Type | `getProductType` | Retrieve a single product type by its unique ID, including its attribute definitions. |
| Get Product Type by Key | `getProductTypeByKey` | Retrieve a single product type by its user-defined key. |
| Get Project | `getProject` | Retrieve the current commercetools project settings, including its key, name, languages, currencies, countries, and configured zones. |
| Get Shipping Method | `getShippingMethod` | Retrieve a single shipping method by its unique ID. |
| Get Shipping Method by Key | `getShippingMethodByKey` | Retrieve a single shipping method by its user-defined key. |
| Get State | `getState` | Retrieve a single state by its unique ID. |
| Get State by Key | `getStateByKey` | Retrieve a single state by its user-defined key. |
| Get Store | `getStore` | Retrieve a single store by its unique ID. |
| Get Store by Key | `getStoreByKey` | Retrieve a single store by its user-defined key. |
| Get Subscription | `getSubscription` | Retrieve a single subscription by its unique ID. |
| Get Subscription by Key | `getSubscriptionByKey` | Retrieve a single subscription by its user-defined key. |
| Get Tax Category | `getTaxCategory` | Retrieve a single tax category by its unique ID. |
| Get Tax Category by Key | `getTaxCategoryByKey` | Retrieve a single tax category by its user-defined key. |
| Get Type | `getType` | Retrieve a single custom-field Type by its unique ID. |
| Get Type by Key | `getTypeByKey` | Retrieve a single custom-field Type by its user-defined key. |
| Get Zone | `getZone` | Retrieve a single zone by its unique ID. |
| Get Zone by Key | `getZoneByKey` | Retrieve a single zone by its user-defined key. |
| Import Order | `importOrder` | Import an order directly without a cart. The total price is required. Optionally set an order number, line items, custom line items, addresses, and order/payment/shipment states. Note: a top-level 'key' field was previously (incorrectly) documented here - live-verified that the commercetools Orders Import endpoint silently ignores it (no error, but the key never persists, and Order also has no 'setKey' update action to add one after the fact - see Update Order's description), so it has been removed from this contract to avoid a false promise. |
| List Cart Discounts | `listCartDiscounts` | Query cart discounts in the project. Supports where predicates, sorting, and pagination. |
| List Carts | `listCarts` | Query carts in the project. Supports where predicates, sorting, pagination, and reference expansion. |
| List Categories | `listCategories` | Query categories in the project. Supports where predicates, sorting, pagination, and reference expansion. |
| List Channels | `listChannels` | Query channels in the project. Supports where predicates, sorting, and pagination. |
| List Customer Groups | `listCustomerGroups` | Query customer groups in the project. Supports where predicates, sorting, pagination, and reference expansion. |
| List Customers | `listCustomers` | Query customers in the project. Supports where predicates, sorting, pagination, and reference expansion. |
| List Discount Codes | `listDiscountCodes` | Query discount codes in the project. Supports where predicates, sorting, pagination, and reference expansion. |
| List Inventory | `listInventory` | Query inventory entries in the project. Supports where predicates, sorting, pagination, and reference expansion. |
| List Messages | `listMessages` | Query the project's messages (change/event records for resources). Requires the Messages Query feature to be enabled in project settings. Supports where predicates, sorting, and pagination. |
| List Order Edits | `listOrderEdits` | Query order edits in the project. Supports where predicates, sorting, and pagination. |
| List Orders | `listOrders` | Query orders in the project. Supports where predicates, sorting, pagination, and reference expansion. |
| List Payments | `listPayments` | Query payments in the project. Supports where predicates, sorting, pagination, and reference expansion. |
| List Product Discounts | `listProductDiscounts` | Query product discounts in the project. Supports where predicates, sorting, and pagination. |
| List Product Projections | `listProductProjections` | Query product projections — the projected (current or staged) representation of products. Use the staged flag to choose the current (published) or staged data. |
| List Product Types | `listProductTypes` | Query product types in the project. Supports where predicates, sorting, pagination, and reference expansion. |
| List Products | `listProducts` | Query products in the project (full product representation). Supports where predicates, sorting, pagination, and reference expansion. |
| List Shipping Methods | `listShippingMethods` | Query shipping methods in the project. Supports where predicates, sorting, pagination, and reference expansion. |
| List States | `listStates` | Query states (custom workflow states for orders, line items, products, reviews, payments, and quotes). Supports where predicates, sorting, and pagination. |
| List Stores | `listStores` | Query stores in the project. Supports where predicates, sorting, and pagination. |
| List Subscriptions | `listSubscriptions` | Query subscriptions (message and change notifications delivered to an external message queue). Supports where predicates, sorting, and pagination. |
| List Tax Categories | `listTaxCategories` | Query tax categories in the project. Supports where predicates, sorting, and pagination. |
| List Types | `listTypes` | Query custom-field Types in the project. Supports where predicates, sorting, and pagination. |
| List Zones | `listZones` | Query zones (geographical areas defined by country/state locations). Supports where predicates, sorting, and pagination. |
| Query GraphQL | `queryGraphql` | Execute a GraphQL query or mutation against the commercetools GraphQL API. Provide the query string and optional variables and operation name. |
| Reset Customer Password | `resetCustomerPassword` | Reset a customer's password using a previously created password reset token and a new password. |
| Search Product Projections | `searchProductProjections` | Full-text and faceted search over product projections. Requires product search indexing to be activated for the project. Supports text queries per locale, filters, facets, fuzzy matching, and sorting. |
| Suggest Product Projections | `suggestProductProjections` | Return search-keyword suggestions for auto-complete, based on the search keywords indexed on products. Requires product search indexing to be activated. Provide a partial keyword for one or more project locales. |
| Update Cart | `updateCart` | Update a cart by ID by applying an ordered array of update actions (e.g. addLineItem, removeLineItem, addCustomLineItem, setShippingAddress, setShippingMethod, addDiscountCode, recalculate). Requires the current version. |
| Update Cart Discount | `updateCartDiscount` | Update a cart discount by ID by applying an ordered array of update actions (e.g. changeName, changeValue, changeCartPredicate, changeTarget, changeSortOrder, changeIsActive). Requires the current version. |
| Update Category | `updateCategory` | Update a category by ID by applying an ordered array of update actions (e.g. changeName, changeSlug, setDescription, changeParent, setKey). Requires the current version. |
| Update Channel | `updateChannel` | Update a channel by ID by applying an ordered array of update actions (e.g. changeName, setAddress, addRoles, setRoles, changeKey). Requires the current version. |
| Update Customer | `updateCustomer` | Update a customer by ID by applying an ordered array of update actions (e.g. changeEmail, setFirstName, addAddress, setCustomerGroup, setKey). Requires the current version. |
| Update Customer Group | `updateCustomerGroup` | Update a customer group by ID by applying an ordered array of update actions (e.g. changeName, setKey, setCustomField). Requires the current version. |
| Update Discount Code | `updateDiscountCode` | Update a discount code by ID by applying an ordered array of update actions (e.g. setName, changeIsActive, setMaxApplications, changeCartDiscounts, setValidFrom). Requires the current version. |
| Update Inventory Entry | `updateInventoryEntry` | Update an inventory entry by ID by applying an ordered array of update actions (e.g. addQuantity, removeQuantity, changeQuantity, setRestockableInDays, setExpectedDelivery, setSupplyChannel). Requires the current version. |
| Update Order | `updateOrder` | Update an order by ID by applying an ordered array of update actions (e.g. changeOrderState, changePaymentState, changeShipmentState, setOrderNumber, setPurchaseOrderNumber, addDelivery, addPayment, setCustomerEmail). Requires the current version. Note: unlike most other commercetools resources, Order does NOT support a 'setKey' update action - the live API returns 400 'Invalid type value setKey' - so do not use setKey here. |
| Update Order Edit | `updateOrderEdit` | Update an order edit by ID by applying an ordered array of update actions (e.g. setComment, setKey, setStagedActions, addStagedAction, setCustomField). Requires the current version. |
| Update Payment | `updatePayment` | Update a payment by ID by applying an ordered array of update actions (e.g. setKey, changeAmountPlanned, addTransaction, setStatusInterfaceText, setMethodInfoMethod, addInterfaceInteraction). Requires the current version. |
| Update Product | `updateProduct` | Update a product by ID by applying an ordered array of update actions (e.g. changeName, setDescription, addPrice, addVariant, publish, unpublish, addToCategory). Requires the current version. |
| Update Product Discount | `updateProductDiscount` | Update a product discount by ID by applying an ordered array of update actions (e.g. changeName, changeValue, changePredicate, changeSortOrder, changeIsActive, setKey). Requires the current version. |
| Update Product Type | `updateProductType` | Update a product type by ID by applying an ordered array of update actions (e.g. changeName, setKey, changeDescription, addAttributeDefinition, removeAttributeDefinition). Requires the current version. |
| Update Project | `updateProject` | Update project settings by applying an ordered array of update actions (e.g. changeName, changeCurrencies, changeCountries, changeMessagesConfiguration). Requires the current project version for optimistic concurrency. |
| Update Shipping Method | `updateShippingMethod` | Update a shipping method by ID by applying an ordered array of update actions (e.g. changeName, setDescription, addZone, addShippingRate, changeTaxCategory, changeIsDefault). Requires the current version. |
| Update State | `updateState` | Update a state by ID by applying an ordered array of update actions (e.g. changeKey, setName, setDescription, changeInitial, setTransitions, addRoles). Requires the current version. |
| Update Store | `updateStore` | Update a store by ID by applying an ordered array of update actions (e.g. setName, setLanguages, addCountry, setDistributionChannels, setSupplyChannels). Requires the current version. |
| Update Subscription | `updateSubscription` | Update a subscription by ID by applying an ordered array of update actions (e.g. setKey, setMessages, setChanges, changeDestination, setCustomField). Requires the current version. |
| Update Tax Category | `updateTaxCategory` | Update a tax category by ID by applying an ordered array of update actions (e.g. changeName, addTaxRate, replaceTaxRate, removeTaxRate, setKey). Requires the current version. |
| Update Type | `updateType` | Update a custom-field Type by ID by applying an ordered array of update actions (e.g. changeName, addFieldDefinition, removeFieldDefinition, changeKey). Requires the current version. |
| Update Zone | `updateZone` | Update a zone by ID by applying an ordered array of update actions (e.g. changeName, addLocation, removeLocation, setDescription, setKey). Requires the current version. |
| Verify Customer Email | `verifyCustomerEmail` | Verify a customer's email address using a previously created email verification token. Sets isEmailVerified to true. |
