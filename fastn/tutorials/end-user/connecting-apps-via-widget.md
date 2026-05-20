---
description: >-
  Find available integrations, authorize your accounts, and activate connections
  through the embedded integration widget.
---

# Connecting Apps via Widget

The product you use has an integrations section powered by Fastn. This is where you connect your third-party apps your Slack workspace, your Shopify store, your HubSpot account so data can flow between them and the product you're using.

**Prerequisites:** Access to a SaaS product that uses Fastn for integrations. An account on the third-party app you want to connect (e.g., Slack, Shopify, HubSpot).

### Finding the integration widget

The integration widget is embedded somewhere in the product you use. Common locations:

* A dedicated "Integrations" page or tab
* A settings section labeled "Connected Apps" or "Connections"
* A sidebar menu item

The exact location depends on how the SaaS company set things up. If you can't find it, check the product's help docs or ask their support team.

> **Screenshot:** Example of an embedded widget as it appears inside a SaaS product — showing the integration hub with available app icons and connect buttons.

### Connecting an app

1. Open the integration widget in your product.
2. You'll see a list of available integrations — these are the apps the product supports.
3. Find the app you want to connect (e.g., **Slack**).
4. Click **Connect** (the button label may vary — "Connect", "Activate", or "Enable").

> **Screenshot:** Widget showing a list of available integrations with Connect buttons next to each one.

5. A popup opens with the third-party app's authorization screen. This is the app's own login page — not the product's, not Fastn's.
6. Sign in with your account on the third-party app.
7. Review the permissions being requested and click **Authorize** (or **Allow**).
8. The popup closes and you're redirected back to the widget. The app now shows as **Connected**.

> **GIF:** Full connection flow — clicking Connect on an app, the OAuth popup appearing, signing in, authorizing, and seeing the connected status in the widget.

### What happens during authorization

When you click Connect and authorize, you're giving the product permission to access your data on the third-party app. For example:

* Connecting Slack lets the product send messages to your channels or read your channel list
* Connecting Shopify lets the product read your orders, products, or customers
* Connecting HubSpot lets the product read or create contacts in your account

The product can only do what it was set up to do — it can't access anything beyond the specific actions configured by the SaaS company.

Your credentials are stored securely and are isolated from other users. No one else using the same product can see your connections or access your third-party accounts.

### Connecting multiple apps

Some products let you connect multiple apps at once. Each connection is independent — connecting Slack doesn't affect your Shopify connection, and disconnecting one doesn't disconnect others.

If the product supports it, you may also be able to connect multiple accounts of the same app (e.g., two different Slack workspaces). Look for a "Add another connection" option.

### Disconnecting an app

If you want to stop an integration:

1. Open the widget.
2. Find the connected app.
3. Click **Disconnect** (or "Deactivate" / "Remove").
4. The connection is removed. The product can no longer access your data on that app.

Disconnecting removes the stored credentials. If you reconnect later, you'll need to authorize again.

> **Screenshot:** Widget showing a connected app with the Disconnect button visible.

### Troubleshooting

**The Connect button does nothing:** Check if your browser is blocking popups. The authorization screen opens in a popup window — if it's blocked, nothing happens. Allow popups for this site and try again.

**Authorization fails:** Make sure you're signing into the correct account on the third-party app. If you have multiple accounts (e.g., multiple Slack workspaces), verify you're authorizing the right one.

**The app shows "Error" after connecting:** The authorization may have succeeded but the initial setup failed. Try disconnecting and reconnecting. If the error persists, contact the product's support team.

### What you've done

* Found the integration widget in your product
* Connected a third-party app by authorizing your account
* Understand what permissions are granted and how your data is protected
