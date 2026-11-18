---
description: "CompanyEnrich is a real-time B2B data API for company enrichment, company and people search, lookalike (similar company) discovery, workforce insights,…"
hidden: true
---

# CompanyEnrich

<img src="../../.gitbook/assets/connectors/lg/companyenrich.png" alt="CompanyEnrich logo">

CompanyEnrich is a real-time B2B data API for company enrichment, company and people search, lookalike (similar company) discovery, workforce insights, reverse email lookup and work-email resolution. This connector covers the full CompanyEnrich REST API: enrichment by domain, properties, batch and bulk jobs; company search, preview, count, scroll and async exports; similar companies; people lookup, search, scroll, email resolution, education and exports; jobs; company lists; geo, industry, keyword, technology and position lookups; and the current user's credit balance.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [companyenrich.com](https://companyenrich.com) |
| **Authentication** | Bearer token |
| **Slug** | `companyenrich` |

## Use it

Add CompanyEnrich from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.companyenrich.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Companies | `autocompleteCompanies` | Returns up to 10 companies whose domain matches a partial domain name, useful for autocompleting domains in your application. Free, no credits deducted. |
| Autocomplete Keywords | `autocompleteKeywords` | Returns keyword suggestions matching a partial keyword, for use in the keywords filter of company searches. |
| Autocomplete Positions | `autocompletePositions` | Returns job position (title) suggestions matching a partial title, for use in the position query filter of people searches. |
| Autocomplete Technologies | `autocompleteTechnologies` | Returns technology name suggestions matching a partial name, for use in the technologies filter of company searches. |
| Batch Enrich Companies | `batchEnrichCompanies` | Enriches up to 50 companies by domain in a single request and returns an array of company profiles. Costs 1 credit per domain enriched (5 more per company with expand=workforce). Batching is recommended for larger domain lists. |
| Count Companies | `countCompanies` | Returns the number of companies matching the given search criteria without retrieving the results. Accepts the same filters as Search Companies. Free, no credits deducted. |
| Count Similar Companies | `countSimilarCompanies` | Returns the number of lookalike companies that match the given seed domains and filters without retrieving them. Accepts the same inputs as Find Similar Companies. Free, no credits deducted. |
| Create Bulk Email Enrichment Job | `createBulkEmailEnrichmentJob` | Creates an asynchronous bulk work-email enrichment job for up to 1,000 people (person id plus optional domain) and returns its job id. Track it with Get Bulk Email Enrichment Job; an optional webhook URL is called on completion. Beta endpoint. Costs up to 10 credits per item, charged on completion for newly accessed found emails only. |
| Create Bulk Enrichment Job | `createBulkEnrichmentJob` | Creates an asynchronous bulk enrichment job for up to 10,000 domains and returns its job id immediately. Track progress with Get Bulk Enrichment Job; an optional webhook URL is called when processing completes. Costs 1 credit per domain successfully enriched, charged on completion. |
| Create Company Export Job | `createCompanyExportJob` | Creates an asynchronous export job for up to 50,000 companies from either a standard company search ('search' filters) or a similar-company search ('similar' filters) and returns its job id immediately. Track it with Get Company Export Job; an optional webhook URL is called on completion. Costs 1 credit per company returned, reserved when the job is created and settled on completion. |

<details>

<summary>See 38 more actions</summary>

