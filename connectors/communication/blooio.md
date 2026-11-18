---
description: "Blooio multi-channel messaging API (v4): iMessage, SMS, RCS and WhatsApp."
hidden: true
---

# Blooio

Blooio multi-channel messaging API (v4): iMessage, SMS, RCS and WhatsApp. Manage channels and sender numbers, contacts and identities, chats, messages, reactions and polls, groups, templates, attachments, phone-number lookup, priorities, API keys, webhooks and a unified event feed.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [blooio.com](https://blooio.com) |
| **Authentication** | API key |
| **Actions** | 159 |
| **Events** | 24 |
| **Slug** | `blooio` |

## Use it

Add Blooio from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.blooio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Chat Participant | `addChatParticipant` | Adds a participant to a chat. NOT YET IMPLEMENTED by Blooio: the v4 route is defined and 501 not_implemented is its only documented response. |
| Add Contact Tags | `addContactTags` | Add one or more tags to a contact. Supply either a tags array or a single tag string. |
| Add Group Member | `addGroupMember` | Blooio v2 API - no v4 equivalent (v4 can only set the member list at group creation). Adds an existing contact to a group, and to the linked iMessage chat when the group is linked. COMING SOON: the vendor has this temporarily disabled and 501 'Adding group members is coming soon' is its only observed response. |
| Assess Bloobability | `assessBloobability` | Blooio v4: scores a conversation against one or more policies with Bloobability v2. Returns, per policy, probability (the policy holds) and answerable (the conversation has enough to judge it), both 0-1; full mode also returns supporting and contradicting message ids. There is no verdict or threshold. Unknown fields and explicit nulls are rejected. |
| Assign Channel To Api Key | `assignChannelToApiKey` | Blooio v4: makes an API key the SOLE owner of a channel's line, so messages sent with that key can originate from it - the programmatic equivalent of assigning a number to a key on the dashboard Channels board. Ownership is exclusive: any other key loses the line. Blooio Apps (OAuth) access tokens only - API-key auth is rejected with 403 oauth_token_required. |
| Attach Contact Identity | `attachContactIdentity` | Attach an additional phone or email identity, on a given channel type, to an existing contact. |
| Batch Look Up Phone Numbers | `batchLookupPhoneNumbers` | Looks up up to 100 phone numbers in one call. Requires a Blooio Enterprise plan; other plans receive 403. |
| Create Api Key | `createApiKey` | Blooio v4: MINTS A NEW LIVE API KEY for the installed organization. *** DANGER: the raw key is returned once in this response and cannot be recovered afterwards; it is a real credential that can send messages and spend the account's quota. Never run this to "test" the route, and never let the response be logged. *** Blooio Apps (OAuth) access tokens only - API-key auth is rejected with 403 oauth_token_required. A new key owns no numbers until channels are assigned to it. |
| Create Attachment | `createAttachment` | Blooio v4: registers an attachment for use in a message. NOT YET IMPLEMENTED by the vendor - always returns 501 {"code":"not_implemented","details":{"resource":"attachments.create"}} pending v4 schema/backfill work. |
| Create Contact | `createContact` | Create a contact, optionally with one identity (a phone number or email on a channel type). |
| Create Group | `createGroup` | Creates a group chat on a group-capable channel (blooio/whatsapp) with one or more members. Members are phone numbers (E.164) or emails, as strings or {identifier} objects; unknown members are auto-created as contacts. |
| Create Message Template | `createTemplate` | Creates a message template. NOT YET IMPLEMENTED by Blooio: 501 not_implemented is the only documented response and the vendor's OpenAPI declares no request schema for it, so any field may be passed through (additionalProperties is open). |
| Create Priority | `createPriority` | Creates a channel priority (a send-time waterfall pool). channels is an array of ch_... ids or {channel_id, priority} objects. The first priority created for a key becomes its default unless is_default false is set. SECURITY: the response echoes the calling key's own value as owner_id. |
| Create Webhook | `createWebhook` | Subscribe an HTTPS endpoint to Blooio events. SECURITY: the response returns the signing_secret once, on creation — treat the response as a secret. Every webhook receives every event type; filter by `type` in your handler. |
| Delete Contact | `deleteContact` | Soft-delete a contact and its identities. |
| Delete Group | `deleteGroup` | Deletes a group by its grp_... id. The group's underlying chat is NOT deleted (Blooio has no delete route for chats). |
| Delete Message Template | `deleteTemplate` | Deletes a message template. NOT YET IMPLEMENTED by Blooio: 501 not_implemented is its only documented response, so this route currently deletes nothing. |
| Delete Priority | `deletePriority` | Deletes a channel priority by its priority_... id. |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription by its wh_ id. Deliveries stop immediately. |
| Deprecate Api Key | `deprecateApiKey` | Blooio v4: REVOKES an API key permanently. *** DANGER: the key stops authenticating immediately, its number ownership is released, and this CANNOT BE UNDONE through the API. Passing the key this connection itself authenticates with will lock the connector out of the account. Confirm the target key is not in use before running. *** Blooio Apps (OAuth) access tokens only - API-key auth is rejected with 403 oauth_token_required. |
| Detach Contact Identity | `detachContactIdentity` | Detach a phone or email identity from a contact. |
| Find Or Create Chat | `createChat` | Finds or creates a 1:1 chat with a recipient on a channel. Returns the chat at the TOP LEVEL (not wrapped in data) with `created` indicating whether it was newly created. NOTE: Blooio has no delete route for chats - every chat created here is permanent. |
| Get Api Key | `getApiKey` | Blooio v4: fetches one API key's metadata by its raw value. SECURITY: the key value travels in the URL path and is echoed in the response. Blooio Apps (OAuth) access tokens only - API-key auth is rejected with 403 oauth_token_required. |
| Get Attachment | `getAttachment` | Blooio v4: gets one attachment by id. NOT YET IMPLEMENTED by the vendor - always returns 501 {"code":"not_implemented","details":{"resource":"attachments.get"}}. |
| Get Authenticated Account | `getMe` | Return the Blooio organization this API key belongs to, its linked devices and numbers, usage and key validity. SECURITY: the response body echoes the caller's own API key in data.api_key — do not log, store or forward this response. |
| Get Channel | `getChannel` | Get one messaging channel by phone number (E.164), alias, or ch_ channel id. |
| Get Channel Capabilities | `getChannelCapabilities` | Return the protocols, content types, actions and interactive features a channel supports. |
| Get Channel Settings | `getChannelSettings` | Read a channel's per-type settings and which of them this channel is allowed to enable. Blooio channels expose auto_mark_read and auto_share_contact. |
| Get Chat | `getChat` | Returns a single chat by its chat_... id. |
| Get Chat Background | `getChatBackground` | Reads a chat's background image state (Blooio channels). Read live from the device. |
| Get Chat Message | `getChatMessage` | Returns a single message in a chat by its msg_... id. |
| Get Contact | `getContact` | Get one contact by its ct_ id, with its identities and tags. |
| Get Contact Capabilities | `getContactCapabilities` | Return per-identity reachability and capabilities for a contact. For blooio identities this performs a live per-number lookup on an active iMessage channel, and returns 409 when the API key has no active iMessage channel. |
| Get Contact Timeline | `getContactTimeline` | Return a single chronological cross-channel activity feed for a contact, unifying every 1:1 and group conversation the contact takes part in. Set include_events true to interleave delivery receipts, reactions and other non-message activity. |
| Get Default Priority | `getMyDefaultPriority` | Return the calling API key's default channel priority, or data:null when none is configured. |
| Get Event | `getEvent` | Get one event from the unified activity feed by its evt_ id. |
| Get Find My Contact | `getLocationContact` | Get one Find My contact's shared location by handle (E.164 phone, email address, or Apple ID). Requires a dedicated number. |
| Get Group | `getGroup` | Returns a single group by its grp_... id, including its members and linked chat id. |
| Get Message Status | `getMessageStatus` | Lightweight delivery status of a message (queued/sent/delivered/read/failed) plus any error. |
| Get Message Template | `getTemplate` | Returns a single message template. NOT YET IMPLEMENTED by Blooio: 501 not_implemented is its only documented response. |
| Get Number Contact Card | `getContactCard` | Get the contact card (name, avatar, sharing settings) shared from one of your sender numbers. |
| Get Number Purchase Status | `getBlooioPurchase` | Poll an asynchronous number purchase by purchase_id. Returns pending, provisioning, completed (with allocations) or failed. |
| Get Number Risk Tolerance | `getNumberRiskTolerance` | Blooio v2 API - no v4 equivalent. Risk-tolerance report for a single organization number: risk_score, risk_level, line_type, metrics, risk_factors and a daily_data series. Requires the number to be on a dedicated or inbound plan; trial/shared numbers return 403 dedicated_plan_required. Give the number in E.164 (the engine URL-encodes + as %2B). |
| Get Poll Results | `getPollResults` | Returns a poll's title, per-option vote counts and total votes. |
| Get Priority | `getPriority` | Returns a single priority by its priority_... id. SECURITY: the response echoes the calling key's own value as owner_id. |
| Get Risk Tolerance Report | `getRiskTolerance` | Blooio v2 API (https://api.blooio.com/v2/api) - no v4 equivalent exists. Per-number risk-tolerance report for every dedicated and inbound number in the organization over a bounded window, sorted riskiest first. Requires at least one dedicated or inbound number; trial/shared-only organizations receive 403 dedicated_plan_required. |
| Get Risk Tolerance Summary | `getRiskToleranceSummary` | Blooio v2 API - no v4 equivalent. Lightweight cached rollup of the organization's most recent risk scores (highest score/level, count of high-risk numbers). Never recomputes, so it is cheap to poll; returns zeros with computed_at null when the organization has never been scored. |
| Get Webhook | `getWebhook` | Get one webhook subscription by its wh_ id. |
| Initiate FaceTime Call | `callFaceTime` | Blooio v2 API - no v4 equivalent. Initiates a FaceTime call to a phone number or email and returns a shareable join link. COMING SOON: the vendor has this endpoint temporarily disabled and 501 'FaceTime calls are coming soon' is its only documented and observed response. |
| List Api Key Channels | `listApiKeyChannels` | Blooio v4: lists the numbered senders (Blooio and Twilio lines) an API key currently owns - the lines the send layer will consider for requests made with that key. Blooio Apps (OAuth) access tokens only - API-key auth is rejected with 403 oauth_token_required. |
| List Api Keys | `listApiKeys` | Blooio v4: lists the organization's API keys. *** SECURITY WARNING: the response contains the RAW KEY VALUE of every key in the organization. Anyone who can run this action, or read its execution record, obtains live credentials. *** Blooio Apps (OAuth) access tokens only - API-key auth is rejected with 403 oauth_token_required. |
| List Available Blooio Numbers | `listAvailableBlooioNumbers` | Browse Blooio number inventory available to purchase, by plan family and optional area code or country. Requires the number purchase API to be enabled for the organization. |
| List Channels | `listChannels` | List every messaging channel (sender number or account) available to this Blooio API key, with its type, address, status and capabilities. |
| List Chat Messages | `listChatMessages` | Lists messages in a chat, newest first by default. Use order=asc for oldest first. Cursor paginated. |
| List Chat Participants | `listChatParticipants` | Lists the participants of a chat. NOT YET IMPLEMENTED by Blooio: the v4 route is defined but returns 501 not_implemented (resource chats.participants.list) pending their v4 schema/backfill work. |
| List Chats | `listChats` | Lists Blooio conversations, most recent first. Optional filters: channel type, state, channel_id, contact_id. Cursor paginated. |
| List Contact Identities | `listContactIdentities` | List the phone and email identities attached to a contact. |
| List Contact Tags | `listContactTags` | List the tags applied to a contact. |
| List Contacts | `listContacts` | List contacts. Cursor pagination by default; supplying offset, q, tag, sort or filter switches to offset pagination and adds a pagination object with the total. |
| List Events | `listEvents` | Read the unified activity feed: message lifecycle, polls, groups, reactions, typing and safety events. Filter by exact event type (e.g. message.received), chat, or message. NOTE: Blooio documents a wildcard form (message.*) but it is accepted and silently matches nothing — use an exact event type. An unknown type returns 400 invalid_type. |
| List Find My Contacts | `listLocationContacts` | List Find My friends sharing their location with the linked Apple account. Requires a dedicated number; shared and trial lines are refused with 403. |
| List Group Members | `listGroupMembers` | Lists the members of a group with their identity id, contact id, role and identifier. |
| List Groups | `listGroups` | Lists group chats owned by the organization. Cursor paginated. |
| List Message Events | `listMessageEvents` | Lifecycle events for a single message (sent, delivered, read, reactions...). Cursor paginated. |
| List Message Templates | `listTemplates` | Lists message templates. NOT YET IMPLEMENTED by Blooio: the v4 route is defined and 501 not_implemented (resource templates.list) is its only documented response. |
| List Priorities | `listPriorities` | Lists the channel priorities owned by the calling API key. SECURITY: Blooio returns the calling key's own value as owner_id on every priority object - treat this response as credential-bearing and do not log or forward it. |
| List Sender Numbers | `listNumbers` | List the phone numbers and sender addresses available to this API key, with status and plan kind. |
| List Webhook Deliveries | `listWebhookDeliveries` | List recent delivery attempts for a webhook subscription, with response status and timing. |
| List Webhooks | `listWebhooks` | List the organization's webhook subscriptions with their url, scope and status. |
| Look Up Phone Number | `lookupPhoneNumber` | Returns parsed info and geocoding for a phone number in E.164. Requires a Blooio Enterprise plan; other plans receive 403 with 'Phone number lookup requires an Enterprise plan'. |
| Look Up Phone Number By Post | `lookupPhoneNumberPost` | POST form of the phone number lookup, taking the number in a JSON body. Requires a Blooio Enterprise plan; other plans receive 403. |
| Mark Chat As Read | `markChatRead` | Sends a read receipt for a chat. Blooio channels only. |
| Merge Contact | `mergeContact` | Collapse two contacts for the same person into one. The path contact survives; the source contact is absorbed into it, its identities are re-parented and its tags are unioned. The source contact is consumed and cannot be recovered. |
| Purchase Blooio Numbers | `purchaseBlooioNumbers` | BILLABLE. Purchase one or more Blooio lines; charges the organization's default payment method and returns a purchase_id to poll. Requires an Idempotency-Key. Provisioning completes asynchronously. |
| React To Message | `addReaction` | Adds or removes a tapback reaction on any message in the chat, inbound or outbound. Prefix + to add and - to remove (e.g. +love, -love). Returns 409 message_not_reactable while the message is still queued on the device. |
| Refresh Find My Locations | `refreshLocationContacts` | Force a refresh of Find My location data from the linked device (POST form). Requires a dedicated number. |
| Refresh Find My Locations (GET) | `refreshLocationContactsGet` | Convenience GET form of the Find My refresh endpoint, for callers that cannot issue a POST. Requires a dedicated number. |
| Remove Blooio Number | `removeBlooioNumber` | DESTRUCTIVE AND IRREVERSIBLE. Unsubscribes an owned Blooio line and cancels its subscription, the same as the dashboard unsubscribe button. Removing your only line leaves the organization unable to send. Requires one or more churn reason codes. |
| Remove Chat Background | `removeChatBackground` | Removes a chat's background image. Blooio channels only; requires a linked device (a trial/unlinked device returns 502 device_error). |
| Remove Chat Participant | `removeChatParticipant` | Removes a participant from a chat by identity id. NOT YET IMPLEMENTED by Blooio: the v4 route is defined and 501 not_implemented is its only documented response. |
| Remove Contact Tag | `removeContactTag` | Remove one tag from a contact. URL-encode tag values containing spaces or special characters. |
| Remove Group Icon | `removeGroupIcon` | Removes a group's icon. Requires the group chat to be linked on a device, otherwise 409 group_chat_not_linked. |
| Remove Group Member | `removeGroupMember` | Blooio v2 API - no v4 equivalent. Removes a contact from a group, and from the linked iMessage chat when the group is linked; removing the organization's own number leaves the chat instead. COMING SOON: the vendor has this temporarily disabled and 501 'Removing group members is coming soon' is its only observed response, so it currently removes nothing. |
| Replay Webhook Delivery | `replayWebhookDelivery` | Re-send a past webhook delivery attempt to the subscription's current endpoint. |
| Request Call Forwarding | `requestCallForwarding` | Open a support request to forward calls from an owned dedicated or inbound Blooio number to a US E.164 destination. Shared or foreign source numbers are rejected with 403. |
| Rotate Webhook Signing Secret | `rotateWebhookSecret` | SECURITY: rotates the webhook's signing secret and returns the new secret once. The previous secret stops validating immediately. Do not log or persist the response — every consumer of this action receives a live secret. |
| Send Message | `sendMessage` | Send a message to one or more recipients across iMessage, SMS, RCS or WhatsApp. Supply `from` (a number, alias or channel id) or `priority_id` to choose the sender, or omit both to route automatically. Set dry_run true to validate and route without delivering. |
| Send Message On Channel | `sendMessageToChannel` | Channel-scoped send: the channel path segment accepts a phone number (URL-encode + as %2B), an alias, or a ch_... id, and the body omits from. Pass dry_run true to get the routing decision without delivering. WARNING: even a dry run materialises the chat for a new recipient, and Blooio has no delete route for chats or messages. |
| Send Message To Chat | `sendMessageToChat` | Sends a message into an existing chat. Sender channel and recipient are inferred from the chat, so from and to must NOT be supplied. Returns the message object at the TOP LEVEL (not wrapped in data). Pass dry_run true to get the full routing decision without delivering anything. |
| Send Poll To Chat | `sendPoll` | Sends a native iMessage poll to a chat. Requires a title and 2+ options. Blooio channels only. Pass dry_run true to validate and preview without delivering. Blooio has no delete route for messages, so a real (non dry-run) poll is permanent. |
| Set Chat Background | `setChatBackground` | Uploads a chat background image as multipart/form-data. Max 10MB; image/jpeg\|png\|gif\|webp\|heic\|heif. Blooio channels only. Supply backgroundFilename, backgroundContentType and backgroundData (the image bytes as text). Binary image payloads are an engine limitation - this carries text-safe payloads only. |
| Set Group Icon | `setGroupIcon` | Uploads a group icon as multipart/form-data. Max 10MB; image/jpeg\|png\|gif\|webp\|heic\|heif. Requires the group chat to be linked on a device, otherwise 409 group_chat_not_linked. Supply iconFilename, iconContentType and iconData. Binary image payloads are an engine limitation - this carries text-safe payloads only. |
| Set Typing Indicator | `setTyping` | Shows or clears a business-to-customer typing indicator in a chat. Blooio channels only. state is started or stopped. |
| Share Contact Card To Chat | `shareContactCard` | Shares the sender's contact card into a chat. Blooio channels only. Requires a linked device; a trial/unlinked device returns 502 device_error. |
| Stop Typing Indicator | `stopTyping` | Clears the typing indicator in a chat. Blooio channels only. |
| Unassign Channel From Api Key | `unassignChannelFromApiKey` | Blooio v4: removes an API key's ownership of a channel's line, so the key can no longer send from it. Hybrid mode is re-evaluated for the key. Blooio Apps (OAuth) access tokens only - API-key auth is rejected with 403 oauth_token_required. |
| Update Channel Profile | `updateChannelProfile` | Update the channel's Blooio-side profile metadata (display_name, about, email, avatar). Null or an empty string clears a field. Unknown keys are rejected. |
| Update Channel Settings | `updateChannelSettings` | Partially update a channel's settings. Blooio: auto_mark_read on dedicated and inbound lines, auto_share_contact on dedicated lines with a contact card. |
| Update Chat State | `updateChat` | Sets chat state (open/closed). VENDOR CONSTRAINT: only writable on Apple Messages for Business chats. Every other channel type (including blooio) returns 422 state_not_writable. |
| Update Contact | `updateContact` | Rename a contact. The name field is required. |
| Update Contact Identity | `updateContactIdentity` | Rename a contact identity in place. An optional name also updates the parent contact in the same request. |
| Update Group Name | `updateGroup` | Renames a group. name is required. |
| Update Number Contact Card | `updateContactCard` | Update the contact card shared from one of your sender numbers. At least one of first_name, last_name, avatar or sharing is required. |
| Update Priority | `updatePriority` | Updates a priority's name, default flag and/or channel set. Supplying channels REPLACES the priority's channels wholesale. SECURITY: the response echoes the calling key's own value as owner_id. |
| Update Webhook | `updateWebhook` | Update a webhook subscription's url or status (active / disabled). |
| Upload Contact Card Avatar | `uploadContactCardAvatar` | Blooio v4: uploads the avatar image for a number's contact card (max 10MB) as multipart/form-data. Send first_name/last_name alongside so the device write is not photo-only. Requires a dedicated plan - other plans return 403 "Contact card features (set name, set picture, share contact) are only available on dedicated plans". Pass the image in `avatar`; an ASCII-safe format such as a P3 Netpbm PPM works through the fastn engine. |
| V2 Add Contact Tags | `v2AddContactTags` | Blooio v2: adds one or more tags to a contact. Returns 201 with the tags that were added. |
| V2 Add Reaction | `v2AddReaction` | Blooio v2: adds or removes a tapback reaction on a message. The reaction string MUST be prefixed: "+love" to add, "-love" to remove. Emoji are accepted ("+U+1F602"). Requires a linked iMessage device chat. |
| V2 Batch Look Up Phone Numbers | `v2BatchLookupPhoneNumbers` | Blooio v2: looks up many phone numbers in one call. Requires an Enterprise plan. |
| V2 Create Contact | `v2CreateContact` | Blooio v2: creates a contact from an identifier (email address or E.164 phone number) and an optional display name. Returns 201 with the contact; its v2 id IS the identifier string. |
| V2 Create Group | `v2CreateGroup` | Blooio v2: creates a group chat. NOTE: this route talks to the paired device and is SLOW - it regularly takes 30-120s to return 201. Prefer the v4 Create Group action for latency-sensitive use. |
| V2 Create Webhook | `v2CreateWebhook` | Blooio v2: RETIRED BY THE VENDOR. Always returns 410 "Creating webhooks through this endpoint is no longer supported. Use POST /v4/webhooks instead." Kept for completeness; use the v4 Create Webhook action. |
| V2 Delete Contact | `v2DeleteContact` | Blooio v2: permanently deletes a contact by its identifier. Chats and messages are not deleted. |
| V2 Delete Group | `v2DeleteGroup` | Blooio v2: deletes a group by id. The underlying chat is not removed. |
| V2 Delete Webhook | `v2DeleteWebhook` | Blooio v2: deletes a legacy v2 webhook by id. |
| V2 Get Chat | `v2GetChat` | Blooio v2: gets one conversation by its v2 chat id (the participant handle). |
| V2 Get Chat Background | `v2GetChatBackground` | Blooio v2: reads the conversation's wallpaper. This route queries the paired Mac - without a linked device the vendor returns 502 "Failed to get chat background from device". |
| V2 Get Contact | `v2GetContact` | Blooio v2: gets one contact by its v2 contact id, which is the identifier string (e.g. name@example.com or +14155550100). |
| V2 Get Contact Capabilities | `v2GetContactCapabilities` | Blooio v2: live lookup of which protocols (iMessage, SMS, FaceTime) a contact can be reached on. |
| V2 Get Group | `v2GetGroup` | Blooio v2: gets one group by id. |
| V2 Get Location Contact | `v2GetLocationContact` | Blooio v2: gets the last known location for one contact handle. Requires a dedicated number - other plans return 403 "Location tracking is only available on dedicated numbers". |
| V2 Get Me | `v2GetMe` | Blooio v2: returns the current authentication context for the API key (organization, numbers, plan). SECURITY WARNING: the response body echoes the caller's own raw API key. Do not log or forward the response. |
| V2 Get Message | `v2GetMessage` | Blooio v2: gets one message in a conversation. NOTE: v2 message ids are the short ids returned by V2 Send Message - v4 msg_ ids return 404 here. |
| V2 Get Message Status | `v2GetMessageStatus` | Blooio v2: gets the delivery status of one message (queued, sent, delivered, failed) plus the protocol used. |
| V2 Get My Contact Card | `v2GetMyContactCard` | Blooio v2: gets the contact card (name, avatar, sharing settings) configured for one of your numbers. Pass the number in E.164 form, e.g. +14155550100. |
| V2 Get Poll Results | `v2GetPollResults` | Blooio v2: returns a poll's options and vote counts. The poll id is the message id of the poll message. |
| V2 Get Webhook | `v2GetWebhook` | Blooio v2: gets one legacy v2 webhook by id. v4-created webhooks are not visible here. |
| V2 List Chat Messages | `v2ListChatMessages` | Blooio v2: lists the messages in a conversation, filterable by direction and time window. |
| V2 List Chats | `v2ListChats` | Blooio v2: lists conversations with offset pagination. NOTE: a v2 chat id is the participant handle (e.g. name@example.com or +14155550100), not the v4 chat_ id. |
| V2 List Contact Tags | `v2ListContactTags` | Blooio v2: lists the tags attached to a contact. |
| V2 List Contacts | `v2ListContacts` | Blooio v2: lists contacts with offset pagination and optional free-text search. Returns {contacts:[...], pagination:{limit,offset,total}}. |
| V2 List Group Members | `v2ListGroupMembers` | Blooio v2: lists the members of a group with offset pagination. |
| V2 List Groups | `v2ListGroups` | Blooio v2: lists group chats with offset pagination and optional search. Returns {groups:[...], pagination:{...}}. |
| V2 List Location Contacts | `v2ListLocationContacts` | Blooio v2: lists the last known locations shared by your contacts. Requires a dedicated number - other plans return 403 "Location tracking is only available on dedicated numbers". |
| V2 List Numbers | `v2ListNumbers` | Blooio v2: lists the phone numbers (lines) owned by the authenticated organization, with active/suspended state and plan kind. |
| V2 List Webhook Logs | `v2ListWebhookLogs` | Blooio v2: lists delivery logs for a legacy v2 webhook, filterable by HTTP response status range. |
| V2 List Webhooks | `v2ListWebhooks` | Blooio v2: lists legacy v2 webhooks. NOTE: webhooks created through the v4 API do NOT appear here - the two versions use separate stores. New webhooks must be created with the v4 Create Webhook action. |
| V2 Look Up Phone Number | `v2LookupPhoneNumber` | Blooio v2: carrier/line-type lookup for one phone number. Requires an Enterprise plan - other plans return 403 "Phone number lookup requires an Enterprise plan." |
| V2 Look Up Phone Number By Post | `v2LookupPhoneNumberPost` | Blooio v2: same lookup as V2 Look Up Phone Number but with the number in a JSON body, so it never appears in a URL. Requires an Enterprise plan. |
| V2 Mark Chat Read | `v2MarkChatRead` | Blooio v2: marks all messages in a conversation as read. |
| V2 Refresh Location Contacts | `v2RefreshLocationContacts` | Blooio v2: asks the device to refresh all contact locations. Requires a dedicated number - other plans return 403 "Location tracking is only available on dedicated numbers". |
| V2 Remove Chat Background | `v2RemoveChatBackground` | Blooio v2: clears the conversation wallpaper. Requires a paired Mac - otherwise the vendor returns 502 "Failed to remove chat background on device". |
| V2 Remove Contact Tag | `v2RemoveContactTag` | Blooio v2: removes a single tag from a contact. |
| V2 Remove Group Icon | `v2RemoveGroupIcon` | Blooio v2: removes the group chat icon. The group must already be linked to a device chat - otherwise the vendor returns 400 "Group is not linked to a device chat. Cannot remove icon." Send a message to the group first. |
| V2 Replay Webhook Event | `v2ReplayWebhookEvent` | Blooio v2: re-delivers one logged webhook event to the webhook's URL. |
| V2 Request Call Forwarding | `v2RequestCallForwarding` | Blooio v2: requests call forwarding from one of your numbers to another number. Requires a dedicated or inbound line - other lines return 403 "Source number is not a dedicated or inbound number in your organization". |
| V2 Rotate Webhook Secret | `v2RotateWebhookSecret` | Blooio v2: rotates a legacy v2 webhook's signing secret. SECURITY WARNING: the response contains a live whsec_ signing secret - do not log, persist, or forward the response body. |
| V2 Send Message | `v2SendMessage` | Blooio v2: sends a message into an existing conversation. WARNING: unlike the v4 send routes, v2 has NO dry_run mode - every call really queues a message to the recipient, and Blooio has no delete route for messages. Returns 202 with the new message_id. Pass an Idempotency-Key to make retries safe. |
| V2 Send Poll | `v2SendPoll` | Blooio v2: sends a poll into a conversation. iMessage conversations only - an SMS or email chat returns 400 poll_imessage_only. WARNING: v2 has no dry_run and Blooio cannot delete messages. |
| V2 Set Chat Background | `v2SetChatBackground` | Blooio v2: sets the conversation wallpaper from a multipart upload. The vendor accepts ONLY image/jpeg, image/jpg, image/png, image/gif, image/webp, image/heic, image/heif - anything else is rejected 400 "Invalid file type". Pass the image bytes in `background`; the part is declared as image/png. Requires a paired Mac - otherwise the vendor returns 502 "Failed to set chat background on device". ENGINE LIMIT: the fastn multipart recipe carries TEXT parts only, so genuinely binary PNG/JPEG bytes cannot be sent from a workflow today. |
| V2 Set Group Icon | `v2SetGroupIcon` | Blooio v2: uploads a group chat icon as multipart/form-data. Pass the raw image bytes in `icon`; an ASCII-safe format such as a P3 Netpbm PPM works through the fastn engine (true binary formats do not). The group must be linked to a device chat first, otherwise the vendor returns 400 "Group is not linked to a device chat". |
| V2 Share Contact Card | `v2ShareContactCard` | Blooio v2: shares your number's contact card into a conversation. Requires a dedicated plan - other plans return 403 "Contact card features (set name, set picture, share contact) are only available on dedicated plans". |
| V2 Start Typing | `v2StartTyping` | Blooio v2: shows the typing indicator in a conversation. |
| V2 Stop Typing | `v2StopTyping` | Blooio v2: hides the typing indicator in a conversation. |
| V2 Update Contact | `v2UpdateContact` | Blooio v2: renames a contact. The contact id is the identifier string. |
| V2 Update Group | `v2UpdateGroup` | Blooio v2: renames a group chat. |
| V2 Update My Contact Card | `v2UpdateMyContactCard` | Blooio v2: updates the contact card shown to recipients for one of your numbers. Requires a dedicated plan - trial and shared lines are rejected with 403 "Contact card features ... are only available on dedicated plans". |
| V2 Update Webhook | `v2UpdateWebhook` | Blooio v2: updates a legacy v2 webhook's event type, expiry, or deprecation flag. |
| Vote On Poll | `votePoll` | Casts or toggles a vote on a poll by option_index (0-based) or option text. Blooio channels only. Returns 409 poll_not_ready until the poll has materialised on the linked device. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Chat Closed | `chat.closed` | A customer ended the conversation and the chat moved to the closed state. |
| Contact Card Shared | `contact.shared` | A contact card was shared into a chat. |
| Contact Merged | `contact.merged` | Two contacts were collapsed into one survivor. |
| Group Icon Changed | `group.icon_changed` | A group chat's icon was set or removed. |
| Group Name Changed | `group.name_changed` | A group chat was renamed. |
| Message Delivered | `message.delivered` | The recipient's device acknowledged delivery. |
| Message Failed | `message.failed` | An outbound message could not be delivered. Payload shape confirmed from a real delivery on this account. |
| Message Pending | `message.pending` | An outbound message is awaiting the device or channel. |
| Message Queued | `message.queued` | An outbound message was accepted and queued. Confirmed from a real delivery on this account. |
| Message Reaction | `message.reaction` | A tapback reaction was added to or removed from a message. |
| Message Read | `message.read` | The recipient read the message (read receipt). |
| Message Received | `message.received` | An inbound message arrived on one of the organization's channels. |
| Message Sent | `message.sent` | An outbound message was handed to the channel. Payload shape confirmed from a real delivery on this account. |
| Number Banned | `safety.number_banned` | A number was banned by the upstream carrier or platform. |
| Number Purchase Completed | `number.purchase.completed` | An asynchronous number purchase finished and the lines were provisioned. |
| Number Purchase Failed | `number.purchase.failed` | An asynchronous number purchase failed. |
| Number Purchase Needs Action | `number.purchase.action_required` | A number purchase is blocked pending customer action, such as a payment confirmation. |
| Number Removed | `number.removed` | A Blooio line was unsubscribed and removed from the organization. |
| Poll Created | `poll.created` | A poll was created in a chat. |
| Poll Received | `poll.received` | An inbound poll arrived in a chat. |
| Poll Voted | `poll.voted` | Somebody cast or changed a vote on a poll. |
| Safety State Changed | `safety.state_changed` | A channel's safety or trust state changed. |
| Typing Started | `typing.started` | The other party started typing in a chat. |
| Typing Stopped | `typing.stopped` | The other party stopped typing in a chat. |
