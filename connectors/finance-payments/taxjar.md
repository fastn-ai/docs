---
description: "Sales tax automation with TaxJar."
hidden: true
---

# TaxJar

<img src="../../.gitbook/assets/connectors/taxjar.png" alt="TaxJar logo" width="64">

Sales tax automation with TaxJar. Calculate sales tax for orders, record order and refund transactions, manage exempt customers, look up tax rates and nexus regions, browse product tax categories, and validate customer addresses.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [taxjar.com](https://taxjar.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `taxjar` |

## Use it

Add TaxJar from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.taxjar.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Calculate Sales Tax | `calculateSalesTax` | Calculates the sales tax to collect for an order based on its origin and destination addresses, line items, and shipping. Returns the total amount to collect plus a full rate breakdown by jurisdiction. This is a calculation only and does not record a transaction. |
| Create Customer | `createCustomer` | Creates an exempt customer in TaxJar. Once created, pass the customer_id when calculating tax or recording an order so the customer's exemption is applied automatically. |
| Create Order Transaction | `createOrderTransaction` | Records a new order transaction in TaxJar for sales tax reporting and filing. Submit the order once it is finalised, including the sales tax actually collected. |
| Create Refund Transaction | `createRefundTransaction` | Records a new refund transaction in TaxJar against an existing order, so refunded sales tax is reflected in your reports and filings. Amounts should be negative to represent money returned to the customer. |
| Delete Customer | `deleteCustomer` | Deletes an exempt customer from TaxJar by its unique identifier. Their exemption will no longer be applied to future tax calculations. |
| Delete Order Transaction | `deleteOrderTransaction` | Deletes an existing order transaction from TaxJar by its unique identifier. The order is removed from your sales tax reports. |
| Delete Refund Transaction | `deleteRefundTransaction` | Deletes an existing refund transaction from TaxJar by its unique identifier. The refund is removed from your sales tax reports. |
| List Customers | `listCustomers` | Lists the unique identifiers of all exempt customers stored in TaxJar. Use Show Customer to retrieve the full details of any returned customer. |
| List Nexus Regions | `listNexusRegions` | Lists the regions where you have nexus configured in TaxJar, meaning you are obliged to collect and remit sales tax there. |
| List Order Transactions | `listOrderTransactions` | Lists the unique identifiers of order transactions recorded in TaxJar. Filter by an exact transaction date or a date range. Either transaction_date or both from_transaction_date and to_transaction_date must be supplied. |

<details>

<summary>See 11 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Refund Transactions | `listRefundTransactions` | Lists the unique identifiers of refund transactions recorded in TaxJar. Filter by an exact transaction date or a date range. Either transaction_date or both from_transaction_date and to_transaction_date must be supplied. |
| List Tax Categories | `listTaxCategories` | Lists all product tax categories supported by TaxJar. Use the returned product_tax_code on order line items so items such as clothing, food, or software are taxed at the correct reduced or exempt rate. |
| Show Customer | `showCustomer` | Retrieves a single exempt customer from TaxJar by its unique identifier, including the exemption type and the regions where the customer is exempt. |
| Show Order Transaction | `showOrderTransaction` | Retrieves a single order transaction recorded in TaxJar by its unique identifier, including its addresses, amounts, collected sales tax, and line items. |
| Show Refund Transaction | `showRefundTransaction` | Retrieves a single refund transaction recorded in TaxJar by its unique identifier, including its addresses, refunded amounts, sales tax, and line items. |
| Show Tax Rates For Location | `showTaxRatesForLocation` | Retrieves the sales tax rates for a given location, broken down by state, county, city, and special district. Supply the street address as well for rooftop-accurate rates. |
| Summarize Tax Rates For All Regions | `summarizeTaxRates` | Retrieves the minimum and average sales tax rates for every region supported by TaxJar, giving a high-level view of rates across all states and countries. |
| Update Customer | `updateCustomer` | Updates an existing exempt customer in TaxJar, such as changing their exemption type, name, address, or the regions where they are exempt. |
| Update Order Transaction | `updateOrderTransaction` | Updates an existing order transaction in TaxJar. Only the fields you supply are sent, so you can amend individual amounts, addresses, or line items without resubmitting the whole order. |
| Update Refund Transaction | `updateRefundTransaction` | Updates an existing refund transaction in TaxJar. Only the fields you supply are sent, so you can amend individual amounts, addresses, or line items without resubmitting the whole refund. |
| Validate Address | `validateAddress` | Validates a customer address and returns a collection of matching, corrected addresses with ZIP+4 precision. Only US addresses can be validated. Requires a TaxJar Professional or higher subscription, and this endpoint is not available in the sandbox environment. |

</details>