* **Create Company List** `createCompanyList`: Creates a saved company list from a standard search ('search' filters, 1 credit per company) or a similar-company search ('similar' filters, 5 credits per company), adding up to the first 5,000 results. The list is not created when no companies match. Requires a plan with the 'lists' capability; other plans receive a 403.
* **Create People Export Job** `createPeopleExportJob`: Creates an asynchronous export job for up to 50,000 people matching the given people search filters (same fields as Search People) and returns its job id immediately. Track it with Get People Export Job; an optional webhook URL is called on completion. Costs 2 credits per person returned, reserved when the job is created and settled on completion.
* **Delete Company List** `deleteCompanyList`: Deletes a saved company list and all of its entries. Requires a plan with the 'lists' capability; other plans receive a 403.
* **Enrich Company By Domain** `enrichCompanyByDomain`: Enriches a company by its domain name and returns the full company profile (firmographics, industry, size, revenue, location, financials, socials, technologies). Costs 1 credit per call (5 more with expand=workforce). Returns 404 when the domain cannot be enriched. Set waitForEnrichment=false to return stored data immediately and schedule enrichment in the background without charging credits.
* **Enrich Company By Properties** `enrichCompanyByProperties`: Enriches a company by matching its properties instead of its domain. Provide at least one of name, linkedinUrl, linkedinId, twitterUrl, facebookUrl, instagramUrl or youTubeUrl; the best match is returned when the lookup is ambiguous. Costs 1 credit per call (5 more with expand=workforce).
* **Find Similar Companies** `findSimilarCompanies`: Finds lookalike companies similar to one or more seed companies given by domain, optionally narrowed by the same filters as Search Companies, with page-based pagination (at most 100 per request). Costs 5 credits per company returned, minimum 5 credits.
* **Get Bulk Email Enrichment Job** `getBulkEmailEnrichmentJob`: Returns the current status of a bulk email enrichment job with found, not-found and unavailable counts and, once completed, the results_url to download the results. Beta endpoint. Free, no credits deducted.
* **Get Bulk Enrichment Job** `getBulkEnrichmentJob`: Returns the current status of a bulk enrichment job, including counts and, once completed, the results_url to download the enrichment results. Free, no credits deducted.
* **Get Company By ID** `getCompanyById`: Returns a company's full profile by its CompanyEnrich ID, as returned by the enrichment and search endpoints. Costs 1 credit per call (5 more with expand=workforce).
* **Get Company Export Job** `getCompanyExportJob`: Returns the current status of a company search export job and, once completed, the results_url to download the export. Free, no credits deducted.
* **Get Company List** `getCompanyList`: Returns a saved company list by id. Requires a plan with the 'lists' capability; other plans receive a 403.
* **Get Company Workforce** `getCompanyWorkforce`: Returns workforce insights for a single company: observed employee count, employee range bucket, headcount by root department and monthly history. Provide exactly one of id or domain. Costs 5 credits per successful call.
* **Get Country By Code** `getCountryByCode`: Returns a country by its ISO 3166-1 alpha-2 code, with its name and coordinates.
* **Get Current User** `getCurrentUser`: Returns information about the authenticated user: user id, credit balance (used and total) and account capabilities such as list management, previews and search limits. Free, no credits deducted.
* **Get Job** `getJob`: Returns the details of a single asynchronous job by id: type, status, title, timestamps, credits charged and any error message. Free, no credits deducted.
* **Get People Export Job** `getPeopleExportJob`: Returns the current status of a people search export job and, once completed, the results_url to download the export. Free, no credits deducted.
* **Get Person By ID** `getPersonById`: Returns a person's profile by CompanyEnrich person ID (from people search or lookup results): name, position, seniority, department, location, socials, work experiences and optionally education. Costs 2 credits per call.
* **Get Person Education** `getPersonEducation`: Returns the education history of a person by CompanyEnrich person ID; an empty list when the person has no education records. Costs 1 credit per successful call.
* **List Bulk Enrichment Jobs** `listBulkEnrichmentJobs`: Returns a paginated list of the authenticated user's bulk enrichment jobs, optionally filtered by status. Free, no credits deducted.
* **List Company Export Jobs** `listCompanyExportJobs`: Returns a paginated list of the authenticated user's company search export jobs, optionally filtered by status. Free, no credits deducted.
* **List Company Lists** `listCompanyLists`: Returns all saved company lists of the current user. List management requires a plan with the 'lists' capability; other plans receive a 403.
* **List Industries** `listIndustries`: Returns the list of company industries with their associated NAICS codes, for use in the NAICS code filter of company searches.
* **List Jobs** `listJobs`: Returns a paginated list of all asynchronous jobs (bulk enrichment, exports and so on) of the authenticated user, optionally filtered by status and type. Free, no credits deducted.
* **List People Export Jobs** `listPeopleExportJobs`: Returns a paginated list of the authenticated user's people search export jobs, optionally filtered by status. Free, no credits deducted.
* **List Regions** `listRegions`: Returns all geographic regions with their ids, parent region and member country codes, for use in the regions filter of company searches.
* **Lookup Person By Email** `lookupPersonByEmail`: Looks up a person by email address: the company is resolved from the email domain and the person is matched by email local-part patterns. Returns the best deterministic match with position, seniority, department, location, work experiences and socials. Costs 5 credits per successful call; returns 404 when no match is found.
* **Preview Company Search** `previewCompanySearch`: Returns the top 25 companies matching the given search criteria as a free preview (id, name, domain, industry, description, keywords, logo) before running a full search. Accepts the same filters as Search Companies. Requires a Scale plan; other plans receive a 403.
* **Preview Similar Companies** `previewSimilarCompanies`: Returns the top 25 lookalike companies for the given seed domains and filters as a free preview before running a full similar search. Accepts the same inputs as Find Similar Companies. Requires a Scale plan; other plans receive a 403.
* **Resolve Person Email** `resolvePersonEmail`: Resolves a work email address for a person (by CompanyEnrich person ID) on a specific company domain; when domain is omitted the person's current experience domains are tried in seniority order. Returns a person summary, the selected domain, a status of pending, found, not-found or unavailable and, when found, the email and its certainty. Beta endpoint. Costs 10 credits per newly accessed found email.
* **Scroll Companies** `scrollCompanies`: Searches companies with cursor-based pagination so more than 10,000 results can be traversed: omit cursor for the first page and pass the returned nextCursor to fetch the next one. Accepts the same filters as Search Companies; at most 100 companies per request. Costs 1 credit per company returned, minimum 1 credit.
* **Scroll People** `scrollPeople`: Searches people with cursor-based pagination so more than 10,000 results can be traversed: omit cursor for the first page and pass the returned nextCursor for the next one. Accepts the same filters as Search People; at most 100 per request. Costs 2 credits per person returned, minimum 2 credits.
* **Scroll Similar Companies** `scrollSimilarCompanies`: Finds lookalike companies for the given seed domains with cursor-based pagination: omit cursor for the first page and pass the returned nextCursor for the next one. Accepts the same filters as Find Similar Companies; at most 100 per request. Costs 5 credits per company returned, minimum 5 credits.
* **Search Cities** `searchCities`: Searches cities by name or country codes and returns up to 100 per page with the ids used in the cities filter of company searches.
* **Search Companies** `searchCompanies`: Searches companies by name or domain query, semantic query, industry (NAICS), location, size, revenue, founded year, funding, keywords, technologies and workforce filters, with page-based pagination (at most 100 per page, page * pageSize up to 10,000; use Scroll Companies beyond that). Costs 1 credit per company returned, minimum 1 credit.
* **Search Countries** `searchCountries`: Searches countries by name and returns up to 100 per page with their ISO codes and coordinates.
* **Search People** `searchPeople`: Searches people by company domains or company filters, job position queries, seniority, department, country, tenure dates and education, with page-based pagination (at most 100 per page, page * pageSize up to 10,000; use Scroll People beyond that). Costs 2 credits per person returned, minimum 2 credits.
* **Search States** `searchStates`: Searches states and provinces by name or country codes and returns up to 100 per page with the ids used in the states filter of company searches.
* **Update Company List** `updateCompanyList`: Renames a saved company list. Requires a plan with the 'lists' capability; other plans receive a 403.

</details>
