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

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Tag</td><td><code>addTag</code></td><td>Add one or more comma-separated tags to an existing person, identified by email, userId, or Encharge id.</td></tr><tr><td>Alias Person</td><td><code>aliasPerson</code></td><td>Change the userId and/or email of a person via the Encharge Ingest API 'alias' event.</td></tr><tr><td>Archive or Delete People</td><td><code>archivePeople</code></td><td>Archive (default) or permanently delete one or more people by email, userId, or id. Set force to true for GDPR-compliant permanent deletion.</td></tr><tr><td>Create or Update Object</td><td><code>upsertObject</code></td><td>Create or update a custom object (such as a company) via the Encharge Ingest API 'group' event, optionally associating it with a person.</td></tr><tr><td>Create or Update People</td><td><code>createUpdatePeople</code></td><td>Create or update a person in Encharge. If a person with the given email or userId exists they are updated, otherwise a new person is created.</td></tr><tr><td>Create Person Fields</td><td><code>createFields</code></td><td>Create a new custom person field in your Encharge account.</td></tr><tr><td>Create Webhook Subscription</td><td><code>createWebhook</code></td><td>Subscribe to an Encharge event by registering a webhook target URL. Supported event types include newUser, updatedUser, unsubscribedUser, added-tag-X, and removed-tag-X.</td></tr><tr><td>Delete Person Field</td><td><code>deleteField</code></td><td>Delete a person field from your Encharge account, identified by its field name.</td></tr><tr><td>Delete Webhook Subscription</td><td><code>deleteWebhook</code></td><td>Delete an existing Encharge event subscription (webhook) by its id.</td></tr><tr><td>Get Account Info</td><td><code>getAccountInfo</code></td><td>Retrieve information about the connected Encharge account, including people count, status, timezone, active services, and site.</td></tr></tbody></table>

<details>

<summary>View 10 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get People</td><td><code>getPeople</code></td><td>Retrieve one or more specific people from your Encharge account by email, userId, or Encharge id.</td></tr><tr><td>Get People in Segment</td><td><code>getPeopleInSegment</code></td><td>Retrieve the people that belong to a given segment, with optional pagination and sorting.</td></tr><tr><td>Get Person Fields</td><td><code>getFields</code></td><td>Retrieve all person fields (custom and system properties) defined in your Encharge account.</td></tr><tr><td>Get Segments</td><td><code>getSegments</code></td><td>Retrieve all dynamic segments defined in your Encharge account.</td></tr><tr><td>Identify Person</td><td><code>identifyPerson</code></td><td>Create or update a person via the Encharge Ingest API using the 'identify' event. Any fields in the user object are stored as person properties.</td></tr><tr><td>Remove Tag</td><td><code>removeTag</code></td><td>Remove one or more comma-separated tags from an existing person, identified by email, userId, or Encharge id.</td></tr><tr><td>Send Transactional Email</td><td><code>sendTransactionalEmail</code></td><td>Send a transactional email via Encharge using a saved template, custom HTML, or plain text. Exactly one of template, html, or text must be provided.</td></tr><tr><td>Track Event</td><td><code>trackEvent</code></td><td>Record a custom event for a person via the Encharge Ingest API. The person is created if they do not exist.</td></tr><tr><td>Unsubscribe Person</td><td><code>unsubscribePerson</code></td><td>Unsubscribe a person so they no longer receive emails. Identify the person by email, userId, or Encharge id.</td></tr><tr><td>Update Person Field</td><td><code>updateField</code></td><td>Modify an existing person field, identified by its field name.</td></tr></tbody></table>

</details>
