---
description: "TimelinesAI is a shared WhatsApp inbox and automation platform for teams."
hidden: true
---

# TimelinesAI

TimelinesAI is a shared WhatsApp inbox and automation platform for teams. This connector covers the full TimelinesAI Public API: chats, chat history and chat updates, message sending to phone numbers, JIDs and existing chats, voice messages, internal notes, message details, delivery status history and reactions, chat labels, file uploads and downloads, connected WhatsApp accounts, workspace info and quotas, teammates and invitations, outbound webhooks, and the WhatsApp Business API (WABA) surface of accounts, templates, chats, messages, reactions, labels and account analytics.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [timelines.ai](https://timelines.ai) |
| **Authentication** | Credentials you enter |
| **Actions** | 50 |
| **Events** | 32 |
| **Slug** | `timelinesAi` |

## Use it

Add TimelinesAI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.timelinesAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Chat Labels | `addChatLabels` | Adds labels to a WhatsApp chat, keeping any labels already applied. Workspace labels that do not yet exist are created automatically. |
| Add Chat Note | `addChatNote` | Adds an internal note to an existing WhatsApp chat in TimelinesAI. Notes are visible to your team only and are never delivered to the WhatsApp contact. |
| Add WABA Chat Labels | `addWabaChatLabels` | Adds labels to a WhatsApp Business API chat, keeping any labels already applied. Workspace labels that do not yet exist are created automatically. |
| Create Webhook | `createWebhook` | Creates an outbound webhook subscription in the TimelinesAI workspace so that a chosen event topic is delivered to your HTTPS endpoint in real time. A workspace may hold up to ten webhooks at once. |
| Delete File | `deleteFile` | Permanently deletes an uploaded file from the TimelinesAI workspace. Messages already sent with the file as an attachment are unaffected. |
| Delete Webhook | `deleteWebhook` | Deletes an outbound webhook subscription from the TimelinesAI workspace so the workspace stops delivering that event topic. |
| Get Chat | `getChat` | Returns the details of a single WhatsApp chat in the TimelinesAI workspace, identified by its numeric TimelinesAI chat id. |
| Get File | `getFile` | Returns the details of an uploaded file in the TimelinesAI workspace together with a temporary download URL for its contents. |
| Get Message | `getMessage` | Returns the details of a single WhatsApp message identified by its TimelinesAI message uid, including its text, direction, attachments and current delivery status. |
| Get Message Reactions | `getMessageReactions` | Returns the current map of emoji reactions on a WhatsApp message, keyed by the participant who reacted. |
| Get Message Status History | `getMessageStatusHistory` | Returns the delivery status history of a WhatsApp message, showing each transition from queued through sent, delivered and read with its timestamp. |
| Get WABA Account | `getWabaAccount` | Returns the details of a single WhatsApp Business API account connected to the TimelinesAI workspace, identified by its internal account id. |
| Get WABA Chat | `getWabaChat` | Returns the details of a single WhatsApp Business API chat in the TimelinesAI workspace, identified by its numeric chat id. |
| Get WABA Message | `getWabaMessage` | Returns the details of a single WhatsApp Business API message identified by its TimelinesAI message uid, including its text, direction, attachments and current delivery status. |
| Get WABA Message Reaction | `getWabaMessageReaction` | Returns the current emoji reaction on a WhatsApp Business API message. |
| Get WABA Message Status History | `getWabaMessageStatusHistory` | Returns the delivery status history of a WhatsApp Business API message, showing each transition from queued through sent, delivered and read with its timestamp. |
| Get WABA Template | `getWabaTemplate` | Returns the details of a single WhatsApp Business API message template, including its name, language, approval status and variable placeholders. |
| Get Webhook | `getWebhook` | Returns a single outbound webhook subscription in the TimelinesAI workspace by its webhook id. |
| Get Workspace | `getWorkspace` | Returns information about the TimelinesAI workspace together with all current quotas and utilization statistics, including plan, seat usage and message sending quota. |
| Invite Teammate | `inviteTeammate` | Invites a new teammate to the TimelinesAI workspace by email and assigns their role and team. The invited person receives an email invitation from TimelinesAI. |
| List Chat Labels | `listChatLabels` | Returns the labels currently applied to a single WhatsApp chat in the TimelinesAI workspace. |
| List Chat Messages | `listChatMessages` | Returns the message history of a single WhatsApp chat, optionally filtered by direction, date range or surrounding message, and sorted by timestamp. |
| List Chats | `listChats` | Returns the full or filtered list of WhatsApp chats in the TimelinesAI workspace. Results are paginated at 50 chats per page; check has_more_pages in the response and increment page to retrieve the rest. |
| List Files | `listFiles` | Returns the files uploaded to the TimelinesAI workspace through the Public API, optionally narrowed to filenames containing a given string. |
| List Teammates | `listTeammates` | Returns every teammate in the TimelinesAI workspace with their user id, display name, email, role and team, along with the list of workspace teams. |
| List WABA Accounts | `listWabaAccounts` | Returns every WhatsApp Business API (WABA) account connected to the TimelinesAI workspace, with its internal id, phone number and status. |
| List WABA Chat Labels | `listWabaChatLabels` | Returns the labels currently applied to a single WhatsApp Business API chat in the TimelinesAI workspace. |
| List WABA Chat Messages | `listWabaChatMessages` | Returns the message history of a single WhatsApp Business API chat, optionally filtered by direction, date range or surrounding message, and sorted by timestamp. |
| List WABA Chats | `listWabaChats` | Returns the full or filtered list of WhatsApp Business API chats in the TimelinesAI workspace. Results are paginated at 50 chats per page. |
| List WABA Templates | `listWabaTemplates` | Returns the WhatsApp Business API message templates available in the TimelinesAI workspace. Results are paginated at 50 templates per page. |
| List Webhooks | `listWebhooks` | Returns every outbound webhook subscription configured in the TimelinesAI workspace, with its event type, destination URL and enabled state. |
| List WhatsApp Accounts | `listWhatsappAccounts` | Returns every WhatsApp account currently connected to the TimelinesAI workspace, with its phone number, wid and connection state. |
| Poll WABA Account Analytics | `pollWabaAnalytics` | Polls a previously requested WhatsApp Business API account analytics job by its handle and returns the report once it is ready. |
| Replace Chat Labels | `replaceChatLabels` | Replaces the complete set of labels on a WhatsApp chat with the labels you supply, removing any label not in the list. Workspace labels that do not yet exist are created automatically. |
| Replace WABA Chat Labels | `replaceWabaChatLabels` | Replaces the complete set of labels on a WhatsApp Business API chat with the labels you supply, removing any label not in the list. Workspace labels that do not yet exist are created automatically. |
| Request WABA Account Analytics | `requestWabaAnalytics` | Starts an asynchronous analytics request for a WhatsApp Business API account over a chosen time window and returns a handle to poll for the result. |
| Revoke Invitation | `revokeInvitation` | Revokes a pending workspace invitation so the invited person can no longer join the TimelinesAI workspace. |
| Send Message To Chat | `sendChatMessage` | Sends a WhatsApp message into an existing TimelinesAI chat, optionally as a reply to an earlier message and optionally carrying a previously uploaded file. Each send consumes one message credit from the workspace quota. |
| Send Message To JID | `sendMessageToJid` | Sends a WhatsApp message to a contact or group addressed by its WhatsApp JID, optionally as a reply to an earlier message. Each send consumes one message credit from the workspace quota. |
| Send Message To Phone Number | `sendMessageToPhone` | Sends a WhatsApp message to a phone number without requiring a previous chat or contact. Each send consumes one message credit from the workspace quota; a message carrying both text and an attachment consumes two. |
| Send Voice Message | `sendVoiceMessage` | Sends an audio file into an existing TimelinesAI chat as a WhatsApp voice note, uploaded as a multipart form request. Each send consumes one message credit from the workspace quota. |
| Send WABA Message To Chat | `sendWabaChatMessage` | Sends a WhatsApp Business API message into an existing WABA chat, as free text, a previously uploaded file, or an approved template. Exactly one of text, file_uid or template must be supplied; a file may carry a text caption. |
| Send WABA Message To Phone Number | `sendWabaMessageToPhone` | Sends a WhatsApp Business API message to a phone number from a chosen WABA account, as free text, a previously uploaded file, or an approved template. Exactly one of text, file_uid or template must be supplied; a file may carry a text caption. |
| Update Chat | `updateChat` | Updates a WhatsApp chat in TimelinesAI: rename it, assign or unassign the responsible teammate, close or reopen it, mark it read or unread, and switch the AI Agent auto-response on or off. Only the fields you supply are changed. |
| Update Message Reaction | `updateMessageReaction` | Sets or clears your own emoji reaction on a WhatsApp message. Supply a single emoji to react, or an empty string to remove your existing reaction. |
| Update WABA Chat | `updateWabaChat` | Updates a WhatsApp Business API chat in TimelinesAI: rename it, assign or unassign the responsible teammate, close or reopen it, and mark it read or unread. Only the fields you supply are changed. |
| Update WABA Message Reaction | `updateWabaMessageReaction` | Sets or clears the emoji reaction on a WhatsApp Business API message. Supply a single emoji to react, or an empty string to remove the existing reaction. |
| Update Webhook | `updateWebhook` | Updates an existing outbound webhook subscription in the TimelinesAI workspace, changing its event topic, destination URL or enabled state. Only the fields you supply are changed. |
| Upload File | `uploadFile` | Uploads a file directly into the TimelinesAI workspace as a multipart form request and returns the file uid to attach to outgoing messages. Text content round-trips reliably; binary payloads should be uploaded with the Upload File From URL action instead. |
| Upload File From URL | `uploadFileFromUrl` | Uploads a file into the TimelinesAI workspace by downloading it from a publicly accessible URL, and returns the file uid to attach to outgoing messages. Share links from services such as Google Drive or OneDrive are not accepted. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Chat Responsible Assigned | `chat:responsible:assigned` | A teammate was assigned as responsible for a WhatsApp chat. |
| Chat Responsible Unassigned | `chat:responsible:unassigned` | The responsible teammate was removed from a WhatsApp chat. |
| Incoming Call Ended | `call:incoming:ended` | An incoming WhatsApp call ended. |
| Incoming Call Missed | `call:incoming:missed` | An incoming WhatsApp call was missed. |
| Message Reaction Changed | `message:reaction` | An emoji reaction on a WhatsApp message was set or cleared. |
| Message Received | `message:received:new` | A new incoming WhatsApp message arrived on a connected account. |
| Message Sent | `message:sent:new` | A new outgoing WhatsApp message was sent from a connected account. |
| New Chat | `chat:new` | A new WhatsApp chat was created in the workspace. |
| New Incoming Chat | `chat:incoming:new` | A new WhatsApp chat was started by a contact. |
| New Incoming WABA Chat | `waba:chat:incoming` | A new WhatsApp Business API chat was started by a contact. |
| New Message | `message:new` | Any new WhatsApp message, incoming or outgoing, on any WhatsApp account connected to the workspace. |
| New Outgoing Chat | `chat:outgoing:new` | A new WhatsApp chat was started from the workspace. |
| New Outgoing WABA Chat | `waba:chat:outgoing` | A new WhatsApp Business API chat was started from the workspace. |
| Outgoing Call Ended | `call:outgoing:ended` | An outgoing WhatsApp call ended. |
| WABA Account Active | `waba:account:active` | A WhatsApp Business API account became active. |
| WABA Account Disabled | `waba:account:disabled` | A WhatsApp Business API account was disabled. |
| WABA Account Disconnected | `waba:account:disconnected` | A WhatsApp Business API account was disconnected from the workspace. |
| WABA Chat Assigned | `waba:chat:assigned` | A teammate was assigned as responsible for a WhatsApp Business API chat. |
| WABA Chat Closed | `waba:chat:closed` | A WhatsApp Business API chat was closed. |
| WABA Chat Reopened | `waba:chat:reopened` | A closed WhatsApp Business API chat was reopened. |
| WABA Chat Unassigned | `waba:chat:unassigned` | The responsible teammate was removed from a WhatsApp Business API chat. |
| WABA Message Delivered | `waba:message:delivered` | A WhatsApp Business API message was delivered to the recipient. |
| WABA Message Failed | `waba:message:failed` | A WhatsApp Business API message failed to send. |
| WABA Message Read | `waba:message:read` | A WhatsApp Business API message was read by the recipient. |
| WABA Message Received | `waba:message:received` | A WhatsApp Business API message arrived from a contact. |
| WABA Template Approved | `waba:template:approved` | A WhatsApp Business API message template was approved. |
| WABA Template Disabled | `waba:template:disabled` | A WhatsApp Business API message template was disabled. |
| WABA Template Rejected | `waba:template:rejected` | A WhatsApp Business API message template was rejected. |
| WhatsApp Account Connected | `whatsapp:account:connected` | A WhatsApp account was connected to the workspace. |
| WhatsApp Account Disconnected | `whatsapp:account:disconnected` | A WhatsApp account was permanently disconnected from the workspace. |
| WhatsApp Account Resumed | `whatsapp:account:resumed` | Message syncing resumed for a previously suspended WhatsApp account. |
| WhatsApp Account Suspended | `whatsapp:account:suspended` | Message syncing for a WhatsApp account was paused, typically after a subscription cancellation or downgrade. |
