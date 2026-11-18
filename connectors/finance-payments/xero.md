---
description: "Xero Accounting API connector."
---

# Xero

Xero Accounting API connector. Manage contacts, invoices, credit notes, bank transactions, payments, accounts, items, quotes, purchase orders, tax rates, organisation, financial reports, currencies, and bank transfers via OAuth 2.0. Every call requires a Xero-Tenant-Id header identifying the connected organisation.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [xero.com](https://xero.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 48 |
| **Events** | 2 |
| **Slug** | `xero` |

## Use it

Add Xero from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.xero.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Account | `createAccount` | Create a new account in the chart of accounts. Xero uses PUT to create. |
| Create Bank Transaction | `createBankTransaction` | Create a spend or receive money bank transaction. Xero uses PUT to create. |
| Create Bank Transfer | `createBankTransfer` | Create a transfer of money between two bank accounts. Xero uses PUT to create. |
| Create Contact | `createContact` | Create a new contact. Xero uses PUT to create new records. |
| Create Credit Note | `createCreditNote` | Create a credit note (ACCRECCREDIT or ACCPAYCREDIT). Xero uses PUT to create. |
| Create Invoice | `createInvoice` | Create a new invoice. Type ACCREC (sales) or ACCPAY (bill). Xero uses PUT to create. |
| Create Item | `createItem` | Create a new item. Xero uses PUT to create. |
| Create Payment | `createPayment` | Apply a payment to an invoice or credit note. Xero uses PUT to create. |
| Create Purchase Order | `createPurchaseOrder` | Create a new purchase order. Xero uses PUT to create. |
| Create Quote | `createQuote` | Create a new quote. Xero uses PUT to create. |
| Delete Account | `deleteAccount` | Delete an account by AccountID. Returns 204. |
| Delete Item | `deleteItem` | Delete an item by ItemID. Returns 204. |
| Delete Payment | `deletePayment` | Delete (reverse) a payment by setting its Status to DELETED. POST to /Payments/{id}. |
| Email Invoice | `emailInvoice` | Send an invoice to the contact via email. POST with empty body to /Invoices/{id}/Email. Returns 204. |
| Get Account | `getAccount` | Retrieve a single account by AccountID. |
| Get Balance Sheet Report | `getBalanceSheet` | Retrieve the Balance Sheet report as at an optional date. |
| Get Bank Transaction | `getBankTransaction` | Retrieve a single bank transaction by BankTransactionID. |
| Get Contact | `getContact` | Retrieve a single contact by ContactID. |
| Get Credit Note | `getCreditNote` | Retrieve a single credit note by CreditNoteID. |
| Get Invoice | `getInvoice` | Retrieve a single invoice by InvoiceID or InvoiceNumber. |
| Get Item | `getItem` | Retrieve a single item by ItemID. |
| Get Organisation | `getOrganisation` | Retrieve details of the connected Xero organisation. |
| Get Payment | `getPayment` | Retrieve a single payment by PaymentID. |
| Get Profit and Loss Report | `getProfitAndLoss` | Retrieve the Profit and Loss report for an optional date range. |
| Get Purchase Order | `getPurchaseOrder` | Retrieve a single purchase order by PurchaseOrderID. |
| Get Quote | `getQuote` | Retrieve a single quote by QuoteID. |
| Get Trial Balance Report | `getTrialBalance` | Retrieve the Trial Balance report as at an optional date. |
| List Accounts | `listAccounts` | Retrieve the chart of accounts. |
| List Bank Transactions | `listBankTransactions` | Retrieve all bank transactions (spend/receive money). |
| List Bank Transfers | `listBankTransfers` | Retrieve all bank transfers between accounts. |
| List Connections | `listConnections` | List the Xero organisations (tenants) the connected access token is authorised for. Returns one entry per tenant with its tenantId, tenantName and tenantType. This is the only endpoint that yields the tenantId that every other Xero action requires in its Xero-Tenant-Id header, so call it first. |
| List Contacts | `listContacts` | Retrieve all contacts in the connected Xero organisation. Supports optional where/order/page filters. |
| List Credit Notes | `listCreditNotes` | Retrieve all credit notes. |
| List Currencies | `listCurrencies` | Retrieve all currencies set up in the organisation. |
| List Invoices | `listInvoices` | Retrieve all invoices (sales ACCREC and bills ACCPAY). Supports where/order/page filters. |
| List Items | `listItems` | Retrieve all inventory/products & services items. |
| List Payments | `listPayments` | Retrieve all payments applied to invoices and credit notes. |
| List Purchase Orders | `listPurchaseOrders` | Retrieve all purchase orders. |
| List Quotes | `listQuotes` | Retrieve all quotes. |
| List Tax Rates | `listTaxRates` | Retrieve all tax rates. |
| Update Account | `updateAccount` | Update an existing account by AccountID. Xero uses POST to update. |
| Update Bank Transaction | `updateBankTransaction` | Update a bank transaction by BankTransactionID. Xero uses POST to update. |
| Update Contact | `updateContact` | Update an existing contact by ContactID. Xero uses POST to update. |
| Update Credit Note | `updateCreditNote` | Update an existing credit note by CreditNoteID. Xero uses POST to update. |
| Update Invoice | `updateInvoice` | Update an existing invoice by InvoiceID. Xero uses POST to update. |
| Update Item | `updateItem` | Update an existing item by ItemID. Xero uses POST to update. |
| Update Purchase Order | `updatePurchaseOrder` | Update a purchase order by PurchaseOrderID. Xero uses POST to update. |
| Update Quote | `updateQuote` | Update an existing quote by QuoteID. Xero uses POST to update. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Contact Created or Updated | `CONTACT` | Fires when a contact is created or updated. eventCategory=CONTACT; eventType is CREATE or UPDATE; resourceId is the ContactID. |
| Invoice Created or Updated | `INVOICE` | Fires when an invoice is created or updated. eventCategory=INVOICE; eventType is CREATE or UPDATE; resourceId is the InvoiceID. |
