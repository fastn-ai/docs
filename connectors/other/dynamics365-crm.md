---
description: "Microsoft Dynamics 365 Customer Engagement / Sales via the Dataverse Web API (OData v4, base https://{org}.crm.dynamics.com/api/data/v9.2)."
hidden: true
---

# Dynamics 365 CRM (Dataverse)

Microsoft Dynamics 365 Customer Engagement / Sales via the Dataverse Web API (OData v4, base https://{org}.crm.dynamics.com/api/data/v9.2). Covers accounts, contacts, leads, opportunities, quotes, sales orders, invoices, products, cases (incidents), tasks/activities, plus a generic OData CRUD pattern, WhoAmI, and $metadata. Auth: Azure AD (Entra ID) OAuth 2.0 (authorization_code).

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [dynamics.com](https://dynamics.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 287 |
| **Events** | 30 |
| **Slug** | `dynamics365Crm` |

## Use it

Add Dynamics 365 CRM (Dataverse) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dynamics365Crm.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Quote | `activateQuote` | Move a draft quote to Active (PATCH statecode 1 / statuscode 2) so it can be won or converted. |
| Add Item To Campaign | `addItemCampaign` | Add a marketing list, product or sales literature to a campaign (POST /AddItemCampaign). |
| Add Marketing List Members | `addListMembers` | Add members to a static marketing list (POST /AddListMembersList). All members must be the list's member type. |
| Add Security Role To User | `addUserRole` | Grant a security role to a user (POST /systemusers(id)/systemuserroles_association/$ref). |
| Add Team Member | `addTeamMember` | Add a user to a team (POST /teams(id)/teammembership_association/$ref). |
| Add To Queue | `addToQueue` | Route a record into a queue (POST /queues(id)/Microsoft.Dynamics.CRM.AddToQueue). Returns the queueitem id. |
| Assign Record (owner) | `assignRecord` | Change the owner of any record (PATCH /{entitySet}(id) with ownerid@odata.bind). Owner is a user (/systemusers(guid)) or team (/teams(guid)). |
| Associate Records (N:N or 1:N) | `associateRecords` | Link two records through a collection-valued navigation property (POST /{entitySet}(id)/{navigationProperty}/$ref), e.g. accounts(id)/contact_customer_accounts/$ref, systemusers(id)/systemuserroles_association/$ref, teams(id)/teammembership_association/$ref, opportunities(id)/opportunitycompetitors_association/$ref, lists(id)/listcontact_association/$ref. |
| Calculate Price | `calculatePrice` | Recalculate totals of an opportunity, quote, order or invoice (POST /CalculatePrice). Returns 204. |
| Cancel Case | `cancelIncident` | Cancel a case (PATCH statecode 2 / statuscode 6 Cancelled or 2000 Merged). |
| Clear Lookup (single-valued) | `clearLookup` | Clear a single-valued lookup on a record (DELETE /{entitySet}(id)/{navigationProperty}/$ref), e.g. accounts(id)/primarycontactid/$ref. |
| Close (resolve) Case | `closeIncident` | Resolve a case (POST /CloseIncident). Status 5 = Problem Solved, 1000 = Information Provided. timespent is billable minutes. |
| Close Quote (lost/canceled/revised) | `closeQuote` | Close a quote without winning it (POST /CloseQuote). Status 5 Lost, 6 Canceled, 7 Revised. Returns 204. |
| Convert Quote To Sales Order | `convertQuoteToSalesOrder` | Create an order from an active quote (POST /ConvertQuoteToSalesOrder). Returns the sales order. |
| Convert Sales Order To Invoice | `convertSalesOrderToInvoice` | Create an invoice from an order (POST /ConvertSalesOrderToInvoice). Returns the invoice. |
| Copy Campaign | `copyCampaign` | Copy a campaign (POST /campaigns(id)/Microsoft.Dynamics.CRM.CopyCampaign). |
| Create Account | `createAccount` | Create a account (POST /accounts). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Appointment | `createAppointment` | Create a appointment (POST /appointments). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Campaign | `createCampaign` | Create a campaign (POST /campaigns). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create CampaignActivity | `createCampaignActivity` | Create a campaignactivity (POST /campaignactivities). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Case (Incident) | `createIncident` | Create a case (POST /incidents). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Competitor | `createCompetitor` | Create a competitor (POST /competitors). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Connection | `createConnection` | Create a connection (POST /connections). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Contact | `createContact` | Create a contact (POST /contacts). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Contract | `createContract` | DEPRECATED by Microsoft (Customer Service, April 2022) - use entitlements instead. Create a contract (POST /contracts). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Discount | `createDiscount` | Create a discount (POST /discounts). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create DiscountType | `createDiscountType` | Create a discounttype (POST /discounttypes). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Email | `createEmail` | Create a email (POST /emails). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Entitlement | `createEntitlement` | Create a entitlement (POST /entitlements). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Goal | `createGoal` | Create a goal (POST /goals). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Invoice | `createInvoice` | Create a invoice (POST /invoices). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Invoice Line | `createInvoiceDetail` | Create a invoicedetail (POST /invoicedetails). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Knowledge Article Version | `createKnowledgeArticleVersion` | Create a new major or minor version (POST /CreateKnowledgeArticleVersion). Returns the new article. |
| Create KnowledgeArticle | `createKnowledgeArticle` | Create a knowledgearticle (POST /knowledgearticles). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Lead | `createLead` | Create a lead (POST /leads). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Letter | `createLetter` | Create a letter (POST /letters). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create List | `createList` | Create a marketing list (POST /lists). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Note | `createAnnotation` | Create a note (POST /annotations). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Opportunity | `createOpportunity` | Create a opportunity (POST /opportunities). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Opportunity Product | `createOpportunityProduct` | Create a opportunityproduct (POST /opportunityproducts). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Order Line | `createSalesOrderDetail` | Create a salesorderdetail (POST /salesorderdetails). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Phone Call | `createPhoneCall` | Create a phonecall (POST /phonecalls). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Price List | `createPriceLevel` | Create a pricelevel (POST /pricelevels). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Product | `createProduct` | Create a product (POST /products). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create ProductPriceLevel | `createProductPriceLevel` | Create a productpricelevel (POST /productpricelevels). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Queue | `createQueue` | Create a queue (POST /queues). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Quote | `createQuote` | Create a quote (POST /quotes). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Quote Line | `createQuoteDetail` | Create a quotedetail (POST /quotedetails). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Sales Order | `createSalesOrder` | Create a salesorder (POST /salesorders). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create SDK Message Processing Step | `createSdkMessageProcessingStep` | Create a sdkmessageprocessingstep (POST /sdkmessageprocessingsteps). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create SdkMessageProcessingStepImage | `createSdkMessageProcessingStepImage` | Create a sdkmessageprocessingstepimage (POST /sdkmessageprocessingstepimages). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Service Endpoint | `createServiceEndpoint` | Create a serviceendpoint (POST /serviceendpoints). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Subject | `createSubject` | Create a subject (POST /subjects). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Task | `createTask` | Create a task (POST /tasks). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Territory | `createTerritory` | Create a territory (POST /territories). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create Uom | `createUom` | Create a unit (POST /uoms). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Create UomSchedule | `createUomSchedule` | Create a unit group (POST /uomschedules). Send only the fields you need; lookups use *@odata.bind with /&lt;entityset&gt;(&lt;guid&gt;). Returns the created record (Prefer: return=representation). |
| Delete Account | `deleteAccount` | Delete a account (DELETE /accounts(id)). Returns 204. |
| Delete Appointment | `deleteAppointment` | Delete a appointment (DELETE /appointments(id)). Returns 204. |
| Delete Campaign | `deleteCampaign` | Delete a campaign (DELETE /campaigns(id)). Returns 204. |
| Delete CampaignActivity | `deleteCampaignActivity` | Delete a campaignactivity (DELETE /campaignactivities(id)). Returns 204. |
| Delete Case (Incident) | `deleteIncident` | Delete a case (DELETE /incidents(id)). Returns 204. |
| Delete Competitor | `deleteCompetitor` | Delete a competitor (DELETE /competitors(id)). Returns 204. |
| Delete Connection | `deleteConnection` | Delete a connection (DELETE /connections(id)). Returns 204. |
| Delete Contact | `deleteContact` | Delete a contact (DELETE /contacts(id)). Returns 204. |
| Delete Contract | `deleteContract` | DEPRECATED by Microsoft (Customer Service, April 2022) - use entitlements instead. Delete a contract (DELETE /contracts(id)). Returns 204. |
| Delete Discount | `deleteDiscount` | Delete a discount (DELETE /discounts(id)). Returns 204. |
| Delete DiscountType | `deleteDiscountType` | Delete a discounttype (DELETE /discounttypes(id)). Returns 204. |
| Delete Email | `deleteEmail` | Delete a email (DELETE /emails(id)). Returns 204. |
| Delete Entitlement | `deleteEntitlement` | Delete a entitlement (DELETE /entitlements(id)). Returns 204. |
| Delete Goal | `deleteGoal` | Delete a goal (DELETE /goals(id)). Returns 204. |
| Delete Invoice | `deleteInvoice` | Delete a invoice (DELETE /invoices(id)). Returns 204. |
| Delete Invoice Line | `deleteInvoiceDetail` | Delete a invoicedetail (DELETE /invoicedetails(id)). Returns 204. |
| Delete KnowledgeArticle | `deleteKnowledgeArticle` | Delete a knowledgearticle (DELETE /knowledgearticles(id)). Returns 204. |
| Delete Lead | `deleteLead` | Delete a lead (DELETE /leads(id)). Returns 204. |
| Delete Letter | `deleteLetter` | Delete a letter (DELETE /letters(id)). Returns 204. |
| Delete List | `deleteList` | Delete a marketing list (DELETE /lists(id)). Returns 204. |
| Delete Note | `deleteAnnotation` | Delete a note (DELETE /annotations(id)). Returns 204. |
| Delete Opportunity | `deleteOpportunity` | Delete a opportunity (DELETE /opportunities(id)). Returns 204. |
| Delete Opportunity Product | `deleteOpportunityProduct` | Delete a opportunityproduct (DELETE /opportunityproducts(id)). Returns 204. |
| Delete Order Line | `deleteSalesOrderDetail` | Delete a salesorderdetail (DELETE /salesorderdetails(id)). Returns 204. |
| Delete Phone Call | `deletePhoneCall` | Delete a phonecall (DELETE /phonecalls(id)). Returns 204. |
| Delete Price List | `deletePriceLevel` | Delete a pricelevel (DELETE /pricelevels(id)). Returns 204. |
| Delete Product | `deleteProduct` | Delete a product (DELETE /products(id)). Returns 204. |
| Delete ProductPriceLevel | `deleteProductPriceLevel` | Delete a productpricelevel (DELETE /productpricelevels(id)). Returns 204. |
| Delete Queue | `deleteQueue` | Delete a queue (DELETE /queues(id)). Returns 204. |
| Delete QueueItem | `deleteQueueItem` | Delete a queueitem (DELETE /queueitems(id)). Returns 204. |
| Delete Quote | `deleteQuote` | Delete a quote (DELETE /quotes(id)). Returns 204. |
| Delete Quote Line | `deleteQuoteDetail` | Delete a quotedetail (DELETE /quotedetails(id)). Returns 204. |
| Delete Sales Order | `deleteSalesOrder` | Delete a salesorder (DELETE /salesorders(id)). Returns 204. |
| Delete SDK Message Processing Step | `deleteSdkMessageProcessingStep` | Delete a sdkmessageprocessingstep (DELETE /sdkmessageprocessingsteps(id)). Returns 204. |
| Delete SdkMessageProcessingStepImage | `deleteSdkMessageProcessingStepImage` | Delete a sdkmessageprocessingstepimage (DELETE /sdkmessageprocessingstepimages(id)). Returns 204. |
| Delete Service Endpoint | `deleteServiceEndpoint` | Delete a serviceendpoint (DELETE /serviceendpoints(id)). Returns 204. |
| Delete Subject | `deleteSubject` | Delete a subject (DELETE /subjects(id)). Returns 204. |
| Delete Task | `deleteTask` | Delete a task (DELETE /tasks(id)). Returns 204. |
| Delete Territory | `deleteTerritory` | Delete a territory (DELETE /territories(id)). Returns 204. |
| Delete Uom | `deleteUom` | Delete a unit (DELETE /uoms(id)). Returns 204. |
| Delete UomSchedule | `deleteUomSchedule` | Delete a unit group (DELETE /uomschedules(id)). Returns 204. |
| Disassociate Records | `disassociateRecords` | Remove a link made through a collection-valued navigation property (DELETE /{entitySet}(id)/{navigationProperty}({relatedId})/$ref). |
| FetchXML Query | `fetchXmlQuery` | Run a FetchXML query (GET /{entitySet}?fetchXml=...). Supports aggregates, joins and paging cookies. Null columns are omitted from results. |
| Full-Text Search Knowledge Articles | `searchKnowledgeArticles` | Full-text search (GET /FullTextSearchKnowledgeArticle(SearchText=@t,UseInflection=@i,RemoveDuplicates=@r,StateCode=@s,QueryExpression=@q)). |
| Generate Invoice From Opportunity | `generateInvoiceFromOpportunity` | Create an invoice from an opportunity (POST /GenerateInvoiceFromOpportunity). Returns the invoice. |
| Generate Quote From Opportunity | `generateQuoteFromOpportunity` | Create a quote with the opportunity's products (POST /GenerateQuoteFromOpportunity). Returns the quote. |
| Generate Sales Order From Opportunity | `generateSalesOrderFromOpportunity` | Create an order from an opportunity (POST /GenerateSalesOrderFromOpportunity). Returns the order. |
| Generic OData Create (any entity) | `genericCreate` | Create a row in any entity set (POST /{entitySet}) from a JSON object string. Escape hatch for custom tables. |
| Generic OData Delete (any entity) | `genericDelete` | Delete a row in any entity set (DELETE /{entitySet}(id)). |
| Generic OData Get by ID (any entity) | `genericGet` | Get one row of any entity set (GET /{entitySet}(id)). |
| Generic OData List (any entity) | `genericList` | List rows of any entity set (GET /{entitySet}) with OData query options. Escape hatch for custom tables; typed list actions exist for the standard ones. |
| Generic OData Update (any entity) | `genericUpdate` | Update a row in any entity set (PATCH /{entitySet}(id), If-Match: *) from a JSON object string of the columns to change. |
| Get Account | `getAccount` | Get one account by id (GET /accounts(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Appointment | `getAppointment` | Get one appointment by id (GET /appointments(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Business Unit | `getBusinessUnit` | Retrieve a single business unit by businessunitid GUID. Read-only. |
| Get By Alternate Key | `getByAlternateKey` | Get a row by an alternate key (GET /{entitySet}({keyAttribute}='{keyValue}')). Requires an alternate key defined on the table, e.g. accounts(accountnumber='ACC-001'). |
| Get Campaign | `getCampaign` | Get one campaign by id (GET /campaigns(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get CampaignActivity | `getCampaignActivity` | Get one campaignactivity by id (GET /campaignactivities(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Case (Incident) | `getIncident` | Get one case by id (GET /incidents(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Competitor | `getCompetitor` | Get one competitor by id (GET /competitors(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Connection | `getConnection` | Get one connection by id (GET /connections(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Contact | `getContact` | Get one contact by id (GET /contacts(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Contract | `getContract` | DEPRECATED by Microsoft (Customer Service, April 2022) - use entitlements instead. Get one contract by id (GET /contracts(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Default Price Level | `getDefaultPriceLevel` | Default price list for a sales entity (GET /pricelevels/Microsoft.Dynamics.CRM.GetDefaultPriceLevel(EntityName='opportunity')). |
| Get Discount | `getDiscount` | Get one discount by id (GET /discounts(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get DiscountType | `getDiscountType` | Get one discounttype by id (GET /discounttypes(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Email | `getEmail` | Get one email by id (GET /emails(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Entitlement | `getEntitlement` | Get one entitlement by id (GET /entitlements(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Global Option Set (metadata) | `getGlobalOptionSet` | One global choice with its options (GET /GlobalOptionSetDefinitions(Name='x')). |
| Get Goal | `getGoal` | Get one goal by id (GET /goals(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Invoice | `getInvoice` | Get one invoice by id (GET /invoices(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Invoice Line | `getInvoiceDetail` | Get one invoicedetail by id (GET /invoicedetails(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Knowledge Article | `getKnowledgeArticle` | Get one knowledgearticle by id (GET /knowledgearticles(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Lead | `getLead` | Get one lead by id (GET /leads(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Letter | `getLetter` | Get one letter by id (GET /letters(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get List | `getList` | Get one marketing list by id (GET /lists(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Next Page | `getNextPage` | Fetch the next page of a list. Take @odata.nextLink from the previous response, read its $skiptoken (new URL(nextLink).searchParams.get('$skiptoken')) and pass it here together with the same $select/$filter/$orderby/$expand and prefer values as the first call. |
| Get Note | `getAnnotation` | Get one note by id (GET /annotations(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get OData Metadata ($metadata) | `getMetadata` | BLOCKED: GET /$metadata returns a multi-MB CSDL XML document that the executor cannot relay. Use listEntityDefinitions / listEntityAttributes / getPicklistOptions instead. |
| Get Opportunity | `getOpportunity` | Get one opportunity by id (GET /opportunities(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Opportunity Product | `getOpportunityProduct` | Get one opportunityproduct by id (GET /opportunityproducts(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Order Line | `getSalesOrderDetail` | Get one salesorderdetail by id (GET /salesorderdetails(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Phone Call | `getPhoneCall` | Get one phonecall by id (GET /phonecalls(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Picklist Options (metadata) | `getPicklistOptions` | Option-set values and labels for one choice column (GET /EntityDefinitions(LogicalName='x')/Attributes(LogicalName='y')/Microsoft.Dynamics.CRM.PicklistAttributeMetadata?$expand=OptionSet). For statecode/statuscode use StateAttributeMetadata/StatusAttributeMetadata via listEntityAttributes. |
| Get Price List | `getPriceLevel` | Get one pricelevel by id (GET /pricelevels(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Product | `getProduct` | Get one product by id (GET /products(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get ProductPriceLevel | `getProductPriceLevel` | Get one productpricelevel by id (GET /productpricelevels(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Queue | `getQueue` | Get one queue by id (GET /queues(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get QueueItem | `getQueueItem` | Get one queueitem by id (GET /queueitems(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Quote | `getQuote` | Get one quote by id (GET /quotes(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Quote Line | `getQuoteDetail` | Get one quotedetail by id (GET /quotedetails(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Sales Order | `getSalesOrder` | Get one salesorder by id (GET /salesorders(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get SdkMessageProcessingStep | `getSdkMessageProcessingStep` | Get one sdkmessageprocessingstep by id (GET /sdkmessageprocessingsteps(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Service Document (entity sets) | `getServiceDocument` | GET /api/data/v9.2/ - the OData service document listing every entity set (large; prefer listEntityDefinitions). |
| Get ServiceEndpoint | `getServiceEndpoint` | Get one serviceendpoint by id (GET /serviceendpoints(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Subject | `getSubject` | Get one subject by id (GET /subjects(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get System User By Email | `getSystemUserByEmail` | Find users by primary email (GET /systemusers?$filter=internalemailaddress eq '...'). Use the returned systemuserid for ownerid binds. |
| Get Task | `getTask` | Get one task by id (GET /tasks(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Team | `getTeam` | Retrieve a single team by teamid GUID. Read-only. |
| Get Territory | `getTerritory` | Get one territory by id (GET /territories(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get Uom | `getUom` | Get one unit by id (GET /uoms(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get UomSchedule | `getUomSchedule` | Get one unit group by id (GET /uomschedules(id)). Use $select to limit columns and prefer=odata.include-annotations="*" for option-set labels and lookup names. |
| Get User | `getSystemUser` | Retrieve a single system user by systemuserid GUID. Read-only. |
| Grant Access (share) | `grantAccess` | Share a record with a user or team (POST /GrantAccess). AccessMask is a comma list of ReadAccess, WriteAccess, AppendAccess, AppendToAccess, CreateAccess, DeleteAccess, ShareAccess, AssignAccess. |
| List Accounts | `listAccounts` | List accounts (GET /accounts) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Activities (timeline) | `listActivityPointers` | All activity types in one query (GET /activitypointers). Filter by regarding record: _regardingobjectid_value eq &lt;guid&gt;. activitytypecode tells the type (task, email, phonecall, appointment, letter). |
| List Appointments | `listAppointments` | List appointments (GET /appointments) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Business Units | `listBusinessUnits` | List business unit records with optional OData query options ($select/$filter/$top/$orderby/$expand). Read-only. |
| List CampaignActivities | `listCampaignActivities` | List campaignactivitys (GET /campaignactivities) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Campaigns | `listCampaigns` | List campaigns (GET /campaigns) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Cases (Incidents) | `listIncidents` | List cases (GET /incidents) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Competitors | `listCompetitors` | List competitors (GET /competitors) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Connection Roles | `listConnectionRoles` | Connection roles (GET /connectionroles) for createConnection record1roleid/record2roleid. |
| List Connections | `listConnections` | List connections (GET /connections) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Contacts | `listContacts` | List contacts (GET /contacts) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Contracts | `listContracts` | DEPRECATED by Microsoft (Customer Service, April 2022) - use entitlements instead. List contracts (GET /contracts) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Discounts | `listDiscounts` | List discounts (GET /discounts) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List DiscountTypes | `listDiscountTypes` | List discounttypes (GET /discounttypes) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Emails | `listEmails` | List emails (GET /emails) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Entitlement Templates | `listEntitlementTemplates` | Entitlement templates (GET /entitlementtemplates). |
| List Entitlements | `listEntitlements` | List entitlements (GET /entitlements) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Entity Attributes (metadata) | `listEntityAttributes` | Column metadata for one table (GET /EntityDefinitions(LogicalName='x')/Attributes). Pass $select, e.g. LogicalName,AttributeType,DisplayName,RequiredLevel,IsValidForCreate,IsValidForUpdate. |
| List Entity Definitions (metadata) | `listEntityDefinitions` | Table metadata (GET /EntityDefinitions). Always pass $select to keep the response small, e.g. LogicalName,EntitySetName,DisplayName,PrimaryIdAttribute,PrimaryNameAttribute,ChangeTrackingEnabled. |
| List Global Option Sets (metadata) | `listGlobalOptionSets` | Global choice definitions (GET /GlobalOptionSetDefinitions). Pass $select=Name,DisplayName to keep it small; expand one with getGlobalOptionSet. |
| List Goal Metrics | `listMetrics` | Goal metrics (GET /metrics) - required for createGoal. |
| List Goal Rollup Queries | `listGoalRollupQueries` | Rollup queries (GET /goalrollupqueries). |
| List Goals | `listGoals` | List goals (GET /goals) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Invoice Lines | `listInvoiceDetails` | List invoicedetails (GET /invoicedetails) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Invoices | `listInvoices` | List invoices (GET /invoices) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Knowledge Articles | `listKnowledgeArticles` | List knowledgearticles (GET /knowledgearticles) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Leads | `listLeads` | List leads (GET /leads) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Letters | `listLetters` | List letters (GET /letters) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Lists | `listLists` | List marketing lists (GET /lists) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Notes | `listAnnotations` | List notes (GET /annotations) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Opportunities | `listOpportunities` | List opportunitys (GET /opportunities) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Opportunity Close Activities | `listOpportunityCloses` | Win/lose close records (GET /opportunitycloses) with actualrevenue, competitor and description. |
| List Opportunity Products | `listOpportunityProducts` | List opportunityproducts (GET /opportunityproducts) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Order Lines | `listSalesOrderDetails` | List salesorderdetails (GET /salesorderdetails) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Organizations (org settings) | `listOrganizations` | Organization settings row (GET /organizations): base currency, time zone, fiscal settings, feature flags. Pass $select. |
| List Phone Calls | `listPhoneCalls` | List phonecalls (GET /phonecalls) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Price Lists | `listPriceLevels` | List pricelevels (GET /pricelevels) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List ProductPriceLevels | `listProductPriceLevels` | List productpricelevels (GET /productpricelevels) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Products | `listProducts` | List products (GET /products) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List QueueItems | `listQueueItems` | List queueitems (GET /queueitems) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Queues | `listQueues` | List queues (GET /queues) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Quote Close Activities | `listQuoteCloses` | Quote close records (GET /quotecloses). |
| List Quote Lines | `listQuoteDetails` | List quotedetails (GET /quotedetails) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Quotes | `listQuotes` | List quotes (GET /quotes) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Sales Orders | `listSalesOrders` | List salesorders (GET /salesorders) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Saved Queries (system views) | `listSavedQueries` | System views (GET /savedqueries). Use returntypecode to filter by table, e.g. returntypecode eq 'account'. |
| List SDK Message Filters | `listSdkMessageFilters` | List Dataverse SDK message filters. Used to find the filter ID for a specific entity+message combination when registering webhook steps. |
| List SDK Messages | `listSdkMessages` | List Dataverse SDK messages (e.g. Create, Update, Delete). Used to look up message IDs for webhook step registration. |
| List SdkMessageProcessingStepImages | `listSdkMessageProcessingStepImages` | List sdkmessageprocessingstepimages (GET /sdkmessageprocessingstepimages) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List SdkMessageProcessingSteps | `listSdkMessageProcessingSteps` | List sdkmessageprocessingsteps (GET /sdkmessageprocessingsteps) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Security Roles | `listRoles` | Security roles (GET /roles). |
| List Service Endpoints | `listServiceEndpoints` | List serviceendpoints (GET /serviceendpoints) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List SLAs | `listSlas` | Service level agreements (GET /slas). |
| List Subjects | `listSubjects` | List subjects (GET /subjects) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Tasks | `listTasks` | List tasks (GET /tasks) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Teams | `listTeams` | List team records with optional OData query options ($select/$filter/$top/$orderby/$expand). Read-only. |
| List Territories | `listTerritories` | List territorys (GET /territories) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List Transaction Currencies | `listTransactionCurrencies` | Currencies enabled in the org (GET /transactioncurrencies). |
| List Uoms | `listUoms` | List units (GET /uoms) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List UomSchedules | `listUomSchedules` | List unit groups (GET /uomschedules) with OData $select/$filter/$orderby/$top/$expand/$count. Pages of up to 5000; when @odata.nextLink is returned pass its $skiptoken to getNextPage. Set prefer=odata.maxpagesize=N for smaller pages. |
| List User Queries (personal views) | `listUserQueries` | Personal views (GET /userqueries). |
| List Users | `listSystemUsers` | List system user records with optional OData query options ($select/$filter/$top/$orderby/$expand). Read-only. |
| List Webhook Steps For Endpoint | `listSdkMessageProcessingStepsForEndpoint` | Steps registered against one service endpoint (GET /sdkmessageprocessingsteps?$filter=_eventhandler_value eq &lt;id&gt;). Audit which entities/messages a fastn webhook is subscribed to. |
| Lose Opportunity | `loseOpportunity` | Close an opportunity as Lost (POST /LoseOpportunity). Status 4 = Canceled, 5 = Out-Sold. Returns 204. |
| Merge Records | `mergeRecords` | Merge two accounts, contacts, leads or cases (POST /Merge). Subordinate is deactivated and its children re-parented to Target. UpdateContent carries columns to copy onto the target. |
| Modify Access | `modifyAccess` | Change the rights already shared with a user or team (POST /ModifyAccess). |
| Pick From Queue | `pickFromQueue` | Assign a queue item to a user and optionally remove it (POST /queueitems(id)/Microsoft.Dynamics.CRM.PickFromQueue). |
| Publish Knowledge Article | `publishKnowledgeArticle` | Publish an article (PATCH statecode 3 / statuscode 7). |
| Qualify Lead | `qualifyLead` | Qualify a lead (POST /leads(id)/Microsoft.Dynamics.CRM.QualifyLead). Creates account/contact/opportunity as requested and returns them. Status 3 = Qualified. |
| Reactivate Case | `reactivateIncident` | Reopen a resolved or cancelled case (PATCH statecode 0 / statuscode 1). |
| Release To Queue | `releaseToQueue` | Release a picked queue item back to the queue (POST /queueitems(id)/Microsoft.Dynamics.CRM.ReleaseToQueue). |
| Remove From Queue | `removeFromQueue` | Remove a queue item (POST /queueitems(id)/Microsoft.Dynamics.CRM.RemoveFromQueue). |
| Remove Marketing List Member | `removeListMember` | Remove one member from a static marketing list (POST /RemoveMemberList). |
| Remove Security Role From User | `removeUserRole` | Revoke a security role from a user (DELETE /systemusers(id)/systemuserroles_association(roleId)/$ref). |
| Remove Team Member | `removeTeamMember` | Remove a user from a team (DELETE /teams(id)/teammembership_association(userId)/$ref). |
| Retrieve Principal Access | `retrievePrincipalAccess` | Rights a user has on a record (GET /systemusers(id)/Microsoft.Dynamics.CRM.RetrievePrincipalAccess(Target=@t)). |
| Retrieve Total Record Count | `retrieveTotalRecordCount` | Approximate row counts per table (GET /RetrieveTotalRecordCount(EntityNames=@p)), refreshed every 24h. Better than $count for large tables. |
| Retrieve Version | `retrieveVersion` | Dataverse server version (GET /RetrieveVersion()). |
| Revise Quote | `reviseQuote` | Create a new revision of a closed quote (POST /ReviseQuote). Returns the new quote. |
| Revoke Access (unshare) | `revokeAccess` | Remove all shared rights of a user or team on a record (POST /RevokeAccess). |
| Send Email | `sendEmail` | Send a draft email activity (POST /emails(id)/Microsoft.Dynamics.CRM.SendEmail). Requires server-side sync or a mailbox for the sender. |
| Set Record State | `setRecordState` | Set statecode and statuscode of any record (PATCH /{entitySet}(id)). Use activate/deactivate here; for Won/Lost/Closed use the dedicated actions (winOpportunity, closeIncident, ...). |
| Track Changes (delta) | `trackChanges` | Change tracking for polling sync (GET /{entitySet} with Prefer: odata.track-changes). First call returns rows plus @odata.deltaLink; pass its $deltatoken next time to get only created/updated rows and deleted ids (entries with @odata.context ending in /$deletedEntity). Change tracking must be enabled on the table. |
| Update Account | `updateAccount` | Update a account (PATCH /accounts(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Appointment | `updateAppointment` | Update a appointment (PATCH /appointments(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Campaign | `updateCampaign` | Update a campaign (PATCH /campaigns(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update CampaignActivity | `updateCampaignActivity` | Update a campaignactivity (PATCH /campaignactivities(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Case (Incident) | `updateIncident` | Update a case (PATCH /incidents(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Competitor | `updateCompetitor` | Update a competitor (PATCH /competitors(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Connection | `updateConnection` | Update a connection (PATCH /connections(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Contact | `updateContact` | Update a contact (PATCH /contacts(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Contract | `updateContract` | DEPRECATED by Microsoft (Customer Service, April 2022) - use entitlements instead. Update a contract (PATCH /contracts(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Discount | `updateDiscount` | Update a discount (PATCH /discounts(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update DiscountType | `updateDiscountType` | Update a discounttype (PATCH /discounttypes(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Email | `updateEmail` | Update a email (PATCH /emails(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Entitlement | `updateEntitlement` | Update a entitlement (PATCH /entitlements(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Goal | `updateGoal` | Update a goal (PATCH /goals(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Invoice | `updateInvoice` | Update a invoice (PATCH /invoices(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Invoice Line | `updateInvoiceDetail` | Update a invoicedetail (PATCH /invoicedetails(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update KnowledgeArticle | `updateKnowledgeArticle` | Update a knowledgearticle (PATCH /knowledgearticles(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Lead | `updateLead` | Update a lead (PATCH /leads(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Letter | `updateLetter` | Update a letter (PATCH /letters(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update List | `updateList` | Update a marketing list (PATCH /lists(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Note | `updateAnnotation` | Update a note (PATCH /annotations(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Opportunity | `updateOpportunity` | Update a opportunity (PATCH /opportunities(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Opportunity Product | `updateOpportunityProduct` | Update a opportunityproduct (PATCH /opportunityproducts(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Order Line | `updateSalesOrderDetail` | Update a salesorderdetail (PATCH /salesorderdetails(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Phone Call | `updatePhoneCall` | Update a phonecall (PATCH /phonecalls(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Price List | `updatePriceLevel` | Update a pricelevel (PATCH /pricelevels(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Product | `updateProduct` | Update a product (PATCH /products(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update ProductPriceLevel | `updateProductPriceLevel` | Update a productpricelevel (PATCH /productpricelevels(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Queue | `updateQueue` | Update a queue (PATCH /queues(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Quote | `updateQuote` | Update a quote (PATCH /quotes(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Quote Line | `updateQuoteDetail` | Update a quotedetail (PATCH /quotedetails(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Sales Order | `updateSalesOrder` | Update a salesorder (PATCH /salesorders(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update SdkMessageProcessingStep | `updateSdkMessageProcessingStep` | Update a sdkmessageprocessingstep (PATCH /sdkmessageprocessingsteps(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update ServiceEndpoint | `updateServiceEndpoint` | Update a serviceendpoint (PATCH /serviceendpoints(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Subject | `updateSubject` | Update a subject (PATCH /subjects(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Task | `updateTask` | Update a task (PATCH /tasks(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Territory | `updateTerritory` | Update a territory (PATCH /territories(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update Uom | `updateUom` | Update a unit (PATCH /uoms(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Update UomSchedule | `updateUomSchedule` | Update a unit group (PATCH /uomschedules(id), If-Match: * so a wrong id 404s instead of creating a record). Send only the fields to change; to change state send statecode and statuscode together. Returns the updated record. |
| Upsert By Alternate Key | `upsertByAlternateKey` | Create-or-update by alternate key (PATCH /{entitySet}({keyAttribute}='{keyValue}')). 201 + record when created, 200 + record when updated. Requires an alternate key on the table. Do not include the key column in recordJson. |
| WhoAmI | `whoAmI` | Returns the system user, business unit, and organization IDs for the authenticated caller. Useful for connection validation. |
| Win Opportunity | `winOpportunity` | Close an opportunity as Won (POST /WinOpportunity). Status 3 = Won. Returns 204. |
| Win Quote | `winQuote` | Mark an active quote as Won (POST /WinQuote). Status 4 = Won. Quote must be Active (activateQuote first). Returns 204. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Account | `account` | Fires on account Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Appointment | `appointment` | Fires on appointment Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Campaign | `campaign` | Fires on campaign Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Campaign Response | `campaignresponse` | Fires on campaign response Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Case (Incident) | `incident` | Fires on case (incident) Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Competitor | `competitor` | Fires on competitor Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Connection | `connection` | Fires on connection Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Contact | `contact` | Fires on contact Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Email | `email` | Fires on email Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Entitlement | `entitlement` | Fires on entitlement Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Goal | `goal` | Fires on goal Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Invoice | `invoice` | Fires on invoice Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Invoice Line | `invoicedetail` | Fires on invoice line Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Knowledge Article | `knowledgearticle` | Fires on knowledge article Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Lead | `lead` | Fires on lead Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Marketing List | `list` | Fires on marketing list Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Note (Annotation) | `annotation` | Fires on note (annotation) Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Opportunity | `opportunity` | Fires on opportunity Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Opportunity Product | `opportunityproduct` | Fires on opportunity product Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Order Line | `salesorderdetail` | Fires on order line Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Phone Call | `phonecall` | Fires on phone call Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Price List | `pricelevel` | Fires on price list Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Product | `product` | Fires on product Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Queue Item | `queueitem` | Fires on queue item Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Quote | `quote` | Fires on quote Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Quote Line | `quotedetail` | Fires on quote line Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Sales Order | `salesorder` | Fires on sales order Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| System User | `systemuser` | Fires on system user Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Task | `task` | Fires on task Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
| Team | `team` | Fires on team Create, Update and Delete (Dataverse webhook, async post-operation). Branch on MessageName. Update carries changed columns in InputParameters.Target plus the full row in PostEntityImages.PostImage; Delete carries the deleted row in PreEntityImages.PreImage. |
