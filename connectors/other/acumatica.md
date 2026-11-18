---
description: "Acumatica Cloud ERP contract-based REST API."
hidden: true
---

# Acumatica

Acumatica Cloud ERP contract-based REST API. Access StockItem, NonStockItem, Customer, Vendor, SalesOrder, PurchaseOrder, Invoice, Bill, Payment, Shipment, InventoryReceipt, InventoryIssue, Account, JournalTransaction, Contact, Lead, Case, Project entities. Base URL: https://{instance}/entity/Default/{endpointVersion}. Auth via login session cookie (POST /entity/auth/login) or OAuth2.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [acumatica.com](https://acumatica.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Actions** | 112 |
| **Events** | 14 |
| **Slug** | `acumatica` |

## Use it

Add Acumatica from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.acumatica.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create/Update Account | `putAccount` | Create or update a GL Account (PUT). Fields use the {value:...} wrapper. |
| Create/Update Bill | `putBill` | Create or update an AP Bill (PUT). Fields use the {value:...} wrapper. |
| Create/Update Business Account | `putBusinessAccount` | Create or update a BusinessAccount (PUT). Fields use the {value:...} wrapper. |
| Create/Update Case | `putCase` | Create or update a Case (PUT). Fields use the {value:...} wrapper. |
| Create/Update Contact | `putContact` | Create or update a Contact (PUT). Fields use the {value:...} wrapper. |
| Create/Update Customer | `putCustomer` | Create or update a Customer (PUT). Fields use the {value:...} wrapper. |
| Create/Update Employee | `putEmployee` | Create or update an Employee (PUT). Fields use the {value:...} wrapper. |
| Create/Update Inventory Issue | `putInventoryIssue` | Create or update an InventoryIssue (PUT). Fields use the {value:...} wrapper. |
| Create/Update Inventory Receipt | `putInventoryReceipt` | Create or update an InventoryReceipt (PUT). Fields use the {value:...} wrapper. |
| Create/Update Invoice | `putInvoice` | Create or update an AR Invoice (PUT). Fields use the {value:...} wrapper. |
| Create/Update Journal Transaction | `putJournalTransaction` | Create or update a GL JournalTransaction batch (PUT). Fields use the {value:...} wrapper. |
| Create/Update Lead | `putLead` | Create or update a Lead (PUT). Fields use the {value:...} wrapper. |
| Create/Update Non-Stock Item | `putNonStockItem` | Create or update a NonStockItem (PUT). Fields use the {value:...} wrapper. |
| Create/Update Payment | `putPayment` | Create or update an AR Payment (PUT). Fields use the {value:...} wrapper. |
| Create/Update Project | `putProject` | Create or update a Project (PUT). Fields use the {value:...} wrapper. |
| Create/Update Purchase Order | `putPurchaseOrder` | Create or update a PurchaseOrder (PUT). Fields use the {value:...} wrapper. |
| Create/Update Sales Invoice | `putSalesInvoice` | Create or update a SalesInvoice (PUT). Fields use the {value:...} wrapper. |
| Create/Update Sales Order | `putSalesOrder` | Create or update a SalesOrder (PUT). Use $expand on the URL when you want detail lines returned. Fields use the {value:...} wrapper. |
| Create/Update Shipment | `putShipment` | Create or update a Shipment (PUT). Fields use the {value:...} wrapper. |
| Create/Update Stock Item | `putStockItem` | Create or update a StockItem record (PUT to entity). Fields use the Acumatica {value:...} wrapper. If InventoryID matches an existing record it is updated, otherwise created. |
| Create/Update Vendor | `putVendor` | Create or update a Vendor (PUT). Fields use the {value:...} wrapper. |
| Create/Update Warehouse | `putWarehouse` | Create or update a Warehouse (PUT). Fields use the {value:...} wrapper. |
| Delete Account By Keys | `deleteAccount` | Delete a GL Account by AccountCD key. Returns 204. |
| Delete Bill By Keys | `deleteBill` | Delete an AP Bill by composite keys Type/ReferenceNbr. Returns 204. |
| Delete Case By Keys | `deleteCase` | Delete a Case by CaseID key. Returns 204. |
| Delete Contact By Keys | `deleteContact` | Delete a Contact by ContactID key. Returns 204. |
| Delete Customer By Keys | `deleteCustomer` | Delete a Customer by CustomerID key. Returns 204. |
| Delete Inventory Issue By Keys | `deleteInventoryIssue` | Delete an InventoryIssue by ReferenceNbr key. Returns 204. |
| Delete Inventory Receipt By Keys | `deleteInventoryReceipt` | Delete an InventoryReceipt by ReferenceNbr key. Returns 204. |
| Delete Invoice By Keys | `deleteInvoice` | Delete an AR Invoice by composite keys Type/ReferenceNbr. Returns 204. |
| Delete Journal Transaction By Keys | `deleteJournalTransaction` | Delete a JournalTransaction batch by composite keys Module/BatchNbr. Returns 204. |
| Delete Lead By Keys | `deleteLead` | Delete a Lead by LeadID key. Returns 204. |
| Delete Non-Stock Item By Keys | `deleteNonStockItem` | Delete a NonStockItem by InventoryID key. Returns 204. |
| Delete Payment By Keys | `deletePayment` | Delete a Payment by composite keys Type/ReferenceNbr. Returns 204. |
| Delete Project By Keys | `deleteProject` | Delete a Project by ProjectID key. Returns 204. |
| Delete Purchase Order By Keys | `deletePurchaseOrder` | Delete a PurchaseOrder by composite keys OrderType/OrderNbr. Returns 204. |
| Delete Sales Order By Keys | `deleteSalesOrder` | Delete a SalesOrder by composite keys OrderType/OrderNbr. Returns 204. |
| Delete Shipment By Keys | `deleteShipment` | Delete a Shipment by ShipmentNbr key. Returns 204. |
| Delete Stock Item By Keys | `deleteStockItem` | Delete a StockItem by key field (InventoryID). Returns 204 No Content on success. |
| Delete Vendor By Keys | `deleteVendor` | Delete a Vendor by VendorID key. Returns 204. |
| Get Account By ID | `getAccountById` | Retrieve a single GL Account by internal GUID id. |
| Get Account By Keys | `getAccount` | Retrieve a single GL Account by AccountCD key. |
| Get Bill By ID | `getBillById` | Retrieve a single AP Bill by internal GUID id. |
| Get Bill By Keys | `getBill` | Retrieve a single AP Bill by composite keys Type/ReferenceNbr. |
| Get Business Account By ID | `getBusinessAccountById` | Retrieve a single BusinessAccount by its system id (GUID). Supports $expand, $select. |
| Get Business Account By Keys | `getBusinessAccount` | Retrieve a single BusinessAccount by key field (BusinessAccountID). Supports $expand, $select. |
| Get Case By ID | `getCaseById` | Retrieve a single Case by internal GUID id. |
| Get Case By Keys | `getCase` | Retrieve a single Case by CaseID key. |
| Get Contact By ID | `getContactById` | Retrieve a single Contact by internal GUID id. |
| Get Contact By Keys | `getContact` | Retrieve a single Contact by ContactID key. |
| Get Customer By ID | `getCustomerById` | Retrieve a single Customer by internal GUID id. |
| Get Customer By Keys | `getCustomer` | Retrieve a single Customer by CustomerID key. Supports $expand and $select. |
| Get Employee By ID | `getEmployeeById` | Retrieve a single Employee by its system id (GUID). Supports $expand, $select. |
| Get Employee By Keys | `getEmployee` | Retrieve a single Employee by key field (EmployeeID). Supports $expand, $select. |
| Get Inventory Issue By ID | `getInventoryIssueById` | Retrieve a single InventoryIssue by internal GUID id. |
| Get Inventory Issue By Keys | `getInventoryIssue` | Retrieve a single InventoryIssue by ReferenceNbr key. |
| Get Inventory Receipt By ID | `getInventoryReceiptById` | Retrieve a single InventoryReceipt by internal GUID id. |
| Get Inventory Receipt By Keys | `getInventoryReceipt` | Retrieve a single InventoryReceipt by ReferenceNbr key. |
| Get Invoice By ID | `getInvoiceById` | Retrieve a single AR Invoice by internal GUID id. |
| Get Invoice By Keys | `getInvoice` | Retrieve a single AR Invoice by composite keys Type/ReferenceNbr. |
| Get Journal Transaction By ID | `getJournalTransactionById` | Retrieve a single JournalTransaction by internal GUID id. |
| Get Journal Transaction By Keys | `getJournalTransaction` | Retrieve a single JournalTransaction batch by composite keys Module/BatchNbr. |
| Get Lead By ID | `getLeadById` | Retrieve a single Lead by internal GUID id. |
| Get Lead By Keys | `getLead` | Retrieve a single Lead by LeadID key. |
| Get Non-Stock Item By ID | `getNonStockItemById` | Retrieve a single NonStockItem by internal GUID id. |
| Get Non-Stock Item By Keys | `getNonStockItem` | Retrieve a single NonStockItem by InventoryID key. Supports $expand and $select. |
| Get Payment By ID | `getPaymentById` | Retrieve a single Payment by internal GUID id. |
| Get Payment By Keys | `getPayment` | Retrieve a single Payment by composite keys Type/ReferenceNbr. |
| Get Project By ID | `getProjectById` | Retrieve a single Project by internal GUID id. |
| Get Project By Keys | `getProject` | Retrieve a single Project by ProjectID key. |
| Get Purchase Order By ID | `getPurchaseOrderById` | Retrieve a single PurchaseOrder by internal GUID id. |
| Get Purchase Order By Keys | `getPurchaseOrder` | Retrieve a single PurchaseOrder by composite keys OrderType/OrderNbr. |
| Get Records (Generic Inquiry) | `getRecords` | Get specific rows from an Acumatica Generic Inquiry exposed via OData, picked with an OData $filter (e.g. one customer). tableName is "&lt;tenant&gt;/&lt;GI name&gt;", e.g. "Company/Four13 - Sync AC BC Customer". Supports $filter, $top, $skip, $select. Returns matching rows in value[]. Uses the connection's username/password (HTTP Basic). |
| Get Records by GI Name (Generic Inquiry) | `getRecordsByGiName` | Same call as Get Records (getRecords), only the input field is named giName instead of tableName. Gets specific rows from an Acumatica Generic Inquiry exposed via OData, picked with an OData $filter (e.g. one customer). giName is the GI name, e.g. "Four13 - Sale Prices" (single company, no company segment needed). Supports $filter, $top, $skip, $select. Returns matching rows in value[]. Uses the connection's username/password (HTTP Basic). |
| Get Sales Invoice By ID | `getSalesInvoiceById` | Retrieve a single SalesInvoice by its system id (GUID). Supports $expand, $select. |
| Get Sales Invoice By Keys | `getSalesInvoice` | Retrieve a single SalesInvoice by key fields (Type, ReferenceNbr). Supports $expand, $select. |
| Get Sales Order By ID | `getSalesOrderById` | Retrieve a single SalesOrder by internal GUID id. |
| Get Sales Order By Keys | `getSalesOrder` | Retrieve a single SalesOrder by composite keys OrderType/OrderNbr. |
| Get Shipment By ID | `getShipmentById` | Retrieve a single Shipment by internal GUID id. |
| Get Shipment By Keys | `getShipment` | Retrieve a single Shipment by ShipmentNbr key. |
| Get Stock Item By ID | `getStockItemById` | Retrieve a single StockItem by its internal GUID id. Supports $expand and $select. |
| Get Stock Item By Keys | `getStockItem` | Retrieve a single StockItem by its key field (InventoryID). Supports $expand and $select. |
| Get Vendor By ID | `getVendorById` | Retrieve a single Vendor by internal GUID id. |
| Get Vendor By Keys | `getVendor` | Retrieve a single Vendor by VendorID key. |
| Get Warehouse By ID | `getWarehouseById` | Retrieve a single Warehouse by its system id (GUID). Supports $expand, $select. |
| Get Warehouse By Keys | `getWarehouse` | Retrieve a single Warehouse by key field (WarehouseID). Supports $expand, $select. |
| List Accounts | `listAccounts` | Retrieve GL Account records. Supports $filter, $expand, $select, $top, $skip. |
| List Bills | `listBills` | Retrieve AP Bill records. Supports $filter, $expand (e.g. Details), $select, $top, $skip. |
| List Business Accounts | `listBusinessAccounts` | Retrieve BusinessAccount records (CRM). Supports $filter, $expand, $select, $top, $skip. |
| List Cases | `listCases` | Retrieve Case (support case) records. Supports $filter, $expand (e.g. Activities), $select, $top, $skip. |
| List Contacts | `listContacts` | Retrieve Contact records. Supports $filter, $expand (e.g. Address,Activities), $select, $top, $skip. |
| List Customers | `listCustomers` | Retrieve a list of Customer records. Supports OData $filter, $expand, $select, $top, $skip. |
| List Employees | `listEmployees` | Retrieve Employee records. Supports $filter, $expand, $select, $top, $skip. |
| List Inventory Issues | `listInventoryIssues` | Retrieve InventoryIssue records. Supports $filter, $expand (e.g. Details), $select, $top, $skip. |
| List Inventory Receipts | `listInventoryReceipts` | Retrieve InventoryReceipt records. Supports $filter, $expand (e.g. Details), $select, $top, $skip. |
| List Invoices | `listInvoices` | Retrieve AR Invoice records. Supports $filter, $expand (e.g. Details,TaxDetails), $select, $top, $skip. |
| List Journal Transactions | `listJournalTransactions` | Retrieve GL JournalTransaction batches. Supports $filter, $expand (e.g. Details), $select, $top, $skip. |
| List Leads | `listLeads` | Retrieve Lead records. Supports $filter, $expand (e.g. Address,Activities), $select, $top, $skip. |
| List Non-Stock Items | `listNonStockItems` | Retrieve a list of NonStockItem records. Supports OData $filter, $expand, $select, $top, $skip. |
| List Payments | `listPayments` | Retrieve AR Payment records. Supports $filter, $expand (e.g. DocumentsToApply,OrdersToApply), $select, $top, $skip. |
| List Projects | `listProjects` | Retrieve Project records. Supports $filter, $expand (e.g. Tasks,Balances), $select, $top, $skip. |
| List Purchase Orders | `listPurchaseOrders` | Retrieve PurchaseOrder records. Supports $filter, $expand (e.g. Details), $select, $top, $skip. |
| List Records (Generic Inquiry) | `listRecords` | Read rows from an Acumatica Generic Inquiry exposed via OData. tableName is "&lt;tenant&gt;/&lt;GI name&gt;", e.g. "Company/Four13 - Sale Prices". Supports OData $filter, $top, $skip, $select. Returns the rows in value[]. The GI must have "Expose via OData" ticked in Acumatica. Uses the connection's username/password (HTTP Basic). |
| List Records by GI Name (Generic Inquiry) | `listRecordsByGiName` | Same call as List Records (listRecords), only the input field is named giName instead of tableName. Reads rows from an Acumatica Generic Inquiry exposed via OData. giName is the GI name, e.g. "Four13 - Sale Prices" (single company, no company segment needed; "&lt;tenant&gt;/&lt;GI name&gt;" also works). Supports OData $filter, $top, $skip, $select; page with $top/$skip. Returns the rows in value[]. The GI must have "Expose via OData" ticked in Acumatica. Uses the connection's username/password (HTTP Basic). |
| List Sales Invoices | `listSalesInvoices` | Retrieve SO Sales Invoice records (SalesInvoice entity). Supports $filter, $expand (e.g. Details), $select, $top, $skip. |
| List Sales Orders | `listSalesOrders` | Retrieve SalesOrder records. Supports $filter, $expand (e.g. Details,ShippingSettings), $select, $top, $skip. |
| List Shipments | `listShipments` | Retrieve Shipment records. Supports $filter, $expand (e.g. Details,Packages), $select, $top, $skip. |
| List Stock Items | `listStockItems` | Retrieve a list of StockItem records. Supports OData $filter, $expand, $select, $top, $skip query parameters. |
| List Vendors | `listVendors` | Retrieve a list of Vendor records. Supports OData $filter, $expand, $select, $top, $skip. |
| List Warehouses | `listWarehouses` | Retrieve Warehouse records. Supports $filter, $expand, $select, $top, $skip. |
| Login | `login` | Sign in to Acumatica and establish a session cookie. POST /entity/auth/login with name, password, company, branch. Phase 2 calls this before entity operations; the Set-Cookie session is carried on subsequent requests. |
| Logout | `logout` | Sign out of Acumatica and release the API session. POST /entity/auth/logout. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Bill Changed | `Bill` | Push notification for AP Bill insert/update. |
| Case Changed | `Case` | Push notification for support Case insert/update. |
| Contact Changed | `Contact` | Push notification for Contact insert/update. |
| Customer Changed | `Customer` | Push notification for Customer record insert/update. Configure in the Acumatica Push Notifications screen. |
| Invoice Changed | `Invoice` | Push notification for AR Invoice insert/update. |
| Lead Changed | `Lead` | Push notification for Lead insert/update. |
| Payment Changed | `Payment` | Push notification for Payment insert/update. |
| Project Changed | `Project` | Push notification for Project insert/update. |
| Purchase Order Changed | `PurchaseOrder` | Push notification for PurchaseOrder insert/update. |
| Push Notification | `push.notification` | Acumatica Push Notification delivered to the webhook destination configured on the Push Notifications screen (SM302000). The payload contains the Inserted rows (rows that newly satisfy the generic-inquiry condition) and Deleted rows (rows that no longer satisfy it). Comparing the Deleted and Inserted sets reveals updated fields. Each notification corresponds to one push-notification definition (Query Id). |
| Sales Order Changed | `SalesOrder` | Push notification for SalesOrder insert/update. |
| Shipment Changed | `Shipment` | Push notification for Shipment insert/update. |
| Stock Item Changed | `StockItem` | Acumatica push notification fired when a StockItem record is inserted or updated. Configure a Push Notification in Acumatica (System Management &gt; Push Notifications) targeting the Stock Items generic inquiry/screen with this fastn webhook URL as the destination. Payload Inserted/Deleted arrays carry the changed field values. |
| Vendor Changed | `Vendor` | Push notification for Vendor record insert/update. |
