---
description: "AbstractAPI Phone Intelligence validates a phone number. Get its format, carrier, line type, location and risk signals."
hidden: true
---

# AbstractAPI Phone Intelligence

<img src="../../.gitbook/assets/connectors/lg/abstract-api-phone-intelligence.png" alt="AbstractAPI Phone Intelligence logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiPhoneIntelligence` |

## Setup

Your customers enter their API key for AbstractAPI Phone Intelligence when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AbstractAPI Phone Intelligence from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AbstractAPI Phone Intelligence**.
2. Select **Connect** on the AbstractAPI Phone Intelligence card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AbstractAPI Phone Intelligence's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Validate Phone Number</td><td><code>validatePhoneNumber</code></td><td>Validates and enriches a phone number, returning its formatting, carrier and line type, geographic location, SMS messaging address, registration name, risk level, and any known data breaches associated with it.</td></tr></tbody></table>

