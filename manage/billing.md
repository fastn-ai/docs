---
description: Your plan, what you have used, and where the ceilings are.
---

# Billing and limits

**Settings → Billing** ([open in app](https://app.fastn.dev/settings/billing)). Owners and admins see everything on this page. Developers see the plan and usage, but not payment details or invoices.

## Plans

fastn is billed by **connected accounts**: each account one of your customers connects through fastn (a customer's HubSpot, their Google Calendar, and so on).

| Plan | Price | What it is for |
| --- | --- | --- |
| **Launch** | $0, forever | Building and testing against a sandbox customer. Includes 3 connected accounts, unlimited connectors and workflows, 50 agent runs a month and community support. Upgrade before you put a paying customer on it. |
| **Scale** | $500 a month, including 10 connected accounts | Production. Each additional connected account is $50 a month, and the count tracks your connected accounts automatically. Subscribe yourself from this page with **Subscribe to Scale**. |
| **Enterprise** | Custom | Priced to your volume, with terms and support agreed up front. Contact sales. |

See [fastn.ai/pricing](https://fastn.ai/pricing) for the full comparison.

The plan card shows what you are on. On Launch it offers **See plans** and **Subscribe to Scale**. On a paid plan it offers **Manage billing** (card and billing details, through Stripe), **Cancel subscription** and **Request plan change**.

## Credits

**Credits this period** tracks AI usage (the agent building and changing integrations) against your monthly allowance. It is the same number as the credits readout in the top bar. Click that readout for the detail: **Your usage** and **Org total** tabs, and a breakdown by agent. Credits reset at the start of each calendar month, UTC.

## Limits

Every quota on your plan is listed with your usage against it. On Launch the main ceilings are:

| Limit | Launch |
| --- | --- |
| Connected accounts | 3 |
| Active integrations | 3 |
| Users per workspace | 3 |
| Webhook endpoints | 3 |
| Events | 500 a day |
| API calls | 1,000 a day |
| Executions | 10,000 a month |
| AI credits | 50 a month |
| Log retention | 7 days |
| Storage | 1 GB |

Paid plans raise or remove these. The page also lists per-customer limits (API keys and workflows per customer), per-minute rate limits, and the workflow categories and labels managed under [Workflows Tags](workflow-tags.md).

**Customize customer limits** overrides the limits for one customer, for example to give a pilot customer more room than the rest.

{% hint style="warning" %}
Going over a limit **stops new work rather than charging you**, and nothing already running is interrupted. There are no surprise invoices, but a sync that stops at a ceiling can look like a broken sync. If runs stop unexpectedly, check this page before you debug the workflow.
{% endhint %}

## Payment and invoices

**Payment** shows the card on file for paid plans, or *Free plan, nothing to pay* on Launch. **Invoices** lists every invoice with its amount and status. Owners and admins can open and download them.

## Related

* [Customers](../operate/customers.md): who your customers are and what each one has connected (Operate → Customers)
* [Roles](roles.md): who can see billing
