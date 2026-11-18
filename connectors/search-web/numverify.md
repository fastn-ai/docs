---
description: "Numverify is a real-time international and national phone number validation and lookup API by APILayer."
---

# Numverify

Numverify is a real-time international and national phone number validation and lookup API by APILayer. It validates phone number format, and returns carrier, line type (mobile/landline/VoIP), and geographic location metadata for numbers across 232 countries.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [numverify.com](https://numverify.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 2 |
| **Events** | 0 |
| **Slug** | `numverify` |

## Use it

Add Numverify from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.numverify.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| List Supported Countries | `listSupportedCountries` | Returns the full list of countries the Numverify API supports for phone number validation, keyed by ISO 3166-1 alpha-2 country code, with each entry's country name and international dialling code. |
| Validate Phone Number | `validatePhoneNumber` | Validates a phone number and returns its format, carrier, line type, and geographic location. Accepts numbers in international (E.164) format directly, or in national format when paired with a country code. |
