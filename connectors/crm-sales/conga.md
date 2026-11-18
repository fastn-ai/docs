---
description: "Conga Advantage Platform (formerly Apttus Intelligent Cloud) — Conga's standalone Revenue Lifecycle Management REST API, covering CRM records (Account,…"
---

# Conga Advantage Platform

Conga Advantage Platform (formerly Apttus Intelligent Cloud) — Conga's standalone Revenue Lifecycle Management REST API, covering CRM records (Account, Contact, Opportunity and any custom object), CPQ (catalog, carts, line items, pricing, checkout), Quotes, Orders, installed-base Assets, and Contract Lifecycle Management (contracts, clauses, documents, requests, templates). Hosts are regional: https://rls.congacloud.com (NA), .eu (EU), .au (AU). Auth is OAuth2 client_credentials against the matching login host. This is the current, non-Salesforce Conga surface documented at developer.conga.com; the legacy Conga CPQ/CLM for Salesforce managed packages are reached through the Salesforce connector instead.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [congacloud.com](https://congacloud.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Actions** | 133 |
| **Events** | 0 |
| **Slug** | `conga` |

## Use it

Add Conga Advantage Platform from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.conga.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Abandon Cart | `abandonCart` | Abandon a cart, discarding the in-progress configuration without deleting the record. |
| Accept Quote | `acceptQuote` | Accept a quote and create the resulting order. Set isAsync to true for large quotes; the response then carries a job id to poll with getQuoteJobStatus. |
| Activate Contract | `activateContract` | Activate a CLM contract, moving it into the in-effect part of its lifecycle. The request root is a JSON array; pass [] unless the org's activation expects document identifiers. |
| Activate Order | `activateOrder` | Activate an order so it can be fulfilled, billed and tracked for revenue. Set isAsync for large orders and poll the returned job. |
| Add Approval Comment | `addApprovalComment` | Add a comment to one or more approval requests. ApprovalRequestIds is passed as a JSON array string and is emitted verbatim into the request body. The documented 200 response body is a bare boolean, so it is exposed here as an object with a single result field. Optional documented body field not templated: AttachmentIds (string). |
| Add Cart Line Items | `addCartLineItems` | Add line items to a cart. Conga takes a JSON array at the request root, so the items are passed as a JSON array string and sent verbatim. Each item normally carries at least a product reference and a quantity. |
| Amend Contract | `amendContract` | Amend an activated contract. Returns the ID of the amendment contract created from it. |
| Apply Promotion To Cart | `applyPromotionToCart` | Apply a promotion or coupon code to a cart. Reprice afterwards to see the resulting adjustments. |
| Approve Approval Request | `approveApprovalRequest` | Approve a single approval request by its request ID. The documented 200 response body is a bare boolean, so it is exposed here as an object with a single result field. Optional documented body field not templated: ApprovalFromEmail (boolean). |
| Assign User Role | `assignUserRole` | Assign a role to a user. Both IDs are path segments and the request carries no body. Get role IDs from List Roles. |
| Cancel Order | `cancelOrder` | Cancel an order. Returns the cancelled order with its CancelledDate set. |
| Change Asset Quantity | `changeAssetQuantity` | Change the quantity of one or more assets, writing the amendment lines into a cart. The request root is a JSON array of change requests, each with AssetId and Quantity. |
| Checkout Cart To Order | `checkoutCartToOrder` | Check a finalized cart out directly into an order, skipping the quote. Set isAsync for large carts. |
| Checkout Cart To Quote | `checkoutCartToQuote` | Check a finalized cart out into a quote. Optionally set quote header values such as name, primary contact and bill-to or ship-to account at the same time. |
| Clone Cart | `cloneCart` | Clone a cart, optionally copying its line items, repricing the copy and retaining the source cart's approval status. |
| Clone Quote | `cloneQuote` | Clone an existing quote, optionally copying its line items. Returns the new quote. |
| Convert Contract Request To Agreement | `convertContractRequest` | Convert an approved contract request into a contract (agreement). |
| Create Account | `createAccount` | Create an Account record. Returns the new record's ID in Data. Set includeRecordPayloadInResponse to true to get the full record back instead. |
| Create Agreement From Quote | `createAgreementFromQuote` | Create a CLM agreement (contract) from an accepted quote. This is the CPQ-to-CLM handoff. Pass overrideValues to set contract fields that should differ from the quote's. |
| Create And Send Sign Transaction | `sendSignTransaction` | Create a Conga Sign transaction and send it to its signers. The payload shape depends on the org's sign configuration, so it is passed as a JSON object string and sent verbatim. |
| Create Carts | `createCarts` | Create one or more CPQ carts. Conga takes a JSON array at the request root, so the carts are passed as a JSON array string and sent verbatim. Common fields: name, account, priceList, businessObjectId, businessObjectType, effectiveDate, expectedStartDate, expectedEndDate, currency. |
| Create Contact | `createContact` | Create a Contact record. Returns the new record's ID in Data. Link it to an Account by passing the Account JSON lookup. |
| Create Contract | `createContract` | Create a CLM contract (agreement) record. RecordType names the contract type configured in the org, such as MSA or NDA. A new contract normally starts in the Request status category. |
| Create Contract Clause | `createContractClause` | Create a clause on a contract. The clause field set is org-specific, so the clause is passed as a JSON object string and sent verbatim. |
| Create Contract Request | `createContractRequest` | Create a contract request. The payload carries a RequestHeader and RequestDetails and is org-specific, so it is passed as a JSON object string and sent verbatim. Convert the request to an agreement later with convertContractRequest. |
| Create Custom Object Record | `createCustomObjectRecord` | Create a record on any custom object. The field set differs per object, so the record body is passed as a JSON object string and sent verbatim. Returns the new record's ID in Data. |
| Create Opportunity | `createOpportunity` | Create an Opportunity record. Returns the new record's ID in Data. Link it to an Account and a primary Contact with the JSON lookup fields. |
| Create Orders | `createOrders` | Add one or more orders. Conga takes a JSON array at the request root, so the orders are passed as a JSON array string and sent verbatim. Common fields: Name, Type, Status, OrderDate, OrderStartDate, OrderEndDate, SoldToAccount, BillToAccount, ShipToAccount, PriceList, PrimaryContact, Currency, PONumber. |
| Create Quotes | `createQuotes` | Create one or more CPQ quotes. Conga takes a JSON array at the request root, so the quotes are passed as a JSON array string and sent verbatim. Common fields: Name, ProposalName, Account, Opportunity, PriceList, PrimaryContact, Currency, ExpectedStartDate, ExpectedEndDate, ValidUntilDate, IsPrimary. |
| Create Service Hook Rule | `createServiceHookRule` | Create a Conga Hooks rule. RuleType DataChange fires on Create, Update or Delete of an object when the condition matches; RuleType Schedule fires on a timer. The target is always custom code already deployed in the tenant, named by ProjectName, ClassName and MethodName - there is no callback URL. |
| Create User | `createUser` | Create a platform user and return its ID. Set userType to Integration to create the kind of user whose client ID and secret drive this connector's OAuth credentials. |
| Deactivate User | `deactivateUser` | Deactivate a user. This is a soft deactivation, not a hard delete - the identity status must be reviewed afterwards. Use Restore User to reverse it. |
| Delete Account | `deleteAccount` | Delete an Account record by its Conga record ID. |
| Delete Cart | `deleteCart` | Delete a CPQ cart by its ID. |
| Delete Cart Line Items | `deleteCartLineItems` | Remove line items from a cart. The request root is a JSON array of objects carrying the primaryLineNumber of each line to remove. |
| Delete Contact | `deleteContact` | Delete a Contact record by its Conga record ID. |
| Delete Contract | `deleteContract` | Delete a CLM contract by ID. |
| Delete Custom Object Record | `deleteCustomObjectRecord` | Delete a record of any custom object by object name and record ID. |
| Delete Opportunity | `deleteOpportunity` | Delete an Opportunity record by its Conga record ID. |
| Delete Quote | `deleteQuote` | Delete a CPQ quote by its ID. |
| Delete Service Hook Rule | `deleteServiceHookRule` | Delete a Conga Hooks rule by name. |
| Finalize Cart | `finalizeCart` | Finalize a cart, locking its configuration and pricing so it can be checked out to a quote or an order. Set hasAcceptedWarning to true to proceed past non-blocking warnings. |
| Generate Contract Document | `generateContractDocument` | Generate a contract document from a template. Use queryTemplates to find a TemplateId. Optionally set an output format, watermark and protection level. |
| Get Account | `getAccount` | Retrieve a single Account record by its Conga record ID (a GUID). |
| Get Active Cart | `getActiveCart` | Get the latest active cart for the calling user, optionally narrowed by a URI-format filter. |
| Get Active Price List | `getActivePriceList` | Retrieve the active price list, optionally resolved for a specific account or storefront. Call this first to get the priceListId that the catalog and cart actions need. |
| Get Approval Request | `getApprovalRequest` | Retrieve a single approval request by its request ID. Use this after submitting for approval or after listing a user's pending approvals to read the request's current assignee, step and status. |
| Get Billing Schedules | `getBillingSchedules` | Get the billing schedule records under a billing header. This is the read entry point into Conga Billing, which the connector otherwise did not cover. The API returns a bare array, wrapped here as an items object. |
| Get Cart | `getCart` | Retrieve a single CPQ cart by ID, optionally including related entities such as line-items, adjustments, price-breakups, usage-tiers or summary-groups. |
| Get Cart Status | `getCartStatus` | Retrieve the pricing and configuration status of a cart and its lines. Use this to poll after an asynchronous reprice or configuration pass. |
| Get Contact | `getContact` | Retrieve a single Contact record by its Conga record ID. |
| Get Contract | `getContract` | Get a CLM contract's details by ID. |
| Get Contract Hierarchy | `getContractHierarchy` | Get the hierarchy of a contract: its parent, amendments and renewals. Use this to walk a contract family rather than stitching it together from individual records. |
| Get Credit Memo | `getCreditMemo` | Retrieve a credit memo with its line items and associated AR transactions. The invoicing counterpart to Get Invoice. |
| Get Custom Object Record | `getCustomObjectRecord` | Retrieve a single record of any custom object by object name and record ID. |
| Get Document Metadata | `getDocumentMetadata` | Get a document's metadata by document ID: name, extension, MIME type, size, version, checkout state and the object it is attached to. |
| Get E-Signature Transaction | `getEsignTransaction` | Get an e-signature transaction's details by transaction ID, including its signers and current status. |
| Get Email Job Status | `getEmailJobStatus` | Get the delivery status of a sent email by the JobId returned from Send Email. Returns the per-recipient delivery state and the event timeline (Delivered, Bounced, Opened and so on). |
| Get Field Metadata | `getFieldMetadata` | Get the metadata for one field on an object: data type, picklist values, lookup target and constraints. |
| Get Invoice | `getInvoice` | Retrieve an invoice's details by ID. |
| Get Latest Sign Transaction For Record | `getLatestSignTransaction` | Get the latest e-signature transaction for a record, such as a contract or a quote, by that record's object ID. Use this to check whether a contract is out for signature and where it stands. |
| Get My Approvals Count | `getMyApprovalsCount` | Count the approvals pending for the calling user, broken down per business object. The calling user is the one named by the user-id credential header. The API returns a bare array, wrapped here as an items object. |
| Get Object Approval Status | `getObjectApprovalStatus` | Get the approval status of a context object (Agreement, Quote, Order, or any approval-enabled business object) by its type and ID. Returns whether the object is submitted, cancelled, completed or recallable, its approval_status, and which comment fields the process makes mandatory. This is the polling counterpart to Submit For Approval. |
| Get Object Schema | `getObjectSchema` | Get the full schema definition of an object, including its field definitions and types. Use this to build field mappings and to check which fields are indexed before writing a query criteria. |
| Get Opportunity | `getOpportunity` | Retrieve a single Opportunity record by its Conga record ID. |
| Get Order | `getOrder` | Retrieve a single order by its unique identifier. |
| Get Organization Info | `getOrganizationInfo` | Get the organization's sitewide settings: number, date and currency formats. A zero-input read, so it also serves as a connection health check. |
| Get Product | `getProduct` | Get a product's details, including its option groups, attributes, prices and categories when requested through includes. Use depth to walk a bundle's sub-bundles. |
| Get Quote | `getQuote` | Retrieve a single CPQ quote by its ID. |
| Get Quote Job Status | `getQuoteJobStatus` | Poll the status of an asynchronous quote job, such as an acceptQuote call made with isAsync set to true. |
| Get User | `getUser` | Get a platform user's details by user ID. |
| Global Search | `globalSearch` | Run a keyword search across every object configured for global search. Restrict or exclude objects with objectList and excludeObjectList, and page with Skip and Limit. |
| Launch Cart For Quote | `launchCartForQuote` | Launch (activate) the configuration cart for a quote. This is the entry point to CPQ configuration: call it first, then add line items, reprice, validate and finalize. |
| List Accounts | `listAccounts` | List Account records from the Conga Advantage Platform data service. Supports a criteria predicate, paging and sorting. Note that any field used in criteria or sortField must be indexed on the object. |
| List Approval Comments | `listApprovalComments` | List the approval comments recorded against a context object, optionally narrowed to a single approval request. The API returns a bare array, wrapped here as an items object. |
| List Assets | `listAssets` | List installed-base asset line items: what an account currently owns or subscribes to. This is the starting point for renewals, amendments, terminations and swaps. |
| List Cart Line Items | `listCartLineItems` | Retrieve the line items on a cart, with optional filtering, sorting, grouping and paging. A maximum of 500 records is returned per page. |
| List Carts | `listCarts` | List CPQ configuration carts. A cart is the working configuration behind a quote or order: it holds the line items, pricing and adjustments until it is finalized and checked out. |
| List Categories | `listCategories` | List catalog categories (the classification hierarchy) for a price list. Use depth to limit how far down the hierarchy is walked. |
| List Contacts | `listContacts` | List Contact records. Supports a criteria predicate, paging and sorting. Fields used in criteria or sortField must be indexed. |
| List Contract Clauses | `listContractClauses` | Get the clauses on a contract. Despite being a POST, this is a read: the body carries the query criteria, sort and paging. |
| List Custom Object Records | `listCustomObjectRecords` | List records of any custom object by object name. Supports a criteria predicate, paging and sorting. Fields used in criteria or sortField must be indexed. |
| List Email Templates | `listEmailTemplates` | List the org's email templates with filter, sort and paging. Use the returned template IDs with the Conga email service to render or send templated mail. |
| List Object Documents | `listObjectDocuments` | List the documents attached to a business object, for example every generated or uploaded document on an Agreement. Returns document metadata only; the binary download endpoint is not exposed because fastn cannot relay octet-stream responses. |
| List Object Names | `listObjectNames` | List every object name available in the org's schema. Use this to populate an object picker before calling any of the custom-object record actions. |
| List Opportunities | `listOpportunities` | List Opportunity records. Supports a criteria predicate, paging and sorting. Fields used in criteria or sortField must be indexed. |
| List Order Line Items | `listOrderLineItems` | Retrieve all line items on an order, with optional filtering, sorting, paging and related-entity includes. |
| List Orders | `listOrders` | Search and retrieve orders. Supports URI-function filters, sorting, page/limit paging, field projection and related-entity includes. Default page size is 50. |
| List Products | `listProducts` | List sellable products for a price list. Conga takes the price list and storefront as request headers, so priceListId is passed through the pricelistid header. Defaults to 50 records per page, maximum 500. |
| List Products In Category | `listCategoryProducts` | Retrieve the products in a catalog category. The category ID is the classification hierarchy ID returned by listCategories. |
| List Quotes | `listQuotes` | Retrieve CPQ quotes (proposals). Supports URI-function filters, sorting, page/limit paging, field projection and related-resource includes. |
| List Replacement Products | `listReplacementProducts` | List the products an existing product can be swapped to. Use this before swapAsset to pick a valid replacement. |
| List Roles | `listRoles` | List the org's roles with their permission groups. Use the returned role IDs with Assign User Role. Criteria and sort fields must be indexed or sortable. |
| List Service Hook Event Types | `listServiceHookEventTypes` | List the event types a Conga Hooks rule can subscribe to. Call this before createServiceHookRule to see what the org supports. |
| List Service Hook Rules | `listServiceHookRules` | List the org's Conga Hooks rules. A rule fires custom code deployed in the tenant on a data change or a schedule. Conga has no callback-URL webhook, so these rules are the only native event mechanism. |
| List Usage Inputs | `listUsageInputs` | List usage input records: metered consumption submitted against a subscription for rating and billing. Supports the cart-family filter, sort, includes and paging vocabulary. The API returns a bare array, wrapped here as an items object. |
| List Users | `listUsers` | List platform users matching a criteria predicate, with paging and sorting. Useful for resolving owner and assignee IDs. |
| Query Accounts | `queryAccounts` | Run a structured query over Account records: criteria predicate, field selection, sort, group-by and Limit/Skip paging. This is the endpoint to use for incremental sync (criteria on ModifiedDate) and for selecting only the fields you need. Use the NextCursor from the response as the after parameter to continue. |
| Query Contacts | `queryContacts` | Run a structured query over Contact records: criteria predicate, field selection, sort, group-by and Limit/Skip paging. Use NextCursor as the after parameter to continue. |
| Query Contract Documents | `queryContractDocuments` | Query the documents attached to a contract, with criteria, field selection, sort and Limit/Skip paging. |
| Query Contract Requests | `queryContractRequests` | Search contract requests: the intake records that precede a contract. Supports criteria, field selection, sort and Limit/Skip paging. |
| Query Contract Templates | `queryContractTemplates` | Find CLM template records by type, name or record types. Use this to resolve the TemplateId that generateContractDocument needs. |
| Query Contracts | `queryContracts` | Search CLM contracts (agreements) with a criteria expression, field selection, sort, group-by and Limit/Skip paging. This is the main CLM read: there is no plain GET list for contracts. Results arrive nested at Data.Data with the count at Data.RecordCount. |
| Query Custom Object Records | `queryCustomObjectRecords` | Run a structured query over any custom object: criteria predicate, field selection, sort, group-by and Limit/Skip paging, plus cursor paging via NextCursor. |
| Query Opportunities | `queryOpportunities` | Run a structured query over Opportunity records: criteria predicate, field selection, sort, group-by and Limit/Skip paging. |
| Reassign Approval Request | `reassignApprovalRequest` | Reassign an approval request to a different assignee. The documented 200 response body is a bare boolean, so it is exposed here as an object with a single result field. |
| Recall Approval Requests | `recallApprovalRequests` | Recall the in-flight approval requests for a context object, returning it to the submitter. Only valid when the object's approval status reports can_recall true. The documented 200 response body is a bare boolean, so it is exposed here as an object with a single result field. |
| Reject Approval Request | `rejectApprovalRequest` | Reject a single approval request by its request ID. The documented 200 response body is a bare boolean, so it is exposed here as an object with a single result field. Optional documented body field not templated: ApprovalFromEmail (boolean). |
| Renew Assets | `renewAssets` | Renew assets into a cart. Give a renewal term or an explicit end date, and optionally co-terminate on the farthest asset end date. Set useAssetPrice to keep the existing asset price and skip configuration and pricing. |
| Renew Contract | `renewContract` | Renew a CLM contract. Returns the ID of the renewal contract created from it. |
| Reprice Cart | `repriceCart` | Re-run pricing on a cart. Pass a JSON array of primary line numbers to reprice only those lines, or an empty array to reprice everything. |
| Restore User | `restoreUser` | Reactivate a previously deactivated user. The identity status must be reviewed afterwards. |
| Search Documents | `searchDocuments` | Search document metadata across the org with a criteria predicate, paging and sorting. Use this to find generated contract documents changed since a timestamp. Criteria fields must be indexed. |
| Search Object Records | `searchObjectRecords` | Run a search query against a single configured object through the search service, returning the fields named in Select. Complements Global Search, which spans every configured object. The object must have a search setting enabled and the criteria fields must be indexed. |
| Search Products | `searchProducts` | Faceted product search across a price list or category. Pass facets and point-of-sale line items in the body to narrow results the way the storefront does. |
| Send Email | `sendEmail` | Send a single email through the Conga platform email service. To, Cc and Bcc are passed as JSON array strings of address objects, e.g. [{\"Address\":\"a@b.com\",\"Name\":\"A B\"}], and are emitted verbatim. Optional documented body fields not templated here: From, FromEmailOption, ReplyTo, Attachments, Priority, Headers, ShouldProcessInbound, OutboundTraceId, EmailProfileName, TrackingOptions. |
| Submit For Approval | `submitForApproval` | Submit a context object (Agreement, Quote, Order, or any approval-enabled business object) into its configured approval process. Returns the resulting approval state for the object, including whether it is submitted, whether it can be recalled, and which comment fields the process makes mandatory. Optional documented body fields not templated here: StepComments (array), AttachmentIds (string), IsExternalId (boolean). |
| Swap Asset | `swapAsset` | Swap an asset for a different product as of an effective date, writing the swap lines into a cart. Use listReplacementProducts to find valid targets. |
| Terminate Assets | `terminateAssets` | Terminate assets as of a given date, writing the termination lines into a cart. |
| Terminate Contract | `terminateContract` | Terminate a CLM contract, ending it before its natural end date. |
| Update Account | `updateAccount` | Update an Account record by ID. Only the fields you supply are sent; omitted fields are left untouched. |
| Update Cart | `updateCart` | Update a CPQ cart by ID. The changed fields are passed as a JSON object string and sent verbatim. |
| Update Cart Line Items | `updateCartLineItems` | Update line items on a cart, for example to change quantity, dates or manual adjustments. The request root is a JSON array, so the items are passed as a JSON array string and sent verbatim; each entry must carry the line item's id. |
| Update Contact | `updateContact` | Update a Contact record by ID. Only the fields you supply are sent. |
| Update Contract | `updateContract` | Update a CLM contract record. The changed fields are passed as a JSON object string and sent verbatim, since the contract field set is configured per org. |
| Update Custom Object Record | `updateCustomObjectRecord` | Update a record on any custom object by object name and record ID. The changed fields are passed as a JSON object string and sent verbatim. |
| Update Opportunity | `updateOpportunity` | Update an Opportunity record by ID, for example to advance StageName. Only the fields you supply are sent. |
| Update Order | `updateOrder` | Modify a single order. The changed fields are passed as a JSON object string and sent verbatim. |
| Update Quote | `updateQuote` | Update a CPQ quote by ID. The changed fields are passed as a JSON object string and sent verbatim, since the quote field set is org-specific. |
| Update User | `updateUser` | Update a user's profile. Create, get and list users were already covered; this closes the identity-sync loop. Optional documented body fields not templated here: Role, Timezone, LocaleName and the other Locale* fields, Currency, PositiveCurrencyFormat, NegativeCurrencyFormat, IsSuspended, Alias, Language, Address, CustomProperties, FederationId, UserType. Use Assign User Role to change a user's role. |
| Upsert Custom Object Records | `upsertCustomObjectRecords` | Bulk upsert records on any custom object. The request body is a JSON array of records; records matched on the platform record identifier are updated, the rest are inserted. Use this for sync writes instead of per-record calls. |
| Upsert Quote | `upsertQuote` | Insert or update a quote in one call, matched on the record identifier carried in the payload. Use this for idempotent sync writes from an external system. |
| Validate Cart | `validateCart` | Run CPQ configuration and constraint validation on a cart. Call this before finalize to surface rule violations. |
