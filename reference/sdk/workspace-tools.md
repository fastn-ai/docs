---
description: "The optional route: list and run the MCP tools your fastn workspace has turned on, with ToolsClient."
---

# Workspace tools

You do not need this page for the flows in the rest of this section. It is an optional second route: if your app or AI agent works with **tools by name** (as an MCP client does), `ToolsClient` lists and runs the tools your fastn workspace has turned on, with the customer set on each call. See [MCP gateway](../../build/mcp-gateway/README.md) for what a workspace exposes.

```typescript
import { ToolsClient, ToolError } from "@fastn-ai/sdk";

const tools = new ToolsClient({
  key: process.env.FASTN_TOOLS_KEY!,
  url: "https://mcp.fastn.dev/your-workspace",
});

const all = await tools.tools();                       // every tool, with its input schema
const calendar = await tools.toolsOf("googleCalendar"); // one app's tools

const r = await tools.customer("acme_customer_42").call("googleCalendar__listCalendars", {});
console.log(r.data);                                    // the tool's answer, JSON-decoded
```

You can also give `FastnClient` a `tools: { key, url }` option. Then `fastn.tools` is a `ToolsClient`, and `fastn.customer(ref).tools` is the same client set to that customer.

{% hint style="info" %}
The workspace key is a different credential from your fastn platform API key. Keep both in your secret store.
{% endhint %}

### ToolsClient

| Option | Required | Meaning |
| ------ | -------- | ------- |
| `key` | Yes | The workspace key. Sent as `Authorization: Bearer`. |
| `url` | Yes | The workspace endpoint. |
| `timeoutMs` | No | Time limit per call. Default 120000 (tools can be slow). |
| `defaults` | No | Options for every call, for example `{ customer: { ref: "acme_customer_42" } }`. |

| Method | Answer |
| ------ | ------ |
| `tools()` | Every tool: `[ { name, title, description, inputSchema, annotations } ]`. Tool names look like `<app>__<action>`. |
| `toolsOf(app)` | The tools of one app. |
| `customer(ref)` | The same client, sending `X-Org-Id: ref` on every call. |
| `call(name, args, opts?)` | `{ data, text, content, structuredContent, isError }`. `data` is the answer JSON-decoded when it parses; `text` is the raw text. |
| `rpc(method, params)` | A raw JSON-RPC call, for methods the client does not wrap. |

Per-call options: `customer`, `userId` (sent as `X-User-Id`, when the workspace runs calls as each person), `headers`, `timeoutMs`, `signal`, `retries` (default `0`, because the SDK cannot know whether a tool is safe to repeat; turn it on for reads).

### ToolError

Failures throw `ToolError`.

| `kind` | Means |
| ------ | ----- |
| `http` | The gateway answered with a non-2xx status, for example `401` for a wrong key. |
| `rpc` | A JSON-RPC error, for example an unknown tool. |
| `tool` | The tool ran and answered with an error. |
| `auth` | The app behind the tool is not connected for this customer yet. |

Other fields: `status`, `code`, `tool`, `body`, and the shortcuts `isAuth`, `isUnknownTool` and `isConnectionRequired`. For kind `auth`, `isConnectionRequired` is `true`, `authorizeUrl` is where to send the customer to connect, and `connector` names the app.

```typescript
import { ToolError } from "@fastn-ai/sdk";

try {
  await tools.customer("acme_customer_42").call("hubspot__getContact", { contactId: "51234567890" });
} catch (e) {
  if (e instanceof ToolError && e.isConnectionRequired) {
    console.log("ask the customer to connect", e.connector, "at", e.authorizeUrl);
  } else {
    throw e;
  }
}
```
