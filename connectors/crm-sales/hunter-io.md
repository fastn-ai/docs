---
description: "Hunter.io helps you find and verify professional email addresses, search all the emails associated with a domain, verify deliverability, enrich people and…"
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

| Action | Slug | What it does |
| --- | --- | --- |
| Create Lead | `createLead` | Create a new lead with contact and company details, optionally assigning it to a leads list. |
| Create Leads List | `createLeadsList` | Create a new leads list to organize leads into folders/campaigns. |
| Delete Lead | `deleteLead` | Permanently delete a lead by its id. Returns no content on success. |
| Delete Leads List | `deleteLeadsList` | Permanently delete a leads list by its id. Returns no content on success. |
| Discover Companies | `discoverCompanies` | Search Hunter's company database using natural language or structured filters (industry, headcount, location, technology, keywords) to find companies matching your ideal customer profile. Consumes credits per call. |
| Enrich Company | `enrichCompany` | Retrieve firmographic data Hunter has about a company from its domain - name, industry, description, size, funding, tech stack, and location. Consumes one credit per call. |
| Enrich Person | `enrichPerson` | Retrieve all the data Hunter has about a person from their email address or LinkedIn profile - name, location, timezone, employment, and social handles. Consumes one credit per call. |
| Enrich Person And Company | `enrichCombined` | Retrieve both person data and company data in one call from a single email address. Consumes one credit per call. |
| Find Company Domain | `findCompanyDomain` | Resolve a company name to its most likely domain name(s), each with a logo and known email count. Free - does not consume any credits. |
| Find Email | `findEmail` | Find the most likely email address for a specific person at a company, given their name and the company's domain or name. Consumes one search credit per call. |

<details>

<summary>See 12 more actions</summary>

* **Get Account Info** `getAccountInfo`: Retrieve the connected Hunter.io account's profile, plan, and remaining monthly credits (search credits, email searches, and verifications). Does not consume any credits.
* **Get Campaign** `getCampaign`: Retrieve a single email outreach campaign (sequence) by its id.
* **Get Email Count** `getEmailCount`: Get the number of email addresses Hunter has for a given domain or company name, broken down by personal/generic type, department, and seniority. Free - does not consume any credits.
* **Get Lead** `getLead`: Retrieve a single lead by its id.
* **Get Leads List** `getLeadsList`: Retrieve a single leads list by its id, including its nested (paginated) leads.
* **List Campaigns** `listCampaigns`: Retrieve all email outreach campaigns (sequences) in the account.
* **List Leads** `listLeads`: Retrieve leads, optionally filtered by leads list, verification status, sending status, or a free-text search on name/email.
* **List Leads Lists** `listLeadsLists`: Retrieve all leads lists in the account.
* **Search Domain** `searchDomain`: Search all email addresses Hunter has found for a domain or company, with names, positions, departments, seniority, and verification status. Consumes one search credit per call.
* **Update Lead** `updateLead`: Update fields on an existing lead, such as name, position, company, or contact details. Returns no content on success.
* **Update Leads List** `updateLeadsList`: Rename a leads list or move it into a different folder. Returns no content on success.
* **Verify Email** `verifyEmail`: Verify whether an email address is valid and deliverable, checking syntax, MX records, SMTP, and disposable/webmail status. Consumes one email verification credit per call (separate pool from search credits).

</details>
