---
description: "Formilla is a live chat and customer messaging platform. Create or update contacts and record contact events."
hidden: true
---

# Formilla

<img src="../../.gitbook/assets/connectors/lg/formilla.png" alt="Formilla logo">

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [formilla.com](https://formilla.com) |
| **Authentication** | API key |
| **Slug** | `formilla` |

## Setup

Your customers enter their API key for Formilla when they connect. Nothing else needs setting up.

## Use it

Add Formilla from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.formilla.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Event</td><td><code>createEvent</code></td><td>Records a customer event (for example 'Placed Order') against a Formilla contact, so message campaigns can be triggered on what a customer did rather than only on who they are. Supply your App ID and the event name, and identify the contact with UserId, Email, or both. Formilla allows up to 100 distinct event names per account and event names cannot be removed through the API, so use a stable set of names. When identity verification is enabled on your Formilla account, also supply a valid ContactHmac; an invalid one is rejected with HTTP 403.</td></tr><tr><td>Create or Update Contact</td><td><code>createOrUpdateContact</code></td><td>Creates a new Formilla contact or updates an existing one. You must supply UserId, Email, or both. When both are given, Formilla matches on UserId first and falls back to Email; if no contact matches, a new one is created. This is a full overwrite: every field you send replaces the value already stored on a matching contact, so send the complete record rather than a partial one.</td></tr></tbody></table>

## Events

Formilla has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
