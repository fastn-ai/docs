---
description: Get told when something crosses a line you care about. Checked every 15 minutes.
---

# Alerts

**Operate → Health → Alerts** · `/health?tab=alerts`

<figure><img src="../.gitbook/assets/activity-alerts.jpg" alt="The Alerts page holding only a No alerts yet empty state, naming the destination address it would send to, with Turn on failure alerts and Custom alert buttons and New alert top-right"><figcaption><strong>Turn on failure alerts</strong> creates the two alerts most teams need in one click.</figcaption></figure>

Without an alert, a sync can fail quietly for hours. This is the cheapest insurance in the product.

At the top of the tab, a **Notification channels** strip ("Email and webhooks work without a connection") shows which messaging apps are connected for alerts, with a way to connect the ones that are not. Below it, until an alert exists, sits the empty state:

> Without one, a sync can fail quietly for hours. One click turns on the two alerts most teams need…

under the heading **No alerts yet**, with **Turn on failure alerts** and **Custom alert** beside it. It names the address the two alerts would go to: the email you signed in with. If your session has no email, **Turn on failure alerts** is disabled; create a custom alert instead. **New alert** sits top-right.

### The one-click start

**Turn on failure alerts** creates the two alerts most teams need in one click: an email the moment a run fails, and a daily reliability check. If you do nothing else on this page, do that.

### Custom alerts

<figure><img src="../.gitbook/assets/alert-editor.jpg" alt="The alert editor open on an Untitled alert badged Paused and No recipients, set to fire when Error rate is above 5% over 24 hours, watching All workflows, with Slack, Email and Webhook delivery fields"><figcaption>Firing history at the bottom reads This alert has not fired yet.</figcaption></figure>

**New alert** (or **Custom alert** on the empty state), opens the editor.

{% hint style="danger" %}
**The editor autosaves, and there is no Save button.** **New alert** persists an alert on the server the moment you click it (an `Untitled alert`, **Paused**, with **No recipients**) and every subsequent edit is saved as you make it. There is nothing to confirm and nothing to cancel. If you opened one by accident, delete it from its row; closing the editor leaves it behind.
{% endhint %}

#### Alert when

Four types. **a metric crosses a threshold** is the default.

* **a run fails (instant)**: fires on the failure itself.
* **an event is not processed in time**: fires when an event arrived a set number of minutes ago (5 to 1440, default 15) and its workflow has not succeeded.
* **a metric crosses a threshold**: fires when a measured value goes above or below a number, over a window. The default.
* **workflow code raises it (fastn.alerts)**: fires only when your workflow code calls `fastn.alerts.send("<alert name>", { ... })`.

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
| **Avg run time**        | Mean duration.                                   | ms      |
| **p95 run time**        | Tail latency.                                    | ms      |
| **Broken connectors**   | Connections that are not active right now.       | count   |
| **Inactive workflows**  | Workflows that have stopped running.             | count   |

Each takes **is above** or **is below**, a value, and a window of **1 hour**, **24 hours**, **7 days** or **30 days**.

{% hint style="warning" %}
Watch the unit when you type a threshold. The default alert is **Error rate is above 5**: five *percent*. Switching the metric resets the threshold to that metric's suggested value, in that metric's unit: **Failed runs** suggests 5 *runs*, and **Avg run time** and **p95 run time** are in milliseconds (suggested 5000 and 10000).
{% endhint %}

**Defaults on a new alert:** **a metric crosses a threshold**, metric **Error rate**, comparator **is above**, threshold **5%**, window **24 hours**.

#### Watch

A multi-select: leave it across everything, or pick the specific workflows this alert applies to. It appears for **a run fails** and **an event is not processed in time** alerts, and for threshold alerts on the run metrics (**Total runs**, **Failed runs**, **Error rate**, **Success rate**, **Avg run time**, **p95 run time**). Scope noisy metrics narrowly; a global error-rate alarm on a workspace with one flaky test workflow trains you to ignore it.

#### Deliver to

