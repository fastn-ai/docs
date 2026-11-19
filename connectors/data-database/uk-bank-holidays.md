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

## Use it

Add UK Bank Holidays from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ukBankHolidays.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Bank Holidays Calendar (ICS)</td><td><code>getBankHolidaysCalendar</code></td><td>Get a division's bank holidays as an iCalendar (.ics) file to import into calendar apps (GET https://www.gov.uk/bank-holidays/{division}.ics). Docs: https://www.gov.uk/bank-holidays</td></tr><tr><td>List Bank Holidays</td><td><code>listBankHolidays</code></td><td>List UK bank holidays for England and Wales, Scotland and Northern Ireland, past and upcoming (GET https://www.gov.uk/bank-holidays.json). Docs: https://www.gov.uk/bank-holidays</td></tr><tr><td>List Division Bank Holidays</td><td><code>listDivisionBankHolidays</code></td><td>List bank holidays for one UK division (GET https://www.gov.uk/bank-holidays/{division}.json). Docs: https://www.gov.uk/bank-holidays</td></tr></tbody></table>

## Events

UK Bank Holidays has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
