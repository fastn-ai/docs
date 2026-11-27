---
description: "UK Bank Holidays lists bank holidays for England and Wales, Scotland and Northern Ireland. List holidays by region or get them as a calendar."
hidden: true
---

# UK Bank Holidays

<img src="../../.gitbook/assets/connectors/lg/uk-bank-holidays.png" alt="UK Bank Holidays logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [gov.uk](https://gov.uk) |
| **Authentication** | No sign-in needed |
| **Slug** | `ukBankHolidays` |

## Setup

UK Bank Holidays needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect UK Bank Holidays from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **UK Bank Holidays**.
2. Select **Connect** on the UK Bank Holidays card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. UK Bank Holidays needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use UK Bank Holidays's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Bank Holidays Calendar (ICS)</td><td><code>getBankHolidaysCalendar</code></td><td>Get a division's bank holidays as an iCalendar (.ics) file to import into calendar apps (GET https://www.gov.uk/bank-holidays/{division}.ics). Docs: https://www.gov.uk/bank-holidays</td></tr><tr><td>List Bank Holidays</td><td><code>listBankHolidays</code></td><td>List UK bank holidays for England and Wales, Scotland and Northern Ireland, past and upcoming (GET https://www.gov.uk/bank-holidays.json). Docs: https://www.gov.uk/bank-holidays</td></tr><tr><td>List Division Bank Holidays</td><td><code>listDivisionBankHolidays</code></td><td>List bank holidays for one UK division (GET https://www.gov.uk/bank-holidays/{division}.json). Docs: https://www.gov.uk/bank-holidays</td></tr></tbody></table>

