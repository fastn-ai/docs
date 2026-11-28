---
description: "AbstractAPI Email Reputation checks an email address. Get its deliverability, quality score, risk and known data breaches."
hidden: true
---

# AbstractAPI Email Reputation

<img src="../../.gitbook/assets/connectors/lg/abstract-api-email-reputation.png" alt="AbstractAPI Email Reputation logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiEmailReputation` |

## Setup

Your customers enter their API key for AbstractAPI Email Reputation when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AbstractAPI Email Reputation from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AbstractAPI Email Reputation**.
2. Select **Connect** on the AbstractAPI Email Reputation card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AbstractAPI Email Reputation's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Email Reputation</td><td><code>checkEmailReputation</code></td><td>Validates and enriches an email address, returning deliverability status, MX/SMTP checks, a quality score, sender and domain details, risk status, and any known data breaches associated with the address.</td></tr></tbody></table>

