---
description: "AbstractAPI Holidays lists public and religious holidays for over 200 countries. Get the holidays for a country on a given date."
hidden: true
---

# AbstractAPI Holidays

<img src="../../.gitbook/assets/connectors/lg/abstract-api-holidays.png" alt="AbstractAPI Holidays logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiHolidays` |

## Setup

Your customers enter their API key for AbstractAPI Holidays when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AbstractAPI Holidays from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AbstractAPI Holidays**.
2. Select **Connect** on the AbstractAPI Holidays card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AbstractAPI Holidays's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Holidays</td><td><code>getHolidays</code></td><td>Returns the public, religious, and observance holidays for a country on a given date. The free plan only accepts a single exact day (country, year, month, and day all supplied together) - a year-only or month-only query</td></tr></tbody></table>

