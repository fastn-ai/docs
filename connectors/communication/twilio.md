---
description: "Twilio communications API — send SMS/MMS, place voice calls, manage phone numbers, phone-number lookup, identity verification, and messaging services."
hidden: true
---

# Twilio

Twilio communications API — send SMS/MMS, place voice calls, manage phone numbers, phone-number lookup, identity verification, and messaging services. Classic REST API (2010-04-01) plus Lookup v2, Verify v2, and Messaging v1.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [twilio.com](https://twilio.com) |
| **Authentication** | Basic auth |
| **Actions** | 29 |
| **Events** | 0 |
| **Slug** | `twilio` |

## Use it

Add Twilio from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.twilio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Verification | `checkVerification` | Verify a code submitted by the user against a Verify service. Provide To and Code. Body is form-urlencoded. |
| Create Call | `createCall` | Place an outbound phone call. Provide To, From, and one of Url, Twiml, or ApplicationSid. Body is application/x-www-form-urlencoded. |
| Create Incoming Phone Number | `createIncomingPhoneNumber` | Provision (buy) a phone number. Provide either PhoneNumber (E.164) or AreaCode. Body is form-urlencoded. NOTE: this purchases a number and incurs charges. |
| Create Messaging Service | `createMessagingService` | Create a Messaging Service (v1). FriendlyName is required. Body is form-urlencoded. |
| Create Verify Service | `createVerifyService` | Create a Verify v2 service. FriendlyName is required. Body is form-urlencoded. |
| Delete Call | `deleteCall` | Delete a completed call record from the logs. Returns 204. |
| Delete Incoming Phone Number | `deleteIncomingPhoneNumber` | Release an owned phone number. Returns 204. |
| Delete Message | `deleteMessage` | Delete a message and its media from the logs. Returns 204 No Content. |
| Delete Messaging Service | `deleteMessagingService` | Delete a Messaging Service. Returns 204. |
| Delete Recording | `deleteRecording` | Delete a recording. Returns 204. |
| Get Account | `getAccount` | Fetch the authenticating account's details. Cheapest free read — ideal for connection validation. |
| Get Call | `getCall` | Fetch a single call by its SID. |
| Get Incoming Phone Number | `getIncomingPhoneNumber` | Fetch a single owned phone number by SID. |
| Get Message | `getMessage` | Fetch a single message by its SID. |
| Get Messaging Service | `getMessagingService` | Fetch a single Messaging Service by SID. |
| Get Recording | `getRecording` | Fetch metadata for a single recording by SID. |
| List Calls | `listCalls` | List calls in the account, optionally filtered by To, From, Status, or StartTime. |
| List Incoming Phone Numbers | `listIncomingPhoneNumbers` | List the phone numbers owned by the account. |
| List Message Media | `listMessageMedia` | List media attached to a specific message. |
| List Messages | `listMessages` | List messages in the account, optionally filtered by To, From, or DateSent. Cheap read suitable for connection validation. |
| List Messaging Services | `listMessagingServices` | List Messaging Services (v1). |
| List Recordings | `listRecordings` | List call recordings, optionally filtered by CallSid or DateCreated. |
| List Verify Services | `listVerifyServices` | List Verify v2 services in the account. |
| Lookup Phone Number | `lookupPhoneNumber` | Look up information about a phone number (validation, line type, caller name, etc.) via Lookup v2. Use the Fields query param to request data packages. |
| Search Available Phone Numbers | `searchAvailablePhoneNumbers` | Search Twilio's inventory for available local phone numbers in a country. Read-only — does not buy. |
| Send Message | `sendMessage` | Send an SMS or MMS message. Provide To plus either From (a Twilio number) or MessagingServiceSid, and Body (or MediaUrl). Body is application/x-www-form-urlencoded. |
| Start Verification | `startVerification` | Send a verification token to a recipient via a Verify service. Provide To and Channel. Body is form-urlencoded. |
| Update Call | `updateCall` | Update a live call to end it (Status=completed/canceled) or redirect it (Url). Body is form-urlencoded. |
| Update Incoming Phone Number | `updateIncomingPhoneNumber` | Update configuration of an owned phone number (friendly name, voice/SMS URLs). Body is form-urlencoded. |
