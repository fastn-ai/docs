---
description: >-
  Reaching your integrations from Claude or another MCP client — the share-link
  route that needs no fastn account, and what to do without one.
hidden: true
---

# Connecting Claude and Other AI Clients

Everything the widget does — list your connections, run an action against a connected app, check what synced — can also be driven from an AI client over the Model Context Protocol (MCP). Your integrations become tools the client can call.

Which route you have depends on how your SaaS provider gave you the widget.

### The short version

| How you reached the widget | Route |
| --- | --- |
| **A share link** your provider sent you | **Copy MCP URL** in the widget's **⋯** menu. No fastn account. |
| **Embedded in their product** (iframe or SDK) | No menu item. Your provider issues you a scoped API key instead. |
| **Your own agent calling in automatically** | **A2A**, marked _Coming soon_ in the widget's embed options. |

### If you opened the widget from a share link

This is the simple path, and it needs nothing from you but a paste.

1. In the widget header, open the **⋯** menu.
2. Click **Copy MCP URL**. The item confirms with **Copied**.
3. Paste that URL into your AI client as a custom MCP connector. In Claude Code:

   ```
   claude mcp add --transport http fastn <the URL you copied>
   ```

   In Claude, add it as a custom connector and paste the URL when asked.

That is the whole setup. **You never sign in to fastn** — the share link itself is what Claude connects with, and it carries your organization's scope.

{% hint style="info" %}
**Copy the URL, do not try to build it.** It identifies your specific link, and the host differs by environment. Always take it from the menu.
{% endhint %}

Two consequences worth knowing:

* **Revoking the link turns the connection off.** If your provider revokes or replaces the share link, the MCP URL stops working with it. That is the intended kill switch — ask for a fresh link and re-add it.
* **Your provider can hide the item.** It is on unless they switch it off (Widget Builder → Features → **Copy MCP URL**).

#### No Copy MCP URL in the menu?

Three possible reasons, in order of likelihood:

1. **You did not open the widget from a share link.** Embedded iframe and SDK sessions do not get the item, by design — the link is the credential, and there isn't one. Use the key route below.
2. **Your provider switched it off** on the widget's Features tab.
3. **Their fastn version predates the feature.** Ask them; it is recent.

### If you are inside their product instead

No menu item, so the route is a key your provider mints for you:

1. **Ask your provider** for an MCP key for your organization, naming the apps and operations you need.
2. **They mint it** under Settings → API keys, scoped to your organization only, on the narrowest permission preset that covers the ask — there is an **End user** preset meant for this.
3. **They send you the key and the gateway URL** to point your client at. It is the same hosted gateway they use themselves — their dashboard has a **Connect an agent** dialog that shows the URL and a one-click **Add to Claude**, so they can copy both from there.
4. **You add it** to your client, sending the key as a bearer token:

   ```
   Authorization: Bearer fsk_live_<your-key>
   ```

If they give you a **test-mode** key (`fsk_test_`), your client must also send `X-fastn-Test-Mode: true` or the gateway refuses the call. If a key appears to do nothing, check that first.

### What the connection reaches, and what it does not

Read this before you ask for either route:

* **It is scoped to your organization.** A connection belongs to one customer, so a tool call runs against your credentials and cannot reach another customer of the same provider.
* **It is capped by a permission preset**, plus a per-resource matrix on top, and can be narrowed to specific actions. Read-only access to one app and nothing else is a configuration your provider can actually make rather than a promise.
* **It acts as you, without asking.** A client holding the credential can call anything it permits, including writes to your connected apps. There is no per-call confirmation at the gateway.
* **It is not a sandbox.** A test key reaches the same live connections as a live key and causes the same real writes.
* **It is attributable.** Calls appear in your provider's audit log and runs show up in their execution history.

{% hint style="danger" %}
Treat either credential like a password for your connected apps. With a key, ask for the narrowest scope that does the job, store it where you would store a database credential, and tell your provider immediately if it leaks so they can revoke it. With a share link, the link itself is the credential — do not forward it.
{% endhint %}

### What is coming

The **A2A** (agent-to-agent) method sits beside Iframe and SDK in the widget's embed options, marked _Coming soon_:

> A2A will let fastn act as a discoverable agent that other AI agents can authenticate with and invoke — enabling cross-platform automation using Google's Agent-to-Agent protocol.

That is the version where your agent authenticates and invokes directly, with no URL or key passed by hand.

### What you can do next

* [Extending a Pre-Built Integration](extending-a-prebuilt-integration.md) — change what an integration does from inside the widget
* [Getting Alerted](getting-alerted.md) — be told when something breaks
