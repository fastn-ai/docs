---
description: "RocketReach finds emails, phone numbers and social profiles for professionals. Look up and search people and companies, one at a time or in bulk."
hidden: true
---

# RocketReach

<img src="../../.gitbook/assets/connectors/lg/rocketreach.png" alt="RocketReach logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [rocketreach.co](https://rocketreach.co) |
| **Authentication** | API key |
| **Slug** | `rocketreach` |

## Setup

Your customers enter their API key for RocketReach when they connect. Nothing else needs setting up.

## Use it

Add RocketReach from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rocketreach.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Bulk People Lookup API</td><td><code>bulkLookupPeople</code></td><td>Bulk People Lookup API. Bulk People Lookup by Criteria</td></tr><tr><td>Company Lookup API</td><td><code>lookupCompany</code></td><td>Company Lookup API. Search Companies by Criteria</td></tr><tr><td>Company Search API</td><td><code>searchCompanies</code></td><td>Company Search API. Search Companies by Criteria</td></tr><tr><td>Email Verify API</td><td><code>verifyEmail</code></td><td>Email Verify API. Verify whether one email address can receive mail. Charges one email verification credit, refunded when the result is `unknown` or the email is incorrectly formatted.</td></tr><tr><td>Look Up Person</td><td><code>lookupPerson</code></td><td>People Lookup API. Person Enrichment API</td></tr><tr><td>People and Company Lookup API</td><td><code>lookupPersonAndCompany</code></td><td>People and Company Lookup API. Person and Company Lookup</td></tr><tr><td>People Lookup Status API</td><td><code>checkPersonLookupStatus</code></td><td>People Lookup Status API. Check Person Lookup Status</td></tr><tr><td>People Search API</td><td><code>searchPeople</code></td><td>People Search API. Search People by Criteria</td></tr><tr><td>Retrieve Account</td><td><code>getAccount</code></td><td>RocketReach API Account. Retrieve &amp; Manage Account Details</td></tr><tr><td>⭐ RocketReach Universal API Account</td><td><code>getUniversalAccount</code></td><td>⭐ RocketReach Universal API Account. Retrieve &amp; Manage Account Details</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>⭐ Universal Bulk People Lookup API</td><td><code>bulkLookupPeopleUniversal</code></td><td>⭐ Universal Bulk People Lookup API. Bulk People Lookup by Criteria</td></tr><tr><td>⭐ Universal Company Lookup API</td><td><code>lookupCompanyUniversal</code></td><td>⭐ Universal Company Lookup API. Search Companies by Criteria</td></tr><tr><td>⭐ Universal Company Search API</td><td><code>searchCompaniesUniversal</code></td><td>⭐ Universal Company Search API. Search Companies by Criteria</td></tr><tr><td>⭐ Universal People Lookup API</td><td><code>lookupPersonUniversal</code></td><td>⭐ Universal People Lookup API. Person Enrichment API</td></tr><tr><td>⭐ Universal People Lookup Status API</td><td><code>checkPersonLookupStatusUniversal</code></td><td>⭐ Universal People Lookup Status API. Check Universal Person Lookup Status</td></tr><tr><td>⭐ Universal People Search API</td><td><code>searchPeopleUniversal</code></td><td>⭐ Universal People Search API. Search People by Criteria</td></tr></tbody></table>

</details>

## Events

RocketReach has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
