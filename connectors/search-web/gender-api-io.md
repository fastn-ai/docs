---
description: "Connect GenderAPI.io to your product with fastn."
hidden: true
---

# GenderAPI.io

<img src="../../.gitbook/assets/connectors/lg/gender-api-io.png" alt="GenderAPI.io logo">

GenderAPI.io predicts gender from a first name, full name, email address or username, with optional country context and AI fallback, and validates and formats international phone numbers. This connector covers the full GenderAPI.io REST API: single and bulk gender lookups by name, email and username, phone number validation, and remaining-credit monitoring.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [genderapi.io](https://genderapi.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `genderApiIo` |

## Use it

Add GenderAPI.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.genderApiIo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Gender By Email</td><td><code>getGenderByEmail</code></td><td>Extracts a likely first name from a single email address and predicts its gender, returning the extracted name, predicted gender, confidence probability and country. Optionally adds country context and an AI fallback. Costs one credit.</td></tr><tr><td>Get Gender By Multiple Emails</td><td><code>getGenderByMultipleEmails</code></td><td>Extracts a likely first name from each of up to 50 email addresses and predicts its gender in one request, with optional per-record country context and your own record identifiers returned unchanged for correlation. Costs one credit per email.</td></tr><tr><td>Get Gender By Multiple Names</td><td><code>getGenderByMultipleNames</code></td><td>Predicts gender for up to 100 first names in one request, with optional per-record country context and your own record identifiers returned unchanged for correlation. Bulk requests do not use the AI fallback. Costs one credit per name.</td></tr><tr><td>Get Gender By Multiple Usernames</td><td><code>getGenderByMultipleUsernames</code></td><td>Extracts potential first names from up to 50 usernames or handles and predicts their gender in one request, with optional per-record country context and your own record identifiers returned unchanged for correlation. Bulk requests do not use the AI fallback. Costs one credit per username.</td></tr><tr><td>Get Gender By Name</td><td><code>getGenderByName</code></td><td>Predicts the gender of a single first name or full name, returning the predicted gender, confidence probability, most likely country and the number of samples behind the prediction. Optionally adds country context, an AI fallback for names not in the database, and forced predictions for nicknames. Costs one credit.</td></tr><tr><td>Get Gender By Username</td><td><code>getGenderByUsername</code></td><td>Extracts a potential first name from a single username, handle or nickname and predicts its gender, returning the extracted name, predicted gender, confidence probability and country. Optionally adds country context, an AI fallback and forced predictions for low-signal handles. Costs one credit.</td></tr><tr><td>Get Remaining Credits</td><td><code>getRemainingCredits</code></td><td>Returns the number of API credits currently available on the account and the package expiration time, without performing a gender lookup. Use it to monitor quota before running bulk jobs.</td></tr><tr><td>Validate Phone Number</td><td><code>validatePhoneNumber</code></td><td>Validates and formats an international phone number, returning national, international and E.164 representations plus validity, number type (mobile, landline, VoIP and more), region, area code and location metadata. Provide an address context such as a country code when the number is not in international format.</td></tr></tbody></table>
