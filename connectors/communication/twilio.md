---
description: "Twilio communications API — send SMS/MMS, place voice calls, manage phone numbers, phone-number lookup, identity verification, and messaging services."
hidden: true
---

# Twilio

<img src="../../.gitbook/assets/connectors/lg/twilio.png" alt="Twilio logo">

Twilio communications API — send SMS/MMS, place voice calls, manage phone numbers, phone-number lookup, identity verification, and messaging services. Classic REST API (2010-04-01) plus Lookup v2, Verify v2, and Messaging v1.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [twilio.com](https://twilio.com) |
| **Authentication** | Basic auth |
| **Slug** | `twilio` |

## Use it

Add Twilio from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.twilio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Verification</td><td><code>checkVerification</code></td><td>Verify a code submitted by the user against a Verify service. Provide To and Code. Body is form-urlencoded.</td></tr><tr><td>Create Call</td><td><code>createCall</code></td><td>Place an outbound phone call. Provide To, From, and one of Url, Twiml, or ApplicationSid. Body is application/x-www-form-urlencoded.</td></tr><tr><td>Create Incoming Phone Number</td><td><code>createIncomingPhoneNumber</code></td><td>Provision (buy) a phone number. Provide either PhoneNumber (E.164) or AreaCode. Body is form-urlencoded. NOTE: this purchases a number and incurs charges.</td></tr><tr><td>Create Messaging Service</td><td><code>createMessagingService</code></td><td>Create a Messaging Service (v1). FriendlyName is required. Body is form-urlencoded.</td></tr><tr><td>Create Verify Service</td><td><code>createVerifyService</code></td><td>Create a Verify v2 service. FriendlyName is required. Body is form-urlencoded.</td></tr><tr><td>Delete Call</td><td><code>deleteCall</code></td><td>Delete a completed call record from the logs. Returns 204.</td></tr><tr><td>Delete Incoming Phone Number</td><td><code>deleteIncomingPhoneNumber</code></td><td>Release an owned phone number. Returns 204.</td></tr><tr><td>Delete Message</td><td><code>deleteMessage</code></td><td>Delete a message and its media from the logs. Returns 204 No Content.</td></tr><tr><td>Delete Messaging Service</td><td><code>deleteMessagingService</code></td><td>Delete a Messaging Service. Returns 204.</td></tr><tr><td>Delete Recording</td><td><code>deleteRecording</code></td><td>Delete a recording. Returns 204.</td></tr></tbody></table>

<details>

<summary>View 19 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Account</td><td><code>getAccount</code></td><td>Fetch the authenticating account's details. Cheapest free read — ideal for connection validation.</td></tr><tr><td>Get Call</td><td><code>getCall</code></td><td>Fetch a single call by its SID.</td></tr><tr><td>Get Incoming Phone Number</td><td><code>getIncomingPhoneNumber</code></td><td>Fetch a single owned phone number by SID.</td></tr><tr><td>Get Message</td><td><code>getMessage</code></td><td>Fetch a single message by its SID.</td></tr><tr><td>Get Messaging Service</td><td><code>getMessagingService</code></td><td>Fetch a single Messaging Service by SID.</td></tr><tr><td>Get Recording</td><td><code>getRecording</code></td><td>Fetch metadata for a single recording by SID.</td></tr><tr><td>List Calls</td><td><code>listCalls</code></td><td>List calls in the account, optionally filtered by To, From, Status, or StartTime.</td></tr><tr><td>List Incoming Phone Numbers</td><td><code>listIncomingPhoneNumbers</code></td><td>List the phone numbers owned by the account.</td></tr><tr><td>List Message Media</td><td><code>listMessageMedia</code></td><td>List media attached to a specific message.</td></tr><tr><td>List Messages</td><td><code>listMessages</code></td><td>List messages in the account, optionally filtered by To, From, or DateSent. Cheap read suitable for connection validation.</td></tr><tr><td>List Messaging Services</td><td><code>listMessagingServices</code></td><td>List Messaging Services (v1).</td></tr><tr><td>List Recordings</td><td><code>listRecordings</code></td><td>List call recordings, optionally filtered by CallSid or DateCreated.</td></tr><tr><td>List Verify Services</td><td><code>listVerifyServices</code></td><td>List Verify v2 services in the account.</td></tr><tr><td>Lookup Phone Number</td><td><code>lookupPhoneNumber</code></td><td>Look up information about a phone number (validation, line type, caller name, etc.) via Lookup v2. Use the Fields query param to request data packages.</td></tr><tr><td>Search Available Phone Numbers</td><td><code>searchAvailablePhoneNumbers</code></td><td>Search Twilio's inventory for available local phone numbers in a country. Read-only — does not buy.</td></tr><tr><td>Send Message</td><td><code>sendMessage</code></td><td>Send an SMS or MMS message. Provide To plus either From (a Twilio number) or MessagingServiceSid, and Body (or MediaUrl). Body is application/x-www-form-urlencoded.</td></tr><tr><td>Start Verification</td><td><code>startVerification</code></td><td>Send a verification token to a recipient via a Verify service. Provide To and Channel. Body is form-urlencoded.</td></tr><tr><td>Update Call</td><td><code>updateCall</code></td><td>Update a live call to end it (Status=completed/canceled) or redirect it (Url). Body is form-urlencoded.</td></tr><tr><td>Update Incoming Phone Number</td><td><code>updateIncomingPhoneNumber</code></td><td>Update configuration of an owned phone number (friendly name, voice/SMS URLs). Body is form-urlencoded.</td></tr></tbody></table>

</details>
