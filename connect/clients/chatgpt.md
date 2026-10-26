---
description: >-
  Add your Fastn Connect gateway to ChatGPT as a custom connector with
  developer mode, sign in, and use your tools in a chat.
---

# ChatGPT

**You need:** your gateway URL from **Home** (`https://mcp.fastn.dev/<your-org>`) and a ChatGPT plan with developer mode for connectors (Plus, Pro, Business, Enterprise or Edu). On Business and Enterprise, a workspace admin may need to allow custom connectors first.

{% hint style="info" %}
**Building fastn integrations from ChatGPT instead?** That uses a different URL, `https://mcp.fastn.dev/fastn-workspace`. See [ChatGPT under MCP gateway](../../build/mcp-gateway/chatgpt.md).
{% endhint %}

### Add the connector

1. In ChatGPT, open **Settings** → **Apps & Connectors**. Under **Advanced settings**, turn on **Developer mode**.
2. Click **Create** (or **Add custom connector**).
3. Enter a **Name** (for example `Fastn Connect`), paste the gateway URL as the **MCP server URL**, and choose **OAuth** for authentication.
4. Confirm you trust the connector and click **Create**.
5. ChatGPT opens Fastn Connect. Click **Continue with fastn**, sign in with your work account, pick the tools on **Choose what ChatGPT can reach**, and click **Authorize ChatGPT**.

<figure><img src="../../.gitbook/assets/connect-consent.webp" alt="The Fastn Connect consent screen listing apps and tools to tick, with an Authorize button"><figcaption>The same consent screen as every client: pick the tools, then authorise.</figcaption></figure>

ChatGPT's menu names change from time to time. If you cannot find **Developer mode**, check ChatGPT's own help for *custom connectors (MCP)*.

### Use it in a chat

1. In a new chat, open the **+** menu, choose **Developer mode**, and select the connector.
2. Ask for what you need. ChatGPT asks for confirmation before it runs a tool that writes.

### Without OAuth

The **ChatGPT** dialog in Fastn Connect also has a **Bearer token** tab. It applies only if your ChatGPT connector form offers a token or API-key option. If it does, an admin creates an [access key](../agents/README.md#create-an-access-key) for you to paste there. Prefer OAuth for people: each person signs in as themselves, and a key cannot tell two people apart.
