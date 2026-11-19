---
description: "BetterContact finds verified work emails and phone numbers. Enrich leads and companies and run lead finder searches."
hidden: true
---

# BetterContact

<img src="../../.gitbook/assets/connectors/lg/bettercontact.png" alt="BetterContact logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [bettercontact.rocks](https://bettercontact.rocks) |
| **Authentication** | API key |
| **Slug** | `bettercontact` |

## Setup

Your customers enter their API key for BetterContact when they connect. Nothing else needs setting up.

## Use it

Add BetterContact from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bettercontact.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Lead Enrichment</td><td><code>createLeadEnrichment</code></td><td>Submits between 1 and 100 leads for asynchronous waterfall enrichment of work email, mobile phone number and LinkedIn profile. Returns a request id immediately; retrieve results with Get Lead Enrichment Results or receive them on the webhook URL. Credits are consumed per valid data point found, and submissions are not idempotent.</td></tr><tr><td>Create Lead Finder Search</td><td><code>createLeadFinderSearch</code></td><td>Starts an asynchronous Lead Finder search for new leads using company and people filters. Returns a request id; retrieve leads with Get Lead Finder Search Results or receive them on the webhook URL. The search itself is free; enabling email or phone enrichment consumes credits. At least one filter value is required.</td></tr><tr><td>Enrich Company Profile</td><td><code>enrichCompanyProfile</code></td><td>Synchronously looks up a single company by website domain or LinkedIn page URL and returns its firmographic profile: name, description, industry, type, founding year, headcount, headquarters and keywords. Free; never consumes credits. At least one of company_domain or company_linkedin_url is required; no match</td></tr><tr><td>Enrich Lead Profile</td><td><code>enrichLeadProfile</code></td><td>Synchronously looks up a single person by LinkedIn profile URL, or by first name, last name and company domain, and returns their professional profile and current company. Costs 0.1 credit per profile found and nothing when no profile matches (404). When linkedin_url is present the other fields are ignored.</td></tr><tr><td>Get Account Credits</td><td><code>getAccountCredits</code></td><td>Returns the credit balance and the email of the BetterContact account that owns the API key. The balance is shared across the whole organisation. This call is free and is used to verify the connection.</td></tr><tr><td>Get Lead Enrichment Results</td><td><code>getLeadEnrichmentResults</code></td><td>Retrieves the status and results of a lead enrichment request by its request id. An unknown request id</td></tr><tr><td>Get Lead Finder Search Results</td><td><code>getLeadFinderSearchResults</code></td><td>Retrieves the status and leads of a Lead Finder search by its request id. An unknown request id</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Lead Enriched</td><td><code>enrichment.contact_enriched</code></td><td>Sent once per lead as soon as it is enriched, when Create Lead Enrichment is called with push_contact_individually set to true and this trigger's URL as contact_webhook. The body is a single flat enriched-contact object including request_id. Unsigned and not retried. The payload carries no event-type field, so use a dedicated trigger URL for this event. Docs: https://doc.bettercontact.rocks/api-reference/webhooks</td></tr><tr><td>Lead Enrichment Completed</td><td><code>enrichment.terminated</code></td><td>Sent once when a lead enrichment batch reaches status terminated. BetterContact has no webhook registration API: delivery is enabled per request by passing this trigger's URL as the webhook field of the Create Lead Enrichment action. The body is identical to Get Lead Enrichment Results (id, status, credits_consumed, credits_left, summary, data[]). Unsigned; retried up to 5 times. The payload carries no event-type field, so use a dedicated trigger URL for this event. Docs: https://doc.bettercontact.rocks/api-reference/webhooks</td></tr><tr><td>Lead Finder Search Completed</td><td><code>leadFinder.terminated</code></td><td>Sent once when a Lead Finder search reaches status terminated. Enabled per request by passing this trigger's URL as the webhook field of the Create Lead Finder Search action. The body is identical to Get Lead Finder Search Results (id, status, credits_consumed, credits_left, summary with leads_found/limit/offset, leads[]). Unsigned; retried up to 5 times. The payload carries no event-type field, so use a dedicated trigger URL for this event. Docs: https://doc.bettercontact.rocks/api-reference/webhooks</td></tr></tbody></table>
