---
description: >-
  Is everything working? Health shows what needs your attention across every
  customer, the totals behind it, vendor changes waiting on you, and your alerts.
---

# Health

**Operate → Health** ([open in app](https://app.fastn.dev/health)). Developers and above.

> The maintainer agent watches the apps you connect to, your customers' connections and your workflows. What it found, with the fix it proposes, is here.

Health is the first place to look each morning. It has four tabs:

| Tab | What it answers |
| --- | --- |
| **Needs attention** (the default) | What is broken right now, and what to do about it |
| **Overview** | How every customer's integrations are doing, in totals and trends |
| **Pending updates** | Which vendor changes are waiting for you to accept a fix |
| **Alerts** | Who gets told when something fails, and where |

## Needs attention

One row per thing that needs a person, each with the action that fixes it:

* **A vendor changed an app you use**, for example *`hubspot` changed*. **Review** opens the fix the maintainer agent proposes. See [Pending updates](../build/connector-updates.md).
* **A customer connection expired or failed.** The row says whether the customer must sign in again. **Open connection** takes you to it.
* **A workflow failed today**, for example *"Order sync" failed 3 of 40 runs today*, with its last run status and a link to the runs.

When there is nothing to do, the tab reads **Nothing needs attention**: no vendor changes are waiting, every customer connection is working, and no workflow failed today.

## Overview

The cross-customer rollup (previously the **Reporting** page): which customers need attention, how many runs and records, and what is failing and why. Filter by customer and date range.

### Filters

* **Customer:** **All customers** (the default), **Admin (your own org)**, or one customer. Picking one customer scopes every number on the page to them.
* **Range:** **Today** (the default), **7 days**, **14 days**, **30 days**, **90 days**, or **Custom range**, up to 365 days.
* **Refresh** reloads the numbers.

### What it shows

**Customer tiles** (with All customers selected): how many **Customers** you have, how many **Need attention**, how many are **Healthy**, how many are **Not connected** yet, and the total number of **Connections**. Click a tile to see the customers behind it. **Need attention** is the exception: it opens the problems themselves rather than a customer list.

**Right now** (live, refreshed on a timer):

* **Workflow runs:** **Running** and **Waiting to start**.
* **Trigger events:** **Waiting for a run** (received, no workflow run yet) and **Retrying delivery** (delivery failed, another attempt is due).

**The selected period:** a strip of **Recovered by retry**, **Sent to DLQ**, **Processed after DLQ**, **Still in DLQ** (deliveries that ran out of retries and are not delivered yet, the ones that need a person) and **Alerts fired**, followed by an **Events** strip with what happened to the events routed in the period.

| Panel | What it tells you |
| --- | --- |
| **Runs** | Runs over the period as a bar chart, with the change against the previous period |
| **Records processed** | Records synced, failed and skipped |
| **Connection health** | How many connections are healthy and how many need action |
| **Processing time** | How long runs take |
| **What's failing** | Failures grouped by cause: Authentication, Permission, Rate limited, Timed out, Not found, Invalid input and Other |
| **Workflows** | Per workflow: last run, runs, failures, average duration, and records synced, failed and skipped |
| **Connectors** | Per connector: customers connected, healthy and broken connections, actions run and actions failed |
| **By day** | Runs and records (or events) for each day in the period, with the total |

{% hint style="info" %}
**What's failing** is the fastest way to triage. *Authentication* failures usually mean a customer must reconnect an account; *Rate limited* and *Timed out* usually resolve on retry; *Invalid input* usually means a mapping or workflow change is needed.
{% endhint %}

## Pending updates

Vendors change their APIs. fastn notices, works out the fix, and files it here for you to accept. Nothing is applied until you do. See [Pending updates](../build/connector-updates.md).

## Alerts

Set who is told when a run fails, an event is not processed in time, a metric crosses a threshold, or your workflow code raises an alert, by email, Slack, Teams or webhook. See [Alerts](alerts.md).

## A daily routine

1. Open **Health**. If **Needs attention** is empty, you are done.
2. Work each row with its action: review the fix, ask the customer to reconnect, or open the failed runs.
3. Use **Overview** to check whether a failure is one customer's credentials or a pattern across many.
4. Go to [Activity](README.md) for the individual events and runs behind a number.
5. Turn anything you find yourself checking by hand into an [alert](alerts.md).

Your customers see their own version of these numbers in the widget, under **⋯ → Insights**. See [View sync status and history](../tutorials/end-user/viewing-sync-status-and-history.md).
