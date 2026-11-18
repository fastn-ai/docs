---
description: "LeadIQ sales intelligence — GraphQL API for contact/person search, company search, advanced people search, prospect enrichment, and prospect-list management."
hidden: true
---

# LeadIQ

<img src="../../.gitbook/assets/connectors/lg/leadiq.png" alt="LeadIQ logo">

LeadIQ sales intelligence — GraphQL API for contact/person search, company search, advanced people search, prospect enrichment, and prospect-list management. Single endpoint POST https://api.leadiq.com/graphql.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [leadiq.com](https://leadiq.com) |
| **Authentication** | Basic auth |
| **Slug** | `leadiq` |

## Use it

Add LeadIQ from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.leadiq.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Prospect To List</td><td><code>addProspectToList</code></td><td>Add a prospect (contact) to an existing prospect list. Provide input.listId and input.prospect (firstName and lastName required). Returns the created prospect.</td></tr><tr><td>Advanced Search - Flat (People)</td><td><code>flatAdvancedSearch</code></td><td>Advanced Search returning a flat list of people matching broad criteria (job title, seniority, role, company name/industry/size/location, etc.). Use companyFilter and contactFilter inside input; set limit to bound results.</td></tr><tr><td>Advanced Search - Grouped (By Company)</td><td><code>groupedAdvancedSearch</code></td><td>Advanced Search returning people grouped by company. Each result is a company with its matching people and total contact count. Use companyFilter/contactFilter inside input; bound with limit and limitPerCompany.</td></tr><tr><td>Create Prospect List</td><td><code>createList</code></td><td>Create a new prospect list. Provide input.name (required) and optional input.description. Returns the created list.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Retrieve the authenticated account's subscription plans and credit usage (DataHub and Universal plans: available/used credits, status, next billing period). No input required.</td></tr><tr><td>Get Contact Tracking Balance</td><td><code>getContactTrackingBalance</code></td><td>Get the current contact-tracking credit balance for the account: total balance, remaining credits, max credits, and plan tier. No input required.</td></tr><tr><td>Get Prospect</td><td><code>getProspect</code></td><td>Fetch a single prospect (a saved contact within a list) by its prospect ID, including contact details, location, and company.</td></tr><tr><td>Get Prospect List</td><td><code>getList</code></td><td>Fetch a single prospect list by ID, including its metadata and the prospects it contains (paginated).</td></tr><tr><td>List Prospect Lists</td><td><code>listLists</code></td><td>List the account's prospect lists (paginated). Returns list metadata and a nextCursor for pagination. limit is required (default 50).</td></tr><tr><td>Search Company</td><td><code>searchCompany</code></td><td>Company Search: find a single company by name, domain, LinkedIn ID or URL. Returns firmographics (industry, size, revenue, location, social URLs). Provide domain, name, linkedinId, or linkedinUrl inside input.</td></tr></tbody></table>

<details>

<summary>View 3 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search People (Contact Search)</td><td><code>searchPeople</code></td><td>Contact Search: find one person and reveal verified work/personal emails and phones by name+company, LinkedIn URL/ID, email, or phone. Consumes a credit when contact info is returned. Provide firstName+lastName+company OR linkedinUrl OR email inside input.</td></tr><tr><td>Search People Preview</td><td><code>searchPeoplePreview</code></td><td>Preview whether a person has an available email/phone in LeadIQ WITHOUT spending a credit. Returns personId and hasEmail/hasPhone booleans. Provide fullName+companyName, or linkedinUrl, or email inside input.</td></tr><tr><td>Submit Person Feedback</td><td><code>submitPersonFeedback</code></td><td>Submit a correction/feedback on a person's contact info (mark an email/phone Correct or Invalid). Provide input.value (the contact value) plus type and status; identify the person via personId or linkedinUrl. Returns a feedback ID.</td></tr></tbody></table>

</details>
