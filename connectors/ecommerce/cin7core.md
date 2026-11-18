---
description: "Cin7 Core (formerly DEAR Inventory) — cloud inventory, sales, purchasing, production and accounting management."
hidden: true
---

# Cin7 Core

<img src="../../.gitbook/assets/connectors/lg/cin7core.png" alt="Cin7 Core logo">

Cin7 Core (formerly DEAR Inventory) — cloud inventory, sales, purchasing, production and accounting management. Wraps the Cin7 Core External API V2 (https://inventory.dearsystems.com/externalapi/v2/).

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [dearsystems.com](https://dearsystems.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `cin7core` |

## Use it

Add Cin7 Core from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cin7core.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Authorise Production Order | `authoriseProductionOrder` | Authorises a Production Order and recalculates capacity. Body (JSON string) requires productionOrderID. |
| Complete Production Run | `completeProductionRun` | Completes a Run. Body (JSON string) requires ProductionOrderID, ProductionRunID, EffectiveDate, and FinishedProducts[] (each: Quantity, WastageQuantity, Received, ReceivedDate, LocationID, ProductID, BatchSN, ExpiryDate). |
| Complete Run Operation | `completeRunOperation` | Completes a Run operation. Body (JSON string) requires ProductionOrderID, ProductionRunID, RunOperationID, and AutoGenerateBatchSerialNumbers (bool, REQUIRED by the API). Optional: WithAutoConsume, WithoutOutput, ManualEndDate, FinishedProducts[] (Quantity, WastageQuantity, BatchSN, ExpiryDate, ReceivedDate, LocationID, ProductID). |
| Create Account | `createAccount` | Create a chart-of-accounts account. POST /ref/account. Pass full JSON object as a string in body. Required: Code, Name, Type (BANK, CURRLIAB, LIABILITY, TERMLIA, PAYGLIABILITY, SUPERANNUATIONLIABILITY, WAGESPAYABLELIABILITY, CURRENT, EXPENSE etc), Status. Optional: Description, Class (ASSET, LIABILITY, EXPENSE, EQUITY, REVENUE), SystemAccount, SystemAccountCode, ForPayments, Bank/BankAccountNumber (required if Type=BANK). |
| Create Advanced Purchase | `createAdvancedPurchase` | Create an Advanced Purchase. POST /advanced-purchase. Body (JSON string): (SupplierID or Supplier) required, Approach (INVOICE\|STOCK) required, Location required, PurchaseType (Simple\|Advanced), IsServiceOnly, Contact, Phone, BlindReceipt, TaxRule, TaxCalculation, Terms, RequiredBy, Note, CurrencyRate, BillingAddress, ShippingAddress, AdditionalAttributes. |
| Create Advanced Purchase Credit Note | `createAdvancedPurchaseCreditNote` | Create an Advanced Purchase Credit Note task. POST /advanced-purchase/creditnote. Body (JSON string): PurchaseID, TaskID (optional), CreditNoteNumber, CreditNoteDate, Status (DRAFT\|AUTHORISED), Lines, AdditionalCharges, Unstock. |
| Create Advanced Purchase Invoice | `createAdvancedPurchaseInvoice` | Create an Advanced Purchase Invoice task. POST /advanced-purchase/invoice. Body (JSON string): PurchaseID, TaskID (optional), Status (DRAFT\|AUTHORISED), InvoiceDate, InvoiceDueDate, Lines [{ProductID,SKU,Name,Quantity,Price,Discount,Tax,TaxRule,Account,Comment,Total}], AdditionalCharges. |
| Create Advanced Purchase Manual Journal | `createAdvancedPurchaseManualJournal` | Create/update Advanced Purchase Manual Journal. POST /advanced-purchase/manualJournal. Body (JSON string): TaskID, Status (DRAFT\|AUTHORISED), Lines [{Reference,Amount,Date,Debit,Credit}]. IsSystem lines cannot be modified. |
| Create Advanced Purchase Payment | `createAdvancedPurchasePayment` | Create an Advanced Purchase Payment/Prepayment/Refund. POST /advanced-purchase/payment. Body (JSON string): TaskID, Type (PREPAYMENT\|PAYMENT\|REFUND), Amount, DatePaid, Account, CurrencyRate, Reference, DepositID. |
| Create Advanced Purchase Put Away | `createAdvancedPurchasePutAway` | Create an Advanced Purchase Put Away task. POST /advanced-purchase/put-away. Body (JSON string): PurchaseID, TaskID, Status (DRAFT\|AUTHORISED), Lines [{Date,Quantity,ProductID,SKU,Name,LocationID,Location,Received,BatchSN,SupplierSKU,ExpiryDate}]. |
| Create Advanced Purchase Stock Received | `createAdvancedPurchaseStock` | Create Advanced Purchase Stock Received task. POST /advanced-purchase/stock. Pass each field as its own input (the body is built from them). Required: PurchaseID, Status (DRAFT\|AUTHORISED), Lines [{Date,Quantity,ProductID,SKU,Name,LocationID,Location,Received,BatchSN,SupplierSKU,ExpiryDate}]. Optional: TaskID (the stock receiving task to add to or update). |
| Create Attribute Set | `createAttributeSet` | Create an attribute set. POST /ref/attributeset. Pass the full JSON object as a string in body. Fields: Name (string, required), Attribute1Name..Attribute10Name (string), Attribute1Type..Attribute10Type (string: List, Checkbox, Text, Not used), Attribute1Values..Attribute10Values (string, comma-separated for List type). |
| Create Bank Transfer | `createBankTransfer` | Create a Bank Transfer. Pass full JSON object as string in 'body'. Fields: Status(req DRAFT\|COMPLETED), FromAccount(req), ToAccount(req), FromAmount(req), ToAmount(req), Date(req), CurrencyConversionRate, Reference, Note. |
| Create Brand | `createBrand` | Create a new product brand in Cin7 Core. POST /ref/brand. Field: Name (string, required) — the brand name. |
| Create Carrier | `createCarrier` | Create a carrier. POST /ref/carrier. Pass Description as an input (the body is built from it). Required: Description (string). |
| Create CRM Task | `createCrmTask` | Create a CRM task. POST /crm/task. Body (JSON string) fields: Name (string, required), EntityType (required; one of Purchase, Sale, Customer, Supplier, Lead, Opportunity, Assembly, Disassembly, Job, Inventory write off, Expense Claim Receipt, Expense Claim, Journal, Production), EntityID (GUID, required), StartDate (DateTime, required), EndDate (DateTime, required), TaskStatus (required), Description, IsAllDay (bool), CompletedDate, Category, WorkflowName, AssignedTo, IsImportant (bool), AssignedBy, VoidDate. |
| Create Custom Price | `createCustomPrice` | Create customer-specific product prices. POST /customPrices (NOTE: live path is /customPrices, not /custom-prices as the apib documents). Pass full JSON object as a string in body. Shape: {CustomPrices:[{CustomerID (Guid), ProductSKU, Price}]}. |
| Create Customer | `createCustomer` | Create a Customer in Cin7 Core. Pass the full JSON as a string in 'body'. Required: Name. Common fields: Currency, PaymentTerm (must exist), TaxRule (must exist), AccountReceivable (account code), RevenueAccount (account code), PriceTier, Status, Discount, Addresses[], Contacts[]. Returns the created customer in CustomerList. |
| Create Customer Full | `createCustomerFull` | Create a Cin7 Core customer with the FULL nested payload, including Contacts[] and Addresses[]. Pass the complete customer object as 'body'. The standard createCustomer action only forwards flat scalar fields and drops nested arrays; this passthrough action sends the whole body so nested contacts/addresses persist. |
| Create Customer Template | `createCustomerTemplate` | Assign default templates to customers. POST /ref/customer/templates. Pass full JSON object as a string in body. Shape: {"CustomerTemplates":[{"CustomerID":Guid,"TemplateID":Guid}]}. |
| Create Deal | `createDeal` | Create a product deal. POST /reference/deals. Pass full JSON object as a string in body. Required: Name, CustomersGroup (All, B2B, POS, Specified, CustomerTags). Optional DealDiscounts array (each {DiscountName, DiscountType, DiscountID, Sequence, IsOrderLevel, DealDiscountBrands, DealDiscountCategories, DealDiscountTags, DealDiscountProducts}). |
| Create Disassembly | `createDisassembly` | Create a new Disassembly. Pass full JSON object as string in 'body'. Fields: Status(req — POST accepts only WORK IN PROGRESS or COMPLETED), ProductID or ProductCode(req), LocationID or Location(req), WIPAccount(req), Quantity(req). WORK IN PROGRESS auto-adds pick items; COMPLETED auto-adds pick+order items and completes. Product must be an assembled/BOM product with sufficient on-hand stock to disassemble. |
| Create Disassembly Order | `createDisassemblyOrder` | Create or update Disassembly Order. Pass full JSON object as string in 'body'. Fields: TaskID(req), Status(req WORK IN PROGRESS\|COMPLETED), CompletionDate, OrderLines(array), OrderServiceLines(array). |
| Create Factory Calendar | `createFactoryCalendar` | Creates a Factory Calendar. Body (JSON string) requires Year (Short), WeekStart (DayOfWeek string), FactoryCalendarDays (array of 7 days each with DayOfWeek, IsWeekend, StartTime, EndTime in minutes 0-1440, optional BreakStartTime/BreakEndTime), optional FactoryCalendarSpecialDays (Date within year, IsHoliday, IsWeekend, StartTime, EndTime, Comment). |
| Create Family Production BOM | `createFamilyProductionBOM` | Creates new Production BOM(s) for a specified product family. Body (JSON string) requires ProductFamilyID and a ProductionBOMs array. NOTE: despite the blueprint marking them readonly, the live API REQUIRES Version (int) and IsDefault (bool) on each BOM in the array, plus OutputQuantity, BufferPercent and Operations[] (each Operation: Order, Name, CycleTime, UnitsPerCycle, WorkCenterID, OperationType, IsDropShip). Operations may include VariationComponents for family BOMs. |
| Create Finished Good | `createFinishedGood` | Create a new Finished Goods task. Pass full JSON object as string in 'body'. Fields: Status(req DRAFT\|AUTHORISED\|IN PROGRESS\|COMPLETED), ProductID or ProductCode(req), LocationID or Location(req), WIPAccount(req), WIPDate(req if not DRAFT), Account(req), Quantity(req), CompletionDate(req if COMPLETED), BinID, Bin, BatchSN, ExpiryDate, Notes, CustomField1-10. |
| Create Finished Goods Order | `createFinishedGoodsOrder` | Create or update a Finished Goods Order. Pass full JSON object as string in 'body'. Fields: TaskID(req), Status(req DRAFT\|AUTHORISED), OrderLines(array: ProductID/ProductCode, Name, ExpenseAccount, Quantity, Unit, WastagePercent). |
| Create Finished Goods Pick | `createFinishedGoodsPick` | Create or update a Finished Goods Pick. Pass full JSON object as string in 'body'. Fields: TaskID(req), Status(req AUTHORISED\|IN PROGRESS\|COMPLETED), WIPAccount, WIPDate, Account, CompletionDate(req), PickLines(array: ProductID/ProductCode, Name, Quantity, Unit, Cost). |
| Create Fixed Asset Type | `createFixedAssetType` | Create a fixed asset type. POST /ref/fixedassettype. Pass full JSON object as a string in body. Required: Name, DepreciationMethod, AveragingMethod, AssetAccountCode, AccumulatedDepreciationAccountCode, DepreciationExpenseAccountCode. Optional: Rate, EffectiveLife. |
| Create Inventory Write-Off | `createInventoryWriteOff` | Create a new Inventory Write-Off. Pass full JSON object as string in 'body'. Fields: Status(req DRAFT\|COMPLETED), LocationID or Location(req), Account(req), EffectiveDate(req if COMPLETED), Notes, Lines(array: ProductID/ProductCode, Name, BinID, Bin, BatchSN, ExpiryDate, ExpenseAccount, Quantity, Cost). |
| Create Journal | `createJournal` | Create a new Journal. Pass full JSON object as string in 'body'. Fields: Status(req DRAFT\|COMPLETED), Currency(req), CurrencyConversionRate(req), EffectiveDate(req), Narration, Notes, Lines(array: Debit, Credit, Reference, Amount, BaseAmount). |
| Create Lead | `createLead` | Create a CRM lead. POST /crm/lead. Body (JSON string) fields: Name (string, required), Currency (string 3-char code, required), LeadStatus (required; one of NEW, ATTEMPTING TO CONTACT, QUALIFIED, DISQUALIFIED), PaymentTerm (string, required), PriceTier (string, required), SalesRepresentative (string, required), TaxRule (string, required), CloseChance (int, required, e.g. 0,10,20...), CloseDate (DateTime, required), Amount (decimal), Comments (string), Addresses (array of address objects: Type, Line1, Line2, City, State, Postcode, Country, DefaultForType), Contacts (array of contact objects: Name, JobTitle, Phone, MobilePhone, Fax, Email, Website, Default, Comment, IncludeInEmail). |
| Create Location | `createLocation` | Create a location. POST /ref/location. Pass full JSON object as a string in body. Required: Name. Optional address fields (AddressLine1, AddressLine2, AddressCitySuburb, AddressStateProvince, AddressZipPostCode, AddressCountry), IsShopfloor, IsCoMan, IsStaging, Bins. |
| Create Me Address | `createMeAddress` | Create a Me address. Pass full JSON object as string in 'body'. Fields: Line1(req), Line2, CitySuburb(req), StateProvince(req), ZipPostCode(req), Country(req), Type(req Billing\|Business\|Shipping), DefaultForType(bool). |
| Create Me Contact | `createMeContact` | Create a Me contact. Pass full JSON object as string in 'body'. Fields: Name(req), Phone, Fax, Email, Website, Comment, Type(Billing\|Business\|Sale\|Shipping\|Employee), DefaultForType(bool). |
| Create Money Operation | `createMoneyOperation` | Create a Receive/Spend Money task. Pass full JSON object as string in 'body'. Fields: TaskType(req Spend Money\|Receive Money), Status(req DRAFT\|COMPLETED), BankAccount(req), Date(req), CurrencyConversionRate, SupplierID/CustomerID (mutually exclusive), Reference, TaxInclusive, Note, Lines(array: Name, Comment, Quantity, Price, Discount, Tax, TaxRuleName, AccountCode, Total). |
| Create Opportunity | `createOpportunity` | Create a CRM opportunity. POST /crm/opportunity. Body (JSON string) required fields: CustomerName, BillingAddressLine1, Currency, CustomerCurrency, TaxRule, Terms, PriceTier, OpportunityLocation, TermMethod (int), TermDueNextMonth (int), SalesRepresentative (must exist in Company Contacts), ShipToOther (bool). Also: CustomerID or LeadID, Contact, Phone, DefaultAccount, TaxPercent, TaxInclusive, TermDays, TaxTotal, Total, OpportunityStatus (DRAFT/IN PROGRESS/WON/LOST), OpportunityComment, OpportunityMemo, CustomerReference, CurrencyConversionRate, ShipTo* fields, CustomField1-10, Lines (array: ProductID or ProductName or ProductSKU, Quantity, Price, Tax, Total, TaxRule, TaxPercent, Discount, Comment), AdditionalCharges (array: Description, Quantity, Amount, Tax, Total, TaxRule, TaxPercent, Discount, Comment). |
| Create Payment Term | `createPaymentTerm` | Create a payment term. POST /ref/paymentterm. Pass full JSON object as a string in body. Required: Name, Duration (int), Method (e.g. 'number of days','days since the end of the month','last day of next month'). Optional: IsActive (bool), IsDefault (bool). |
| Create Product | `createProduct` | Create a new product in Cin7 Core. Required: SKU, Name, Category, Type, CostingMethod, UOM, Status, and PriceTier1 (the API requires at least one non-empty price tier). PriceTier2–10 default to 0 if not provided — supply them to set tiered pricing at creation time. |
| Create Product Category | `createProductCategory` | Create a product category. POST /ref/category. Pass full JSON object as a string in body. Required: Name. |
| Create Product Discount | `createProductDiscount` | Create product discount rule(s). POST /reference/discount. Pass full JSON object as a string in body. Shape: {DiscountRules:[{Name, IsActive, Type (Simple, QuantityBased, FreeShipping), DiscountLines:[{MinValue, MaxValue, DiscountType (DiscountAmount, DiscountPercent, MarkupAmount, MarkupPercent, PriceOverride, FlatAmount, FreeShipping), Amount, OrderExceeds}]}]}. |
| Create Product Family | `createProductFamily` | Create a Product Family in Cin7 Core. Pass the full JSON as a string in 'body'. Required: SKU (unique), Name, Category (must exist), CostingMethod, DefaultLocation (must exist), UOM (must exist), Option1Name. Optional: Brand, PriceTier1..10, accounts, tax rules, Products[], DropShipMode, HSCode, CountryOfOrigin. |
| Create Product Supplier | `createProductSupplier` | Create Product Supplier sourcing settings. Pass the full JSON as a string in 'body'. Body shape: {"ProductSuppliers":[{SupplierID, ProductID, Cost, FixedCost, Currency, PurchaseCost, DropShip, SupplierInventoryCode, SupplierProductName, SupplierProductURL, ProductSupplierOptions:[{LocationID, LocationName, ReorderQuantity, Lead, Safety, MinimumToReorder, SupplyIntervals:[]}]}]}. Returns {Success:true}. |
| Create Production BOM | `createProductionBOM` | Creates new Production BOM(s) for a specified product. Body (JSON string) requires ProductID and a ProductionBOMs array. Each BOM: OutputQuantity, BufferPercent, Version, Name, IsDefault, and Operations[] (each Operation: Order, Name, CycleTime seconds, UnitsPerCycle, WorkCenterID, OperationType, IsDropShip, plus Resources/Components/Attachments/Notes/OperationLinks). |
| Create Production Order | `createProductionOrder` | Creates a new Production Order. Body (JSON string) requires ProductID, LocationID, Quantity, and typically CapacityCalculationType (FromStartForward/FromRequiredBackward), StartDate or RequiredByDate, BOMVersion, FinishedGoodsAccountCode, WIPAccountCode. Optional query param RecalculateDates triggers capacity calculation. |
| Create Production Resource | `createProductionResource` | Creates production resource(s). Body (JSON string) requires a Resources array. Each resource: Name (required), ResourceType (Labor/Machine/Other), CycleDuration (1-7776000 seconds), optional Code, IsActive flags, Tags, ResourceCapacities, ResourceCosts, ResourceRemarks, ResourceAttachments. |
| Create Production Run | `createProductionRun` | Creates new Runs for a Production Order. Body (JSON string) requires ProductionOrderID and a Runs array (each Run: Quantity, optional WIPAccount); optional IncreaseOrderQuantity (bool). |
| Create Purchase | `createPurchase` | Create a Simple Purchase. POST /purchase. Pass each field as its own input (the body is built from them). Required: Approach (INVOICE\|STOCK), Location, and Supplier or SupplierID. Optional: Contact, Phone, BlindReceipt, TaxRule (overrides the supplier default), TaxCalculation (Inclusive\|Exclusive), Terms, RequiredBy, Note, CurrencyRate, BillingAddress, ShippingAddress, AdditionalAttributes. |
| Create Purchase Credit Note | `createPurchaseCreditNote` | Create Simple Purchase Credit Note. POST /purchase/creditnote. Body (JSON string): TaskID, CreditNoteNumber, CreditNoteDate, Status (DRAFT\|AUTHORISED), Lines, AdditionalCharges, Unstock [{CardID,Date,Quantity,ProductID,SKU,Name,Location,BatchSN,ExpiryDate}]. |
| Create Purchase Invoice | `createPurchaseInvoice` | Create Simple Purchase Invoice. POST /purchase/invoice. Body (JSON string): TaskID, Status (DRAFT\|AUTHORISED), InvoiceDate, InvoiceDueDate, Lines [{ProductID,SKU,Name,Quantity,Price,Discount,Tax,TaxRule,Account,Comment,Total}], AdditionalCharges, CombineAdditionalCharges. |
| Create Purchase Manual Journal | `createPurchaseManualJournal` | Create/update Simple Purchase Manual Journal. POST /purchase/manualJournal. Body (JSON string): TaskID, Status (DRAFT\|AUTHORISED), Lines [{Reference,Amount,Date,Debit,Credit}]. IsSystem lines cannot be modified. |
| Create Purchase Order | `createPurchaseOrder` | Create/update a Simple Purchase Order. POST /purchase/order. Pass each field as its own input (the body is built from them). Required: TaskID, Status (DRAFT\|AUTHORISED), Memo, Lines [{ProductID,SKU,Name,Quantity,Price,Discount,Tax,TaxRule,SupplierSKU,Comment,Total}]. Optional: AdditionalCharges (e.g. freight), CombineAdditionalCharges. |
| Create Purchase Payment | `createPurchasePayment` | Create a Simple Purchase Payment/Prepayment/Refund. POST /purchase/payment. Body (JSON string): TaskID, Type (PREPAYMENT\|PAYMENT\|REFUND), Amount, DatePaid, Account, CurrencyRate, Reference, DepositID. Payments require authorised invoice; refunds require authorised credit note. |
| Create Purchase Stock Received | `createPurchaseStock` | Add/authorise Simple Purchase Stock Received. POST /purchase/stock. Body (JSON string): TaskID, Status (DRAFT\|AUTHORISED), Lines [{Date,Quantity,ProductID,SKU,Name,Location,LocationID,Received,BatchSN,SupplierSKU,ExpiryDate,CardID}]. Empty Lines authorises. |
| Create Sale | `createSale` | Creates a sale in Cin7 Core for a customer given by Customer (name) or CustomerID, covering contact details, billing and shipping addresses, tax and payment terms, carrier and fulfilment mode, dates, references and the ten custom attribute slots. Required: Location, and Customer or CustomerID. Returns the created sale with its generated order and invoice numbers. |
| Create Sale Credit Note | `createSaleCreditNote` | Create or update a sale credit note task. Pass JSON as a STRING in 'body'. Required: SaleID, TaskID (empty GUID to create new), CreditNoteInvoiceNumber, Status, CreditNoteDate. Fails if credit note status not DRAFT/NOT AVAILABLE or invoice not AUTHORISED/PAID. |
| Create Sale Fulfilment | `createSaleFulfilment` | Create a new fulfilment task for a sale. Pass JSON as a STRING in 'body'. Required: SaleID. Fails if order status not AUTHORISED. |
| Create Sale Fulfilment Pack | `createSaleFulfilmentPack` | Create/add lines to the pack for a fulfilment task. Pass JSON as a STRING in 'body'. Required: TaskID, Status (DRAFT or AUTHORISED), Lines. Fails if Pick status is DRAFT/NOT AVAILABLE or Pack status not DRAFT/NOT AVAILABLE. |
| Create Sale Fulfilment Pick | `createSaleFulfilmentPick` | Create/set the pick for a fulfilment task. Pass JSON as a STRING in 'body'. Required: TaskID, Status (DRAFT or AUTHORISED), Lines. Optional AutoPickMode=AUTOPICK. Fails if Pick status not DRAFT/NOT AVAILABLE or order not AUTHORISED. |
| Create Sale Fulfilment Ship | `createSaleFulfilmentShip` | Create/add shipment lines for a fulfilment task. Pass JSON as a STRING in 'body'. Required: TaskID, Status (DRAFT/PARTIALLY AUTHORISED/AUTHORISED), Lines. Fails if Pack status not AUTHORISED or Ship already AUTHORISED. |
| Create Sale Invoice | `createSaleInvoice` | Create or update a sale invoice task. Pass each field as its own input (the body is built from them). Required: SaleID, TaskID (use the empty GUID 00000000-0000-0000-0000-000000000000 to create new), Status. Optional: InvoiceDate, InvoiceDueDate (Cin7 uses the customer terms when left out), CurrencyConversionRate, Memo, Lines, AdditionalCharges (e.g. freight), billing address lines. Fails if invoice status not DRAFT/NOT AVAILABLE or order not AUTHORISED. |
| Create Sale Manual Journal | `createSaleManualJournal` | Create or update manual journals for a sale. Pass JSON as a STRING in 'body'. Required: SaleID, Status (DRAFT or AUTHORISED), Lines. |
| Create Sale Order | `createSaleOrder` | Create or update the order for a sale. Pass each field as its own input (the body is built from them). Required: SaleID, Status (DRAFT or AUTHORISED), Memo, Lines. Optional: AutoPickPackShipMode (NOPICK/AUTOPICK/AUTOPICKPACK/AUTOPICKPACKSHIP), AdditionalCharges. POST fails if Order status not DRAFT/NOT AVAILABLE or Quote not AUTHORISED. |
| Create Sale Payment | `createSalePayment` | Create a payment/prepayment/refund for a sale task. Pass JSON as a STRING in 'body'. Required: TaskID, Type, Amount, DatePaid, Account, CurrencyRate. |
| Create Sale Quote | `createSaleQuote` | Create or update the quote for a sale. Pass the full JSON as a STRING in 'body'. Required: SaleID, Status (DRAFT or AUTHORISED), Lines. POST fails if Quote status is not DRAFT/NOT AVAILABLE or SkipQuote is true. |
| Create Ship Zone | `createShipZone` | Create a shipping zone. POST /reference/shipZones. Pass full JSON object as a string in body. Required: Name, IsRestZone, PricesInclTax, Negative, TaxRuleID (Guid). Optional AppliesTo array ({Country2, StateID, StateName, PostCodeFrom, PostCodeTo, PostCodesList, ShippingRate}), Conditions array ({MinValue, MaxValue, ShippingCost, ConditionType (Price\|Weight), ConditionDescription}). |
| Create Stock Adjustment | `createStockAdjustment` | Create a new Stock Adjustment. Documented fields: EffectiveDate (DateTime, required), Status (DRAFT or COMPLETED, required), Reference (required), Account (optional expense account code), Comment, UpdateOnHand (boolean; true sets on-hand to the line quantity), Lines (array of New Stock Line: ProductID/SKU, ProductName, Quantity, UnitCost, LocationID/Location, BatchSN, ExpiryDate, ReceivedDate, Comments; required). |
| Create Stock Take | `createStockTake` | Create a new Stock Take (status IN PROGRESS). Pass full JSON object as string in 'body'. Fields: EffectiveDate(req), Account(req), LocationID or Location (req), Tags(array), PickZones(array), StockLocators(array), Categories/Brands/Bins (array of {ID,Name}), Reference, UseRelativeQuantity(bool). |
| Create Stock Transfer | `createStockTransfer` | Create a new Stock Transfer. Pass full JSON object as string in 'body'. Fields: Status(req DRAFT\|IN TRANSIT\|COMPLETED), From or FromLocation(req), To or ToLocation(req), CompletionDate(req), CostDistributionType, InTransitAccount (req if IN TRANSIT), DepartureDate (req if IN TRANSIT), RequiredByDate, Reference, SkipOrder(bool), Lines(req array: ProductID/SKU, ProductName, TransferQuantity, BatchSN, ExpiryDate, Comments). |
| Create Stock Transfer Order | `createStockTransferOrder` | Create or update a Stock Transfer Order. Pass full JSON object as string in 'body'. Fields: TaskID(req), Status(req DRAFT\|AUTHORISED\|NOT AVAILABLE), Lines(req array: ProductID/SKU, ProductName, TransferQuantity, Comments). |
| Create Supplier | `createSupplier` | Create a Supplier in Cin7 Core. Pass the full JSON as a string in 'body'. Required: Name. Common fields: Currency, PaymentTerm (must exist), TaxRule (must exist), AccountPayable (account code), Status, Discount, AttributeSet, Addresses[], Contacts[]. Returns the created supplier in SupplierList. |
| Create Task Category | `createTaskCategory` | Create a CRM task category. POST /crm/taskcategory. Body (JSON string) fields: Name (string, required), Color (6-char RGB HEX, e.g. F7CAFE), BackgroundColor (6-char RGB HEX). |
| Create Tax | `createTax` | Create a tax rule. POST /ref/tax. Pass full JSON object as a string in body. Required: Name, Account (must be one of the org's valid account codes), IsActive, TaxInclusive, TaxPercent, IsTaxForSale, IsTaxForPurchase, Components (array of {Name, Percent (string), AccountCode, Compound (BOOLEAN true/false), ComponentOrder}). |
| Create Unit Of Measure | `createUnit` | Create a unit of measure. POST /ref/unit. Pass full JSON object as a string in body. Required: Name. |
| Create Webhook | `createWebhook` | Create (register) a webhook subscription. POST /webhooks. Body (JSON string) fields: Type (string, required; one of the supported event types e.g. Sale/Created, Sale/OrderAuthorised, Stock/AvailableStockLevelChanged, Lead/Updated, Opportunity/Voided, Task/Overdue, etc.), IsActive (bool, required), ExternalURL (string, required; callback URL), ExternalAuthorizationType (required; one of noauth, basicauth, bearerauth), ExternalUserName/ExternalPassword (required if basicauth), ExternalBearerToken (required if bearerauth), ExternalHeaders (array of {Key, Value}). |
| Create Work Center | `createWorkCenter` | Creates work center(s). Body (JSON string) requires a Workcenters array. Each: Code, Name, IsActive, IsCoMan, IsCoManPurchase; SupplierID and CoManProcurementType (Transfer/Buysell/Purchase) required for co-man; optional WorkCenterLocations[] (LocationID, Type Consumption/Output), WorkCenterSuppliers[]. |
| Create Workflow | `createWorkflow` | Create a CRM workflow. POST /crm/workflow. Body (JSON string) fields: Name (string, required), EntityType (required; same types as Task), DueDaysType (required; COMPLETED_DATE or START_DATE), IsActive (bool), Steps (array of WorkflowStep: Name (required), Category, Days (int), StartTime (hh:mm:ss), EndTime (hh:mm:ss), UserName, SkipHoliday (required; one of move_next, move_previous, leave, ph_move_next, ph_move_previous)). |
| Delete Account | `deleteAccount` | Delete a chart-of-accounts account by Code. DELETE /ref/account?Code={Code}. NOTE: live account deletes are blocked ('Old code is required') when the org has Xero/Quickbooks integration enabled. |
| Delete Advanced Purchase Credit Note | `deleteAdvancedPurchaseCreditNote` | Void/delete an Advanced Purchase Credit Note task. DELETE /advanced-purchase/creditnote?TaskID=. |
| Delete Advanced Purchase Invoice | `deleteAdvancedPurchaseInvoice` | Void/delete an Advanced Purchase Invoice task. DELETE /advanced-purchase/invoice?TaskID=&Void=. |
| Delete Advanced Purchase Payment | `deleteAdvancedPurchasePayment` | Delete an Advanced Purchase Payment. DELETE /advanced-purchase/payment?ID=&DeleteAllocation=. |
| Delete Advanced Purchase Stock Received | `deleteAdvancedPurchaseStock` | Void/delete an Advanced Purchase Stock Received task. DELETE /advanced-purchase/stock?TaskID=&Void=. |
| Delete Attribute Set | `deleteAttributeSet` | Delete an attribute set by ID. DELETE /ref/attributeset?ID={ID}. |
| Delete Brand | `deleteBrand` | Delete a brand by ID. DELETE /ref/brand?ID={ID}. |
| Delete Carrier | `deleteCarrier` | Delete a carrier. DELETE /ref/carrier?CarrierID={CarrierID}. Live API requires the CarrierID query param (the apib documents ?ID= but the API rejects ID). |
| Delete Custom Price | `deleteCustomPrice` | Delete a customer-specific product price. DELETE /custom-prices?ProductID={ProductID}&CustomerID={CustomerID}. NOTE: POST/PUT use /customPrices, but DELETE is documented under /custom-prices. The /customPrices path returns 405 for DELETE and /custom-prices is currently returning a 502 gateway error server-side; the delete endpoint appears unreliable on this account. |
| Delete Customer Template | `deleteCustomerTemplate` | Remove a default template assignment from a customer. DELETE /ref/customer/templates?TemplateId={TemplateId}&CustomerId={CustomerId}. |
| Delete Family Production BOM | `deleteFamilyProductionBOM` | Deletes a Production BOM of a product family. NOTE: The Cin7 Core API v2 production/productionBOM endpoint returns HTTP 405 'DELETE not supported' on the live API — hard delete is not supported by the provider despite being in the blueprint. Action wiring (path/auth/params ProductFamilyID & BOMID) is correct. |
| Delete Location | `deleteLocation` | Delete a location by ID. DELETE /ref/location?ID={ID}. |
| Delete Me Address | `deleteMeAddress` | Delete a Me address by ID. |
| Delete Me Contact | `deleteMeContact` | Delete a Me contact by ID. |
| Delete Payment Term | `deletePaymentTerm` | Delete a payment term by ID. DELETE /ref/paymentterm?ID={ID}. |
| Delete Product Attachment | `deleteProductAttachment` | Delete a Product attachment by its attachment ID. Pass ID as query parameter. Returns the remaining/deleted attachment list. |
| Delete Product Category | `deleteProductCategory` | Delete a product category by ID. DELETE /ref/category?ID={ID}. |
| Delete Product Family Attachment | `deleteProductFamilyAttachment` | Delete a Product Family attachment by its attachment ID. Pass ID as a query parameter. Returns the remaining attachment list. |
| Delete Product Supplier | `deleteProductSupplier` | Delete the specified Product Supplier settings (with their Options and Intervals). Pass ProductID and SupplierID as required query parameters. Returns {Success:true}. |
| Delete Production BOM | `deleteProductionBOM` | Deletes a Production BOM of a product. NOTE: The Cin7 Core API v2 production/productionBOM endpoint returns HTTP 405 'DELETE not supported' on the live API — hard delete is not supported by the provider despite being in the blueprint. Action wiring (path/auth/params ProductID & BOMID) is correct. |
| Delete Production Order Attachment | `deleteProductionOrderAttachment` | Deletes a Production Order attachment by ProductionOrderAttachmentID. |
| Delete Production Resource | `deleteProductionResource` | Deletes a production resource by ResourceID. NOTE: The Cin7 Core API v2 production/resource endpoint returns HTTP 405 'DELETE not supported' on the live API — hard delete is not supported by the provider (only SalePayments supports DELETE in v2). To deactivate a resource, use Update Production Resource with IsActive=false. Action wiring (path/auth/param) is correct. |
| Delete Purchase Attachment | `deletePurchaseAttachment` | Delete a Simple Purchase Attachment. DELETE /purchase/attachment?ID=. |
| Delete Purchase Payment | `deletePurchasePayment` | Delete a Simple Purchase Payment. DELETE /purchase/payment?ID=&DeleteAllocation=. |
| Delete Sale | `deleteSale` | Delete/void a Cin7 Core sale by ID. Maps to DELETE /sale?ID=&Void=. NOTE: this is Cin7's Void endpoint — Void=true voids an AUTHORISED sale; it does NOT delete or void an unauthorised draft (ORDERING/ESTIMATED/QUOTE), which returns 200 with no change. Unauthorised drafts can only be removed from the Cin7 web UI. |
| Delete Sale Attachment | `deleteSaleAttachment` | Delete a sale attachment by ID. |
| Delete Sale Credit Note | `deleteSaleCreditNote` | Void or undo a sale credit note task by TaskID. Only for Advanced Sale. Void=true voids, false undoes. |
| Delete Sale Fulfilment | `deleteSaleFulfilment` | Void or undo a sale fulfilment task by TaskID. Only for Advanced Sale. Void=true voids, false undoes. |
| Delete Sale Invoice | `deleteSaleInvoice` | Void or undo a sale invoice task by TaskID. Only for Advanced Sale. Void=true voids, false undoes. |
| Delete Sale Payment | `deleteSalePayment` | Delete a sale payment by ID. Returns {Success:true}. |
| Delete Ship Zone | `deleteShipZone` | Delete a shipping zone. DELETE /reference/shipZone?ShipZoneID={ShipZoneID} (singular path — the plural /reference/shipZones returns 405 for DELETE). NOTE: this endpoint is currently returning a 502 gateway error server-side; the delete operation appears unavailable on this account. |
| Delete Unit Of Measure | `deleteUnit` | Delete a unit of measure by ID. DELETE /ref/unit?ID={ID}. |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription. DELETE /webhooks?ID={ID}. Provide the webhook ID to delete. |
| Delete Work Center | `deleteWorkCenter` | Deletes a work center by WorkCenterId. NOTE: The Cin7 Core production work center endpoint (/production/workCenter) returns HTTP 405 'DELETE not supported' on the live API — hard delete is not supported by the provider. To deactivate a work center, use Update Work Center with IsActive=false instead. Action wiring (path/auth/param) is correct. |
| Get Account Info (Me) | `getMe` | Retrieve information about the current Cin7 Core account/organisation (company name, currency, base settings). Good first call to verify connectivity. |
| Get Advanced Purchase | `getAdvancedPurchase` | Get a single Advanced Purchase by ID. GET /advanced-purchase?ID=&CombineAdditionalCharges=. |
| Get Advanced Purchase Credit Note | `getAdvancedPurchaseCreditNote` | Get Advanced Purchase Credit Notes. GET /advanced-purchase/creditnote?PurchaseID=&CombineAdditionalCharges=. Returns PurchaseID and CreditNotes array. |
| Get Advanced Purchase Invoice | `getAdvancedPurchaseInvoice` | Get Advanced Purchase Invoices. GET /advanced-purchase/invoice?PurchaseID=&CombineAdditionalCharges=. Returns PurchaseID and Invoices array. |
| Get Advanced Purchase Manual Journals | `getAdvancedPurchaseManualJournals` | Get Advanced Purchase Manual Journals. GET /advanced-purchase/manualJournal?PurchaseID=. |
| Get Advanced Purchase Payments | `getAdvancedPurchasePayments` | Get Advanced Purchase Payments. GET /advanced-purchase/payment?PurchaseID=&OrderNumber=&InvoiceNumber=&CreditNoteNumber=. Any one filter required. |
| Get Advanced Purchase Put Away | `getAdvancedPurchasePutAway` | Get Advanced Purchase Put Away. GET /advanced-purchase/put-away?PurchaseID=. Returns PurchaseID and PutAway array of tasks. |
| Get Advanced Purchase Stock Received | `getAdvancedPurchaseStock` | Get Advanced Purchase Stock Received. GET /advanced-purchase/stock?PurchaseID=. Returns PurchaseID and StockReceiving array of receipt tasks. |
| Get Bank Transfer | `getBankTransfer` | Get detailed info of a particular Bank Transfer by TaskID. |
| Get Disassembly | `getDisassembly` | Get detailed info of a particular Disassembly by TaskID. |
| Get Disassembly Order | `getDisassemblyOrder` | Get Order info of a particular Disassembly by TaskID. |
| Get Factory Calendar | `getFactoryCalendar` | Returns the Factory Calendar for a given year, including working days and special days. |
| Get Family Production BOM | `getFamilyProductionBOM` | Returns all Production BOMs of a specified product family. |
| Get Finished Good | `getFinishedGood` | Get detailed info of a particular Finished Goods task by TaskID. |
| Get Finished Goods Order | `getFinishedGoodsOrder` | Get Order info of a particular Finished Goods task by TaskID. |
| Get Finished Goods Pick | `getFinishedGoodsPick` | Get Pick info of a particular Finished Goods task by TaskID. |
| Get Inventory Write-Off | `getInventoryWriteOff` | Get detailed info of a particular Inventory Write-Off by TaskID. |
| Get Markup Prices | `getMarkupPrices` | Get all markup price tiers for a product. GET /product/markupprices?ProductID={ProductID}. If a markup does not exist for a tier, MarkupType is 'D'. |
| Get Money Operation | `getMoneyOperation` | Get detailed info of a particular Money Task (Receive/Spend Money) by TaskID. |
| Get Product Attachments | `getProductAttachments` | Returns the list of attachments for a particular Product. Pass ProductID as a query parameter. |
| Get Product Family | `getProductFamily` | Returns a single Product Family with full fields by ID (or filter by Name/Sku/ModifiedSince with pagination). Pass ID as a query parameter for single-fetch. |
| Get Product Family Attachments | `getProductFamilyAttachments` | Returns the list of attachments for a particular Product Family. Pass FamilyID as a query parameter. |
| Get Production BOM | `getProductionBOM` | Returns all Production BOMs of a specified product. |
| Get Production Order | `getProductionOrder` | Returns a Production Order and its nested items by ProductionOrderID. |
| Get Production Order Attachments | `getProductionOrderAttachments` | Returns all attachments of a Production Order: order attachments, operation attachments, and operation resource attachments. |
| Get Production Order Reference Data | `getProductionOrderReferenceData` | Returns accumulated reference data useful for creating and updating production orders: tags, chart of accounts, shop floor locations, logistics paths, work centers, price tiers, accounts, suspend reasons. |
| Get Production Resource | `getProductionResource` | Returns a single production resource by ResourceID, including capacities, costs, remarks and (optionally) attachments. |
| Get Production Run | `getProductionRun` | Returns all Runs for a Production Order. |
| Get Purchase | `getPurchase` | Get a single Simple Purchase by ID. GET /purchase?ID=&CombineAdditionalCharges=. Returns full purchase incl Order, StockReceived, Invoice, CreditNote, ManualJournals, Attachments. |
| Get Purchase Attachments | `getPurchaseAttachments` | Get Simple Purchase Attachments. GET /purchase/attachment?TaskID=. |
| Get Purchase Credit Note | `getPurchaseCreditNote` | Get Simple Purchase Credit Note. GET /purchase/creditnote?TaskID=&CombineAdditionalCharges=. |
| Get Purchase Invoice | `getPurchaseInvoice` | Get Simple Purchase Invoice. GET /purchase/invoice?TaskID=&CombineAdditionalCharges=. |
| Get Purchase Manual Journals | `getPurchaseManualJournals` | Get Simple Purchase Manual Journals. GET /purchase/manualJournal?TaskID=. |
| Get Purchase Order | `getPurchaseOrder` | Get a Simple Purchase Order. GET /purchase/order?TaskID=&CombineAdditionalCharges=. |
| Get Purchase Payments | `getPurchasePayments` | Get Simple Purchase Payments. GET /purchase/payment?TaskID=. Returns array of payments/refunds/prepayments. |
| Get Purchase Stock Received | `getPurchaseStock` | Get Simple Purchase Stock Received. GET /purchase/stock?TaskID=. |
| Get Sale | `getSale` | Get detailed info of a particular sale by ID, including quote, order, fulfilments, invoices, credit notes, payments and optionally transactions. |
| Get Sale Attachments | `getSaleAttachments` | Get the attachments of a particular sale by SaleID. |
| Get Sale Credit Note | `getSaleCreditNote` | Get the credit notes of a particular sale by SaleID. |
| Get Sale Fulfilment | `getSaleFulfilment` | Get the fulfilments (pick/pack/ship) of a particular sale by SaleID. |
| Get Sale Fulfilment Pack | `getSaleFulfilmentPack` | Get the pack of a fulfilment task by TaskID. |
| Get Sale Fulfilment Pick | `getSaleFulfilmentPick` | Get the pick of a fulfilment task by TaskID. |
| Get Sale Fulfilment Ship | `getSaleFulfilmentShip` | Get the shipment of a fulfilment task by TaskID. |
| Get Sale Invoice | `getSaleInvoice` | Get the invoices of a particular sale by SaleID. |
| Get Sale Manual Journals | `getSaleManualJournals` | Get the manual journals of a particular sale by SaleID. |
| Get Sale Order | `getSaleOrder` | Get the order of a particular sale by SaleID. |
| Get Sale Payments | `getSalePayments` | Get the payments (prepayments/payments/refunds) of a particular sale by SaleID. Returns an array. |
| Get Sale Quote | `getSaleQuote` | Get the quote of a particular sale by SaleID. |
| Get Ship Zones Enabled | `getShipZonesEnabled` | Check whether shipping zones are enabled. GET /reference/shipZonesEnabled. |
| Get Stock Adjustment | `getStockAdjustment` | Get detailed info of a particular Stock Adjustment by TaskID. |
| Get Stock Take | `getStockTake` | Get detailed info of a particular Stock Take by TaskID. |
| Get Stock Transfer | `getStockTransfer` | Get detailed info of a particular Stock Transfer by TaskID. |
| Get Stock Transfer Order | `getStockTransferOrder` | Get detailed info of a particular Stock Transfer Order by TaskID. |
| List Account Receivable | `listAccountReceivable` | List accounts receivable (A/R) accounts from the Cin7 Core chart of accounts. Returns general ledger accounts with Type=CURRENT - every one carries SystemAccount 'Accounts receivable', including per-currency A/R accounts (AUD, CAD, EUR, GBP, INR, LKR, NZD, USD) and any custom-named A/R accounts. Optionally narrow by Code, Name or Status. |
| List Active Sale Taxes | `listActiveSaleTaxes` | List only ACTIVE Cin7 tax rules that apply to sales (IsActive=true & IsTaxForSale=true). Used to populate the widget Tax Rule dropdowns so inactive/non-sale rules are not selectable. Same endpoint as listTaxes with server-side filters baked in. |
| List Attribute Sets | `listAttributeSets` | Retrieve attribute sets (custom attribute definitions) defined in Cin7 Core. Supports paging and filtering by ID or Name. |
| List Bank Accounts | `listBankAccounts` | Retrieve bank accounts from the chart of accounts in Cin7 Core. |
| List Brands | `listBrands` | Retrieve product brands defined in Cin7 Core. |
| List Carriers | `listCarriers` | Retrieve shipping carriers defined in Cin7 Core. |
| List Chart of Accounts | `listChartOfAccounts` | Retrieve the chart of accounts (general ledger accounts) from Cin7 Core. Filter by Code, Name, Type or Status. |
| List CRM Tasks | `listCrmTasks` | List CRM tasks with pagination and filters. GET /crm/task. |
| List Customer Credits | `listCustomerCredits` | Retrieve customer credit notes/credits available in Cin7 Core. |
| List Customer Templates | `listCustomerTemplates` | List customer default templates. GET /ref/customer/templates. Optional query params: Page, Limit, CustomerId (Guid). |
| List Customers | `listCustomers` | Retrieve customers from Cin7 Core. Supports filtering by ID, Name, ModifiedSince and inclusion flags. |
| List Deals | `listDeals` | List product deals. GET /reference/deals. Optional query params: ID (Guid for detailed single deal), Page, Limit (default 25), Search. |
| List Disassemblies | `listDisassemblies` | Get a paginated list of Disassembly tasks. Optional filters: Page, Limit, Status, Search. |
| List Finished Goods | `listFinishedGoods` | Get a paginated list of Finished Goods tasks. Optional filters: Page, Limit, Status, Search, SaleID. |
| List Fixed Asset Types | `listFixedAssetTypes` | Retrieve fixed asset types defined in Cin7 Core. |
| List Inventory Write-Offs | `listInventoryWriteOffs` | Get a paginated list of Inventory Write-Off tasks. Optional filters: Page, Limit, Status, Search. |
| List Journals | `listJournals` | Get a paginated list of Journals, or a single Journal by TaskID. Optional filters: Page, Limit, TaskID, Status, Search. |
| List Leads | `listLeads` | List CRM leads with pagination and filters. GET /crm/lead. |
| List Locations | `listLocations` | Retrieve inventory locations (warehouses) defined in Cin7 Core. |
| List Me Addresses | `listMeAddresses` | List the organisation's own (Me) addresses. Optional filters: Page, Limit, ID, Type, DefaultForType, Country, StateProvince, CitySuburb. |
| List Me Contacts | `listMeContacts` | List the organisation's own (Me) contacts. Optional filters: Page, Limit, ID, Name, Type, DefaultForType, Phone, Fax, Email. |
| List Money Tasks | `listMoneyTasks` | Get a paginated list of Money Tasks. Optional filters: Page, Limit, Status, Search, TaskType. |
| List Opportunities | `listOpportunities` | List CRM opportunities with pagination and filters. GET /crm/opportunity. |
| List Payment Terms | `listPaymentTerms` | Retrieve payment terms defined in Cin7 Core. |
| List Price Tiers | `listPriceTiers` | Retrieve the sell price tiers configured in Cin7 Core. |
| List Product Availability | `listProductAvailability` | Retrieve current stock availability per product/location/batch in Cin7 Core (on hand, allocated, available, on order). |
| List Product Categories | `listProductCategories` | Retrieve product categories defined in Cin7 Core. |
| List Product Discounts | `listProductDiscounts` | List product discount rules. GET /reference/discount. Optional query params: ID (Guid), Page, Limit (default 25), Search. |
| List Product Families | `listProductFamilies` | Retrieve product families (variant parents) defined in Cin7 Core. |
| List Product Suppliers | `listProductSuppliers` | Return the Product Suppliers (supplier sourcing settings, options and supply intervals) for a particular Product. Pass ProductID as a required query parameter. |
| List Production Orders | `listProductionOrders` | Returns Production Orders and Production Runs according to provided filters. |
| List Production Resources | `listProductionResources` | Returns all production resources with pagination and optional name/active filters. |
| List Products | `listProducts` | Retrieve products from Cin7 Core. Supports filtering by ID, Name, SKU, ModifiedSince and several inclusion flags (BOM, suppliers, movements, attachments, reorder levels, custom prices). |
| List Purchase Credit Notes | `listPurchaseCreditNotes` | Retrieve the list of purchase credit notes from Cin7 Core. |
| List Purchases | `listPurchases` | Retrieve the list of purchases from Cin7 Core with combined status fields. Supports extensive filtering and paging. |
| List Revenue Account | `listRevenueAccount` | List revenue accounts from the Cin7 Core chart of accounts. Returns general ledger accounts with Class=REVENUE (Type=INCOME) - the income accounts used to record sales revenue. Optionally narrow by Code, Name or Status. |
| List Sale Account | `listSaleAccount` | List sale accounts from the Cin7 Core chart of accounts. Returns revenue (Class=REVENUE) accounts whose name begins with 'Sales' - the sales GL accounts such as 'Sales Account' and 'Sales of Product Income'. Sales-tax liability accounts are excluded. Optionally narrow by Code or Status. |
| List Sale Credit Notes | `listSaleCreditNotes` | Retrieve the list of sale credit notes from Cin7 Core. |
| List Sales | `listSales` | Retrieve the list of sales (orders) from Cin7 Core with combined status fields. Supports extensive filtering and paging. |
| List Ship Zones | `listShipZones` | List shipping zones. GET /reference/shipZones. Optional query params: ID (Guid for a single zone), Page, Limit (default 25), Search. |
| List Stock Adjustments | `listStockAdjustments` | Retrieve the list of stock adjustments from Cin7 Core. |
| List Stock Takes | `listStockTakes` | Retrieve the list of stocktakes (stock counts) from Cin7 Core. |
| List Stock Transfers | `listStockTransfers` | Retrieve the list of stock transfers from Cin7 Core. |
| List Supplier Deposits | `listSupplierDeposits` | Retrieve supplier deposits/prepayments recorded in Cin7 Core. |
| List Suppliers | `listSuppliers` | Retrieve suppliers from Cin7 Core. Supports filtering by ID, Name, ModifiedSince and deprecated inclusion. |
| List Suspend Reasons | `listSuspendReasons` | Returns all suspend reasons, optionally filtered by work center. |
| List Task Categories | `listTaskCategories` | List CRM task categories. GET /crm/taskcategory. |
| List Taxes | `listTaxes` | Retrieve tax rules/rates defined in Cin7 Core. |
| List Templates | `listTemplates` | Retrieve document/email templates defined in Cin7 Core. |
| List Transactions | `listTransactions` | Retrieve general-ledger transactions from Cin7 Core within a date range and optional account filter. |
| List Units of Measure | `listUnits` | Retrieve units of measure defined in Cin7 Core. |
| List Webhooks | `listWebhooks` | Retrieve all webhook subscriptions configured for this Cin7 Core API application. |
| List Work Centers | `listWorkCenters` | Returns all work centers with pagination and optional name filter. |
| List Workflows | `listWorkflows` | List CRM workflows. GET /crm/workflow. |
| Release Production Order | `releaseProductionOrder` | Releases a Production Order. May create Transfer/Purchase Orders (returned in Warning). Body (JSON string) requires productionOrderID. |
| Resume Run Operation | `resumeRunOperation` | Resumes a suspended Run operation. Body (JSON string) requires ProductionOrderID, ProductionRunID, RunOperationID. |
| Start Run Operation | `startRunOperation` | Starts a Run operation. Body (JSON string) requires ProductionOrderID, ProductionRunID, RunOperationID; optional WithAutoConsume, ManualStartDate, InputProducts[] (ProductID/ProductCode, BatchSN, Quantity). |
| Start Workflow | `startWorkflow` | Start a CRM workflow on an entity. POST /crm/workflowstart with query params. Either Workflow ID or Name must be provided. StartDate, EnityType and EntityID are required. |
| Subscribe Webhook (register) | `subscribeWebhook` | Register a webhook subscription with explicit fields (used by the connector's webhook subscription engine). POST /webhooks. All four fields are required. |
| Suspend Run Operation | `suspendRunOperation` | Suspends a Run operation. Body (JSON string) requires ProductionOrderID, ProductionRunID, RunOperationID, SuspendReasonID. |
| Undo Production Order | `undoProductionOrder` | Undoes a Production Order. Body (JSON string) requires productionOrderID and optionally ApplyToTasks (bool). |
| Undo Production Run | `undoProductionRun` | Undoes a Run. Body (JSON string) requires ProductionOrderID, ProductionRunID, and optionally ApplyToRelatedTasks (bool). |
| Update Account | `updateAccount` | Update a chart-of-accounts account. PUT /ref/account. Pass full JSON object as a string in body. Required: Code, Name, Type, Status. Optional Description, Class. Not allowed while Xero/Quickbooks integration enabled. |
| Update Advanced Purchase | `updateAdvancedPurchase` | Update an Advanced Purchase. PUT /advanced-purchase. Body (JSON string) must include ID plus the same fields as create. |
| Update Advanced Purchase Payment | `updateAdvancedPurchasePayment` | Update an Advanced Purchase Payment. PUT /advanced-purchase/payment. Body (JSON string): TaskID, ID (required), Type, Amount, DatePaid, Account, CurrencyRate, Reference. Prepayments cannot be modified. |
| Update Advanced Purchase Stock Received | `updateAdvancedPurchaseStock` | Update an Advanced Purchase Stock Received task. PUT /advanced-purchase/stock. Body (JSON string): PurchaseID, TaskID (required), Status, Lines. |
| Update Attribute Set | `updateAttributeSet` | Update an attribute set. PUT /ref/attributeset. Pass full JSON object as a string in body. Required: ID (Guid), Name. Plus AttributeNName/AttributeNType/AttributeNValues for N=1..10. |
| Update Bank Transfer | `updateBankTransfer` | Update an existing Bank Transfer. Pass full JSON object as string in 'body'. Requires TaskID. Same fields as create plus TaskID(required). |
| Update Brand | `updateBrand` | Update a brand. PUT /ref/brand. Pass full JSON object as a string in body. Required: ID (Guid), Name (string). |
| Update Carrier | `updateCarrier` | Update a carrier. PUT /ref/carrier. Pass full JSON object as a string in body. Required: CarrierID (Guid), Description (string). |
| Update CRM Task | `updateCrmTask` | Update an existing CRM task. PUT /crm/task. Body (JSON string) must include ID plus the task fields (same as Create CRM Task). |
| Update Custom Price | `updateCustomPrice` | Update customer-specific product prices. PUT /customPrices (NOTE: live path is /customPrices, not /custom-prices). Pass full JSON object as a string in body. Shape: {CustomPrices:[{CustomerID (Guid), ProductSKU, Price}]}. |
| Update Customer | `updateCustomer` | Update a Customer in Cin7 Core. Pass the full JSON as a string in 'body'. ID is REQUIRED. Same fields as Create Customer. |
| Update Customer Full | `updateCustomerFull` | Update a Cin7 Core customer with the FULL nested payload, including Contacts[] and Addresses[]. Pass the complete customer object (must include ID) as 'body'. Passthrough action so nested contacts/addresses persist on update. |
| Update Deal | `updateDeal` | Update a product deal. PUT /reference/deals. Pass full JSON object as a string in body. Required: ID (Guid), Name, CustomersGroup. Optional DealDiscounts array (include IDs to update existing lines). |
| Update Factory Calendar | `updateFactoryCalendar` | Updates a Factory Calendar. FactoryCalendarDays only overwritten when collection is not empty; FactoryCalendarSpecialDays overwritten even when empty. Body is the full Factory Calendar JSON as a string. |
| Update Family Production BOM | `updateFamilyProductionBOM` | Updates a Production BOM for a specified product family. Body (JSON string) requires BOMID, ProductFamilyID and the fields to update. |
| Update Finished Good | `updateFinishedGood` | Update an existing Finished Goods task. Pass full JSON object as string in 'body'. Requires ID. Fields can only be changed in certain statuses (see docs). Fields: ID(req), ProductID/ProductCode, LocationID/Location, BinID, Bin, WIPAccount, WIPDate, Account, Quantity, CompletionDate, BatchSN, ExpiryDate, Notes, CustomField1-10. |
| Update Fixed Asset Type | `updateFixedAssetType` | Update a fixed asset type. PUT /ref/fixedassettype. Pass full JSON object as a string in body. Required: FixedAssetTypeID (Guid), Name, DepreciationMethod, AveragingMethod, AssetAccountCode, AccumulatedDepreciationAccountCode, DepreciationExpenseAccountCode. Optional Rate, EffectiveLife. |
| Update Inventory Write-Off | `updateInventoryWriteOff` | Update an existing Inventory Write-Off. Pass full JSON object as string in 'body'. Requires TaskID. Same fields as create plus TaskID(required). |
| Update Journal | `updateJournal` | Update an existing Journal. Pass full JSON object as string in 'body'. Requires TaskID. Same fields as create plus TaskID(required). |
| Update Lead | `updateLead` | Update an existing CRM lead. PUT /crm/lead. Body (JSON string) must include ID plus the same fields as Create Lead (Name, Currency, LeadStatus, PaymentTerm, PriceTier, SalesRepresentative, TaxRule, CloseChance, CloseDate, Amount, Comments, Addresses, Contacts). |
| Update Location | `updateLocation` | Update a location. PUT /ref/location. Pass full JSON object as a string in body. Required: ID (Guid), Name. Optional address fields, IsShopfloor, IsCoMan. |
| Update Markup Prices | `updateMarkupPrices` | Create/update/delete markup price tiers for a product. PUT /product/markupprices. Pass full JSON object as a string in body. Shape: {ProductID, MarkupPrices:[{TierNumber, MarkupType ('A' to set, 'D' to delete), UsePriceType, MarkupValue}]}. |
| Update Me Address | `updateMeAddress` | Update a Me address. Pass full JSON object as string in 'body'. Requires AddressID. Fields: AddressID(req), Line1, Line2, CitySuburb, StateProvince, ZipPostCode, Country, Type, DefaultForType. |
| Update Me Contact | `updateMeContact` | Update a Me contact. Pass full JSON object as string in 'body'. Requires ContactID. Fields: ContactID(req), Name, Phone, Fax, Email, Website, Comment, Type, DefaultForType. |
| Update Money Operation | `updateMoneyOperation` | Update an existing Money Task. Pass full JSON object as string in 'body'. Requires TaskID. Same fields as create plus TaskID(required). |
| Update Opportunity | `updateOpportunity` | Update an existing CRM opportunity. PUT /crm/opportunity. Body (JSON string) must include ID plus the opportunity fields (same as Create Opportunity, including required TermDueNextMonth and a SalesRepresentative that exists in Company Contacts). |
| Update Payment Term | `updatePaymentTerm` | Update a payment term. PUT /ref/paymentterm. Pass full JSON object as a string in body. Required: ID (Guid), Name, Duration, Method. Optional IsActive, IsDefault. |
| Update Product | `updateProduct` | Update an existing Product in Cin7 Core. Pass the full product JSON as a string in 'body'. ID is REQUIRED. Type is read-only on update. Other fields same as Create Product. |
| Update Product Category | `updateProductCategory` | Update a product category. PUT /ref/category. Pass full JSON object as a string in body. Required: ID (Guid), Name. |
| Update Product Discount | `updateProductDiscount` | Update a product discount rule. PUT /reference/discount. Pass full JSON object as a string in body. Required: ID (Guid), Name, DiscountLines (include line IDs to update existing). |
| Update Product Family | `updateProductFamily` | Update a Product Family in Cin7 Core. Pass the full JSON as a string in 'body'. ID is REQUIRED. Products in the body will be added or updated (deletes are not allowed via PUT). |
| Update Product Supplier | `updateProductSupplier` | Update existing Product Supplier sourcing settings. Pass the full JSON as a string in 'body'. Each ProductSuppliers item should include ProductSupplierID (and option/interval IDs) for the records being updated. Returns {Success:true}. |
| Update Product With Description | `updateProductWithDescription` | Same as Update Product, plus Description. The shared updateProduct action omits Description from its body template, so description edits never reach Cin7 on update (create carries it). Description is sent on every call, so an empty value clears the existing description in Cin7. |
| Update Production BOM | `updateProductionBOM` | Updates a Production BOM for a specified product. Body (JSON string) requires BOMID, ProductID, Version and the fields to update. |
| Update Production Order | `updateProductionOrder` | Updates a Production Order (only some fields, and only while in Draft or Planned status). Body (JSON string) requires ProductionOrderID. Optional query params AllowRecalculateDates and AllowRecalculateCyclesAndQuantities. |
| Update Production Order Attachment | `updateProductionOrderAttachment` | Updates the IsProcessed field of a Production Order attachment. Body (JSON string) requires AttachmentID and IsProcessed. |
| Update Production Resource | `updateProductionResource` | Updates a production resource. NOTE: the PUT body must be a SINGLE resource object at the ROOT (NOT wrapped in a Resources array, unlike create). Required: ResourceID (or Code) plus fields to update: Name, ResourceType, CycleDuration, IsActive and other flags, Tags. Nested collections (ResourceCapacities/Costs/Remarks/Attachments) support creation/deletion only. |
| Update Production Run | `updateProductionRun` | Updates a Run. Query params ProductionOrderID (required) and IncreaseOrderQuantity (required bool). Body (JSON string) requires RunID and the fields to update (e.g. Quantity, Operations). |
| Update Production Run Manual Journals | `updateProductionRunManualJournals` | Creates or updates Manual Journals of a Run. Query param ProductionOrderID required. Body (JSON string) requires RunID and ManualJournals[] (each: Reference, Amount, Date, Debit, Credit account codes, optional OperationID, JournalID for update). |
| Update Purchase | `updatePurchase` | Update a Simple Purchase. PUT /purchase. Body (JSON string) must include ID and the same fields as create. |
| Update Purchase Payment | `updatePurchasePayment` | Update a Simple Purchase Payment. PUT /purchase/payment. Body (JSON string): TaskID, ID (required), Type, Amount, DatePaid, Account, CurrencyRate, Reference. Prepayments cannot be modified. |
| Update Sale | `updateSale` | Update an existing sale. Pass the full JSON object as a STRING in 'body'. ID (GUID) is required. Same field set as createSale. |
| Update Sale Fulfilment Pack | `updateSaleFulfilmentPack` | Replace the pack for a fulfilment task (requires non-authorised packing). Pass JSON as a STRING in 'body'. Required: TaskID, Status, Lines. |
| Update Sale Fulfilment Pick | `updateSaleFulfilmentPick` | Replace the pick for a fulfilment task. Pass JSON as a STRING in 'body'. Required: TaskID, Status, Lines. Fails if Pick status not DRAFT/NOT AVAILABLE or order not AUTHORISED. |
| Update Sale Fulfilment Ship | `updateSaleFulfilmentShip` | Replace/update the shipment for a fulfilment task. Pass each field as its own input (the body is built from them). Required: TaskID, Status, Lines. Add AddTrackingNumbers=true to update tracking/carrier on an authorised shipment. |
| Update Sale Invoice | `updateSaleInvoice` | Update an existing sale invoice. Pass JSON as a STRING in 'body'. Required: SaleID, TaskID. Other fields optional; an empty Lines/AdditionalCharges collection deletes existing records. |
| Update Sale Payment | `updateSalePayment` | Update an existing sale payment by ID. Pass JSON as a STRING in 'body'. Required: ID. Prepayment type cannot be modified. |
| Update Ship Zone | `updateShipZone` | Update a shipping zone. PUT /reference/shipZones. Pass full JSON object as a string in body. Required: ZoneID (Guid), Name. Optional AppliesTo and Conditions arrays (include ZoneConditionID/ID to update existing). |
| Update Ship Zones Enabled | `updateShipZonesEnabled` | Enable or disable shipping zones. PUT /reference/shipZonesEnabled. Pass full JSON object as a string in body. Shape: {IsEnabled: bool}. |
| Update Stock Adjustment | `updateStockAdjustment` | Update an existing Stock Adjustment. Pass full JSON object as string in 'body'. Requires TaskID. Same fields as create plus TaskID(required). |
| Update Stock Take | `updateStockTake` | Update an existing Stock Take. Pass full JSON object as string in 'body'. Requires TaskID and Status. Available statuses: DRAFT, IN PROGRESS, COMPLETED, VOIDED. |
| Update Stock Transfer | `updateStockTransfer` | Update an existing Stock Transfer. PUT /stockTransfer. Pass each field as its own input; only the fields given are sent. Required: TaskID, Status (DRAFT\|IN TRANSIT\|COMPLETED). Optional: CompletionDate, From/FromLocation, To/ToLocation, CostDistributionType, InTransitAccount and DepartureDate (needed for IN TRANSIT), RequiredByDate, Reference, SkipOrder, Comment, Lines. |
| Update Supplier | `updateSupplier` | Update a Supplier in Cin7 Core. Pass the full JSON as a string in 'body'. ID is REQUIRED. Same fields as Create Supplier, plus Addresses[] and Contacts[]. |
| Update Suspend Reason | `updateSuspendReason` | Creates or updates a Suspend Reason. Body (JSON string): omit SuspendReasonID to add a new reason (Reason required), or include SuspendReasonID to modify. Workcenters is a guid array (create/delete only, no modify). |
| Update Task Category | `updateTaskCategory` | Update a CRM task category. PUT /crm/taskcategory. Body (JSON string) must include ID plus Name, Color, BackgroundColor. |
| Update Tax | `updateTax` | Update a tax rule. PUT /ref/tax. Pass full JSON object as a string in body. Required: ID (Guid), Name, Account, IsActive, TaxInclusive, TaxPercent, IsTaxForSale, IsTaxForPurchase, Components (Compound is a BOOLEAN). NOTE: updating tax is blocked while the org has Xero/QuickBooks integration enabled. |
| Update Unit Of Measure | `updateUnit` | Update a unit of measure. PUT /ref/unit. Pass full JSON object as a string in body. Required: ID (Guid), Name. |
| Update Webhook | `updateWebhook` | Update a webhook subscription. PUT /webhooks. Body (JSON string) must include ID plus Type, IsActive, ExternalURL, ExternalAuthorizationType and any auth fields (same as Create Webhook). |
| Update Work Center | `updateWorkCenter` | Updates a work center. NOTE: the PUT body must be a SINGLE work center object at the ROOT (NOT wrapped in a Workcenters array, unlike create). Required: WorkCenterID plus the fields to update (Code, Name, IsActive, IsCoMan, IsCoManPurchase, WorkCenterLocations[], WorkCenterSuppliers[]). Work center locations are created if missing, updated if present. |
| Update Workflow | `updateWorkflow` | Update a CRM workflow. PUT /crm/workflow. Body (JSON string) must include ID plus the workflow fields (same as Create Workflow). |
| Upload Product Attachment | `uploadProductAttachment` | Add an attachment to a Product. Pass the JSON body as a string in 'body'. Required: ProductID, FileName, and either Content (file content as base64 string) or FileDownloadUrl. Optional: IsDefault (bool, for images). |
| Upload Product Family Attachment | `uploadProductFamilyAttachment` | Add an attachment to a Product Family. Pass the JSON body as a string in 'body'. Required: FamilyID, FileName, and either Content (base64 string) or FileDownloadUrl. Optional: IsDefault (bool, for images). |
| Upload Production Order Attachment | `uploadProductionOrderAttachment` | Adds an attachment to a Production Order. Query param ProductionOrderID required. Body (JSON string) requires FileName, ContentType, Content (Base64), and optionally Date, IsProcessed. |
| Upload Purchase Attachment | `uploadPurchaseAttachment` | Upload a Simple Purchase Attachment. POST /purchase/attachment. Body (JSON string): PurchaseID (required), FileName (required), FileDownloadUrl (optional), Content (base64 string, required if FileDownloadUrl empty). |
| Upload Sale Attachment | `uploadSaleAttachment` | Upload an attachment to a sale. Pass JSON as a STRING in 'body'. Required: SaleID, FileName, and either Content (base64) or FileDownloadUrl. |
| Void Advanced Purchase | `voidAdvancedPurchase` | Void or undo an Advanced Purchase. DELETE /advanced-purchase?ID=&Void=. Required: ID. Void defaults to true (voids the record); pass Void=false to undo it back to DRAFT. |
| Void Bank Transfer | `voidBankTransfer` | Void or Undo a Bank Transfer by ID. Set Void=true to void, false to undo. |
| Void Disassembly | `voidDisassembly` | Void or Undo a Disassembly by ID. Set Void=true to void, false to undo. |
| Void Finished Good | `voidFinishedGood` | Void or Undo a Finished Goods task by ID. Set Void=true to void, false to undo. |
| Void Inventory Write-Off | `voidInventoryWriteOff` | Void or Undo an Inventory Write-Off by ID. Set Void=true to void, false to undo. |
| Void Journal | `voidJournal` | Void or Undo a Journal by ID. Set Void=true to void, false to undo. |
| Void Money Operation | `voidMoneyOperation` | Void or Undo a Money Task by ID. Set Void=true to void, false to undo. |
| Void Production Order | `voidProductionOrder` | Voids a Production Order. Body (JSON string) requires productionOrderID and optionally ApplyToTasks (bool). |
| Void Production Run | `voidProductionRun` | Voids a Run. Body (JSON string) requires ProductionOrderID, ProductionRunID, and optionally ApplyToRelatedTasks (bool). |
| Void Purchase | `voidPurchase` | Void or undo a Simple Purchase. DELETE /purchase?ID=&Void=. Required: ID. Void defaults to true (voids the record); pass Void=false to undo it back to DRAFT. |
| Void Sale | `voidSale` | Void or undo a sale by ID. ID (GUID) required. Void=true voids the sale, false undoes the void. |
| Void Sale Query | `voidSaleQuery` | Void a Cin7 sale by sending Void as a QUERY parameter (the connector's default voidSale puts Void in the body, which Cin7 ignores → only un-authorises). DELETE /sale?ID=..&Void=true actually transitions the sale to VOIDED. Input: ID (sale GUID), Void ("true" to void, "false" to undo). |
| Void Stock Adjustment | `voidStockAdjustment` | Void or Undo a Stock Adjustment by ID. Set Void=true to void, false to undo. |
| Void Stock Take | `voidStockTake` | Void or Undo a Stock Take by ID. Set Void=true to void, false to undo. |
| Void Stock Transfer | `voidStockTransfer` | Void or undo a Stock Transfer. DELETE /stockTransfer?ID=&Void=. Required: ID. Void defaults to true (voids the record); pass Void=false to undo it back to DRAFT. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Available Stock Level Changed | `Stock/AvailableStockLevelChanged` | Fires when a product's available stock level changes. |
| Customer Updated | `Customer/Updated` | Fires when a customer record is created or updated. |
| Lead Converted | `Lead/Converted` | Fires when a CRM lead is converted. |
| Lead Updated | `Lead/Updated` | Fires when a CRM lead is created or updated. |
| Opportunity Attachment Added | `Opportunity/AttachmentAdded` | Fires when an attachment is added to a CRM opportunity. |
| Opportunity Authorized | `Opportunity/Authorized` | Fires when a CRM opportunity is authorized. |
| Opportunity Converted | `Opportunity/Converted` | Fires when a CRM opportunity is converted. |
| Opportunity Voided | `Opportunity/Voided` | Fires when a CRM opportunity is voided. |
| Product Updated | `Product/Updated` | Fires when a product is created or updated. |
| Purchase Credit Note Authorised | `Purchase/CreditNoteAuthorised` | Fires when a purchase credit note is authorised. |
| Purchase Invoice Authorised | `Purchase/InvoiceAuthorised` | Fires when a purchase invoice is authorised. |
| Purchase Order Authorised | `Purchase/OrderAuthorised` | Fires when a purchase order is authorised. |
| Purchase Stock Received Authorised | `Purchase/StockReceivedAuthorised` | Fires when purchase stock receipt is authorised. |
| Purchase Updated | `Purchase/Updated` | Fires when a purchase is updated. |
| Sale Additional Attributes Changed | `Sale/AdditionalAttributesChanged` | Fires when a sale's additional attributes change. |
| Sale Attachment Added | `Sale/AttachmentAdded` | Fires when an attachment is added to a sale. |
| Sale Backordered | `Sale/Backordered` | Fires when a sale is placed on backorder. |
| Sale Created | `Sale/Created` | Fires when a new sale is created. |
| Sale Credit Note Authorised | `Sale/CreditNoteAuthorised` | Fires when a sale credit note is authorised. |
| Sale Full Payment Received | `Sale/FullPaymentReceived` | Fires when full payment is received against a sale. |
| Sale Invoice Authorised | `Sale/InvoiceAuthorised` | Fires when a sale invoice is authorised. |
| Sale Order Authorised | `Sale/OrderAuthorised` | Fires when a sale order is authorised. |
| Sale Pack Authorised | `Sale/PackAuthorised` | Fires when a sale pack is authorised. |
| Sale Partial Payment Received | `Sale/PartialPaymentReceived` | Fires when a partial payment is received against a sale. |
| Sale Pick Authorised | `Sale/PickAuthorised` | Fires when a sale pick is authorised. |
| Sale Quote Authorised | `Sale/QuoteAuthorised` | Fires when a sale quote is authorised. |
| Sale Shipment Authorised | `Sale/ShipmentAuthorised` | Fires when a sale shipment is authorised. |
| Sale Shipment Tracking Number Changed | `Sale/ShipmentTrackingNumberChanged` | Fires when a sale shipment tracking number changes. |
| Sale Undo | `Sale/Undo` | Fires when a sale status is undone/reverted. |
| Sale Voided | `Sale/Voided` | Fires when a sale is voided/cancelled. |
| Supplier Updated | `Supplier/Updated` | Fires when a supplier record is created or updated. |
| Task Overdue | `Task/Overdue` | Fires when a CRM task becomes overdue. |
