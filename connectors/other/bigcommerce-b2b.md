---
description: "BigCommerce B2B Edition Server-to-Server REST Management API (api-b2b.bigcommerce.com, base path /api/v3/io)."
hidden: true
---

# BigCommerce B2B Edition

<img src="../../.gitbook/assets/connectors/lg/bigcommerce-b2b.png" alt="BigCommerce B2B Edition logo">

BigCommerce B2B Edition Server-to-Server REST Management API (api-b2b.bigcommerce.com, base path /api/v3/io). Manage Companies (CRUD, extra fields, attachments, status, catalogs/price-list assignment, hierarchy), Company Users, Addresses, Quotes/RFQ (CRUD, products, shipping rates, checkout/order, email, PDF), B2B Orders, Shopping Lists (CRUD + items), Sales Reps (sales staff), Super Admins / user assignment, Roles & Permissions, Invoices & Payments, Channels, and Storefront/backend token generation. Authenticates with a store-level X-Auth-Token API token.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [bigcommerce.com](https://bigcommerce.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `bigcommerceB2b` |

## Use it

Add BigCommerce B2B Edition from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bigcommerceB2b.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Assign Company Parent | `assignCompanyParent` | Assign a parent company to a B2B company, building an account hierarchy. |
| Assign Super Admins to Company | `assignCompanySuperAdmins` | Assign or unassign super admins to/from a company. |
| Bulk Create Addresses | `bulkCreateAddresses` | Create multiple B2B addresses in a single request. |
| Bulk Create Companies | `bulkCreateCompanies` | Create multiple B2B companies in a single request. |
| Bulk Create Company Users | `bulkCreateCompanyUsers` | Create multiple B2B company users in a single request. |
| Bulk Create Super Admins | `bulkCreateSuperAdmins` | Create multiple B2B super admins in a single request. KNOWN ISSUE (unfixed): the live API requires the request body to be a bare top-level JSON array of super admin objects, not an object wrapping a 'superAdmins' key (live-verified: wrapped body -&gt; 422 'Expected a list of items but got type dict'). Reverted to the wrapped-object form (functionally identical to the original) since none of the attempted fixes work; this action remains broken until the platform supports a bodyTemplate that resolves to a bare array. |
| Bulk Update Companies | `bulkUpdateCompanies` | Update multiple B2B companies in a single request. |
| Checkout Quote | `checkoutQuote` | Create a checkout from a B2B quote so the buyer can complete payment. |
| Convert Customer Group to Company | `convertCustomerGroupToCompany` | Convert a BigCommerce customer group into a B2B company. Provide the default company + admin details applied to the created company. |
| Convert Customer Orders to B2B | `convertCustomerOrdersToB2b` | Convert a customer's existing BigCommerce orders into B2B orders. |
| Create Address | `createAddress` | Create a new address for a B2B company. Note: the httpConfig previously used a hardcoded JSON-string bodyTemplate that only forwarded the 7 required fields - every optional field (zipCode, isBilling, isShipping, phoneNumber, label, extraFields, stateCode, countryCode, externalId, isDefaultBilling, isDefaultShipping, addressLine2) was silently dropped regardless of what the caller sent (live-verified: sent zipCode/isBilling/isShipping, Get Address confirmed all three came back null/false). Fixed to a templated object bodyTemplate that forwards every field. |
| Create B2B Order | `createOrder` | Associate an existing BigCommerce order with a B2B customer / company. |
| Create Backend Token | `createBackendToken` | [DEPRECATED] Retired by BigCommerce. "As of September 30, 2025, the B2B Edition API authToken is deprecated and replaced by the standard BigCommerce API X-Auth-Token used together with a new header X-Store-Hash" (https://docs.bigcommerce.com/developer/docs/b2b-edition/getting-started/authentication) - the notice names "Get a Server to Server Token" explicitly. POST /api/v3/io/auth/backend now answers 404 Not Found. Use a store-level API account token via X-Auth-Token + X-Store-Hash instead; every other action on this connector already does. |
| Create Company | `createCompany` | Create a new B2B company account along with its admin user. Company addresses are NOT set here - create them separately against the company via the Addresses resource (see createAddress). Note: the httpConfig previously used a hardcoded JSON-string bodyTemplate that only forwarded the 7 required fields - every optional field (uuid, catalogId, channelIds, extraFields, customerGroupId, originChannelId, adminPhoneNumber, acceptCreationEmail) was silently dropped regardless of what the caller sent. Fixed to a templated object bodyTemplate that forwards every field (this is the same bug class found and fixed in Create Address). |
| Create Company Attachment | `createCompanyAttachment` | Attach a file (by URL) to a B2B company account. Note: the real API field for the file URL is 'attachment_file', not 'fileUrl' as previously sent (live-verified: sending fileUrl 422'd 'attachment_file: This field may not be null.'). Fixed the httpConfig to map input.fileUrl onto attachment_file. |
| Create Company Permission | `createCompanyPermission` | Create a custom B2B company permission. Note: hardcoded string bodyTemplate previously dropped the optional 'description' field (same bug class as Create Address/Create Company/Create Company User in this connector); fixed to a templated object. |
| Create Company Role | `createCompanyRole` | Create a new B2B company role with a set of permissions. |
| Create Company User | `createCompanyUser` | Create a new B2B company user under a company. Note: the httpConfig previously used a hardcoded JSON-string bodyTemplate that only forwarded the 5 required fields, silently dropping extraFields, phoneNumber, originChannelId, acceptWelcomeEmail (same bug class as Create Address/Create Company). Fixed to a templated object bodyTemplate. |
| Create Invoice | `createInvoice` | Create a B2B invoice. |
| Create Invoice from Order | `createInvoiceFromOrder` | Create a B2B invoice from a BigCommerce order. |
| Create Offline Payment | `createOfflinePayment` | Record an offline payment against one or more B2B invoices. |
| Create Quote | `createQuote` | Create a new B2B quote (RFQ) with a product list and totals. Note: (1) 'expiredAt' is actually required by the live API despite being documented optional - now marked required. (2) each productList item needs both a real sku AND a real productId from the store's catalog. (3) hardcoded string bodyTemplate previously dropped notes/message/currency/companyId/legalTerms/quoteTitle/bcCustomerId/allowCheckout/referenceNumber/shippingAddress - fixed to a templated object. |
| Create Shopping List | `createShoppingList` | Create a new B2B shopping list, optionally with items. Note: hardcoded string bodyTemplate previously dropped optional 'items' and 'channelId' fields (same bug class found across this connector); fixed to a templated object. |
| Create Super Admin | `createSuperAdmin` | Create a B2B super admin user. Note: hardcoded string bodyTemplate previously dropped optional phone/channelIds/extraFields/originChannelId (same bug class as other Create actions in this connector); fixed to a templated object. |
| Create Webhook (B2B Events) | `createWebhook` | Register a BigCommerce v3 webhook subscription for a B2B Edition event scope (e.g. store/company/created, store/company/user/created, store/quote/created). Uses the standard Webhooks v3 API at api.bigcommerce.com/stores/{storeHash}/v3/hooks with the connection's store token. Returns the created hook with its id and active state. |
| Delete Address | `deleteAddress` | Delete a B2B address by its address ID. |
| Delete Backend Token | `deleteBackendToken` | [DEPRECATED] Retired by BigCommerce. "As of September 30, 2025, the B2B Edition API authToken is deprecated and replaced by the standard BigCommerce API X-Auth-Token used together with a new header X-Store-Hash" (https://docs.bigcommerce.com/developer/docs/b2b-edition/getting-started/authentication) - the notice names "Delete Backend API Tokens" explicitly. The endpoint now answers 404 Not Found. There are no backend authTokens left to delete; use a store-level API account token via X-Auth-Token + X-Store-Hash. |
| Delete Company | `deleteCompany` | Delete a B2B company account by ID. |
| Delete Company Attachment | `deleteCompanyAttachment` | Delete a file attachment from a B2B company account. |
| Delete Company Permission | `deleteCompanyPermission` | Delete a B2B company permission by permission ID. |
| Delete Company Role | `deleteCompanyRole` | Delete a B2B company role by role ID. |
| Delete Company User | `deleteCompanyUser` | Delete a B2B company user by user ID. |
| Delete Invoice | `deleteInvoice` | Delete a B2B invoice by invoice ID. |
| Delete Payment | `deletePayment` | Delete a B2B payment by payment ID. |
| Delete Quote | `deleteQuote` | Delete a B2B quote (RFQ) by quote ID. |
| Delete Quote Shipping Rate | `deleteQuoteShippingRate` | Remove the selected shipping rate from a B2B quote. |
| Delete Shopping List | `deleteShoppingList` | Delete a B2B shopping list by ID. |
| Delete Shopping List Item | `deleteShoppingListItem` | Delete an item from a B2B shopping list. |
| Delete Webhook (B2B Events) | `deleteWebhook` | Delete a BigCommerce v3 webhook subscription by id, removing a B2B Edition event subscription. Uses the standard control-plane Webhooks v3 API at api.bigcommerce.com/stores/{storeHash}/v3/hooks/{id} with a store-level X-Auth-Token (not the B2B Edition token). Returns 204 No Content on success. |
| Download Invoice PDF | `downloadInvoicePdf` | Download the PDF for a B2B invoice. |
| Export Quote PDF | `exportQuotePdf` | Generate a PDF export of a B2B quote. |
| Get Address | `getAddress` | Get a single B2B address by its address ID. |
| Get Addresses By External ID | `getAddressesByExternalId` | Look up B2B company addresses by the external ID assigned in a third-party system (e.g. an ERP). Calls GET /api/v3/io/addresses with the externalId[] filter. Returns a list (usually 0 or 1 match); data is empty when no address carries that external ID. |
| Get B2B Order | `getOrder` | Get B2B order data (company association, purchaser) for a BigCommerce order ID. |
| Get B2B Order Products | `getOrderProducts` | Get the product line items for a B2B order. |
| Get Channel | `getChannel` | Get a single storefront channel by channel ID. |
| Get Company Credit | `getCompanyCredit` | Get the store credit configuration for a B2B company. |
| Get Company Details | `getCompany` | Get details of a single B2B company by its company ID. |
| Get Company Hierarchy | `getCompanyHierarchy` | Get the account hierarchy tree for a B2B company. |
| Get Company Payment Methods (By Company) | `getCompanyPaymentMethodsByCompany` | List all payment methods for one Company, indicating which are enabled for its users. GET /api/v3/io/companies/{companyId}/payments. |
| Get Company Payment Terms | `getCompanyPaymentTerms` | Get the payment terms for a B2B company. |
| Get Company Role | `getCompanyRole` | Get a single B2B company role by role ID. |
| Get Company User | `getCompanyUser` | Get a single B2B company user by user ID. |
| Get Invoice | `getInvoice` | Get a single B2B invoice by invoice ID. |
| Get Payment | `getPayment` | Get a single B2B payment by payment ID. |
| Get Payment Transactions | `getPaymentTransactions` | List the transactions for a B2B payment. |
| Get Quote | `getQuote` | Get a single B2B quote (RFQ) by its quote ID. |
| Get Quote Shipping Rates | `getQuoteShippingRates` | Get available shipping rates for a B2B quote. |
| Get Sales Rep | `getSalesRep` | Get a single B2B sales representative by sales staff ID. |
| Get Shopping List | `getShoppingList` | Get a single B2B shopping list (with its items) by ID. |
| Get Storefront API authToken | `getStorefrontAuthStatus` | Returns an existing B2B storefront authToken from the JWT of an active storefront session. GET https://api-b2b.bigcommerce.com/api/io/auth/storefront?jwtToken=...&channelId=... per https://docs.bigcommerce.com/developer/api-reference/rest/b2b/management/authentication/get-auth-storefront and https://docs.bigcommerce.com/developer/docs/b2b-edition/getting-started/authentication#get-a-storefront-api-authtoken. jwtToken is REQUIRED and must come from the BigCommerce Current Customer API for a signed-in Company user; it cannot be produced server-side. channelId is optional and should be omitted on single-storefront stores (the vendor documents unpredictable behaviour if it is sent there). Corrected 2026-09-03: the path was /api/v3/io/auth/storefront, which does not exist and 404d, and jwtToken was missing entirely. |
| Get Storefront Token (by Credentials) | `getStorefrontTokenByCredentials` | Generate a B2B storefront authToken using a company user's login email and password. |
| Get Storefront Token (by Customer ID) | `getStorefrontToken` | Generate a B2B storefront authToken for a company user, based on a BigCommerce customer ID. |
| Get Super Admin Info | `getSuperAdminInfo` | Get details for a B2B super admin by super admin ID. |
| Get User by BigCommerce Customer ID | `getUserByCustomerId` | Get the B2B company user associated with a BigCommerce customer ID. |
| Get Webhook (B2B Events) | `getWebhook` | Get a single BigCommerce v3 webhook subscription by id. Uses the standard control-plane Webhooks v3 API at api.bigcommerce.com/stores/{storeHash}/v3/hooks/{id} with a store-level X-Auth-Token (not the B2B Edition token). |
| List Address Extra Field Configs | `listAddressExtraFields` | List the extra-field configurations defined for addresses. |
| List Addresses | `listAddresses` | List B2B company addresses with optional filtering and pagination. |
| List B2B Orders | `listOrders` | List B2B orders with optional filters and pagination (GET /api/v3/io/orders). Set showExtra=true to include each order's extraFields. Filters: companyId, bcOrderId (BigCommerce order ID), min/maxCreated and min/maxModified (Unix seconds); sort with sortBy (createdAt\|updatedAt) and orderBy (ASC\|DESC). |
| List Backend Tokens | `listBackendTokens` | [DEPRECATED] Retired by BigCommerce, part of the same backend authToken family. The B2B Edition API authToken was deprecated on 2025-09-30 and replaced by the standard BigCommerce X-Auth-Token plus X-Store-Hash (https://docs.bigcommerce.com/developer/docs/b2b-edition/getting-started/authentication); GET /api/v3/io/backend/tokens answers 404 Not Found, consistent with the create and delete endpoints of the same family, which that notice names explicitly. Use a store-level API account token via X-Auth-Token + X-Store-Hash. |
| List Channels | `listChannels` | List the storefront channels available in B2B Edition. |
| List Companies | `listCompanies` | List all B2B companies with optional filtering and pagination. |
| List Companies for Super Admins | `listSuperAdminsCompanies` | List companies available for super admin assignment. |
| List Company Attachments | `listCompanyAttachments` | List file attachments on a B2B company account. |
| List Company Extra Field Configs | `listCompanyExtraFields` | List the extra-field configurations defined for company accounts. |
| List Company Payment Methods | `listCompanyPaymentMethods` | List the payment methods available to B2B companies. |
| List Company Permissions | `listCompanyPermissions` | List the available B2B company permission codes. |
| List Company Roles | `listCompanyRoles` | List B2B company roles. |
| List Company Subsidiaries | `listCompanySubsidiaries` | List the subsidiary (child) companies of a B2B company. |
| List Company Super Admins | `listCompanySuperAdmins` | List the super admins assigned to a specific company. |
| List Company Users | `listCompanyUsers` | List B2B company users (GET /api/v3/io/users) with optional filters and pagination. Filter by role with `roles` (0=admin, 1=senior buyer, 2=junior buyer); set isIncludeExtraFields=1 to include each user's extra fields in the response. Note: this action previously exposed a `role` (singular) filter that the vendor ignores (live check: role=0 returned all users, roles=0 returned only admins); it was renamed to `roles` to match the documented parameter. Callers passing `role` must switch to `roles`. |
| List Countries | `listCountries` | Look up a country by name or ISO code. searchType=0 searches by name, 1 by two-letter ISO code; q is the value to match. |
| List Custom Shipping Methods | `listQuoteCustomShippingMethods` | List custom shipping methods available for B2B quotes. |
| List Invoice Extra Field Configs | `listInvoiceExtraFields` | List the extra-field configurations defined for invoices. |
| List Invoices | `listInvoices` | List B2B invoices with optional filtering and pagination. |
| List Order Extra Field Configs | `listOrderExtraFields` | List the extra-field configurations defined for B2B orders. |
| List Payments | `listPayments` | List B2B invoice payments with optional filtering. |
| List Quote Extra Field Configs | `listQuoteExtraFields` | List the extra-field configurations defined for quotes. |
| List Quotes | `listQuotes` | List B2B quotes (RFQ) with optional filtering and pagination. |
| List Sales Reps | `listSalesReps` | List B2B sales representatives (sales staff). |
| List Shopping Lists | `listShoppingLists` | List B2B shopping lists for a customer. Requires customerId (BigCommerce customer id) or userId. |
| List States | `listStates` | Look up a state/province within a country. searchType=0 searches by state name, 1 by state abbreviation; q is the state value; country is the country code or name (e.g. US). |
| List Super Admin Companies | `listSuperAdminCompanies` | List the companies assigned to a B2B super admin. |
| List User Extra Field Configs | `listUserExtraFields` | List the extra-field configurations defined for company users. |
| List Webhooks (B2B Events) | `listWebhooks` | List all BigCommerce v3 webhook subscriptions for the store, including any registered B2B Edition event hooks. Uses the standard Webhooks v3 API at api.bigcommerce.com/stores/{storeHash}/v3/hooks with the connection's store token. |
| Mark Quote Ordered | `markQuoteOrdered` | Associate a placed BigCommerce order with a B2B quote (mark the quote as ordered). |
| Remove Company Subsidiary | `removeCompanySubsidiary` | Remove a subsidiary (child) company from a parent company's hierarchy. |
| Select Quote Shipping Rate | `selectQuoteShippingRate` | Select a shipping rate (or set a custom shipping method) for a B2B quote. |
| Send Quote Email | `sendQuoteEmail` | Send a B2B quote to a recipient by email. |
| Update Address | `updateAddress` | Update a B2B address by address ID (PUT /api/v3/io/addresses/{addressId}). Partial update: every body field is optional, so you can send only externalId (e.g. an ERP/D365 LocationId). Send isBilling/isShipping when changing isDefaultBilling/isDefaultShipping. |
| Update B2B Order | `updateOrder` | Update a B2B order's PO number and/or extra fields (PUT /api/v3/io/orders/{bcOrderId}). bcOrderId is the BigCommerce order ID. Send at least one of poNumber or extraFields; either can be sent alone. extraFields is an array of {fieldName, fieldValue}. |
| Update Company | `updateCompany` | Update an existing B2B company account by ID (PUT /api/v3/io/companies/{companyId}). Per the vendor docs every body field is optional; only the fields you send are forwarded, including extraFields [{fieldName, fieldValue}] and the company's primary address (addressLine1, addressLine2, city, state, zipCode, country). Additional per-company addresses are still managed via the Addresses resource (see updateAddress/createAddress). Note: the httpConfig previously used a hardcoded JSON-string bodyTemplate that only forwarded companyName, companyEmail, companyPhone, country and description, silently dropping extraFields and the address fields (same bug class fixed in Create Address / Create Company / Create Company User), and a company name containing a double quote produced invalid JSON. Fixed to a templated object bodyTemplate that forwards every field. |
| Update Company Catalogs (Assign Price List) | `updateCompanyCatalogs` | Assign a catalog / price list to a B2B company by setting its catalogId. |
| Update Company Credit | `updateCompanyCredit` | Update a B2B company's credit settings: turn credit on or off, set the currency and available credit, limit purchases above available credit, or put the company on credit hold. All fields are optional, but send at least one. Fails with 'Store company credit is not enabled' when the store has the company credit feature off. |
| Update Company Payment Methods | `updateCompanyPaymentMethods` | Enable or disable payment methods for one Company. PUT /api/v3/io/companies/{companyId}/payments with payments [{code, isEnabled}]. Only the listed methods change. |
| Update Company Payment Terms | `updateCompanyPaymentTerms` | Set the payment terms (e.g. net days) for a B2B company. |
| Update Company Permission | `updateCompanyPermission` | Update a B2B company permission by permission ID. |
| Update Company Role | `updateCompanyRole` | Update a B2B company role by role ID. |
| Update Company Status | `updateCompanyStatus` | Update the approval status of a B2B company (0=pending,1=approved,2=rejected,3=inactive). |
| Update Company User | `updateCompanyUser` | Update an existing B2B company user by user ID. Note: hardcoded string bodyTemplate previously dropped optional role/email/extraFields/phoneNumber (same bug class as other Create/Update actions in this connector); fixed to a templated object. |
| Update Invoice | `updateInvoice` | Update a B2B invoice by invoice ID: status, balances, dates, PO number, details, extra fields and external IDs. Only the fields you send are changed. |
| Update Offline Payment | `updateOfflinePayment` | Update an offline B2B payment by payment ID. |
| Update Order Company Association | `updateOrderCompany` | Bulk update the company association of B2B orders for a customer. |
| Update Quote | `updateQuote` | Update an existing B2B quote (RFQ) by quote ID. |
| Update Sales Rep | `updateSalesRep` | Update a B2B sales representative's assigned companies/channels by sales staff ID. |
| Update Shopping List | `updateShoppingList` | Update a B2B shopping list and its items by ID. Note: hardcoded string bodyTemplate previously dropped optional 'items' field (same bug class as Create Shopping List); fixed to a templated object. |
| Update Super Admin | `updateSuperAdmin` | Update a B2B super admin's company assignments by super admin ID. Provide a companies array of {companyId, isAssigned} entries. |
| Update Super Admin Info | `updateSuperAdminInfo` | Update profile details for a B2B super admin by super admin ID. Note: hardcoded string bodyTemplate previously dropped optional 'phone' field; fixed to a templated object. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Company Address Created | `store/company/address/created` | Fires when an address is added to a B2B Company account. Payload data carries company_id and address_id. |
| Company Address Deleted | `store/company/address/deleted` | Fires when an address is removed from a B2B Company account. Payload data carries company_id and address_id. |
| Company Address Updated | `store/company/address/updated` | Fires when an address on a B2B Company account is updated. Payload data carries company_id and address_id. |
| Company Created | `store/company/created` | Fires when a new B2B Company account is created. The payload data object carries the company_id. |
| Company Status Changed | `store/company/statusChanged` | Fires when a B2B Company account's activity status changes (e.g. pending to approved). Payload data carries company_id. |
| Company Updated | `store/company/updated` | Fires when a B2B Company account's information is updated. Payload data carries company_id. |
| Company User Created | `store/company/user/created` | Fires when a Company user (a B2B buyer with a Buyer Portal account linked to a Company) is created. Payload data carries company_id and user_id. |
| Company User Deleted | `store/company/user/deleted` | Fires when a Company user is removed. Payload data carries company_id and user_id. |
| Company User Updated | `store/company/user/updated` | Fires when a Company user is updated. Payload data carries company_id and user_id. |
| Quote Created | `store/quote/created` | Fires when a new B2B sales quote (RFQ) is created across storefront channels. Payload data carries quote_id and quote_uuid. |
| Quote Updated | `store/quote/updated` | Fires when a B2B sales quote is updated (e.g. by a sales rep or a change in quote status). Payload data carries quote_id and quote_uuid. |
