---
description: "Snipcart headless e-commerce REST API — manage orders, subscriptions, customers, products, discounts, abandoned carts, custom shipping methods, refunds, order…"
hidden: true
---

# Snipcart

<img src="../../.gitbook/assets/connectors/snipcart.png" alt="Snipcart logo" width="64">

Snipcart headless e-commerce REST API — manage orders, subscriptions, customers, products, discounts, abandoned carts, custom shipping methods, refunds, order notifications, and store domain settings.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [snipcart.com](https://snipcart.com) |
| **Authentication** | Basic auth |
| **Slug** | `snipcart` |

## Use it

Add Snipcart from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.snipcart.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Allowed Domains | `addAllowedDomains` | Add one or more allowed domains. Provide a JSON array of objects, each with a domain and optional protocol. |
| Archive Product | `archiveProduct` | Archive a product by its id. The product is marked archived rather than permanently deleted. |
| Batch Update Order Statuses | `batchUpdateOrders` | Update the status of multiple orders in a single request. Provide a JSON array of objects, each with an order id (token) and a new status. |
| Cancel Subscription | `cancelSubscription` | Cancel an active subscription by its id. |
| Count Subscriptions | `countSubscriptions` | Count the subscriptions in your store that are in one or more given states. |
| Create Discount | `createDiscount` | Create a discount. The trigger determines when the discount applies and the type determines how it reduces the total; supply the conditional fields required by the chosen trigger and type. |
| Create Order Notification | `createOrderNotification` | Create a notification on an order — for example a private comment, an email to the customer, or a tracking-number notice. |
| Create Order Refund | `createOrderRefund` | Issue a full or partial refund on an order, optionally auto-refunding taxes and notifying the customer. |
| Create Shipping Method | `createShippingMethod` | Create a custom shipping method with one or more rates and optional conditions (country, postal-code, order total, shipping zone). |
| Delete Discount | `deleteDiscount` | Permanently delete a discount by its id. |

<details>

<summary>See 30 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Shipping Method | `deleteShippingMethod` | Delete a custom shipping method by its id. |
| Fetch Product From URL | `fetchProduct` | Fetch and register a product by crawling the given URL where the Snipcart buy-button markup is found. |
| Get Abandoned Cart | `getAbandonedCart` | Retrieve a single abandoned cart by its token. |
| Get Customer | `getCustomer` | Retrieve the details and statistics of a single customer by id. |
| Get Discount | `getDiscount` | Retrieve a single discount by its id. |
| Get Order | `getOrder` | Retrieve the full details of a single order by its unique token. |
| Get Order Refund | `getOrderRefund` | Retrieve a single refund on an order by its refund id. |
| Get Product | `getProduct` | Retrieve a single product by its Snipcart GUID or user-defined ID, including stock, variants, and custom fields. |
| Get Shipping Method | `getShippingMethod` | Retrieve a single custom shipping method by its id. |
| Get Store Domain | `getStoreDomain` | Retrieve your store's default domain and protocol. |
| Get Subscription | `getSubscription` | Retrieve the details of a single subscription by its id. |
| List Abandoned Carts | `listAbandonedCarts` | Retrieve a cursor-paginated list of abandoned carts, with optional filters for time range, value, email, product, and campaign. |
| List Allowed Domains | `listAllowedDomains` | List every allowed domain and subdomain other than your default website domain. |
| List Customer Orders | `listCustomerOrders` | List all orders placed by a specific customer. |
| List Customers | `listCustomers` | Retrieve a paginated list of customers with optional filters for status, email, name, and date range. |
| List Discounts | `listDiscounts` | Retrieve all discounts configured in your Snipcart store. |
| List Order Digital Goods | `listOrderDigitalGoods` | List the digital goods (downloadable files) associated with an order, including download URLs and usage limits. |
| List Order Notifications | `listOrderNotifications` | Retrieve the notifications (emails, comments, logs) attached to a specific order. |
| List Order Refunds | `listOrderRefunds` | List all refunds issued against a specific order. |
| List Orders | `listOrders` | Retrieve a paginated list of orders in your Snipcart store, with optional filters for status, payment status, date range, and addresses. |
| List Products | `listProducts` | Retrieve a paginated list of products defined in your Snipcart store, with optional filters and sorting. |
| List Shipping Methods | `listShippingMethods` | Retrieve all custom shipping methods configured in your store. |
| List Subscription Invoices | `listSubscriptionInvoices` | Return the invoices (recurring orders) issued for a subscription. |
| List Subscriptions | `listSubscriptions` | Retrieve a paginated list of subscriptions with optional filters for status, date range, and customer. |
| Remove Allowed Domains | `removeAllowedDomains` | Remove one or more allowed domains. Provide a JSON array of objects, each with a domain and optional protocol. |
| Update Discount | `updateDiscount` | Update an existing discount by id. Supply the fields you want to change; you can also archive the discount. |
| Update Order | `updateOrder` | Update an order's status, payment status, tracking information, addresses, notes, custom fields, or metadata. |
| Update Product Inventory | `updateProduct` | Update the inventory management settings and stock levels of a product. |
| Update Shipping Method | `updateShippingMethod` | Replace a custom shipping method by id with a new full definition. |
| Update Store Domain | `updateStoreDomain` | Change your store's default domain and optionally its protocol. |

</details>
