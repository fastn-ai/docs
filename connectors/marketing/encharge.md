---
description: "Encharge marketing automation — manage people, segments, tags, custom person fields, webhooks (event subscriptions), send transactional emails, and ingest…"
hidden: true
---

# Encharge

<img src="../../.gitbook/assets/connectors/lg/encharge.png" alt="Encharge logo">

Encharge marketing automation — manage people, segments, tags, custom person fields, webhooks (event subscriptions), send transactional emails, and ingest events/identify/alias/group objects.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [encharge.io](https://encharge.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `encharge` |

## Use it

Add Encharge from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.encharge.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Tag | `addTag` | Add one or more comma-separated tags to an existing person, identified by email, userId, or Encharge id. |
| Alias Person | `aliasPerson` | Change the userId and/or email of a person via the Encharge Ingest API 'alias' event. |
| Archive or Delete People | `archivePeople` | Archive (default) or permanently delete one or more people by email, userId, or id. Set force to true for GDPR-compliant permanent deletion. |
| Create or Update Object | `upsertObject` | Create or update a custom object (such as a company) via the Encharge Ingest API 'group' event, optionally associating it with a person. |
| Create or Update People | `createUpdatePeople` | Create or update a person in Encharge. If a person with the given email or userId exists they are updated, otherwise a new person is created. |
| Create Person Fields | `createFields` | Create a new custom person field in your Encharge account. |
| Create Webhook Subscription | `createWebhook` | Subscribe to an Encharge event by registering a webhook target URL. Supported event types include newUser, updatedUser, unsubscribedUser, added-tag-X, and removed-tag-X. |
| Delete Person Field | `deleteField` | Delete a person field from your Encharge account, identified by its field name. |
| Delete Webhook Subscription | `deleteWebhook` | Delete an existing Encharge event subscription (webhook) by its id. |
| Get Account Info | `getAccountInfo` | Retrieve information about the connected Encharge account, including people count, status, timezone, active services, and site. |

<details>

<summary>See 10 more actions</summary>

* **Get People** `getPeople`: Retrieve one or more specific people from your Encharge account by email, userId, or Encharge id.
* **Get People in Segment** `getPeopleInSegment`: Retrieve the people that belong to a given segment, with optional pagination and sorting.
* **Get Person Fields** `getFields`: Retrieve all person fields (custom and system properties) defined in your Encharge account.
* **Get Segments** `getSegments`: Retrieve all dynamic segments defined in your Encharge account.
* **Identify Person** `identifyPerson`: Create or update a person via the Encharge Ingest API using the 'identify' event. Any fields in the user object are stored as person properties.
* **Remove Tag** `removeTag`: Remove one or more comma-separated tags from an existing person, identified by email, userId, or Encharge id.
* **Send Transactional Email** `sendTransactionalEmail`: Send a transactional email via Encharge using a saved template, custom HTML, or plain text. Exactly one of template, html, or text must be provided.
* **Track Event** `trackEvent`: Record a custom event for a person via the Encharge Ingest API. The person is created if they do not exist.
* **Unsubscribe Person** `unsubscribePerson`: Unsubscribe a person so they no longer receive emails. Identify the person by email, userId, or Encharge id.
* **Update Person Field** `updateField`: Modify an existing person field, identified by its field name.

</details>
