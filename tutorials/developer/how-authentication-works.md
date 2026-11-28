---
description: Every credential Fastn uses, where each one lives, and how a call names the customer it acts for.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# How authentication works

Fastn uses a few credentials, each held by a different party. Your API key stays on your backend, the browser only gets a short-lived token, and Fastn keeps your customers' app sign-ins. That way, a leaked page or a compromised browser can't reach your account or another customer's data.

<figure><img src="../../.gitbook/assets/diagrams/auth-flow.svg" alt="How authentication works: your backend mints an embed token from Fastn with your API key, passes only the token to your frontend, which opens the widget; the customer signs in to their app and Fastn saves the credential."><figcaption><p>Your API key stays on your backend. Only the short-lived token reaches the browser.</p></figcaption></figure>

1. Your backend calls Fastn with your **API key** and names the customer in `x-org-id`.
2. Fastn returns an **embed token** for that one customer. It lasts 8 hours.
3. Your backend passes only the token to your frontend.
4. Your frontend opens the widget with the token.
5. The customer signs in to their own app in the widget.
6. Fastn stores that **connection's credential**, encrypted and scoped to that customer.

### The credentials

| Credential | Where it lives | What it does | Details |
| --- | --- | --- | --- |
| **API key** (`fsk_test_…`, `fsk_live_…`) | Your backend only | Authenticates every call your backend makes to Fastn | [API keys](../../manage/api-keys.md) |
| **Identity secret** | Your backend only | Signs `x-org-id` and `x-user-id` as `x-identity-hmac`, so a call can't claim to be another customer | [Verify caller identity](../../manage/identity-verification.md) |
| **Embed token** | Your frontend, one page load | Opens the widget for one customer and user. Expires after 8 hours; refresh is capped at 7 days per session | [Generate embed tokens](generating-embed-tokens.md) |
| **Connection credential** | Fastn, encrypted | One customer's sign-in to one app. Every run for that customer reuses it | [Connections](../../build/connections/README.md) |
| **MCP sign-in** | Your AI tool | Connects your AI tool to the Fastn MCP server. You sign in to Fastn; no API key is needed | [Fastn MCP server](../../build/mcp-gateway/README.md) |
| **Customer MCP URL** | Your customer's AI tool | A one-time URL, valid for 10 minutes, that connects a customer's AI tool as that customer | [Customer MCP URL](../../embed/embedding/customer-mcp-url.md) |

### How a call names the customer

A call acts for one of your customers when it sends `x-org-id`: your own id for the customer (its **External ID**), or Fastn's id for it. Leave it out to act as your own organization.

A key can reach every customer or only the ones you pick. A backend that serves many customers uses a key that reaches every customer, and names one in each call. See [Find your org identifier](finding-your-org-identifier.md) and [Scoping a call to a customer](../../reference/api.md#scoping-a-call-to-a-customer).

### Test and Live keys

Every API key has a mode, shown in its prefix:

| Mode | Prefix | Runs | Extra header |
| --- | --- | --- | --- |
| **Test** | `fsk_test_` | The latest published version of each workflow | `X-fastn-Test-Mode: true`, or the call is refused with `403` |
| **Live** | `fsk_live_` | The version deployed to the one environment the key is pinned to | None |

The mode decides which version of your workflows runs, not which data they touch.

{% hint style="danger" %}
Neither mode is a sandbox. A Test key reaches the same live connections as a Live key and causes the same real writes in your customers' apps. To test without touching real data, run the workflow with **Fully Mock** in the editor.
{% endhint %}

### Environments

An environment is a stage your workflows deploy to. Test and Live are built in, and you can add others, such as staging. A Live key is pinned to one environment when you create it, and runs what's deployed there. It can also send `x-fastn-env: test` to run the latest published version. See [Environments and GitHub](../../manage/environments.md).

### What's next

* [Set up authentication](set-up-authentication.md): create a key and make your first authenticated request.
* [Which header carries the key](../../reference/api.md#which-header-carries-the-key): the headers each endpoint accepts.
