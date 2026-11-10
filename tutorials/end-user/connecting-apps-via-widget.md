---
description: >-
  Find an integration in the embedded widget, sign in to your account on the
  app, and manage or remove what you set up.
---

# Connecting Apps via Widget

The product you use has an integrations section powered by fastn. This is where you connect your other apps - your Slack workspace, your Shopify store, your HubSpot account - so data can move between them and the product.

**Prerequisites:** Access to a SaaS product that uses fastn for integrations. An account on the app you want to connect (for example Slack, Shopify or HubSpot).

### Finding the integration widget

The widget is embedded somewhere in the product you use. Common locations:

* A dedicated "Integrations" page or tab
* A settings section labeled "Connected Apps" or "Connections"
* A sidebar menu item

The exact location depends on how the SaaS company set things up. If you can't find it, check the product's help docs or ask their support team.

### What the widget shows

The widget is a list of the integrations the product offers:

* A **Search integrations** box at the top filters the list by name - useful when many apps are available.
* Each integration shows a short status line under its name (see below) and a **Connect** button, or **Manage** once you've set it up.
* The **⋯** menu in the widget header holds **Insights** (activity, health and alerts) and, unless the product turned it off, **Generate MCP URL** for [connecting Claude](connecting-claude.md).
* Workflows live inside each integration: open an integration to see its **Workflows** list.
* If the product offers it, a round sparkle button at the bottom right (**Ask the assistant**) opens the AI assistant.

{% hint style="warning" %}
What you see can vary: the SaaS company decides which integrations, menu items and sections their widget shows.
{% endhint %}

### Reading an integration's status

The line under each integration's name tells you where it stands:

| Status | Meaning |
| --- | --- |
| **Not connected** | You haven't set this integration up yet. |
| **Connected** | Set up, and every account it needs is signed in. |
| **N setups** | You have more than one setup of this integration, all connected. |
| **N of M connected** | Set up, but some of the accounts it needs are not signed in yet (for example "1 of 2 connected"). |
| **Setup incomplete** | A setup exists but isn't finished. |
| **Status unavailable** | The widget couldn't load your connection status right now. Try again later. |
| **Waiting for your account to be set up** | The product hasn't finished preparing your account yet. If it persists, contact the product's support team. |

### Connecting an app

1. Open the integration widget in your product.
2. Find the app you want, by scrolling or by typing in **Search integrations**.
3. Click **Connect**. A setup wizard opens and walks you through each account the integration needs.
4. When you connect an account, a popup opens with the app's own sign-in screen - the app's login page, not the product's and not fastn's.
5. Sign in with your account on that app.
6. Review the permissions being requested and approve them. The button wording is the app's own, for example Authorize or Allow.
7. The popup closes and you're back in the wizard. When setup finishes, the integration's detail view opens, and in the list its button now reads **Manage**. When every account it needs is signed in, its status reads **Connected**.

### What happens during authorization

When you authorize, you're giving the product permission to access your data on that app. For example:

* Connecting Slack lets the product send messages to your channels or read your channel list
* Connecting Shopify lets the product read your orders, products or customers
* Connecting HubSpot lets the product read or create contacts in your account

The product can only do what it was set up to do - it can't access anything beyond the specific actions the SaaS company configured.

Your credentials are stored securely and are isolated from other customers. No one at another company using the same product can see your connections or access your accounts.

### Managing an integration

Click **Manage** on an integration you've set up. The detail view lists your setups (installations) and the integration's **Workflows**. On each installation, click **View** to expand it and see its accounts, its **Configuration** row (see [Customizing Your Integrations](customizing-your-integrations.md)) and, where the product offers it, its **Triggers** row.

### Adding another setup or account

Each connection is independent: connecting Slack doesn't affect your Shopify connection, and removing one doesn't remove the others.

* **Another setup of the same integration:** open the integration and click **New installation**. This button appears only when the integration allows more than one setup; many allow just one.
* **A different account on the same app** (for example a second Slack workspace): each setup holds one account per app. Remove the current account with **Delete connection**, then click that app's **Connect** button in the setup to sign in with the other account. To keep both accounts, add another setup with **New installation**, where the integration allows it.

### Removing an integration

1. Open the widget and click **Manage** on the integration.
2. On the installation you want to remove, click the trash icon (**Delete installation**). It is on the installation's header, so you don't need to expand it with **View** first.
3. Confirm **Delete installation** in the dialog.

This removes that installation and its configuration. Your signed-in accounts usually stay; only for some apps does the product remove the account too, and in that case the dialog warns you that anything using that connection stops working until someone reconnects it.

A signed-in account is a separate connection. To remove one, use **Delete connection** next to the account in the installation. If you connect it again later, you'll need to authorize again.

### Troubleshooting

**The sign-in popup doesn't appear:** The sign-in screen opens in a popup window. If your browser blocks it, the widget falls back to opening the sign-in page in the same tab and returns you to the wizard afterwards. If neither happens, allow popups for this site and try again.

**Authorization fails:** Make sure you're signing in to the correct account on the app. If you have several (for example multiple Slack workspaces), check you're authorizing the right one.

**The status doesn't say "Connected" after you authorize:** Read the status line. **N of M connected** or **Setup incomplete** means an account or step is still missing: click **Manage** and finish connecting every account. **Status unavailable** means the widget couldn't load the status; try again later. If it stays wrong, contact the product's support team.

### What you've done

* Found the integration widget in your product
* Connected an app by authorizing your account
* Learned how to read an integration's status and where to manage or remove it
* Understand what permissions are granted and how your data is protected
