---
description: "Prospeo B2B contact data API."
hidden: true
---

# Prospeo

<img src="../../.gitbook/assets/connectors/lg/prospeo.png" alt="Prospeo logo">

Prospeo B2B contact data API. Enrich people and companies with verified emails, mobile numbers and firmographic data, search a database of 200M+ contacts and 30M+ companies with 30+ filters, resolve filter values via search suggestions, and monitor credit usage. Every enrichment or search call consumes account credits.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [prospeo.io](https://prospeo.io) |
| **Authentication** | API key |
| **Slug** | `prospeo` |

## Use it

Add Prospeo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.prospeo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Enrich Companies | `bulkEnrichCompany` | Enrich up to 50 companies in a single synchronous request. Each entry needs your own identifier plus at least one of company_website, company_linkedin_url, company_name or company_id. Results are split into matched, not_matched and invalid_datapoints, with total_cost reporting the credits actually spent. COST: 1 credit per matched company; nothing is charged when no result is found. |
| Bulk Enrich People | `bulkEnrichPerson` | Enrich up to 50 people in a single synchronous request. Each entry needs your own identifier plus one valid matching combination (first_name + last_name + company identifier, full_name + company identifier, linkedin_url, email, or person_id). Results are split into matched, not_matched and invalid_datapoints, with total_cost reporting the credits actually spent. COST: same model as Enrich Person — 1 credit per email found, 10 per mobile found when enrich_mobile is true, nothing for misses or records re-enriched within 90 days. Returns real individuals' contact details. |
| Enrich Company | `enrichCompany` | Enrich a single company from its website domain, LinkedIn page, name or Prospeo company_id, returning firmographics, description, industry, headcount, location, funding, technology stack and job postings. COST: 1 credit per matched company; no charge when nothing is found or when the same record was enriched within the last 90 days ("free_enrichment": true). |
| Enrich Person | `enrichPerson` | Enrich a single person with a verified business email, optional mobile number and full professional profile plus their company. Supply at least one identifying combination: first_name + last_name + a company identifier, full_name + a company identifier, linkedin_url, email, or a person_id from Search People. COST: 1 credit per email found, or 10 credits when enrich_mobile is true and a mobile is found (the email is then included). No charge when nothing is found or when the same record was enriched within the last 90 days ("free_enrichment": true). Returns a real individual's contact details — handle the response under your data-protection obligations. |
| Get Account Information | `getAccountInformation` | Retrieve the Prospeo account's current plan, remaining and used credits, team member count and the date of the next quota renewal. Free — consumes no credits. Use it before any enrichment or search call to check the remaining credit balance. |
| Get Search Suggestions | `getSearchSuggestions` | Look up the exact filter values accepted by Search People and Search Companies — locations, job titles, technologies, industries, NAICS and SIC codes, integrations, awards, investors and ICP attributes. Supply exactly one search parameter of at least 2 characters. Free: consumes no credits. Rate limited to 15 requests per second. |
| Search Companies | `searchCompany` | Search Prospeo's database of 30M+ companies using firmographic, technographic, funding, hiring, traffic and ICP filters. Returns up to 25 companies per page. Costs 1 credit per request that returns at least one company; identical result sets repeated within 30 days are free and flagged with "free": true. |
| Search People | `searchPerson` | Search Prospeo's database of 200M+ B2B contacts using person and company filters. Returns up to 25 people per page with their company, with email and mobile fields masked — pass a returned person_id to Enrich Person to reveal contact details. Costs 1 credit per request that returns at least one person; identical result sets repeated within 30 days are free and flagged with "free": true. |
