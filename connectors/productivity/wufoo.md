---
description: "Wufoo is an online form builder for collecting submissions, payments and survey responses."
---

# Wufoo

Wufoo is an online form builder for collecting submissions, payments and survey responses. This connector covers the Wufoo REST API v3: listing and retrieving forms and their field definitions, reading and submitting form entries, entry counts, entry comments and comment counts, reports with their entries, fields and widgets, account users, the login endpoint that exchanges account details for an API key, and the WebHook API for registering and removing per-form webhook subscriptions.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Authentication** | Credentials you enter |
| **Actions** | 18 |
| **Events** | 0 |
| **Slug** | `wufoo` |

## Use it

Add Wufoo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.wufoo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Form Webhook | `createFormWebhook` | Registers a webhook on a Wufoo form so that each new entry is POSTed to your endpoint. The WebHook API is a paid-plan feature: accounts without it receive HTTP 402 Payment Required. |
| Delete Form Webhook | `deleteFormWebhook` | Removes a previously registered webhook from a Wufoo form, identified by the hash returned when it was created. |
| Get API Key By Login | `getApiKeyByLogin` | Exchanges a Wufoo username, password and integration key for that account's API key. Intended for applications that onboard Wufoo users without asking them to copy their key by hand. |
| Get Form | `getForm` | Retrieves a single Wufoo form by its hashed identifier or URL title, returning its name, description, settings and entry links. |
| Get Form Comment Count | `getFormCommentCount` | Retrieves the total number of comments left on a Wufoo form's entries. |
| Get Form Entry Count | `getFormEntryCount` | Retrieves the total number of entries submitted to a Wufoo form. |
| Get Form Fields | `getFormFields` | Retrieves the field definitions of a Wufoo form, including each field's identifier, label, type, requiredness and available choices. Use the returned field identifiers as the keys when submitting an entry. |
| Get Report | `getReport` | Retrieves a single Wufoo report by its hashed identifier or URL title. |
| Get Report Entry Count | `getReportEntryCount` | Retrieves the total number of entries included in a Wufoo report. |
| Get Report Fields | `getReportFields` | Retrieves the field definitions backing a Wufoo report, describing the columns its entries contain. |
| List Form Comments | `listFormComments` | Retrieves the comments left on a Wufoo form's entries, optionally narrowed to a single entry. |
| List Form Entries | `listFormEntries` | Retrieves the entries submitted to a Wufoo form, with optional sorting and column filtering. Entry keys are the form's field identifiers, so pair this with Get Form Fields to interpret the values. |
| List Forms | `listForms` | Retrieves every form in the Wufoo account the API key belongs to, including each form's name, description, settings and hashed identifier. |
| List Report Entries | `listReportEntries` | Retrieves the entries included in a Wufoo report, after the report's own filters have been applied. |
| List Report Widgets | `listReportWidgets` | Retrieves the widgets that make up a Wufoo report, such as charts, graphs and number totals, along with their type and size. |
| List Reports | `listReports` | Retrieves every report in the Wufoo account, including each report's name, description and hashed identifier. |
| List Users | `listUsers` | Retrieves every user on the Wufoo account, including their username, email address, role and administrative permissions. |
| Submit Form Entry | `submitFormEntry` | Submits a new entry to a Wufoo form. Supply the values as form-encoded field identifiers such as Field1 and Field2, which you can discover with Get Form Fields. Wufoo runs the form's own validation and returns per-field errors when it rejects the submission. Note that a successful submission fires the form's configured email notifications. |
