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
| `customerArg` | No | Default `true`: a call scoped to a customer fills `endOrgRef` into every Fastn Workspace tool whose input schema takes it, so the customer is named once; `orgId` in the arguments is passed to a Fastn Workspace tool that spells the customer `endOrgId` or `end_org_id` under that spelling, so you write `orgId` everywhere; and Fastn Workspace answers come back without fastn's internal customer id keys (`endOrgId`, `end_org_id`), so the only customer id you see is yours (`r.text` keeps the raw answer). `false` turns all three off. |

| Method | Answer |
| ------ | ------ |
| `tools()` | Every tool: `[ { name, title, description, inputSchema, annotations } ]`. Tool names look like `<app>__<action>`. |
| `toolsOf(app)` | The tools of one app. |
| `customer(ref)` | The same client, sending `X-Org-Id: ref` on every call and filling `endOrgRef: ref` into the Fastn Workspace tools that take it (the unified record tools). The tool schemas come from one `tools()` listing per workspace, shared by every `customer()` client; after 10 minutes a call still goes out at once with the cached schemas and one refresh runs in the background. Call `tools()` once at startup if the first call must not pay for the listing. A call is never sent without the customer on a guess: when the listing fails or comes back empty, the call throws that error (and the next call lists again); a `fastnPlatform__*` tool missing from the cached map triggers one fresh listing, then an unknown-tool `ToolError`. An `endOrgRef` or `endOrgId` you pass yourself wins. |
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

Other fields: `status`, `code`, `tool`, `body`, and the shortcuts `isAuth`, `isUnknownTool` and `isConnectionRequired`.

{% hint style="warning" %}
Today the gateway reports an app refusal (a record id that does not exist, a value the app rejects) as a tool error whose message is only `error code: 502`, the same text as a real upstream hiccup. The app's own message is on its way (platform ticket KAT-8586). Until then: a 502 that comes back again after one retry is the app refusing the request, so check the id or the value rather than retrying further.
{% endhint %} For kind `auth`, `isConnectionRequired` is `true`, `authorizeUrl` is where to send the customer to connect, and `connector` names the app.

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
