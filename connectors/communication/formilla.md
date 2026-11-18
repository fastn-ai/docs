---
description: "Formilla is a live chat, chatbot and customer messaging platform."
hidden: true
---

# Formilla

<img src="../../.gitbook/assets/connectors/formilla.png" alt="Formilla logo" width="64">

Formilla is a live chat, chatbot and customer messaging platform. This connector wraps the Formilla REST API, which pushes customer data from your own systems into Formilla so you can target automatic email and in-app messages on that data. It covers creating or updating a contact with custom attributes, and recording a customer event against a contact.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [formilla.com](https://formilla.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `formilla` |

## Use it

Add Formilla from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.formilla.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Event | `createEvent` | Records a customer event (for example 'Placed Order') against a Formilla contact, so message campaigns can be triggered on what a customer did rather than only on who they are. Supply your App ID and the event name, and identify the contact with UserId, Email, or both. Formilla allows up to 100 distinct event names per account and event names cannot be removed through the API, so use a stable set of names. When identity verification is enabled on your Formilla account, also supply a valid ContactHmac; an invalid one is rejected with HTTP 403. Returns HTTP 200 with an empty body on success. |
| Create or Update Contact | `createOrUpdateContact` | Creates a new Formilla contact or updates an existing one. You must supply UserId, Email, or both. When both are given, Formilla matches on UserId first and falls back to Email; if no contact matches, a new one is created. This is a full overwrite: every field you send replaces the value already stored on a matching contact, so send the complete record rather than a partial one. Returns HTTP 200 with an empty body on success. |
