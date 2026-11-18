---
description: "Postmark transactional email API (base https://api.postmarkapp.com)."
hidden: true
---

# Postmark

<img src="../../.gitbook/assets/connectors/postmark.png" alt="Postmark logo" width="64">

Postmark transactional email API (base https://api.postmarkapp.com). Send single/batch email (raw or with templates), manage bounces, templates, message streams, suppressions, outbound/inbound messages, opens/clicks, delivery & engagement stats, webhooks, and data removals (all via the Server Token, header X-Postmark-Server-Token). Account-level operations — servers, domains (DKIM/return-path), and sender signatures — require the Account Token (header X-Postmark-Account-Token); supply it as the accountToken credential and it is injected on those actions. Requires Accept and Content-Type application/json.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [postmarkapp.com](https://postmarkapp.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `postmark` |

## Use it

Add Postmark from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.postmark.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Bounce | `activateBounce` | Reactivate a deactivated bounced address so Postmark will deliver to it again. Server-level. |
| Archive Message Stream | `archiveMessageStream` | Archive a message stream. Returns the expected purge date (~45 days). Server-level. |
| Bypass Inbound Message | `bypassInboundMessage` | Bypass inbound processing rules for a blocked inbound message so it is delivered. Server-level. |
| Create Data Removal | `createDataRemoval` | Request erasure of all data for a recipient email. ACCOUNT-LEVEL: requires the Account Token. Available by request; account-owner only. |
| Create Domain | `createDomain` | Create a domain. ACCOUNT-LEVEL: requires the Account Token. Name required. |
| Create Inbound Rule Trigger | `createInboundRuleTrigger` | Create an inbound rule trigger that blocks inbound mail from an email address or a whole domain. Server-level. |
| Create Message Stream | `createMessageStream` | Create a transactional or broadcast message stream. ID, Name, MessageStreamType required (Inbound cannot be created). Server-level. |
| Create Sender Signature | `createSenderSignature` | Create a sender signature. ACCOUNT-LEVEL: requires the Account Token. FromEmail and Name required. |
| Create Server | `createServer` | Create a new server. ACCOUNT-LEVEL: requires the Account Token. Name required; DeliveryType (Live/Sandbox) is immutable after creation. |
| Create Suppression | `createSuppression` | Suppress one or more recipient addresses on a message stream (max 50). Server-level. |

<details>

<summary>See 74 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Template | `createTemplate` | Create a template or layout. Name required; provide HtmlBody and/or TextBody; Subject required for Standard templates. Server-level. |
| Create Webhook | `createWebhook` | Create a webhook for delivery/bounce/open/click/spam/subscription events. Url required. Server-level. |
| Delete Domain | `deleteDomain` | Delete a domain by ID. ACCOUNT-LEVEL: requires the Account Token. |
| Delete Inbound Rule Trigger | `deleteInboundRuleTrigger` | Delete a single inbound rule trigger by ID. Server-level. |
| Delete Sender Signature | `deleteSenderSignature` | Delete a sender signature by ID. ACCOUNT-LEVEL: requires the Account Token. |
| Delete Server | `deleteServer` | Delete a server by ID. ACCOUNT-LEVEL: requires the Account Token. Gated; not enabled on all accounts. |
| Delete Suppression | `deleteSuppression` | Remove one or more suppressions from a message stream (max 50). SpamComplaint suppressions cannot be deleted. Server-level. |
| Delete Template | `deleteTemplate` | Delete a template by ID or alias. Server-level. |
| Delete Webhook | `deleteWebhook` | Delete a webhook by ID. Server-level. |
| Edit Domain | `editDomain` | Edit a domain's return-path. ACCOUNT-LEVEL: requires the Account Token. |
| Edit Message Stream | `editMessageStream` | Edit a message stream's name, description, or subscription config. Type is immutable. Server-level. |
| Edit Sender Signature | `editSenderSignature` | Edit a sender signature. ACCOUNT-LEVEL: requires the Account Token. Name required; FromEmail is immutable. |
| Edit Server | `editServer` | Update the current server's configuration. Send only the fields to change. Server-level. |
| Edit Server By ID | `editServerById` | Update a server by ID. ACCOUNT-LEVEL: requires the Account Token. Send only fields to change. |
| Edit Template | `editTemplate` | Edit an existing template by ID or alias. Send only the fields to change. Server-level. |
| Edit Webhook | `editWebhook` | Edit a webhook by ID (partial update). MessageStream is not editable. Server-level. |
| Get Bounce | `getBounce` | Get a single bounce by ID, including full Content. Server-level. |
| Get Bounce Counts | `getBounceCounts` | Get a time-series of bounce counts by type. Server-level. |
| Get Bounce Dump | `getBounceDump` | Get the raw SMTP dump for a bounce. Empty if unavailable (not stored beyond 30 days). Server-level. |
| Get Bounces | `getBounces` | List bounces with filtering and paging. count and offset are required (count max 500; count+offset &lt;= 10000). Server-level. |
| Get Browser Platform Usage | `getBrowserPlatformUsage` | Gets an overview of the browser platforms used to click links in your emails (Desktop, Mobile, Unknown), with a per-day breakdown. Server-level (X-Postmark-Server-Token). |
| Get Browser Usage | `getBrowserUsage` | Gets an overview of the browsers used to click links in your emails. Keys are browser family names (e.g. 'Safari mobile', 'Chrome'), with a per-day breakdown. Server-level (X-Postmark-Server-Token). |
| Get Bulk Email Status | `getBulkEmailStatus` | Get the status/details of a Bulk API request by its ID (requires Bulk API approval). Server-level. |
| Get Click Counts | `getClickCounts` | Get a time-series of link-click counts (total and unique). Server-level. |
| Get Click Location | `getClickLocation` | Gets an overview of which part of the email links were clicked from (HTML or Text), with a per-day breakdown. Server-level (X-Postmark-Server-Token). |
| Get Data Removal Status | `getDataRemovalStatus` | Check the status of a data removal request by ID. ACCOUNT-LEVEL: requires the Account Token. |
| Get Delivery Stats | `getDeliveryStats` | Get the bounce delivery stats summary: count of inactive emails and bounce counts by type. Free read, good for connection validation. Server-level. |
| Get Domain | `getDomain` | Get a single domain with full DKIM/SPF/return-path details. ACCOUNT-LEVEL: requires the Account Token. |
| Get Email Client Usage | `getEmailClientUsage` | Gets an overview of the email clients used to open your emails. Keys are client names (e.g. 'Apple Mail', 'Gmail'), with a per-day breakdown. Server-level (X-Postmark-Server-Token). |
| Get Email Platform Usage | `getEmailPlatformUsage` | Gets an overview of the platforms used to open your emails (Desktop, Mobile, WebMail, Unknown), with a per-day breakdown. Server-level (X-Postmark-Server-Token). |
| Get Inbound Message Details | `getInboundMessageDetails` | Get full details for a single inbound message including bodies, headers, attachments. Server-level. |
| Get Message Clicks | `getMessageClicks` | Get link-click events for a single message. count and offset required. Server-level. |
| Get Message Opens | `getMessageOpens` | Get open events for a single message. count and offset required. Server-level. |
| Get Message Stream | `getMessageStream` | Get a single message stream by ID. Server-level. |
| Get Open Counts | `getOpenCounts` | Get a time-series of open counts (total and unique). Server-level. |
| Get Outbound Message Details | `getOutboundMessageDetails` | Get full details for a single outbound message including bodies and message events. Server-level. |
| Get Outbound Message Dump | `getOutboundMessageDump` | Get the raw SMTP source of an outbound message. May be empty. Server-level. |
| Get Outbound Stats Overview | `getOutboundStatsOverview` | Get the outbound stats overview (sends, bounces, opens, clicks, spam, tracking). All filters optional. Server-level. |
| Get Sender Signature | `getSenderSignature` | Get a single sender signature with full DKIM/return-path details. ACCOUNT-LEVEL: requires the Account Token. |
| Get Sent Counts | `getSentCounts` | Get a time-series of sent email counts. Server-level. |
| Get Server | `getServer` | Get the current server's configuration (settings, webhook URLs, tracking). Free read, ideal for connection validation. Server-level. |
| Get Server By ID | `getServerById` | Get a single server by ID. ACCOUNT-LEVEL: requires the Account Token. |
| Get Spam Complaints | `getSpamComplaints` | Get a time-series of spam complaint counts. Server-level. |
| Get Template | `getTemplate` | Get a single template by ID or alias, including Subject, HtmlBody, TextBody. Server-level. |
| Get Tracked Email Counts | `getTrackedEmailCounts` | Get a time-series of tracked email counts. Server-level. |
| Get Webhook | `getWebhook` | Get a single webhook configuration by ID. Server-level. |
| Get Webhook Statistics | `getWebhookStatistics` | Get delivery statistics for a webhook over a rolling 24-hour window (totals and per trigger). Server-level. |
| List Bulk Email Requests | `listBulkEmailRequests` | List Bulk API requests on the server, newest first (requires Bulk API approval). Page with the returned PaginationKey. Server-level. |
| List Domains | `listDomains` | List all domains on the account. ACCOUNT-LEVEL: requires the Account Token. count and offset required. |
| List Inbound Rule Triggers | `listInboundRuleTriggers` | List inbound rule triggers (blocked senders/domains) for the server. count and offset are required. Server-level. |
| List Message Streams | `listMessageStreams` | List message streams on the server. Optionally filter by type and include archived. Server-level. |
| List Sender Signatures | `listSenderSignatures` | List sender signatures on the account. ACCOUNT-LEVEL: requires the Account Token. count and offset required. |
| List Servers | `listServers` | List all servers on the account. ACCOUNT-LEVEL: requires the Account Token. count and offset required. |
| List Suppressions | `listSuppressions` | List (dump) suppressions on a message stream with optional filters. Server-level. |
| List Templates | `listTemplates` | List templates and layouts. count and offset are required. Free read, useful for validation. Server-level. |
| List Webhooks | `listWebhooks` | List webhooks, optionally filtered by message stream. Server-level (X-Postmark-Server-Token). |
| Push Templates | `pushTemplates` | Push templates from a source server to a destination server. ACCOUNT-LEVEL: requires the Account Token (accountToken credential). Set PerformChanges false for a dry-run preview. |
| Resend Sender Confirmation | `resendSenderConfirmation` | Resend the confirmation email for a sender signature. ACCOUNT-LEVEL: requires the Account Token. |
| Retry Inbound Message | `retryInboundMessage` | Retry processing of a failed inbound message. Server-level. |
| Rotate Domain DKIM | `rotateDomainDkim` | Rotate (create a new pending) DKIM key for a domain. ACCOUNT-LEVEL: requires the Account Token. |
| Search Inbound Messages | `searchInboundMessages` | Search received inbound messages with filters. count and offset required. Server-level. |
| Search Message Clicks | `searchMessageClicks` | Search link-click events across messages. count and offset required. Server-level. |
| Search Message Opens | `searchMessageOpens` | Search open events across messages with client/OS/geo filters. count and offset required. Server-level. |
| Search Outbound Messages | `searchOutboundMessages` | Search sent outbound messages with filters. count and offset required (count+offset &lt;= 10000). Server-level. Filter by metadata with extra input keys named metadata_&lt;key&gt; (e.g. metadata_color); they are passed through as query parameters. |
| Send Batch Emails | `sendBatchEmails` | Send up to 500 emails in one call. Body is a raw JSON array of message objects (same shape as Send Email). Returns a result array in the same order; check each item's ErrorCode. Server-level. |
| Send Batch Emails With Templates | `sendBatchEmailsWithTemplates` | Send up to 500 template-based emails in one call. Body is {Messages:[...]} where each message has TemplateId/Alias + TemplateModel. Returns a result array. Server-level. |
| Send Bulk Email | `sendBulkEmail` | Send one message to many recipients via the Bulk API (requires Bulk API approval on the account). Define content once (HtmlBody/TextBody or TemplateId/TemplateAlias) and personalise per recipient with TemplateModel. Defaults to the broadcast stream. Server-level. |
| Send Email | `sendEmail` | Send a single transactional email via Postmark. Requires From and To; provide HtmlBody and/or TextBody (at least one). Server-level (X-Postmark-Server-Token). |
| Send Email With Template | `sendEmailWithTemplate` | Send a single email rendered from a Postmark template. Provide TemplateId or TemplateAlias plus TemplateModel. Subject comes from the template. Server-level. |
| Unarchive Message Stream | `unarchiveMessageStream` | Restore an archived message stream before its purge date. Server-level. |
| Validate Template | `validateTemplate` | Validate template content and test-render with a model without saving. Server-level. |
| Verify Domain DKIM | `verifyDomainDkim` | Trigger DKIM verification for a domain. ACCOUNT-LEVEL: requires the Account Token. |
| Verify Domain Return-Path | `verifyDomainReturnPath` | Trigger return-path verification for a domain. ACCOUNT-LEVEL: requires the Account Token. |
| Verify Webhook | `verifyWebhook` | Test a webhook endpoint for each enabled event type. If every enabled event returns 200 the webhook is marked verified, otherwise unverified (and it won't receive events). Server-level. |

</details>
