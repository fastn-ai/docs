---
description: "DataForB2B is a B2B data API for searching and enriching people and companies."
hidden: true
---

# DataForB2B

<img src="../../.gitbook/assets/connectors/lg/dataforb2b.png" alt="DataForB2B logo">

DataForB2B is a B2B data API for searching and enriching people and companies. This connector covers the DataForB2B REST API: people, company, job and social post search; natural-language text-to-filters, one-shot and multi-turn reasoning search; result counts and filter typeahead; profile enrichment (full profile, work and personal email, phone, GitHub) and company enrichment; the signal catalog and monitors that push real-time signals such as post engagement to your webhook; and the account credit balance. Authenticates with an API key sent in the api_key header.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [dataforb2b.ai](https://dataforb2b.ai) |
| **Authentication** | API key |
| **Slug** | `dataforb2b` |

## Use it

Add DataForB2B from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dataforb2b.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Monitor Targets | `addMonitorTargets` | Adds values to watch on an existing monitor, such as more author profile URLs, up to 100 per request. The target type is detected automatically. |
| Convert Text To Filters | `convertTextToFilters` | Converts a natural-language query into a structured filter group usable with Search People or Search Companies, optionally with a result count and incremental refinement of a previous query. Charges 1 credit per filter generation. |
| Count Search Results | `countSearchResults` | Counts how many people or companies match a filter group without running the search or returning records. Free; the count is capped at 10,000. |
| Create Monitor | `createMonitor` | Creates a monitor that subscribes to a signal (for example post_engagement) for the watched profiles and delivers events to your HTTPS webhook URL, optionally signed with a secret. Creating a monitor is free; delivered engagers are charged per signal pricing. |
| Delete Monitor | `deleteMonitor` | Deletes a monitor and all of its targets, stopping its deliveries. Returns 404 if the monitor does not exist on the API key. |
| Enrich Company | `enrichCompany` | Enriches a company by LinkedIn universal name, URL, encoded id or Twitter/X handle with general information, size, metrics, locations, funding rounds, investors and growth. Charges 1.5 credits per company. |
| Enrich Profile | `enrichProfile` | Enriches a person by LinkedIn URL, public id, encoded profile id or Twitter/X handle with the data types you select: full profile (1.5 credits), work email (1 credit), personal email (3 credits), phone (10 credits) and GitHub profile (1 credit). Only successful enrichments are charged. |
| Get Account | `getAccount` | Returns whether the API key is valid and the remaining credit balance of the DataForB2B account. Free; used to verify the connection. |
| Get Filter Suggestions | `getFilterSuggestions` | Autocompletes canonical filter values (companies, industries, categories, locations, cities, regions, schools, titles, skills, investors) for use in search filters. Charges 0.01 credit per result returned. |
| List Monitor Events | `listMonitorEvents` | Lists recent events delivered to a monitor, newest first, with limit and offset paging. |

<details>

<summary>See 10 more actions</summary>

* **List Monitors** `listMonitors`: Lists every monitor on the API key with its signal, watched targets, webhook URL, active state and filters.
* **List Signals** `listSignals`: Returns the signal catalog: every signal you can monitor, its allowed target types, whether a target is required and its sub-event types. Free.
* **Remove Monitor Targets** `removeMonitorTargets`: Removes one or more targets from a monitor by their URL or key.
* **Run Reasoning Search** `runReasoningSearch`: Runs the multi-turn AI search agent: send a query, answer any clarifying questions with the returned session id, or refine a previous search. Returns either needs_input questions or complete results. Charges 2 credits per completed search plus 0.75 or 1.5 credits per result.
* **Run Reasoning Search Stream** `runReasoningSearchStream`: Runs the multi-turn AI search agent and streams its progress as server-sent events (thinking, searching, questions and a final result event). Accepts the same inputs as Run Reasoning Search and charges the same credits.
* **Search By Natural Language** `searchByNaturalLanguage`: Runs a one-shot search from a natural-language query: generates the filters and returns matching people or companies in a single call. Charges 1 credit for filter generation plus 0.75 or 1.5 credits per result depending on live enrichment.
* **Search Companies** `searchCompanies`: Searches companies with a structured filter group of column conditions (name, domain, industry, size, headquarters, offices, growth, funding and more). Charges 0.75 credits per result with cached data or 1.5 credits per result with live enrichment.
* **Search Jobs** `searchJobs`: Searches job postings on LinkedIn or Indeed by keyword, location, company, employment type, work arrangement, seniority and freshness, with optional full descriptions. Documented price is 1.5 credits per 10 postings returned; the API requires a balance of 0.75 credits per requested posting before running the search.
* **Search People** `searchPeople`: Searches professional profiles with a structured filter group of column conditions (current company, title, location, skills, education, experience and more). Charges 0.75 credits per result with cached data or 1.5 credits per result with live enrichment. Unknown columns are rejected with 400.
* **Search Social Posts** `searchSocialPosts`: Searches posts on LinkedIn, Twitter/X or Reddit by keyword with author, content-type and freshness filters, optionally attaching the people who reacted or commented, or fetches the engagers of one post by URL. Documented price is 1 credit per 10 posts and per 10 engagers returned; the API requires a balance of 0.75 credits per requested post before running the search.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Founder Signal: AI Lab To Founder | `ai_lab_to_founder` | Market-wide founder signal (founder_move): AI-lab alumnus becomes founder. Envelope documented; data body not published by the vendor. |
| Founder Signal: FAANG Exit | `fang_exit` | Market-wide founder signal (founder_move): FAANG exit. Envelope documented; data body not published by the vendor. |
| Founder Signal: FAANG To Founder | `faang_to_founder` | Market-wide founder signal (founder_move): FAANG alumnus becomes founder. Envelope documented; data body not published by the vendor. |
| Founder Signal: Refounder | `refounder` | Market-wide founder signal (founder_move): a repeat founder starts again. Envelope documented; data body not published by the vendor. |
| Founder Signal: Stealth Join | `stealth_join` | Market-wide founder signal (signal founder_move, no watch target): someone joined a stealth company. Envelope documented; data body not published by the vendor. |
| Founder Signal: Top School Founder | `top_school_founder` | Market-wide founder signal (founder_move): founder from a top school. Envelope documented; data body not published by the vendor. |
| Founder Signal: Unicorn To Founder | `unicorn_to_founder` | Market-wide founder signal (founder_move): unicorn alumnus becomes founder. Envelope documented; data body not published by the vendor. |
| Job Change: Company Changed | `company_changed` | A watched person changed company (signal job_change, listed by GET /signals). Set watch to profile URLs. The vendor documents only the unified envelope for this signal; the data body is not published. |
| Job Change: Hiring Status Changed | `hiring_changed` | A watched person's hiring status changed (signal job_change). Envelope documented; data body not published by the vendor. |
| Job Change: New Company | `new_company` | A watched person joined a new company (signal job_change). Envelope documented; data body not published by the vendor. |

<details>

<summary>See 4 more events</summary>

* **Job Change: Open To Work Changed** `open_to_work_changed`: A watched person's open-to-work status changed (signal job_change). Envelope documented; data body not published by the vendor.
* **Job Change: Position Changed** `position_changed`: A watched person changed title (signal job_change). Envelope documented; data body not published by the vendor.
* **Job Change: Position Ended** `position_ended`: A watched person's position ended (signal job_change). Envelope documented; data body not published by the vendor.
* **Post Engagement** `post_engagement`: New reactors and commenters on a watched author's 10 most recent posts (signal post_engagement). Set the watch input to comma-separated author LinkedIn profile URLs. Usage-based: 0.2 credits per backlog engager, 0.5 per go-forward engager; the monitor pauses when credits run out. Deliveries are signed with X-Webhook-Signature sha256=HMAC-SHA256(secret, raw body) when a secret is set.

</details>
