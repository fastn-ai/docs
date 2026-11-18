---
description: "Gender-API.com determines the most likely gender behind a first name, full name or email address, optionally localised by country, locale or IP address, and…"
---

# Gender-API.com

Gender-API.com determines the most likely gender behind a first name, full name or email address, optionally localised by country, locale or IP address, and can also infer a name's country of origin, ethnicity and meaning. This connector covers the full Gender-API.com Unified API v2: single and multiple-name gender lookups by first name, full name and email address, country-of-origin lookups, account usage statistics and free-tier sign-up.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [gender-api.com](https://gender-api.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 9 |
| **Events** | 0 |
| **Slug** | `genderApi` |

## Use it

Add Gender-API.com from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.genderApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Country Of Origin | `getCountryOfOrigin` | Determines the likely countries of origin, ethnicity, language of origin and meaning of a name, together with its gender, from a first name, a full name or an email address. Exactly one of first_name, full_name or email must be supplied. Costs 2 credits. A missing parameter is reported as HTTP 200 with a problem-details body (status 400, title 'mandatory-parameter-missing'). |
| Get Statistics | `getStatistics` | Retrieves usage statistics for the connected Gender-API.com account, including the number of remaining request credits, whether the monthly limit has been reached and the credits used last month. This call does not consume credits. |
| Query Gender By Email Address | `queryGenderByEmailAddress` | Extracts a name from an email address and determines the most likely gender, with optional localisation by ISO country code, browser locale or IP address. Costs 1 credit. Validation errors are returned as HTTP 200 with a problem-details body (status, title, detail); check result_found and status. |
| Query Gender By Email Address Multiple | `queryGenderByEmailAddressMultiple` | Extracts names from several email addresses and determines the most likely gender for each in a single request. Pass the queries as a JSON array string; each query may carry its own country, locale, IP address and client id. Costs 1 credit per address; free API keys are limited to 3 lookups per request. The response is an array with one result object per query, in the same order. |
| Query Gender By First Name | `queryGenderByFirstName` | Determines the most likely gender for a single first name, with optional localisation by ISO country code, browser locale or IP address for higher accuracy. Costs 1 credit. Validation errors are returned as HTTP 200 with a problem-details body (status, title, detail); check result_found and status. |
| Query Gender By First Name Multiple | `queryGenderByFirstNameMultiple` | Determines the most likely gender for several first names in a single request. Pass the queries as a JSON array string; each query may carry its own country, locale, IP address and client id. Costs 1 credit per name; free API keys are limited to 3 lookups per request. The response is an array with one result object per query, in the same order. |
| Query Gender By Full Name | `queryGenderByFullName` | Splits a combined full name into first and last name and determines the most likely gender, with optional localisation by ISO country code, browser locale or IP address. Costs 1 credit. Validation errors are returned as HTTP 200 with a problem-details body (status, title, detail); check result_found and status. |
| Query Gender By Full Name Multiple | `queryGenderByFullNameMultiple` | Splits several full names into first and last name and determines the most likely gender for each in a single request. Pass the queries as a JSON array string; each query may carry its own country, locale, IP address and client id. Costs 1 credit per name; free API keys are limited to 3 lookups per request. The response is an array with one result object per query, in the same order. |
| Sign Up | `signUp` | Creates a new free-tier Gender-API.com account (100 requests per month) for an email address and returns a dashboard password and an API token. The account starts in 'awaiting_activation'; the token works once the user clicks the activation link emailed to them. This public endpoint needs no authentication and sends an activation email to the given address, so only call it with an address whose owner has consented. Invalid input returns HTTP 400 with a problem-details body. |
