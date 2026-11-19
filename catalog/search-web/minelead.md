---
description: "Minelead finds company and professional email addresses. Find and enrich emails, generate leads and manage lead lists."
hidden: true
---

# Minelead

<img src="../../.gitbook/assets/connectors/lg/minelead.png" alt="Minelead logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [minelead.io](https://minelead.io) |
| **Authentication** | API key |
| **Slug** | `minelead` |

## Setup

Your customers enter their API key for Minelead when they connect. Nothing else needs setting up.

## Use it

Add Minelead from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.minelead.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Leads</td><td><code>addLeads</code></td><td>Adds one or more leads to your Minelead leads list. Each lead requires an email address and can include a first name, last name and company.</td></tr><tr><td>Create Recipient List</td><td><code>createRecipientList</code></td><td>Creates a new campaign recipient list with a name and an initial set of recipient email addresses.</td></tr><tr><td>Delete Leads</td><td><code>deleteLeads</code></td><td>Deletes one or more leads from your Minelead leads list, matched by email address.</td></tr><tr><td>Detect Disposable Email</td><td><code>detectDisposableEmail</code></td><td>Checks whether an email address comes from a disposable or temporary email provider, returning a disposability score, domain type and A, PTR and MX record status.</td></tr><tr><td>Enrich Email</td><td><code>enrichEmail</code></td><td>Enriches a single email address with professional profile data such as full name, job title, location, gender, industry and a short summary. Providing the person's name and company improves accuracy. Consumes Minelead credits.</td></tr><tr><td>Find Email</td><td><code>findEmail</code></td><td>Finds a person's professional email address from their first name, last name and company domain. Consumes Minelead credits.</td></tr><tr><td>Find Emails From Social Profile</td><td><code>findSocialEmails</code></td><td>Finds verified professional emails from a YouTube channel or Twitter/X profile URL, grouped by the domains linked to that profile. Consumes Minelead credits.</td></tr><tr><td>Generate Leads From Tags</td><td><code>generateLeadsFromTags</code></td><td>Generates a list of company domains matching keyword tags such as an industry and a location (for example "hotel" and "new york"). On the Free plan part of the returned domains are masked. Consumes Minelead credits.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Retrieves the authenticated Minelead account's details, including email, username, subscription plan, remaining lead credits and recipient lists. Useful for verifying that the API key is valid.</td></tr><tr><td>Get Buying Intent</td><td><code>getBuyingIntent</code></td><td>Analyzes a company's buying intent by scanning news, job postings, company website and LinkedIn signals. Returns an intent score from 0 to 100, an intent level, categorised signals with evidence, a recommended pitch angle and suggested solutions. Each call costs 5 Minelead credits; accounts with fewer credits receive HTTP 402 "Insufficient credits".</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Campaigns</td><td><code>listCampaigns</code></td><td>Lists the email campaigns in your Minelead account with their status flags (active, paused, archived, completed, running).</td></tr><tr><td>List Leads</td><td><code>listLeads</code></td><td>Lists all leads saved to your Minelead account with their id, name, company, email and verification details. Returns status "not-found" when the account has no saved leads.</td></tr><tr><td>List Recipient Lists</td><td><code>listRecipientLists</code></td><td>Lists the campaign recipient lists in your Minelead account, including each list's name, recipient count and recipient emails.</td></tr><tr><td>List Search History</td><td><code>listSearchHistory</code></td><td>Lists your Minelead search history with the date, result status and query of each search, paginated with a start offset and a limit.</td></tr><tr><td>Search Company Emails</td><td><code>searchCompanyEmails</code></td><td>Searches for email addresses belonging to a company by domain (or by company name when no domain is known). Optionally limits the number of results, prioritises generic role-based emails, enriches emails with professional profile data, or runs an AI Deep Search for employee emails. Consumes Minelead credits; the Free plan allows 2 search requests per minute.</td></tr><tr><td>Update Leads</td><td><code>updateLeads</code></td><td>Updates the first name, last name or company of one or more existing leads in your Minelead leads list, matched by email address.</td></tr><tr><td>Update Recipient List</td><td><code>updateRecipientList</code></td><td>Adds emails to or removes emails from an existing campaign recipient list.</td></tr><tr><td>Validate Email</td><td><code>validateEmail</code></td><td>Checks the validity and deliverability of an email address: format, webmail, MX record and mailbox existence, and whether it belongs to a disposable email provider. Consumes Minelead credits.</td></tr></tbody></table>

</details>

## Events

Minelead has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
