---
description: Get told when something crosses a line you care about. Checked every 15 minutes.
---

# Alerts

**Activity → Alerts**

<figure><img src="../.gitbook/assets/activity-alerts.jpg" alt="The Alerts page holding only a No alerts yet empty state, naming the destination address it would send to, with Turn on failure alerts and Custom alert buttons and New alert top-right"><figcaption><strong>Turn on failure alerts</strong> creates the two alerts most teams need in one click.</figcaption></figure>

Without an alert, a sync can fail quietly for hours. This is the cheapest insurance in the product. The empty state says as much:

> Without one, a sync can fail quietly for hours. One click turns on the two alerts most teams need…

under the heading **No alerts yet**, with **Turn on failure alerts** and **Custom alert** beside it. It names the address the two alerts would go to: the email you signed in with. **New alert** sits top-right, and the empty state is the whole page until an alert exists.

### The one-click start

**Turn on failure alerts** creates the two alerts most teams need in one click: an email the moment a run fails, and a daily reliability check. If you do nothing else on this page, do that.

### Custom alerts

<figure><img src="../.gitbook/assets/alert-editor.jpg" alt="The alert editor open on an Untitled alert badged Paused and No recipients, set to fire when Error rate is above 5% over 24 hours, watching All workflows, with Slack, Email and Webhook delivery fields"><figcaption>Firing history at the bottom reads This alert has not fired yet.</figcaption></figure>

**New alert** (or **Custom alert** on the empty state), opens the editor.

{% hint style="danger" %}
**The editor autosaves, and there is no Save button.** **New alert** persists an alert on the server the moment you click it (an `Untitled alert`, **Paused**, with **No recipients**) and every subsequent edit is saved as you make it. There is nothing to confirm and nothing to cancel. If you opened one by accident, delete it from its row; closing the editor leaves it behind.
{% endhint %}

#### Alert when

Two shapes. **a metric crosses a threshold** is the default.

* **a run fails (instant)**: fires on the failure itself.
* **a metric crosses a threshold**: fires when a measured value goes above or below a number, over a window. The default.

#### Metrics

**Error rate** is the default.

| Metric                  | Measures                                        | Unit    |
| ----------------------- | ------------------------------------------------- | ------- |
| **Error rate**          | Percent of runs that failed in the window.       | %       |
| **Success rate**        | The inverse.                                     | %       |
| **Failed runs**         | Count of failures.                               | count   |
| **Total runs**          | Count of runs: catches a source that went quiet. | count   |
| **Records synced**      | Volume moved.                                    | count   |
| **Records failed**      | Records rejected downstream.                     | count   |
| **Avg run time**        | Mean duration.                                   | time    |
| **p95 run time**        | Tail latency.                                    | time    |
| **Broken connectors**   | Connectors with failing connections.             | count   |
| **Inactive workflows**  | Workflows that have stopped running.             | count   |

Each takes **is above** or **is below**, a value, and a window of **1 hour**, **24 hours**, **7 days** or **30 days**.

{% hint style="warning" %}
Watch the unit when you type a threshold. The default alert is **Error rate is above 5**: five *percent*. Switch the metric to **Failed runs** and the same 5 means five *runs*, which on a busy workspace is a far tighter trigger than it looks.
{% endhint %}

**Defaults on a new alert:** **a metric crosses a threshold**, metric **Error rate**, comparator **is above**, threshold **5%**, window **24 hours**.

#### Watch

A multi-select: leave it across everything, or pick the specific workflows this alert applies to. Scope noisy metrics narrowly; a global error-rate alarm on a workspace with one flaky test workflow trains you to ignore it.

#### Deliver to

| Channel     | Configure                       |
| ----------- | --------------------------------- |
| **Slack**   | An incoming webhook URL.        |
| **Email**   | One or more addresses.          |
| **Webhook** | An HTTPS endpoint of your own.  |

An alert with no recipients shows **No recipients** and will not notify anyone.

#### Firing history

Each alert keeps a record of every time it fired: the fastest way to tell a real signal from a threshold set too tight. On a new one it reads `This alert has not fired yet.`

### Evaluation

Threshold alerts are evaluated every 15 minutes. Run-failure alerts are instant.

### A starting set

| Alert                                                | Why                                              |
| ---------------------------------------------------- | -------------------------------------------------- |
| A run fails → email + Slack                          | The baseline.                                     |
| Error rate above 5% over 1 hour                      | Catches degradation before it is total.           |
| Total runs below 1 over 24 hours, on a daily sync    | Catches a schedule that silently stopped.         |
| Broken connectors above 0                            | Catches expired credentials before the customer does. |

### Alerts your customers set up

Your customers can set up alerts themselves, from the integration hub inside your app. They do it from the **Insights** panel of the hub. Their alerts watch their own integrations and go to their own recipients, separately from the alerts on this page.

**Step 1: Open Insights**

1. Open the **Integrations** hub in your app.
2. Click the **...** (menu) button in the top right corner of the hub header.
3. Select **Insights**.

<figure><img src="../.gitbook/assets/widget-menu-insights.png" alt="The integration hub header, titled Integrations with the subtitle Connect your favorite tools, with the three-dot menu open showing Insights"><figcaption>The <strong>...</strong> menu in the hub header.</figcaption></figure>

**Step 2: Go to the alerts section**

Scroll to the bottom of the **Insights** panel. There are two options there:

* **Sync failure notifications**: click **Turn on** to be notified the moment any sync run fails. This is the quickest option.
* **New alert**: create a custom alert with your own conditions (Step 3).

<figure><img src="../.gitbook/assets/customer-alerts-sync-failure-row.webp" alt="The alerts section of the Insights panel: a New alert button above the Sync failure notifications row, which reads Off, a sync can fail silently, with an Edit channels toggle"><figcaption><strong>Sync failure notifications</strong> and <strong>New alert</strong>.</figcaption></figure>

**Step 3: Create a custom alert**

Click **New alert** and fill in:

* **Name**: for example, "Order sync failures".
* **Alert when**: the condition to alert on, for example error rate is above 5% over 24 hours.
* **Watch**: all workflows, or only a specific one (for example, HubSpot Deal to Order).
* **Deliver to**: where the alert is sent: Email, Slack, Microsoft Teams or a Webhook.

The fields are the same as in a [custom alert](#custom-alerts) above.

<figure><img src="../.gitbook/assets/widget-alert-card.png" alt="A new alert card named Untitled alert, badged Paused and No recipients, with Alert when set to Error rate is above 5 percent over 24 hours, Watch set to All workflows, Deliver to rows for Email, Slack, Teams and Webhook, and a Firing history reading This alert has not fired yet"><figcaption>A new custom alert, before it is turned on.</figcaption></figure>

**Step 4: Turn the alert on**

1. Switch the toggle next to the alert name on. A new alert starts paused.
2. Optionally, click the test (play) button to send a test alert and check it arrives.
3. **Firing history** under the alert shows every time it has fired.