| Channel     | Configure                       |
| ----------- | --------------------------------- |
| **Email**   | One or more addresses, sent through fastn email or one of your Gmail connections, with an optional **Subject**. |
| **Slack**   | An incoming webhook URL, or a Slack connection and a channel. |
| **Teams**   | A connected Microsoft Teams account: pick the team, then the channel. |
| **Webhook** | An `http` or `https` endpoint of your own. |

Discord and Telegram deliveries can be set up through the API.

An alert with no recipients shows **No recipients** and will not notify anyone.

#### Firing history

The editor shows the five most recent times the alert fired, each marked **Delivered** or with the delivery error: the fastest way to tell a real signal from a threshold set too tight. On a new one it reads `This alert has not fired yet.`

### Evaluation

Threshold alerts are evaluated every 15 minutes by default. Run-failure alerts fire within about a minute of the failure. Processing alerts fire once an event has waited longer than the minutes you set. Code alerts fire when your workflow code sends them.

### A starting set

| Alert                                                | Why                                              |
| ---------------------------------------------------- | -------------------------------------------------- |
| A run fails → email + Slack                          | The baseline.                                     |
| Error rate above 5% over 1 hour                      | Catches degradation before it is total.           |
| Total runs below 1 over 24 hours, on a daily sync    | Catches a schedule that silently stopped.         |
| Broken connectors above 0                            | Catches expired credentials before the customer does. |

### Alerts your customers set up

Your customers can set up alerts themselves, from the widget inside your app. They do it from the **Insights** panel of the widget. Their alerts watch their own integrations and go to their own recipients, separately from the alerts on this page.

**Step 1: Open Insights**

1. Open the **Integrations** widget in the product where it's embedded.
2. Click the **...** (menu) button in the top right corner of the widget header.
3. Select **Insights**.

<figure><img src="../.gitbook/assets/widget-menu-insights.png" alt="The widget header, titled Integrations with the subtitle Connect your favorite tools, with the three-dot menu open showing Insights"><figcaption>The <strong>...</strong> menu in the widget header.</figcaption></figure>

**Step 2: Go to the alerts section**

Scroll to the bottom of the **Insights** panel. With no alerts yet, it shows **No alerts yet** with two buttons:

* **Turn on failure alerts**: turns on an email the moment a run fails and a daily reliability check. This is the quickest option. It is disabled if the session has no email.
* **Custom alert**: create a custom alert with your own conditions (Step 3).

Once an alert exists, the section shows a **Sync failure notifications** card (switch its toggle on to be notified the moment any sync run fails) and a **New alert** button.

<figure><img src="../.gitbook/assets/customer-alerts-sync-failure-row.webp" alt="The alerts section of the Insights panel: a New alert button above the Sync failure notifications row, which reads Off, a sync can fail silently, with an Edit channels toggle"><figcaption><strong>Sync failure notifications</strong> and <strong>New alert</strong>.</figcaption></figure>

**Step 3: Create a custom alert**

Click **Custom alert** (or **New alert** once an alert exists) and fill in:

* **Name**: for example, "Order sync failures".
* **Alert when**: the condition to alert on, for example error rate is above 5% over 24 hours.
* **Watch**: all workflows, or only a specific one (for example, HubSpot Deal to Order).
* **Deliver to**: where the alert is sent: Email, Slack, Microsoft Teams or a Webhook.

The fields are the same as in a [custom alert](#custom-alerts) above.

<figure><img src="../.gitbook/assets/widget-alert-card.png" alt="A new alert card named Untitled alert, badged Paused and No recipients, with Alert when set to Error rate is above 5 percent over 24 hours, Watch set to All workflows, Deliver to rows for Email, Slack, Teams and Webhook, and a Firing history reading This alert has not fired yet"><figcaption>A new custom alert, before it is turned on.</figcaption></figure>

**Step 4: Turn the alert on**

1. Switch the toggle next to the alert name on. A new alert starts paused.
2. Optionally, click the test (play) button to send a test alert and check it arrives.

**Firing history** under the alert shows every time it has fired.
