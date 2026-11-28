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

## Connect in Fastn

Your customers connect Formilla from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Formilla**.
2. Select **Connect** on the Formilla card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Formilla's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Event</td><td><code>createEvent</code></td><td>Records a customer event (for example 'Placed Order') against a Formilla contact, so message campaigns can be triggered on what a customer did rather than only on who they are. Supply your App ID and the event name, and identify the contact with UserId, Email, or both. Formilla allows up to 100 distinct event names per account and event names cannot be removed through the API, so use a stable set of names. When identity verification is enabled on your Formilla account, also supply a valid ContactHmac; an invalid one is rejected with HTTP 403.</td></tr><tr><td>Create or Update Contact</td><td><code>createOrUpdateContact</code></td><td>Creates a new Formilla contact or updates an existing one. You must supply UserId, Email, or both. When both are given, Formilla matches on UserId first and falls back to Email; if no contact matches, a new one is created. This is a full overwrite: every field you send replaces the value already stored on a matching contact, so send the complete record rather than a partial one.</td></tr></tbody></table>

