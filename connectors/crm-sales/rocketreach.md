---
description: "RocketReach is a contact-data and sales-intelligence platform covering emails, phone numbers and social profiles for 700M+ professionals and 35M+ companies."
hidden: true
---

# RocketReach

<img src="../../.gitbook/assets/connectors/lg/rocketreach.png" alt="RocketReach logo">

RocketReach is a contact-data and sales-intelligence platform covering emails, phone numbers and social profiles for 700M+ professionals and 35M+ companies. This connector wraps the RocketReach API v2 at https://api.rocketreach.co/api/v2: account details and API key management, people lookup with asynchronous status polling, people and company search, company lookup, combined person-and-company lookup, bulk people lookup, email verification, and the newer Universal API family (universal account, person search, company search, person lookup, company lookup, bulk lookup and lookup status).

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [rocketreach.co](https://rocketreach.co) |
| **Authentication** | Credentials you enter |
| **Slug** | `rocketreach` |

## Use it

Add RocketReach from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rocketreach.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk People Lookup API | `bulkLookupPeople` | Bulk People Lookup API. Bulk People Lookup by Criteria |
| Company Lookup API | `lookupCompany` | Company Lookup API. Search Companies by Criteria |
| Company Search API | `searchCompanies` | Company Search API. Search Companies by Criteria |
| Email Verify API | `verifyEmail` | Email Verify API. Verify whether one email address can receive mail. Charges one email verification credit, refunded when the result is `unknown` or the email is incorrectly formatted. |
| Look Up Person | `lookupPerson` | People Lookup API. Person Enrichment API |
| People and Company Lookup API | `lookupPersonAndCompany` | People and Company Lookup API. Person and Company Lookup |
| People Lookup Status API | `checkPersonLookupStatus` | People Lookup Status API. Check Person Lookup Status |
| People Search API | `searchPeople` | People Search API. Search People by Criteria |
| Retrieve Account | `getAccount` | RocketReach API Account. Retrieve & Manage Account Details |
| ⭐ RocketReach Universal API Account | `getUniversalAccount` | ⭐ RocketReach Universal API Account. Retrieve & Manage Account Details |

<details>

<summary>See 6 more actions</summary>

* **⭐ Universal Bulk People Lookup API** `bulkLookupPeopleUniversal`: ⭐ Universal Bulk People Lookup API. Bulk People Lookup by Criteria
* **⭐ Universal Company Lookup API** `lookupCompanyUniversal`: ⭐ Universal Company Lookup API. Search Companies by Criteria
* **⭐ Universal Company Search API** `searchCompaniesUniversal`: ⭐ Universal Company Search API. Search Companies by Criteria
* **⭐ Universal People Lookup API** `lookupPersonUniversal`: ⭐ Universal People Lookup API. Person Enrichment API
* **⭐ Universal People Lookup Status API** `checkPersonLookupStatusUniversal`: ⭐ Universal People Lookup Status API. Check Universal Person Lookup Status
* **⭐ Universal People Search API** `searchPeopleUniversal`: ⭐ Universal People Search API. Search People by Criteria

</details>
