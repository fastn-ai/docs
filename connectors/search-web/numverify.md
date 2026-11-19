---
description: "Numverify is a real-time international and national phone number validation and lookup API by APILayer."
hidden: true
---

# Numverify

<img src="../../.gitbook/assets/connectors/lg/numverify.png" alt="Numverify logo">

It validates phone number format, and returns carrier, line type (mobile/landline/VoIP), and geographic location metadata for numbers across 232 countries.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [numverify.com](https://numverify.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `numverify` |

## Use it

Add Numverify from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.numverify.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Supported Countries</td><td><code>listSupportedCountries</code></td><td>Returns the full list of countries the Numverify API supports for phone number validation, keyed by ISO 3166-1 alpha-2 country code, with each entry's country name and international dialling code.</td></tr><tr><td>Validate Phone Number</td><td><code>validatePhoneNumber</code></td><td>Validates a phone number and returns its format, carrier, line type, and geographic location. Accepts numbers in international (E.164) format directly, or in national format when paired with a country code.</td></tr></tbody></table>
