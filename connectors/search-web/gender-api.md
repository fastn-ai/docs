---
description: "Gender-API.com predicts gender from a first name, full name or email address. Look up single or multiple names and country of origin."
hidden: true
---

# Gender-API.com

<img src="../../.gitbook/assets/connectors/lg/gender-api.png" alt="Gender-API.com logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [gender-api.com](https://gender-api.com) |
| **Authentication** | API key |
| **Slug** | `genderApi` |

## Setup

Your customers enter their API key for Gender-API.com when they connect. Nothing else needs setting up.

## Use it

Add Gender-API.com from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.genderApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Country Of Origin</td><td><code>getCountryOfOrigin</code></td><td>Determines the likely countries of origin, ethnicity, language of origin and meaning of a name, together with its gender, from a first name, a full name or an email address. Exactly one of first_name, full_name or email must be supplied. Costs 2 credits. A missing parameter is reported as HTTP 200 with a problem-details body (status 400, title 'mandatory-parameter-missing').</td></tr><tr><td>Get Statistics</td><td><code>getStatistics</code></td><td>Retrieves usage statistics for the connected Gender-API.com account, including the number of remaining request credits, whether the monthly limit has been reached and the credits used last month. This call does not consume credits.</td></tr><tr><td>Query Gender By Email Address</td><td><code>queryGenderByEmailAddress</code></td><td>Extracts a name from an email address and determines the most likely gender, with optional localisation by ISO country code, browser locale or IP address. Costs 1 credit. Validation errors are returned as HTTP 200 with a problem-details body (status, title, detail); check result_found and status.</td></tr><tr><td>Query Gender By Email Address Multiple</td><td><code>queryGenderByEmailAddressMultiple</code></td><td>Extracts names from several email addresses and determines the most likely gender for each in a single request. Pass the queries as a JSON array string; each query may carry its own country, locale, IP address and client id. Costs 1 credit per address; free API keys are limited to 3 lookups per request. The response is an array with one result object per query, in the same order.</td></tr><tr><td>Query Gender By First Name</td><td><code>queryGenderByFirstName</code></td><td>Determines the most likely gender for a single first name, with optional localisation by ISO country code, browser locale or IP address for higher accuracy. Costs 1 credit. Validation errors are returned as HTTP 200 with a problem-details body (status, title, detail); check result_found and status.</td></tr><tr><td>Query Gender By First Name Multiple</td><td><code>queryGenderByFirstNameMultiple</code></td><td>Determines the most likely gender for several first names in a single request. Pass the queries as a JSON array string; each query may carry its own country, locale, IP address and client id. Costs 1 credit per name; free API keys are limited to 3 lookups per request. The response is an array with one result object per query, in the same order.</td></tr><tr><td>Query Gender By Full Name</td><td><code>queryGenderByFullName</code></td><td>Splits a combined full name into first and last name and determines the most likely gender, with optional localisation by ISO country code, browser locale or IP address. Costs 1 credit. Validation errors are returned as HTTP 200 with a problem-details body (status, title, detail); check result_found and status.</td></tr><tr><td>Query Gender By Full Name Multiple</td><td><code>queryGenderByFullNameMultiple</code></td><td>Splits several full names into first and last name and determines the most likely gender for each in a single request. Pass the queries as a JSON array string; each query may carry its own country, locale, IP address and client id. Costs 1 credit per name; free API keys are limited to 3 lookups per request. The response is an array with one result object per query, in the same order.</td></tr><tr><td>Sign Up</td><td><code>signUp</code></td><td>Creates a new free-tier Gender-API.com account (100 requests per month) for an email address and returns a dashboard password and an API token. The account starts in 'awaiting_activation'; the token works once the user clicks the activation link emailed to them. This public endpoint needs no authentication and sends an activation email to the given address, so only call it with an address whose owner has consented. Invalid input</td></tr></tbody></table>

## Events

Gender-API.com has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
