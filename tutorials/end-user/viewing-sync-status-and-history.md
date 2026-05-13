---
description: >-
  Check what's syncing, view execution history, spot errors, and know when to
  contact support.
---

# Viewing Sync Status & History

Once your integrations are running, you'll want to know:

* Is my data syncing?
* When did it last run?
* Did anything fail?

The widget provides visibility into your integration activity depending on what the SaaS company has enabled.

### Checking sync status

Open the integration widget and look at your connected apps. Each one typically shows a status indicator:

| Status                             | What it means                                     |
| ---------------------------------- | ------------------------------------------------- |
| **Active** / **Connected** (green) | Integration is running normally                   |
| **Syncing** / **Running**          | A sync is currently in progress                   |
| **Error** / **Failed** (red)       | The last sync encountered a problem               |
| **Paused** / **Disabled** (gray)   | Integration is connected but not actively running |

> **Screenshot needed:** Widget showing multiple connected apps with different status indicators — one active (green), one with an error (red).

### Viewing execution history

If the SaaS company has enabled history logs in the widget, you can see a record of past syncs:

1. Open the widget.
2. Click on a connected app or look for a **History** / **Activity** / **Logs** tab.
3. You'll see a list of recent executions, each showing:
   * **Timestamp** — when the sync ran
   * **Status** — success or failure
   * **Duration** — how long it took
   * **Summary** — what happened (e.g., "Synced 45 orders", "Created 12 invoices")

> &#x20;**Screenshot needed:** Execution history view inside the widget showing a list of recent syncs with timestamps, status, and summaries.

{% hint style="info" %}
⚠️ **Note:** Not all integrations show detailed history in the widget. If you don't see a history section, the SaaS company may not have enabled it. Contact their support for execution details.
{% endhint %}

### Understanding errors

When a sync fails, the history may show an error message. Common causes:

**Authentication expired** — Your connection to the third-party app is no longer valid. This happens when:

* You changed your password on the third-party app
* You revoked access in the third-party app's settings
* The OAuth token expired and couldn't be refreshed

**Fix:** Disconnect and reconnect the app through the widget.

**Rate limiting** — The third-party app rejected requests because too many were sent in a short time. This usually resolves on its own — the next scheduled sync will retry.

**Data validation error** — A specific record couldn't be synced because it didn't match the expected format. For example, a required field was empty or a date was in the wrong format.

**Service unavailable** — The third-party app was temporarily down. The next sync will retry automatically.

> **Screenshot needed:** Error detail view showing a failed sync with the error type and a brief explanation.

### What to do when something fails

1. **Check if it's temporary.** Rate limits and service outages resolve on their own. Wait for the next scheduled sync.
2. **Try reconnecting.** If the error mentions authentication, disconnect the app and reconnect it.
3. **Check the third-party app.** Log into the app directly and verify your account is active, your API access is enabled, and nothing has changed.
4. **Contact support.** If the error persists after reconnecting, reach out to the SaaS company's support team. Give them:
   * Which integration is failing
   * When it started failing
   * The error message (screenshot it if you can)

### Monitoring ongoing syncs

For integrations that sync on a schedule (hourly, daily), you can verify they're running by checking:

* The **last synced** timestamp on the connected app in the widget
* The history log for regular entries at the expected intervals
* Whether new data is appearing as expected in both apps

If the last sync timestamp is older than expected (e.g., a daily sync hasn't run in 3 days), something may be wrong. Check for errors in the history or contact support.

> **Screenshot needed:** Widget showing a connected app with "Last synced: 2 hours ago" timestamp visible.

### What you've learned

* How to read sync status indicators (active, error, paused)
* How to access and interpret execution history
* Common error types and what causes them
* Steps to troubleshoot failed syncs
* When to contact the SaaS company's support team

{% hint style="info" %}
**For SaaS Admins:** If your customers report sync issues, check **Activity → Executions** in your Fastn dashboard. Filter by workflow name or time range. You'll see the full execution detail including status, duration, and triggered-by info, which provides more information than what's visible in the widget.
{% endhint %}
