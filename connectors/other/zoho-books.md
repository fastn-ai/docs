---
description: "Zoho Books cloud accounting and invoicing platform."
---

# Zoho Books

Zoho Books cloud accounting and invoicing platform. Manage organizations, contacts (customers/vendors), contact persons, items, estimates, sales orders, invoices, recurring invoices, delivery challans, retainer invoices, credit notes, customer payments, expenses, recurring expenses, purchase orders, bills, recurring bills, vendor credits, vendor payments, bank accounts, bank transactions, chart of accounts, journals, projects, users, price lists, currencies, taxes, and opening balances via the Zoho Books REST API v3 (books.zoho.com/api/v3). OAuth 2.0 authorization code auth via the shared Zoho API Console app.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [books.zoho.com](https://books.zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 122 |
| **Events** | 0 |
| **Slug** | `zohoBooks` |

## Use it

Add Zoho Books from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoBooks.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Project | `activateProject` | Mark a project as active in Zoho Books. |
| Create Bank Account | `createBankAccount` | Create a bank or credit card account in Zoho Books. |
| Create Bank Transaction | `createBankTransaction` | Create a manual transaction (deposit/withdrawal) for a bank account in Zoho Books. |
| Create Bill | `createBill` | Create a vendor bill in Zoho Books. |
| Create Chart Of Account | `createChartOfAccount` | Create a new account in the chart of accounts in Zoho Books. |
| Create Contact | `createContact` | Create a customer or vendor contact in Zoho Books. |
| Create Contact Person | `createContactPerson` | Add a new contact person to an existing contact in Zoho Books. |
| Create Credit Note | `createCreditNote` | Create a credit note for a customer in Zoho Books. |
| Create Currency | `createCurrency` | Add a new currency to a Zoho Books organization. |
| Create Customer Payment | `createCustomerPayment` | Record a payment received from a customer against one or more invoices in Zoho Books. |
| Create Estimate | `createEstimate` | Create an estimate/quote for a customer in Zoho Books. |
| Create Expense | `createExpense` | Record an expense in Zoho Books. |
| Create Invoice | `createInvoice` | Create an invoice for a customer in Zoho Books. |
| Create Item | `createItem` | Create an inventory or service item in Zoho Books. |
| Create Journal | `createJournal` | Create a manual journal entry (double-entry accounting) in Zoho Books. |
| Create Organization | `createOrganization` | Create a new organization (business) in Zoho Books. |
| Create Project | `createProject` | Create a project for a customer in Zoho Books. |
| Create Purchase Order | `createPurchaseOrder` | Create a purchase order for a vendor in Zoho Books. |
| Create Recurring Invoice | `createRecurringInvoice` | Create a recurring invoice profile for a customer in Zoho Books. |
| Create Sales Order | `createSalesOrder` | Create a sales order for a customer in Zoho Books. |
| Create Tax | `createTax` | Create a tax rate in Zoho Books. |
| Create Vendor Credit | `createVendorCredit` | Create a vendor credit in Zoho Books. |
| Create Vendor Payment | `createVendorPayment` | Record a payment made to a vendor against one or more bills in Zoho Books. |
| Delete Bank Account | `deleteBankAccount` | Delete a bank account from Zoho Books. |
| Delete Bank Transaction | `deleteBankTransaction` | Delete a bank transaction from Zoho Books. |
| Delete Bill | `deleteBill` | Delete a vendor bill from Zoho Books. |
| Delete Chart Of Account | `deleteChartOfAccount` | Delete a chart-of-accounts entry from Zoho Books. |
| Delete Contact | `deleteContact` | Delete a contact (customer or vendor) from Zoho Books. |
| Delete Contact Person | `deleteContactPerson` | Delete a contact person from Zoho Books. |
| Delete Credit Note | `deleteCreditNote` | Delete a credit note from Zoho Books. |
| Delete Currency | `deleteCurrency` | Delete a currency from Zoho Books. |
| Delete Customer Payment | `deleteCustomerPayment` | Delete a customer payment from Zoho Books. |
| Delete Estimate | `deleteEstimate` | Delete an estimate from Zoho Books. |
| Delete Expense | `deleteExpense` | Delete an expense from Zoho Books. |
| Delete Invoice | `deleteInvoice` | Delete an invoice from Zoho Books. |
| Delete Item | `deleteItem` | Delete an item from Zoho Books. |
| Delete Journal | `deleteJournal` | Delete a manual journal entry from Zoho Books. |
| Delete Project | `deleteProject` | Delete a project from Zoho Books. |
| Delete Purchase Order | `deletePurchaseOrder` | Delete a purchase order from Zoho Books. |
| Delete Recurring Invoice | `deleteRecurringInvoice` | Delete a recurring invoice profile from Zoho Books. |
| Delete Sales Order | `deleteSalesOrder` | Delete a sales order from Zoho Books. |
| Delete Tax | `deleteTax` | Delete a tax rate from Zoho Books. |
| Delete User | `deleteUser` | Remove a user from a Zoho Books organization. |
| Delete Vendor Credit | `deleteVendorCredit` | Delete a vendor credit from Zoho Books. |
| Delete Vendor Payment | `deleteVendorPayment` | Delete a vendor payment from Zoho Books. |
| Get Bank Account | `getBankAccount` | Get details of a single bank account by account_id. |
| Get Bill | `getBill` | Get details of a single vendor bill by bill_id. |
| Get Chart Of Account | `getChartOfAccount` | Get details of a single chart-of-accounts entry by account_id. |
| Get Contact | `getContact` | Get details of a single contact (customer or vendor) by contact_id. |
| Get Credit Note | `getCreditNote` | Get details of a single credit note by creditnote_id. |
| Get Currency | `getCurrency` | Get details of a single currency by currency_id. |
| Get Current User | `getCurrentUser` | Get the currently authenticated user's details in Zoho Books. |
| Get Customer Payment | `getCustomerPayment` | Get details of a single customer payment by payment_id. |
| Get Estimate | `getEstimate` | Get details of a single estimate by estimate_id. |
| Get Expense | `getExpense` | Get details of a single expense by expense_id. |
| Get Invoice | `getInvoice` | Get details of a single invoice by invoice_id. |
| Get Item | `getItem` | Get details of a single item by item_id. |
| Get Journal | `getJournal` | Get details of a single manual journal entry by journal_id. |
| Get Organization | `getOrganization` | Get details of a single Zoho Books organization by its organization_id. |
| Get Project | `getProject` | Get details of a single project by project_id. |
| Get Purchase Order | `getPurchaseOrder` | Get details of a single purchase order by purchaseorder_id. |
| Get Recurring Invoice | `getRecurringInvoice` | Get details of a single recurring invoice profile. |
| Get Sales Order | `getSalesOrder` | Get details of a single sales order by salesorder_id. |
| Get Tax | `getTax` | Get details of a single tax by tax_id. |
| Get Vendor Credit | `getVendorCredit` | Get details of a single vendor credit by vendor_credit_id. |
| Get Vendor Payment | `getVendorPayment` | Get details of a single vendor payment by payment_id. |
| Invite User | `inviteUser` | Invite a new user to a Zoho Books organization. |
| List Bank Accounts | `listBankAccounts` | List bank and credit card accounts in a Zoho Books organization. |
| List Bank Transactions | `listBankTransactions` | List transactions for a bank account in Zoho Books. |
| List Bills | `listBills` | List vendor bills in a Zoho Books organization. |
| List Chart Of Accounts | `listChartOfAccounts` | List the chart of accounts in a Zoho Books organization. |
| List Contact Persons | `listContactPersons` | List all contact persons across contacts, or for a specific contact, in Zoho Books. |
| List Contacts | `listContacts` | List customers and vendors (contacts) in a Zoho Books organization, with optional filters. |
| List Credit Notes | `listCreditNotes` | List credit notes in a Zoho Books organization. |
| List Currencies | `listCurrencies` | List currencies configured in a Zoho Books organization. |
| List Customer Payments | `listCustomerPayments` | List payments received from customers in a Zoho Books organization. |
| List Estimates | `listEstimates` | List estimates/quotes in a Zoho Books organization. |
| List Expenses | `listExpenses` | List expenses in a Zoho Books organization. |
| List Invoices | `listInvoices` | List invoices in a Zoho Books organization, with optional filters. |
| List Items | `listItems` | List inventory/service items in a Zoho Books organization. |
| List Journals | `listJournals` | List manual journal entries in a Zoho Books organization. |
| List Organizations | `listOrganizations` | List all organizations the connected user has access to in Zoho Books. Use this to obtain organization_id, which is required on every other action. |
| List Projects | `listProjects` | List projects in a Zoho Books organization. |
| List Purchase Orders | `listPurchaseOrders` | List purchase orders in a Zoho Books organization. |
| List Recurring Invoices | `listRecurringInvoices` | List recurring invoice profiles in a Zoho Books organization. |
| List Sales Orders | `listSalesOrders` | List sales orders in a Zoho Books organization. |
| List Taxes | `listTaxes` | List taxes configured in a Zoho Books organization. |
| List Users | `listUsers` | List users in a Zoho Books organization. |
| List Vendor Credits | `listVendorCredits` | List vendor credits (debit notes) in a Zoho Books organization. |
| List Vendor Payments | `listVendorPayments` | List payments made to vendors in a Zoho Books organization. |
| Mark Contact Active | `markContactActive` | Mark a contact as active in Zoho Books. |
| Mark Contact Inactive | `markContactInactive` | Mark a contact as inactive in Zoho Books. |
| Mark Estimate As Sent | `markEstimateSent` | Mark a draft estimate as sent in Zoho Books. |
| Mark Invoice As Sent | `markInvoiceSent` | Mark a draft invoice as sent in Zoho Books. |
| Mark Purchase Order As Open | `markPurchaseOrderOpen` | Mark a draft purchase order as open in Zoho Books. |
| Mark Sales Order As Open | `markSalesOrderOpen` | Mark a draft sales order as open in Zoho Books. |
| Resume Recurring Invoice | `resumeRecurringInvoice` | Resume a stopped recurring invoice profile in Zoho Books. |
| Stop Recurring Invoice | `stopRecurringInvoice` | Stop a recurring invoice profile in Zoho Books. |
| Update Bank Account | `updateBankAccount` | Update an existing bank account in Zoho Books. |
| Update Bill | `updateBill` | Update an existing vendor bill in Zoho Books. |
| Update Chart Of Account | `updateChartOfAccount` | Update an existing chart-of-accounts entry in Zoho Books. |
| Update Contact | `updateContact` | Update an existing contact (customer or vendor) in Zoho Books. |
| Update Contact Person | `updateContactPerson` | Update an existing contact person in Zoho Books. |
| Update Credit Note | `updateCreditNote` | Update an existing credit note in Zoho Books. |
| Update Currency | `updateCurrency` | Update an existing currency's code, symbol, price precision and display format in Zoho Books. Exchange rates are not part of this request; Zoho Books manages them through the separate currency exchange rates endpoint. |
| Update Customer Payment | `updateCustomerPayment` | Update an existing customer payment in Zoho Books. |
| Update Estimate | `updateEstimate` | Update an existing estimate in Zoho Books. |
| Update Expense | `updateExpense` | Update an existing expense in Zoho Books. |
| Update Invoice | `updateInvoice` | Update an existing invoice in Zoho Books. When the invoice has already been marked as sent or is open, Zoho Books requires an audit reason for the change. |
| Update Item | `updateItem` | Update an existing item in Zoho Books. |
| Update Journal | `updateJournal` | Update an existing manual journal entry in Zoho Books. |
| Update Organization | `updateOrganization` | Update an existing Zoho Books organization's profile settings. |
| Update Project | `updateProject` | Update an existing project in Zoho Books. |
| Update Purchase Order | `updatePurchaseOrder` | Update an existing purchase order in Zoho Books. |
| Update Sales Order | `updateSalesOrder` | Update an existing sales order in Zoho Books. |
| Update Tax | `updateTax` | Update an existing tax rate in Zoho Books. |
| Update User | `updateUser` | Update an existing user's details in Zoho Books. |
| Update Vendor Payment | `updateVendorPayment` | Update an existing vendor payment in Zoho Books. |
| Void Bill | `voidBill` | Void a vendor bill in Zoho Books. |
| Void Credit Note | `voidCreditNote` | Void a credit note in Zoho Books. |
| Void Invoice | `voidInvoice` | Void an invoice in Zoho Books. |
| Void Vendor Credit | `voidVendorCredit` | Void a vendor credit in Zoho Books. |
