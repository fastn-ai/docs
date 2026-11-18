---
description: "Microsoft Dynamics 365 Finance & Operations connector via the OData v4 data-entity REST API (base https://{instance}.operations.dynamics.com/data)."
hidden: true
---

# Dynamics 365 Finance & Operations

<img src="../../.gitbook/assets/connectors/lg/dynamics365-fo.png" alt="Dynamics 365 Finance & Operations logo">

Microsoft Dynamics 365 Finance & Operations connector via the OData v4 data-entity REST API (base https://{instance}.operations.dynamics.com/data). Covers Customers, Vendors, Sales/Purchase orders, Released products, General journal entries, Customer payment journals, Ledger journals, Invoices plus a generic OData CRUD pattern and metadata. Auth: Azure AD OAuth 2.0 (authorization_code or client_credentials).

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [dynamics.microsoft.com](https://dynamics.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `dynamics365Fo` |

## Use it

Add Dynamics 365 Finance & Operations from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dynamics365Fo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Count Customers (CustomersV3 $count) | `countCustomers` | Return the total number of customer records in CustomersV3 (OData /$count). Supports $filter and cross-company. Response body is a plain integer. |
| Create Bank Account | `createBankAccount` | Create a new bank account in D365 FO. |
| Create Currency | `createCurrency` | Create a new currency in D365 FO. |
| Create Customer (CustomersV3) | `createCustomer` | Create a customer in D365 CustomersV3 (auto-numbered CustomerAccount). Requires dataAreaId, CustomerGroupId, OrganizationName, SalesCurrencyCode, PartyType, primary DeliveryMode/DeliveryTerms, and the OSG-specific mandatory backorder fields envBackorderDlvMode/envBackorderDlvTerms. |
| Create Customer Group | `createCustomerGroup` | Create a new customer group (POST /data/CustomerGroups). |
| Create Customer Location (PartyLocationPostalAddressesV2) | `createPartyLocationPostalAddress` | Create a postal address location for a party (customer) in PartyLocationPostalAddressesV2. Returns the created record with generated LocationId and ValidFrom. Yes/No flags are strings. |
| Create Customer Payment Journal Header (CustomerPaymentJournalHeaders) | `createCustomerPaymentJournalHeader` | Create a customer payment journal header in CustomerPaymentJournalHeaders. Requires dataAreaId and JournalName. |
| Create Customer Postal Address (Customer Location) | `createCustomerPostalAddress` | Create a new customer location (postal address) in the CustomerPostalAddresses data entity. Returns the created record including the generated AddressLocationId. Enum flags use 'Yes'/'No'. |
| Create Department | `createDepartment` | Create a department (OMDepartment operating unit). BLOCKED: the Departments OData entity rejects direct POST - it requires an internal 'Record type' field that is not settable via the public entity (OrganizationType/OperatingUnitTypes do not satisfy it). Departments are normally created through the D365 org-hierarchy designer. URL/entity is correct; left in test pending a settable record-type path. |
| Create Depreciation Profile (AssetDepreciationProfiles) | `createDepreciationProfile` | Create a new asset depreciation profile defining the calculation method for asset depreciation. |

<details>

<summary>See 193 more actions</summary>

* **Create Exchange Rate** `createExchangeRate`: Create an exchange rate. BLOCKED: posting a dated rate to ExchangeRateCurrencyPairs fails - in D365 the currency PAIR entity defines the pair (ExchangeRateTypeName/From/To) while the dated rate VALUE lives in a separate ExchangeRates entity; the single-POST shape here is rejected. Left in test pending the correct two-entity create path (create pair, then post dated rate).
* **Create Fixed Asset (FixedAssetsV2)** `createFixedAsset`: Create a new fixed asset record in the FixedAssetsV2 entity set. AssetId can be auto-assigned by number sequence if left blank.
* **Create Fixed Asset Book (FixedAssetBooks)** `createFixedAssetBook`: Create a new fixed asset book record linking a fixed asset to a depreciation book. Acquisition details are optional.
* **Create Item Group** `createItemGroup`: Create a new inventory item group in D365 FO (POST to InventItemGroups). Required: ItemGroupId, Name.
* **Create Ledger Journal Header (LedgerJournalHeaders)** `createLedgerJournal`: Create a general ledger journal header in LedgerJournalHeaders. Requires dataAreaId and JournalName.
* **Create Ledger Journal Line** `createLedgerJournalLine`: Create a new line in an existing unposted ledger journal. TransDate must match all rows sharing the same Voucher.
* **Create Main Account** `createMainAccount`: Create a new main account in the chart of accounts.
* **Create Payment Terms** `createPaymentTerms`: Create a new payment terms record (POST /data/PaymentTerms).
* **Create Position** `createPosition`: Create a new position in the HR organizational structure.
* **Create Project** `createProject`: Create a new project in Dynamics 365 F&O ProjectTable. ProjectId can be omitted to auto-assign from the number sequence.
* **Create Project Transaction** `createProjectTransaction`: Post a new item transaction against a project in Dynamics 365 F&O ProjTransactionItems.
* **Create Purchase Order Header (PurchaseOrderHeadersV2)** `createPurchaseOrderHeader`: Create a purchase order header in PurchaseOrderHeadersV2. Requires dataAreaId, OrderVendorAccountNumber, CurrencyCode.
* **Create Purchase Order Line** `createPurchaseOrderLine`: Create a new Purchase Order Line. PurchaseOrderNumber must reference an existing header. LineNumber is auto-assigned by number sequence if omitted.
* **Create Released Product (ReleasedProductsV2)** `createReleasedProduct`: Create a released product in ReleasedProductsV2. Requires dataAreaId, ItemNumber, ProductType, ProductNumber.
* **Create Return Order** `createReturnOrder`: Create a new return order (RMA) header in D365 FO. ReturnOrderNum is auto-assigned by number sequence if omitted.
* **Create Sales Order Header (SalesOrderHeadersV2)** `createSalesOrderHeader`: Create a sales order header in SalesOrderHeadersV2. Requires dataAreaId, OrderingCustomerAccountNumber, CurrencyCode. SalesOrderNumber may be auto-assigned by a number sequence.
* **Create Sales Order Line (SalesOrderLines)** `createSalesOrderLine`: Create a sales order line in SalesOrderLines. Requires dataAreaId, SalesOrderNumber, ItemNumber, OrderedSalesQuantity.
* **Create Sales Quotation** `createSalesQuotation`: Create a new sales quotation header in D365 FO. QuotationId is auto-assigned by number sequence if omitted.
* **Create Sales Quotation Line** `createSalesQuotationLine`: Add a line to an existing sales quotation. LineNum is auto-assigned if omitted.
* **Create Sales Tax Code** `createSalesTaxCode`: Create a new sales tax code (POST /data/SalesTaxCodes).
* **Create Sales Tax Group** `createSalesTaxGroup`: Create a new sales tax group (POST /data/SalesTaxGroups).
* **Create Site** `createSite`: Create a new operational/inventory site in D365 FO (POST OperationalSites). Requires dataAreaId, SiteId, SiteName, and a DefaultFinancialDimensionValue (a financial-dimension value, e.g. a BusinessUnit member, that is not already bound to another site). NOTE: not promoted to live — in this OSG-UAT instance every existing dimension value (1-4) is already tied to a site, so a non-destructive 201 cannot be produced without first creating a new dimension member (master-data setup). Config/contract are correct; needs a free dimension value at runtime.
* **Create Unit** `createUnit`: Create a new unit of measure (POST /data/Units).
* **Create Vendor (VendorsV2)** `createVendor`: Create a vendor record in VendorsV2. Requires dataAreaId, VendorAccountNumber, VendorGroupId, VendorOrganizationName, CurrencyCode.
* **Create Vendor Group** `createVendorGroup`: Create a new vendor group (POST /data/VendorGroups).
* **Create Vendor Invoice** `createVendorInvoice`: Create a new Vendor Invoice Header. InvoiceDate must be ISO date. TotalInvoiceAmount is optional.
* **Create Vendor Invoice Line** `createVendorInvoiceLine`: Create a new Vendor Invoice Line. InvoiceNumber must reference an existing Vendor Invoice Header.
* **Create Vendor Payment Journal** `createVendorPaymentJournal`: Create a new vendor payment journal header. JournalBatchNumber is auto-assigned by the system if omitted.
* **Create Vendor Payment Journal Line** `createVendorPaymentJournalLine`: Create a new payment line in an existing unposted vendor payment journal. Account is the vendor account number.
* **Create Warehouse** `createWarehouse`: Create a warehouse (POST /data/Warehouses). Entity corrected from InventWarehouses; name field corrected to WarehouseName. BLOCKED: the Warehouse public entity's site-reference property name could not be confirmed via probing ($select rejects InventSiteId/SiteId/WarehouseSiteId; the entity returns wide records that exceed the 4KB inspection limit), and creating a warehouse has downstream inventory-dimension impact. Left in test pending the confirmed site field name.
* **Create Worker** `createWorker`: Create a new worker (employee or contractor) in the HCM module.
* **Create Worker Employment** `createWorkerEmployment`: Create a new employment record linking a worker to a legal entity with a start date.
* **Delete Customer (CustomersV3)** `deleteCustomer`: Delete a customer from D365 CustomersV3 by composite OData key. NOT promoted to live only because a fully non-destructive success round-trip requires a throwaway customer to delete, and createCustomer is currently blocked (see its notes), so no safe deletable test record exists. Config/key format are correct.
* **Delete Customer Payment Journal Header (CustomerPaymentJournalHeaders)** `deleteCustomerPaymentJournalHeader`: Delete a customer payment journal header from CustomerPaymentJournalHeaders by composite key.
* **Delete Fixed Asset (FixedAssetsV2)** `deleteFixedAsset`: Delete a fixed asset record by its composite key (dataAreaId + AssetId).
* **Delete Ledger Journal Header (LedgerJournalHeaders)** `deleteLedgerJournal`: Delete a ledger journal header from LedgerJournalHeaders by composite key.
* **Delete Ledger Journal Line** `deleteLedgerJournalLine`: Delete a ledger journal line by its composite key. Only unposted lines can be deleted.
* **Delete Project** `deleteProject`: Delete a project from Dynamics 365 F&O by its composite OData key (dataAreaId + ProjectId).
* **Delete Purchase Order Header (PurchaseOrderHeadersV2)** `deletePurchaseOrderHeader`: Delete a purchase order header from PurchaseOrderHeadersV2 by composite key.
* **Delete Purchase Order Line** `deletePurchaseOrderLine`: Delete a Purchase Order Line by composite key (dataAreaId, PurchaseOrderNumber, LineNumber). Returns 204 No Content on success.
* **Delete Released Product (ReleasedProductsV2)** `deleteReleasedProduct`: Delete a released product from ReleasedProductsV2 by composite key.
* **Delete Sales Order Header (SalesOrderHeadersV2)** `deleteSalesOrderHeader`: Delete a sales order header from SalesOrderHeadersV2 by composite key.
* **Delete Sales Order Line (SalesOrderLines)** `deleteSalesOrderLine`: Delete a sales order line from SalesOrderLines by its OData key (dataAreaId, InventoryLotId).
* **Delete Sales Quotation** `deleteSalesQuotation`: Delete a sales quotation header by dataAreaId and QuotationId. Cannot delete a confirmed quotation.
* **Delete Sales Quotation Line** `deleteSalesQuotationLine`: Delete a sales quotation line by dataAreaId, QuotationId, and LineNum.
* **Delete Site** `deleteSite`: Delete an inventory site from D365 FO by composite key (dataAreaId + InventSiteId).
* **Delete Vendor (VendorsV2)** `deleteVendor`: Delete a vendor record from VendorsV2 by composite key.
* **Delete Vendor Payment Journal** `deleteVendorPaymentJournal`: Delete a vendor payment journal header by dataAreaId and JournalBatchNumber. Only unposted journals can be deleted.
* **Delete Vendor Payment Journal Line** `deleteVendorPaymentJournalLine`: Delete a vendor payment journal line by its composite key (dataAreaId, JournalBatchNumber, LineNumber).
* **Delete Warehouse** `deleteWarehouse`: Delete a warehouse from D365 FO by composite key (dataAreaId + InventWarehouseId).
* **Generic OData Create (any entity)** `genericCreate`: Generic OData POST to create a record in any F&O data entity. Provide the entity set name and the complete record as a JSON object in recordJson. recordJson must be a valid JSON object string including dataAreaId and all required fields.
* **Generic OData Delete (any entity)** `genericDelete`: Generic OData DELETE against any F&O data entity by key predicate.
* **Generic OData Get by Key (any entity)** `genericGetByKey`: Generic OData GET by key against any F&O data entity. Provide the entity set name and the full OData key predicate (the contents between the parentheses), e.g. keyPredicate = dataAreaId='usmf',CustomerAccount='US-001'.
* **Generic OData List (any entity)** `genericList`: Generic OData GET list against any F&O data entity set. Provide the entity set name (e.g. CustomersV3) plus optional $filter/$select/$expand/$top/$skip/$orderby/$count. Use this for entities without a dedicated action.
* **Generic OData Update (any entity)** `genericUpdate`: Generic OData PATCH to update a record in any F&O data entity. Provide the entity set, the key predicate, and the fields to change as a JSON object in recordJson.
* **Get Active Prices (Pricing Calculation API)** `getActivePrices`: Calculate real-time prices and simple discounts for products without creating a sales order, via the Unified Pricing Management calculation API. POST /api/services/GUPPricingServiceGroup/GUPPricingService/getActivePrices. Requires SCM 10.0.47+ with Unified pricing management enabled. Provide dataAreaId or HeaderContext.ChannelId, and either productIds or priceLookupContext.LineContexts (not both).
* **Get Bank Account** `getBankAccount`: Get a single bank account by dataAreaId and BankAccountId.
* **Get Currency** `getCurrency`: Get a single currency by CurrencyCode.
* **Get Customer by Key (CustomersV3)** `getCustomer`: Retrieve a single customer from CustomersV3 by its composite key (dataAreaId and CustomerAccount).
* **Get Customer Group** `getCustomerGroup`: Get a single customer group by dataAreaId and CustomerGroupId (OData key predicate).
* **Get Customer Location By ID (PartyLocationPostalAddressesV2)** `getPartyLocationPostalAddress`: Get a party (customer) location postal address by LocationId from PartyLocationPostalAddressesV2. Returns an OData value array with PartyNumber, LocationId, ValidFrom (needed for updates), address fields and roles.
* **Get Customer Payment Journal Header by Key (CustomerPaymentJournalHeaders)** `getCustomerPaymentJournalHeader`: Retrieve a single customer payment journal header from CustomerPaymentJournalHeaders by composite key (dataAreaId, JournalBatchNumber).
* **Get Customer Postal Address By Location ID** `getCustomerPostalAddress`: Get a customer location (postal address) by its AddressLocationId from the CustomerPostalAddresses data entity. Returns an OData value array (0 or 1 match).
* **Get Department** `getDepartment`: Get a single department by DepartmentNumber.
* **Get Depreciation Profile by Key (AssetDepreciationProfiles)** `getDepreciationProfile`: Retrieve a single depreciation profile by its composite key (dataAreaId + DepreciationProfileId).
* **Get Entity List (OData service root)** `getEntityList`: List all exposed OData entity sets for the environment by querying the OData service document root (/data). Returns the name and url of every available data entity set.
* **Get Exchange Rate** `getExchangeRate`: Get a specific exchange rate currency pair by ExchangeRateTypeId, FromCurrencyCode, and ToCurrencyCode.
* **Get Fixed Asset Book by Key (FixedAssetBooks)** `getFixedAssetBook`: Retrieve a single fixed asset book record by its composite key (dataAreaId + AssetId + BookId).
* **Get Fixed Asset by Key (FixedAssetsV2)** `getFixedAsset`: Retrieve a single fixed asset by its composite key (dataAreaId + AssetId).
* **Get General Journal Entry by Key (GeneralJournalEntries)** `getGeneralJournalEntry`: Retrieve a single general journal entry. BLOCKED: the OData entity set 'GeneralJournalEntries' does not exist in this environment (404). The only exposed general-ledger entry entities are read-only Bi/CDR aggregates (e.g. GeneralJournalAccountEntryBiEntities, 9.6M rows) whose filterable key property names could not be confirmed (metadata Properties expand returns 500, $select/$filter field-name probing inconclusive). Left in test pending confirmed entity/field schema.
* **Get Inventory On-Hand by Item** `getInventoryOnHandByItem`: Get on-hand inventory for a specific item in a given site and warehouse using OData composite key predicate.
* **Get Item Group** `getItemGroup`: Get a specific item group by composite key (dataAreaId + ItemGroupId) from InventItemGroups.
* **Get Ledger Journal Header by Key (LedgerJournalHeaders)** `getLedgerJournal`: Retrieve a single ledger journal header from LedgerJournalHeaders by composite key (dataAreaId, JournalBatchNumber).
* **Get Ledger Journal Line** `getLedgerJournalLine`: Get a single ledger journal line by its composite key (JournalBatchNumber and LineNumber).
* **Get Main Account** `getMainAccount`: Get a single main account by MainAccountId.
* **Get OData Metadata ($metadata)** `getMetadata`: Retrieve the OData $metadata CSDL document describing the EDM schema (entity types, properties, keys, navigation properties) for all exposed data entities. Returned as XML.
* **Get Payment Terms** `getPaymentTerms`: Get a single payment terms record by TermsOfPaymentCode.
* **Get Position** `getPosition`: Get a single position by PositionId.
* **Get Posted Customer Invoice by Key (SalesInvoiceHeaders)** `getInvoice`: Retrieve a posted customer sales invoice from SalesInvoiceHeaders by InvoiceNumber via $filter (this entity's full composite key is multi-segment, so a $filter lookup is used). Returns a value array. Optionally constrain by dataAreaId.
* **Get Pricing (rsmWebPriceService)** `getRsmWebPrice`: Call the custom RSM web price service to calculate prices for a customer's line items. POST /api/services/rsmWebPriceServiceGroup/rsmWebPriceService/create with body {_request:{LegalEntity, Customer, CouponCode, LineItems:[{Item, Quantity}]}}. Customer-specific custom service (not standard D365).
* **Get Project** `getProject`: Retrieve a single project by its composite OData key (dataAreaId + ProjectId) from Dynamics 365 F&O.
* **Get Project Transaction** `getProjectTransaction`: Get a project transaction. Now targets the correct entity set ProjItemTransCDREntities (the one listProjectTransactions uses) via filter-based GET. BLOCKED: this entity contains ZERO records in the sandbox (@odata.count=0), so it cannot be validated and the exact filter field name (ProjectID rejected) is unconfirmable without data. Left in test pending project-transaction data.
* **Get Purchase Order Header by Key (PurchaseOrderHeadersV2)** `getPurchaseOrderHeader`: Retrieve a single purchase order header from PurchaseOrderHeadersV2 by composite key (dataAreaId, PurchaseOrderNumber).
* **Get Purchase Order Line** `getPurchaseOrderLine`: Get a specific Purchase Order Line by composite key (dataAreaId, PurchaseOrderNumber, LineNumber).
* **Get Released Product by Key (ReleasedProductsV2)** `getReleasedProduct`: Retrieve a single released product from ReleasedProductsV2 by composite key (dataAreaId, ItemNumber).
* **Get Return Order** `getReturnOrder`: Get a single return order header by dataAreaId and ReturnOrderNumber key predicate.
* **Get Sales Invoice Header V2 by Key (SalesInvoiceHeadersV2)** `getSalesInvoiceHeaderV2`: Get a single Sales Invoice Header V2 by composite key (dataAreaId, InvoiceNumber, InvoiceDate, LedgerVoucher) from SalesInvoiceHeadersV2.
* **Get Sales Invoice Line V2 by Key (SalesInvoiceV2Lines)** `getSalesInvoiceLineV2`: Get a single Sales Invoice Line V2 by composite key (dataAreaId, InvoiceNumber, LineCreationSequenceNumber, InvoiceDate, LedgerVoucher) from SalesInvoiceV2Lines.
* **Get Sales Order Confirmation Header by Key (SalesOrderConfirmationHeaders)** `getSalesOrderConfirmationHeader`: Get a single Sales Order Confirmation Header by composite key (dataAreaId, SalesOrderNumber, ConfirmationDate, ConfirmationNumber) from SalesOrderConfirmationHeaders.
* **Get Sales Order Confirmation Line by Key (SalesOrderConfirmationLines)** `getSalesOrderConfirmationLine`: Get a single Sales Order Confirmation Line by composite key (dataAreaId, SalesOrderNumber, ConfirmationDate, ConfirmationNumber, LineNumber) from SalesOrderConfirmationLines.
* **Get Sales Order Header by Key (SalesOrderHeadersV2)** `getSalesOrderHeader`: Retrieve a single sales order header from SalesOrderHeadersV2 by composite key (dataAreaId, SalesOrderNumber).
* **Get Sales Order Header V3 by Key (SalesOrderHeadersV3)** `getSalesOrderHeaderV3`: Get a single Sales Order Header V3 by composite key (dataAreaId, SalesOrderNumber) from SalesOrderHeadersV3.
* **Get Sales Order Line by Key (SalesOrderLines)** `getSalesOrderLine`: Retrieve a single sales order line from SalesOrderLines by its OData key InventoryLotId (composite key dataAreaId, InventoryLotId).
* **Get Sales Order Line V3 by Key (SalesOrderLinesV3)** `getSalesOrderLineV3`: Get a single Sales Order Line V3 by composite key (dataAreaId, InventoryLotId) from SalesOrderLinesV3.
* **Get Sales Quotation** `getSalesQuotation`: Get a single sales quotation header by dataAreaId and SalesQuotationNumber key predicate.
* **Get Sales Quotation Line** `getSalesQuotationLine`: Get a single sales quotation line via $filter on dataAreaId, SalesQuotationNumber and LineCreationSequenceNumber (the SalesQuotationLines OData key predicate is not directly addressable, so a filtered list is used).
* **Get Sales Tax Code** `getSalesTaxCode`: Get a single sales tax code by dataAreaId and TaxCode.
* **Get Sales Tax Group** `getSalesTaxGroup`: Get a single sales tax group by dataAreaId and TaxGroupCode.
* **Get Shipment Packing Slip Journal Header by Key (ShipmentPackingSlipJournalHeaders)** `getShipmentPackingSlipJournalHeader`: Get a shipment packing slip journal header by key. Entity set ShipmentPackingSlipJournalHeaders resolves and returns 200, but contains ZERO records in this sandbox, so a by-key GET cannot be validated. Config is correct; left in test pending real packing-slip data.
* **Get Shipment Packing Slip Journal Line by Key (ShipmentPackingSlipJournalLines)** `getShipmentPackingSlipJournalLine`: Get a shipment packing slip journal line by key. Entity set ShipmentPackingSlipJournalLines resolves and returns 200, but contains ZERO records in this sandbox, so a by-key GET cannot be validated. Config is correct; left in test pending real packing-slip data.
* **Get Site** `getSite`: Get a specific inventory site by composite key (dataAreaId + InventSiteId) from InventSites.
* **Get Unit** `getUnit`: Get a single unit of measure by UnitId.
* **Get Vendor by Key (VendorsV2)** `getVendor`: Retrieve a single vendor from VendorsV2 by composite key (dataAreaId, VendorAccountNumber).
* **Get Vendor Group** `getVendorGroup`: Get a single vendor group by dataAreaId and VendorGroupId.
* **Get Vendor Invoice** `getVendorInvoice`: Get a Vendor Invoice Header by composite key (dataAreaId, InvoiceNumber).
* **Get Vendor Invoice Line** `getVendorInvoiceLine`: Get a Vendor Invoice Line by composite key (dataAreaId, InvoiceNumber, LineNumber). LineNumber is numeric.
* **Get Vendor Payment Journal** `getVendorPaymentJournal`: Get a single vendor payment journal header by its composite key (dataAreaId and JournalBatchNumber).
* **Get Vendor Payment Journal Line** `getVendorPaymentJournalLine`: Get a single vendor payment journal line by its composite key (dataAreaId, JournalBatchNumber, LineNumber).
* **Get Warehouse** `getWarehouse`: Get a specific warehouse by composite key (dataAreaId + InventWarehouseId) from InventWarehouses.
* **Get Worker** `getWorker`: Get a single worker by PersonnelNumber from Human Capital Management (HCM).
* **Get Worker Employment** `getWorkerEmployment`: Get employment record for a specific worker by PersonnelNumber.
* **List Address States (AddressStates)** `listAddressStates`: List states/provinces per country/region from the AddressStates data entity. Supports OData $filter (e.g. CountryRegionId eq 'USA'), $select, $top, $skip, $count.
* **List Bank Accounts** `listBankAccounts`: List all bank accounts in D365 FO with optional OData filtering.
* **List Currencies** `listCurrencies`: List all currencies configured in D365 FO.
* **List Customer Groups** `listCustomerGroups`: List all customer groups (OData GET /data/CustomerGroups). Supports filtering, paging and sorting.
* **List Customer Payment Journal Headers (CustomerPaymentJournalHeaders)** `listCustomerPaymentJournalHeaders`: List customer payment journal headers from CustomerPaymentJournalHeaders. Supports $filter, $select, $expand, $top, $skip, $orderby, $count.
* **List Customers (CustomersV3)** `listCustomers`: List customer records from the CustomersV3 data entity. Supports OData query options $filter, $select, $expand, $top, $skip, $orderby, $count.
* **List Departments** `listDepartments`: List all departments in the organizational hierarchy.
* **List Depreciation Profiles (AssetDepreciationProfiles)** `listDepreciationProfiles`: List asset depreciation profiles from the AssetDepreciationProfiles entity set.
* **List Exchange Rates** `listExchangeRates`: List exchange rate currency pairs in D365 FO.
* **List Fixed Asset Books (FixedAssetBooks)** `listFixedAssetBooks`: List fixed asset book records from the FixedAssetBooks entity set. Each record links a fixed asset to a depreciation book.
* **List Fixed Assets (FixedAssetsV2)** `listFixedAssets`: List fixed assets from the FixedAssetsV2 entity set. Supports OData query options for filtering, sorting, and pagination.
* **List General Journal Entries (GeneralJournalEntries)** `listGeneralJournalEntries`: List general journal entries from the GeneralJournalEntries data entity. Supports $filter, $select, $expand, $top, $skip, $orderby, $count.
* **List Inventory On-Hand** `listInventoryOnHand`: List on-hand inventory quantities from InventWarehouseOnHandV2. Supports OData $filter, $top, $skip, $select, $orderby, and cross-company query.
* **List Item Groups** `listItemGroups`: List all inventory item groups (InventItemGroups). Supports OData $filter, $top, $skip, $select, $orderby, and cross-company.
* **List Ledger Journal Headers (LedgerJournalHeaders)** `listLedgerJournals`: List general ledger journal headers from LedgerJournalHeaders. Supports $filter, $select, $expand, $top, $skip, $orderby, $count.
* **List Ledger Journal Lines** `listLedgerJournalLines`: List journal lines from the LedgerJournalLines entity. Supports OData query parameters for filtering, pagination, and sorting.
* **List Main Accounts** `listMainAccounts`: List all main accounts (chart of accounts) in D365 FO with optional OData filtering.
* **List Payment Terms** `listPaymentTerms`: List all payment terms (OData GET /data/PaymentTerms). Supports filtering, paging and sorting.
* **List Positions** `listPositions`: List all positions (job positions with department, job, and FTE details).
* **List Postal Address Electronic Contacts (PostalAddressElectronicContactsV2)** `listPostalAddressElectronicContacts`: List electronic contacts (phone, email, URL) attached to postal addresses, e.g. customer address contacts, from PostalAddressElectronicContactsV2. Supports OData $filter, $select, $top, $skip and cross-company.
* **List Posted Customer Invoices (SalesInvoiceHeaders)** `listInvoices`: List posted customer sales invoices from the SalesInvoiceHeaders data entity (the available posted-customer-invoice entity in this sandbox; CustomerInvoiceJournalHeaders is not exposed). Supports $filter, $select, $expand, $top, $skip, $orderby, $count. Use a narrow $select to avoid the big-row parse limit.
* **List Product Categories (ProductCategories)** `listProductCategories`: List product categories across category hierarchies from the ProductCategories data entity. Filter by hierarchy, e.g. $filter=ProductCategoryHierarchyName eq 'Retail'.
* **List Product Category Assignments (ProductCategoryAssignments)** `listProductCategoryAssignments`: List product-to-category assignments from ProductCategoryAssignments, optionally expanding ProductCategoryHierarchy. Filter by product, e.g. $filter=ProductNumber eq 'A0001'.
* **List Product Inventory On-Hand (ProductInventoryOnHands)** `listProductInventoryOnHands`: List on-hand inventory per product from the ProductInventoryOnHands data entity. Filter by product, e.g. $filter=ProductNumber eq 'A0001'. Supports $select and cross-company.
* **List Project Transactions** `listProjectTransactions`: Retrieve a list of project transaction items from Dynamics 365 F&O ProjTransactionItems with optional OData filtering and pagination.
* **List Projects** `listProjects`: Retrieve a list of projects from Dynamics 365 F&O ProjectTable with optional OData filtering, sorting, and pagination.
* **List Purchase Order Headers (PurchaseOrderHeadersV2)** `listPurchaseOrderHeaders`: List purchase order headers from PurchaseOrderHeadersV2. Supports $filter, $select, $expand, $top, $skip, $orderby, $count.
* **List Purchase Order Lines** `listPurchaseOrderLines`: List Purchase Order Lines with optional OData filtering ($filter, $top, $skip, $select, $orderby, $count, cross-company).
* **List Released Products (ReleasedProductsV2)** `listReleasedProducts`: List released products from ReleasedProductsV2. Supports $filter, $select, $expand, $top, $skip, $orderby, $count.
* **List Return Orders** `listReturnOrders`: List return order headers from D365 FO with OData query support.
* **List Sales Invoice Header V2s (SalesInvoiceHeadersV2)** `listSalesInvoiceHeaderV2s`: List Sales Invoice Header V2 records from the SalesInvoiceHeadersV2 OData data entity. Supports $filter,$select,$expand,$top,$skip,$orderby,$count.
* **List Sales Invoice Line V2s (SalesInvoiceV2Lines)** `listSalesInvoiceLineV2s`: List Sales Invoice Line V2 records from the SalesInvoiceV2Lines OData data entity. Supports $filter,$select,$expand,$top,$skip,$orderby,$count.
* **List Sales Order Confirmation Headers (SalesOrderConfirmationHeaders)** `listSalesOrderConfirmationHeaders`: List Sales Order Confirmation Header records from the SalesOrderConfirmationHeaders OData data entity. Supports $filter,$select,$expand,$top,$skip,$orderby,$count.
* **List Sales Order Confirmation Lines (SalesOrderConfirmationLines)** `listSalesOrderConfirmationLines`: List Sales Order Confirmation Line records from the SalesOrderConfirmationLines OData data entity. Supports $filter,$select,$expand,$top,$skip,$orderby,$count.
* **List Sales Order Header Document Attachments** `listSalesOrderHeaderDocumentAttachments`: List document attachments (notes, files, URLs) on sales order headers from the SalesOrderHeaderDocumentAttachments data entity. Filter by order, e.g. $filter=SalesOrderNumber eq '000123' and dataAreaId eq 'usmf'. File content is returned in the Attachment field.
* **List Sales Order Header V3s (SalesOrderHeadersV3)** `listSalesOrderHeaderV3s`: List Sales Order Header V3 records from the SalesOrderHeadersV3 OData data entity. Supports $filter,$select,$expand,$top,$skip,$orderby,$count.
* **List Sales Order Headers (SalesOrderHeadersV2)** `listSalesOrderHeaders`: List sales order headers from SalesOrderHeadersV2. Supports $filter, $select, $expand, $top, $skip, $orderby, $count.
* **List Sales Order Line V3s (SalesOrderLinesV3)** `listSalesOrderLineV3s`: List Sales Order Line V3 records from the SalesOrderLinesV3 OData data entity. Supports $filter,$select,$expand,$top,$skip,$orderby,$count.
* **List Sales Order Lines (SalesOrderLines)** `listSalesOrderLines`: List sales order lines from the SalesOrderLines data entity. Supports $filter, $select, $expand, $top, $skip, $orderby, $count.
* **List Sales Quotation Lines** `listSalesQuotationLines`: List sales quotation lines from D365 FO with OData query support.
* **List Sales Quotations** `listSalesQuotations`: List sales quotation headers from D365 FO with OData query support.
* **List Sales Tax Codes** `listSalesTaxCodes`: List all sales tax codes (OData GET /data/SalesTaxCodes). Supports filtering, paging and sorting.
* **List Sales Tax Groups** `listSalesTaxGroups`: List all sales tax groups (OData GET /data/SalesTaxGroups). Supports filtering, paging and sorting.
* **List Ship Carrier Third Party Addresses (NMBShipCarrierAddresses)** `listShipCarrierThirdPartyAddresses`: List ship carrier third-party addresses from the custom NMBShipCarrierAddresses data entity. Supports OData $filter, $select, $top, $skip and cross-company. Customer-specific custom entity.
* **List Shipment Packing Slip Journal Headers (ShipmentPackingSlipJournalHeaders)** `listShipmentPackingSlipJournalHeaders`: List Shipment Packing Slip Journal Header records from the ShipmentPackingSlipJournalHeaders OData data entity. Supports $filter,$select,$expand,$top,$skip,$orderby,$count.
* **List Shipment Packing Slip Journal Lines (ShipmentPackingSlipJournalLines)** `listShipmentPackingSlipJournalLines`: List Shipment Packing Slip Journal Line records from the ShipmentPackingSlipJournalLines OData data entity. Supports $filter,$select,$expand,$top,$skip,$orderby,$count.
* **List Sites** `listSites`: List all inventory sites (InventSites). Supports OData $filter, $top, $skip, $select, $orderby, and cross-company.
* **List Units** `listUnits`: List all units of measure (OData GET /data/Units). Supports filtering, paging and sorting.
* **List Vendor Groups** `listVendorGroups`: List all vendor groups (OData GET /data/VendorGroups). Supports filtering, paging and sorting.
* **List Vendor Invoice Lines** `listVendorInvoiceLines`: List Vendor Invoice Lines with optional OData filtering. Keys: dataAreaId, InvoiceNumber, LineNumber.
* **List Vendor Invoices** `listVendorInvoices`: List Vendor Invoice Headers with optional OData filtering. Keys: dataAreaId, InvoiceNumber.
* **List Vendor Payment Journal Lines** `listVendorPaymentJournalLines`: List vendor payment journal lines from the VendorPaymentJournalLines entity. Supports OData query parameters.
* **List Vendor Payment Journals** `listVendorPaymentJournals`: List vendor payment journal headers from the VendorPaymentJournalHeaders entity. Supports OData query parameters.
* **List Vendors (VendorsV2)** `listVendors`: List vendor records from the VendorsV2 data entity. Supports $filter, $select, $expand, $top, $skip, $orderby, $count.
* **List Warehouses** `listWarehouses`: List all warehouses (InventWarehouses). Supports OData $filter, $top, $skip, $select, $orderby, and cross-company.
* **List Worker Employments** `listWorkerEmployments`: List worker employment records (start/end dates, legal entity assignments).
* **List Workers** `listWorkers`: List all workers (employees and contractors) from Human Capital Management (HCM).
* **Update Bank Account** `updateBankAccount`: Update an existing bank account (PATCH — send only fields to change).
* **Update Customer (CustomersV3)** `updateCustomer`: Update an existing customer in CustomersV3 by composite key using PATCH (partial update).
* **Update Customer Address (PartyLocationPostalAddressesV2)** `updatePartyLocationPostalAddress`: Partially update a party (customer) postal address by composite key PartyNumber, LocationId, ValidFrom via OData PATCH on PartyLocationPostalAddressesV2. Get the key values from Get Customer Location By ID.
* **Update Customer Postal Address** `updateCustomerPostalAddress`: Partially update a customer postal address in CustomerPostalAddresses via OData PATCH. keyPredicate is the entity's composite key as returned in @odata.id / @odata.etag of a Get/List call. Only the fields you pass are changed.
* **Update Department** `updateDepartment`: Update an existing department's details (PATCH — sends only changed fields).
* **Update Fixed Asset (FixedAssetsV2)** `updateFixedAsset`: Update an existing fixed asset record using PATCH. Only include fields that need to be changed. Keys (dataAreaId, AssetId) are required for the key predicate.
* **Update Ledger Journal Line** `updateLedgerJournalLine`: Update fields on an existing unposted ledger journal line using PATCH. Caller must supply at least one of the update fields (AmountCurDebit or AmountCurCredit is required to be meaningful).
* **Update Main Account** `updateMainAccount`: Update an existing main account by MainAccountId (PATCH — send only fields to change).
* **Update Position** `updatePosition`: Update an existing position's details (PATCH — sends only changed fields).
* **Update Project** `updateProject`: Update an existing project in Dynamics 365 F&O using PATCH. Key fields (dataAreaId + ProjectId) route to the record; only Name is sent in the body by default.
* **Update Purchase Order Header (PurchaseOrderHeadersV2)** `updatePurchaseOrderHeader`: Update a purchase order header in PurchaseOrderHeadersV2 by composite key using PATCH.
* **Update Purchase Order Line** `updatePurchaseOrderLine`: Update a Purchase Order Line (PATCH — send only changed fields). Key: dataAreaId, PurchaseOrderNumber, LineNumber. If-Match: * header required.
* **Update Released Product (ReleasedProductsV2)** `updateReleasedProduct`: Update a released product in ReleasedProductsV2 by composite key using PATCH.
* **Update Return Order** `updateReturnOrder`: Update an existing return order header via PATCH. Sends only changed fields; key fields identify the record.
* **Update Sales Order Header (SalesOrderHeadersV2)** `updateSalesOrderHeader`: Update a sales order header in SalesOrderHeadersV2 by composite key using PATCH.
* **Update Sales Order Line (SalesOrderLines)** `updateSalesOrderLine`: Update a sales order line in SalesOrderLines by its OData key (dataAreaId, InventoryLotId) using PATCH.
* **Update Sales Quotation** `updateSalesQuotation`: Update an existing sales quotation header via PATCH. Sends only changed fields; key fields identify the record.
* **Update Sales Quotation Line** `updateSalesQuotationLine`: Update an existing sales quotation line via PATCH. Key fields identify the record; only changed fields are sent.
* **Update Sales Tax Code** `updateSalesTaxCode`: Update a sales tax code (PATCH /data/SalesTaxCodes). Only changed fields need to be sent.
* **Update Site** `updateSite`: Update an existing inventory site in D365 FO (PATCH InventSites). Key fields required; others optional.
* **Update Vendor (VendorsV2)** `updateVendor`: Update a vendor in VendorsV2 by composite key using PATCH.
* **Update Vendor Payment Journal Line** `updateVendorPaymentJournalLine`: Update fields on an existing unposted vendor payment journal line using PATCH. Key fields and AmountCurDebit are required; all other fields optional.
* **Update Warehouse** `updateWarehouse`: Update an existing warehouse in D365 FO (PATCH InventWarehouses). Key fields required; all others optional.
* **Update Worker** `updateWorker`: Update an existing worker's details by PersonnelNumber (PATCH — sends only changed fields).
* **Update Worker Employment** `updateWorkerEmployment`: Update an existing worker employment record (e.g. set end date for termination).

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Bank Statement Imported | `BankStatementImportedBusinessEvent` | Fires when a bank statement is imported in D365 FO cash and bank management. |
| Bank Statement Imported | `BankStatementImportedBusinessEvent` | Fires when a bank statement is imported in D365 FO. |
| Customer Invoice Posted | `CustInvoicePostedBusinessEvent` | Fires when a customer invoice is posted in D365 FO accounts receivable. |
| Customer Invoice Posted | `CustInvoicePostedBusinessEvent` | Fires when a customer invoice is posted in D365 FO accounts receivable. |
| Customer Payment Journal Posted | `CustPaymentJournalPostedBusinessEvent` |  |
| Customer Payment Journal Posted | `CustPaymentJournalPostedBusinessEvent` | Fires when a customer payment journal is posted in D365 FO |
| Customer Payment Journal Posted | `CustPaymentJournalPostedBusinessEvent` | Fires when a customer payment journal is posted in D365 FO. |
| Customer Payment Journal Posted | `CustPaymentJournalPostedBusinessEvent` | Fires when a customer payment journal is posted in D365 FO. |
| Department Created | `HcmDepartmentCreatedBusinessEvent` | Fires when a new department is created in the organizational hierarchy. |
| Department Created | `HcmDepartmentCreatedBusinessEvent` | Fires when a new department is created in D365 FO HCM. |

<details>

<summary>See 54 more events</summary>

* **Department Updated** `HcmDepartmentUpdatedBusinessEvent`: Fires when a department record is updated (e.g. name or manager change).
* **Department Updated** `HcmDepartmentUpdatedBusinessEvent`: Fires when a department is updated in D365 FO HCM.
* **Employment Created** `HcmEmploymentCreatedBusinessEvent`: Fires when a new worker employment record is created (worker hired into a legal entity).
* **Employment Created** `HcmEmploymentCreatedBusinessEvent`: Fires when a new employment record is created in D365 FO HCM.
* **Employment Terminated** `HcmEmploymentTerminatedBusinessEvent`: Fires when a worker employment record is terminated (end date set) in HCM.
* **Employment Terminated** `HcmEmploymentTerminatedBusinessEvent`: Fires when an employment record is terminated in D365 FO HCM.
* **Fixed Asset Acquisition Posted** `FixedAssetAcquisitionPostedBusinessEvent`: Fires when a fixed asset acquisition transaction is posted in D365 FO.
* **Fixed Asset Acquisition Posted** `FixedAssetAcquisitionPostedBusinessEvent`: Fires when a fixed asset acquisition transaction is posted in D365 FO.
* **Fixed Asset Transaction** `AssetTransBusinessEvent`
* **Fixed Asset Transaction** `AssetTransBusinessEvent`: Fires when a fixed asset transaction occurs in D365 FO
* **Fixed Asset Transaction** `AssetTransBusinessEvent`: Fires when a fixed asset transaction (acquisition, depreciation, disposal) is posted in D365 FO.
* **Fixed Asset Transaction** `AssetTransBusinessEvent`: Fires when a fixed asset transaction is posted in D365 FO.
* **Ledger Journal Posted** `LedgerJournalPostedBusinessEvent`
* **Ledger Journal Posted** `LedgerJournalPostedBusinessEvent`: Fires when a general ledger journal is posted in D365 FO
* **Ledger Journal Posted** `LedgerJournalPostedBusinessEvent`: Fires when a general ledger journal is posted in D365 FO.
* **Ledger Journal Posted** `LedgerJournalPostedBusinessEvent`: Fires when a general ledger journal is posted in D365 FO.
* **Position Created** `HcmPositionCreatedBusinessEvent`: Fires when a new organizational position is created in HCM.
* **Position Created** `HcmPositionCreatedBusinessEvent`: Fires when a new position is created in D365 FO HCM.
* **Position Updated** `HcmPositionUpdatedBusinessEvent`: Fires when an organizational position is updated in HCM (e.g. department change, FTE change).
* **Position Updated** `HcmPositionUpdatedBusinessEvent`: Fires when a position is updated in D365 FO HCM.
* **Project Transaction Posted** `ProjProjTransactionPostedBusinessEvent`
* **Project Transaction Posted** `ProjProjTransactionPostedBusinessEvent`: Fires when a project transaction is posted in D365 FO
* **Project Transaction Posted** `ProjProjTransactionPostedBusinessEvent`: Fires when a project transaction is posted in D365 FO.
* **Project Transaction Posted** `ProjProjTransactionPostedBusinessEvent`: Fires when a project transaction is posted in D365 FO.
* **Purchase Order Confirmed** `PurchPurchaseOrderConfirmedBusinessEvent`
* **Purchase Order Confirmed** `PurchPurchaseOrderConfirmedBusinessEvent`: Fires when a purchase order is confirmed in D365 FO
* **Purchase Order Confirmed** `PurchPurchaseOrderConfirmedBusinessEvent`: Fires when a purchase order is confirmed in D365 FO.
* **Purchase Order Confirmed** `PurchPurchaseOrderConfirmedBusinessEvent`: Fires when a purchase order is confirmed in D365 FO.
* **Purchase Product Receipt Posted** `PurchProductReceiptPostedBusinessEvent`: Fires when a product receipt is posted against a purchase order.
* **Purchase Product Receipt Posted** `PurchProductReceiptPostedBusinessEvent`: Fires when a product receipt is posted against a purchase order.
* **Sales Order Confirmed** `SalesOrderConfirmedBusinessEvent`
* **Sales Order Confirmed** `SalesOrderConfirmedBusinessEvent`: Fires when a sales order is confirmed in D365 FO
* **Sales Order Confirmed** `SalesOrderConfirmedBusinessEvent`: Fires when a sales order is confirmed in D365 FO.
* **Sales Order Confirmed** `SalesOrderConfirmedBusinessEvent`: Fires when a sales order is confirmed in D365 FO.
* **Sales Order Created** `SalesOrderCreatedBusinessEvent`
* **Sales Order Created** `SalesOrderCreatedBusinessEvent`: Fires when a sales order is created in D365 FO
* **Sales Order Created** `SalesOrderCreatedBusinessEvent`: Fires when a new sales order is created in D365 FO.
* **Sales Order Created** `SalesOrderCreatedBusinessEvent`: Fires when a new sales order is created in D365 FO.
* **Transfer Order Created** `InventTransferOrderCreatedBusinessEvent`: Fires when an inventory transfer order is created in D365 FO.
* **Transfer Order Created** `InventTransferOrderCreatedBusinessEvent`: Fires when an inventory transfer order is created in D365 FO.
* **Transfer Order Received** `InventTransferOrderReceivedBusinessEvent`: Fires when an inventory transfer order is received at the destination warehouse.
* **Transfer Order Received** `InventTransferOrderReceivedBusinessEvent`: Fires when an inventory transfer order is received in D365 FO.
* **Transfer Order Shipped** `InventTransferOrderShippedBusinessEvent`: Fires when an inventory transfer order is shipped from the source warehouse.
* **Transfer Order Shipped** `InventTransferOrderShippedBusinessEvent`: Fires when an inventory transfer order is shipped in D365 FO.
* **Vendor Invoice Posted** `VendInvoicePostedBusinessEvent`: Fires when a vendor invoice is posted in D365 FO accounts payable.
* **Vendor Invoice Posted** `VendInvoicePostedBusinessEvent`: Fires when a vendor invoice is posted in D365 FO accounts payable.
* **Vendor Payment Journal Posted** `VendPaymentJournalPostedBusinessEvent`
* **Vendor Payment Journal Posted** `VendPaymentJournalPostedBusinessEvent`: Fires when a vendor payment journal is posted in D365 FO
* **Vendor Payment Journal Posted** `VendPaymentJournalPostedBusinessEvent`: Fires when a vendor payment journal is posted in D365 FO.
* **Vendor Payment Journal Posted** `VendPaymentJournalPostedBusinessEvent`: Fires when a vendor payment journal is posted in D365 FO.
* **Worker Created** `HcmWorkerCreatedBusinessEvent`: Fires when a new worker (employee or contractor) is created in the HCM module.
* **Worker Created** `HcmWorkerCreatedBusinessEvent`: Fires when a new worker is created in D365 FO HCM.
* **Worker Updated** `HcmWorkerUpdatedBusinessEvent`: Fires when a worker record is updated in the HCM module.
* **Worker Updated** `HcmWorkerUpdatedBusinessEvent`: Fires when a worker record is updated in D365 FO HCM.

</details>
