---
description: "Telnyx CPaaS platform."
hidden: true
---

# Telnyx

Telnyx CPaaS platform. Messaging (SMS/MMS), phone numbers and porting, Voice and Call Control, TeXML, Verify, Programmable Fax, Wireless/SIM, Storage, Email, AI Assistants, Video Rooms and account billing via the Telnyx v2 REST API.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [telnyx.com](https://telnyx.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 1156 |
| **Events** | 0 |
| **Slug** | `telnyx` |

## Use it

Add Telnyx from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.telnyx.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Shared Campaign | `acceptCampaign` | Manually accept a campaign shared with Telnyx |
| Accepts This Address Suggestion as a New Emergency Address for Operator Connect and Finishes the | `acceptAddressSuggestions` | Accepts this address suggestion as a new emergency address for Operator Connect and finishes the uploads of the numbers associated with it to Microsoft. |
| Activate Branded Calling on an Enterprise | `activateBrandedCalling` | Branded Calling is a paid product that must be activated on each enterprise. Activation is idempotent: - First call: marks the enterprise as activated and begins onboarding it with the Branded Calling platform asynchronously. Returns 200 with branded calling enabled: true . - Re-call after success: no-op, returns the same enterprise body. - Re-call after a prior failure: re-queues onboarding, returns 200 . Prerequisite: the calling user must have agreed to the Branded Calling Terms of Service ( POST /terms of service/branded calling/agree ). Without that, this endpoint returns 403 terms of service not accepted . Failure modes: - 403 - Branded Calling Terms of Service not accepted. - 404 - enterprise does not exist or does not belong to your account. Pricing: This is a billable action. See https://telnyx.com/pricing/numbers for current pricing. |
| Activate Every Number in a Porting Order Asynchronously. | `activatePortingOrder` | Activate each number in a porting order asynchronously. This operation is limited to US FastPort orders only. |
| Add a Group Suppression | `addGroupSuppression` | Creates a suppression with reason: unsubscribe , source: manual , group id: . All other body fields are ignored; only to is read. Idempotent (same dedupe key → 200 , no new event). |
| Add a Notification Setting | `createNotificationSetting` | Add a notification setting. |
| Add Assistant Tag | `addassistanttag` | Add Assistant Tag |
| Add Assistant Tool | `addassistanttool` | Add Assistant Tool |
| Add Messages to AI Assistant | `callAddMessagesToAIAssistant` | Add messages to the conversation started by an AI assistant on the call. |
| Add Phone Numbers to a DIR | `addDirPhoneNumbersSimplified` | Register phone numbers under a DIR. The enterprise is resolved server-side from the DIR id. Same body, failure modes, and batch semantics whichever path form you use. Pricing: This is a billable action. See https://telnyx.com/pricing/numbers for current pricing. |
| Add RCS Test Number | `inviteATestNumberToRCS` | Adds a test phone number to an RCS agent for testing purposes. |
| Add SSL Certificate | `addStorageSSLCertificate` | Uploads an SSL certificate and its matching secret so that you can use Telnyx's storage as your CDN. |
| Add Step(s) to Plan | `postpublicmissionsmissionsmissionidrunsrunidplansteps` | Add one or more steps to an existing plan |
| Aggregate Conversation Insights | `aggregateconversationinsights` | Aggregate conversation insights by specified fields |
| Agree to the Branded Calling Terms of Service | `agreeToBrandedCallingTos` | Records the authenticated user's agreement to the current Branded Calling ToS. No body required. Idempotent - re-calling after agreement is a no-op and returns the existing agreement. This is a prerequisite for activating Branded Calling on any enterprise ( POST /enterprises/{id}/branded calling ); without an agreement, activation returns 403 . |
| Agree to the Phone Number Reputation Terms of Service | `agreeNumberReputationTermsOfService` | Records the authenticated user's agreement to the current Phone Number Reputation ToS. No body required. Idempotent. Prerequisite for using any of the /v2/.../reputation/ endpoints. |
| Answer Call | `answerCall` | Answer an incoming call. You must issue this command before executing subsequent commands on an incoming call. Expected Webhooks: - call.answered - call.hold and call.unhold if the call is held/unheld - call.deepfake detection.result if deepfake detection was enabled - call.deepfake detection.error if deepfake detection was enabled and an error occurred - streaming.started , streaming.stopped or streaming.failed if stream url was set When the record parameter is set to record-from-answer , the response will include a recording id field. |
| Assign Insight Template to Group | `assigninsighttogroup` | Assign an insight to a group |
| Assign Messaging Profile to Campaign | `postAssignMessagingProfileToCampaign` | This endpoint allows you to link all phone numbers associated with a Messaging Profile to a campaign. Please note: if you want to assign phone numbers to a campaign that you did not create with Telnyx 10DLC services, this endpoint allows that provided that you've shared the campaign with Telnyx. In this case, only provide the parameter, tcrCampaignId , and not campaignId . In all other cases (where the campaign you're assigning was created with Telnyx 10DLC services), only provide campaignId , not tcrCampaignId . |
| Assistant Chat (BETA) | `assistantchatpublicassistantsassistantidchatpost` | This endpoint allows a client to send a chat message to a specific AI Assistant. The assistant processes the message and returns a relevant reply based on the current conversation context. Refer to the Conversation API to create a conversation, filter existing conversations, fetch messages for a conversation, and manually add messages to a conversation. |
| Assistant SMS Chat | `assistantsmschatassistantsassistantidchatsmspost` | Send an SMS message for an assistant. This endpoint: 1. Validates the assistant exists and has messaging profile configured 2. If should create conversation is true, creates a new conversation with metadata 3. Sends the SMS message (If text is set, this will be sent. Otherwise, if this is the first message in the conversation and the assistant has a greeting configured, this will be sent. Otherwise the assistant will generate the text to send.) 4. Updates conversation metadata if provided 5. Returns the conversation ID |
| Authorization Server Metadata | `getOAuthAuthorizationServerMetadata` | OAuth 2.0 Authorization Server Metadata (RFC 8414) |
| Bridge Calls | `bridgeCall` | Bridge two call control calls. Expected Webhooks: - call.bridged for Leg A - call.bridged for Leg B |
| Bulk Update Phone Number Profiles | `bulkUpdateMessagingSettingsOnPhoneNumbers` | Bulk update phone number profiles |
| Cancel a Fax | `cancelFax` | Cancel the outbound fax that is in one of the following states: queued , media.processed , originated or sending |
| Cancel a Fine Tuning Job | `cancelnewfinetuningjobpublicfinetuningpost` | Cancel a fine tuning job. |
| Cancel a Pending Requirement Version | `cancelPendingRequirementVersion` | Cancel a pending requirement version. The pending version is marked as cancelled and the previously active version is restored with effective end at set to NULL. |
| Cancel a Porting Order | `cancelPortingOrder` | Cancel a porting order |
| Cancel a Scheduled Email Message | `cancelScheduledEmailMessage` | Cancels a scheduled email and returns it with status cancelled . The legacy /v2/emails/{id}/schedule DELETE route is an alias. |
| Cancel a Scheduled Message | `cancelMessage` | Cancel a scheduled message that has not yet been sent. Only messages with status=scheduled and send at more than a minute from now can be cancelled. |
| Cancel a Sub Number Order | `cancelSubNumberOrder` | Allows you to cancel a sub number order in 'pending' status. |
| Cancel Run | `postpublicmissionsmissionsmissionidrunsrunidcancel` | Cancel a running or paused run |
| Change the Bundle Status for a Phone Number (set to Being in a Bundle or Remove from a Bundle) | `phoneNumberBundleStatusChange` | Change the bundle status for a phone number (set to being in a bundle or remove from a bundle) |
| Change the Reputation Refresh Frequency | `updateReputationFrequency` | Update how often Telnyx refreshes the reputation data for this enterprise's registered numbers. The new frequency takes effect on the next scheduled refresh. The enterprise's reputation must be in approved status. A request made while the status is pending is rejected with 400 Bad Request . |
| Check a Credential Connection Registration Status | `checkRegistrationStatus` | Checks the registration status for a credential connection, ( registration status ) as well as the timestamp for the last SIP registration event ( registration status updated at ) |
| Check a UAC Connection Registration Status | `checkUacConnectionRegistrationStatus` | Checks the registration status for a UAC connection ( registration status ) as well as the timestamp for the last SIP registration event ( registration status updated at ). |
| Check Hosted Messaging Eligibility | `checkEligibilityNumbers` | Check hosted messaging eligibility |
| Check RCS Capabilities | `listRCSCapabilitiesOfAPhoneNumber` | Check RCS capabilities |
| Check RCS Capabilities (batch) | `listRCSCapabilitiesOfAPhoneNumbersBatch` | Check RCS capabilities (batch) |
| Clone Assistant | `cloneassistantpublicassistantsassistantidclonepost` | Clone an existing assistant, excluding telephony and messaging settings. |
| Clone Mission | `postpublicmissionsmissionsmissionidclone` | Clone an existing mission |
| Compute New Clusters | `computenewclusterpublictextclusterspost` | Starts a background task to compute how the data in an embedded storage bucket is clustered. This helps identify common themes and patterns in the data. |
| Conference Recording Pause | `pauseConferenceRecording` | Pause conference recording. |
| Conference Recording Resume | `resumeConferenceRecording` | Resume conference recording. |
| Conference Recording Start | `startConferenceRecording` | Start recording the conference. Recording will stop on conference end, or via the Stop Recording command. Expected Webhooks: - conference.recording.saved |
| Conference Recording Stop | `stopConferenceRecording` | Stop recording the conference. Expected Webhooks: - conference.recording.saved |
| Confirm an Email-ownership Verification Code | `confirmDirEmailVerification` | Submit the 6-digit code that was emailed to the DIR's authorizer email. On success the authorizer email is marked verified. For security, any failure (wrong, expired, already-used, or too many attempts) returns the same generic message. |
| Contest an Infringement Claim | `contestInfringementClaim` | Submit a written response and supporting documents disputing the claim. The first call moves the claim from pending to contested ; subsequent calls append supplementary evidence without changing status. The documents[] you attach are aggregated across rounds in the claim's contest documents field. Only pending and contested claims accept new evidence. A resolved claim returns 400 . Failure modes: - 400 - the claim is resolved (terminal); cannot be contested further. - 404 - the claim does not exist or is not against a DIR you own. - 422 - contest notes is too short ( 2000 chars), documents is 20 entries, or a document id is duplicated within the same submission. |
| Create a Batch Email Validation Job | `createEmailValidationBatch` | Creates an asynchronous batch validation job for up to 1,000 email addresses. |
| Create a Batch of Email Messages | `createEmailMessageBatch` | Creates up to 50 email messages in a single request. |
| Create a Billing Group | `createBillingGroup` | Create a billing group |
| Create a Call Control Application | `createCallControlApplication` | Create a call control application. |
| Create a Chat Completion | `chatpublicchatcompletionspost` | Deprecated : Use POST /v2/ai/openai/chat/completions instead. Chat with a language model. This endpoint is consistent with the OpenAI Chat Completions API and may be used with the OpenAI JS or Python SDK. |
| Create a Chat Completion (OpenAI-compatible) | `createopenaichatcompletion` | Chat with a language model. This endpoint is consistent with the OpenAI Chat Completions API and may be used with the OpenAI JS or Python SDK by setting the base URL to https://api.telnyx.com/v2/ai/openai . |
| Create a CloudFS Filesystem | `createCloudfsFilesystem` | Creates a CloudFS filesystem. Provisioning is synchronous — typically a few seconds, up to a few minutes — and the filesystem is returned with status ready , together with its S3 bucket and metadata connection details. This response is the only time the filesystem's meta token — and the credential-bearing meta url — are returned; store them securely. If the token is lost, issue a new one with the rotate-meta-token action. Names are unique within your organization: creating with an existing name returns a 422 . Requests are idempotent: retrying with the same Idempotency-Key within 24 hours replays the original response instead of creating another filesystem. |
| Create a Comment | `createComment` | Create a comment |
| Create a Comment for a Porting Order | `createPortingOrderComment` | Creates a new comment for a porting order. |
| Create a Comment on a Portout Request | `postPortRequestComment` | Creates a comment on a portout request. |
| Create a Conversation | `createnewconversationpublicconversationspost` | Create a new AI Conversation. |
| Create a Credential | `createTelephonyCredential` | Create a credential. |
| Create a Credential Connection | `createCredentialConnection` | Creates a credential connection. |
| Create a CSV Download | `createCsvDownload` | Create a CSV download |
| Create a Custom Storage Credential | `createCustomStorageCredentials` | Creates a custom storage credentials configuration. |
| Create a Customer Service Record | `createCustomerServiceRecord` | Create a new customer service record for the provided phone number. |
| Create a Dialogflow Connection | `createDialogflowConnection` | Save Dialogflow Credentiails to Telnyx, so it can be used with other Telnyx services. |
| Create a Display Identity Record (DIR) | `createDir` | Create a new DIR under the given enterprise. The DIR starts in draft status; it must be submitted ( POST .../submit ) and approved by Telnyx before any phone number can be attached. Field rules - display name : 1–35 characters, no emoji or whitespace-only strings; this is the name shown to recipients. - call reasons : 1–10 strings, each ≤64 characters; describe why your business calls customers (e.g. 'Appointment reminders', 'Billing inquiries'). Validate the wording against POST /call reasons/validate . - logo url : HTTPS URL (max 128 chars) to a 256×256 BMP (max 1 MB). The image is downloaded and hashed at submission time. - documents : up to 20 entries; each document id must be obtained by uploading the file via the Telnyx Documents API first. Within one DIR a document id may only appear once. - certify brand is accurate , certify no shaft content , certify ip ownership MUST all be true . Failure modes - 422 - validation error; errors[].source.pointer names the offending field. -. |
| Create a Dynamic Emergency Address. | `createDynamicEmergencyAddress` | Creates a dynamic emergency address. |
| Create a Dynamic Emergency Endpoint. | `createDynamicEmergencyEndpoint` | Creates a dynamic emergency endpoints. |
| Create a Fine Tuning Job | `createnewfinetuningjobpublicfinetuningpost` | Create a new fine tuning job. |
| Create a Global IP | `createGlobalIp` | Create a Global IP. |
| Create a Global IP Assignment | `createGlobalIpAssignment` | Create a Global IP assignment. |
| Create a Global IP Health Check | `createGlobalIpHealthCheck` | Create a Global IP health check. |
| Create a KV Namespace | `createKvNamespace` | Creates a new KV namespace. Provisioning is asynchronous: the namespace is returned with status pending and becomes usable once it reaches provision ok . |
| Create a Ledger Billing Group Report | `createBillingGroupReport` | Create a ledger billing group report |
| Create a List of Additional Documents | `createAdditionalDocuments` | Creates a list of additional documents for a porting order. |
| Create a List of Phone Number Configurations | `createPhoneNumberConfigurations` | Creates a list of phone number configurations. |
| Create a List of Supporting Documents on a Portout Request | `postPortRequestSupportingDocuments` | Creates a list of supporting documents on a portout request. |
| Create a LOA Configuration | `createLoaConfiguration` | Create a LOA configuration. |
| Create a Manual Suppression | `createEmailBlock` | Creates a suppression with reason: manual block and source: manual . Caller-supplied reason / source are ignored ; scope is derived server-side from domain id / from and is never trusted. Idempotent: if a matching row already exists (NULL-safe dedupe key: account id, scope, to, reason, domain id, from), returns the existing record with 200 (no new audit event). bounce category , dsn code , meta , and group id are not accepted on the public surface. Use the unsubscribe-group suppression endpoint or the internal create surface for those. |
| Create a Message (Anthropic-compatible) | `createanthropicmessage` | Send a message to a language model using the Anthropic Messages API format. This endpoint is compatible with the Anthropic Messages API and may be used with the Anthropic JS or Python SDK by setting the base URL to https://api.telnyx.com/v2/ai/anthropic . The endpoint translates Anthropic-format requests into Telnyx's inference internals, then translates the response back to the Anthropic message shape. Streaming responses use Anthropic SSE event types ( message start , content block start , content block delta , content block stop , message delta , message stop ). |
| Create a Messaging Hosted Number Order | `createMessagingHostedNumberOrder` | Create a messaging hosted number order |
| Create a Messaging Profile | `createMessagingProfile` | Create a messaging profile |
| Create a Migration | `createMigration` | Initiate a migration of data from an external provider into Telnyx Cloud Storage. Currently, only S3 is supported. |
| Create a Migration Source | `createMigrationSource` | Create a source from which data can be migrated from. |
| Create a Mobile Voice Connection | `createMobileVoiceConnection` | Create a Mobile Voice Connection |
| Create a Network | `createNetwork` | Create a new Network. |
| Create a New Assistant Test | `createassistanttestpublicassistantstestspost` | Creates a comprehensive test configuration for evaluating AI assistant performance |
| Create a New CDR Report Request | `submitCdrRequest` | Creates a new CDR report request with the specified filters |
| Create a New Legacy Usage V2 CDR Report Request | `submitCdrUsageReport` | Creates a new legacy usage V2 CDR report request with the specified filters |
| Create a New Legacy Usage V2 MDR Report Request | `submitMdrUsageReport` | Creates a new legacy usage V2 MDR report request with the specified filters |
| Create a New Managed Account. | `createManagedAccount` | Create a new managed account owned by the authenticated user. You need to be explictly approved by Telnyx in order to become a manager account. |
| Create a New MDR Detailed Report Request | `submitMdrRequest` | Creates a new MDR detailed report request with the specified filters |
| Create a New Queue | `createTexmlQueue` | Creates a new queue resource. |
| Create a New Requirement Group | `createRequirementGroup` | Create a new requirement group |
| Create a New SIM Card Data Usage Notification | `postSimCardDataUsageNotification` | Creates a new SIM card data usage notification. |
| Create a New Speech to Text Batch Report Request | `submitSttRequest` | Creates a new Speech to Text batch report request with the specified filters |
| Create a Notification Channel | `createNotificationChannels` | Create a notification channel. |
| Create a Notification Profile | `createNotificationProfile` | Create a notification profile. |
| Create a Number Block Order | `createNumberBlockOrder` | Creates a phone number block order. |
| Create a Number Order | `createNumberOrder` | Creates a phone number order. |
| Create a Number Reservation | `createNumberReservation` | Creates a Phone Number Reservation for multiple numbers. |
| Create a Payment Quote | `createX402Quote` | Creates a payment quote for the specified USD amount. Returns payment details including the x402 payment requirements, network, and expiration time. The quote must be settled before it expires. |
| Create a Phone Number Block | `createPortingPhoneNumberBlock` | Creates a new phone number block. |
| Create a Phone Number Extension | `createPortingPhoneNumberExtension` | Creates a new phone number extension. |
| Create a Port-out Related Report | `createPortoutReport` | Generate reports about port-out operations. |
| Create a Porting Order | `createPortingOrder` | Creates a new porting order object. |
| Create a Porting Related Report | `createPortingReport` | Generate reports about porting operations. |
| Create a Private Wireless Gateway | `createPrivateWirelessGateway` | Asynchronously create a Private Wireless Gateway for SIM cards for a previously created network. This operation may take several minutes so you can check the Private Wireless Gateway status at the section Get a Private Wireless Gateway. |
| Create a Pronunciation Dictionary | `createPronunciationDict` | Create a new pronunciation dictionary for the authenticated organization. Each dictionary contains a list of items that control how specific words are spoken. Items can be alias type (text replacement) or phoneme type (IPA pronunciation notation). As an alternative to providing items directly as JSON, you can upload a dictionary file (PLS/XML or plain text format, max 1MB) using multipart/form-data. PLS files use the standard W3C Pronunciation Lexicon Specification XML format. Text files use a line-based format: word=alias for aliases, word:/phoneme/ for IPA phonemes. Limits: - Maximum 50 dictionaries per organization - Maximum 100 items per dictionary - Text: max 200 characters - Alias/phoneme value: max 500 characters - File upload: max 1MB (1,048,576 bytes) |
| Create a Public Internet Gateway | `createPublicInternetGateway` | Create a new Public Internet Gateway. |
| Create a Queue | `createQueue` | Create a new call queue. |
| Create a Response | `chatpublicresponsescompletionspost` | Deprecated : Use POST /v2/ai/openai/responses instead. This endpoint is compatible with the OpenAI Responses API and may be used with the OpenAI JS or Python SDK. Response id parameter is not supported at the moment. Use the conversation parameter with a Telnyx Conversation ID to leverage persistent conversations. |
| Create a Room Composition. | `createRoomComposition` | Asynchronously create a room composition. |
| Create a Room. | `createRoom` | Synchronously create a Room. |
| Create a Scheduled Event | `createscheduledevent` | Create a scheduled event for an assistant |
| Create a Secret | `createintegrationsecret` | Create a new secret with an associated identifier that can be used to securely integrate with other services. |
| Create a SIM Card Group | `createSimCardGroup` | Creates a new SIM card group object |
| Create a SIM Card Order | `createSimCardOrder` | Creates a new order for SIM cards. |
| Create a SIPREC Connector | `createSiprecConnector` | Creates a new SIPREC connector configuration. |
| Create a Stored Payment Transaction | `createStoredPaymentTransaction` | Create a stored payment transaction |
| Create a Sub Number Orders Report | `createSubNumberOrdersReport` | Create a CSV report for sub number orders. The report will be generated asynchronously and can be downloaded once complete. |
| Create a TeXML Secret | `createTexmlSecret` | Create a TeXML secret which can be later used as a Dynamic Parameter for TeXML when using Mustache Templates in your TeXML. In your TeXML you will be able to use your secret name, and this name will be replaced by the actual secret value when processing the TeXML on Telnyx side. The secrets are not visible in any logs. |
| Create a Traffic Policy Profile | `createTrafficPolicyProfile` | Create a new traffic policy profile. At least one of services , ip ranges , or domains must be provided. |
| Create a UAC Connection | `createUacConnection` | Creates a UAC connection. A UAC (User Agent Client) Connection registers Telnyx to your PBX — the opposite of a standard SIP trunk, where the PBX registers to Telnyx. Use UAC when your PBX doesn’t support outbound SIP registration or you need Telnyx to maintain the registration. |
| Create a Verify Profile | `createVerifyProfile` | Creates a new Verify profile to associate verifications with. |
| Create a Virtual Cross Connect | `createVirtualCrossConnect` | Create a new Virtual Cross Connect. For AWS and GCE, you have the option of creating the primary connection first and the secondary connection later. You also have the option of disabling the primary and/or secondary connections at any time and later re-enabling them. With Azure, you do not have this option. Azure requires both the primary and secondary connections to be created at the same time and they can not be independantly disabled. |
| Create a Voice Clone from a Voice Design | `createVoiceClone` | Creates a new voice clone by capturing the voice identity of an existing voice design. The clone can then be used for text-to-speech synthesis. |
| Create a Voice Clone from an Audio File Upload | `createVoiceCloneFromUpload` | Creates a new voice clone by uploading an audio file directly. Supported formats: WAV, MP3, FLAC, OGG, M4A. For best results, provide 5–10 seconds of clear speech. Maximum file size: 5MB for Telnyx, 20MB for Minimax. |
| Create a Webhook for an Email Domain | `createEmailDomainWebhook` | Creates a webhook endpoint subscribed to a specific allowlist of event types. Both email. events (published by email-api) and email domain. events (published by this service) flow through the same webhooks. |
| Create a Whatsapp Message Template | `postWhatsappTemplate` | Create a Whatsapp message template |
| Create a WireGuard Interface | `createWireguardInterface` | Create a new WireGuard Interface. Current limitation of 10 interfaces per user can be created. |
| Create a WireGuard Peer | `createWireguardPeer` | Create a new WireGuard Peer. Current limitation of 5 peers per interface can be created. |
| Create a Wireless Blocklist | `createWirelessBlocklist` | Create a Wireless Blocklist to prevent SIMs from connecting to certain networks. |
| Create a Wireless Detail Records (WDRs) Report | `createWdrReport` | Asynchronously create a report containing Wireless Detail Records (WDRs) for the SIM cards that consumed wireless data in the given time period. |
| Create Advanced Order | `createadvancedorderv2` | Create Advanced Order |
| Create an Access Token. | `createTelephonyCredentialToken` | Create an Access Token (JWT) for the credential. |
| Create an Alphanumeric Sender ID | `createAlphanumericSenderId` | Create a new alphanumeric sender ID associated with a messaging profile. |
| Create an Assistant | `createnewassistantpublicassistantspost` | Create a new AI Assistant. |
| Create an Associated Phone Number | `createPortingAssociatedPhoneNumber` | Creates a new associated phone number for a porting order. This is used for partial porting in GB to specify which phone numbers should be kept or disconnected. |
| Create an Async CSV Import Job | `createEmailBlockImport` | Accepts multipart/form-data with a file field (the CSV) and an optional block ttl days (integer 0, default 30). Validates: - content ≤ 25 MiB, else 413 - row count ≤ 250 000, else 413 - header-only / all-blank / undetectable provider → 400 Returns 202 with the import record (status pending ); an Oban worker ( EmailBlockImportWorker , max attempts 3) transitions pending → processing → completed \| failed . block ttl days applies only to imported manual block rows; other reasons get expires at: nil . Provider is auto-detected from the CSV header ( sendgrid / mailgun / ses / generic ). |
| Create an Email Domain | `createEmailDomain` | Create an email domain |
| Create an Email Template | `createEmailTemplate` | Creates a Liquid email template. Variables are auto-extracted when omitted. |
| Create an Enterprise | `createEnterprise` | Create the legal entity (enterprise) that represents your business on the Telnyx platform. The response carries a server-assigned id you use for every subsequent call. An enterprise is created once and reused; the API collects all required fields up front. Common failure modes: - 422 - a required field is missing or malformed (the response errors[].source.pointer names the field). - 409 - an enterprise with the same identifying details already exists under your account. |
| Create an FQDN | `createFqdn` | Create a new FQDN object. |
| Create an FQDN Connection | `createFqdnConnection` | Creates a FQDN connection. |
| Create an Inexplicit Number Order | `createInexplicitNumberOrder` | Create an inexplicit number order to programmatically purchase phone numbers without specifying exact numbers. |
| Create an Inventory Coverage Request | `createInventoryCoverage` | Creates an inventory coverage request. If locality, npa or national destination code is used in groupBy, and no region or locality filters are used, the whole paginated set is returned. |
| Create an IP | `createIp` | Create a new IP object. |
| Create an IP Connection | `createIpConnection` | Creates an IP connection. |
| Create an OpenAI-compatible Response | `chatpublicopenairesponsescompletionspost` | Create a response using Telnyx's OpenAI-compatible Responses API. This endpoint is compatible with the OpenAI Responses API and may be used with the OpenAI JS or Python SDK by setting the base URL to https://api.telnyx.com/v2/ai/openai . The conversation parameter refers to a Telnyx Conversation rather than an OpenAI-hosted conversation object. To persist a thread across turns, first create a conversation with POST /ai/conversations , then pass that conversation's id in the Responses request as conversation . The endpoint appends the new input, assistant output, reasoning, and tool-call messages to that conversation. Reuse the same conversation id on subsequent Responses requests, including tool-result followups, so the model receives the prior context. If conversation is omitted, the request is processed without persisting messages to a Telnyx conversation. Use the Conversations API to manage history: list conversations (optionally filtered by metadata), fetch messages for a. |
| Create an Outbound Voice Profile | `createVoiceProfile` | Create an outbound voice profile. |
| Create an Unsubscribe Group | `createUnsubscribeGroup` | Create an unsubscribe group |
| Create Auto-response Setting | `createAutorespConfig` | Create auto-response setting |
| Create Brand | `createBrandPost` | This endpoint is used to create a new brand. A brand is an entity created by The Campaign Registry (TCR) that represents an organization or a company. It is this entity that TCR created campaigns will be associated with. Each brand creation will entail an upfront, non-refundable $4 expense. |
| Create Canary Deploy | `createcanarydeployassistantsassistantidcanarydeployspost` | Endpoint to create a canary deploy configuration for an assistant. Creates a new canary deploy configuration with multiple version IDs and their traffic percentages for A/B testing or gradual rollouts of assistant versions. |
| Create Client Token to Join a Room. | `createRoomClientToken` | Synchronously create an Client Token to join a Room. Client Token is necessary to join a Telnyx Room. Client Token will expire after token ttl secs , a Refresh Token is also provided to refresh a Client Token, the Refresh Token expires after refresh token ttl secs . |
| Create Conference | `createConference` | Create a conference from an existing call leg using a call control id and a conference name. Upon creating the conference, the call will be automatically bridged to the conference. Conferences will expire after all participants have left the conference or after 4 hours regardless of the number of active participants. Expected Webhooks: - conference.created - conference.participant.joined - conference.participant.left - conference.ended - conference.recording.saved - conference.floor.changed |
| Create Default Gateway. | `createDefaultGateway` | Create Default Gateway. |
| Create Embeddings | `createopenaiembeddings` | Creates an embedding vector representing the input text. This endpoint is compatible with the OpenAI Embeddings API and may be used with the OpenAI JS or Python SDK by setting the base URL to https://api.telnyx.com/v2/ai/openai . |
| Create Hosted Number Verification Codes | `createVerificationCodesForMessagingHostedNumberOrder` | Create verification codes to validate numbers of the hosted order. The verification codes will be sent to the numbers of the hosted order. |
| Create Initial Plan | `postpublicmissionsmissionsmissionidrunsrunidplan` | Create the initial plan for a run |
| Create Insight Template | `createinsight` | Create a new insight |
| Create Insight Template Group | `createinsightgroup` | Create a new insight group |
| Create Knowledge Base | `postpublicmissionsmissionsmissionidknowledgebases` | Create a new knowledge base for a mission |
| Create MCP Server | `createmcpserver` | Create a new MCP server. |
| Create MCP Server | `postpublicmissionsmissionsmissionidmcpservers` | Create a new MCP server for a mission |
| Create MDR Usage Report | `submitUsageReport` | Submit request for new new messaging usage report. This endpoint will pull and aggregate messaging data in specified time period. |
| Create Message | `addnewmessage` | Add a new message to the conversation. Used to insert a new messages to a conversation manually ( without using chat endpoint ) |
| Create Message Template | `createMessageTemplate` | Create a new Verify profile message template. |
| Create Mission | `postpublicmissionsmissions` | Create a new mission definition |
| Create New Access IP Address | `createAccessIpAddress` | Create new Access IP Address |
| Create New Access IP Range | `createAccessIPRange` | Create new Access IP Range |
| Create New Phone Number Campaign | `createPhoneNumberCampaign` | Create New Phone Number Campaign |
| Create New Phone Number Campaign | `putPhoneNumberCampaign` | Create New Phone Number Campaign |
| Create OAuth Client | `createOAuthClient` | Create a new OAuth client |
| Create OAuth Grant | `createOAuthGrant` | Create an OAuth authorization grant |
| Create or Add a Version to a Voice Design | `createVoiceDesign` | Creates a new voice design (version 1) when voice design id is omitted. When voice design id is provided, adds a new version to the existing design instead. A design can have at most 50 versions. |
| Create or Send an Email Message | `createEmailMessage` | Queues, schedules, or sandbox-sends an email message. The legacy /v2/emails POST route is a backward-compatible alias for this operation. subject is required unless template id is supplied. When using template id , do not also provide subject , html body , or text body ; the template is rendered with template variables . Note: template lookup failures (not found, wrong account) return 400, not 404. |
| Create Presigned Object URL | `createPresignedObjectUrl` | Returns a timed and authenticated URL to download (GET) or upload (PUT) an object. This is the equivalent to AWS S3’s “presigned” URL. Please note that Telnyx performs authentication differently from AWS S3 and you MUST NOT use the presign method of AWS s3api CLI or SDK to generate the presigned URL. Refer to: https://developers.telnyx.com/docs/cloud-storage/presigned-urls |
| Create Tool | `createtoolpost` | Create Tool |
| Create Tool | `postpublicmissionsmissionsmissionidtools` | Create a new tool for a mission |
| Create User Bundles | `createUserBundlesBulk` | Creates multiple user bundles for the user. |
| Create Voicemail | `createVoicemail` | Create voicemail settings for a phone number |
| Creates a Fax Application | `createFaxApplication` | Creates a new Fax Application based on the parameters sent in the request. The application name and webhook URL are required. Once created, you can assign phone numbers to your application using the /phone numbers endpoint. |
| Creates a New Mobile Push Credential | `createPushCredential` | Creates a new mobile push credential |
| Creates a TeXML Application | `createTexmlApplication` | Creates a TeXML Application. |
| Creates a User Address | `createUserAddress` | Creates a user address. |
| Creates an Address | `createAddress` | Creates an address. |
| Creates an Authentication Provider | `createAuthenticationProvider` | Creates an authentication provider. |
| Creates an External Connection | `createExternalConnection` | Creates a new External Connection based on the parameters sent in the request. The external sip connection and outbound voice profile id are required. Once created, you can assign phone numbers to your application using the /phone numbers endpoint. |
| Creates an Upload Request | `createExternalConnectionUpload` | Creates a new Upload request to Microsoft teams with the included phone numbers. Only one of civic address id or location id must be provided, not both. The maximum allowed phone numbers for the numbers ids array is 1000. |
| Deactivate Campaign | `deactivateCampaign` | Terminate a campaign. Note that once deactivated, a campaign cannot be restored. |
| Deactivate User Bundle | `deactivateUserBundle` | Deactivates a user bundle by its ID. |
| Delete a Batch of Numbers | `createDeletePhoneNumbersJob` | Creates a new background job to delete a batch of numbers. At most one thousand numbers can be updated per API call. |
| Delete a Billing Group | `deleteBillingGroup` | Delete a billing group |
| Delete a Call Control Application | `deleteCallControlApplication` | Deletes a call control application. |
| Delete a Call Recording | `deleteRecording` | Permanently deletes a call recording. |
| Delete a CDR Report Request | `deleteCdrRequest` | Deletes a specific CDR report request by ID |
| Delete a CloudFS Filesystem | `deleteCloudfsFilesystem` | Permanently deletes a CloudFS filesystem, removing its S3 bucket and its metadata database. Deletion is synchronous: the response returns the filesystem's final state with status deleted . There is no restore. A filesystem that is still provisioning returns a 409 . If the filesystem still contains data, the request may be rejected with a 409 — drain the bucket and retry. |
| Delete a Cluster | `deleteclusterbytaskidpublictextclusterstaskiddelete` | Delete a cluster |
| Delete a Conference Participant | `deleteTexmlConferenceParticipant` | Deletes a conference participant |
| Delete a Conversation | `deleteconversationbyidpublicconversationsdelete` | Delete a specific conversation by its ID. |
| Delete a Credential | `deleteTelephonyCredential` | Delete an existing credential. |
| Delete a Credential Connection | `deleteCredentialConnection` | Deletes an existing credential connection. |
| Delete a DIR | `deleteDirSimple` | Delete a DIR. Failure modes: 400 if a child phone number is in a non-deletable status, 409 if the DIR has an unresolved infringement claim, 404 if the DIR is not yours. |
| Delete a Document | `deleteDocument` | Delete a document. A document can only be deleted if it's not linked to a service. If it is linked to a service, it must be unlinked prior to deleting. |
| Delete a Dynamic Emergency Address | `deleteDynamicEmergencyAddress` | Deletes the dynamic emergency address based on the ID provided |
| Delete a Dynamic Emergency Endpoint | `deleteDynamicEmergencyEndpoint` | Deletes the dynamic emergency endpoint based on the ID provided |
| Delete a Fax | `deleteFax` | Delete a fax |
| Delete a Global IP | `deleteGlobalIp` | Delete a Global IP. |
| Delete a Global IP Assignment | `deleteGlobalIpAssignment` | Delete a Global IP assignment. |
| Delete a Global IP Health Check | `deleteGlobalIpHealthCheck` | Delete a Global IP health check. |
| Delete a Key | `deleteKvKey` | Deletes a key. Idempotent: deleting a key that does not exist still succeeds. The namespace itself must exist and be provisioned. |
| Delete a KV Namespace | `deleteKvNamespace` | Deletes a KV namespace and all of the keys it contains. Deletion is asynchronous: the namespace is returned with status deleting . Deleting a namespace whose deletion is already in progress returns a 409 . |
| Delete a List of Call Recordings | `deleteRecordings` | Permanently deletes a list of call recordings. |
| Delete a LOA Configuration | `deleteLoaConfiguration` | Delete a specific LOA configuration. |
| Delete a MDR Detailed Report Request | `deleteMdrRequest` | Deletes a specific MDR detailed report request by ID |
| Delete a Messaging Hosted Number | `deleteMessagingHostedNumber` | Delete a messaging hosted number |
| Delete a Messaging Hosted Number Order | `deleteMessagingHostedNumberOrder` | Delete a messaging hosted number order and all associated phone numbers. |
| Delete a Messaging Profile | `deleteMessagingProfile` | Delete a messaging profile |
| Delete a Migration Source | `deleteMigrationSource` | Delete a Migration Source |
| Delete a Mobile Voice Connection | `deleteMobileVoiceConnection` | Delete a Mobile Voice Connection |
| Delete a Network | `deleteNetwork` | Delete a Network. |
| Delete a Notification Channel | `deleteNotificationChannel` | Delete a notification channel. |
| Delete a Notification Profile | `deleteNotificationProfile` | Delete a notification profile. |
| Delete a Notification Setting | `deleteNotificationSetting` | Delete a notification setting. |
| Delete a Phone Number | `deletePhoneNumber` | Delete a phone number |
| Delete a Phone Number Block | `deletePortingPhoneNumberBlock` | Deletes a phone number block. |
| Delete a Phone Number Extension | `deletePortingPhoneNumberExtension` | Deletes a phone number extension. |
| Delete a Porting Order | `deletePortingOrder` | Deletes an existing porting order. This operation is restrict to porting orders in draft state. |
| Delete a Private Wireless Gateway | `deleteWirelessGateway` | Deletes the Private Wireless Gateway. |
| Delete a Pronunciation Dictionary | `deletePronunciationDict` | Permanently delete a pronunciation dictionary. |
| Delete a Public Internet Gateway | `deletePublicInternetGateway` | Delete a Public Internet Gateway. |
| Delete a Queue | `deleteQueue` | Delete an existing call queue. |
| Delete a Queue Resource | `deleteTexmlQueue` | Delete a queue resource. |
| Delete a Recording Transcription | `deleteRecordingTranscription` | Permanently deletes a recording transcription. |
| Delete a Recording Transcription | `deleteTeXMLRecordingTranscription` | Permanently deletes a recording transcription. |
| Delete a Requirement Group by ID | `deleteRequirementGroup` | Delete a requirement group by ID |
| Delete a Room Composition. | `deleteRoomComposition` | Synchronously delete a room composition. |
| Delete a Room Recording. | `deleteRoomRecording` | Synchronously delete a Room Recording. |
| Delete a Room. | `deleteRoom` | Synchronously delete a Room. Participants from that room will be kicked out, they won't be able to join that room anymore, and you won't be charged anymore for that room. |
| Delete a Scheduled Event | `deletescheduledevent` | If the event is pending, this will cancel the event. Otherwise, this will simply remove the record of the event. |
| Delete a SIM Card Group | `deleteSimCardGroup` | Permanently deletes a SIM card group |
| Delete a SIPREC Connector | `deleteSiprecConnector` | Deletes a stored SIPREC connector. |
| Delete a Specific Assistant Version | `deleteassistantversionpublicassistantsassistantidversionsversioniddelete` | Permanently removes a specific version of an assistant. Can not delete main version |
| Delete a Specific Version of a Voice Design | `deleteVoiceDesignVersion` | Permanently deletes a specific version of a voice design. The version number must be a positive integer. |
| Delete a Speech to Text Batch Report Request | `deleteSttRequest` | Deletes a specific Speech to Text batch report request by ID |
| Delete a Stored Credential | `deleteCustomStorageCredentials` | Deletes a stored custom credentials configuration. |
| Delete a Traffic Policy Profile | `deleteTrafficPolicyProfile` | Deletes the traffic policy profile. |
| Delete a UAC Connection | `deleteUacConnection` | Deletes an existing UAC connection. |
| Delete a V2 Legacy Usage CDR Report Request | `deleteCdrUsageReport` | Deletes a specific V2 legacy usage CDR report request by ID |
| Delete a V2 Legacy Usage MDR Report Request | `deleteMdrUsageReport` | Deletes a specific V2 legacy usage MDR report request by ID |
| Delete a Verified Number | `deleteVerifiedNumber` | Delete a verified number |
| Delete a Virtual Cross Connect | `deleteVirtualCrossConnect` | Delete a Virtual Cross Connect. |
| Delete a Voice Clone | `deleteVoiceClone` | Permanently deletes a voice clone. This action cannot be undone. |
| Delete a Voice Design | `deleteVoiceDesign` | Permanently deletes a voice design and all of its versions. This action cannot be undone. |
| Delete a Webhook | `deleteEmailDomainWebhook` | Delete a webhook |
| Delete a Whatsapp Business Account | `deleteWaba` | Delete a Whatsapp Business Account |
| Delete a Whatsapp Message Template | `deleteWhatsappTemplate` | Delete a Whatsapp message template |
| Delete a Whatsapp Phone Number | `deleteWhatsappPhoneNumber` | Delete a Whatsapp phone number |
| Delete a WireGuard Interface | `deleteWireguardInterface` | Delete a WireGuard Interface. |
| Delete a Wireless Blocklist | `deleteWirelessBlocklist` | Deletes the Wireless Blocklist. |
| Delete a Wireless Detail Record (WDR) Report | `deleteWdrReport` | Deletes one specific WDR report. |
| Delete Access IP Address | `deleteAccessIpAddress` | Delete access IP address |
| Delete Access IP Ranges | `deleteAccessIpRange` | Delete access IP ranges |
| Delete an Additional Document | `deleteAdditionalDocument` | Deletes an additional document for a porting order. |
| Delete an Alphanumeric Sender ID | `deleteAlphanumericSenderId` | Delete an alphanumeric sender ID and disassociate it from its messaging profile. |
| Delete an Assistant | `deleteassistantpublicassistantsassistantiddelete` | Delete an AI Assistant by assistant id . |
| Delete an Assistant Test | `deleteassistanttestpublicassistantsteststestiddelete` | Permanently removes an assistant test and all associated data |
| Delete an Associated Phone Number | `deletePortingAssociatedPhoneNumber` | Deletes an associated phone number from a porting order. |
| Delete an Email Domain | `deleteEmailDomain` | Delete an email domain |
| Delete an Email Template | `deleteEmailTemplate` | Delete an email template |
| Delete an Enterprise | `deleteEnterprise` | Soft-delete an enterprise. Failure modes: - 400 - the enterprise still has dependent resources in a non-deletable state. Remove those first; the response detail identifies what is blocking the delete. - 409 - the enterprise has a dependent resource with an unresolved claim. Resolve it before deleting. - 404 - the enterprise does not exist or does not belong to your account. |
| Delete an FQDN | `deleteFqdn` | Delete an FQDN. |
| Delete an FQDN Connection | `deleteFqdnConnection` | Deletes an FQDN connection. |
| Delete an Integration Secret | `deleteintegrationsecret` | Delete an integration secret given its ID. |
| Delete an IP | `deleteIp` | Delete an IP. |
| Delete an IP Connection | `deleteIpConnection` | Deletes an existing IP connection. |
| Delete an Outbound Voice Profile | `deleteOutboundVoiceProfile` | Deletes an existing outbound voice profile. |
| Delete an Unsubscribe Group | `deleteUnsubscribeGroup` | If the group has 0 active suppressions, hard-deletes the row. With force=true , soft-deletes all active suppressions first (status → removed , group id cleared, removed audit event per block) in a single transaction, then hard-deletes the group. Without force and active suppressions present → 409 . Audit trail is preserved. force only accepts the string "true" or boolean true ; all other values are false. |
| Delete Auto-Response Setting | `deleteAutorespConfig` | Delete Auto-Response Setting |
| Delete Brand | `deleteBrand` | Delete Brand. This endpoint is used to delete a brand. Note the brand cannot be deleted if it contains one or more active campaigns, the campaigns need to be inactive and at least 3 months old due to billing purposes. |
| Delete Canary Deploy | `deletecanarydeployassistantsassistantidcanarydeploysdelete` | Endpoint to delete a canary deploy configuration for an assistant. Removes all canary deploy configurations for the specified assistant. |
| Delete Default Gateway. | `deleteDefaultGateway` | Delete Default Gateway. |
| Delete Insight Template | `deleteinsightbyid` | Delete insight by ID |
| Delete Insight Template Group | `deleteinsightgroupbyid` | Delete insight group by ID |
| Delete Integration Connection | `deleteintegrationconnection` | Delete a specific integration connection. |
| Delete Knowledge Base | `deletepublicmissionsmissionsmissionidknowledgebasesknowledgebaseid` | Delete a knowledge base from a mission |
| Delete MCP Server | `deletemcpserver` | Delete a specific MCP server. |
| Delete MCP Server | `deletepublicmissionsmissionsmissionidmcpserversmcpserverid` | Delete an MCP server from a mission |
| Delete MDR Usage Report | `deleteUsageReport` | Delete messaging usage report by id |
| Delete Mission | `deletepublicmissionsmissionsmissionid` | Delete a mission |
| Delete OAuth Client | `deleteOAuthClient` | Delete an OAuth client |
| Delete Organization User | `deleteOrganizationUser` | Deletes a user in your organization. |
| Delete Phone Number Campaign | `deletePhoneNumberCampaign` | This endpoint allows you to remove a campaign assignment from the supplied phoneNumber . |
| Delete Recording Resource | `deleteTeXMLCallRecording` | Deletes recording resource identified by recording id. |
| Delete Several Room Recordings in a Bulk. | `deleteRoomRecordings` | Delete several room recordings in a bulk. |
| Delete SIM Card Data Usage Notifications | `deleteSimCardDataUsageNotifications` | Delete the SIM Card Data Usage Notification. |
| Delete Stored Dialogflow Connection | `deleteDialogflowConnection` | Deletes a stored Dialogflow Connection. |
| Delete Telco Data Usage Report | `deleteTelcoDataUsageReport` | Delete a specific telco data usage report by its ID |
| Delete the WireGuard Peer | `deleteWireguardPeer` | Delete the WireGuard peer. |
| Delete Tool | `deletepublicmissionsmissionsmissionidtoolstoolid` | Delete a tool from a mission |
| Delete Tool | `deletetooltoolid` | Delete Tool |
| Delete Verification Request | `deleteVerificationRequest` | Delete a verification request A request may only be deleted when when the request is in the "rejected" state. HTTP 200 : request successfully deleted HTTP 400 : request exists but can't be deleted (i.e. not rejected) HTTP 404 : request unknown or already deleted |
| Delete Verify Profile | `deleteProfile` | Delete Verify profile |
| Delete Whatsapp Profile Photo | `deleteWhatsappProfilePhoto` | Delete Whatsapp profile photo |
| Deletes a Fax Application | `deleteFaxApplication` | Permanently deletes a Fax Application. Deletion may be prevented if the application is in use by phone numbers. |
| Deletes a Mobile Push Credential | `deletePushCredentialById` | Deletes a mobile push credential based on the given push credential id |
| Deletes a SIM Card | `deleteSimCard` | The SIM card will be decommissioned, removed from your account and you will stop being charged. The SIM card won't be able to connect to the network after the deletion is completed, thus making it impossible to consume data. Transitioning to the disabled state may take a period of time. Until the transition is completed, the SIM card status will be disabling disabling . In order to re-enable the SIM card, you will need to re-register it. |
| Deletes a TeXML Application | `deleteTexmlApplication` | Deletes a TeXML Application. |
| Deletes All Numbers Associated with a Phone Number Block | `createPhoneNumberBlockDeletionJob` | Creates a new background job to delete all the phone numbers associated with the given block. We will only consider the phone number block as deleted after all phone numbers associated with it are removed, so multiple executions of this job may be necessary in case some of the phone numbers present errors during the deletion process. |
| Deletes an Address | `deleteAddress` | Deletes an existing address. |
| Deletes an Authentication Provider | `deleteAuthenticationProvider` | Deletes an existing authentication provider. |
| Deletes an External Connection | `deleteExternalConnection` | Permanently deletes an External Connection. Deletion may be prevented if the application is in use by phone numbers, is active, or if it is an Operator Connect connection. To remove an Operator Connect integration please contact Telnyx support. |
| Deletes Stored Media | `deleteMediaStorage` | Deletes a stored media file. |
| Dial | `dialCall` | Dial a number or SIP URI from a given connection. A successful response will include a call leg id which can be used to correlate the command with subsequent webhooks. Expected Webhooks: - call.initiated - call.answered or call.hangup - call.hold and call.unhold if the call is held/unheld - call.machine.detection.ended if answering machine detection was requested - call.machine.greeting.ended if answering machine detection was requested to detect the end of machine greeting - call.machine.premium.detection.ended if answering machine detection=premium was requested - call.machine.premium.greeting.ended if answering machine detection=premium was requested and a beep was detected - call.deepfake detection.result if deepfake detection was enabled - call.deepfake detection.error if deepfake detection was enabled and an error occurred - streaming.started , streaming.stopped or streaming.failed if stream url was set When the record parameter is set to record-from-answer , the response will. |
| Dial a New Conference Participant | `dialTexmlConferenceParticipant` | Dials a new conference participant |
| Disable AI for an Embedded Bucket | `embeddingbucketfilespublicembeddingbucketsbucketnamedelete` | Deletes an entire bucket's embeddings and disables the bucket for AI-use, returning it to normal storage pricing. |
| Disable Phone-number Reputation for an Enterprise | `disableReputationSettings` | Disable Phone Number Reputation. All registered numbers are de-registered as a cascade. The enterprise itself is unaffected. Returns 204 on success, 404 if reputation is not enabled for this enterprise. |
| Disables a Managed Account | `disableManagedAccount` | Disables a managed account, forbidding it to use Telnyx services, including sending or receiving phone calls and SMS messages. Ongoing phone calls will not be affected. The managed account and its sub-users will no longer be able to log in via the mission control portal. |
| Dismiss a Log Message | `deleteExternalConnectionLogMessage` | Dismiss a log message for an external connection associated with your account. |
| Display Information About Allocatable Global Outbound Channels for the Current User. | `listAllocatableGlobalOutboundChannels` | Display information about allocatable global outbound channels for the current user. Only usable by account managers. |
| Download a Document | `downloadDocument` | Download a document. |
| Download a Porting Order Loa Template | `getPortingOrderLoaTemplate` | Download a porting order loa template |
| Download a Sub Number Orders Report | `downloadSubNumberOrdersReport` | Download the CSV file for a completed sub number orders report. The report status must be 'success' before the file can be downloaded. |
| Download Stored Media | `downloadMedia` | Downloads a stored media file. |
| Download Voice Clone Audio Sample | `getVoiceCloneSample` | Downloads the WAV audio sample that was used to create the voice clone. |
| Download Voice Design Audio Sample | `getVoiceDesignSample` | Downloads the WAV audio sample for the voice design. Returns the latest version's sample by default, or a specific version when ?version=N is provided. The id parameter accepts either a UUID or the design name. |
| Dynamic Client Registration | `registerOAuthClient` | Register a new OAuth client dynamically (RFC 7591) |
| Edit a Porting Order | `updatePortingOrder` | Edits the details of an existing porting order. Any or all of a porting orders attributes may be included in the resource object included in a PATCH request. If a request does not include all of the attributes for a resource, the system will interpret the missing attributes as if they were included with their current values. To explicitly set something to null, it must be included in the request with a null value. |
| Embed Documents | `postEmbedding` | Perform embedding on a Telnyx Storage Bucket using the a embedding model. The current supported file types are: - PDF - HTML - txt/unstructured text files - json - csv - audio / video (mp3, mp4, mpeg, mpga, m4a, wav, or webm ) - Max of 100mb file size. Any files not matching the above types will be attempted to be embedded as unstructured text. This process can be slow, so it runs in the background and the user can check the status of the task using the endpoint /ai/embeddings/{task id} . Important Note : When you update documents in a Telnyx Storage bucket, their associated embeddings are automatically kept up to date. If you add or update a file, it is automatically embedded. If you delete a file, the embeddings are deleted for that particular file. You can also specify a custom loader param. Currently the only supported loader value is intercom which loads Intercom article jsons as specified by the Intercom article API This loader will split each article into paragraphs and save. |
| Embed URL Content | `postEmbeddingUrl` | Embed website content from a specified URL, including child pages up to 5 levels deep within the same domain. The process crawls and loads content from the main URL and its linked pages into a Telnyx Cloud Storage bucket. As soon as each webpage is added to the bucket, its content is immediately processed for embeddings, that can be used for similarity search and clustering. |
| Enable Emergency for a Phone Number | `enablePhoneNumberEmergency` | Enable emergency for a phone number |
| Enable or Disable Whatsapp Calling for a Phone Number | `patchWhatsappCallingSettings` | Enable or disable Whatsapp calling for a phone number |
| Enable Phone-number Reputation for an Enterprise | `enableReputationSettings` | Activate Phone Number Reputation for the given enterprise. Requires an uploaded Letter of Authorization document (the loa document id references the Telnyx Documents API) and a refresh-frequency selection. After activation, individual phone numbers can be registered via POST .../reputation/numbers . Prerequisite : the calling user must have agreed to the Phone Number Reputation Terms of Service ( POST /terms of service/number reputation/agree ). Failure modes: - 403 - Phone Number Reputation Terms of Service not accepted. - 404 - enterprise does not exist or does not belong to your account. - 400 - reputation already enabled for this enterprise. - 422 - loa document id missing or check frequency invalid. Pricing: This is a billable action. See https://telnyx.com/pricing/numbers for current pricing. |
| Enables a Managed Account | `enableManagedAccount` | Enables a managed account and its sub-users to use Telnyx services. |
| End a Conference | `endConference` | End a conference and terminate all active participants. |
| End a Room Session. | `endSession` | Note: this will also kick all participants currently present in the room |
| Enhance Assistant Instructions | `enhanceassistantinstructionspublicassistantsassistantidinstructionsenhancepost` | Enhance an assistant's instructions using an LLM. The endpoint reads the assistant's current instructions and tools, then streams back improved instructions as they are generated. Optionally provide an enhancement prompt to steer the changes (for example, "make the instructions more concise" or "add error handling guidance"). When omitted, the assistant's existing instructions are used as the basis for the enhancement. The enhancement focuses on tool-calling reliability, clarity and precision, completeness and error handling, tool schema alignment, and conversation flow structure. The response is streamed as text/plain using chunked transfer encoding; consume the body incrementally to render the enhanced instructions as they arrive. |
| Enqueue Call | `enqueueCall` | Put the call in a queue. |
| Export Suppressions as CSV | `exportEmailBlocks` | Streams the account's suppressions as a chunked CSV (server-side cursor; never materialized). Content-type text/csv , header Content-Disposition: attachment; filename="email blocks export.csv" . Filters ( filter[reason] , filter[domain id] , filter[created after] , filter[created before] ) are the only params that affect output. sort and page[ ] are parsed (bad values still produce 400 ) but ignored — rows stream ORDER BY created at ASC, id ASC with no pagination. CSV columns: id,to,from,reason,source,scope,status,domain id, created at,updated at,expires at,group id . The CSV carries the group id column so group-scoped suppressions' group link survives the export (empty for account-scope rows). |
| Extend a Number Reservation | `extendNumberReservationExpiryTime` | Extends reservation expiry time on all phone numbers. |
| Fetch a Call | `getTexmlCall` | Returns an individual call identified by its CallSid. This endpoint is eventually consistent. |
| Fetch a Cluster | `fetchclusterbytaskidpublictextclusterstaskidget` | Fetch a cluster |
| Fetch a Cluster Visualization | `fetchclusterimagebytaskidpublictextclusterstaskidimageget` | Fetch a cluster visualization |
| Fetch a Conference Resource | `getTexmlConference` | Returns a conference resource. |
| Fetch a Queue Resource | `getTexmlQueue` | Returns a queue resource. |
| Fetch a Recording Transcription Resource | `getTeXMLRecordingTranscription` | Returns the recording transcription resource identified by its ID. |
| Fetch All MDR Records | `getPaginatedMdrs` | Fetch all Mdr records |
| Fetch All Messaging Usage Reports | `getMdrUsageReportsGet` | Fetch all messaging usage reports. Usage reports are aggregated messaging data for specified time period and breakdown |
| Fetch Multiple Call Resources | `getTexmlCalls` | Returns multiple call resouces for an account. This endpoint is eventually consistent. |
| Fetch Multiple Recording Resources | `getTeXMLCallRecordings` | Returns multiple recording resources for an account. |
| Fetch Recording Resource | `getTeXMLCallRecording` | Returns recording resource identified by recording id. |
| Fetch Recordings for a Call | `fetchTeXMLCallRecordings` | Returns recordings for a call identified by call sid. |
| Fetch Recordings for a Conference | `fetchTeXMLConferenceRecordings` | Returns recordings for a conference identified by conference sid. |
| Fetch Whatsapp User Data | `getWhatsappUserData` | Fetch Whatsapp user data |
| Fetches All WDR Records | `getPaginatedWdrs` | Fetch all Wdr records |
| Find Webhook Delivery Details by ID | `getWebhookDelivery` | Provides webhook delivery debug data, such as timestamps, delivery status and attempts. |
| Force a Reputation Refresh | `refreshReputationNumbers` | Immediately refresh the stored reputation data for the listed numbers. This is in addition to the periodic refresh determined by check frequency . Up to 100 numbers per call. The response carries the kicked-off jobs; the actual refresh runs asynchronously. Pricing: Forcing a refresh performs live reputation lookups, which are billable. See https://telnyx.com/pricing/numbers for current pricing. |
| Force Remove a Call from a Queue | `removeQueueCall` | Removes an inactive call from a queue. If the call is no longer active, use this command to remove it from the queue. |
| Forking Start | `startCallFork` | Call forking allows you to stream the media from a call to a specific target in realtime. This stream can be used to enable realtime audio analysis to support a variety of use cases, including fraud detection, or the creation of AI-generated audio responses. Requests must specify either the target attribute or the rx and tx attributes. Expected Webhooks: - call.fork.started - call.fork.stopped |
| Forking Stop | `stopCallFork` | Stop forking a call. Expected Webhooks: - call.fork.stopped |
| Gather | `gatherCall` | Gather DTMF signals to build interactive menus. You can pass a list of valid digits. The Answer command must be issued before the gather command. Expected Webhooks: - call.dtmf.received (you may receive many of these webhooks) - call.gather.ended |
| Gather DTMF Using Audio Prompt in a Conference | `conferenceGatherUsingAudio` | Play an audio file to a specific conference participant and gather DTMF input. |
| Gather Stop | `stopCallGather` | Stop current gather. Expected Webhooks: - call.gather.ended |
| Gather Using AI | `callGatherUsingAI` | Gather parameters defined in the request payload using a voice assistant. You can pass parameters described as a JSON Schema object and the voice assistant will attempt to gather these informations. Expected Webhooks: - call.ai gather.ended - call.conversation.ended - call.ai gather.partial results (if send partial results is set to true ) - call.ai gather.message history updated (if send message history updates is set to true ) |
| Gather Using Audio | `gatherUsingAudio` | Play an audio file on the call until the required DTMF signals are gathered to build interactive menus. You can pass a list of valid digits along with an 'invalid audio url', which will be played back at the beginning of each prompt. Playback will be interrupted when a DTMF signal is received. The Answer command must be issued before the gather using audio command. Expected Webhooks: - call.playback.started - call.playback.ended - call.dtmf.received (you may receive many of these webhooks) - call.gather.ended |
| Gather Using Speak | `gatherUsingSpeak` | Convert text to speech and play it on the call until the required DTMF signals are gathered to build interactive menus. You can pass a list of valid digits along with an 'invalid payload', which will be played back at the beginning of each prompt. Speech will be interrupted when a DTMF signal is received. The Answer command must be issued before the gather using speak command. Expected Webhooks: - call.dtmf.received (you may receive many of these webhooks) - call.gather.ended |
| Generate a Temporary Download Link for a Document | `getDocumentDownloadLink` | Generates a temporary pre-signed URL that can be used to download the document directly from the storage backend without authentication. |
| Generate and Fetch MDR Usage Report | `getMDRUsageReportSync` | Generate and fetch messaging usage report synchronously. This endpoint will both generate and fetch the messaging report over a specified time period. No polling is necessary but the response may take up to a couple of minutes. |
| Generate RCS Deeplink | `generateRCSDeeplink` | Generate a deeplink URL that can be used to start an RCS conversation with a specific agent. |
| Generate Speech from Text | `generateSpeech` | Generate synthesized speech audio from text input. Returns audio in the requested format (binary audio stream, base64-encoded JSON, or an audio URL for later retrieval). Authentication is provided via the standard Authorization: Bearer header. The voice parameter provides a convenient shorthand to specify provider, model, and voice in a single string (e.g. telnyx.NaturalHD.Alloy or Telnyx.Ultra. ). Alternatively, specify provider explicitly along with provider-specific parameters. Supported providers: aws , telnyx , azure , elevenlabs , minimax , rime , resemble , xai . The Telnyx Ultra model supports 44 languages with emotion control, speed adjustment, and volume control. Use the telnyx provider-specific parameters to configure these features. |
| Generates and Fetches CDR Usage Reports | `getCDRUsageReportSync` | Generate and fetch voice usage report synchronously. This endpoint will both generate and fetch the voice report over a specified time period. No polling is necessary but the response may take up to a couple of minutes. |
| Get a Batch Email Validation Job | `getEmailValidationBatch` | Retrieves the current status and, once completed, validation results for a batch job. |
| Get a Billing Group | `getBillingGroup` | Get a billing group |
| Get a CDR Usage Report | `getCdrUsageReport` | Fetch single cdr usage report by id. |
| Get a CloudFS Filesystem | `getCloudfsFilesystem` | Retrieves a CloudFS filesystem by its ID. The returned meta url omits the credential — the metadata token is only ever returned by create and rotate-meta-token. A filesystem whose last lifecycle action failed includes a customer-safe error message. |
| Get a Conversation | `getconversationbyidpublicconversationsget` | Retrieve a specific AI conversation by its ID. |
| Get a Credential | `getTelephonyCredential` | Get the details of an existing On-demand Credential. |
| Get a Customer Service Record | `getCustomerServiceRecord` | Get a specific customer service record. |
| Get a DIR by ID | `getDirByIdSimple` | Returns a single DIR by id. The enterprise is resolved server-side from the DIR id. Returns 404 if the DIR does not exist or is not yours. |
| Get a Dynamic Emergency Address | `getDynamicEmergencyAddress` | Returns the dynamic emergency address based on the ID provided |
| Get a Dynamic Emergency Endpoint | `getDynamicEmergencyEndpoint` | Returns the dynamic emergency endpoint based on the ID provided |
| Get a Fine Tuning Job | `getfinetuningjobpublicfinetuningjobidget` | Retrieve a fine tuning job by job id . |
| Get a Key's Value | `getKvKey` | Returns the raw stored value for a key. The response body is the value exactly as it was written; the Content-Type header echoes the value's stored content type (defaults to application/octet-stream ). |
| Get a KV Namespace | `getKvNamespace` | Retrieves a KV namespace by its ID, including its provisioning status. |
| Get a Ledger Billing Group Report | `getBillingGroupReport` | Get a ledger billing group report |
| Get a Migration | `getMigration` | Get a Migration |
| Get a Migration Source | `getMigrationSource` | Get a Migration Source |
| Get a Notification Channel | `getNotificationChannel` | Get a notification channel. |
| Get a Notification Profile | `getNotificationProfile` | Get a notification profile. |
| Get a Notification Setting | `getNotificationSetting` | Get a notification setting. |
| Get a Phone-number Batch | `getDirPhoneNumberBatchSimplified` | Get a single phone-number batch by id. The enterprise is resolved server-side from the DIR id. |
| Get a Portout Request | `findPortoutRequest` | Returns the portout request based on the ID provided |
| Get a Private Wireless Gateway | `getPrivateWirelessGateway` | Retrieve information about a Private Wireless Gateway. |
| Get a Pronunciation Dictionary | `getPronunciationDict` | Retrieve a single pronunciation dictionary by ID. |
| Get a Reputation Remediation Request | `getReputationRemediation` | Retrieve the full detail of a remediation request, including current status, per-number results (once available), and submission metadata. |
| Get a Reputation-monitored Number (no Enterprise ID Required) | `getPhoneNumberReputationSimplified` | Convenience alias for GET /v2/enterprises/{enterprise id}/reputation/numbers/{phone number} . |
| Get a Scheduled Event | `getscheduledevent` | Retrieve a scheduled event by event ID |
| Get a Single Reputation-monitored Phone Number | `getPhoneNumberReputation` | Retrieve one registered number with its latest reputation snapshot. The phone number path parameter is in E.164 format and must be URL-encoded (e.g. %2B19493253498 ). |
| Get a Single Requirement Group by ID | `getRequirementGroup` | Get a single requirement group by ID |
| Get a Single SIM Card Data Usage Notification | `getSimCardDataUsageNotification` | Get a single SIM Card Data Usage Notification. |
| Get a Single SIM Card Order | `getSimCardOrder` | Get a single SIM card order by its ID. |
| Get a Single Whatsapp Business Account | `getSingleWaba` | Get a single Whatsapp Business Account |
| Get a Specific Assistant Version | `getassistantversionpublicassistantsassistantidversionsversionidget` | Retrieves a specific version of an assistant by assistant id and version id |
| Get a Specific CDR Report Request | `getCdrRequest` | Retrieves a specific CDR report request by ID |
| Get a Specific MDR Detailed Report Request | `getMdrRequest` | Retrieves a specific MDR detailed report request by ID |
| Get a Specific Speech to Text Batch Report Request | `getSttRequest` | Retrieves a specific Speech to Text batch report request by ID |
| Get a Terms of Service Agreement by ID | `getTermsOfServiceAgreement` | Retrieve a single ToS agreement record. Returns 404 if the agreement does not exist or does not belong to the authenticated user. |
| Get a Traffic Policy Profile | `getTrafficPolicyProfile` | Returns the details regarding a specific traffic policy profile. |
| Get a Voice Design | `getVoiceDesign` | Returns the latest version of a voice design, or a specific version when ?version=N is provided. The id parameter accepts either a UUID or the design name. |
| Get a Whatsapp Message Template by ID | `getWhatsappTemplate` | Get a Whatsapp message template by ID |
| Get a Wireless Blocklist | `getWirelessBlocklist` | Retrieve information about a Wireless Blocklist. |
| Get a Wireless Detail Record (WDR) Report | `getWdrReport` | Returns one specific WDR report |
| Get Activation Code for an ESIM | `getSimCardActivationCode` | It returns the activation code for an eSIM. This API is only available for eSIMs. If the given SIM is a physical SIM card, or has already been installed, an error will be returned. |
| Get Advanced Order | `getadvancedorderv2` | Get Advanced Order |
| Get All Available Traffic Policy Profile Services | `getTrafficPolicyProfileServices` | Get all available PCEF services that can be used in traffic policy profiles. |
| Get All CDR Report Requests | `getCdrRequests` | Retrieves all CDR report requests for the authenticated user |
| Get All MDR Detailed Report Requests | `getMdrRequests` | Retrieves all MDR detailed report requests for the authenticated user |
| Get All Outbound Voice Profiles | `listOutboundVoiceProfiles` | Get all outbound voice profiles belonging to the user that match the given filters. |
| Get All Possible Wireless Blocklist Values | `wirelessBlocklistsGetAll` | Retrieve all wireless blocklist values for a given blocklist type. |
| Get All Private Wireless Gateways | `getPrivateWirelessGateways` | Get all Private Wireless Gateways belonging to the user. |
| Get All SIM Card Groups | `getAllSimCardGroups` | Get all SIM card groups belonging to the user that match the given filters. |
| Get All SIM Card Orders | `getSimCardOrders` | Get all SIM card orders according to filters. |
| Get All SIM Cards | `getSimCards` | Get all SIM cards belonging to the user that match the given filters. |
| Get All Speech to Text Batch Report Requests | `getSttRequests` | Retrieves all Speech to Text batch report requests for the authenticated user |
| Get All Tags | `getallassistanttags` | Get All Tags |
| Get All Test Suite Names | `fetchtestsuitespublicassistantsteststestsuitesget` | Retrieves a list of all distinct test suite names available to the current user |
| Get All Traffic Policy Profiles | `getTrafficPolicyProfiles` | Get all traffic policy profiles belonging to the user that match the given filters. |
| Get All Versions of an Assistant | `getassistantversionspublicassistantsassistantidversionsget` | Retrieves all versions of a specific assistant with complete configuration and metadata |
| Get All Wireless Blocklists | `getWirelessBlocklistsGateways` | Get all Wireless Blocklists belonging to the user. |
| Get All Wireless Detail Records (WDRs) Reports | `getWdrReports` | Returns the WDR Reports that match the given parameters. |
| Get All Wireless Regions | `wirelessRegionsGetAll` | Retrieve all wireless regions for the given product. |
| Get an Assistant | `getassistantpublicassistantsassistantidget` | Retrieve an AI Assistant configuration by assistant id . |
| Get an Email Message | `getEmailMessage` | The legacy /v2/emails/{id} GET route is a backward-compatible alias for this operation. |
| Get an Email Template | `getEmailTemplate` | Get an email template |
| Get an Embedding Task's Status | `getEmbeddingTask` | Check the status of a current embedding task. Will be one of the following: - queued - Task is waiting to be picked up by a worker - processing - The embedding task is running - success - Task completed successfully and the bucket is embedded - failure - Task failed and no files were embedded successfully - partial success - Some files were embedded successfully, but at least one failed |
| Get an Enterprise | `getEnterprise` | Retrieve a single enterprise by id. Returns 404 if the id does not exist or does not belong to your account. |
| Get an Infringement Claim | `getInfringementClaim` | Retrieve a single claim by id. Returns 404 if the claim does not exist or is not against a DIR you own. |
| Get an MDR Usage Report | `getMdrUsageReport` | Fetch single MDR usage report by id. |
| Get API Usage | `getStorageAPIUsage` | Returns the detail on API usage on a bucket of a particular time period, group by method category. |
| Get Assignment Task Status | `getAssignmentTaskStatus` | Check the status of the task associated with assigning all phone numbers on a messaging profile to a campaign by taskId . |
| Get Assistant Test by ID | `getassistanttestpublicassistantsteststestidget` | Retrieves detailed information about a specific assistant test |
| Get Assistant TeXML | `getassistanttexmlpublicassistantsassistantidtexmlget` | Get an assistant texml by assistant id . |
| Get Auto-Response Setting | `getAutorespConfig` | Get Auto-Response Setting |
| Get Available CDR Report Fields | `getCdrsAvailableFields` | Retrieves all available fields that can be used in CDR reports |
| Get Available Models | `getmodelspublicmodelsget` | Deprecated : Use GET /v2/ai/openai/models instead. Returns the same ModelsResponse payload as the OpenAI-compatible endpoint — open-source LLMs hosted on Telnyx (e.g. moonshotai/Kimi-K2.6 , zai-org/GLM-5.1-FP8 , MiniMaxAI/MiniMax-M2.7 ), embedding models, and fine-tuned models — kept around for backwards compatibility. New integrations should use /v2/ai/openai/models . Model ids follow the {organization}/{model name} convention from Hugging Face. |
| Get Available Models (OpenAI-compatible) | `listopenaimodels` | Lists every model currently available to your account on Telnyx Inference, including SOTA open-source LLMs hosted on Telnyx GPUs (for example moonshotai/Kimi-K2.6 , zai-org/GLM-5.1-FP8 , and MiniMaxAI/MiniMax-M2.7 ), embedding models, and any fine-tuned models you have created. Each entry is a ModelMetadata object describing the model id, owner, task, context length, supported languages, billing tier, pricing per 1M tokens, deployment regions, and whether the model supports vision or fine-tuning. Use this endpoint to discover model ids you can pass to POST /v2/ai/openai/chat/completions . Model ids follow the {organization}/{model name} convention from Hugging Face (for example moonshotai/Kimi-K2.6 ). This endpoint is OpenAI-compatible: clients pointed at https://api.telnyx.com/v2/ai/openai can call client.models.list() to retrieve the same payload. |
| Get Brand | `getBrand` | Retrieve a brand by brandId . |
| Get Brand Feedback by ID | `getBrandFeedbackById` | Get feedback about a brand by ID. This endpoint can be used after creating or revetting a brand. Possible values for .category[].id : TAX ID - Data mismatch related to tax id and its associated properties. STOCK SYMBOL - Non public entity registered as a public for profit entity or the stock information mismatch. GOVERNMENT ENTITY - Non government entity registered as a government entity. Must be a U.S. government entity. NONPROFIT - Not a recognized non-profit entity. No IRS tax-exempt status found. OTHERS - Details of the data misrepresentation if any. |
| Get Brand SMS OTP Status | `getBrandSmsOtpStatus` | Query the status of an SMS OTP (One-Time Password) for Sole Proprietor brand verification. This endpoint allows you to check the delivery and verification status of an OTP sent during the Sole Proprietor brand verification process. You can query by either: referenceId - The reference ID returned when the OTP was initially triggered brandId - Query parameter for portal users to look up OTP status by Brand ID The response includes delivery status, verification dates, and detailed delivery information. |
| Get Brand SMS OTP Status by Brand ID | `getBrandSmsOtpStatusByBrandId` | Query the status of an SMS OTP (One-Time Password) for Sole Proprietor brand verification using the Brand ID. This endpoint allows you to check the delivery and verification status of an OTP sent during the Sole Proprietor brand verification process by looking it up with the brand ID. The response includes delivery status, verification dates, and detailed delivery information. Note: This is an alternative to the /10dlc/brand/smsOtp/{referenceId} endpoint when you have the Brand ID but not the reference ID. |
| Get Bucket SSL Certificate | `getStorageSSLCertificates` | Returns the stored certificate detail of a bucket, if applicable. |
| Get Bucket Usage | `getBucketUsage` | Returns the amount of storage space and number of files a bucket takes up. |
| Get Bulk SIM Card Action Details | `getBulkSimCardAction` | This API fetches information about a bulk SIM card action. A bulk SIM card action contains details about a collection of individual SIM card actions. |
| Get Bundle by ID | `getBillingBundleById` | Get a single bundle by ID. |
| Get Calling Settings for a Phone Number | `getWhatsappCallingSettings` | Get calling settings for a phone number |
| Get Campaign | `getCampaign` | Retrieve campaign details by campaignId . |
| Get Campaign Cost | `getCampaignCost` | Get Campaign Cost |
| Get Campaign Mno Metadata | `getCampaignMnoMetadata` | Get the campaign metadata for each MNO it was submitted to. |
| Get Campaign Operation Status | `getCampaignOperationStatus` | Retrieve campaign's operation status at MNO level. |
| Get Canary Deploy | `getcanarydeployassistantsassistantidcanarydeploysget` | Endpoint to get a canary deploy configuration for an assistant. Retrieves the current canary deploy configuration with all version IDs and their traffic percentages for the specified assistant. |
| Get Conference Participant Resource | `getTexmlConferenceParticipant` | Gets conference participant resource |
| Get Conversation Messages | `getconversationspublicconversationidmessagesget` | Retrieve messages for a specific conversation, including tool calls made by the assistant. |
| Get Conversation Window Status for a Phone Number | `getWhatsappConversationWindow` | Returns whether the 24-hour conversation window is currently open for a given source/destination pair. If window active is false, only template messages may be sent. |
| Get Country Coverage | `retreiveCountryCoverage` | Get country coverage |
| Get Coverage for a Specific Country | `retreiveSpecificCountryCoverage` | Get coverage for a specific country |
| Get Default Gateway Status. | `getDefaultGateway` | Get Default Gateway status. |
| Get Detailed Messaging Profile Metrics | `getDetailedProfileMetrics` | Get detailed metrics for a specific messaging profile, broken down by time interval. |
| Get Domain Health Summary | `getEmailDomainHealth` | Returns a summary of domain health including verification status and usability. |
| Get Email Event Statistics | `getEmailEventStats` | Returns counts and rates for email events over a time range. The default start time is 30 days ago. |
| Get Email-ownership Verification Status | `getDirEmailVerificationStatus` | Whether the DIR's current authorizer email has been verified. |
| Get Enum | `getEnumEndpoint` | Returns the accepted values for the selected 10DLC enumeration endpoint. Use these values when constructing brand and campaign requests. |
| Get Event Details | `getpublicmissionsmissionsmissionidrunsrunideventseventid` | Get details of a specific event |
| Get File-level Embedding Statuses for a Bucket | `getBucketName` | Get all embedded files for a given user bucket, including their processing status. |
| Get Insight Template | `getinsightbyid` | Get insight by ID |
| Get Insight Template Group | `getinsightgroupbyid` | Get insight group by ID |
| Get Insight Template Groups | `getallinsightgroups` | Get all insight groups |
| Get Insight Templates | `getallinsights` | Get all insights |
| Get Insights for a Conversation | `getconversationspublicconversationidinsightsget` | Retrieve insights for a specific conversation |
| Get Invoice by ID | `getInvoiceById` | Retrieve a single invoice by its unique identifier. |
| Get Knowledge Base | `getpublicmissionsmissionsmissionidknowledgebasesknowledgebaseid` | Get a specific knowledge base by ID |
| Get MCP Server | `getmcpserver` | Retrieve details for a specific MCP server. |
| Get MCP Server | `getpublicmissionsmissionsmissionidmcpserversmcpserverid` | Get a specific MCP server by ID |
| Get Metadata Overview | `getSessionAnalysisMetadata` | Returns all available record types and supported query parameters for session analysis. |
| Get Mission | `getpublicmissionsmissionsmissionid` | Get a mission by ID (includes tools, knowledge bases, mcp servers) |
| Get Monthly Charges Breakdown | `getMonthlyChargesBreakdown` | Retrieve a detailed breakdown of monthly charges for phone numbers in a specified date range. The date range cannot exceed 31 days. |
| Get Monthly Charges Summary | `getMonthlyChargesSummary` | Retrieve a summary of monthly charges for a specified date range. The date range cannot exceed 31 days. |
| Get OAuth Client | `getOAuthClient` | Retrieve a single OAuth client by ID |
| Get OAuth Consent Token | `getOAuthConsentToken` | Retrieve details about an OAuth consent token |
| Get OAuth Grant | `getOAuthGrant` | Retrieve a single OAuth grant by ID |
| Get Organization User | `getOrganizationUser` | Returns a user in your organization. |
| Get Organization Users Groups Report | `getOrganizationUsersGroupsReport` | Returns a report of all users in your organization with their group memberships. This endpoint returns all users without pagination and always includes group information. The report can be retrieved in JSON or CSV format by sending specific content-type headers. |
| Get OSR Campaign Attributes | `getCampaignOsrAttributes` | Get OSR campaign attributes |
| Get OTA Update | `getOtaUpdate` | This API returns the details of an Over the Air (OTA) update. |
| Get Phone Number Business Profile | `getWhatsappProfile` | Get phone number business profile |
| Get Phone Number Status | `getPhoneNumberStatus` | Check the status of the individual phone number/campaign assignments associated with the supplied taskId . |
| Get Phone-number Reputation Settings for an Enterprise | `getReputationSettings` | Phone Number Reputation tracks how your outbound caller-IDs are perceived (spam risk, engagement, etc.) across the call-screening ecosystem. This endpoint reads the enterprise-level settings: whether the product is enabled, the refresh cadence, and the stored Letter of Authorization document id. Returns 404 if reputation has never been enabled for this enterprise. |
| Get Plan | `getpublicmissionsmissionsmissionidrunsrunidplan` | Get the plan (all steps) for a run |
| Get Record Type Metadata | `getSessionAnalysisRecordTypeMetadata` | Returns detailed metadata for a specific record type, including relationships and examples. |
| Get Run Details | `getpublicmissionsmissionsmissionidrunsrunid` | Get details of a specific run |
| Get Session Analysis | `getSessionAnalysis` | Retrieves a full session analysis tree for a given event, including costs, child events, and product linkages. |
| Get Sharing Status | `getCampaignSharingStatus` | Get Sharing Status |
| Get Sharing Status | `getPartnerCampaignSharingStatus` | Get Sharing Status |
| Get SIM Card | `getSimCard` | Returns the details regarding a specific SIM card. |
| Get SIM Card Action Details | `getSimCardAction` | This API fetches detailed information about a SIM card action to follow-up on an existing asynchronous operation. |
| Get SIM Card Device Details | `getSimCardDeviceDetails` | It returns the device details where a SIM card is currently being used. |
| Get SIM Card Group | `getSimCardGroup` | Returns the details regarding a specific SIM card group |
| Get SIM Card Group Action Details | `getSimCardGroupAction` | This API allows fetching detailed information about a SIM card group action resource to make follow-ups in an existing asynchronous operation. |
| Get SIM Card Public IP Definition | `getSimCardPublicIp` | It returns the public IP requested for a SIM card. |
| Get Single Phone Number Campaign | `getSinglePhoneNumberCampaign` | Retrieve an individual phone number/campaign assignment by phoneNumber . |
| Get Single Shared Campaign | `getSharedCampaign` | Retrieve campaign details by campaignId . |
| Get Specific Test Run Details | `gettestrunpublicassistantsteststestidrunsrunidget` | Retrieves detailed information about a specific test run execution |
| Get Speech to Text Usage Report | `getSttUsageReportSync` | Generate and fetch speech to text usage report synchronously. This endpoint will both generate and fetch the speech to text report over a specified time period. |
| Get Step Details | `getpublicmissionsmissionsmissionidrunsrunidplanstepsstepid` | Get details of a specific plan step |
| Get Tasks by Status | `getTasksByStatus` | Retrieve tasks for the user that are either queued , processing , failed , success or partial success based on the query string. Defaults to queued and processing . |
| Get Telco Data Usage Report by ID | `getTelcoDataUsageReport` | Retrieve a specific telco data usage report by its ID |
| Get Telnyx Product Usage Data (BETA) | `getUsageReports` | Get Telnyx usage data by product, broken out by the specified dimensions |
| Get Terms of Service Information | `getTermsOfServiceInfo` | Returns the available Terms of Service agreements (product, current version, terms URL, effective date). Omit product type to return all products; pass it to scope to one. |
| Get Test Run History for a Specific Test | `gettestrunsfortestpublicassistantsteststestidrunsget` | Retrieves paginated execution history for a specific assistant test with filtering options |
| Get Test Suite Run History | `gettestsuiterunsfortestpublicassistantsteststestsuitessuitenamerunsget` | Retrieves paginated history of test runs for a specific test suite with filtering options |
| Get the Calling User's Terms of Service Status | `getTermsOfServiceStatus` | Returns whether the authenticated user has agreed to the current Terms of Service for the product given by product type . Used during onboarding to decide whether to prompt the user with the ToS dialog before continuing. agreement required: true means the user has not yet agreed (or has agreed to an outdated version) and must agree before using that product's endpoints. |
| Get the Count of Pending Upload Requests | `getExternalConnectionUploadsStatus` | Returns the count of all pending upload requests for the given external connection. |
| Get Tool | `getpublicmissionsmissionsmissionidtoolstoolid` | Get a specific tool by ID |
| Get Tool | `gettooltoolid` | Get Tool |
| Get Unused User Bundles | `getUnusedUserBundles` | Returns all user bundles that aren't in use. |
| Get Usage Reports Query Options (BETA) | `listUsageReportsOptions` | Get the Usage Reports options for querying usage, including the products available and their respective metrics and dimensions |
| Get User Balance Details | `getUserBalance` | Get user balance details |
| Get User Bundle by ID | `getUserBundleById` | Retrieves a user bundle by its ID. |
| Get User Bundle Resources | `getUserBundleResources` | Retrieves the resources of a user bundle by its ID. |
| Get User Bundles | `getUserBundles` | Get a paginated list of user bundles. |
| Get User Integration Connection by ID | `getuserintegrationbyidpublicintegrationsconnectionsuserconnectionidget` | Get user setup integrations |
| Get Verification Request | `getVerificationRequest` | Get a single verification request by its ID. |
| Get Verification Request Status History | `getVerificationStatusHistory` | Get the history of status changes for a verification request. Returns a paginated list of historical status changes including the reason for each change and when it occurred. |
| Get Voicemail | `getVoicemail` | Returns the voicemail settings for a phone number |
| Get WABA Settings | `getWabaSettings` | Get WABA settings |
| Get Whatsapp Profile Photo | `getWhatsappProfilePhoto` | Get Whatsapp profile photo |
| Global IP Assignment Health Check Metrics | `getGlobalIpAssignmentHealth` | Global IP Assignment Health Check Metrics |
| Global IP Assignment Usage Metrics | `getGlobalIpAssignmentUsage` | Global IP Assignment Usage Metrics |
| Global IP Latency Metrics | `getGlobalIpLatency` | Global IP Latency Metrics |
| Global IP Usage Metrics | `getGlobalIpUsage` | Global IP Usage Metrics |
| Hangup Call | `hangupCall` | Hang up the call. Expected Webhooks: - call.hangup - call.recording.saved |
| Hold Conference Participants | `holdConferenceParticipants` | Hold a list of participants in a conference call |
| Import Assistants from External Provider | `importassistantspublicassistantsimportpost` | Import assistants from external providers. Any assistant that has already been imported will be overwritten with its latest version from the importing provider. |
| Import External Vetting Record | `putExternalVettingRecord` | This operation can be used to import an external vetting record from a TCR-approved vetting provider. If the vetting provider confirms validity of the record, it will be saved with the brand and will be considered for future campaign qualification. |
| Initialize Whatsapp Phone Number Verification | `initializeWhatsappVerification` | Initialize Whatsapp phone number verification |
| Initiate an Action Requirement | `initiatePortingActionRequirement` | Initiates a specific action requirement for a porting order. |
| Initiate an Outbound AI Call | `initiateTexmlAICall` | Initiate an outbound AI call with warm-up support. Validates parameters, builds an internal TeXML with an AI Assistant configuration, encodes instructions into client state, and calls the dial API. The Twiml, Texml, and Url parameters are not allowed and will result in a 422 error. Expected callback events: Status callbacks: initiated , ringing , answered , one terminal status ( completed , no-answer , busy , canceled , or failed ), then analyzed after post-call processing completes. Conversation callbacks: conversation created and conversation ended . Recording, AMD, transcription, and deepfake detection callbacks are only sent when those features are enabled. |
| Initiate an Outbound Call | `initiateTexmlCall` | Initiate an outbound TeXML call. Telnyx will request TeXML from the XML Request URL configured for the connection in the Mission Control Portal. |
| Join a Conference | `joinConference` | Join an existing call leg to a conference. Issue the Join Conference command with the conference ID in the path and the call control id of the leg you wish to join to the conference as an attribute. The conference can have up to a certain amount of active participants, as set by the max participants parameter in conference creation request. Expected Webhooks: - conference.participant.joined - conference.participant.left |
| Join AI Assistant Conversation | `callJoinAIAssistant` | Add a participant to an existing AI assistant conversation. Use this command to bring an additional call leg into a running AI conversation. |
| JSON Web Key Set | `getOAuthJWKS` | Retrieve the JSON Web Key Set for token verification |
| Kick Participants from a Room Session. | `kickParticipantInSession` | Kick participants from a room session. |
| Leave a Conference | `leaveConference` | Removes a call leg from a conference and moves it back to parked state. Expected Webhooks: - conference.participant.left |
| Link Telnyx Agent to Run | `postpublicmissionsmissionsmissionidrunsrunidtelnyxagents` | Link a Telnyx AI agent (voice/messaging) to a run |
| List a DIR's References | `listDirReferences` | List the business and financial references submitted for a DIR. Returns the two business references (slots 0 and 1) followed by the single financial reference. Each entry carries only the customer-supplied details (name, title, organization, relationship, phone, email, timezone). Returns an empty list when no references were submitted. |
| List Account Email Events | `listEmailEvents` | Lists account-level email events sorted oldest first by occurred at asc, id asc . |
| List Action Requirements for a Porting Order | `listPortingActionRequirements` | Returns a list of action requirements for a specific porting order. |
| List Additional Documents | `listAdditionalDocuments` | Returns a list of additional documents for a porting order. |
| List Advanced Orders | `listadvancedordersv2` | List Advanced Orders |
| List All Access IP Addresses | `listAccessIpAddresses` | List all Access IP Addresses |
| List All Access IP Ranges | `listAccessIpRanges` | List all Access IP Ranges |
| List All Active Calls for Given Connection | `listConnectionActiveCalls` | Lists all active calls for given connection. Acceptable connections are either SIP connections with webhook url or xml request url, call control or texml. Returned results are cursor paginated. |
| List All Addresses | `findAddresses` | Returns a list of your addresses. |
| List All Associated Phone Numbers | `listPortingAssociatedPhoneNumbers` | Returns a list of all associated phone numbers for a porting order. Associated phone numbers are used for partial porting in GB to specify which phone numbers should be kept or disconnected. |
| List All Billing Groups | `listBillingGroups` | List all billing groups |
| List All Call Recordings | `getRecordings` | Returns a list of your call recordings. |
| List All Civic Addresses and Locations | `listCivicAddresses` | Returns the civic addresses and locations from Microsoft Teams. |
| List All Clusters | `listallrequestedclusterspublictextclustersget` | List all clusters |
| List All Comments for a Portout Request | `findPortoutComments` | Returns a list of comments for a portout request. |
| List All Comments of a Porting Order | `listPortingOrderComments` | Returns a list of all comments of a porting order. |
| List All Credentials | `findTelephonyCredentials` | List all On-demand Credentials. |
| List All DIRs Across Your Enterprises | `listAllDirs` | Returns every DIR (Display Identity Record) you own, across all of your enterprises, as a single list. Pagination is JSON:API style ( page[number] , page[size] , max 250). Supports filter[] query params: filter[enterprise id] , filter[status] , filter[display name][contains] , filter[call reason][contains] , plus the renewal-window filters filter[expiring at][gte] / filter[expiring at][lte] . Sortable by created at , updated at , display name , status (prefix - for descending; default -created at ). |
| List All Document Links | `listDocumentLinks` | List all documents links ordered by created at descending. |
| List All Documents | `listDocuments` | List all documents ordered by created at descending. |
| List All Exception Types | `listExceptionTypes` | Returns a list of all possible exception types for a porting order. |
| List All External Connections | `listExternalConnections` | This endpoint returns a list of your External Connections inside the 'data' attribute of the response. External Connections are used by Telnyx customers to seamless configure SIP trunking integrations with Telnyx Partners, through External Voice Integrations in Mission Control Portal. |
| List All Fax Applications | `listFaxApplications` | This endpoint returns a list of your Fax Applications inside the 'data' attribute of the response. You can adjust which applications are listed by using filters. Fax Applications are used to configure how you send and receive faxes using the Programmable Fax API with Telnyx. |
| List All Global IP Allowed Ports | `listGlobalIpAllowedPorts` | List all Global IP Allowed Ports |
| List All Global IP Assignments | `listGlobalIpAssignments` | List all Global IP assignments. |
| List All Global IP Health Check Types | `listGlobalIpHealthCheckTypes` | List all Global IP Health check types. |
| List All Global IP Health Checks | `listGlobalIpHealthChecks` | List all Global IP health checks. |
| List All Global IP Protocols | `listGlobalIpProtocols` | List all Global IP Protocols |
| List All Global IPs | `listGlobalIps` | List all Global IPs. |
| List All Interfaces for a Network. | `listNetworkInterfaces` | List all Interfaces for a Network. |
| List All Log Messages | `listExternalConnectionLogMessages` | Retrieve a list of log messages for all external connections associated with your account. |
| List All Migration Sources | `listMigrationSources` | List all Migration Sources |
| List All Migrations | `listMigrations` | List all Migrations |
| List All Networks | `listNetworks` | List all Networks. |
| List All Notifications Events | `findNotificationsEvents` | Returns a list of your notifications events. |
| List All Notifications Events Conditions | `findNotificationsEventsConditions` | Returns a list of your notifications events conditions. |
| List All Notifications Profiles | `findNotificationsProfiles` | Returns a list of your notifications profiles. |
| List All Numbers Using Channel Billing | `getAllNumbersChannelZones` | Retrieve a list of all phone numbers using Channel Billing, grouped by Zone. |
| List All Phone Number Blocks | `listPortingPhoneNumberBlocks` | Returns a list of all phone number blocks of a porting order. |
| List All Phone Number Configurations | `listPhoneNumberConfigurations` | Returns a list of phone number configurations paginated. |
| List All Phone Number Extensions | `listPortingPhoneNumberExtensions` | Returns a list of all phone number extensions of a porting order. |
| List All Phone Numbers | `listExternalConnectionPhoneNumbers` | Returns a list of all active phone numbers associated with the given external connection. |
| List All Port-out Events | `listPortoutEvents` | Returns a list of all port-out events. |
| List All Porting Activation Jobs | `listPortingOrderActivationJobs` | Returns a list of your porting activation jobs. |
| List All Porting Events | `listPortingEvents` | Returns a list of all porting events. |
| List All Porting Orders | `listPortingOrders` | Returns a list of your porting order. |
| List All Porting Phone Numbers | `listPortingPhoneNumbers` | Returns a list of your porting phone numbers. |
| List All Public Internet Gateways | `listPublicInternetGateways` | List all Public Internet Gateways. |
| List All RCS Agents | `listRCSAgents` | List all RCS agents |
| List All Recording Transcriptions | `getRecordingTranscriptions` | Returns a list of your recording transcriptions. |
| List All Regions | `listRegions` | List all regions and the interfaces that region supports |
| List All Releases | `listExternalConnectionReleases` | Returns a list of your Releases for the given external connection. These are automatically created when you change the connection id of a phone number that is currently on Microsoft Teams. |
| List All Requirement Types | `listRequirementTypes` | List all requirement types ordered by created at descending |
| List All Requirements | `listRequirements` | List all requirements with filtering, sorting, and pagination |
| List All SSO Authentication Providers | `findAuthenticationProviders` | Returns a list of your SSO authentication providers. |
| List All TeXML Applications | `findTexmlApplications` | Returns a list of your TeXML Applications. |
| List All Upload Requests | `listExternalConnectionUploads` | Returns a list of your Upload requests for the given external connection. |
| List All User Addresses | `findUserAddress` | Returns a list of your user addresses. |
| List All Verified Numbers | `listVerifiedNumbers` | Gets a paginated list of Verified Numbers. |
| List All Verify Profiles | `listProfiles` | Gets a paginated list of Verify profiles. |
| List All Virtual Cross Connects | `listVirtualCrossConnects` | List all Virtual Cross Connects. |
| List All WireGuard Interfaces | `listWireguardInterfaces` | List all WireGuard Interfaces. |
| List All WireGuard Peers | `listWireguardPeers` | List all WireGuard peers. |
| List Allowed FOC Dates | `listAllowedFocWindows` | Returns a list of allowed FOC dates for a porting order. |
| List Alphanumeric Sender IDs | `listAlphanumericSenderIds` | List all alphanumeric sender IDs for the authenticated user. |
| List Alphanumeric Sender IDs for a Messaging Profile | `listProfileAlphanumericSenderIds` | List all alphanumeric sender IDs associated with a specific messaging profile. |
| List Assistant Tests with Pagination | `getassistanttestspublicassistantstestsget` | Retrieves a paginated list of assistant tests with optional filtering capabilities |
| List Assistants | `getassistantspublicassistantsget` | Retrieve a list of all AI Assistants configured by the user. |
| List Audit Events for a Suppression | `listEmailBlockEvents` | Offset pagination only ( page[number] default 1, page[size] default 50 , max 100). No sort , no filter , no cursor — ordering is fixed desc occurred at, desc id . Verifies the block belongs to the account first (cross-account → 404). |
| List Audit Logs | `listAuditLogs` | Retrieve a list of audit log entries. Audit logs are a best-effort, eventually consistent record of significant account-related changes. |
| List Auto Recharge Preferences | `getAutoRechargePrefs` | Returns the payment auto recharge preferences. |
| List Auto-Response Settings | `getAutorespConfigs` | List Auto-Response Settings |
| List Available Carriers in the UK | `listPortingUKCarriers` | List available carriers in the UK. |
| List Available Phone Number Blocks | `listAvailablePhoneNumberBlocks` | List available phone number blocks |
| List Available Phone Numbers | `listAvailablePhoneNumbers` | List available phone numbers |
| List Available Voices | `listVoices` | Retrieve a list of available voices from one or all TTS providers. When provider is specified, returns voices for that provider only. Otherwise, returns voices from all providers. Some providers (ElevenLabs, Resemble) require an API key to list voices. |
| List Brands | `getBrands` | This endpoint is used to list all brands associated with your organization. |
| List Bulk SIM Card Actions | `listBulkSimCardActions` | This API lists a paginated collection of bulk SIM card actions. A bulk SIM card action contains details about a collection of individual SIM card actions. |
| List Call Control Applications | `listCallControlApplications` | Return a list of call control applications. |
| List Call Events | `listCallEvents` | Filters call events by given filter parameters. Events are ordered by occurred at . If filter for leg id or application session id is not present, it only filters events from the last 24 hours. Note : Only one filter[occurred at] can be passed. |
| List Campaigns | `getCampaigns` | Retrieve a list of campaigns associated with a supplied brandId . |
| List CDR Usage Reports | `getCdrUsageReports` | Fetch all previous requests for cdr usage reports. |
| List CloudFS Filesystems | `listCloudfsFilesystems` | Lists the CloudFS filesystems for the authenticated user's organization. Results use cursor-based pagination: fetch the next page by passing meta.cursors.after as page[after] , or follow the meta.next URL. |
| List Comments on a DIR | `listCommentsSimple` | List the comments on a DIR. The enterprise is resolved server-side from the DIR id. |
| List Conference Participants | `getTexmlConferenceParticipants` | Lists conference participants |
| List Conference Participants | `listConferenceParticipants` | Lists conference participants |
| List Conference Recordings | `getTexmlConferenceRecordings` | Lists conference recordings |
| List Conference Resources | `getTexmlConferences` | Lists conference resources. |
| List Conferences | `listConferences` | Lists conferences. Conferences are created on demand, and will expire after all participants have left the conference or after 4 hours regardless of the number of active participants. Conferences are listed in descending order by expires at . |
| List Connections | `listConnections` | Returns a list of your connections irrespective of type. |
| List Conversations | `getconversationspublicconversationsget` | Retrieve a list of all AI conversations configured by the user. Supports PostgREST-style query parameters for filtering. Examples are included for the standard metadata fields, but you can filter on any field in the metadata JSON object. For example, to filter by a custom field metadata- custom field , use metadata- custom field=eq.value . |
| List Credential Connections | `listCredentialConnections` | Returns a list of your credential connections. |
| List CSV Downloads | `listCsvDownloads` | List CSV downloads |
| List Customer Service Records | `listCustomerServiceRecords` | List customer service records. |
| List DIRs in an Enterprise | `listDirsForEnterprise` | Return the DIRs (Display Identity Records) belonging to a single enterprise. Pagination is JSON:API style ( page[number] , page[size] , max 250). Supports filter[] query params: filter[status] , filter[display name][contains] , filter[call reason][contains] , plus the renewal-window filters filter[expiring at][gte] / filter[expiring at][lte] and the convenience filter[expiring within days] (mutually exclusive with the explicit gte/lte form). Sortable by created at , updated at , display name , status , submitted at , verified at , expiring at (prefix - for descending; default -created at ). |
| List DNS Records for an Email Domain | `listEmailDomainDnsRecords` | List DNS records for an email domain |
| List Dynamic Emergency Addresses | `listDynamicEmergencyAddresses` | Returns the dynamic emergency addresses according to filters |
| List Dynamic Emergency Endpoints | `listDynamicEmergencyEndpoints` | Returns the dynamic emergency endpoints according to filters |
| List Eligible Port-out Rejection Codes for a Specific Order | `listPortoutRejections` | Given a port-out ID, list rejection codes that are eligible for that port-out |
| List Email Domains | `listEmailDomains` | Shared ( type: shared ) Telnyx-managed domains are included/readable for every account, in addition to the account's own custom domains. |
| List Email Messages | `listEmailMessages` | Lists messages sorted newest first by inserted at desc, id desc . No filters other than cursor pagination are implemented. The legacy /v2/emails GET route is a backward-compatible alias for this operation. |
| List Email Templates | `listEmailTemplates` | Lists templates sorted newest first by inserted at desc, id desc . |
| List Embedded Buckets | `getEmbeddingBuckets` | Get all embedding buckets for a user. |
| List Embedding Models | `listopenaiembeddingmodels` | Returns a list of available embedding models. This endpoint is compatible with the OpenAI Models API format. |
| List Enterprises | `listEnterprises` | Return the enterprises you own, paginated. The default page size is 20; the maximum is 250. |
| List Events | `getpublicmissionsmissionsmissionidrunsrunidevents` | List events for a run (paginated) |
| List Events for an Email Message | `listEmailMessageEvents` | Lists events for a single message sorted oldest first by occurred at asc, id asc . The legacy /v2/emails/{id}/events GET route is a backward-compatible alias. |
| List External Vettings | `listExternalVettings` | Get list of valid external vetting record for a given brand |
| List Fine Tuning Jobs | `getfinetuningjobpublicfinetuningget` | Retrieve a list of all fine tuning jobs created by the user. |
| List FQDN Connections | `listFqdnConnections` | Returns a list of your FQDN connections. |
| List FQDNs | `listFqdns` | Get all FQDNs belonging to the user that match the given filters. |
| List High-level Messaging Profile Metrics | `getProfileMetrics` | List high-level metrics for all messaging profiles belonging to the authenticated user. |
| List Inexplicit Number Orders | `listInexplicitNumberOrders` | Get a paginated list of inexplicit number orders. |
| List Infringement Claims for a DIR | `listInfringementClaimsForDir` | Return the trademark or copyright claims filed against this DIR. Each claim's status is pending (newly filed; DIR auto-suspended), contested (you have submitted contest evidence; awaiting resolution), or resolved (final). Resolution outcomes: upheld (claim accepted; DIR stays suspended/permanently rejected), rejected (claim dismissed; DIR restored to verified ), modified (partial outcome). |
| List Integration by ID | `listintegrationbyidpublicintegrationsintegrationidget` | Retrieve integration details |
| List Integration Secrets | `listintegrationsecrets` | Retrieve a list of all integration secrets configured by the user. |
| List Integrations | `listintegrationspublicintegrationsget` | List all available integrations. |
| List Invoices | `listInvoices` | Retrieve a paginated list of invoices. |
| List IP Connections | `listIpConnections` | Returns a list of your IP connections. |
| List Ips | `listIps` | Get all IPs belonging to the user that match the given filters. |
| List Keys | `listKvKeys` | Lists the keys in a namespace. Returns key names and metadata only, never values. Results are paginated with limit and an opaque cursor . |
| List Knowledge Bases | `getpublicmissionsmissionsmissionidknowledgebases` | List all knowledge bases for a mission |
| List KV Namespaces | `listKvNamespaces` | Lists the KV namespaces for the authenticated user's organization. Results use page-based pagination ( page[number] / page[size] ). |
| List Linked Telnyx Agents | `getpublicmissionsmissionsmissionidrunsrunidtelnyxagents` | List all Telnyx agents linked to a run |
| List LOA Configurations | `listLoaConfigurations` | List the LOA configurations. |
| List MCP Servers | `getpublicmissionsmissionsmissionidmcpservers` | List all MCP servers for a mission |
| List MCP Servers | `listmcpservers` | Retrieve a list of MCP servers. |
| List MDR Usage Reports | `getMdrUsageReports` | Fetch all previous requests for MDR usage reports. |
| List Messaging Hosted Number Orders | `listMessagingHostedNumberOrders` | List messaging hosted number orders |
| List Messaging Hosted Numbers | `listMessagingHostedNumbers` | List all hosted numbers associated with the authenticated user. |
| List Messaging Profiles | `listMessagingProfiles` | List messaging profiles |
| List Messaging URL Domains | `listMessagingUrlDomains` | List messaging URL domains |
| List Migration Source Coverage | `listMigrationSourceCoverage` | List Migration Source coverage |
| List Missions | `getpublicmissionsmissions` | List all missions for the organization |
| List Mobile Network Operators | `getMobileNetworkOperators` | Telnyx has a set of GSM mobile operators partners that are available through our mobile network roaming. This resource is entirely managed by Telnyx and may change over time. That means that this resource won't allow any write operations for it. Still, it's available so it can be used as a support resource that can be related to other resources or become a configuration option. |
| List Mobile Phone Numbers | `listMobilePhoneNumbers` | List Mobile Phone Numbers |
| List Mobile Phone Numbers with Messaging Settings | `listMobilePhoneNumbersWithMessagingSettings` | List mobile phone numbers with messaging settings |
| List Mobile Push Credentials | `listPushCredentials` | List mobile push credentials |
| List Mobile Voice Connections | `listMobileVoiceConnections` | List Mobile Voice Connections |
| List Network Coverage Locations | `listNetworkCoverage` | List all locations and the interfaces that region supports |
| List Notification Channels | `listNotificationChannels` | List notification channels. |
| List Notification Settings | `listNotificationSettings` | List notification settings. |
| List Number Block Orders | `listNumberBlockOrders` | Get a paginated list of number block orders. |
| List Number Orders | `listNumberOrders` | Get a paginated list of number orders. |
| List Number Reservations | `listNumberReservations` | Gets a paginated list of phone number reservations. |
| List Numbers Using Channel Billing for a Specific Zone | `getNumbersChannelZones` | Retrieve a list of phone numbers using Channel Billing for a specific Zone. |
| List OAuth Clients | `listOAuthClients` | Retrieve a paginated list of OAuth clients for the authenticated user |
| List OAuth Grants | `listOAuthGrants` | Retrieve a paginated list of OAuth grants for the authenticated user |
| List Opt-outs | `listOptOuts` | Retrieve a list of opt-out blocks. |
| List Organization Users | `listOrganizationUsers` | Returns a list of the users in your organization. |
| List OTA Updates | `listOtaUpdates` | List OTA updates |
| List Phone Number Campaigns | `getAllPhoneNumberCampaigns` | List phone number campaigns |
| List Phone Numbers | `listPhoneNumbers` | List phone numbers |
| List Phone Numbers Associated with a Messaging Profile | `listProfilePhoneNumbers` | List phone numbers associated with a messaging profile |
| List Phone Numbers Attached to a DIR | `listDirPhoneNumbersSimplified` | List the phone numbers registered under a DIR. The enterprise is resolved server-side from the DIR id. |
| List Phone Numbers for a WABA | `listWabaPhones` | List phone numbers for a WABA |
| List Phone Numbers with Messaging Settings | `listPhoneNumbersWithMessagingSettings` | List phone numbers with messaging settings |
| List Phone Numbers with Voice Settings | `listPhoneNumbersWithVoiceSettings` | List phone numbers with voice settings |
| List Phone-number Batches for a DIR | `listDirPhoneNumberBatchesSimplified` | List the phone-number batches submitted under a DIR. The enterprise is resolved server-side from the DIR id. |
| List Port-out Related Reports | `listPortoutReports` | List the reports generated about port-out operations. |
| List Porting Order Requirements | `listPortingOrderRequirements` | Returns a list of all requirements based on country/number type for this porting order. |
| List Porting Related Reports | `listPortingReports` | List the reports generated about porting operations. |
| List Portout Requests | `listPortoutRequest` | Returns the portout requests according to filters |
| List Pronunciation Dictionaries | `listPronunciationDicts` | List all pronunciation dictionaries for the authenticated organization. Results are paginated using offset-based pagination. |
| List Queue Resources | `getTexmlQueues` | Lists queue resources. |
| List Queues | `listQueues` | List all queues for the authenticated user. |
| List Recent Events | `getpublicmissionsmissionsevents` | List recent events across all missions |
| List Recent Runs | `getpublicmissionsmissionsruns` | List recent runs across all missions |
| List Recording Transcriptions | `getTeXMLRecordingTranscriptions` | Returns multiple recording transcription resources for an account. |
| List Reputation Remediation Requests for an Enterprise | `listReputationRemediations` | Paginated list of remediation requests for this enterprise. List items omit per-number results and webhook URLs to keep the response small; call GET by id for full detail. Supports JSON:API pagination and optional filters on status and created-at range. |
| List Reputation-monitored Phone Numbers Across All Enterprises | `listReputationNumbersSimplified` | Convenience alias for GET /v2/enterprises/{enterprise id}/reputation/numbers that returns numbers across every enterprise you own. Useful when you don't want to look up the enterprise id first. |
| List Reputation-monitored Phone Numbers for an Enterprise | `listReputationNumbers` | Paginated list of phone numbers registered for reputation monitoring under this enterprise. The response includes the latest reputation snapshot per number where one has been collected. |
| List Requirement Groups | `getRequirementGroups` | List requirement groups |
| List Runs for Mission | `getpublicmissionsmissionsmissionidruns` | List all runs for a specific mission |
| List Scheduled Events | `getscheduledevents` | Get scheduled events for an assistant with pagination and filtering |
| List Shared Campaigns | `getSharedCampaigns` | Retrieve all partner campaigns you have shared to Telnyx in a paginated fashion. This endpoint is currently limited to only returning shared campaigns that Telnyx has accepted. In other words, shared but pending campaigns are currently omitted from the response from this endpoint. |
| List Shared Partner Campaigns | `getPartnerCampaignsSharedByUser` | Get all partner campaigns you have shared to Telnyx in a paginated fashion This endpoint is currently limited to only returning shared campaigns that Telnyx has accepted. In other words, shared but pending campaigns are currently omitted from the response from this endpoint. |
| List Short Codes | `listShortCodes` | List short codes |
| List Short Codes Associated with a Messaging Profile | `listProfileShortCodes` | List short codes associated with a messaging profile |
| List SIM Card Actions | `listSimCardActions` | This API lists a paginated collection of SIM card actions. It enables exploring a collection of existing asynchronous operations using specific filters. |
| List SIM Card Data Usage Notifications | `listDataUsageNotifications` | Lists a paginated collection of SIM card data usage notifications. It enables exploring the collection using specific filters. |
| List SIM Card Group Actions | `getSimCardGroupActions` | This API allows listing a paginated collection a SIM card group actions. It allows to explore a collection of existing asynchronous operation using specific filters. |
| List Standard Call Reasons | `listCallReasons` | Telnyx maintains a library of pre-vetted call-reason phrases (e.g. "Appointment reminders", "Billing inquiries") that carry through DIR vetting smoothly. You can use any string that fits your use case in DirCreateRequest.call reasons , but matching one of these reduces the chance the vetting team flags the phrasing for clarification. |
| List Sub Number Orders | `listSubNumberOrders` | Get a paginated list of sub number orders. |
| List Supported DIR Document Types | `listDocumentTypes` | Reference list of document type values accepted by DirCreateRequest.documents[].document type and the infringement-contest endpoint. Each entry has a stable short name (used in API calls) and a customer-facing description. |
| List Supported STT Providers | `listSttProviders` | Retrieve the canonical list of supported speech-to-text providers, models, accepted language codes, and the service types each model supports. Service types: streaming — standalone WebSocket transcription via /speech-to-text/transcription . file based — file-based transcription via /ai/audio/transcriptions . in call — live call transcription via Call Control transcription start . ai assistant — STT configured on a Call Control AI Assistant via voice-assistant TranscriptionConfig (covers both live-streaming and non-streaming/batch models). Use this endpoint to discover which (provider, model) combinations are available for the surface you need, and which language codes each accepts. auto in a languages array indicates the provider performs language detection. |
| List Supporting Documents on a Portout Request | `getPortRequestSupportingDocuments` | List every supporting documents for a portout request. |
| List Suppressions | `listEmailBlocks` | Account-scoped list. Two mutually exclusive pagination modes: - Offset : page[number] (default 1) + page[size] (default 25, max 100). meta contains total pages . - Cursor : page[after] and/or page[before] (opaque Base.url encode64 of {"created at","id"} ). Cannot combine with page[number] ; after + before together is an error. meta contains next cursor / previous cursor (omitted when their flag is false). Sort defaults to -created at (desc); only created at is sortable. A -- prefix is an error. nil /empty filter values are silently dropped. |
| List Suppressions in a Group | `listGroupSuppressions` | Account + group scoped. Offset pagination only ( page[number] default 1, page[size] default 25, max 100). No sort / filter / cursor — ordering fixed desc created at, desc id . Uses the shared QueryParser.parse offset/1 — a malformed page returns 400 (code 10015 ), consistent with GET /v2/email blocks . meta includes total pages . Rows reuse the standard suppression shape ( group id set to this group). |
| List Telco Data Usage Reports | `getTelcoDataUsageReports` | Retrieve a paginated list of telco data usage reports |
| List the Calling User's Terms of Service Agreements | `listTermsOfServiceAgreements` | Returns the Terms of Service agreements the authenticated user has on file. Each entry records the version agreed to and when. Most users only have one agreement per product, but if the ToS is updated and the user re-agrees a new entry is added. Results are paginated with the standard page[number] / page[size] parameters; the response uses the standard {data, meta} JSON:API envelope. By default this returns agreements for all products the user has agreed to. Pass the product type query parameter to scope the result to a single product. |
| List Tools | `getpublicmissionsmissionsmissionidtools` | List all tools for a mission |
| List Tools | `listtools` | List Tools |
| List UAC Connections | `listUacConnections` | Returns a list of your UAC connections. A UAC (User Agent Client) Connection registers Telnyx to your PBX — the opposite of a standard SIP trunk, where the PBX registers to Telnyx. Use UAC when your PBX doesn’t support outbound SIP registration or you need Telnyx to maintain the registration. |
| List Unsubscribe Groups | `listUnsubscribeGroups` | Offset pagination only ( page[number] default 1, page[size] default 25, max 100). No sort / filter /cursor — ordering fixed desc created at, desc id . Uses the shared QueryParser.parse offset/1 — a malformed page (e.g. flat ?page=1 instead of ?page[number]=1 ) returns 400 (code 10015 ), consistent with GET /v2/email blocks . meta includes total pages . |
| List Uploaded Media | `listMediaStorage` | Returns a list of stored media files. |
| List User Integrations | `listuserintegrationspublicintegrationsconnectionsget` | List user setup integrations |
| List User Tags | `getUserTags` | List all user tags. |
| List Verification Codes | `listVerificationCodes` | Returns a list of verification codes for a porting order. |
| List Verification Requests | `listVerificationRequests` | Get a list of previously-submitted tollfree verification requests |
| List Verifications by Phone Number | `listVerifications` | List verifications by phone number |
| List Virtual Cross Connect Cloud Coverage | `listVirtualCrossConnectCoverage` | List Virtual Cross Connects Cloud Coverage. This endpoint shows which cloud regions are available for the location code your Virtual Cross Connect will be provisioned in. |
| List Voice Clones | `listVoiceClones` | Returns a paginated list of voice clones belonging to the authenticated account. |
| List Voice Designs | `listVoiceDesigns` | Returns a paginated list of voice designs belonging to the authenticated account. |
| List Voice SDK Call Reports | `listVoiceSdkCallReports` | Returns paginated raw call report stats JSON payloads stored for the authenticated user. The user is derived from Telnyx authentication, not from request parameters. |
| List Webhook Deliveries | `getWebhookDeliveries` | Lists webhook deliveries for the authenticated user |
| List Webhooks for an Email Domain | `listEmailDomainWebhooks` | List webhooks for an email domain |
| List Whatsapp Business Accounts | `listWabas` | List Whatsapp Business Accounts |
| List Whatsapp Message Templates | `listWhatsappTemplates` | List Whatsapp message templates |
| List Whatsapp Phone Numbers | `listPhoneNumbersGet` | List Whatsapp phone numbers |
| List Wireless Connectivity Logs | `getWirelessConnectivityLogs` | This API allows listing a paginated collection of Wireless Connectivity Logs associated with a SIM Card, for troubleshooting purposes. |
| List Your Voice Channels for Non-US Zones | `getChannelZones` | Returns the non-US voice channels for your account. voice channels allow you to use Channel Billing for calls to your Telnyx phone numbers. Please check the Telnyx Support Articles section for full information and examples of how to utilize Channel Billing. |
| List Your Voice Channels for US Zone | `listInboundChannels` | Returns the US Zone voice channels for your account. voice channels allows you to use Channel Billing for calls to your Telnyx phone numbers. Please check the Telnyx Support Articles section for full information and examples of how to utilize Channel Billing. |
| Lists Accounts Managed by the Current User. | `listManagedAccounts` | Lists the accounts managed by the current user. Users need to be explictly approved by Telnyx in order to become manager accounts. |
| Lists the Phone Number Blocks Jobs | `listPhoneNumberBlocksJobs` | Lists the phone number blocks jobs |
| Lists the Phone Numbers Jobs | `listPhoneNumbersJobs` | Lists the phone numbers jobs |
| Log Event | `postpublicmissionsmissionsmissionidrunsrunidevents` | Log an event for a run |
| Lookup Phone Number Data | `lookupNumber` | Returns information about the provided phone number. |
| Mark a Comment as Read | `markCommentRead` | Mark a comment as read |
| Modify an RCS Agent | `updateRCSAgentById` | Modify an RCS agent |
| Mute Conference Participants | `muteConferenceParticipants` | Mute a list of participants in a conference call |
| Mute Participants in Room Session. | `muteParticipantInSession` | Mute participants in room session. |
| Noise Suppression Start (BETA) | `noiseSuppressionStart` | Noise Suppression Start (BETA) |
| Noise Suppression Stop (BETA) | `noiseSuppressionStop` | Noise Suppression Stop (BETA) |
| OAuth Authorization Endpoint | `authorizeOAuth` | OAuth 2.0 authorization endpoint for the authorization code flow |
| OAuth Token Endpoint | `exchangeOAuthToken` | Exchange authorization code, client credentials, or refresh token for access token |
| Order Brand External Vetting | `postOrderExternalVetting` | Order new external vetting for a brand. Duplicate orders for the same evpId and vettingClass return 400 with code 10012 if a successful vetting exists within the last 180 days, or one is currently being processed. Failed vettings can be retried immediately. |
| Pause Run | `postpublicmissionsmissionsmissionidrunsrunidpause` | Pause a running run |
| Play Audio to Conference Participants | `playConferenceAudio` | Play audio to all or some participants on a conference call. |
| Play Audio URL | `startCallPlayback` | Play an audio file on the call. If multiple play audio commands are issued consecutively, the audio files will be placed in a queue awaiting playback. Notes: - When overlay is enabled, target legs is limited to self . - A customer cannot Play Audio with overlay=true unless there is a Play Audio with overlay=false actively playing. Expected Webhooks: - call.playback.started - call.playback.ended |
| Poll an Import Job | `showEmailBlockImport` | Account-scoped fetch (cross-account → 404; malformed UUID → 404). Nullable fields are omitted until terminal: provider / completed at when nil; processed rows / created count / existing count / skipped count / error count only when status == completed ; errors only when non-empty; failure reason only on terminal failure. |
| Post a Comment on a DIR | `createCommentSimple` | Post a customer comment on a DIR (for example, to respond to reviewer notes). Send only content (1–5000 chars) and an optional parent comment id ; the server sets the comment type, visibility, and author automatically. The enterprise is resolved server-side from the DIR id. |
| Preview a LOA Configuration | `previewLoaConfiguration` | Preview a specific LOA configuration. |
| Preview SIM Card Orders | `previewSimCardOrders` | Preview SIM card order purchases. |
| Preview the LOA Configuration Parameters | `previewLoaConfigurationParams` | Preview the LOA template that would be generated without need to create LOA configuration. |
| Promote an Assistant Version to Main | `promoteassistantversionpublicassistantsassistantidversionsversionidpromotepost` | Promotes a specific version to be the main/current version of the assistant. This will delete any existing canary deploy configuration and send all live production traffic to this version. |
| Protected Resource Metadata | `getOAuthProtectedResourceMetadata` | OAuth 2.0 Protected Resource Metadata for resource discovery |
| Purchase ESIMs | `purchaseESim` | Purchases and registers the specified amount of eSIMs to the current user's account. If sim card group id is provided, the eSIMs will be associated with that group. Otherwise, the default group for the current user will be used. |
| Qualify by Usecase | `getUsecaseQualification` | This endpoint allows you to see whether or not the supplied brand is suitable for your desired campaign use case. |
| Record Pause | `pauseCallRecording` | Pause recording the call. Recording can be resumed via Resume recording command. Expected Webhooks: There are no webhooks associated with this command. |
| Record Resume | `resumeCallRecording` | Resume recording the call. Expected Webhooks: There are no webhooks associated with this command. |
| Recording Start | `startCallRecord` | Start recording the call. Recording will stop on call hang-up, or can be initiated via the Stop Recording command. Expected Webhooks: - call.recording.saved - call.recording.transcription.saved - call.recording.error |
| Recording Stop | `stopCallRecording` | Stop recording the call. Expected Webhooks: - call.recording.saved |
| Refresh a Fax | `refreshFax` | Refreshes the inbound fax's media url when it has expired |
| Refresh Client Token to Join a Room. | `refreshRoomClientToken` | Synchronously refresh an Client Token to join a Room. Client Token is necessary to join a Telnyx Room. Client Token will expire after token ttl secs . |
| Refresh Operator Connect Integration | `operatorConnectRefresh` | This endpoint will make an asynchronous request to refresh the Operator Connect integration with Microsoft Teams for the current user. This will create new external connections on the user's account if needed, and/or report the integration results as log messages. |
| Refresh the Status of All Upload Requests | `refreshExternalConnectionUploads` | Forces a recheck of the status of all pending Upload requests for the given external connection in the background. |
| Regenerate Messaging Profile Secret | `regenerateMessagingProfileSecret` | Regenerate the v1 secret for a messaging profile. |
| Register Phone Numbers for Reputation Monitoring | `associateReputationNumbers` | Add up to 100 phone numbers to reputation monitoring on this enterprise. Each must be in E.164 format ( +1NPANXXXXXX for US/CA) and belong to your Telnyx phone-number inventory. Prerequisite : reputation must already be enabled on this enterprise (see POST .../reputation ). Pricing: This is a billable action. See https://telnyx.com/pricing/numbers for current pricing. |
| Register SIM Cards | `registerSimCards` | Register the SIM cards associated with the provided registration codes to the current user's account. If sim card group id is provided, the SIM cards will be associated with that group. Otherwise, the default group for the current user will be used. |
| Reject a Call | `rejectCall` | Reject an incoming call. Expected Webhooks: - call.hangup |
| Remove a Group Suppression | `removeGroupSuppression` | Soft-deletes all active blocks for (account, group, normalized email) — one removed audit event per block ( actor: manual ). The email path segment is normalized (trim + lower-case) before matching. Idempotent on already-removed rows (returns 404 since they're no longer active ). Two distinct 404 cases: a missing/cross-account group returns 10001 "The requested unsubscribe group was not found" ; a group that exists but has no active suppression for that email returns 10001 "The requested group suppression was not found" . |
| Remove a Phone Number from Reputation Monitoring | `disassociateReputationNumber` | Stop tracking the reputation of this phone number. The number itself remains in your inventory; only the reputation registration is removed. |
| Remove a Phone Number from Reputation Monitoring (no Enterprise ID Required) | `disassociateReputationNumberSimplified` | Convenience alias for DELETE /v2/enterprises/{enterprise id}/reputation/numbers/{phone number} . |
| Remove Assistant Tag | `removeassistanttag` | Remove Assistant Tag |
| Remove Assistant Tool | `removeassistanttool` | Remove Assistant Tool |
| Remove Call from a Queue | `leaveQueue` | Removes the call from a queue. |
| Remove Phone Numbers from a DIR | `deleteDirPhoneNumbersSimplified` | Deregister phone numbers from a DIR. The enterprise is resolved server-side from the DIR id. Returns a partial-success envelope. |
| Remove SSL Certificate | `removeStorageSSLCertificate` | Deletes an SSL certificate and its matching secret. |
| Rename a Voice Design | `updateVoiceDesign` | Updates the name of a voice design. All versions retain their other properties. |
| Render a Phone-number Reputation Letter of Authorization | `generateReputationLoa` | Render the LOA for this enterprise as a PDF. The enterprise identity, address, and authorized-representative contact are taken from the enterprise record; the optional agent block is supplied only when a third-party partner manages the numbers. The response is the PDF itself (unsigned unless a signature is provided). Sign it and upload it to the Telnyx Documents API ( POST /v2/documents , see https://developers.telnyx.com/api/documents) to obtain the loa document id required by POST .../reputation . |
| Render an Email Template | `renderEmailTemplate` | Renders a template using the provided Liquid variables. Missing template variables defaults to {} . |
| Render the Branded Calling LOA for a DIR | `renderDirLoa` | Generate a pre-filled Letter of Authorization (LOA) PDF for a DIR. Enterprise identity (legal name, DBA, address, contact, website, tax id) and the DIR display name are read server-side; the caller supplies the telephone numbers to authorize, an optional Authorized Agent block, and an optional drawn signature. When signature is omitted the PDF is returned unsigned so the customer can sign it externally and upload it via the Documents API. When signature is present the PDF embeds the supplied image, printed name, and signed-at date. Returns application/pdf . |
| Replace an Email Template | `replaceEmailTemplate` | Replaces template fields. Behaves identically to PATCH; provided for compatibility with Phoenix resource routes. |
| Replace an Enterprise | `updateEnterprise` | Replace the enterprise's mutable fields. Only mutable fields may be sent. Server-assigned and immutable fields ( id , record type , created at , updated at , status fields, organization type , country code , role type ) cannot be changed: including any of them in the body is rejected with 400 Bad Request ( Field 'X' is not allowed in this request ). |
| Replace the Reputation Letter of Authorization Document | `replaceReputationLoa` | Point the enterprise's reputation settings at a new signed LOA document. This resets LOA approval to pending ; the new document must be approved before additional phone numbers can be added. |
| Republish a Port-out Event | `republishPortoutEvent` | Republish a specific port-out event. |
| Republish a Porting Event | `republishPortingEvent` | Republish a specific porting event. |
| Request a SIM Card Disable | `disableSimCard` | This API disables a SIM card, disconnecting it from the network and making it impossible to consume data. The API will trigger an asynchronous operation called a SIM Card Action. Transitioning to the disabled state may take a period of time. The status of the SIM Card Action can be followed through the List SIM Card Action API. |
| Request a SIM Card Enable | `enableSimCard` | This API enables a SIM card, connecting it to the network and making it possible to consume data. To enable a SIM card, it must be associated with a SIM card group. The API will trigger an asynchronous operation called a SIM Card Action. Transitioning to the enabled state may take a period of time. The status of the SIM Card Action can be followed through the List SIM Card Action API. |
| Request Bulk Disabling Voice on SIM Cards. | `disableVoiceBulk` | This API triggers an asynchronous operation to disable voice on SIM cards belonging to a specified SIM Card Group. For each SIM Card a SIM Card Action will be generated. The status of the SIM Card Actions can be followed through the List SIM Card Action API. The overall status of the Bulk SIM Card Action can be followed through the List Bulk SIM Card Action API. |
| Request Bulk Enabling Voice on SIM Cards. | `enableVoiceBulk` | This API triggers an asynchronous operation to enable voice on SIM cards belonging to a specified SIM Card Group. For each SIM Card a SIM Card Action will be generated. The status of the SIM Card Actions can be followed through the List SIM Card Action API. The overall status of the Bulk SIM Card Action can be followed through the List Bulk SIM Card Action API. |
| Request Bulk Setting SIM Card Public IPs. | `setPublicIPsBulk` | This API triggers an asynchronous operation to set a public IP for each of the specified SIM cards. For each SIM Card a SIM Card Action will be generated. The status of the SIM Card Action can be followed through the List SIM Card Action API. |
| Request Phone Number Verification | `createVerifiedNumber` | Initiates phone number verification procedure. Supports DTMF extension dialing for voice calls to numbers behind IVR systems. |
| Request Private Wireless Gateway Assignment for SIM Card Group | `setPrivateWirelessGatewayForSimCardGroup` | This action will asynchronously assign a provisioned Private Wireless Gateway to the SIM card group. Completing this operation defines that all SIM cards in the SIM card group will get their traffic controlled by the associated Private Wireless Gateway. This operation will also imply that new SIM cards assigned to a group will inherit its network definitions. If it's moved to a different group that doesn't have a Private Wireless Gateway, it'll use Telnyx's default mobile network configuration. |
| Request Private Wireless Gateway Removal from SIM Card Group | `removeSimCardGroupPrivateWirelessGateway` | This action will asynchronously remove an existing Private Wireless Gateway definition from a SIM card group. Completing this operation defines that all SIM cards in the SIM card group will get their traffic handled by Telnyx's default mobile network configuration. |
| Request Recording for a Call | `startTeXMLCallRecording` | Starts recording with specified parameters for call idientified by call sid. |
| Request Removing a SIM Card Public IP | `removeSimCardPublicIp` | This API removes an existing public IP from a SIM card. The API will trigger an asynchronous operation called a SIM Card Action. The status of the SIM Card Action can be followed through the List SIM Card Action API. |
| Request Setting a SIM Card Public IP | `setSimCardPublicIp` | This API makes a SIM card reachable on the public internet by mapping a random public IP to the SIM card. The API will trigger an asynchronous operation called a SIM Card Action. The status of the SIM Card Action can be followed through the List SIM Card Action API. Setting a Public IP to a SIM Card incurs a charge and will only succeed if the account has sufficient funds. |
| Request Setting a SIM Card to Standby | `setSimCardStandby` | The SIM card will be able to connect to the network once the process to set it to standby has been completed, thus making it possible to consume data. To set a SIM card to standby, it must be associated with SIM card group. The API will trigger an asynchronous operation called a SIM Card Action. Transitioning to the standby state may take a period of time. The status of the SIM Card Action can be followed through the List SIM Card Action API. |
| Request Siprec Session for a Call | `startTeXMLSiprecSession` | Starts siprec session with specified parameters for call idientified by call sid. |
| Request Wireless Blocklist Assignment for SIM Card Group | `setWirelessBlocklistForSimCardGroup` | This action will asynchronously assign a Wireless Blocklist to all the SIMs in the SIM card group. |
| Request Wireless Blocklist Removal from SIM Card Group | `removeWirelessBlocklistForSimCardGroup` | This action will asynchronously remove an existing Wireless Blocklist to all the SIMs in the SIM card group. |
| Resend Brand 2FA Email | `resendBrand2faEmail` | Resend brand 2FA email |
| Resend Verification Code | `resendWhatsappVerification` | Resend verification code |
| Resume Run | `postpublicmissionsmissionsmissionidrunsrunidresume` | Resume a paused run |
| Retrieve a Call Control Application | `retrieveCallControlApplication` | Retrieves the details of an existing call control application. |
| Retrieve a Call from a Queue | `retrieveCallFromQueue` | Retrieve an existing call from an existing queue |
| Retrieve a Call Queue | `retrieveCallQueue` | Retrieve an existing call queue |
| Retrieve a Call Recording | `getRecording` | Retrieves the details of an existing call recording. |
| Retrieve a Call Status | `retrieveCallStatus` | Returns the status of a call (data is available 10 minutes after call ended). |
| Retrieve a Civic Address | `getExternalConnectionCivicAddress` | Return the details of an existing Civic Address with its Locations inside the 'data' attribute of the response. |
| Retrieve a Comment | `retrieveComment` | Retrieve a comment |
| Retrieve a Conference | `retrieveConference` | Retrieve an existing conference |
| Retrieve a Conference Participant | `retrieveConferenceParticipant` | Retrieve details of a specific conference participant by their ID or label. |
| Retrieve a Connection | `retrieveConnection` | Retrieves the high-level details of an existing connection. To retrieve specific authentication information, use the endpoint for the specific connection type. |
| Retrieve a Credential Connection | `retrieveCredentialConnection` | Retrieves the details of an existing credential connection. |
| Retrieve a CSV Download | `getCsvDownload` | Retrieve a CSV download |
| Retrieve a Document | `retrieveDocument` | Retrieve a document. |
| Retrieve a Document Requirement | `retrieveDocumentRequirements` | Retrieve a document requirement record |
| Retrieve a Fax Application | `getFaxApplication` | Return the details of an existing Fax Application inside the 'data' attribute of the response. |
| Retrieve a Global IP | `getGlobalIp` | Retrieve a Global IP. |
| Retrieve a Global IP | `getGlobalIpAssignment` | Retrieve a Global IP assignment. |
| Retrieve a Global IP Health Check | `getGlobalIpHealthCheck` | Retrieve a Global IP health check. |
| Retrieve a List of Phone Numbers Associated to Orders | `retrieveOrderPhoneNumbers` | Get a list of phone numbers associated to orders. |
| Retrieve a LOA Configuration | `getLoaConfiguration` | Retrieve a specific LOA configuration. |
| Retrieve a Log Message | `getExternalConnectionLogMessage` | Retrieve a log message for an external connection associated with your account. |
| Retrieve a Managed Account | `retrieveManagedAccount` | Retrieves the details of a single managed account. |
| Retrieve a Message | `getMessage` | Note: This API endpoint can only retrieve messages that are no older than 10 days since their creation. If you require messages older than this, please generate an MDR report. |
| Retrieve a Messaging Hosted Number | `getMessagingHostedNumber` | Retrieve a specific messaging hosted number by its ID or phone number. |
| Retrieve a Messaging Hosted Number Order | `getMessagingHostedNumberOrder` | Retrieve a messaging hosted number order |
| Retrieve a Messaging Profile | `retrieveMessagingProfile` | Retrieve a messaging profile |
| Retrieve a Mobile Phone Number | `retrieveMobilePhoneNumber` | Retrieve a Mobile Phone Number |
| Retrieve a Mobile Phone Number with Messaging Settings | `getMobilePhoneNumberMessagingSettings` | Retrieve a mobile phone number with messaging settings |
| Retrieve a Mobile Voice Connection | `retrieveMobileVoiceConnection` | Retrieve a Mobile Voice Connection |
| Retrieve a Network | `getNetwork` | Retrieve a Network. |
| Retrieve a Number Block Order | `retrieveNumberBlockOrder` | Get an existing phone number block order. |
| Retrieve a Number Order | `retrieveNumberOrder` | Get an existing phone number order. |
| Retrieve a Number Reservation | `retrieveNumberReservation` | Gets a single phone number reservation. |
| Retrieve a Phone Number | `getExternalConnectionPhoneNumber` | Return the details of a phone number associated with the given external connection. |
| Retrieve a Phone Number | `retrievePhoneNumber` | Retrieve a phone number |
| Retrieve a Phone Number with Messaging Settings | `getPhoneNumberMessagingSettings` | Retrieve a phone number with messaging settings |
| Retrieve a Phone Number with Voice Settings | `getPhoneNumberVoiceSettings` | Retrieve a phone number with voice settings |
| Retrieve a Phone Numbers Job | `retrievePhoneNumbersJob` | Retrieve a phone numbers job |
| Retrieve a Porting Activation Job | `getPortingOrdersActivationJob` | Returns a porting activation job. |
| Retrieve a Porting Order | `getPortingOrder` | Retrieves the details of an existing porting order. |
| Retrieve a Public Internet Gateway | `getPublicInternetGateway` | Retrieve a Public Internet Gateway. |
| Retrieve a Recording Transcription | `getRecordingTranscription` | Retrieves the details of an existing recording transcription. |
| Retrieve a Release Request | `getExternalConnectionRelease` | Return the details of a Release request and its phone numbers. |
| Retrieve a Report | `getPortingReport` | Retrieve a specific report generated. |
| Retrieve a Report | `getPortoutReport` | Retrieve a specific report generated. |
| Retrieve a Requirement Types | `retrieveRequirementType` | Retrieve a requirement type by id |
| Retrieve a Short Code | `retrieveShortCode` | Retrieve a short code |
| Retrieve a Single Phone Number Within a Number Order. | `getNumberOrderPhoneNumber` | Get an existing phone number in number order. |
| Retrieve a SIPREC Connector | `getSiprecConnector` | Returns details of a stored SIPREC connector. |
| Retrieve a Stored Credential | `getCustomStorageCredentials` | Returns the information about custom storage credentials. |
| Retrieve a Sub Number Order | `getSubNumberOrder` | Get an existing sub number order. |
| Retrieve a Sub Number Orders Report | `getSubNumberOrdersReport` | Get the status and details of a sub number orders report. |
| Retrieve a Suppression | `showEmailBlock` | Retrieve a suppression |
| Retrieve a TeXML Application | `getTexmlApplication` | Retrieves the details of an existing TeXML Application. |
| Retrieve a UAC Connection | `retrieveUacConnection` | Retrieves the details of an existing UAC connection. |
| Retrieve a User Address | `getUserAddress` | Retrieves the details of an existing user address. |
| Retrieve a Verified Number | `getVerifiedNumber` | Retrieve a verified number |
| Retrieve a Virtual Cross Connect | `getVirtualCrossConnect` | Retrieve a Virtual Cross Connect. |
| Retrieve a Webhook | `getEmailDomainWebhook` | Retrieve a webhook |
| Retrieve a WireGuard Interfaces | `getWireguardInterface` | Retrieve a WireGuard Interfaces. |
| Retrieve All Comments | `listComments` | Retrieve all comments |
| Retrieve an Access IP Address | `getAccessIpAddress` | Retrieve an access IP address |
| Retrieve an Address | `getAddress` | Retrieves the details of an existing address. |
| Retrieve an Alphanumeric Sender ID | `getAlphanumericSenderId` | Retrieve a specific alphanumeric sender ID. |
| Retrieve an Authentication Provider | `getAuthenticationProvider` | Retrieves the details of an existing authentication provider. |
| Retrieve an Email Domain | `getEmailDomain` | Shared ( type: shared ) Telnyx-managed domains are included/readable for every account, in addition to the account's own custom domains. |
| Retrieve an External Connection | `getExternalConnection` | Return the details of an existing External Connection inside the 'data' attribute of the response. |
| Retrieve an FQDN | `retrieveFqdn` | Return the details regarding a specific FQDN. |
| Retrieve an FQDN Connection | `retrieveFqdnConnection` | Retrieves the details of an existing FQDN connection. |
| Retrieve an Inexplicit Number Order | `retrieveInexplicitNumberOrder` | Get an existing inexplicit number order by ID. |
| Retrieve an IP | `retrieveIp` | Return the details regarding a specific IP. |
| Retrieve an IP Connection | `retrieveIpConnection` | Retrieves the details of an existing ip connection. |
| Retrieve an Outbound Voice Profile | `getOutboundVoiceProfile` | Retrieves the details of an existing outbound voice profile. |
| Retrieve an RCS Agent | `getRCSAgentById` | Retrieve an RCS agent |
| Retrieve an Unsubscribe Group | `showUnsubscribeGroup` | Retrieve an unsubscribe group |
| Retrieve an Upload Request | `getExternalConnectionUpload` | Return the details of an Upload request and its phone numbers. |
| Retrieve Black Box Test Results | `getBlackBoxTestResults` | Returns the results of the various black box tests |
| Retrieve Bulk Update Status | `getBulkUpdateMessagingSettingsOnPhoneNumbersStatus` | Retrieve bulk update status |
| Retrieve Bundles | `getUserBillingBundles` | Get all allowed bundles. |
| Retrieve Calls from a Queue | `listQueueCalls` | Retrieve the list of calls in an existing queue |
| Retrieve Group MMS Messages | `getGroupMmsMessages` | Retrieve all messages in a group MMS conversation by the group message ID. |
| Retrieve Messaging Report | `getUsageReport` | Fetch a single messaging usage report by id |
| Retrieve Regulatory Requirements | `listRegulatoryRequirements` | Retrieve regulatory requirements |
| Retrieve Regulatory Requirements for a List of Phone Numbers | `listRegulatoryRequirementsPhoneNumbers` | Retrieve regulatory requirements for a list of phone numbers |
| Retrieve Stored Dialogflow Connection | `getDialogflowConnection` | Return details of the Dialogflow connection associated with the given CallControl connection. |
| Retrieve Stored Media | `getMediaStorage` | Returns the information about a stored media file. |
| Retrieve the Associated V1 Sub Request ID and Port Request ID | `getPortingOrderSubRequest` | Retrieve the associated V1 sub request id and port request id |
| Retrieve the Features for a List of Numbers | `postNumbersFeatures` | Retrieve the features for a list of numbers |
| Retrieve the WireGuard Peer | `getWireguardPeer` | Retrieve the WireGuard peer. |
| Retrieve Verification | `retrieveVerification` | Retrieve verification |
| Retrieve Verify Profile | `getVerifyProfile` | Gets a single Verify profile. |
| Retrieve Verify Profile Message Templates | `listProfileMessageTemplates` | List all Verify profile message templates. |
| Retrieve Voice SDK Call Reports by Call ID | `getVoiceSdkCallReport` | Returns raw call report stats JSON payloads stored for the authenticated user and call id . The user is derived from Telnyx authentication, not from request parameters. |
| Retrieve WireGuard Config Template for Peer | `getWireguardPeerConfig` | Retrieve Wireguard config template for Peer |
| Retrieves a Mobile Push Credential | `getPushCredentialById` | Retrieves mobile push credential based on the given push credential id |
| Retrieves a Phone Number Blocks Job | `getPhoneNumberBlocksJob` | Retrieves a phone number blocks job |
| Retry an Upload Request | `retryUpload` | If there were any errors during the upload process, this endpoint will retry the upload request. In some cases this will reattempt the existing upload request, in other cases it may create a new upload request. Please check the ticket id in the response to determine if a new upload request was created. |
| Revet Brand | `revetBrand` | This operation allows you to revet the brand. However, revetting is allowed once after the successful brand registration and thereafter limited to once every 3 months. |
| Revoke OAuth Grant | `revokeOAuthGrant` | Revoke an OAuth grant |
| Rotate the Metadata Token | `rotateCloudfsMetaToken` | Issues a new metadata access token for the filesystem and returns the full filesystem, including the new meta token and credential-bearing meta url . The previous token stops authenticating immediately; the metadata database and S3 bucket are unchanged. The request takes no body. Allowed while the filesystem is ready or needs format ; otherwise returns a 409 . Retrying with the same Idempotency-Key within 24 hours replays the original response — including the same token — instead of rotating again. |
| Run a Portability Check | `postPortabilityCheck` | Runs a portability check, returning the results immediately. |
| Schedule a Future Requirement Version | `createRequirementVersion` | Create a new pending version of a requirement with a future effective start date. Only one pending version may exist per requirement at a time. |
| Schedule a Message | `scheduleMessage` | Schedule a message with a Phone Number, Alphanumeric Sender ID, Short Code or Number Pool. This endpoint allows you to schedule a message with any messaging resource. Current messaging resources include: long-code, short-code, number-pool, and alphanumeric-sender-id. |
| Search Conversation Histories | `searchConversationHistories` | Performs semantic vector search across conversation history records. How it works: 1. The query text is embedded into a 1024-dimensional vector using the multilingual-e5-large model. 2. The vector is compared against indexed record chunks using semantic similarity search. 3. When no region is specified, all regions are queried in parallel (fan-out) and results are merged by score. 4. Results are ranked by similarity score (descending) and paginated via page[number] / page[size] . Authentication: Requires a Telnyx API key via Authorization: Bearer . Results are automatically scoped to the caller's organization — organization id is injected from the auth token and cannot be overridden. Chunking: Records are split into chunks of up to 480 tokens with 64-token overlap at ingestion time. Each search result represents a single chunk, with chunk index and chunk total indicating its position within the original record. Filtering: Use filter[field][operator]=value query parameters to narrow. |
| Search Detail Records | `searchDetailRecords` | Search for any detail record across the Telnyx Platform |
| Search for Documents | `postEmbeddingSimilaritySearch` | Perform a similarity search on a Telnyx Storage Bucket, returning the most similar num docs document chunks to the query. Currently the only available distance metric is cosine similarity which will return a distance between 0 and 1. The lower the distance, the more similar the returned document chunks are to the query. A certainty will also be returned, which is a value between 0 and 1 where the higher the certainty, the more similar the document. You can read more about Weaviate distance metrics here: Weaviate Docs If a bucket was embedded using a custom loader, such as intercom , the additional metadata will be returned in the loader metadata field. |
| Send a Fax | `sendFax` | Send a fax. Files have size limits and page count limit validations. If a file is bigger than 50MB or has more than 350 pages it will fail with file size limit exceeded and page count limit exceeded respectively. Supported file formats: - PDF ( application/pdf ) - TIFF ( application/tiff , image/tiff ) - JPEG ( image/jpeg ) - PNG ( image/png ) - Microsoft Word .doc ( application/msword ) - Microsoft Word .docx ( application/vnd.openxmlformats-officedocument.wordprocessingml.document ) - Rich Text Format .rtf ( application/rtf ) - Plain text .txt ( text/plain ) Expected Webhooks: - fax.queued - fax.media.processed - fax.sending.started - fax.delivered - fax.failed |
| Send a Group MMS Message | `createGroupMmsMessage` | Send a group MMS message |
| Send a Long Code Message | `createLongCodeMessage` | Send a long code message |
| Send a Message | `sendMessage` | Send a message with a Phone Number, Alphanumeric Sender ID, Short Code or Number Pool. This endpoint allows you to send a message with any messaging resource. Current messaging resources include: long-code, short-code, number-pool, and alphanumeric-sender-id. |
| Send a Message Using an Alphanumeric Sender ID | `sendAlphanumericSenderIdMessage` | Send an SMS message using an alphanumeric sender ID. This is SMS only. |
| Send a Message Using Number Pool | `createNumberPoolMessage` | Send a message using number pool |
| Send a Short Code Message | `createShortCodeMessage` | Send a short code message |
| Send a Whatsapp Message | `sendWhatsappMessage` | Send a Whatsapp message |
| Send an Email-ownership Verification Code | `requestDirEmailVerification` | Email a 6-digit code to the DIR's authorizer email to confirm ownership of that address. The code expires in 15 minutes. Requesting a new code invalidates any previous one. Resends are rate limited (a short cooldown plus a daily cap). Submit the code to POST /dir/{dir id}/verify email/confirm . |
| Send an RCS Message | `sendRCSMessage` | Send an RCS message |
| Send DTMF | `sendDTMF` | Sends DTMF tones from this leg. DTMF tones will be heard by the other end of the call. Expected Webhooks: There are no webhooks associated with this command. |
| Send DTMF to Conference Participants | `conferenceSendDTMF` | Send DTMF tones to one or more conference participants. |
| Send SIP Info | `sendSIPInfo` | Sends SIP info from this leg. Expected Webhooks: - call.sip info.received (to be received on the target call leg) |
| Send the Verification Codes | `sendPortingVerificationCodes` | Send the verification code for all porting phone numbers. |
| Set a Key's Value | `putKvKey` | Creates or replaces the value for a key. The request body is stored verbatim as the value — no base64, no JSON envelope — up to 1 MiB. The request's Content-Type header is stored with the value and echoed back on retrieval. Returns 201 when the key is created and 200 when an existing key is updated. |
| Settle a Payment | `settleX402Payment` | Settles an x402 payment using the quote ID and a signed payment authorization. The payment signature can be provided via the PAYMENT-SIGNATURE header or the payment signature body parameter. Settlement is idempotent — submitting the same quote ID multiple times returns the existing transaction. |
| Share a Porting Order | `sharePortingOrder` | Creates a sharing token for a porting order. The token can be used to share the porting order with non-Telnyx users. |
| Show a Port-out Event | `showPortoutEvent` | Show a specific port-out event. |
| Show a Porting Event | `showPortingEvent` | Show a specific porting event. |
| SIP Refer a Call | `referCall` | Initiate a SIP Refer on a Call Control call. You can initiate a SIP Refer at any point in the duration of a call. Expected Webhooks: - call.refer.started - call.refer.completed - call.refer.failed |
| SIP Registration Status | `getSipRegistrationStatus` | Returns the live SIP registration state of a UAC connection: whether it is currently registered, when it last registered, and the last response Telnyx received from the registrar. Only uac external credential is supported today. |
| SIPREC Start | `startSiprecSession` | Start siprec session to configured in SIPREC connector SRS. Expected Webhooks: - siprec.started - siprec.stopped - siprec.failed |
| SIPREC Stop | `stopSiprecSession` | Stop SIPREC session. Expected Webhooks: - siprec.stopped |
| Slim List Phone Numbers | `slimListPhoneNumbers` | List phone numbers, This endpoint is a lighter version of the /phone numbers endpoint having higher performance and rate limit. |
| Soft-delete a Suppression | `deleteEmailBlock` | Soft-deletes (status → removed ; tombstone retained). A removed audit event is appended unless the block was already removed (idempotent — returns the existing row with 200 and no new event). Mutates updated at . |
| Speak Text | `speakCall` | Convert text to speech and play it back on the call. If multiple speak text commands are issued consecutively, the audio files will be placed in a queue awaiting playback. Expected Webhooks: - call.speak.started - call.speak.ended |
| Speak Text to Conference Participants | `speakTextToConference` | Convert text to speech and play it to all or some participants. |
| Speech to Text Over WebSocket | `transcriptionOverWs` | DEPRECATED - NOT AN HTTP ENDPOINT, CANNOT WORK AS AN ACTION. Telnyx speech-to-text streaming is a WebSocket service: you open wss://api.telnyx.com/v2/speech-to-text/transcription, send binary audio frames and read JSON transcript frames (https://developers.telnyx.com/docs/tts-stt/stt-websocket-streaming and https://developers.telnyx.com/api-reference/websockets/stream-speech-to-text-over-websocket). Modelled here as a plain HTTP GET, so Telnyx rejects every call with 400 "'connection' header must contain 'upgrade', got []" (verified 2026-09-03). No catalog edit can fix this - fastn HTTP actions cannot perform a WebSocket upgrade or stream frames. For non-streaming transcription use the Transcribe Speech to Text action (POST /v2/ai/audio/transcriptions) instead. |
| Start a Run | `postpublicmissionsmissionsmissionidruns` | Start a new run for a mission |
| Start AI Assistant | `callStartAIAssistant` | Start an AI assistant on the call. Expected Webhooks: - call.conversation.ended - call.conversation insights.generated |
| Start Conversation Relay | `callStartConversationRelay` | Start a Conversation Relay session on an active call. Conversation Relay connects the call audio to your WebSocket so your application can exchange realtime messages with the caller while Telnyx handles speech recognition and text-to-speech. Only one AI Assistant or Conversation Relay session can be active on a call at a time. Expected Webhooks: - call.conversation.ended - Sent when the Conversation Relay session ends. If the customer WebSocket disconnects, the webhook payload reason is customer disconnect . |
| Start Streaming Media from a Call. | `startTeXMLCallStreaming` | Starts streaming media from a call to a specific WebSocket address. |
| Stop a Migration | `stopMigration` | Stop a Migration |
| Stop AI Assistant | `callStopAIAssistant` | Stop an AI assistant on the call. |
| Stop Audio Being Played on the Conference | `stopConferenceAudio` | Stop audio being played to all or some participants on a conference call. |
| Stop Audio Playback | `stopCallPlayback` | Stop audio being played on the call. Expected Webhooks: - call.playback.ended or call.speak.ended |
| Stop Conversation Relay | `callStopConversationRelay` | Stop the active Conversation Relay session on a call. |
| Stream Text to Speech Over WebSocket | `textToSpeechOverWs` | Open a WebSocket connection to stream text and receive synthesized audio in real time. Authentication is provided via the standard Authorization: Bearer header. Send JSON frames with text to synthesize; receive JSON frames containing base64-encoded audio chunks. Supported providers: aws , telnyx , azure , murfai , minimax , rime , resemble , elevenlabs , xai . Connection flow: 1. Open WebSocket with query parameters specifying provider, voice, and model. 2. Send an initial handshake message {"text": " "} (single space) with optional voice settings to initialize the session. 3. Send text messages as {"text": "Hello world"} . 4. Receive audio chunks as JSON frames with base64-encoded audio. 5. A final frame with isFinal: true indicates the end of audio for the current text. To interrupt and restart synthesis mid-stream, send {"force": true} — the current worker is stopped and a new one is started. Note: The Telnyx Ultra model is not available over WebSocket. Use the HTTP POST. |
| Streaming Start | `startCallStreaming` | Start streaming the media from a call to a specific WebSocket address or Dialogflow connection in near-realtime. Audio will be delivered as base64-encoded RTP payload (raw audio), wrapped in JSON payloads. Please find more details about media streaming messages specification under the link. |
| Streaming Stop | `stopCallStreaming` | Stop streaming a call to a WebSocket. Expected Webhooks: - streaming.stopped |
| Submit a DIR for Vetting | `submitDirSimple` | Submit a DIR for vetting. Sends the DIR back through the vetting cycle from any non-terminal status. When re-submitting from suspended or expired , the DIR's previous Branded Calling registration is torn down transactionally and its phone numbers flip back to submitted . When re-submitting from verified , the existing registration stays live throughout the new vetting cycle. Returns 400 from submitted / in review / permanently rejected . Returns 409 if the DIR has an unresolved infringement claim. |
| Submit a DIR's References | `submitDirReferences` | Submit the two business references and one financial reference for a DIR. The DIR's authorizer email must be verified first (see the email-verification endpoint). Until it is, this returns 409 and no references are stored. The request body carries exactly two business references plus one financial reference. On success the references are stored and the response echoes them in the same shape as the GET. Submitting again converges on the already-stored references rather than erroring. |
| Submit a Porting Order. | `confirmPortingOrder` | Confirm and submit your porting order. |
| Submit a Requirement Group for Approval | `submitRequirementGroup` | Submit a Requirement Group for Approval |
| Submit Campaign | `postCampaign` | Before creating a campaign, use the Qualify By Usecase endpoint to ensure that the brand you want to assign a new campaign to is qualified for the desired use case of that campaign. Please note: After campaign creation, you'll only be able to edit the campaign's sample messages. Creating a campaign will entail an upfront, non-refundable three month's cost that will depend on the campaign's use case (see 10DLC Costs section for details). |
| Submit Campaign Appeal for Manual Review | `appealCampaign` | Submits an appeal for rejected native campaigns in TELNYX FAILED or MNO REJECTED status. The appeal is recorded for manual compliance team review and the campaign status is reset to TCR ACCEPTED. Note: Appeal forwarding is handled manually to allow proper review before incurring upstream charges. |
| Submit Phone Numbers for Reputation Remediation | `submitReputationRemediation` | Submit a batch of phone numbers belonging to this enterprise for reputation remediation. The request is accepted asynchronously: this endpoint returns 202 with the persisted request id, then the request transitions through processing states until completion. Use the GET endpoints to poll status and per-number results. Each phone number must be in E.164 format and belong to this enterprise. A number that already has an in-flight remediation request is rejected. |
| Submit Telco Data Usage Report | `submitTelcoDataUsageReport` | Submit a new telco data usage report |
| Submit Verification Code | `verifyVerificationCode` | Submit verification code |
| Submit Verification Code for a Phone Number | `verifyWhatsappPhoneNumber` | Submit verification code for a phone number |
| Submit Verification Request | `submitVerificationRequest` | Submit a new tollfree verification request |
| Summarize File Content | `postSummary` | Generate a summary of a file's contents. Supports the following text formats: - PDF, HTML, txt, json, csv Supports the following media formats (billed for both the transcription and summary): - flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm - Up to 100 MB |
| Switch Supervisor Role | `switchSupervisorRole` | Switch the supervisor role for a bridged call. This allows switching between different supervisor modes during an active call |
| Test Assistant Tool | `testassistanttoolpublicassistantsassistantidtoolstoolidtestpost` | Test a webhook tool for an assistant |
| Token Introspection | `introspectOAuthToken` | Introspect an OAuth access token to check its validity and metadata |
| Transcribe Speech to Text | `audiopublicaudiotranscriptionspost` | Transcribe speech to text. This endpoint is consistent with the OpenAI Transcription API and may be used with the OpenAI JS or Python SDK. |
| Transcription Start | `startCallTranscription` | Start real-time transcription. Transcription will stop on call hang-up, or can be initiated via the Transcription stop command. Expected Webhooks: - call.transcription |
| Transcription Stop | `stopCallTranscription` | Stop real-time transcription. |
| Transfer Call | `transferCall` | Transfer a call to a new destination. If the transfer is unsuccessful, a call.hangup webhook for the other call (Leg B) will be sent indicating that the transfer could not be completed. The original call will remain active and may be issued additional commands, potentially transfering the call to an alternate destination. Expected Webhooks: - call.initiated - call.bridged to Leg B - call.answered or call.hangup - call.machine.detection.ended if answering machine detection was requested - call.machine.greeting.ended if answering machine detection was requested to detect the end of machine greeting - call.machine.premium.detection.ended if answering machine detection=premium was requested - call.machine.premium.greeting.ended if answering machine detection=premium was requested and a beep was detected |
| Trigger a Manual Test Run | `triggertestrunpublicassistantsteststestidrunspost` | Initiates immediate execution of a specific assistant test |
| Trigger Brand SMS OTP | `triggerBrandSmsOtp` | Trigger or re-trigger an SMS OTP (One-Time Password) for Sole Proprietor brand verification. Important Notes: Only allowed for Sole Proprietor ( SOLE PROPRIETOR ) brands Triggers generation of a one-time password sent to the mobilePhone number in the brand's profile Campaigns cannot be created until OTP verification is complete US/CA numbers only for real OTPs; mock brands can use non-US/CA numbers for testing Returns a referenceId that can be used to check OTP status via the GET /10dlc/brand/smsOtp/{referenceId} endpoint Use Cases: Initial OTP trigger after Sole Proprietor brand creation Re-triggering OTP if the user didn't receive or needs a new code |
| Trigger Call Verification | `createVerificationCall` | Trigger Call verification |
| Trigger Flash Call Verification | `createFlashcallVerification` | Trigger Flash call verification |
| Trigger SMS Verification | `createVerificationSms` | Trigger SMS verification |
| Trigger Test Suite Execution | `triggertestsuiterunspublicassistantsteststestsuitessuitenamerunspost` | Executes all tests within a specific test suite as a batch operation |
| Trigger WhatsApp Verification | `createWhatsappVerification` | Trigger WhatsApp verification |
| Unassign Insight Template from Group | `unassigninsightfromgroup` | Remove an insight from a group |
| Unhold Conference Participants | `unholdConferenceParticipants` | Unhold a list of participants in a conference call |
| Unlink Telnyx Agent | `deletepublicmissionsmissionsmissionidrunsrunidtelnyxagentstelnyxagentid` | Unlink a Telnyx agent from a run |
| Unmute Conference Participants | `unmuteConferenceParticipants` | Unmute a list of participants in a conference call |
| Unmute Participants in Room Session. | `unmuteParticipantInSession` | Unmute participants in room session. |
| Update a Batch of Numbers | `createUpdatePhoneNumbersJob` | Creates a new background job to update a batch of numbers. At most one thousand numbers can be updated per API call. At least one of the updateable fields must be submitted. IMPORTANT: You must either specify filters (using the filter parameters) or specific phone numbers (using the phone numbers parameter in the request body). If you specify filters, ALL phone numbers that match the given filters (up to 1000 at a time) will be updated. If you want to update only specific numbers, you must use the phone numbers parameter in the request body. When using the phone numbers parameter, ensure you follow the correct format as shown in the example (either phone number IDs or phone numbers in E164 format). |
| Update a Billing Group | `updateBillingGroup` | Update a billing group |
| Update a Call Control Application | `updateCallControlApplication` | Updates settings of an existing call control application. |
| Update a CloudFS Filesystem | `updateCloudfsFilesystem` | Updates a CloudFS filesystem. Only name can be changed; other fields are immutable and unknown fields are rejected with a 400 . Renaming to a name that already exists in your organization returns a 422 . |
| Update a Conference Participant | `updateConferenceParticipant` | Update properties of a conference participant. |
| Update a Conference Participant | `updateTexmlConferenceParticipant` | Updates a conference participant |
| Update a Conference Resource | `updateTexmlConference` | Updates a conference resource. |
| Update a Credential | `updateTelephonyCredential` | Update an existing credential. |
| Update a Credential Connection | `updateCredentialConnection` | Updates settings of an existing credential connection. |
| Update a DIR | `updateDirSimple` | Edit a DIR. DIRs in draft , rejected , unsuccessful , or suspended can be edited freely: PATCH is a pure edit, status is never changed, and you re-vet by calling POST /v2/dir/{dir id}/submit explicitly. A verified DIR can also be edited in place: a PATCH that changes any value returns the DIR to draft and branded delivery stops until you re-submit and the DIR is approved again, while a PATCH that changes nothing (an empty body or values identical to the current ones) leaves the DIR verified , so idempotent retries are safe. DIRs in any other status ( submitted , in review , expired , infringement claimed , permanently rejected ) cannot be edited. |
| Update a DIR Reference | `updateDirReference` | Partially update one reference, addressed by the DIR id plus the reference's type (business or financial) and slot. Cosmetic fields (full name, job title, organization, relationship, email) are always editable. The phone number and timezone may only be changed while a scheduled call has not yet been dialed; if a call is in progress or all attempts are complete, those fields are locked. Changing the timezone reschedules any pending call into the new local calling window. |
| Update a DIR to Resolve an Infringement Concern | `updateDirInfringement` | Push a fix for a DIR that is suspended with an open infringement claim back into vetting. POST /dir/{dir id}/submit is blocked while a claim is open, so this is the customer-callable path to update the DIR's content and re-certify before Telnyx adjudicates the claim. All four certification booleans must be true . Optional content fields ( display name , logo url , call reasons , documents ) update the DIR; documents are append-only. |
| Update a Document | `updateDocument` | Update a document. |
| Update a Fax Application | `updateFaxApplication` | Updates settings of an existing Fax Application based on the parameters of the request. |
| Update a Global IP Assignment | `updateGlobalIpAssignment` | Update a Global IP assignment. |
| Update a LOA Configuration | `updateLoaConfiguration` | Update a specific LOA configuration. |
| Update a Location's Static Emergency Address | `updateLocation` | Update a location's static emergency address |
| Update a Managed Account | `updateManagedAccount` | Update a single managed account. |
| Update a Messaging Hosted Number | `updateMessagingHostedNumber` | Update the messaging settings for a hosted number. |
| Update a Messaging Profile | `updateMessagingProfile` | Update a messaging profile |
| Update a Mobile Phone Number | `updateMobilePhoneNumber` | Update a Mobile Phone Number |
| Update a Mobile Voice Connection | `updateMobileVoiceConnection` | Update a Mobile Voice Connection |
| Update a Network | `updateNetwork` | Update a Network. |
| Update a Notification Channel | `updateNotificationChannel` | Update a notification channel. |
| Update a Notification Profile | `updateNotificationProfile` | Update a notification profile. |
| Update a Number Order | `updateNumberOrder` | Updates a phone number order. |
| Update a Phone Number | `updateExternalConnectionPhoneNumber` | Asynchronously update settings of the phone number associated with the given external connection. |
| Update a Phone Number | `updatePhoneNumber` | Update a phone number |
| Update a Phone Number with Voice Settings | `updatePhoneNumberVoiceSettings` | Update a phone number with voice settings |
| Update a Porting Activation Job | `updatePortingOrdersActivationJob` | Updates the activation time of a porting activation job. |
| Update a Pronunciation Dictionary | `updatePronunciationDict` | Update the name and/or items of an existing pronunciation dictionary. Uses optimistic locking — if the dictionary was modified concurrently, the request returns 409 Conflict. |
| Update a Queue | `updateQueue` | Update properties of an existing call queue. |
| Update a Queue Resource | `updateTexmlQueue` | Updates a queue resource. |
| Update a Room. | `updateRoom` | Synchronously update a Room. |
| Update a SIM Card | `updateSimCard` | Updates SIM card data |
| Update a SIM Card Group | `updateSimCardGroup` | Updates a SIM card group |
| Update a SIPREC Connector | `updateSiprecConnector` | Updates a stored SIPREC connector configuration. |
| Update a Specific Assistant Version | `updateassistantversionpublicassistantsassistantidversionsversionidpost` | Updates the configuration of a specific assistant version. Can not update main version |
| Update a Stored Credential | `updateCustomStorageCredentials` | Updates a stored custom credentials configuration. |
| Update a Sub Number Order's Requirements | `updateSubNumberOrder` | Updates a sub number order. |
| Update a TeXML Application | `updateTexmlApplication` | Updates settings of an existing TeXML Application. |
| Update a Traffic Policy Profile | `updateTrafficPolicyProfile` | Updates a traffic policy profile. |
| Update a UAC Connection | `updateUacConnection` | Updates settings of an existing UAC connection. |
| Update a Voice Clone | `updateVoiceClone` | Updates the name, language, or gender of a voice clone. |
| Update a Webhook | `updateEmailDomainWebhook` | Update a webhook's URL and/or event subscription. A webhook is bound to its domain — domain id is not mutable. |
| Update a Whatsapp Message Template | `patchWhatsappTemplate` | Update a Whatsapp message template |
| Update a Wireless Blocklist | `updateWirelessBlocklist` | Update a Wireless Blocklist. |
| Update Advanced Order | `updateadvancedorderv2` | Update Advanced Order |
| Update an Assistant | `updateassistantpublicassistantsassistantidpost` | Update an AI Assistant's attributes. |
| Update an Assistant Test | `updateassistanttestpublicassistantsteststestidput` | Updates an existing assistant test configuration with new settings |
| Update an Authentication Provider | `updateAuthenticationProvider` | Updates settings of an existing authentication provider. |
| Update an Email Domain | `updateEmailDomain` | Update an email domain |
| Update an Email Template | `updateEmailTemplate` | Updates one or more template fields. |
| Update an External Connection | `updateExternalConnection` | Updates settings of an existing External Connection based on the parameters of the request. |
| Update an FQDN | `updateFqdn` | Update the details of a specific FQDN. |
| Update an FQDN Connection | `updateFqdnConnection` | Updates settings of an existing FQDN connection. |
| Update an IP | `updateIp` | Update the details of a specific IP. |
| Update an IP Connection | `updateIpConnection` | Updates settings of an existing IP connection. |
| Update an Unsubscribe Group | `updateUnsubscribeGroup` | Partial update (only name / description ). PUT is not routed. |
| Update Auto Recharge Preferences | `updateAutoRechargePrefs` | Update payment auto recharge preferences. |
| Update Auto-Response Setting | `updateAutoRespConfig` | Update Auto-Response Setting |
| Update Brand | `updateBrand` | Update a brand's attributes by brandId . |
| Update Call | `updateTexmlCall` | Update TeXML call. Please note that the keys present in the payload MUST BE formatted in CamelCase as specified in the example. |
| Update Campaign | `updateCampaign` | Update a campaign's properties by campaignId . Please note: only sample messages are editable. |
| Update Canary Deploy | `updatecanarydeployassistantsassistantidcanarydeploysput` | Endpoint to update a canary deploy configuration for an assistant. Updates the existing canary deploy configuration with new version IDs and percentages. All old versions and percentages are replaces by new ones from this request. |
| Update Client State | `updateClientState` | Updates client state |
| Update Conference Participant | `updateConference` | Update conference participant supervisor role |
| Update Conversation Metadata | `updateconversationbyidpublicconversationsput` | Update metadata for a specific conversation. |
| Update Insight Template | `updateinsightbyid` | Update an insight template |
| Update Insight Template Group | `updateinsightgroupbyid` | Update an insight template group |
| Update Knowledge Base | `putpublicmissionsmissionsmissionidknowledgebasesknowledgebaseid` | Update a knowledge base definition |
| Update MCP Server | `putpublicmissionsmissionsmissionidmcpserversmcpserverid` | Update an MCP server definition |
| Update MCP Server | `updatemcpserver` | Update an existing MCP server. |
| Update Message Template | `updateMessageTemplate` | Update an existing Verify profile message template. |
| Update Mission | `putpublicmissionsmissionsmissionid` | Update a mission definition |
| Update OAuth Client | `updateOAuthClient` | Update an existing OAuth client |
| Update Phone Number Business Profile | `patchWhatsappProfile` | Update phone number business profile |
| Update Queued Call | `updateCallInQueue` | Update queued call's keep after hangup flag |
| Update Recording on a Call | `updateTeXMLCallRecording` | Updates recording resource for particular call. |
| Update Requirement Group for a Phone Number Order | `updateNumberOrderPhoneNumberRequirementGroup` | Update requirement group for a phone number order |
| Update Requirement Group for a Sub Number Order | `updateSubNumberOrderRequirementGroup` | Update requirement group for a sub number order |
| Update Requirement Values in Requirement Group | `updateRequirementGroup` | Update requirement values in requirement group |
| Update Requirements for a Single Phone Number Within a Number Order. | `updateNumberOrderPhoneNumber` | Updates requirements for a single phone number within a number order. |
| Update Run | `patchpublicmissionsmissionsmissionidrunsrunid` | Update run status and/or result |
| Update Short Code | `updateShortCode` | Update the settings for a specific short code. To unbind a short code from a profile, set the messaging profile id to null or an empty string. To add or update tags, include the tags field as an array of strings. |
| Update Single Shared Campaign | `updateSharedCampaign` | Update campaign details by campaignId . Please note: Only webhook urls are editable. |
| Update Status | `updatePortoutStatus` | Authorize or reject portout request |
| Update Step Status | `patchpublicmissionsmissionsmissionidrunsrunidplanstepsstepid` | Update the status of a plan step |
| Update Stored Dialogflow Connection | `updateDialogflowConnection` | Updates a stored Dialogflow Connection. |
| Update Stored Media | `updateMediaStorage` | Updates a stored media file. |
| Update Streaming on a Call | `updateTeXMLCallStreaming` | Updates streaming resource for particular call. |
| Update the Amount of Allocatable Global Outbound Channels Allocated to a Specific Managed Account. | `updateManagedAccountGlobalChannelLimit` | Update the amount of allocatable global outbound channels allocated to a specific managed account. |
| Update the Emergency Settings from a Batch of Numbers | `createPhoneNumbersJobUpdateEmergencySettings` | Creates a background job to update the emergency settings of a collection of phone numbers. At most one thousand numbers can be updated per API call. |
| Update the Messaging Profile And/or Messaging Product of a Phone Number | `updatePhoneNumberMessagingSettings` | Update the messaging profile and/or messaging product of a phone number |
| Update the Virtual Cross Connect | `updateVirtualCrossConnect` | Update the Virtual Cross Connect. Cloud IPs can only be patched during the created state, as GCE will only inform you of your generated IP once the pending connection requested has been accepted. Once the Virtual Cross Connect has moved to provisioning , the IPs can no longer be patched. Once the Virtual Cross Connect has moved to provisioned and you are ready to enable routing, you can toggle the routing announcements to true . |
| Update the WireGuard Peer | `updateWireguardPeer` | Update the WireGuard peer. |
| Update Tool | `putpublicmissionsmissionsmissionidtoolstoolid` | Update a tool definition |
| Update Tool | `updatetooltoolid` | Update Tool |
| Update Verification Request | `updateVerificationRequest` | Update an existing tollfree verification request. This is particularly useful when there are pending customer actions to be taken. |
| Update Verify Profile | `updateVerifyProfile` | Update Verify profile |
| Update Voice Channels for Non-US Zones | `patchChannelZone` | Update the number of Voice Channels for the Non-US Zones. This allows your account to handle multiple simultaneous inbound calls to Non-US numbers. Use this endpoint to increase or decrease your capacity based on expected call volume. |
| Update Voice Channels for US Zone | `updateOutboundChannels` | Update the number of Voice Channels for the US Zone. This allows your account to handle multiple simultaneous inbound calls to US numbers. Use this endpoint to increase or decrease your capacity based on expected call volume. |
| Update Voicemail | `updateVoicemail` | Update voicemail settings for a phone number |
| Update WABA Settings | `patchWabaSettings` | Update WABA settings |
| Update Whatsapp User Data | `patchWhatsappUserData` | Update Whatsapp user data |
| Updates an Existing Outbound Voice Profile. | `updateOutboundVoiceProfile` | Updates an existing outbound voice profile. |
| Updates Information for a SIM Card Data Usage Notification | `patchSimCardDataUsageNotification` | Updates information for a SIM Card Data Usage Notification. |
| Updates Siprec Session for a Call | `updateTeXMLSiprecSession` | Updates siprec session identified by siprec sid. |
| Upload a Document | `createDocument` | Upload a document. Uploaded files must be linked to a service within 30 minutes or they will be automatically deleted. |
| Upload Hosted Number Document | `uploadMessagingHostedNumberOrderFile` | Upload hosted number document |
| Upload Media | `createMediaStorage` | Upload media file to Telnyx so it can be used with other Telnyx services |
| Upload Whatsapp Profile Photo | `postWhatsappProfilePhoto` | Upload Whatsapp profile photo |
| Validate a List of Call Reasons | `validateCallReasons` | Check up to 10 candidate call reasons strings against Telnyx's vetting heuristics before sending them on a DIR create or update. The endpoint flags strings that are likely to be rejected during vetting (too generic, banned phrases, length issues, etc.) so you can fix them up front. |
| Validate a Single Email Address | `createEmailValidation` | Validates a single email address and returns deliverability checks. |
| Validate an Address | `validateAddress` | Validates an address for emergency services. |
| Validate Hosted Number Codes | `validateVerificationCodesForMessagingHostedNumberOrder` | Validate the verification codes sent to the numbers of the hosted order. The verification codes must be created in the verification codes endpoint. |
| Validate SIM Cards Registration Codes | `validateRegistrationCodes` | It validates whether SIM card registration codes are valid or not. |
| Verify Brand SMS OTP | `verifyBrandSmsOtp` | Verify the SMS OTP (One-Time Password) for Sole Proprietor brand verification. Verification Flow: 1. User receives OTP via SMS after triggering 2. User submits the OTP pin through this endpoint 3. Upon successful verification: - A BRAND OTP VERIFIED webhook event is sent to the CSP - The brand's identityStatus changes to VERIFIED - Campaigns can now be created for this brand Error Handling: Provides proper error responses for: Invalid OTP pins Expired OTPs OTP verification failures |
| Verify CSR Phone Number Coverage | `verifyPhoneNumberCoverage` | Verify the coverage for a list of phone numbers. |
| Verify DNS Records for an Email Domain | `verifyEmailDomainDnsRecords` | Verify DNS records for an email domain |
| Verify Ownership of Phone Numbers | `verifyPhoneNumberOwnership` | Verifies ownership of the provided phone numbers and returns a mapping of numbers to their IDs, plus a list of numbers not found in the account. |
| Verify the Verification Code for a List of Phone Numbers | `verifyPortingVerificationCodes` | Verifies the verification code for a list of phone numbers. |
| Verify Verification Code by ID | `verifyVerificationCodeById` | Verify verification code by ID |
| Verify Verification Code by Phone Number | `verifyVerificationCodeByPhoneNumber` | Verify verification code by phone number |
| View a Fax | `viewFax` | View a fax |
| View a List of Faxes | `listFaxes` | View a list of faxes |
| View a List of Room Compositions. | `listRoomCompositions` | View a list of room compositions. |
| View a List of Room Participants. | `listRoomParticipants` | View a list of room participants. |
| View a List of Room Participants. | `retrieveListRoomParticipants` | View a list of room participants. |
| View a List of Room Recordings. | `listRoomRecordings` | View a list of room recordings. |
| View a List of Room Sessions. | `listRoomSessions` | View a list of room sessions. |
| View a List of Room Sessions. | `retrieveListRoomSessions` | View a list of room sessions. |
| View a List of Rooms. | `listRooms` | View a list of rooms. |
| View a Room Composition. | `viewRoomComposition` | View a room composition. |
| View a Room Participant. | `viewRoomParticipant` | View a room participant. |
| View a Room Recording. | `viewRoomRecording` | View a room recording. |
| View a Room Session. | `viewRoomSession` | View a room session. |
| View a Room. | `viewRoom` | View a room. |
