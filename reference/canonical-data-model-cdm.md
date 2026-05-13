---
description: >-
  Field-level specification for all 6 CDM entities — Contact, Product, Order,
  Invoice, InventoryLevel, Fulfillment — with types, requirements, and connector
  mappings.
---

# Canonical Data Model (CDM)

The CDM is Fastn's universal data format. All connectors map their native data to/from CDM entities, enabling cross-system normalization. A "customer" in Shopify becomes a CDMContact. That same CDMContact maps to a "contact" in HubSpot or a "client" in Xero.

### CDMContact

Unified customer/contact data across CRM, e-commerce, and accounting systems.

| Field          | Type       | Required | Description                                           |
| -------------- | ---------- | -------- | ----------------------------------------------------- |
| `id`           | string     | Yes      | Unique identifier                                     |
| `email`        | string     | No       | Primary email address                                 |
| `firstName`    | string     | No       | First name                                            |
| `lastName`     | string     | No       | Last name                                             |
| `company`      | string     | No       | Company or organization name                          |
| `phone`        | string     | No       | Primary phone number                                  |
| `addresses`    | Address\[] | No       | Array of postal addresses                             |
| `tags`         | string\[]  | No       | Labels or categories                                  |
| `customFields` | object     | No       | Key-value pairs for fields not in the standard schema |

**Connector mappings:**

| Connector | Native field → CDM field                                                                           |
| --------- | -------------------------------------------------------------------------------------------------- |
| Shopify   | `customer.first_name` → `firstName`, `customer.last_name` → `lastName`, `customer.email` → `email` |
| HubSpot   | `contact.firstname` → `firstName`, `contact.lastname` → `lastName`, `contact.email` → `email`      |
| Xero      | `contact.Name` → `company`, `contact.EmailAddress` → `email`                                       |
| Stripe    | `customer.name` → (split to firstName/lastName), `customer.email` → `email`                        |

### CDMProduct

Product catalog normalization across e-commerce, inventory, and ERP systems.

| Field          | Type           | Required | Description                            |
| -------------- | -------------- | -------- | -------------------------------------- |
| `id`           | string         | Yes      | Unique identifier                      |
| `name`         | string         | Yes      | Product name                           |
| `sku`          | string         | No       | Stock keeping unit                     |
| `description`  | string         | No       | Product description                    |
| `variants`     | Variant\[]     | No       | Product variations (size, color, etc.) |
| `pricingTiers` | PricingTier\[] | No       | Price levels (retail, wholesale, etc.) |
| `category`     | string         | No       | Product category or type               |
| `status`       | string         | No       | Active, draft, archived                |
| `inventory`    | object         | No       | Inventory summary (available, onHand)  |

**Connector mappings:**

| Connector | Native field → CDM field                                                                        |
| --------- | ----------------------------------------------------------------------------------------------- |
| Shopify   | `product.title` → `name`, `product.variants[].sku` → `sku`, `product.body_html` → `description` |
| Cin7 Core | `product.Name` → `name`, `product.SKU` → `sku`, `product.Category` → `category`                 |

### CDMOrder

Order data from any e-commerce or ERP system.

| Field             | Type        | Required | Description                                              |
| ----------------- | ----------- | -------- | -------------------------------------------------------- |
| `id`              | string      | Yes      | Unique identifier                                        |
| `contact`         | CDMContact  | No       | Customer who placed the order                            |
| `lineItems`       | LineItem\[] | Yes      | Products/services in the order                           |
| `totals`          | Totals      | Yes      | Subtotal, tax, shipping, discount, total                 |
| `payments`        | Payment\[]  | No       | Payment records                                          |
| `status`          | string      | Yes      | Order status (pending, processing, completed, cancelled) |
| `shippingAddress` | Address     | No       | Delivery address                                         |
| `billingAddress`  | Address     | No       | Billing address                                          |
| `currency`        | string      | No       | ISO 4217 currency code (USD, EUR, GBP)                   |
| `createdAt`       | datetime    | No       | Order creation timestamp                                 |

**Connector mappings:**

| Connector | Native field → CDM field                                                                                    |
| --------- | ----------------------------------------------------------------------------------------------------------- |
| Shopify   | `order.line_items` → `lineItems`, `order.total_price` → `totals.total`, `order.financial_status` → `status` |
| Stripe    | `invoice.lines` → `lineItems`, `invoice.total` → `totals.total`, `invoice.status` → `status`                |

### CDMInvoice

Invoice normalization across accounting systems.

