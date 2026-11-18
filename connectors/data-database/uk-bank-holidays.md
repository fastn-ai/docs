---
description: "UK Bank Holidays is the free GOV.UK data feed of bank holidays in England and Wales, Scotland and Northern Ireland, including substitute days."
hidden: true
---

# UK Bank Holidays

<img src="../../.gitbook/assets/connectors/lg/uk-bank-holidays.png" alt="UK Bank Holidays logo">

UK Bank Holidays is the free GOV.UK data feed of bank holidays in England and Wales, Scotland and Northern Ireland, including substitute days. Get all divisions or one division as JSON, or a division's iCalendar file. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [gov.uk](https://gov.uk) |
| **Authentication** | No authentication |
| **Slug** | `ukBankHolidays` |

## Use it

Add UK Bank Holidays from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ukBankHolidays.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Bank Holidays Calendar (ICS) | `getBankHolidaysCalendar` | Get a division's bank holidays as an iCalendar (.ics) file to import into calendar apps (GET https://www.gov.uk/bank-holidays/{division}.ics). Docs: https://www.gov.uk/bank-holidays |
| List Bank Holidays | `listBankHolidays` | List UK bank holidays for England and Wales, Scotland and Northern Ireland, past and upcoming (GET https://www.gov.uk/bank-holidays.json). Docs: https://www.gov.uk/bank-holidays |
| List Division Bank Holidays | `listDivisionBankHolidays` | List bank holidays for one UK division (GET https://www.gov.uk/bank-holidays/{division}.json). Docs: https://www.gov.uk/bank-holidays |
