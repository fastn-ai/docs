---
description: "LeadIQ sales intelligence — GraphQL API for contact/person search, company search, advanced people search, prospect enrichment, and prospect-list management."
---

# LeadIQ

LeadIQ sales intelligence — GraphQL API for contact/person search, company search, advanced people search, prospect enrichment, and prospect-list management. Single endpoint POST https://api.leadiq.com/graphql.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [leadiq.com](https://leadiq.com) |
| **Authentication** | Basic auth |
| **Actions** | 13 |
| **Events** | 0 |
| **Slug** | `leadiq` |

## Use it

Add LeadIQ from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.leadiq.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Prospect To List | `addProspectToList` | Add a prospect (contact) to an existing prospect list. Provide input.listId and input.prospect (firstName and lastName required). Returns the created prospect. |
| Advanced Search - Flat (People) | `flatAdvancedSearch` | Advanced Search returning a flat list of people matching broad criteria (job title, seniority, role, company name/industry/size/location, etc.). Use companyFilter and contactFilter inside input; set limit to bound results. |
| Advanced Search - Grouped (By Company) | `groupedAdvancedSearch` | Advanced Search returning people grouped by company. Each result is a company with its matching people and total contact count. Use companyFilter/contactFilter inside input; bound with limit and limitPerCompany. |
| Create Prospect List | `createList` | Create a new prospect list. Provide input.name (required) and optional input.description. Returns the created list. |
| Get Account | `getAccount` | Retrieve the authenticated account's subscription plans and credit usage (DataHub and Universal plans: available/used credits, status, next billing period). No input required. |
| Get Contact Tracking Balance | `getContactTrackingBalance` | Get the current contact-tracking credit balance for the account: total balance, remaining credits, max credits, and plan tier. No input required. |
| Get Prospect | `getProspect` | Fetch a single prospect (a saved contact within a list) by its prospect ID, including contact details, location, and company. |
| Get Prospect List | `getList` | Fetch a single prospect list by ID, including its metadata and the prospects it contains (paginated). |
| List Prospect Lists | `listLists` | List the account's prospect lists (paginated). Returns list metadata and a nextCursor for pagination. limit is required (default 50). |
| Search Company | `searchCompany` | Company Search: find a single company by name, domain, LinkedIn ID or URL. Returns firmographics (industry, size, revenue, location, social URLs). Provide domain, name, linkedinId, or linkedinUrl inside input. |
| Search People (Contact Search) | `searchPeople` | Contact Search: find one person and reveal verified work/personal emails and phones by name+company, LinkedIn URL/ID, email, or phone. Consumes a credit when contact info is returned. Provide firstName+lastName+company OR linkedinUrl OR email inside input. |
| Search People Preview | `searchPeoplePreview` | Preview whether a person has an available email/phone in LeadIQ WITHOUT spending a credit. Returns personId and hasEmail/hasPhone booleans. Provide fullName+companyName, or linkedinUrl, or email inside input. |
| Submit Person Feedback | `submitPersonFeedback` | Submit a correction/feedback on a person's contact info (mark an email/phone Correct or Invalid). Provide input.value (the contact value) plus type and status; identify the person via personId or linkedinUrl. Returns a feedback ID. |
