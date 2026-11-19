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

## Use it

Add AbstractAPI Holidays from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiHolidays.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Holidays</td><td><code>getHolidays</code></td><td>Returns the public, religious, and observance holidays for a country on a given date. The free plan only accepts a single exact day (country, year, month, and day all supplied together) - a year-only or month-only query</td></tr></tbody></table>

## Events

AbstractAPI Holidays has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
