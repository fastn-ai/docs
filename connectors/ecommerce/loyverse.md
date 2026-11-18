---
description: "Loyverse is a point-of-sale and retail management platform for small businesses."
hidden: true
---

# Loyverse

<img src="../../.gitbook/assets/connectors/lg/loyverse.png" alt="Loyverse logo">

Loyverse is a point-of-sale and retail management platform for small businesses. This connector covers the full Loyverse API: merchant and store information, items, variants, categories, modifiers, discounts and taxes, inventory levels, customers, suppliers, employees, payment types, POS devices, receipts and refunds, shifts, and webhook subscriptions.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [loyverse.com](https://loyverse.com) |
| **Authentication** | Bearer token |
| **Slug** | `loyverse` |

## Use it

Add Loyverse from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.loyverse.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Or Update Category | `createOrUpdateCategory` | Creates an item category, or updates an existing one. This endpoint is an upsert: supplying the identifier of an existing category updates it, and omitting the identifier creates a new one. |
| Create Or Update Customer | `createOrUpdateCustomer` | Creates a customer in the loyalty database, or updates an existing one. This endpoint is an upsert: supplying the identifier of an existing customer updates it, and omitting the identifier creates a new one. Loyalty points, visit counts and total spend are maintained by Loyverse from receipts and cannot be written here. |
| Create Or Update Discount | `createOrUpdateDiscount` | Creates a discount, or updates an existing one. This endpoint is an upsert: supplying the identifier of an existing discount updates it, and omitting the identifier creates a new one. Supply the amount only for fixed-amount discounts and the percentage only for fixed-percent discounts; variable discounts take their value at the till. |
| Create Or Update Item | `createOrUpdateItem` | Creates an item in the product catalogue, or updates an existing one. This endpoint is an upsert: supplying the identifier of an existing item updates it, and omitting the identifier creates a new one. Creating an item without a variants list gives it one auto-generated variant with a sequential SKU. Note two Loyverse constraints: the option names cannot be added to or removed from an item that already has variants, and the request field is modifiers_ids while the response field is modifier_ids. |
| Create Or Update Modifier | `createOrUpdateModifier` | Creates a modifier with its options, or updates an existing one. This endpoint is an upsert: supplying the identifier of an existing modifier updates it, and omitting the identifier creates a new one. The options list replaces the modifier's existing options, so send the full set every time. |
| Create Or Update POS Device | `createOrUpdatePosDevice` | Registers a POS device against a store, or updates an existing one. This endpoint is an upsert: supplying the identifier of an existing device updates it, and omitting the identifier creates a new one. A newly created device is inactive until it is paired with a physical till in the Loyverse app. |
| Create Or Update Supplier | `createOrUpdateSupplier` | Creates a supplier, or updates an existing one. This endpoint is an upsert: supplying the identifier of an existing supplier updates it, and omitting the identifier creates a new one. |
| Create Or Update Tax | `createOrUpdateTax` | Creates a tax, or updates an existing one. This endpoint is an upsert: supplying the identifier of an existing tax updates it, and omitting the identifier creates a new one. |
| Create Or Update Variant | `createOrUpdateVariant` | Creates a variant on an existing item, or updates an existing variant. This endpoint is an upsert: supplying the identifier of an existing variant updates it, and omitting the identifier adds a new variant to the given item. Adding a variant requires the parent item to already define the matching option names. |
| Create Or Update Webhook | `createOrUpdateWebhook` | Subscribes a URL to a Loyverse event, or updates an existing subscription. This endpoint is an upsert: supplying the identifier of an existing webhook updates it, and omitting the identifier creates a new one. Loyverse then POSTs the event payload to your URL whenever that event occurs. |

<details>

<summary>See 47 more actions</summary>

* **Create Receipt** `createReceipt`: Records a completed sale in Loyverse, exactly as if it had been rung up on a till. This is a real financial transaction: it appears in sales reports, decrements tracked stock, awards loyalty points and cannot be deleted - only refunded. Use it to push sales in from another channel, never to test connectivity.
* **Create Refund** `createRefund`: Issues a refund against an existing sales receipt, returning money to the customer. This is a real financial transaction: it appears in sales reports, returns tracked stock and reverses loyalty points, and it cannot be undone. Refund only the lines you mean to, identified by their line item identifiers from the original receipt.
* **Delete Category** `deleteCategory`: Deletes an item category. Items already assigned to the category are left in place but lose their category.
* **Delete Customer** `deleteCustomer`: Deletes a customer from the loyalty database. Loyverse schedules the record for permanent deletion rather than removing it instantly, which is reflected in the customer's permanent deletion date.
* **Delete Discount** `deleteDiscount`: Deletes a discount so it can no longer be applied at the POS.
* **Delete Item** `deleteItem`: Deletes an item and all of its variants from the product catalogue. Receipts that already reference the item keep their historical record.
* **Delete Item Image** `deleteItemImage`: Removes the picture attached to an item, leaving the item itself in place.
* **Delete Modifier** `deleteModifier`: Deletes a modifier and all of its options, removing it from the items that used it.
* **Delete POS Device** `deletePosDevice`: Removes a POS device registration. The physical till is unpaired and can no longer take sales under this device.
* **Delete Supplier** `deleteSupplier`: Deletes a supplier from the merchant's supplier list.
* **Delete Tax** `deleteTax`: Deletes a tax. Items that referenced the tax stop having it applied at the till.
* **Delete Variant** `deleteVariant`: Deletes a single item variant. An item must keep at least one variant, so deleting its only variant is rejected - delete the item instead.
* **Delete Webhook** `deleteWebhook`: Removes a webhook subscription so Loyverse stops sending that event to the target URL.
* **Get Category** `getCategory`: Returns a single item category by its identifier.
* **Get Customer** `getCustomer`: Returns a single customer by their identifier, including loyalty points, total spend and visit history.
* **Get Discount** `getDiscount`: Returns a single discount by its identifier, with its type, value and store availability.
* **Get Employee** `getEmployee`: Returns a single employee by their identifier, with the stores they are assigned to.
* **Get Item** `getItem`: Returns a single item by its identifier, with all of its variants and their per-store pricing.
* **Get Merchant** `getMerchant`: Returns information about the Loyverse merchant account the access token belongs to, including the business name, contact email, country and the currency all money amounts in the API are expressed in.
* **Get Modifier** `getModifier`: Returns a single modifier by its identifier, including all of its options and their prices.
* **Get Payment Type** `getPaymentType`: Returns a single payment type by its identifier, including which stores accept it.
* **Get POS Device** `getPosDevice`: Returns a single POS device by its identifier, with its store and activation state.
* **Get Receipt** `getReceipt`: Returns a single receipt by its receipt number, with its line items, taxes, discounts and payments. Note that receipts are addressed by receipt number rather than by a UUID.
* **Get Shift** `getShift`: Returns a single till shift by its identifier, with its cash reconciliation figures and the cash movements recorded during it.
* **Get Store** `getStore`: Returns a single store by its identifier, with its address and contact details.
* **Get Supplier** `getSupplier`: Returns a single supplier by its identifier, with full contact and address details.
* **Get Tax** `getTax`: Returns a single tax by its identifier, with its rate and per-store settings.
* **Get Variant** `getVariant`: Returns a single item variant by its identifier, with its SKU, barcode, cost and per-store pricing.
* **Get Webhook** `getWebhook`: Returns a single webhook subscription by its identifier, showing its target URL, event type and whether it is currently enabled.
* **List Categories** `listCategories`: Returns the item categories defined for the merchant, each with its display colour.
* **List Customers** `listCustomers`: Returns the customers in the merchant's loyalty database, with their contact details, loyalty points and visit history.
* **List Discounts** `listDiscounts`: Returns the discounts configured for the merchant, with their type, value and which stores they are available in.
* **List Employees** `listEmployees`: Returns the employees of the merchant, with the stores they work at and their assigned POS access. Employee identifiers appear on receipts and shifts.
* **List Inventory Levels** `listInventoryLevels`: Returns current stock levels per item variant per store. Only variants belonging to items with stock tracking enabled appear here.
* **List Items** `listItems`: Returns the items in the product catalogue, each with its variants, taxes, modifiers and per-store pricing.
* **List Modifiers** `listModifiers`: Returns the modifiers defined for the merchant, each with its options. Modifiers are the add-ons and variations offered at the till, such as extra shot or choice of sauce.
* **List Payment Types** `listPaymentTypes`: Returns the payment types configured for the merchant, such as cash and card. Payment type identifiers are required when recording the payments on a sales receipt.
* **List POS Devices** `listPosDevices`: Returns the POS devices registered for the merchant, showing which store each is connected to and whether it has been activated against a physical till.
* **List Receipts** `listReceipts`: Returns sales and refund receipts, each with its line items, taxes, discounts and payments. This is the record of what was actually sold, and is the usual starting point for reporting or accounting syncs.
* **List Shifts** `listShifts`: Returns till shifts, each covering the period between a cash drawer being opened and closed, with the opening and closing amounts and the cash movements recorded during it.
* **List Stores** `listStores`: Returns the stores belonging to the merchant, with their addresses and contact details. Store identifiers are needed by most other resources, such as inventory, receipts and POS devices.
* **List Suppliers** `listSuppliers`: Returns the suppliers defined for the merchant, with their contact and address details. The list is sorted by creation time with the most recent suppliers first.
* **List Taxes** `listTaxes`: Returns the taxes configured for the merchant, with their rates, type and which stores they apply in.
* **List Variants** `listVariants`: Returns item variants across the catalogue, each with its SKU, barcode, cost and per-store pricing. Variants are the sellable units referenced by inventory levels and receipt line items.
* **List Webhooks** `listWebhooks`: Returns the webhooks registered for the merchant. Loyverse only returns webhooks created by the same application as the access token making the request, so this will not show subscriptions made by other integrations.
* **Update Inventory Levels** `updateInventoryLevels`: Sets the stock level for one or more item variants at a store. The value you supply is the resulting stock, not a delta, so read the current level first if you mean to adjust it. This writes directly to live inventory and immediately changes what the tills will sell.
* **Upload Item Image** `uploadItemImage`: Uploads a picture for an item, shown on its POS tile. Loyverse expects the raw PNG bytes as the request body. Note that fastn's HTTP executor cannot currently send raw binary bodies without corrupting non-UTF-8 bytes, so this action is not usable for real image uploads from fastn today - set the item's Image URL through Create Or Update Item instead, or upload the picture in the Loyverse Back Office.

</details>
