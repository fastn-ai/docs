---
description: "Retently is a customer experience platform for running NPS, CSAT, CES and STAR surveys."
hidden: true
---

# Retently

<img src="../../.gitbook/assets/connectors/retently.png" alt="Retently logo" width="64">

Retently is a customer experience platform for running NPS, CSAT, CES and STAR surveys. This connector covers the full Retently CX REST API v2: account status, customers, companies, feedback responses, outbox records, survey templates, campaigns, campaign reports, metric scores, trend groups, transactional survey sending, historical feedback import, response tags and topics, subscription management, and email and domain suppression lists.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [retently.com](https://retently.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `retently` |

## Use it

Add Retently from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.retently.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Feedback Tags | `addFeedbackTags` | Adds or replaces the tags on a survey response. Set Operation to append to keep existing tags; otherwise the given tags replace them. |
| Add Feedback Topics | `addFeedbackTopics` | Adds or replaces the topics on a survey response to classify it by theme and sentiment. Set Operation to append to keep existing topics; otherwise the given topics replace them. |
| Add Suppressed Domain | `addSuppressedDomain` | Adds a domain pattern, which may use wildcards such as *.example.com, to the account's suppression list so matching emails never receive surveys. |
| Add Suppressed Email | `addSuppressedEmail` | Adds an email address to the account's suppression list so it never receives surveys, with an optional note. Set Operation to delete to also delete the contact from Retently. |
| Create or Update Customers | `createOrUpdateCustomers` | Creates new customers or updates existing ones in bulk, up to 1000 per request, matched by email address. Supports names, company, tags, custom properties, and removing specific properties or tags. This does not send any survey. |
| Delete Customers | `deleteCustomers` | Permanently deletes one or more customers and all of their associated data, identified by email address. |
| Delete Feedback Records | `deleteFeedbackRecords` | Soft-deletes one or more survey responses, identified either by feedback ID or by email address, and recalculates company scores and rating statistics. Email-based deletion removes every matching response unless narrowed by campaign or date range. |
| Delete Outbox Records | `deleteOutboxRecords` | Soft-deletes one or more sent-survey outbox records, identified either by survey ID or by email address. Email-based deletion removes every matching record unless narrowed by campaign or date range. |
| Get Account Status | `getAccountStatus` | Returns a snapshot of the authenticated Retently account, including its identity and timezone, the current plan, the survey credit balance for the active billing period, and usage counters for contacts, feedback, outbox, queue and suppressions. Use it as a lightweight health check and to confirm survey credits are available before sending. |
| Get Campaign Report | `getCampaignReport` | Retrieves the report for a single survey campaign, including trend data, delivery statistics and additional rating question statistics, optionally limited to a reporting window. |

<details>

<summary>See 28 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Company | `getCompany` | Retrieves a single company by its unique Retently company ID or by its domain name, including industry, tags, NPS, CSAT and CES metrics and customer count. |
| Get Customer | `getCustomer` | Retrieves a single customer by their unique Retently customer ID, including profile fields, location, tags, custom properties, last survey sent and survey subscription status. Retently answers an unknown ID with HTTP 200 and a body whose code field is 404, so check the code field in the response. |
| Get Feedback | `getFeedback` | Retrieves a single survey response by its unique feedback ID, including the score, comment, tags, topics and the customer snapshot captured at response time. Retently answers an unknown ID with HTTP 200 and a body whose code field is 404, so check the code field in the response. |
| Get Latest Score | `getLatestScore` | Retrieves the most recent score for one survey metric - NPS, CSAT, CES or STAR - together with the rating distribution and response counts for that metric. |
| Get Template | `getTemplate` | Retrieves a single survey template by its ID, always including its survey questions and each question's stable UUID. Use it to discover the question UUIDs needed to build the additional questions payload for Import Feedback. |
| Import Feedback | `importFeedback` | Synchronously imports up to 200 historical survey responses into a campaign, for example when migrating from another feedback tool. Imported responses count toward the score and trend by their response date, are excluded from delivery statistics, consume no send credits and never trigger webhooks or reminders. |
| List Campaign Reports | `listCampaignReports` | Retrieves reports for every survey campaign on the account, including trend data, delivery statistics and additional rating question statistics, optionally limited to a reporting window. |
| List Campaigns | `listCampaigns` | Retrieves every survey campaign on the account with its name, metric type, delivery channel, associated survey template and whether it is currently active. |
| List Companies | `listCompanies` | Retrieves a paginated list of companies on the account, including industry, tags, NPS, CSAT and CES metrics, and the number of customers attached to each company. |
| List Customers | `listCustomers` | Retrieves a paginated list of customers, with optional filtering by email address, creation date range and customer properties, and optional sorting. Returns each customer's profile, tags, custom properties, last survey sent and subscription status. |
| List Feedback | `listFeedback` | Retrieves survey responses, with optional filtering by customer email or ID, campaign, creation date range and customer properties. Returns each response's score, comment, tags, topics and the customer snapshot captured at response time. |
| List NPS Templates (Deprecated) | `listTemplatesLegacy` | Deprecated by Retently in favour of List Templates. Retrieves the account's NPS survey templates. |
| List Outbox | `listOutbox` | Retrieves a paginated list of sent surveys with their delivery status and recipient details, with optional filtering by email, campaign, channel, how the survey was sent, send date range and customer properties. |
| List Responses (Deprecated) | `listResponsesLegacy` | Deprecated by Retently in favour of List Feedback. Retrieves a paginated list of NPS survey responses, optionally limited to a creation date range. |
| List Suppressed Domains | `listSuppressedDomains` | Retrieves the domain patterns on the account's suppression list. Emails matching these patterns are blocked from receiving surveys. |
| List Suppressed Emails | `listSuppressedEmails` | Retrieves the email addresses on the account's suppression list. Suppressed emails are blocked from receiving any surveys. |
| List Templates | `listTemplates` | Retrieves every survey template on the account with its name, delivery channel and associated survey metric. |
| List Transactional Campaigns (Deprecated) | `listCampaignsLegacy` | Deprecated by Retently in favour of List Campaigns. Retrieves the account's active transactional campaigns, and returns 404 when none are active. |
| List Trend Groups | `listTrendGroups` | Retrieves every trend group on the account with its metric type, whether it is the default group, and its creation date. |
| List Trends of a Group | `listTrendsOfGroup` | Retrieves the trends in one trend group, including current and baseline scores with deltas, trend lines and respondent distributions, for a preset or custom date range. |
| Remove Suppressed Domain | `removeSuppressedDomain` | Removes a domain pattern from the account's suppression list by its suppression ID. Only manually added suppressions can be removed. |
| Remove Suppressed Email | `removeSuppressedEmail` | Removes an email address from the account's suppression list by its suppression ID. Only manually added suppressions can be removed. Retently answers an unknown or non-removable ID with HTTP 200 and a body whose code field is 404. |
| Remove Suppressed Email by Address | `removeSuppressedEmailByAddress` | Removes an email address from the account-level suppression list using the address itself rather than the suppression ID. Only manually added account-level suppressions are removed; domain and global suppressions are not affected. |
| Resubscribe Customers | `resubscribeCustomers` | Resubscribes customers that an account owner previously unsubscribed through the API or the app. Idempotent: an already-subscribed contact returns status already_subscribed. Contacts who unsubscribed themselves or hard-bounced are skipped with a reason, for compliance. |
| Send Transactional Survey | `sendTransactionalSurvey` | Queues a transactional email or in-app survey through the given campaign for 1 to 100 customers, creating or updating those customers at the same time. An optional delay in days postpones the send and overrides the campaign's own scheduling. This sends real surveys and consumes survey credits. |
| Sync Customer Attributes | `syncCustomerAttributes` | Refreshes the customer snapshot stored on existing feedback and outbox records from each customer's current profile, so later feedback and outbox reads reflect the latest tags, properties, name and company. Select customers by exactly one of IDs, emails or a filter. The work runs asynchronously and returns one job per scope. |
| Unsubscribe Customers | `unsubscribeCustomers` | Unsubscribes one or more customers from receiving future surveys, with an optional opt-out message. |
| Update Feedback Tags (Deprecated) | `updateFeedbackTagsLegacy` | Deprecated by Retently in favour of Add Feedback Tags. Adds or replaces the tags on an NPS survey response. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Contact Opted Out | `contact_opted_out` | Fires when a surveyed contact opts out of future surveys. Retently has no webhook registration API, so this is configured by hand in each Retently survey campaign: open the campaign editor, go to Webhooks (Export), click '+ Create new webhook', choose the event 'Contact opted out', paste the fastn webhook URL as the Endpoint URL, and in the Request body keep the default fields and set the literal values "event": "contact_opted_out" and "account_id": "&lt;your Retently account ID from Get Account Status&gt;". Save and switch the webhook ON. Repeat for every campaign that should deliver this event. Retently does not sign deliveries. The payload shape is admin-composed; the schema below is Retently's documented default request body. |
| Feedback In Custom Score Range | `custom_score_range` | Fires when a survey response's score falls inside the score range chosen on the webhook. Retently has no webhook registration API, so this is configured by hand in each Retently survey campaign: open the campaign editor, go to Webhooks (Export), click '+ Create new webhook', choose the event 'Custom score range', paste the fastn webhook URL as the Endpoint URL, and in the Request body keep the default fields and set the literal values "event": "custom_score_range" and "account_id": "&lt;your Retently account ID from Get Account Status&gt;". Save and switch the webhook ON. Repeat for every campaign that should deliver this event. Retently does not sign deliveries. The payload shape is admin-composed; the schema below is Retently's documented default request body. |
| New Feedback | `new_feedback` | Fires when a customer submits a survey response, with or without a comment. Retently has no webhook registration API, so this is configured by hand in each Retently survey campaign: open the campaign editor, go to Webhooks (Export), click '+ Create new webhook', choose the event 'New feedback (with or without comment)', paste the fastn webhook URL as the Endpoint URL, and in the Request body keep the default fields and set the literal values "event": "new_feedback" and "account_id": "&lt;your Retently account ID from Get Account Status&gt;". Save and switch the webhook ON. Repeat for every campaign that should deliver this event. Retently does not sign deliveries. The payload shape is admin-composed; the schema below is Retently's documented default request body. |
| New Feedback With Comment | `new_feedback_with_comment` | Fires when a customer submits a survey response that includes a comment. Retently has no webhook registration API, so this is configured by hand in each Retently survey campaign: open the campaign editor, go to Webhooks (Export), click '+ Create new webhook', choose the event 'New feedback (with comment)', paste the fastn webhook URL as the Endpoint URL, and in the Request body keep the default fields and set the literal values "event": "new_feedback_with_comment" and "account_id": "&lt;your Retently account ID from Get Account Status&gt;". Save and switch the webhook ON. Repeat for every campaign that should deliver this event. Retently does not sign deliveries. The payload shape is admin-composed; the schema below is Retently's documented default request body. |
| New Feedback Without Comment | `new_feedback_without_comment` | Fires when a customer submits a survey response without a comment. Retently has no webhook registration API, so this is configured by hand in each Retently survey campaign: open the campaign editor, go to Webhooks (Export), click '+ Create new webhook', choose the event 'New feedback (without comment)', paste the fastn webhook URL as the Endpoint URL, and in the Request body keep the default fields and set the literal values "event": "new_feedback_without_comment" and "account_id": "&lt;your Retently account ID from Get Account Status&gt;". Save and switch the webhook ON. Repeat for every campaign that should deliver this event. Retently does not sign deliveries. The payload shape is admin-composed; the schema below is Retently's documented default request body. |
| Response Assigned | `response_updated_assigned` | Fires when a user in Retently assigns a survey response to a teammate. Save and switch the webhook ON. One such webhook delivers all seven response-action events. Retently does not sign deliveries. Schema modelled from Retently's documented default body plus the four response-action fields. |
| Response Marked Not Resolved | `response_updated_unresolved` | Fires when a user in Retently marks a survey response as not resolved. Save and switch the webhook ON. One such webhook delivers all seven response-action events. Retently does not sign deliveries. Schema modelled from Retently's documented default body plus the four response-action fields. |
| Response Marked Resolved | `response_updated_resolved` | Fires when a user in Retently marks a survey response as resolved. Save and switch the webhook ON. One such webhook delivers all seven response-action events. Retently does not sign deliveries. Schema modelled from Retently's documented default body plus the four response-action fields. |
| Response Note Added or Edited | `response_updated_notes_updated` | Fires when a user in Retently adds or edits a note on a survey response. Save and switch the webhook ON. One such webhook delivers all seven response-action events. Retently does not sign deliveries. Schema modelled from Retently's documented default body plus the four response-action fields. |
| Response Starred | `response_updated_starred` | Fires when a user in Retently stars a survey response. Save and switch the webhook ON. One such webhook delivers all seven response-action events. Retently does not sign deliveries. Schema modelled from Retently's documented default body plus the four response-action fields. |

<details>

<summary>See 3 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Response Unassigned | `response_updated_unassigned` | Fires when a user in Retently unassigns a survey response. Save and switch the webhook ON. One such webhook delivers all seven response-action events. Retently does not sign deliveries. Schema modelled from Retently's documented default body plus the four response-action fields. |
| Response Unstarred | `response_updated_unstarred` | Fires when a user in Retently removes the star from a survey response. Save and switch the webhook ON. One such webhook delivers all seven response-action events. Retently does not sign deliveries. Schema modelled from Retently's documented default body plus the four response-action fields. |
| Survey Bounced | `survey_bounced` | Fires when a survey email bounces. Retently has no webhook registration API, so this is configured by hand in each Retently survey campaign: open the campaign editor, go to Webhooks (Export), click '+ Create new webhook', choose the event 'Survey bounced', paste the fastn webhook URL as the Endpoint URL, and in the Request body keep the default fields and set the literal values "event": "survey_bounced" and "account_id": "&lt;your Retently account ID from Get Account Status&gt;". Save and switch the webhook ON. Repeat for every campaign that should deliver this event. Retently does not sign deliveries. The payload shape is admin-composed; the schema below is Retently's documented default request body. |

</details>
