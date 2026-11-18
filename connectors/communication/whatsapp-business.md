---
description: "WhatsApp Business Cloud API via Meta Graph API v23.0 (base https://graph.facebook.com/v23.0)."
hidden: true
---

# WhatsApp Business

<img src="../../.gitbook/assets/connectors/lg/whatsapp-business.png" alt="WhatsApp Business logo">

WhatsApp Business Cloud API via Meta Graph API v23.0 (base https://graph.facebook.com/v23.0). Send messages (text, template, media, interactive, location, contacts, reaction), mark read, manage media, phone numbers, business profile, message templates, registration, and webhook app subscriptions. Auth: Bearer access token (system user / app token). phone_number_id and waba_id are per-request inputs.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [graph.facebook.com](https://graph.facebook.com) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Slug** | `whatsappBusiness` |

## Use it

Add WhatsApp Business from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.whatsappBusiness.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Call | `acceptCall` | Accept an incoming user-initiated WhatsApp call once the WebRTC connection is ready (POST /{phoneNumberId}/calls, action accept). call_id comes from the calls 'connect' webhook; session carries your SDP answer. Optional biz_opaque_callback_data is echoed back in the terminate webhook. |
| Create Message Template | `createMessageTemplate` | Create a message template for review (POST /{wabaId}/message_templates). |
| Delete Media | `deleteMedia` | Delete an uploaded media asset (DELETE /{mediaId}). |
| Delete Message Template | `deleteMessageTemplate` | Delete a message template (DELETE /{wabaId}/message_templates?name=). Supplying hsm_id as well deletes only that one language version; without it Meta deletes ALL language versions of the named template. |
| Get Business | `getBusiness` | Get a Meta Business (Business Manager) by id (GET /{businessId}). Use List Businesses to find businessId. Requires the business_management permission. |
| Get Business Profile | `getBusinessProfile` | Get the WhatsApp business profile for a phone number (GET /{phoneNumberId}/whatsapp_business_profile). |
| Get Call Permission | `getCallPermission` | Get whether the business may call a WhatsApp user, and which call actions are currently allowed (GET /{phoneNumberId}/call_permissions?user_wa_id=). Returns permission.status (temporary, permanent, no_permission), expiration_time, actions[] and limits[]. Read-only. |
| Get Call Settings | `getCallSettings` | Get the phone number's settings, including WhatsApp Calling configuration (GET /{phoneNumberId}/settings): calling status, call icon visibility, callback permission, call hours and SIP. Set include_sip_credentials=true to also return SIP credentials. |
| Get Media URL | `getMediaUrl` | Retrieve a temporary download URL and metadata for a media ID (GET /{mediaId}). |
| Get Phone Number | `getPhoneNumber` | Get details of a WhatsApp business phone number (GET /{phoneNumberId}). |
| Get WhatsApp Business Account | `getWhatsAppBusinessAccount` | Get one WhatsApp Business Account (GET /{wabaId}): name, currency, timezone, template namespace, plus optional fields like account_review_status, business_verification_status, health_status, ownership_type, status. Use List Owned WhatsApp Business Accounts to find wabaId. |
| List Business System Users | `listBusinessSystemUsers` | List the system users of a Meta Business (GET /{businessId}/system_users), with their role (e.g. ADMIN, EMPLOYEE). System users own the long-lived tokens used for WhatsApp Cloud API. Requires business_management and admin access to the business. |
| List Businesses | `listBusinesses` | List the Meta Businesses the connected token can see (GET /me/businesses). This is the discovery entry point: every other WhatsApp action needs a WABA id, and a WABA is found by listing a business's owned WhatsApp Business Accounts. |
| List Client WhatsApp Business Accounts | `listClientWhatsAppBusinessAccounts` | List WhatsApp Business Accounts shared with a Meta Business by clients (GET /{businessId}/client_whatsapp_business_accounts), e.g. for solution partners. Each WABA includes permitted_tasks. Use List Owned WhatsApp Business Accounts for WABAs the business owns. |
| List Message Templates | `listMessageTemplates` | List message templates on a WABA (GET /{wabaId}/message_templates). |
| List Owned WhatsApp Business Accounts | `listOwnedWhatsAppBusinessAccounts` | List the WhatsApp Business Accounts (WABAs) owned by a Meta Business (GET /{businessId}/owned_whatsapp_business_accounts). Use List Businesses first to get businessId. Returns the wabaId that every template, phone-number and webhook action needs. Requires the business_management permission on the token. |
| List Phone Numbers | `listPhoneNumbers` | List phone numbers on a WhatsApp Business Account (GET /{wabaId}/phone_numbers). |
| List Subscribed Apps | `listSubscribedApps` | List apps subscribed to a WABA's webhooks (GET /{wabaId}/subscribed_apps). |
| List WABA Assigned Users | `listWabaAssignedUsers` | List users (people and system users) assigned to a WhatsApp Business Account and their tasks (GET /{wabaId}/assigned_users?business={businessId}). businessId is the business that owns or is managing the WABA. Requires business_management. |
| List WhatsApp Accounts For Trigger | `listWhatsAppAccountsForTrigger` | Lists every WhatsApp Business Account (WABA) the connected user can reach, grouped under each Meta Business they belong to (GET /me/businesses with owned WABAs expanded). Needs no input. Used by app triggers so the user can pick which WhatsApp account's events to receive; the WABA id matches entry[].id in WhatsApp webhooks. |
| Mark Message Read | `markMessageRead` | Mark an inbound message as read, optionally also displaying a typing indicator (POST /{phoneNumberId}/messages with status=read). Supply typing_indicator {type:'text'} to show the typing bubble; it is dismissed when you send a message or after 25 seconds. |
| Pre-Accept Call | `preAcceptCall` | Pre-accept an incoming user-initiated WhatsApp call so the WebRTC media connection can be set up before accepting (POST /{phoneNumberId}/calls, action pre_accept). call_id and the SDP offer come from the calls 'connect' webhook; session carries your SDP answer. |
| Register Phone Number | `registerPhoneNumber` | Register a phone number for Cloud API with a 6-digit PIN (POST /{phoneNumberId}/register). |
| Reject Call | `rejectCall` | Reject an incoming user-initiated WhatsApp call (POST /{phoneNumberId}/calls, action reject). call_id comes from the calls 'connect' webhook. |
| Send Call Permission Request | `sendCallPermissionRequest` | Ask a WhatsApp user for permission to call them (POST /{phoneNumberId}/messages, interactive call_permission_request). Sends a real message. The user's answer arrives as a messages webhook with interactive.type call_permission_reply. |
| Send Contacts Message | `sendContactsMessage` | Send one or more contact cards (POST /{phoneNumberId}/messages, type contacts). Contract mirrors Meta's payload so the engine builds and escapes the JSON. |
| Send Interactive Message | `sendInteractiveMessage` | Send an interactive message (buttons, list, CTA URL, flow or product) (POST /{phoneNumberId}/messages, type interactive). The interactive object is declared in the contract so the engine builds and escapes it; |
| Send Location Message | `sendLocationMessage` | Send a location message (POST /{phoneNumberId}/messages, type location). Latitude and longitude are numbers as Meta requires; name and address are genuinely optional and are no longer sent as empty strings. |
| Send Media Message | `sendMediaMessage` | Send a media message by uploaded media ID or public link (POST /{phoneNumberId}/messages). Set `type` and populate the matching object (image/video/audio/document/sticker) with either `id` or `link`. Caption is only valid on image/video/document; audio and sticker have none. |
| Send Reaction | `sendReaction` | React to a message with an emoji (POST /{phoneNumberId}/messages, type reaction). Pass an empty emoji string to remove an existing reaction. |
| Send Template Message | `sendTemplateMessage` | Send a pre-approved template message (POST /{phoneNumberId}/messages, type template). Inputs mirror Meta's payload exactly; the engine builds and escapes the JSON. |
| Send Text Message | `sendTextMessage` | Send a text message (POST /{phoneNumberId}/messages, type text). |
| Start Call | `startCall` | Start a business-initiated WhatsApp call to a user who has granted call permission (POST /{phoneNumberId}/calls, action connect). session carries your SDP offer. Returns calls[0].id (the call_id). Not available for business numbers in US, Canada, Egypt, Vietnam or Nigeria. This rings a real phone. |
| Subscribe App to WABA | `subscribeApp` | Subscribe the app to a WABA's webhooks (POST /{wabaId}/subscribed_apps). Used by the webhook config. |
| Terminate Call | `terminateCall` | End an active WhatsApp call, user- or business-initiated (POST /{phoneNumberId}/calls, action terminate). A calls 'terminate' webhook follows with duration and status. |
| Unsubscribe App from WABA | `unsubscribeApp` | Unsubscribe the app from a WABA's webhooks (DELETE /{wabaId}/subscribed_apps). |
| Update Business Profile | `updateBusinessProfile` | Update the WhatsApp business profile (POST /{phoneNumberId}/whatsapp_business_profile). |
| Update Call Settings | `updateCallSettings` | Enable, disable or configure WhatsApp Calling on a business phone number (POST /{phoneNumberId}/settings). Send only the calling fields you want to change. Enabling requires a messaging limit of 2,000 or more. Returns {success:true}. |
| Upload Media | `uploadMedia` | Upload a media file and get a media ID (POST /{phoneNumberId}/media). The returned id is what Send Media Message, Get Media URL and Delete Media consume - nothing else in this connector could create one. Sent as raw multipart/form-data. LIMITATION: the fastn executor UTF-8-expands binary payloads, so true binary files (JPEG, MP4, PDF) can corrupt in transit; text-based media and vendor-hosted links are reliable. For binary, prefer sending by public `link` on Send Media Message. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Account Review Update | `account_review_update` | WABA review status changed. |
| Account Update | `account_update` | WABA account-level changes (e.g. ban, verification, decisions). |
| Calls | `calls` | WhatsApp Calling events. value.calls[] carries event 'connect' (incoming user call with SDP offer, direction USER_INITIATED) or 'terminate' (status Completed/Failed, start_time, end_time, duration). value.statuses[] with type 'call' carries business-initiated call status RINGING, ACCEPTED or REJECTED. |
| Message Template Status Update | `message_template_status_update` | A message template was approved, rejected, or flagged. |
| Messages & Statuses | `messages` | Inbound messages and outbound message status updates (sent/delivered/read/failed). value contains messages[] or statuses[]. A user's reply to a call permission request also arrives here as messages[].interactive.type = call_permission_reply (response accept/reject, is_permanent, expiration_timestamp). |
| Phone Number Name Update | `phone_number_name_update` | Display name review result for a phone number. |
| Phone Number Quality Update | `phone_number_quality_update` | Phone number quality rating / messaging limit changed. |
| Template Category Update | `template_category_update` | A template's category was changed by Meta. |
