---
description: "Moving connectors and actions in and out of a workspace as JSON files: importing, exporting actions, and exporting connectors."
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

# Import and export

**Build → Integrations → Connectors** · [Open in Fastn](https://app.fastn.dev/integrations)

You can save connectors and actions to JSON files and load them into another workspace. Use this to:

* **Copy a connector:** copy it between environments.
* **Version control:** keep a copy of the connector's definition in your repository.
* **Share a definition:** give the file to someone else to import.

A file holds definitions only. Connections and their credentials are never exported.

{% hint style="info" %}
**Do this from your AI tool.** Fastn recommends connecting your preferred AI agent, such as Claude, Cursor or VS Code, to the [Fastn MCP server](../mcp-gateway/README.md) and using its tools to create and copy connectors. For example, ask it: *"Copy the Acme CRM connector into a new connector named Acme CRM v2."* To connect your AI agent, see [Connect your AI tool](../mcp-gateway/README.md#open-the-connect-dialog), or the setup guide for [Claude](../mcp-gateway/claude.md), [Claude Code](../mcp-gateway/claude-code.md), [Cursor](../mcp-gateway/cursor.md), [VS Code](../mcp-gateway/vscode.md) or [any other MCP client](../mcp-gateway/README.md#how-your-ai-tool-connects).
{% endhint %}

### Export actions

You can export the actions of any connector, managed or owned.

1. Open the connector's detail page.
2. Either tick the actions you want in the connector rail (or **Select all**) and click **Export** in the *n selected* bar, or open one action's **⋯** menu and click **Export**.
3. The browser downloads a JSON file. A bulk export from the rail is named `<connector-slug>-<n>-actions.json`, for example `hubspot-2-actions.json`. Exporting a single action from its **⋯** menu downloads `<action-slug>.json`.

The file looks like this (shortened):

```json
{
  "$schema": "https://fastn.ai/schemas/actions/v1.json",
  "version": "1.0",
  "exportedAt": "2026-10-08T11:28:39.012Z",
  "connector": { "id": "…", "name": "HubSpot", "slug": "hubspot" },
  "actions": [
    {
      "id": "…",
      "name": "Add List Members",
      "slug": "addListMembers",
      "description": "Add records to a MANUAL list. …",
      "httpConfig": { "…": "method, URL, headers, query parameters, body" },
      "ftpConfig": null,
      "redisConfig": null,
      "authConfig": null,
      "inputContract": { "…": "the Input schema" },
      "outputContract": { "…": "the Output schema" },
      "rateLimit": null,
      "stage": "live",
      "version": "v1.2"
    }
  ]
}
```

| Field | Meaning |
| --- | --- |
| `connector` | The connector the actions came from. |
| `httpConfig` | The request: everything on the Params, Headers, and Body tabs. `ftpConfig` and `redisConfig` hold the equivalent for FTP and REDIS connectors. |
| `authConfig` | The **Stored action setting** from the Auth tab. It is not used at run time. |
| `inputContract` / `outputContract` | The **Input schema** and **Output schema**. |
| `stage` | `test` or `live`. |
| `version` | The action's version. |

### Export connectors

Connectors your workspace owns (badged `Custom`) have a **⋯** menu on their catalog card with **Select**, **Edit**, **Export**, and **Delete**.

* **⋯ → Export** downloads that one connector as `<slug>-bundle.json`.
* **⋯ → Select** ticks the card and adds **Export Selected (n)** to the page header. Select more cards, then click it to download them together.
* On the connector's detail page, its row in the rail also has a **⋯** menu with **Export All** and **Import**.

**Export Selected (n)** downloads a file named `connectors-bundle-<date>.json`, for example `connectors-bundle-2026-10-08.json`:

```json
{
  "$schema": "https://fastn.ai/schemas/connector-bundle/v1.json",
  "version": "1.0",
  "exportedAt": "2026-10-08T11:56:56.422Z",
  "connectors": [
    {
      "connector": { "name": "Docs Demo CRM", "slug": "docsDemoCrm", "protocol": "REST", "visibility": "private", "authMethods": [], "…": "…" },
      "actions": [ { "name": "List Users", "slug": "listUsers", "httpConfig": { "method": "GET", "url": "https://jsonplaceholder.typicode.com/users" }, "…": "…" } ],
      "webhookConfigs": [],
      "authProviders": [],
      "appRegistrations": []
    }
  ]
}
```

A single-connector `<slug>-bundle.json` is flat: `connector`, `actions`, `webhookConfigs`, `authProviders`, and `appRegistrations` sit at the top level, with no `connectors` array.

Each entry carries the connector's definition, its actions, its webhook configs, its auth providers, and its app registrations. Connections are never included. Managed connectors do not have this menu; to copy one of their actions, use [Export actions](#export-actions).

{% hint style="warning" %}
If the connector has its own OAuth app, the file carries it in `authProviders`. Open the file and check those entries before you share it.
{% endhint %}

### Import

**Create connector → Import from file** on the catalog page opens a file picker (if your role cannot create connectors, the page shows an **Import** button instead). Choose one `.json` file, such as a `connectors-bundle-<date>.json` from [Export connectors](#export-connectors). There is no form to fill in: the file is read and its connectors are created in your workspace as connectors you own.

If a connector in the file already exists in your workspace, Fastn asks first:

> **Replace existing connector?**
>
> *&lt;name&gt;* already exists. Importing will replace its actions and configuration. Saved connections are preserved.

**Replace** overwrites the existing connector's actions and configuration with the file's. Connections on it are kept, so customers do not need to reconnect. **Cancel** stops the import.
