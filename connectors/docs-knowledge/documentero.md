---
description: "Documentero Cloud API - generate Word/Excel/PDF documents from templates, list account document templates, and validate API credentials."
hidden: true
---

# Documentero

<img src="../../.gitbook/assets/connectors/lg/documentero.png" alt="Documentero logo">

Base https://app.documentero.com/api.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [documentero.com](https://documentero.com) |
| **Authentication** | API key |
| **Slug** | `documentero` |

## Use it

Add Documentero from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.documentero.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate Document</td><td><code>generateDocument</code></td><td>Generates a document from a Documentero template and returns an expirable (~1 hour) signed download link. POST /api/generate. Pass 'document' (template identifier from List Templates) and 'data' (an object whose keys match the template's placeholder fields; use \n for line breaks). Optional 'format' ("docx" or "pdf", default inherited from the template setting) and the email* fields, which e-mail the generated document to real recipients as an attachment. Always assert message == "Document Generated Successfully" and that data holds a URL: Documentero's docs state some data errors are returned with HTTP 200 plus an error string in "message" (observed failures - missing document field, unknown template - return a real HTTP 400). Consumes one document from the account quota.</td></tr><tr><td>List Templates</td><td><code>listTemplates</code></td><td>Lists every document template in the Documentero account. GET /api/templates. Returns {status:200, data:[{label:"&lt;template name&gt;", value:"&lt;template identifier&gt;"}]}. The "value" field is the template identifier to pass as "document" to Generate Document.</td></tr><tr><td>Validate API Key</td><td><code>validateApiKey</code></td><td>Validates the stored Documentero API key and returns the account name. GET /api/me. Returns {status:200, message:"Valid API Key", name:"&lt;account&gt;"}. An invalid key returns HTTP 400 with message "Invalid apiKey". Use this as a connection health check.</td></tr></tbody></table>
