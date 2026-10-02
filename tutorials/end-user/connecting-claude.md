---
description: >-
  Driving your integrations from Claude or another MCP client — what exists
  today, what does not, and the one route that works.
hidden: true
---

# Connecting Claude and Other AI Clients

Everything the widget does — list your connections, run an action against a connected app, check what synced — can also be driven from an AI client over the Model Context Protocol (MCP). Your integrations become tools the client can call.

This page is deliberately explicit about what is and is not available to you as a customer of a SaaS product, because the honest answer has a gap in it.

### The short version

| You want | Today |
| --- | --- |
| A "connect to Claude" button inside the widget | **Not available.** There is no MCP link in the widget. |
| Your integrations as tools in your own Claude | **Possible**, but your SaaS provider has to issue you a scoped API key. |
| Your own agent calling the integrations automatically | **Coming** — the A2A embed method is marked _Coming soon_. |
| Doing it by logging into fastn yourself | **Not the intended path** — the widget exists so you never need a fastn account. |

{% hint style="warning" %}
**There is no MCP link in the widget.** If you are looking for one because a colleague mentioned it, it is not hidden behind a setting — the widget surface for this does not currently exist. The route below is the supported one.
{% endhint %}

### The route that works

fastn runs a hosted MCP gateway:

```
https://mcp.fastn.dev
```

It authenticates with an API key, and an API key can be scoped to **one customer** — you. So the flow is:

1. **You ask your SaaS provider** for an MCP key for your organization, and say which apps and which operations you need.
2. **They mint it** in fastn under Settings → API keys, scoped to your organization only, with the narrowest permission preset that covers what you asked for.
3. **They send it to you** through whatever channel they use for secrets.
4. **You add the gateway** to your client. In Claude Code:

   ```
   claude mcp add --transport http fastn https://mcp.fastn.dev
   ```

   For any other MCP client, point it at the same URL and send the key:

   ```
   Authorization: Bearer fsk_live_<your-key>
   ```

You never sign in to fastn. The key is the whole credential.

If your provider gives you a **test-mode** key (`fsk_test_`), your client must also send `X-fastn-Test-Mode: true` or the gateway refuses the call. If a key appears to do nothing, check that first.

> **Screenshot needed (provider side):** Settings → API keys, the create form with **Customers it can reach** set to _Only the ones I pick_ and the **End user** permission preset selected. Redact the key value and any customer names other than a placeholder.

### What the key does and does not reach

This matters more than the setup, so read it before you ask for one:

* **It is scoped to your organization.** A connection belongs to one customer, so a tool call runs against your credentials and cannot reach another customer of the same provider.
* **It is capped by a permission preset.** Your provider picks one — there is an **End user** preset meant for exactly this — plus a per-resource matrix on top.
* **It can be narrowed to specific actions.** Read-only access to one app, and nothing else, is a configuration your provider can actually make rather than a promise.
* **It acts as you, without asking you.** An AI client holding the key can call anything the key permits, including writes to your connected apps. There is no per-call confirmation at the gateway.
* **It is not a sandbox.** A test-mode key reaches the same live connections as a live key and causes the same real writes.
* **It is attributable.** Everything done with the key appears in your provider's audit log against that key's name, and runs show up in their execution history.

{% hint style="danger" %}
Treat the key like a password for your connected apps. Ask for the narrowest scope that does the job, store it where you would store a database credential, and tell your provider immediately if it leaks so they can revoke it. One key per client, named after that client, makes a revocation cheap.
{% endhint %}

### What is coming

The **A2A** (agent-to-agent) method sits beside Iframe and SDK in the widget's embed options, marked _Coming soon_. Its description:

> A2A will let fastn act as a discoverable agent that other AI agents can authenticate with and invoke — enabling cross-platform automation using Google's Agent-to-Agent protocol.

That is the version of this that will not need a hand-delivered key: your agent authenticates and invokes directly. Until it ships, the scoped-key route above is the one that works.

### If your provider says no

They may well, and it is a reasonable position — handing out a key that can write to live systems is a decision with consequences, and some providers would rather keep that surface inside their own product. Two things worth asking for instead:

* **A narrower key** — read-only, one app, one operation. Much easier to say yes to.
* **The capability inside their product** — if they are already building an AI surface, your integrations can be reached from their backend without a key ever leaving their systems.

### What you can do next

* [Extending a Pre-Built Integration](extending-a-prebuilt-integration.md) — change what an integration does from inside the widget
* [Getting Alerted](getting-alerted.md) — be told when something breaks
