---
description: "Connect Hunter.io to your product with fastn."
hidden: true
---

# Hunter.io

<img src="../../.gitbook/assets/connectors/lg/hunter-io.png" alt="Hunter.io logo">

Hunter.io helps you find and verify professional email addresses, search all the emails associated with a domain, verify deliverability, enrich people and companies with firmographic data, discover companies matching criteria, and manage leads, leads lists, and outreach campaigns.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [hunter.io](https://hunter.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `hunterIo` |

## Use it

Add Hunter.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.hunterIo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Lead</td><td><code>createLead</code></td><td>Create a new lead with contact and company details, optionally assigning it to a leads list.</td></tr><tr><td>Create Leads List</td><td><code>createLeadsList</code></td><td>Create a new leads list to organize leads into folders/campaigns.</td></tr><tr><td>Delete Lead</td><td><code>deleteLead</code></td><td>Permanently delete a lead by its id. Returns no content on success.</td></tr><tr><td>Delete Leads List</td><td><code>deleteLeadsList</code></td><td>Permanently delete a leads list by its id. Returns no content on success.</td></tr><tr><td>Discover Companies</td><td><code>discoverCompanies</code></td><td>Search Hunter's company database using natural language or structured filters (industry, headcount, location, technology, keywords) to find companies matching your ideal customer profile. Consumes credits per call.</td></tr><tr><td>Enrich Company</td><td><code>enrichCompany</code></td><td>Retrieve firmographic data Hunter has about a company from its domain - name, industry, description, size, funding, tech stack, and location. Consumes one credit per call.</td></tr><tr><td>Enrich Person</td><td><code>enrichPerson</code></td><td>Retrieve all the data Hunter has about a person from their email address or LinkedIn profile - name, location, timezone, employment, and social handles. Consumes one credit per call.</td></tr><tr><td>Enrich Person And Company</td><td><code>enrichCombined</code></td><td>Retrieve both person data and company data in one call from a single email address. Consumes one credit per call.</td></tr><tr><td>Find Company Domain</td><td><code>findCompanyDomain</code></td><td>Resolve a company name to its most likely domain name(s), each with a logo and known email count. Free - does not consume any credits.</td></tr><tr><td>Find Email</td><td><code>findEmail</code></td><td>Find the most likely email address for a specific person at a company, given their name and the company's domain or name. Consumes one search credit per call.</td></tr></tbody></table>

<details>

<summary>View 12 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Account Info</td><td><code>getAccountInfo</code></td><td>Retrieve the connected Hunter.io account's profile, plan, and remaining monthly credits (search credits, email searches, and verifications). Does not consume any credits.</td></tr><tr><td>Get Campaign</td><td><code>getCampaign</code></td><td>Retrieve a single email outreach campaign (sequence) by its id.</td></tr><tr><td>Get Email Count</td><td><code>getEmailCount</code></td><td>Get the number of email addresses Hunter has for a given domain or company name, broken down by personal/generic type, department, and seniority. Free - does not consume any credits.</td></tr><tr><td>Get Lead</td><td><code>getLead</code></td><td>Retrieve a single lead by its id.</td></tr><tr><td>Get Leads List</td><td><code>getLeadsList</code></td><td>Retrieve a single leads list by its id, including its nested (paginated) leads.</td></tr><tr><td>List Campaigns</td><td><code>listCampaigns</code></td><td>Retrieve all email outreach campaigns (sequences) in the account.</td></tr><tr><td>List Leads</td><td><code>listLeads</code></td><td>Retrieve leads, optionally filtered by leads list, verification status, sending status, or a free-text search on name/email.</td></tr><tr><td>List Leads Lists</td><td><code>listLeadsLists</code></td><td>Retrieve all leads lists in the account.</td></tr><tr><td>Search Domain</td><td><code>searchDomain</code></td><td>Search all email addresses Hunter has found for a domain or company, with names, positions, departments, seniority, and verification status. Consumes one search credit per call.</td></tr><tr><td>Update Lead</td><td><code>updateLead</code></td><td>Update fields on an existing lead, such as name, position, company, or contact details. Returns no content on success.</td></tr><tr><td>Update Leads List</td><td><code>updateLeadsList</code></td><td>Rename a leads list or move it into a different folder. Returns no content on success.</td></tr><tr><td>Verify Email</td><td><code>verifyEmail</code></td><td>Verify whether an email address is valid and deliverable, checking syntax, MX records, SMTP, and disposable/webmail status. Consumes one email verification credit per call (separate pool from search credits).</td></tr></tbody></table>

</details>
