---
description: "BetterContact is a waterfall enrichment platform that finds verified work emails and mobile phone numbers by querying many data providers in sequence."
---

# BetterContact

BetterContact is a waterfall enrichment platform that finds verified work emails and mobile phone numbers by querying many data providers in sequence. This connector wraps the BetterContact REST API v2: asynchronous lead enrichment (email, phone and LinkedIn profile) with result retrieval, Lead Finder people search with result retrieval, synchronous lead and company profile enrichment, and the account credit balance. Results can be pushed to a webhook URL supplied on each asynchronous request. Authenticates with an API key sent in the X-API-Key header.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [bettercontact.rocks](https://bettercontact.rocks) |
| **Authentication** | API key |
| **Actions** | 7 |
| **Events** | 3 |
| **Slug** | `bettercontact` |

## Use it

Add BetterContact from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bettercontact.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Lead Enrichment | `createLeadEnrichment` | Submits between 1 and 100 leads for asynchronous waterfall enrichment of work email, mobile phone number and LinkedIn profile. Returns a request id immediately; retrieve results with Get Lead Enrichment Results or receive them on the webhook URL. Credits are consumed per valid data point found, and submissions are not idempotent. |
| Create Lead Finder Search | `createLeadFinderSearch` | Starts an asynchronous Lead Finder search for new leads using company and people filters. Returns a request id; retrieve leads with Get Lead Finder Search Results or receive them on the webhook URL. The search itself is free; enabling email or phone enrichment consumes credits. At least one filter value is required. |
| Enrich Company Profile | `enrichCompanyProfile` | Synchronously looks up a single company by website domain or LinkedIn page URL and returns its firmographic profile: name, description, industry, type, founding year, headcount, headquarters and keywords. Free; never consumes credits. At least one of company_domain or company_linkedin_url is required; no match returns 404. |
| Enrich Lead Profile | `enrichLeadProfile` | Synchronously looks up a single person by LinkedIn profile URL, or by first name, last name and company domain, and returns their professional profile and current company. Costs 0.1 credit per profile found and nothing when no profile matches (404). When linkedin_url is present the other fields are ignored. |
| Get Account Credits | `getAccountCredits` | Returns the credit balance and the email of the BetterContact account that owns the API key. The balance is shared across the whole organisation. This call is free and is used to verify the connection. |
| Get Lead Enrichment Results | `getLeadEnrichmentResults` | Retrieves the status and results of a lead enrichment request by its request id. While the request is running the API answers 202 with status processing and no data; results, summary and credit usage are present only once status is terminated. An unknown request id returns 406. |
| Get Lead Finder Search Results | `getLeadFinderSearchResults` | Retrieves the status and leads of a Lead Finder search by its request id. While the search is running the API answers 202 with status processing and no leads; leads and summary are present once status is terminated. An unknown request id returns 404. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Lead Enriched | `enrichment.contact_enriched` | Sent once per lead as soon as it is enriched, when Create Lead Enrichment is called with push_contact_individually set to true and this trigger's URL as contact_webhook. The body is a single flat enriched-contact object including request_id. Unsigned and not retried. The payload carries no event-type field, so use a dedicated trigger URL for this event. Docs: https://doc.bettercontact.rocks/api-reference/webhooks |
| Lead Enrichment Completed | `enrichment.terminated` | Sent once when a lead enrichment batch reaches status terminated. BetterContact has no webhook registration API: delivery is enabled per request by passing this trigger's URL as the webhook field of the Create Lead Enrichment action. The body is identical to Get Lead Enrichment Results (id, status, credits_consumed, credits_left, summary, data[]). Unsigned; retried up to 5 times. The payload carries no event-type field, so use a dedicated trigger URL for this event. Docs: https://doc.bettercontact.rocks/api-reference/webhooks |
| Lead Finder Search Completed | `leadFinder.terminated` | Sent once when a Lead Finder search reaches status terminated. Enabled per request by passing this trigger's URL as the webhook field of the Create Lead Finder Search action. The body is identical to Get Lead Finder Search Results (id, status, credits_consumed, credits_left, summary with leads_found/limit/offset, leads[]). Unsigned; retried up to 5 times. The payload carries no event-type field, so use a dedicated trigger URL for this event. Docs: https://doc.bettercontact.rocks/api-reference/webhooks |
