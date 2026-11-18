---
description: "AbstractAPI Holidays returns public, religious, and observance holidays for 200+ countries by date."
---

# AbstractAPI Holidays

AbstractAPI Holidays returns public, religious, and observance holidays for 200+ countries by date. On the free plan, queries must specify a single exact day (country, year, month, and day together); broader month- or year-only queries require a paid plan.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 1 |
| **Events** | 0 |
| **Slug** | `abstractApiHolidays` |

## Use it

Add AbstractAPI Holidays from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiHolidays.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Holidays | `getHolidays` | Returns the public, religious, and observance holidays for a country on a given date. The free plan only accepts a single exact day (country, year, month, and day all supplied together) - a year-only or month-only query returns a 402 payment_required error and requires a paid plan. |
