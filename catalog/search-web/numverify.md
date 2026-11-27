---
description: "Numverify validates phone numbers. Check a number and get its country, carrier and line type."
hidden: true
---

# Numverify

<img src="../../.gitbook/assets/connectors/lg/numverify.png" alt="Numverify logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [numverify.com](https://numverify.com) |
| **Authentication** | API key |
| **Slug** | `numverify` |

## Setup

Your customers enter their API key for Numverify when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Numverify from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Numverify**.
2. Select **Connect** on the Numverify card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Numverify's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Supported Countries</td><td><code>listSupportedCountries</code></td><td>Returns the full list of countries the Numverify API supports for phone number validation, keyed by ISO 3166-1 alpha-2 country code, with each entry's country name and international dialling code.</td></tr><tr><td>Validate Phone Number</td><td><code>validatePhoneNumber</code></td><td>Validates a phone number and returns its format, carrier, line type, and geographic location. Accepts numbers in international (E.164) format directly, or in national format when paired with a country code.</td></tr></tbody></table>

