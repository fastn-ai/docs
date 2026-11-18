---
description: "Klenty sales engagement platform."
---

# Klenty

Klenty sales engagement platform. Manage prospects, lists, cadences/sequences, tags, custom fields, call and email engagement reports, and webhooks via the Klenty REST API.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [klenty.com](https://klenty.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 30 |
| **Events** | 0 |
| **Slug** | `klenty` |

## Use it

Add Klenty from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.klenty.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Custom Field Value | `addCustomFieldValue` | Set custom field values on an EXISTING prospect, identified by email in the URL path. Uses Klenty's Update Prospect endpoint; the prospect must already exist. |
| Add Prospect To List | `addProspectToList` | Assign an existing prospect to a Klenty list, identified by email in the URL path. Verified live on 2026-09-14: a prospect on list "default" sent List="fastn-e2e" moves to that list and the change persists on a subsequent Get Prospect. Sending an existing prospect through Create Prospect instead is rejected with K01205005 "Prospect already exists in Klenty.", so this is the correct action for changing the list of a prospect that already exists. The target list must already exist in the account. |
| Add Tags To Prospect | `addTagsToProspect` | Set the tags on an existing prospect, identified by email in the URL path. Tags are pipe-separated (Tag1\|Tag2). IMPORTANT: this REPLACES the prospect's entire tag set rather than appending to it — it uses Klenty's Update Prospect endpoint, which overwrites the Tags field. Verified live: a prospect tagged "tagX,tagY" sent Tags="newTag" ends up tagged only "newTag". To add a tag while keeping the existing ones, read the prospect first with Get Prospect and send the full combined list. The prospect must already exist. |
| Add Webhook | `addWebhook` | Create a webhook subscription for a Klenty event. |
| Bulk Create Prospects | `bulkCreateProspects` | Create up to 100 prospects in one call. Pass a JSON array string of prospect objects (same fields as Create Prospect). |
| Create Prospect | `createProspect` | Create a new prospect. Only Email is required; all other fields are optional. CustomFields is an array of {key,value} objects. This does NOT upsert: verified live, an email that already exists is rejected with HTTP 200 carrying error K01205005 "Prospect already exists in Klenty." Use Update Prospect to change an existing prospect, and Add Prospect To List to move one between lists. Klenty exposes no delete-prospect endpoint, so prospects created here cannot be removed via the API. |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription by id. |
| Get All Webhooks | `getAllWebhooks` | Get all webhook subscriptions configured for the user. |
| Get Call Completion Report | `getCallCompletion` | Retrieve call completion records for the account over a date range. Klenty rejects any range wider than the last 30 days with error K2002, and answers HTTP 200 with status false and error K2003 when no call records match. |
| Get Company Cadences | `getCompanyCadences` | Get all company/team cadences (sequences). Uses the Company API Key. |
| Get Email Engagements Report | `getEmailEngagements` | Get aggregate email engagement metrics for a cadence within a date range. |
| Get Lists | `getLists` | Get all prospect lists in the Klenty account. |
| Get Prospect | `getProspect` | Get full details of a single prospect by email address. Pass customFields=true to include custom field values. |
| Get Prospect Status By Email | `getProspectStatusByEmail` | Get the cadence status and prospect status for a prospect by email. |
| Get Prospect Status By Id | `getProspectStatusById` | Get the cadence status and prospect status for a prospect by Klenty prospect id. |
| Get Step Wise Engagements Report | `getStepWiseEngagements` | Get per-step engagement metrics for a cadence within a date range. |
| Get User Cadences | `getUserCadences` | Get the cadences owned by a specific user, filtered by owner email (username query param). |
| List Prospects By Created Date | `listProspectsByCreatedDate` | Get prospects created within a date range. Dates MUST be yyyy/mm/dd (slash-separated); yyyy-mm-dd is rejected by Klenty with K06101027 'Invalid startDate in payload'. |
| List Prospects By List | `listProspectsByList` | Get prospects belonging to a specific Klenty list, with pagination. |
| List Prospects By Updated Date | `listProspectsByUpdatedDate` | Get prospects last updated within a date range. Dates MUST be yyyy/mm/dd (slash-separated); yyyy-mm-dd is rejected by Klenty with K06101027 'Invalid startDate in payload'. |
| Mark Do Not Contact | `markDoNotContact` | Change a prospect's status to Do Not Contact. |
| Remove Tags From Prospect | `removeTagsFromProspect` | Remove one or more tags from a prospect by email. |
| Resume Cadence | `resumeCadence` | Resume a paused cadence for a prospect by email. ACCOUNT PREREQUISITE: the Klenty user must have a connected sending email account, otherwise Klenty returns HTTP 200 with an error body - K06102045 'You dont have a connected email account to add to cadence' - and nothing is resumed. Always inspect response.errors; a 200 does not mean the cadence resumed. Endpoint matches Klenty's documented POST /apis/v1/user/{email}/cadences/resume. |
| Revert Do Not Contact | `revertDoNotContact` | Revert a prospect's status from Do Not Contact. |
| Start Cadence | `startCadence` | Add a prospect to a cadence (start the cadence) by email and cadence name. |
| Stop Cadence | `stopCadence` | Stop a cadence for a prospect by email and cadence name. |
| Stop Mails | `stopMails` | Stop all scheduled mails for a prospect by email. |
| Unsubscribe Prospect | `unsubscribeProspect` | Unsubscribe a prospect by email. |
| Update Prospect | `updateProspect` | Update an existing prospect by email. Only prospectEmail is required; include any fields to change. Fields not sent are left unchanged. |
| Update Webhook | `updateWebhook` | Update an existing webhook subscription. |
