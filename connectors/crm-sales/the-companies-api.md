---
description: "The Companies API is a company data and enrichment platform."
hidden: true
---

# The Companies API

<img src="../../.gitbook/assets/connectors/lg/the-companies-api.png" alt="The Companies API logo">

The Companies API is a company data and enrichment platform. This connector covers the full v2 REST surface: company search by segmentation query, name, natural-language prompt or similarity; company enrichment from a domain, an email address or a social network URL; company context, email patterns and AI question answering; analytics and analytics exports; reference data for industries, technologies, cities, counties, states, countries and continents; job title enrichment; company list management and membership; background enrichment jobs (actions); saved prompts and prompt-to-segmentation conversion; and team and user account information.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [thecompaniesapi.com](https://thecompaniesapi.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `theCompaniesApi` |

## Use it

Add The Companies API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.theCompaniesApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Ask Company | `askCompany` | Asks an AI model a free-form question about a company and returns a grounded answer drawn from the pages the platform has crawled for that domain. Supply Fields to receive the answer as typed, structured values instead of prose. Known platform issue as of 2026-09-12: this endpoint returns HTTP 500 'Maximum call stack size exceeded' for every company that exists, while an unknown domain correctly returns 404, so the fault is in the vendor's answer generation rather than in the request. Use Run Product Prompt with an 'ask-list' job as a working alternative until the vendor resolves it. |
| Convert Prompt To Segmentation | `promptToSegmentation` | Turns a plain-English audience description such as 'fintech companies in Europe with more than 200 employees' into a structured segmentation query. Feed the returned conditions straight into Search Companies, Count Companies or Create List. |
| Count Companies | `countCompanies` | Returns the number of companies in the database matching a segmentation query or a free-text search, without returning the company records themselves. Use it to size an audience before running a paid search or an enrichment job. |
| Count Companies By Segmentation Body | `countCompaniesPost` | Returns the number of companies matching a segmentation query sent in the request body. Use this variant instead of Count Companies when the query has many conditions or long values that would exceed a practical query-string length. |
| Create List | `createList` | Creates a company list. A list can be left empty and filled later, populated from a segmentation query, or seeded from a set of similar domains. Mark it dynamic to have the platform keep re-running the query so the membership stays current. |
| Create Team Webhook | `createTeamWebhook` | Registers a webhook endpoint on a team so The Companies API can post payloads to your own URL when activity happens on the company lists attached to it, for example when companies are added to a list or an enrichment job finishes. Attach lists afterwards with Update Team Webhook. This route is not part of the published OpenAPI document but is live on the v2 API and backs the Webhooks page in the settings. |
| Delete List | `deleteList` | Permanently deletes a company list and its membership. The companies themselves are not affected, only the list that grouped them. This cannot be undone. |
| Delete Prompt | `deletePrompt` | Permanently deletes a saved prompt from your team history, which also clears the cached response the platform would otherwise reuse for the same text. |
| Delete Team Webhook | `deleteTeamWebhook` | Removes a webhook endpoint from a team so it stops receiving payloads, and returns the deleted webhook. This route is not part of the published OpenAPI document but is live on the v2 API and backs the Webhooks page in The Companies API settings. |
| Enrich Company From Email | `fetchCompanyByEmail` | Identifies the company behind a work email address and returns its full record, alongside the parsed parts of the email and whether the address uses a free provider. Use it to enrich a sign-up the moment a user submits their email. |

<details>

<summary>See 39 more actions</summary>

* **Enrich Company From Social Profile** `fetchCompanyBySocial`: Resolves a company from one of its social network profiles and returns its full company record. Supply the full profile URL for whichever network you hold, most commonly LinkedIn. Provide exactly one network per call. A profile the platform cannot match returns HTTP 404 with the message 'companyNotFound'.
* **Enrich Job Title** `enrichJobTitles`: Normalises a raw job title and classifies it into a department and a seniority level, with Spanish and French variants. Use it to standardise job titles collected from sign-up forms or imported contact records before routing or scoring them. A title the platform does not recognise returns HTTP 404 with the message 'jobTitleNotFound'.
* **Export Companies Analytics** `exportCompaniesAnalytics`: Exports the analytics breakdown of a segmentation query or a company list across several attributes at once, in the file format you choose. Use it to produce a market-sizing report covering industry, headcount, revenue and location in a single call.
* **Fetch API Health** `fetchApiHealth`: Retrieves the current health status of The Companies API, including the node serving the request and a per-subsystem health report. Useful as a lightweight availability check before running a batch of enrichment calls.
* **Fetch Companies Analytics** `fetchCompaniesAnalytics`: Breaks a segmentation query or a company list down by a single attribute and returns the count of companies in each bucket. Use it to profile an audience by industry, headcount, revenue, country, technology or any other supported attribute.
* **Fetch Company By Domain** `fetchCompany`: Enriches a single company from its website domain and returns the full company record, including firmographics, industries, headquarters location, social profiles, detected technologies, contact points and key URLs. Consumes enrichment credits.
* **Fetch Company Context** `fetchCompanyContext`: Returns the full crawled context behind a company record: the company record itself, a set of categorised facts the platform has aggregated about the business, and the source pages with their extracted text and links. Use it to ground your own AI prompts in what the platform actually read about the company. A domain the platform has never crawled returns HTTP 404 with the message 'companyNotFound'.
* **Fetch Company Email Patterns** `fetchCompanyEmailPatterns`: Returns the email address patterns observed for a company, such as first.last or first initial plus last name, each with how often it is used. Combine a pattern with a person's name to construct a likely work email address.
* **Fetch Company In List** `fetchCompanyInList`: Returns a single company from a saved list by its domain, including the enrichment fields any AI job has written onto that list membership. Use it to check whether a specific company is in a list and read its list-scoped data.
* **Fetch OpenAPI Specification** `fetchOpenApi`: Retrieves the current OpenAPI 3.1 specification of The Companies API, describing every available path, parameter and schema. Use it to discover newly released endpoints or to generate a client. The document is large, so expect a multi-hundred-kilobyte response.
* **Fetch Team** `fetchTeam`: Retrieves a team, including its remaining enrichment credits, credit pack size, subscription state and the role the authenticated user holds in it. Use it to check the credit balance before launching a large enrichment run.
* **Get Current User** `fetchUser`: Retrieves the profile of the user that owns the API token, including the email address, verification state, display preferences and the identifier of the team the requests are billed to.
* **List Team Webhooks** `fetchTeamWebhooks`: Lists the webhook endpoints registered on a team, including the destination URL, the payload format and the company lists each webhook is attached to. This route is not part of the published OpenAPI document but is live on the v2 API and backs the Webhooks page in The Companies API settings.
* **Request Action** `requestAction`: Queues a background job or estimates its cost before running it. Use it to enrich a set of companies or a whole list with AI-extracted fields, to answer a question about a domain or a list, or to clean up a list. Set Estimate to true to receive the credit cost without queueing anything.
* **Retry Action** `retryAction`: Requeues a background job that previously failed, so the platform attempts it again with the same payload. Only actions belonging to your own team and in a retryable type can be retried.
* **Run Product Prompt** `productPrompt`: Sends a natural-language prompt to the platform assistant and returns its answer along with the saved prompt record. The assistant answers in the context you specify, so it can explain the product, interpret a list or reason about a company. Repeated prompts are served from cache unless Force is set.
* **Search Actions** `fetchActions`: Lists and filters the background jobs (actions) requested by your team, such as company enrichment runs, list clean-ups and AI question jobs. Supports filtering by status, type, list, team, free-text search and explicit identifiers, and returns pagination metadata.
* **Search Cities** `searchCities`: Searches the city reference data the platform uses for company headquarters, returning each city with its code, coordinates and its parent county, state, country and continent. Use the returned codes as values for the 'locations.headquarters.city.code' segmentation attribute.
* **Search Companies** `searchCompanies`: Searches the company database using a segmentation query and returns the matching company records with pagination metadata. Combine conditions on industry, headcount, revenue, location, technologies, social presence and more to build a target audience. Consumes credits per result page.
* **Search Companies By Name** `searchCompaniesByName`: Resolves a company name to matching company records, ranked by relevance. Use it to power a company autocomplete field or to attach a domain to a name captured on a form, optionally narrowing the candidates to given countries.
* **Search Companies By Prompt** `searchCompaniesByPrompt`: Finds companies from a plain-English description of the audience, such as 'European fintech startups using Stripe'. The platform interprets the prompt semantically and returns the closest matching companies, so no segmentation query has to be written by hand.
* **Search Companies By Segmentation Body** `searchCompaniesPost`: Searches the company database using a segmentation query sent in the request body, returning the matching company records with pagination metadata. Use this variant instead of Search Companies when the query has many conditions or long values that would exceed a practical query-string length.
* **Search Companies In List** `fetchCompaniesInList`: Returns the companies held in a saved list, optionally narrowed further by a segmentation query and sorted. Use it to page through a list you built earlier and export or sync its members.
* **Search Companies In List By Segmentation Body** `fetchCompaniesInListPost`: Returns the companies held in a saved list, narrowed by a segmentation query sent in the request body. Use this variant instead of Search Companies In List when the query has many conditions or long values that would exceed a practical query-string length.
* **Search Continents** `searchContinents`: Searches the continent reference data the platform uses for company headquarters, returning each continent with its code, localised names and coordinates. Use the returned codes as values for the 'locations.headquarters.continent.code' segmentation attribute.
* **Search Counties** `searchCounties`: Searches the county reference data the platform uses for company headquarters, returning each county with its code, coordinates and its parent state, country and continent. Use the returned codes as values for the 'locations.headquarters.county.code' segmentation attribute.
* **Search Countries** `searchCountries`: Searches the country reference data the platform uses for company headquarters, returning each country with its code, localised names, population, coordinates and its continent. Use the returned codes as values for the 'locations.headquarters.country.code' segmentation attribute.
* **Search Industries** `searchIndustries`: Searches the industry taxonomy used by the platform and returns each matching industry with its slug and the number of companies classified under it. Use the returned slugs as values for the 'about.industry' and 'about.industries' segmentation attributes.
* **Search Lists** `fetchLists`: Lists the company lists owned by your team, including their segmentation query, whether they refresh dynamically, their processing state and their company counts.
* **Search Prompts** `fetchPrompts`: Lists the natural-language prompts previously submitted by your team, together with the segmentation or answer each one resolved to. Filter by the product area the prompt came from, the feature it drove, the model used, or the list or company it targeted.
* **Search Similar Companies** `searchSimilarCompanies`: Finds companies that look like one or more seed companies, ranked by similarity and annotated with the attributes they share. Use it to build lookalike audiences from your best customers. Tune how close the matches must be with Proximity Term or Proximity Exact.
* **Search Similar Industries** `searchIndustriesSimilar`: Finds the industries most closely related to one or more seed industries, ranked by semantic similarity. Use it to widen a segmentation beyond a single industry slug without listing every variant by hand.
* **Search States** `searchStates`: Searches the state and region reference data the platform uses for company headquarters, returning each state with its code, coordinates and its parent country and continent. Use the returned codes as values for the 'locations.headquarters.state.code' segmentation attribute.
* **Search Technologies** `searchTechnologies`: Searches the catalogue of web technologies the platform detects on company websites, returning each technology with its slug, vendor, categories and adoption counts. Use the returned slugs as values for the 'technologies.active' segmentation attribute.
* **Send Team Webhook Test Event** `sendTeamWebhookTestEvent`: Sends a sample 'companies:added' event to a team webhook endpoint so you can confirm the destination URL receives and parses deliveries. The sample payload describes a placeholder list with example companies. This route is not part of the published OpenAPI document but is live on the v2 API and backs the 'Send a test event' button in The Companies API settings.
* **Toggle Companies In List** `toggleCompaniesInList`: Adds companies to a list or removes them from it. Identify the companies either by their website domains or by their numeric company identifiers, and set Action to 'attach' to add them or 'detach' to remove them.
* **Update List** `updateList`: Updates a company list. Only the fields you supply are changed, so you can rename a list, change its segmentation query, switch it between dynamic and static, adjust its company cap or digest frequency, mark it as seen, or trigger a resynchronisation.
* **Update Team** `updateTeam`: Updates the profile of a team. Only the fields you supply are changed, so you can set the team name, its country or its website independently. Credits and subscription state are managed by billing and cannot be changed here.
* **Update Team Webhook** `updateTeamWebhook`: Updates a webhook endpoint on a team: rename it, change its destination URL or payload format, and attach or detach the company lists whose activity triggers it. A webhook only delivers events for the lists attached to it. This route is not part of the published OpenAPI document but is live on the v2 API and backs the Webhooks page in The Companies API settings. Returns the webhook with its attached lists.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Background Job Completed | `jobs:request` | Delivered when a background job requested with Request Action finishes on a company list the webhook endpoint is attached to. The job carried by the delivery is named in data.job and is one of ask-domain, ask-list, enrich-companies, enrich-list or cleanup-list. |
| Companies Added To List | `companies:added` | Delivered when companies are added to one of the company lists the webhook endpoint is attached to, including the companies themselves and the list they landed in. The webhook must be attached to at least one list - the subscription attaches the list given as List ID, and a webhook attached to no list never receives anything. |
