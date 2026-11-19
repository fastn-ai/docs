---
description: "TaxJar automates sales tax. Calculate sales tax, record order and refund transactions, and manage exempt customers."
hidden: true
---

# TaxJar

<img src="../../.gitbook/assets/connectors/lg/taxjar.png" alt="TaxJar logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [taxjar.com](https://taxjar.com) |
| **Authentication** | API token |
| **Slug** | `taxjar` |

## Setup

Your customers enter their API token for TaxJar when they connect. Nothing else needs setting up.

## Use it

Add TaxJar from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.taxjar.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Calculate Sales Tax</td><td><code>calculateSalesTax</code></td><td>Calculates the sales tax to collect for an order based on its origin and destination addresses, line items, and shipping. Returns the total amount to collect plus a full rate breakdown by jurisdiction. This is a calculation only and does not record a transaction.</td></tr><tr><td>Create Customer</td><td><code>createCustomer</code></td><td>Creates an exempt customer in TaxJar. Once created, pass the customer_id when calculating tax or recording an order so the customer's exemption is applied automatically.</td></tr><tr><td>Create Order Transaction</td><td><code>createOrderTransaction</code></td><td>Records a new order transaction in TaxJar for sales tax reporting and filing. Submit the order once it is finalised, including the sales tax actually collected.</td></tr><tr><td>Create Refund Transaction</td><td><code>createRefundTransaction</code></td><td>Records a new refund transaction in TaxJar against an existing order, so refunded sales tax is reflected in your reports and filings. Amounts should be negative to represent money returned to the customer.</td></tr><tr><td>Delete Customer</td><td><code>deleteCustomer</code></td><td>Deletes an exempt customer from TaxJar by its unique identifier. Their exemption will no longer be applied to future tax calculations.</td></tr><tr><td>Delete Order Transaction</td><td><code>deleteOrderTransaction</code></td><td>Deletes an existing order transaction from TaxJar by its unique identifier. The order is removed from your sales tax reports.</td></tr><tr><td>Delete Refund Transaction</td><td><code>deleteRefundTransaction</code></td><td>Deletes an existing refund transaction from TaxJar by its unique identifier. The refund is removed from your sales tax reports.</td></tr><tr><td>List Customers</td><td><code>listCustomers</code></td><td>Lists the unique identifiers of all exempt customers stored in TaxJar. Use Show Customer to retrieve the full details of any returned customer.</td></tr><tr><td>List Nexus Regions</td><td><code>listNexusRegions</code></td><td>Lists the regions where you have nexus configured in TaxJar, meaning you are obliged to collect and remit sales tax there.</td></tr><tr><td>List Order Transactions</td><td><code>listOrderTransactions</code></td><td>Lists the unique identifiers of order transactions recorded in TaxJar. Filter by an exact transaction date or a date range. Either transaction_date or both from_transaction_date and to_transaction_date must be supplied.</td></tr></tbody></table>

<details>

<summary>View 11 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Refund Transactions</td><td><code>listRefundTransactions</code></td><td>Lists the unique identifiers of refund transactions recorded in TaxJar. Filter by an exact transaction date or a date range. Either transaction_date or both from_transaction_date and to_transaction_date must be supplied.</td></tr><tr><td>List Tax Categories</td><td><code>listTaxCategories</code></td><td>Lists all product tax categories supported by TaxJar. Use the returned product_tax_code on order line items so items such as clothing, food, or software are taxed at the correct reduced or exempt rate.</td></tr><tr><td>Show Customer</td><td><code>showCustomer</code></td><td>Retrieves a single exempt customer from TaxJar by its unique identifier, including the exemption type and the regions where the customer is exempt.</td></tr><tr><td>Show Order Transaction</td><td><code>showOrderTransaction</code></td><td>Retrieves a single order transaction recorded in TaxJar by its unique identifier, including its addresses, amounts, collected sales tax, and line items.</td></tr><tr><td>Show Refund Transaction</td><td><code>showRefundTransaction</code></td><td>Retrieves a single refund transaction recorded in TaxJar by its unique identifier, including its addresses, refunded amounts, sales tax, and line items.</td></tr><tr><td>Show Tax Rates For Location</td><td><code>showTaxRatesForLocation</code></td><td>Retrieves the sales tax rates for a given location, broken down by state, county, city, and special district. Supply the street address as well for rooftop-accurate rates.</td></tr><tr><td>Summarize Tax Rates For All Regions</td><td><code>summarizeTaxRates</code></td><td>Retrieves the minimum and average sales tax rates for every region supported by TaxJar, giving a high-level view of rates across all states and countries.</td></tr><tr><td>Update Customer</td><td><code>updateCustomer</code></td><td>Updates an existing exempt customer in TaxJar, such as changing their exemption type, name, address, or the regions where they are exempt.</td></tr><tr><td>Update Order Transaction</td><td><code>updateOrderTransaction</code></td><td>Updates an existing order transaction in TaxJar. Only the fields you supply are sent, so you can amend individual amounts, addresses, or line items without resubmitting the whole order.</td></tr><tr><td>Update Refund Transaction</td><td><code>updateRefundTransaction</code></td><td>Updates an existing refund transaction in TaxJar. Only the fields you supply are sent, so you can amend individual amounts, addresses, or line items without resubmitting the whole refund.</td></tr><tr><td>Validate Address</td><td><code>validateAddress</code></td><td>Validates a customer address and returns a collection of matching, corrected addresses with ZIP+4 precision. Only US addresses can be validated. Requires a TaxJar Professional or higher subscription, and this endpoint is not available in the sandbox environment.</td></tr></tbody></table>

</details>

## Events

TaxJar has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
