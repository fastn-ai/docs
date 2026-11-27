---
description: "LeadIQ is a sales prospecting tool. Search people and companies, read prospects and manage prospect lists."
hidden: true
---

# LeadIQ

<img src="../../.gitbook/assets/connectors/lg/leadiq.png" alt="LeadIQ logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [leadiq.com](https://leadiq.com) |
| **Authentication** | Username and password |
| **Slug** | `leadiq` |

## Setup

Your customers enter their username and password for LeadIQ when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect LeadIQ from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **LeadIQ**.
2. Select **Connect** on the LeadIQ card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use LeadIQ's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Prospect To List</td><td><code>addProspectToList</code></td><td>Add a prospect (contact) to an existing prospect list. Provide input.listId and input.prospect (firstName and lastName required). Returns the created prospect.</td></tr><tr><td>Advanced Search - Flat (People)</td><td><code>flatAdvancedSearch</code></td><td>Advanced Search returning a flat list of people matching broad criteria (job title, seniority, role, company name/industry/size/location, etc.). Use companyFilter and contactFilter inside input; set limit to bound results.</td></tr><tr><td>Advanced Search - Grouped (By Company)</td><td><code>groupedAdvancedSearch</code></td><td>Advanced Search returning people grouped by company. Each result is a company with its matching people and total contact count. Use companyFilter/contactFilter inside input; bound with limit and limitPerCompany.</td></tr><tr><td>Create Prospect List</td><td><code>createList</code></td><td>Create a new prospect list. Provide input.name (required) and optional input.description. Returns the created list.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Retrieve the authenticated account's subscription plans and credit usage (DataHub and Universal plans: available/used credits, status, next billing period). No input required.</td></tr><tr><td>Get Contact Tracking Balance</td><td><code>getContactTrackingBalance</code></td><td>Get the current contact-tracking credit balance for the account: total balance, remaining credits, max credits, and plan tier. No input required.</td></tr><tr><td>Get Prospect</td><td><code>getProspect</code></td><td>Fetch a single prospect (a saved contact within a list) by its prospect ID, including contact details, location, and company.</td></tr><tr><td>Get Prospect List</td><td><code>getList</code></td><td>Fetch a single prospect list by ID, including its metadata and the prospects it contains (paginated).</td></tr><tr><td>List Prospect Lists</td><td><code>listLists</code></td><td>List the account's prospect lists (paginated). Returns list metadata and a nextCursor for pagination. limit is required (default 50).</td></tr><tr><td>Search Company</td><td><code>searchCompany</code></td><td>Company Search: find a single company by name, domain, LinkedIn ID or URL. Returns firmographics (industry, size, revenue, location, social URLs). Provide domain, name, linkedinId, or linkedinUrl inside input.</td></tr></tbody></table>

<details>

<summary>View 3 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search People (Contact Search)</td><td><code>searchPeople</code></td><td>Contact Search: find one person and reveal verified work/personal emails and phones by name+company, LinkedIn URL/ID, email, or phone. Consumes a credit when contact info is returned. Provide firstName+lastName+company OR linkedinUrl OR email inside input.</td></tr><tr><td>Search People Preview</td><td><code>searchPeoplePreview</code></td><td>Preview whether a person has an available email/phone in LeadIQ WITHOUT spending a credit. Returns personId and hasEmail/hasPhone booleans. Provide fullName+companyName, or linkedinUrl, or email inside input.</td></tr><tr><td>Submit Person Feedback</td><td><code>submitPersonFeedback</code></td><td>Submit a correction/feedback on a person's contact info (mark an email/phone Correct or Invalid). Provide input.value (the contact value) plus type and status; identify the person via personId or linkedinUrl. Returns a feedback ID.</td></tr></tbody></table>

</details>