| Field           | Type        | Required | Description                                |
| --------------- | ----------- | -------- | ------------------------------------------ |
| `id`            | string      | Yes      | Unique identifier                          |
| `contact`       | CDMContact  | No       | Customer or vendor                         |
| `lineItems`     | LineItem\[] | Yes      | Invoice line items                         |
| `totals`        | Totals      | Yes      | Subtotal, tax, total                       |
| `status`        | string      | Yes      | Draft, submitted, authorised, paid, voided |
| `dueDate`       | datetime    | No       | Payment due date                           |
| `payments`      | Payment\[]  | No       | Payment records applied to the invoice     |
| `currency`      | string      | Yes      | ISO 4217 currency code                     |
| `invoiceNumber` | string      | No       | Human-readable invoice number              |

**Connector mappings:**

| Connector  | Native field → CDM field                                                                                                        |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Xero       | `invoice.Contact` → `contact`, `invoice.LineItems` → `lineItems`, `invoice.Total` → `totals.total`, `invoice.Status` → `status` |
| QuickBooks | `invoice.CustomerRef` → `contact`, `invoice.Line` → `lineItems`, `invoice.TotalAmt` → `totals.total`                            |

### CDMInventoryLevel

Real-time inventory across warehouses and channels.

| Field        | Type   | Required | Description                             |
| ------------ | ------ | -------- | --------------------------------------- |
| `productId`  | string | Yes      | Reference to CDMProduct                 |
| `variantId`  | string | No       | Specific variant (size, color)          |
| `locationId` | string | No       | Warehouse or channel location           |
| `available`  | number | Yes      | Available for sale                      |
| `onHand`     | number | No       | Physically in stock (includes reserved) |
| `committed`  | number | No       | Allocated to orders but not yet shipped |
| `reserved`   | number | No       | Held for specific purposes              |

**Connector mappings:**

| Connector | Native field → CDM field                                                                |
| --------- | --------------------------------------------------------------------------------------- |
| Shopify   | `inventory_level.available` → `available`, `inventory_level.location_id` → `locationId` |
| Cin7 Core | `stock.StockOnHand` → `onHand`, `stock.Available` → `available`                         |

### CDMFulfillment

Shipping and fulfillment tracking across providers.

| Field            | Type        | Required | Description                                        |
| ---------------- | ----------- | -------- | -------------------------------------------------- |
| `id`             | string      | Yes      | Unique identifier                                  |
| `orderId`        | string      | Yes      | Reference to CDMOrder                              |
| `status`         | string      | Yes      | pending, in\_transit, delivered, failed, cancelled |
| `trackingNumber` | string      | No       | Carrier tracking number                            |
| `carrier`        | string      | No       | Shipping carrier name                              |
| `lineItems`      | LineItem\[] | No       | Items included in this fulfillment                 |
| `shippedAt`      | datetime    | No       | Shipment date                                      |
| `deliveredAt`    | datetime    | No       | Delivery date                                      |

**Connector mappings:**

| Connector | Native field → CDM field                                                                                                      |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Shopify   | `fulfillment.tracking_number` → `trackingNumber`, `fulfillment.tracking_company` → `carrier`, `fulfillment.status` → `status` |
| Cin7 Omni | `shipment.TrackingNo` → `trackingNumber`, `shipment.Carrier` → `carrier`                                                      |

### Shared types

#### Address

| Field        | Type   | Description             |
| ------------ | ------ | ----------------------- |
| `line1`      | string | Street address          |
| `line2`      | string | Apartment, suite, unit  |
| `city`       | string | City                    |
| `state`      | string | State or province       |
| `postalCode` | string | ZIP or postal code      |
| `country`    | string | ISO 3166-1 country code |
| `company`    | string | Company name at address |

#### LineItem

| Field        | Type   | Description                                                 |
| ------------ | ------ | ----------------------------------------------------------- |
| `productId`  | string | Reference to CDMProduct                                     |
| `name`       | string | Item description                                            |
| `quantity`   | number | Quantity ordered                                            |
| `unitPrice`  | string | Price per unit (string, not float — for currency precision) |
| `totalPrice` | string | Line total                                                  |
| `sku`        | string | SKU if available                                            |

#### Totals

| Field      | Type   | Description             |
| ---------- | ------ | ----------------------- |
| `subtotal` | string | Before tax and shipping |
| `tax`      | string | Tax amount              |
| `shipping` | string | Shipping cost           |
| `discount` | string | Discount applied        |
| `total`    | string | Final total             |

{% hint style="info" %}
**Note:** Currency values are strings, not floats. This avoids floating-point precision issues. The Type Coercer handles conversion between string and numeric representations. See [Transformation Engine](https://docs.fastn.ai/~/revisions/aj5eaS57qHvafrgYtfbL/reference/transformation-engine).
{% endhint %}
