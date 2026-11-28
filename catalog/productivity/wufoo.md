---
description: "Wufoo is an online form builder. Read forms, fields, entry counts and reports, and create and delete form webhooks."
hidden: true
---

# Wufoo

<img src="../../.gitbook/assets/connectors/lg/wufoo.png" alt="Wufoo logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Authentication** | Subdomain and API key |
| **Slug** | `wufoo` |

## Setup

Your customers enter their subdomain and api key for Wufoo when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Wufoo from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Wufoo**.
2. Select **Connect** on the Wufoo card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Wufoo's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Form Webhook</td><td><code>createFormWebhook</code></td><td>Registers a webhook on a Wufoo form so that each new entry is POSTed to your endpoint. The WebHook API is a paid-plan feature: accounts without it receive HTTP 402 Payment Required.</td></tr><tr><td>Delete Form Webhook</td><td><code>deleteFormWebhook</code></td><td>Removes a previously registered webhook from a Wufoo form, identified by the hash returned when it was created.</td></tr><tr><td>Get API Key By Login</td><td><code>getApiKeyByLogin</code></td><td>Exchanges a Wufoo username, password and integration key for that account's API key. Intended for applications that onboard Wufoo users without asking them to copy their key by hand.</td></tr><tr><td>Get Form</td><td><code>getForm</code></td><td>Retrieves a single Wufoo form by its hashed identifier or URL title, returning its name, description, settings and entry links.</td></tr><tr><td>Get Form Comment Count</td><td><code>getFormCommentCount</code></td><td>Retrieves the total number of comments left on a Wufoo form's entries.</td></tr><tr><td>Get Form Entry Count</td><td><code>getFormEntryCount</code></td><td>Retrieves the total number of entries submitted to a Wufoo form.</td></tr><tr><td>Get Form Fields</td><td><code>getFormFields</code></td><td>Retrieves the field definitions of a Wufoo form, including each field's identifier, label, type, requiredness and available choices. Use the returned field identifiers as the keys when submitting an entry.</td></tr><tr><td>Get Report</td><td><code>getReport</code></td><td>Retrieves a single Wufoo report by its hashed identifier or URL title.</td></tr><tr><td>Get Report Entry Count</td><td><code>getReportEntryCount</code></td><td>Retrieves the total number of entries included in a Wufoo report.</td></tr><tr><td>Get Report Fields</td><td><code>getReportFields</code></td><td>Retrieves the field definitions backing a Wufoo report, describing the columns its entries contain.</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Form Comments</td><td><code>listFormComments</code></td><td>Retrieves the comments left on a Wufoo form's entries, optionally narrowed to a single entry.</td></tr><tr><td>List Form Entries</td><td><code>listFormEntries</code></td><td>Retrieves the entries submitted to a Wufoo form, with optional sorting and column filtering. Entry keys are the form's field identifiers, so pair this with Get Form Fields to interpret the values.</td></tr><tr><td>List Forms</td><td><code>listForms</code></td><td>Retrieves every form in the Wufoo account the API key belongs to, including each form's name, description, settings and hashed identifier.</td></tr><tr><td>List Report Entries</td><td><code>listReportEntries</code></td><td>Retrieves the entries included in a Wufoo report, after the report's own filters have been applied.</td></tr><tr><td>List Report Widgets</td><td><code>listReportWidgets</code></td><td>Retrieves the widgets that make up a Wufoo report, such as charts, graphs and number totals, along with their type and size.</td></tr><tr><td>List Reports</td><td><code>listReports</code></td><td>Retrieves every report in the Wufoo account, including each report's name, description and hashed identifier.</td></tr><tr><td>List Users</td><td><code>listUsers</code></td><td>Retrieves every user on the Wufoo account, including their username, email address, role and administrative permissions.</td></tr><tr><td>Submit Form Entry</td><td><code>submitFormEntry</code></td><td>Submits a new entry to a Wufoo form. Supply the values as form-encoded field identifiers such as Field1 and Field2, which you can discover with Get Form Fields. Wufoo runs the form's own validation and returns per-field errors when it rejects the submission. Note that a successful submission fires the form's configured email notifications.</td></tr></tbody></table>

</details>

