---
description: "Wafeq is cloud accounting software for the Middle East."
hidden: true
---

# Wafeq

<img src="../../.gitbook/assets/connectors/lg/wafeq.png" alt="Wafeq logo">

Wafeq is cloud accounting software for the Middle East. This connector wraps the Wafeq Public API v1: invoices, simplified invoices, bills, quotes, purchase orders, credit and debit notes, payments, payment requests, expenses, contacts, items, accounts, bank accounts and transactions, manual journals, journal line items, employees, payslips, projects, cost centers, branches, warehouses, custom fields, files, tax rates, units of measure, amortizations, revenue recognitions and financial reports.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [wafeq.com](https://wafeq.com) |
| **Authentication** | API key, OAuth 2.0 |
| **Slug** | `wafeq` |

## Use it

Add Wafeq from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.wafeq.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Apply credit note to invoice | `invoiceCreditNotesCreate` | Apply credit note to invoice. Apply an amount of a credit note to an invoice of the same customer and currency. Both documents must be posted. The application posts a journal entry on its date, which defaults to the credit note's date and must fall in an open period, and lowers the balance of both documents. A credit note can be applied to the same invoice more than once. |
| Apply debit note to bill | `billDebitNotesCreate` | Apply debit note to bill. Apply an amount of a debit note to a bill of the same supplier and currency. Both documents must be posted. The application posts a journal entry on its date, which defaults to the debit note's date and must fall in an open period, and lowers the balance of both documents. A debit note can be applied to the same bill more than once. |
| Balance Sheet | `reportsBalanceSheetList` | Balance Sheet . Generate balance sheet report in `currency` at `date` with `period_count` periods to compare and group it by `group_by` parameter. |
| Cash Flow | `reportsCashFlowList` | Cash Flow . Generate cash flow report in `currency` from `date_after` to `date_before` range and group it by `group_by` parameter. |
| Convert purchase order to bill | `purchaseOrdersBillCreate` | Convert purchase order to bill. This endpoint can be used to convert a purchase order to a draft bill. |
| Convert quote to invoice | `quotesInvoiceCreate` | Convert quote to invoice. This endpoint can be used to convert a quote to an invoice. |
| Create Account | `accountsCreate` | Create account. Endpoint for creating a new account. |
| Create Bank Account | `bankAccountsCreate` | Create bank account. Endpoint for creating a new bank account. |
| Create Bank Ledger Transaction | `bankAccountsLedgerTransactionsCreate` | Create bank ledger transaction. Endpoint for creating a new bank ledger transaction. |
| Create Bank Statement Transaction | `bankAccountsStatementTransactionsCreate` | Create bank statement transaction. Endpoint for creating a new bank statement transaction. |
| Create Beneficiary | `beneficiariesCreate` | Create beneficiary. Endpoint for creating a new beneficiary. |
| Create Bill | `billsCreate` | Create bill. Endpoint for creating a new bill. |
| Create Bill Line Item | `billsLineItemsCreate` | Create bill line item. Endpoint for creating a new bill line item. |
| Create Branch | `branchesCreate` | Create branch. Endpoint for creating a new branch. |
| Create Contact | `contactsCreate` | Create contact. Endpoint for creating a new contact. |
| Create Cost Center | `costCentersCreate` | Create cost center. Endpoint for creating a new cost center. |
| Create Credit Note | `creditNotesCreate` | Create credit note. Endpoint for creating a new credit note. |
| Create Credit Note Line Item | `creditNotesLineItemsCreate` | Create credit note line item. Endpoint for creating a new credit note line item. |
| Create Custom Field | `customFieldsCreate` | Create custom field. Endpoint for creating a new custom field. |
| Create Debit Note | `debitNotesCreate` | Create debit note. Endpoint for creating a new debit note. |
| Create Debit Note Line Item | `debitNotesLineItemsCreate` | Create debit note line item. Endpoint for creating a new debit note line item. |
| Create Employee | `employeesCreate` | Create employee. Endpoint for creating a new employee. |
| Create Expense | `expensesCreate` | Create expense. Endpoint for creating a new expense. |
| Create file | `uploadFile` | Create file. Endpoint for creating a new file. Upload a file using multipart/form-data. |
| Create file (advance) | `uploadFileRaw` | Create file (advance). Create file in advance mode by sending raw binary file content directly in the request body. You must include a Content-Disposition header with the filename. |
| Create invoice | `invoicesCreate` | Create invoice. Endpoint for creating a new invoice. |
| Create invoice line item | `invoicesLineItemsCreate` | Create invoice line item. Endpoint for creating a new invoice line item. |
| Create item | `itemsCreate` | Create item. Endpoint for creating a new item. |
| Create item unit of measure | `itemUnitsOfMeasureCreate` | Create item unit of measure. Endpoint for creating a new item unit of measure. |
| Create manual journal | `manualJournalsCreate` | Create manual journal. Endpoint for creating a new manual journal. |
| Create pay item | `payslipsPayItemsCreate` | Create pay item. Endpoint for creating a new pay item. |
| Create payment | `paymentsCreate` | Create payment. Endpoint for creating a new payment. |
| Create payment request | `paymentRequestsCreate` | Create payment request. Endpoint for creating a new payment request. |
| Create payslip | `payslipsCreate` | Create payslip. Endpoint for creating a new payslip. |
| Create project | `projectsCreate` | Create project. Endpoint for creating a new project. |
| Create purchase order | `purchaseOrdersCreate` | Create purchase order. Endpoint for creating a new purchase order. |
| Create purchase order line item | `purchaseOrdersLineItemsCreate` | Create purchase order line item. Endpoint for creating a new purchase order line item. |
| Create quote | `quotesCreate` | Create quote. Endpoint for creating a new quote. |
| Create quote line item | `quotesLineItemsCreate` | Create quote line item. Endpoint for creating a new quote line item. |
| Create simplified invoice | `simplifiedInvoicesCreate` | Create simplified invoice. Endpoint for creating a new simplified invoice. |
| Create simplified invoice line item | `simplifiedInvoicesLineItemsCreate` | Create simplified invoice line item. Endpoint for creating a new simplified invoice line item. |
| Create unit of measure | `unitsOfMeasureCreate` | Create unit of measure. Endpoint for creating a new unit of measure. |
| Create warehouse | `warehousesCreate` | Create warehouse. Endpoint for creating a new warehouse. |
| Delete Account | `accountsDestroy` | Delete account. Endpoint for deleting an existing account. |
| Delete Amortization | `amortizationsDestroy` | Delete amortization. Endpoint for deleting an existing amortization. |
| Delete Bank Account | `bankAccountsDestroy` | Delete bank account. Endpoint for deleting an existing bank account. |
| Delete Bank Ledger Transaction | `bankAccountsLedgerTransactionsDestroy` | Delete bank ledger transaction. Endpoint for deleting an existing bank ledger transaction. |
| Delete Bank Statement Transaction | `bankAccountsStatementTransactionsDestroy` | Delete bank statement transaction. Endpoint for deleting an existing bank statement transaction. |
| Delete Beneficiary | `beneficiariesDestroy` | Delete beneficiary. Endpoint for deleting an existing beneficiary. |
| Delete Bill | `billsDestroy` | Delete bill. Endpoint for deleting an existing bill. |
| Delete Bill Line Item | `billsLineItemsDestroy` | Delete bill line item. Endpoint for deleting an existing bill line item. |
| Delete Branch | `branchesDestroy` | Delete branch. Endpoint for deleting an existing branch. |
| Delete Contact | `contactsDestroy` | Delete contact. Endpoint for deleting an existing contact. |
| Delete Cost Center | `costCentersDestroy` | Delete cost center. Endpoint for deleting an existing cost center. |
| Delete Credit Note | `creditNotesDestroy` | Delete credit note. Endpoint for deleting an existing credit note. |
| Delete Credit Note Line Item | `creditNotesLineItemsDestroy` | Delete credit note line item. Endpoint for deleting an existing credit note line item. |
| Delete Custom Field | `customFieldsDestroy` | Delete custom field. Endpoint for deleting an existing custom field. The custom field must not be in use on any documents. |
| Delete Debit Note | `debitNotesDestroy` | Delete debit note. Endpoint for deleting an existing debit note. |
| Delete Debit Note Line Item | `debitNotesLineItemsDestroy` | Delete debit note line item. Endpoint for deleting an existing debit note line item. |
| Delete Employee | `employeesDestroy` | Delete employee. Endpoint for deleting an existing employee. |
| Delete Expense | `expensesDestroy` | Delete expense. Endpoint for deleting an existing expense. |
| Delete file | `filesDestroy` | Delete file. Endpoint for deleting an existing file. |
| Delete invoice | `invoicesDestroy` | Delete invoice. Endpoint for deleting an existing invoice. |
| Delete invoice line item | `invoicesLineItemsDestroy` | Delete invoice line item. Endpoint for deleting an existing invoice line item. |
| Delete item | `itemsDestroy` | Delete item. Endpoint for deleting an existing item. |
| Delete item unit of measure | `itemUnitsOfMeasureDestroy` | Delete item unit of measure. Endpoint for deleting an existing item unit of measure. |
| Delete manual journal | `manualJournalsDestroy` | Delete manual journal. Endpoint for deleting an existing manual journal. |
| Delete pay item | `payslipsPayItemsDestroy` | Delete pay item. Endpoint for deleting an existing pay item. |
| Delete payment | `paymentsDestroy` | Delete payment. Endpoint for deleting an existing payment. |
| Delete payment request | `paymentRequestsDestroy` | Delete payment request. Endpoint for deleting an existing payment request. |
| Delete payslip | `payslipsDestroy` | Delete payslip. Endpoint for deleting an existing payslip. |
| Delete project | `projectsDestroy` | Delete project. Endpoint for deleting an existing project. |
| Delete purchase order | `purchaseOrdersDestroy` | Delete purchase order. Endpoint for deleting an existing purchase order. |
| Delete purchase order line item | `purchaseOrdersLineItemsDestroy` | Delete purchase order line item. Endpoint for deleting an existing purchase order line item. |
| Delete quote | `quotesDestroy` | Delete quote. Endpoint for deleting an existing quote. |
| Delete quote line item | `quotesLineItemsDestroy` | Delete quote line item. Endpoint for deleting an existing quote line item. |
| Delete revenue recognition | `revenueRecognitionsDestroy` | Delete revenue recognition. Endpoint for deleting an existing revenue recognition. |
| Delete simplified invoice | `simplifiedInvoicesDestroy` | Delete simplified invoice. Endpoint for deleting an existing simplified invoice. |
| Delete simplified invoice line item | `simplifiedInvoicesLineItemsDestroy` | Delete simplified invoice line item. Endpoint for deleting an existing simplified invoice line item. |
| Delete unit of measure | `unitsOfMeasureDestroy` | Delete unit of measure. Endpoint for deleting an existing unit of measure. |
| Delete warehouse | `warehousesDestroy` | Delete warehouse. Endpoint for deleting an existing warehouse. |
| Download Bill PDF | `billsDownloadRetrieve` | Download bill PDF. Endpoint for downloading a PDF of the bill. |
| Download Credit Note PDF | `creditNotesDownloadRetrieve` | Download credit note PDF. Endpoint for downloading a PDF of the credit note. |
| Download Debit Note PDF | `debitNotesDownloadRetrieve` | Download debit note PDF. Endpoint for downloading a PDF of the debit note. |
| Download invoice PDF | `invoicesDownloadRetrieve` | Download invoice PDF. Endpoint for downloading a PDF of the invoice. |
| Download payment PDF | `paymentsDownloadRetrieve` | Download payment PDF. Endpoint for downloading a PDF of the payment. |
| Download payslip PDF | `payslipsDownloadRetrieve` | Download payslip PDF. Endpoint for downloading a PDF of the payslip. |
| Download purchase order PDF | `purchaseOrdersDownloadRetrieve` | Download purchase order PDF. Endpoint for downloading a PDF of the purchase order. |
| Download quote PDF | `quotesDownloadRetrieve` | Download quote PDF. Endpoint for downloading a PDF of the quote. |
| Download simplified invoice PDF | `simplifiedInvoicesDownloadRetrieve` | Download simplified invoice PDF. Endpoint for downloading a PDF of the simplified invoice. |
| End Amortization Early | `amortizationsEndEarlyCreate` | End amortization early. Endpoint for terminating an amortization early, recognizing the remaining balance against the provided account. |
| End revenue recognition early | `revenueRecognitionsEndEarlyCreate` | End revenue recognition early. Endpoint for terminating a revenue recognition early, recognizing the remaining balance against the provided account. |
| List Accounts | `accountsList` | List accounts. Endpoint for retrieving a list of accounts. |
| List Amortizations | `amortizationsList` | List amortizations. Endpoint for retrieving a list of amortizations. |
| List Bank Accounts | `bankAccountsList` | List bank accounts. Endpoint for retrieving a list of bank accounts. |
| List Bank Ledger Transactions | `bankAccountsLedgerTransactionsList` | List bank ledger transactions. Endpoint for retrieving a list of bank ledger transactions. |
| List Bank Statement Transactions | `bankAccountsStatementTransactionsList` | List bank statement transactions. Endpoint for retrieving a list of bank statement transactions. |
| List Beneficiaries | `beneficiariesList` | List beneficiaries. Endpoint for retrieving a list of beneficiaries. |
| List Bill Line Items | `billsLineItemsList` | List bill line items. Endpoint for retrieving a list of bill line items. |
| List Bills | `billsList` | List bills. Endpoint for retrieving a list of bills. |
| List Branches | `branchesList` | List branches. Endpoint for retrieving a list of branches. |
| List Contacts | `contactsList` | List contacts. Endpoint for retrieving a list of contacts. |
| List Cost Centers | `costCentersList` | List cost centers. Endpoint for retrieving a list of cost centers. |
| List Credit Note Line Items | `creditNotesLineItemsList` | List credit note line items. Endpoint for retrieving a list of credit note line items. |
| List Credit Notes | `creditNotesList` | List credit notes. Endpoint for retrieving a list of credit notes. |
| List Custom Fields | `customFieldsList` | List custom fields. Endpoint for retrieving a list of custom fields. |
| List Debit Note Line Items | `debitNotesLineItemsList` | List debit note line items. Endpoint for retrieving a list of debit note line items. |
| List Debit Notes | `debitNotesList` | List debit notes. Endpoint for retrieving a list of debit notes. |
| List Employees | `employeesList` | List employees. Endpoint for retrieving a list of employees. |
| List expense reports | `expenseReportsList` | List expense reports. Endpoint for retrieving a list of expense reports. |
| List Expenses | `expensesList` | List expenses. Endpoint for retrieving a list of expenses. |
| List files | `filesList` | List files. Endpoint for retrieving a list of files. |
| List invoice line items | `invoicesLineItemsList` | List invoice line items. Endpoint for retrieving a list of invoice line items. |
| List invoices | `invoicesList` | List invoices. Endpoint for retrieving a list of invoices. |
| List item unit of measures | `itemUnitsOfMeasureList` | List item unit of measures. Endpoint for retrieving a list of item unit of measures. |
| List items | `itemsList` | List items. Endpoint for retrieving a list of items. |
| List journal line items | `journalLineItemsList` | List journal line items. Endpoint for retrieving a list of journal line items. |
| List manual journals | `manualJournalsList` | List manual journals. Endpoint for retrieving a list of manual journals. |
| List pay items | `payslipsPayItemsList` | List pay items. Endpoint for retrieving a list of pay items. |
| List payment requests | `paymentRequestsList` | List payment requests. Endpoint for retrieving a list of payment requests. |
| List payments | `paymentsList` | List payments. Endpoint for retrieving a list of payments. |
| List payslips | `payslipsList` | List payslips. Endpoint for retrieving a list of payslips. |
| List projects | `projectsList` | List projects. Endpoint for retrieving a list of projects. |
| List purchase order line items | `purchaseOrdersLineItemsList` | List purchase order line items. Endpoint for retrieving a list of purchase order line items. |
| List purchase orders | `purchaseOrdersList` | List purchase orders. Endpoint for retrieving a list of purchase orders. |
| List quote line items | `quotesLineItemsList` | List quote line items. Endpoint for retrieving a list of quote line items. |
| List quotes | `quotesList` | List quotes. Endpoint for retrieving a list of quotes. |
| List revenue recognitions | `revenueRecognitionsList` | List revenue recognitions. Endpoint for retrieving a list of revenue recognitions. |
| List simplified invoice line items | `simplifiedInvoicesLineItemsList` | List simplified invoice line items. Endpoint for retrieving a list of simplified invoice line items. |
| List simplified invoices | `simplifiedInvoicesList` | List simplified invoices. Endpoint for retrieving a list of simplified invoices. |
| List tax rates | `taxRatesList` | List tax rates. Endpoint for retrieving a list of tax rates. |
| List unit of measures | `unitsOfMeasureList` | List unit of measures. Endpoint for retrieving a list of unit of measures. |
| List warehouses | `warehousesList` | List warehouses. Endpoint for retrieving a list of warehouses. |
| Mark Expense as Draft | `expensesMarkAsDraftCreate` | Mark expense as draft. Moves a posted expense back to draft (removes its journal from the ledger). |
| Mark Expense as Posted | `expensesMarkAsPostedCreate` | Mark expense as posted. Posts a draft expense to the ledger (generates its journal). |
| Partial Update Employee | `employeesPartialUpdate` | Partial update employee. Endpoint for partially updating an existing employee. |
| Partial Update Expense | `expensesPartialUpdate` | Partial update expense. Endpoint for partially updating an existing expense. |
| Partial update invoice | `invoicesPartialUpdate` | Partial update invoice. Endpoint for partially updating an existing invoice. |
| Partial update invoice line item | `invoicesLineItemsPartialUpdate` | Partial update invoice line item. Endpoint for partially updating an existing invoice line item. |
| Partial update item | `itemsPartialUpdate` | Partial update item. Endpoint for partially updating an existing item. |
| Partial update item unit of measure | `itemUnitsOfMeasurePartialUpdate` | Partial update item unit of measure. Endpoint for partially updating an existing item unit of measure. |
| Partial update manual journal | `manualJournalsPartialUpdate` | Partial update manual journal. Endpoint for partially updating an existing manual journal. |
| Partial update pay item | `payslipsPayItemsPartialUpdate` | Partial update pay item. Endpoint for partially updating an existing pay item. |
| Partial update payment | `paymentsPartialUpdate` | Partial update payment. Endpoint for partially updating an existing payment. |
| Partial update payment request | `paymentRequestsPartialUpdate` | Partial update payment request. Endpoint for partially updating an existing payment request. |
| Partial update payslip | `payslipsPartialUpdate` | Partial update payslip. Endpoint for partially updating an existing payslip. |
| Partial update project | `projectsPartialUpdate` | Partial update project. Endpoint for partially updating an existing project. |
| Partial update purchase order | `purchaseOrdersPartialUpdate` | Partial update purchase order. Endpoint for partially updating an existing purchase order. |
| Partial update purchase order line item | `purchaseOrdersLineItemsPartialUpdate` | Partial update purchase order line item. Endpoint for partially updating an existing purchase order line item. |
| Partial update quote | `quotesPartialUpdate` | Partial update quote. Endpoint for partially updating an existing quote. |
| Partial update quote line item | `quotesLineItemsPartialUpdate` | Partial update quote line item. Endpoint for partially updating an existing quote line item. |
| Partial update simplified invoice | `simplifiedInvoicesPartialUpdate` | Partial update simplified invoice. Endpoint for partially updating an existing simplified invoice. |
| Partial update simplified invoice line item | `simplifiedInvoicesLineItemsPartialUpdate` | Partial update simplified invoice line item. Endpoint for partially updating an existing simplified invoice line item. |
| Partial update unit of measure | `unitsOfMeasurePartialUpdate` | Partial update unit of measure. Endpoint for partially updating an existing unit of measure. |
| Partial update warehouse | `warehousesPartialUpdate` | Partial update warehouse. Endpoint for partially updating an existing warehouse. |
| Partially Update Account | `accountsPartialUpdate` | Partial update account. Endpoint for partially updating an existing account. |
| Partially Update Bank Account | `bankAccountsPartialUpdate` | Partial update bank account. Endpoint for partially updating an existing bank account. |
| Partially Update Bank Ledger Transaction | `bankAccountsLedgerTransactionsPartialUpdate` | Partial update bank ledger transaction. Endpoint for partially updating an existing bank ledger transaction. |
| Partially Update Bank Statement Transaction | `bankAccountsStatementTransactionsPartialUpdate` | Partial update bank statement transaction. Endpoint for partially updating an existing bank statement transaction. |
| Partially Update Beneficiary | `beneficiariesPartialUpdate` | Partial update beneficiary. Endpoint for partially updating an existing beneficiary. |
| Partially Update Bill | `billsPartialUpdate` | Partial update bill. Endpoint for partially updating an existing bill. |
| Partially Update Bill Line Item | `billsLineItemsPartialUpdate` | Partial update bill line item. Endpoint for partially updating an existing bill line item. |
| Partially Update Branch | `branchesPartialUpdate` | Partial update branch. Endpoint for partially updating an existing branch. |
| Partially Update Contact | `contactsPartialUpdate` | Partial update contact. Endpoint for partially updating an existing contact. |
| Partially Update Cost Center | `costCentersPartialUpdate` | Partial update cost center. Endpoint for partially updating an existing cost center. |
| Partially Update Credit Note | `creditNotesPartialUpdate` | Partial update credit note. Endpoint for partially updating an existing credit note. |
| Partially Update Credit Note Line Item | `creditNotesLineItemsPartialUpdate` | Partial update credit note line item. Endpoint for partially updating an existing credit note line item. |
| Partially Update Custom Field | `customFieldsPartialUpdate` | Partial update custom field. Endpoint for partially updating an existing custom field. |
| Partially Update Debit Note | `debitNotesPartialUpdate` | Partial update debit note. Endpoint for partially updating an existing debit note. |
| Partially Update Debit Note Line Item | `debitNotesLineItemsPartialUpdate` | Partial update debit note line item. Endpoint for partially updating an existing debit note line item. |
| Preview a revenue recognition schedule | `revenueRecognitionsPreviewCreate` | Preview the revenue recognition schedule (POST /revenue-recognitions/preview/) without saving it. Docs: https://developer.wafeq.com/reference/revenue_recognitions_preview_create |
| Preview Amortization Early Termination | `amortizationsPreviewEndEarlyCreate` | Preview early termination. Endpoint for previewing the remaining balance and the posted events that would be reversed by terminating the amortization early at the given date. |
| Preview Amortization Schedule | `amortizationsPreviewCreate` | Preview the amortization events that would be generated for a given schedule, without creating an amortization. Read-only - nothing is posted. |
| Preview early termination | `revenueRecognitionsPreviewEndEarlyCreate` | Preview early termination. Endpoint for previewing the remaining balance and the posted events that would be reversed by terminating the revenue recognition early at the given date. |
| Profit and Loss | `reportsProfitAndLossList` | Profit and Loss . Generate profit and loss report in `currency` from `date_after` to `date_before` range and group it by `group_by` parameter. |
| Reconcile bank statement transaction | `bankAccountsStatementTransactionsReconcileCreate` | Reconcile bank statement transaction. Reconcile this bank statement transaction against existing bank-side journal lines. Payments and adjustments must already exist. The linked total must equal the statement amount. Repeating the complete set of existing matches is safe. Returns the bank statement transaction with is_posted set to true. |
| Report Credit Note to Tax Authority | `creditNotesTaxAuthorityReportCreate` | Report credit note to tax authority. Report the credit note to the tax authority for processing and validation. A `PENDING` status means the submission was accepted and the tax authority's verdict is still outstanding. The credit note is issued and can no longer be edited. Retrieve the credit note to read the final status. A concurrent report or retry returns HTTP 409 with code `report_in_progress`; refresh the document before deciding whether to retry. |
| Report invoice to tax authority | `invoicesTaxAuthorityReportCreate` | Report invoice to tax authority. Report the invoice to the tax authority for processing and validation. A `PENDING` status means the submission was accepted and the tax authority's verdict is still outstanding. The invoice is issued and can no longer be edited. Retrieve the invoice to read the final status. A concurrent report or retry returns HTTP 409 with code `report_in_progress`; refresh the document before deciding whether to retry. |
| Report simplified invoice to tax authority | `simplifiedInvoicesTaxAuthorityReportCreate` | Report simplified invoice to tax authority. Report the simplified invoice to the tax authority for processing and validation. A `PENDING` status means the submission was accepted and the tax authority's verdict is still outstanding. The simplified invoice is issued and can no longer be edited. Retrieve the simplified invoice to read the final status. A concurrent report or retry returns HTTP 409 with code `report_in_progress`; refresh the document before deciding whether to retry. |
| Retrieve Account | `accountsRetrieve` | Retrieve account. Endpoint for retrieving a single account. |
| Retrieve Amortization | `amortizationsRetrieve` | Retrieve amortization. Endpoint for retrieving a single amortization. |
| Retrieve Bank Account | `bankAccountsRetrieve` | Retrieve bank account. Endpoint for retrieving a single bank account. |
| Retrieve Bank Ledger Transaction | `bankAccountsLedgerTransactionsRetrieve` | Retrieve bank ledger transaction. Endpoint for retrieving a single bank ledger transaction. |
| Retrieve Bank Statement Transaction | `bankAccountsStatementTransactionsRetrieve` | Retrieve bank statement transaction. Endpoint for retrieving a single bank statement transaction. |
| Retrieve Beneficiary | `beneficiariesRetrieve` | Retrieve beneficiary. Endpoint for retrieving a single beneficiary. |
| Retrieve Bill | `billsRetrieve` | Retrieve bill. Endpoint for retrieving a single bill. |
| Retrieve Bill Line Item | `billsLineItemsRetrieve` | Retrieve bill line item. Endpoint for retrieving a single bill line item. |
| Retrieve Branch | `branchesRetrieve` | Retrieve branch. Endpoint for retrieving a single branch. |
| Retrieve Contact | `contactsRetrieve` | Retrieve contact. Endpoint for retrieving a single contact. |
| Retrieve Cost Center | `costCentersRetrieve` | Retrieve cost center. Endpoint for retrieving a single cost center. |
| Retrieve Credit Note | `creditNotesRetrieve` | Retrieve credit note. Endpoint for retrieving a single credit note. |
| Retrieve credit note application | `invoiceCreditNotesRetrieve` | Retrieve credit note application. Retrieve one application of a credit note to an invoice. An invoice lists its applications in `credit_notes`. |
| Retrieve Credit Note Line Item | `creditNotesLineItemsRetrieve` | Retrieve credit note line item. Endpoint for retrieving a single credit note line item. |
| Retrieve Custom Field | `customFieldsRetrieve` | Retrieve custom field. Endpoint for retrieving a single custom field. |
| Retrieve Debit Note | `debitNotesRetrieve` | Retrieve debit note. Endpoint for retrieving a single debit note. |
| Retrieve debit note application | `billDebitNotesRetrieve` | Retrieve debit note application. Retrieve one application of a debit note to a bill. A bill lists its applications in `debit_notes`. |
| Retrieve Debit Note Line Item | `debitNotesLineItemsRetrieve` | Retrieve debit note line item. Endpoint for retrieving a single debit note line item. |
| Retrieve Employee | `employeesRetrieve` | Retrieve employee. Endpoint for retrieving a single employee. |
| Retrieve Expense | `expensesRetrieve` | Retrieve expense. Endpoint for retrieving a single expense. |
| Retrieve expense report | `expenseReportsRetrieve` | Retrieve expense report. Endpoint for retrieving a single expense report. |
| Retrieve file | `filesRetrieve` | Retrieve file. Endpoint for retrieving a single file. |
| Retrieve invoice | `invoicesRetrieve` | Retrieve invoice. Endpoint for retrieving a single invoice. |
| Retrieve invoice line item | `invoicesLineItemsRetrieve` | Retrieve invoice line item. Endpoint for retrieving a single invoice line item. |
| Retrieve item | `itemsRetrieve` | Retrieve item. Endpoint for retrieving a single item. |
| Retrieve item unit of measure | `itemUnitsOfMeasureRetrieve` | Retrieve item unit of measure. Endpoint for retrieving a single item unit of measure. |
| Retrieve journal line item | `journalLineItemsRetrieve` | Retrieve journal line item. Endpoint for retrieving a single journal line item. |
| Retrieve manual journal | `manualJournalsRetrieve` | Retrieve manual journal. Endpoint for retrieving a single manual journal. |
| Retrieve organization | `organizationRetrieve` | Retrieve organization. Endpoint for retrieving a single organization. |
| Retrieve organization profile | `organizationProfileRetrieve` | Retrieve organization profile. Retrieve the current organization profile using an organization API key or an admin OAuth scope. |
| Retrieve pay item | `payslipsPayItemsRetrieve` | Retrieve pay item. Endpoint for retrieving a single pay item. |
| Retrieve payment | `paymentsRetrieve` | Retrieve payment. Endpoint for retrieving a single payment. |
| Retrieve payment request | `paymentRequestsRetrieve` | Retrieve payment request. Endpoint for retrieving a single payment request. |
| Retrieve payslip | `payslipsRetrieve` | Retrieve payslip. Endpoint for retrieving a single payslip. |
| Retrieve project | `projectsRetrieve` | Retrieve project. Endpoint for retrieving a single project. |
| Retrieve purchase order | `purchaseOrdersRetrieve` | Retrieve purchase order. Endpoint for retrieving a single purchase order. |
| Retrieve purchase order line item | `purchaseOrdersLineItemsRetrieve` | Retrieve purchase order line item. Endpoint for retrieving a single purchase order line item. |
| Retrieve quote | `quotesRetrieve` | Retrieve quote. Endpoint for retrieving a single quote. |
| Retrieve quote line item | `quotesLineItemsRetrieve` | Retrieve quote line item. Endpoint for retrieving a single quote line item. |
| Retrieve revenue recognition | `revenueRecognitionsRetrieve` | Retrieve revenue recognition. Endpoint for retrieving a single revenue recognition. |
| Retrieve simplified invoice | `simplifiedInvoicesRetrieve` | Retrieve simplified invoice. Endpoint for retrieving a single simplified invoice. |
| Retrieve simplified invoice line item | `simplifiedInvoicesLineItemsRetrieve` | Retrieve simplified invoice line item. Endpoint for retrieving a single simplified invoice line item. |
| Retrieve unit of measure | `unitsOfMeasureRetrieve` | Retrieve unit of measure. Endpoint for retrieving a single unit of measure. |
| Retrieve warehouse | `warehousesRetrieve` | Retrieve warehouse. Endpoint for retrieving a single warehouse. |
| Trial Balance | `reportsTrialBalanceList` | Trial Balance . Generate trial balance report from `from_date` to `to_date` optionally with PNL openings `with_pnl_openings` and accounts with zero balances `include_zero_balances`. |
| Unapply credit note from invoice | `invoiceCreditNotesDestroy` | Unapply credit note from invoice. Unapply a credit note from an invoice. The application and its journal entry are removed, and the balance of both documents is restored. An application dated in a closed period cannot be removed. |
| Unapply debit note from bill | `billDebitNotesDestroy` | Unapply debit note from bill. Unapply a debit note from a bill. The application and its journal entry are removed, and the balance of both documents is restored. An application dated in a closed period cannot be removed. |
| Update Account | `accountsUpdate` | Update account. Endpoint for updating an existing account. |
| Update Bank Account | `bankAccountsUpdate` | Update bank account. Endpoint for updating an existing bank account. |
| Update Bank Ledger Transaction | `bankAccountsLedgerTransactionsUpdate` | Update bank ledger transaction. Endpoint for updating an existing bank ledger transaction. |
| Update Bank Statement Transaction | `bankAccountsStatementTransactionsUpdate` | Update bank statement transaction. Endpoint for updating an existing bank statement transaction. |
| Update Beneficiary | `beneficiariesUpdate` | Update beneficiary. Endpoint for updating an existing beneficiary. |
| Update Bill | `billsUpdate` | Update bill. Endpoint for updating an existing bill. |
| Update Bill Line Item | `billsLineItemsUpdate` | Update bill line item. Endpoint for updating an existing bill line item. |
| Update Branch | `branchesUpdate` | Update branch. Endpoint for updating an existing branch. |
| Update Contact | `contactsUpdate` | Update contact. Endpoint for updating an existing contact. |
| Update Cost Center | `costCentersUpdate` | Update cost center. Endpoint for updating an existing cost center. |
| Update Credit Note | `creditNotesUpdate` | Update credit note. Endpoint for updating an existing credit note. |
| Update credit note application | `invoiceCreditNotesPartialUpdate` | Update credit note application. Change the amount or date of an application in place. Its journal entry is updated rather than replaced. The credit note and invoice cannot change: to move an application, delete it and create another. |
| Update Credit Note Line Item | `creditNotesLineItemsUpdate` | Update credit note line item. Endpoint for updating an existing credit note line item. |
| Update Custom Field | `customFieldsUpdate` | Update custom field. Endpoint for updating an existing custom field. |
| Update Debit Note | `debitNotesUpdate` | Update debit note. Endpoint for updating an existing debit note. |
| Update debit note application | `billDebitNotesPartialUpdate` | Update debit note application. Change the amount or date of an application in place. Its journal entry is updated rather than replaced. The debit note and bill cannot change: to move an application, delete it and create another. |
| Update Debit Note Line Item | `debitNotesLineItemsUpdate` | Update debit note line item. Endpoint for updating an existing debit note line item. |
| Update Employee | `employeesUpdate` | Update employee. Endpoint for updating an existing employee. |
| Update Expense | `expensesUpdate` | Update expense. Endpoint for updating an existing expense. |
| Update invoice | `invoicesUpdate` | Update invoice. Endpoint for updating an existing invoice. |
| Update invoice line item | `invoicesLineItemsUpdate` | Update invoice line item. Endpoint for updating an existing invoice line item. |
| Update item | `itemsUpdate` | Update item. Endpoint for updating an existing item. |
| Update item unit of measure | `itemUnitsOfMeasureUpdate` | Update item unit of measure. Endpoint for updating an existing item unit of measure. |
| Update manual journal | `manualJournalsUpdate` | Update manual journal. Endpoint for updating an existing manual journal. |
| Update organization profile | `organizationProfilePartialUpdate` | Update organization profile. Update the current organization profile using an organization API key or an admin OAuth scope. Country and base currency are immutable; updates are disabled while ZATCA is enabled. |
| Update pay item | `payslipsPayItemsUpdate` | Update pay item. Endpoint for updating an existing pay item. |
| Update payment | `paymentsUpdate` | Update payment. Endpoint for updating an existing payment. |
| Update payment request | `paymentRequestsUpdate` | Update payment request. Endpoint for updating an existing payment request. |
| Update payslip | `payslipsUpdate` | Update payslip. Endpoint for updating an existing payslip. |
| Update project | `projectsUpdate` | Update project. Endpoint for updating an existing project. |
| Update purchase order | `purchaseOrdersUpdate` | Update purchase order. Endpoint for updating an existing purchase order. |
| Update purchase order line item | `purchaseOrdersLineItemsUpdate` | Update purchase order line item. Endpoint for updating an existing purchase order line item. |
| Update quote | `quotesUpdate` | Update quote. Endpoint for updating an existing quote. |
| Update quote line item | `quotesLineItemsUpdate` | Update quote line item. Endpoint for updating an existing quote line item. |
| Update simplified invoice | `simplifiedInvoicesUpdate` | Update simplified invoice. Endpoint for updating an existing simplified invoice. |
| Update simplified invoice line item | `simplifiedInvoicesLineItemsUpdate` | Update simplified invoice line item. Endpoint for updating an existing simplified invoice line item. |
| Update unit of measure | `unitsOfMeasureUpdate` | Update unit of measure. Endpoint for updating an existing unit of measure. |
| Update warehouse | `warehousesUpdate` | Update warehouse. Endpoint for updating an existing warehouse. |
