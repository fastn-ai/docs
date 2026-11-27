---
description: "Documentero creates Word, Excel and PDF documents from templates. List templates and generate documents."
hidden: true
---

# Documentero

<img src="../../.gitbook/assets/connectors/lg/documentero.png" alt="Documentero logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [documentero.com](https://documentero.com) |
| **Authentication** | API key |
| **Slug** | `documentero` |

## Setup

Your customers enter their API key for Documentero when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Documentero from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Documentero**.
2. Select **Connect** on the Documentero card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Documentero's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate Document</td><td><code>generateDocument</code></td><td>Generates a document from a Documentero template and returns an expirable (~1 hour) signed download link. Pass 'document' (template identifier from List Templates) and 'data' (an object whose keys match the template's placeholder fields; use \n for line breaks). Optional 'format' ("docx" or "pdf", default inherited from the template setting) and the email* fields, which e-mail the generated document to real recipients as an attachment. Always assert message == "Document Generated Successfully" and that data holds a URL: Documentero's docs state some data errors are returned with HTTP 200 plus an error string in "message" (observed failures - missing document field, unknown template - return a real HTTP 400). Consumes one document from the account quota.</td></tr><tr><td>List Templates</td><td><code>listTemplates</code></td><td>Lists every document template in the Documentero account. Returns {status:200, data:[{label:"&lt;template name&gt;", value:"&lt;template identifier&gt;"}]}. The "value" field is the template identifier to pass as "document" to Generate Document.</td></tr><tr><td>Validate API Key</td><td><code>validateApiKey</code></td><td>Validates the stored Documentero API key and returns the account name. Returns {status:200, message:"Valid API Key", name:"&lt;account&gt;"}. An invalid key Use this as a connection health check.</td></tr></tbody></table>

