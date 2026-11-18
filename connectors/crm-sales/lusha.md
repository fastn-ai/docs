---
description: "Lusha B2B sales intelligence API (V3)."
hidden: true
---

# Lusha

Lusha B2B sales intelligence API (V3). Search, enrich, and prospect contacts and companies; AI lookalikes; real-time buying signals; decision makers; website-visit intent; prospecting/signal filter discovery; account usage/credits; and webhook subscription management for signal notifications. Base https://api.lusha.com, API key in the api_key header.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [lusha.com](https://lusha.com) |
| **Authentication** | API key |
| **Actions** | 34 |
| **Events** | 0 |
| **Slug** | `lusha` |

## Use it

Add Lusha from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.lusha.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Company Lookalikes | `companyLookalikes` | AI-powered recommendations for companies similar to 5-100 seed companies (via domains or linkedinUrls). Omit dedupeSessionId on the first call; pass the returned value on later calls to page without duplicates. Use 'exclude' to filter out companies. Charged per result via lookalikeCompany (1 credit per 5). |
| Company Signals | `companySignals` | Retrieve signal events (hiring, headcount changes, web traffic, IT spend, news) for up to 100 company ids. Use signalTypes (or allSignals); optionally set startDate. Charged per matched signal per result via showSignalsCompany (1 credit each). |
| Contact Lookalikes | `contactLookalikes` | AI-powered recommendations for contacts similar to 5-100 seed contacts (via linkedinUrls, emails, Lusha ids, or name+company). Omit dedupeSessionId on the first call (server returns one); pass it on later calls to page without duplicates (30-day retention). Use 'exclude' to always filter out contacts. Charged per result via lookalikeContact (1 credit per 5). |
| Contact Signals | `contactSignals` | Retrieve signal events (job changes, promotions) for up to 100 contact ids. Use signalTypes (promotion, companyChange, or allSignals); optionally set startDate. Charged per matched signal per result via showSignalsContact (1 credit each). |
| Create Opt-Out Subscription | `createOptOutSubscription` | Subscribe to real-time notifications when a contact opts out of data processing. Create one opt-out subscription per account (scoped to contact entity type). Lusha POSTs the contact identity, opt-out date, and data points to remove to your URL. Requires an account webhook secret. No credit cost. |
| Create Subscription | `createSubscription` | Create one or more webhook subscriptions (max 25 per request) for real-time signal notifications. 'defaults' sets url/entityType/signalTypes applied to all; each item in 'subscriptions' requires entityId and may override entityType/signalTypes/name. Requires an account webhook secret to exist first (see Regenerate Account Secret). |
| Delete Subscriptions | `deleteSubscriptions` | Delete one or more webhook subscriptions by ID (bulk, partial success supported, deduped). Invalid IDs are reported as NOT_FOUND. Deletion is permanent. No credit cost. |
| Enrich Companies | `enrichCompanies` | Reveal full firmographic data (size, revenue, industry, locations, technologies, funding, intent, social) for company ids from Search Companies. Pass up to 100 ids. Optional 'reveal' unlocks extra fields (employeesByDepartment/Location/Seniority, competitors, intent), each charged separately. Base charge revealCompany 1 credit per result. |
| Enrich Contacts | `enrichContacts` | Reveal full contact data (emails, phones, employment) for contact ids obtained from Search Contacts. Pass up to 100 ids. Use 'reveal' to control what to unlock (emails and/or phones); omit for both. Charged per revealed field: revealEmail 1 credit, revealPhone 5 credits. |
| Get Account Secret | `getAccountSecret` | Retrieve the current account webhook secret used to sign webhook deliveries (HMAC-SHA256). No credit cost. |
| Get Account Usage | `getAccountUsage` | Returns a full snapshot of your Lusha account: credits (total/used/remaining), rate limit windows (daily/hourly/minute), plan details, and per-action credit pricing. Does not consume credits. Rate limited to 5 requests/minute. |
| Get Audit Log Statistics | `getAuditLogStats` | Get webhook delivery statistics for your account (total, success, failed, successRate). Optionally filter by subscriptionId. No credit cost. |
| Get Audit Logs | `getAuditLogs` | Retrieve webhook delivery logs for your account (success and failures, status codes, response times, errors). Filter by subscriptionId and status. Paginate with limit (1-100) and offset. Logs retained 90 days (success) / 180 days (failed). No credit cost. |
| Get Company Filter Types | `getCompanyFilterTypes` | Discovery: returns all available filter types for company prospecting and whether each requires a search query (names, sizes, revenues, locations, sics, naics, industriesLabels, intentTopics, technologies). No credit cost. |
| Get Company Filter Values | `getCompanyFilterValues` | Returns valid values for a single company prospecting filter type. names, locations and technologies require a query (2-256 chars). No credit cost. The full live filter list is returned by Get Company Filter Types. |
| Get Company Signal Filter Values | `getCompanySignalFilterValues` | Returns valid values for a single company signal filter type. hiringByLocations requires a query (2-256 chars). No credit cost. |
| Get Company Signal Filters | `getCompanySignalFilters` | Discovery: returns all available filter types for company signals and whether each requires a search query (newsEventTypes, hiringByDepartments, hiringByLocations). No credit cost. |
| Get Company Signal Types | `getCompanySignalTypes` | Returns the full list of supported signal types for companies (headcount, hiring, web traffic, IT spend, news categories). No credit cost. |
| Get Contact Filter Types | `getContactFilterTypes` | Discovery: returns all available filter types for contact prospecting and whether each requires a search query (departments, seniority, existingDataPoints, countries, locations). No credit cost. |
| Get Contact Filter Values | `getContactFilterValues` | Returns valid values for a single contact prospecting filter type. locations, jobTitles, certifications and awards require a query (2-256 chars). No credit cost. The full live filter list is returned by Get Contact Filter Types. |
| Get Contact Signal Types | `getContactSignalTypes` | Returns the full list of supported signal types for contacts (e.g. allSignals, promotion, companyChange). No credit cost. |
| Get Decision Makers | `getDecisionMakers` | Retrieve the decision makers (buying group) at one or more companies, identified by domain or Lusha company id. Billed as buyingGroupReveal at 1 credit per decision maker returned, and the minimum page size is 10, so the cheapest possible call costs 10 credits. |
| Get Subscription | `getSubscription` | Returns a single webhook subscription by its ID. No credit cost. |
| Get Website Visits | `getWebsiteVisits` | Returns companies ranked by website-visit signals for your tracked domains and date range (must be configured for tracking in the Lusha dashboard). Each result combines a company firmographic preview with visit metrics (score, sessions, unique visitors, avg session length). Date range must be &lt;= 3 months; limit 1-150. If any requested domain is not tracked, the whole request 400s. |
| List Subscriptions | `listSubscriptions` | Returns all webhook subscriptions for your account, sorted by createdAt descending. Paginate with limit (1-100, default 10) and offset. No credit cost. |
| Prospecting Companies | `prospectingCompanies` | Search the Lusha company database with structured ICP filters and return a page of matching company profiles. pagination.page is zero-based and pagination.size must be between 10 and 50 - Lusha rejects a size below 10 with 400 'pagination.size must not be less than 10'. Billed at 1 credit per 25 results returned. |
| Prospecting Contacts | `prospectingContacts` | Search the Lusha contact database with structured contact and company filters and return a page of matching contact profiles (no emails or phones are revealed). pagination.page is zero-based and pagination.size must be between 10 and 50 - Lusha rejects a size below 10 with 400 'pagination.size must not be less than 10'. Billed at 1 credit per 25 results returned. |
| Regenerate Account Secret | `regenerateAccountSecret` | Regenerate (or create) the account webhook secret. Affects all subscriptions; the old secret is invalidated. The new secret is only shown once. An account secret must exist before webhooks can be delivered. No credit cost. |
| Search and Enrich Companies | `searchAndEnrichCompanies` | Find companies and reveal full firmographic data in one call. Provide the same identifiers as Search Companies. Up to 100 companies. Charged per successful result via reveal_company (1 credit). |
| Search and Enrich Contacts | `searchAndEnrichContacts` | Find contacts and reveal their full data (emails/phones) in one call. Provide the same identifiers as Search Contacts; use 'reveal' to control what to unlock. Up to 100 contacts. Two charges: api_search (1/25) plus per revealed field (revealEmail 1, revealPhone 5). |
| Search Companies | `searchCompanies` | Look up companies by identifier (Lusha id, name, or domain). Returns a preview per company with a 'has' list of data available via Enrich Companies. Up to 100 companies per request. Charged per successful result via api_search (1 credit per 25 results). |
| Search Contacts | `searchContacts` | Look up contacts by identifier (Lusha id, linkedinUrl, email, or firstName+lastName+companyName/companyDomain). Returns a non-PII preview per profile with 'has' and 'canReveal'. Up to 100 contacts per request. Charged per successful result via api_search (1 credit per 25 results). |
| Test Subscription | `testSubscription` | Send a test signal to a webhook subscription. Modes: direct (HTTP check only), kafka (fanout handler), full (end-to-end, default). Test deliveries use mock data and do NOT consume credits. |
| Update Subscription | `updateSubscription` | Update an existing webhook subscription (all body fields optional). Set isActive true to reactivate a disabled subscription (clears block reason and resets retries). Set regenerateSecret true to mint a new account webhook secret (returned once). No credit cost. |
