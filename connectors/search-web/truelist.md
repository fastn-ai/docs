---
description: "Truelist is an email validation platform."
hidden: true
---

# Truelist

<img src="../../.gitbook/assets/connectors/truelist.png" alt="Truelist logo" width="64">

Truelist is an email validation platform. This connector covers the Truelist REST API: verify up to three email addresses inline, upload batches of email addresses for background validation, list, retrieve and delete batches, search individual email validation results, and read the authenticated user and account.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [truelist.io](https://truelist.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `truelist` |

## Use it

Add Truelist from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.truelist.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Batch | `createBatch` | Uploads a list of email addresses as a batch for background validation. Provide at least two rows; each row is an array whose values include one email address and may carry extra identifying data returned in the annotated CSV. Poll Get Batch for progress, or supply a webhook URL that Truelist calls with the batch id when the batch completes. |
| Delete Batch | `deleteBatch` | Deletes an email validation batch by its UUID. Only completed batches can be deleted; deleting a batch that is still processing returns a 422 error. A successful delete returns HTTP 204 with an empty body. |
| Get Batch | `getBatch` | Retrieves a single email validation batch by its UUID, including its processing state, result counts and result CSV download links. Counts are only populated once the batch is completed. |
| Get Current User | `getCurrentUser` | Retrieves the Truelist user that owns the API key, including their email, name, time zone and the account they belong to with its payment plan and users. |
| List Batches | `listBatches` | Lists all email validation batches in the Truelist account with their processing state, result counts and result CSV download links. |
| List Email Validation Results | `listEmailAddresses` | Lists validated email addresses and their results, optionally filtered by batch, email state, sub state or a specific address, with page-based pagination. |
| Verify Emails Inline | `verifyEmailsInline` | Verifies up to three email addresses synchronously within the request and returns the validation state of each. Requests time out if SMTP checks take longer than 30 seconds. Each verification consumes a validation credit unless a recent cached result is reused. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Batch Completed | `batch.completed` | Fires when a Truelist email validation batch finishes processing. Truelist has no account-level webhook registration: the callback is set per batch. To receive this event, pass this connector's fastn webhook URL as the Webhook URL input of the Create Batch action (the webhook_url field of POST /api/v1/batches). When the batch completes, Truelist sends a POST with a JSON body containing only batch_id (also sent in the X-Batch-Id header); call Get Batch with that id to read the results. Truelist sends a single event type with no event-type field and does not sign deliveries, so no event key or signature verification is configured. Payload schema captured from a real delivery on 2026-09-15. |
