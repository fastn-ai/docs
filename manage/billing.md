---
description: Your plan, what you have used, and where the ceilings are.
---

# Billing and limits

**Settings → Billing**

<figure><img src="../.gitbook/assets/settings-billing.jpg" alt="The Billing page with a Free, $0 per month plan card, a Credits this period tile reading 0 of 50 used and resetting in 27 days, and a Limits list where API keys per customer reads 4 / 2, 100%"><figcaption>Rows marked not measured have a cap but no usage reading behind them.</figcaption></figure>

### Plan and credits

The plan card shows what you are on and what it costs — **Free**, at **$0 per month**, until you upgrade. **See plans** is the upgrade control, and the only one on the page.

**Credits this period** tracks AI usage against the allowance. It is the same number as the AI credits readout in the top bar, and the popover behind that readout is where the detail lives: tabs for **Your usage** and **Org total**, a **By agent** breakdown, and a reset at the start of the calendar month, UTC.

### Limits

Each quota is listed with usage against it. **Customize customer limits** overrides limits for a single customer.

| Limit                       | Scope        |
| --------------------------- | ------------ |
| API keys                    | per customer |
| Events                      | per day, per minute |
| API calls                   | per day, per minute |
| Active integrations         | total        |
| Connectors allowed          | total        |
| Workflows                   | per customer |
| Steps                       | per flow     |

The list continues past the visible area with further rows — concurrency, AI sessions and tokens, retention, storage, connected accounts, users, webhook endpoints, payload size, executions and AI credits are all reported to appear further down. Scroll the page and read the rows themselves rather than relying on that list being complete or the scopes being as described.

{% hint style="info" %}
Going over a limit **stops new work rather than charging you, and nothing already running is interrupted.** No surprise invoices, but also no silent overage — a sync that stops because you hit a ceiling looks like a broken sync until you check this page.
{% endhint %}

### Below the fold

Sections further down this page — **Customer tiers** and **Create tier**, **Usage by customer**, **Payment** and **Invoices** — have not been captured, so this page does not describe how they behave. Read them in the product before planning around them.

One thing about tiers is corroborated from elsewhere: the [Roles](roles.md) screen states that a custom role can be assigned to an embed tier under Billing, which is how you scope what an embedded end user may do.
