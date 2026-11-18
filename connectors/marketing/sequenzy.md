---
description: "Sequenzy email marketing and automation platform."
hidden: true
---

# Sequenzy

<img src="../../.gitbook/assets/connectors/lg/sequenzy.png" alt="Sequenzy logo">

Sequenzy email marketing and automation platform. Manage subscribers, lists, segments, tags, campaigns, sequences, templates, landing pages, forms, popups, A/B tests, transactional email, SMS, metrics, integrations and outbound webhooks via the Sequenzy REST API (https://api.sequenzy.com/api/v1).

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [sequenzy.com](https://sequenzy.com) |
| **Authentication** | API key |
| **Slug** | `sequenzy` |

## Use it

Add Sequenzy from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.sequenzy.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Account Suggestions | `acceptAccountSuggestions` | Accept Account Suggestions. POST /api/v1/account-suggestions. Docs: https://docs.sequenzy.com/api-reference/accounts/suggestions-accept |
| Activate Storefront Pixel | `activateStorefrontPixel` | Activate Storefront Pixel for an integration. POST /api/v1/integrations/{id}/pixel. |
| Add A/B Test Variant | `addABTestVariant` | Add A/B Test Variant. POST /api/v1/ab-tests/{abTestId}/variants. Docs: https://docs.sequenzy.com/api-reference/ab-tests/add-variant |
| Add Account Members | `addAccountMembers` | Add Account Members (attach subscribers to a B2B account). POST /api/v1/accounts/{externalId}/members. Docs: https://docs.sequenzy.com/api-reference/accounts/members |
| Add Outbound Webhook Signing Secret | `addOutboundWebhookSigningSecret` | Add a signing secret to an Outbound Webhook. POST /api/v1/webhooks/{webhookId}/secrets. SECURITY: the response contains the new signing secret in plaintext. |
| Add Sending Domain | `addSendingDomain` | Add a sending domain. POST /api/v1/websites. |
| Add Several Tags to Subscriber | `addSeveralTagsToSubscriber` | Add several tags to one subscriber. POST /api/v1/subscribers/tags/bulk. |
| Add Subscriber Note by External ID | `addSubscriberNoteByExternalId` | Add a note to a Subscriber identified by external id. POST /api/v1/subscribers/external/notes?externalId=... BLOCKED BY A FASTN ENGINE BUG: the engine strips the query string from POST requests (both the queryParams map and an inline ?query in the url), so externalId never reaches the host and it always answers 400 "externalId is required". The host does NOT read externalId from the JSON body. Unblocked once the engine sends query params on POST. |
| Add Subscribers to List | `addSubscribersToList` | Add Subscribers to a List. POST /api/v1/lists/{listId}/subscribers. WARNING: enrollInSequences true can start sending email. |
| Add Tag to Subscriber | `addTagToSubscriber` | Add one tag to a subscriber (creates the contact if new). POST /api/v1/subscribers/tags. WARNING: a tag_added sequence trigger can start sending email. |

<details>

<summary>See 309 more actions</summary>

* **Add Tags to Many Subscribers** `addTagsToManySubscribers`: Bulk add tags to subscribers. POST /api/v1/subscribers/bulk/tags/add. WARNING: a tag_added sequence trigger can start sending email.
* **Approve Migration Plan** `approveMigrationPlan`: Approve Migration Plan. POST /api/v1/migrations/{runId}/approve-plan.
* **Archive Sequence** `archiveSequence`: Archive Sequence. POST /api/v1/sequences/{sequenceId}/archive.
* **Attach Product Delivery File** `attachProductDeliveryFile`: Attach a digital delivery file to a Product by URL. PUT /api/v1/products/{productId}/delivery.
* **Cancel Campaign** `cancelCampaign`: Cancel Campaign (stop a scheduled or sending campaign). POST /api/v1/campaigns/{campaignId}/cancel. Docs: https://docs.sequenzy.com/api-reference/campaigns/cancel
* **Cancel Migration** `cancelMigration`: Cancel Migration run. POST /api/v1/migrations/{runId}/cancel.
* **Cancel Sequence Audience Enrollment** `cancelSequenceAudienceEnrollment`: Cancel a Sequence Audience Enrollment run. POST /api/v1/sequences/{sequenceId}/audience-enrollments/{runId}/cancel.
* **Cancel Sequence Enrollments** `cancelSequenceEnrollments`: Cancel Sequence Enrollments (supports dryRun). POST /api/v1/sequences/{sequenceId}/enrollments/cancel.
* **Cancel Subscriber Operation** `cancelSubscriberOperation`: Cancel a bulk Subscriber Operation. POST /api/v1/subscribers/operations/{id}/cancel.
* **Cancel Team Invitation** `cancelTeamInvitation`: Cancel a pending Team Invitation. DELETE /api/v1/team/invitations/{invitationId}.
* **Clear Saved AI Email Style** `clearSavedAiEmailStyle`: Clear Saved AI Email Style. DELETE /api/v1/email-ai-style. Requires expectedStyleId as an optimistic-concurrency guard.
* **Complete Image Upload** `completeImageUpload`: Complete Image Upload (register an uploaded object as media). POST /api/v1/media/complete-upload.
* **Configure Sequence Inbound Webhook** `configureSequenceInboundWebhook`: Configure a sequence's inbound-webhook endpoint and field mapping. PUT /api/v1/sequences/{sequenceId}/inbound-webhook.
* **Connect Integration** `connectIntegration`: Connect an API-key or webhook-secret Integration. POST /api/v1/integrations/connect. SECURITY: the body carries a third-party provider credential.
* **Connect Landing Page Domain** `connectLandingPageDomain`: Connect a workspace Landing Page Domain. POST /api/v1/landing-pages/domain.
* **Connect Migration Source** `connectMigrationSource`: Connect Migration Source platform. POST /api/v1/migrations/{runId}/connect-source. SECURITY: the body carries the source platform credential.
* **Create A/B Test** `createABTest`: Create A/B Test. POST /api/v1/ab-tests. Docs: https://docs.sequenzy.com/api-reference/ab-tests/create
* **Create Accounts From Organization ID** `createAccountsFromOrganizationId`: Create Accounts From Organization ID. POST /api/v1/account-suggestions/organization-ids. Docs: https://docs.sequenzy.com/api-reference/accounts/organization-ids-create
* **Create API Key** `createApiKey`: Create API Key. POST /api/v1/api-keys. SECURITY: the response contains the new key in plaintext (shown once). Do not log or persist this action's output. Docs: https://docs.sequenzy.com/api-reference/api-keys/create
* **Create Audience Sync** `createAudienceSync`: Create Audience Sync. POST /api/v1/audience-syncs. Docs: https://docs.sequenzy.com/api-reference/audience-syncs/create
* **Create Campaign** `createCampaign`: Create Campaign (draft). POST /api/v1/campaigns. Docs: https://docs.sequenzy.com/api-reference/campaigns/create
* **Create Campaign From Audience** `createCampaignFromAudience`: Create Campaign From Audience (build a draft campaign targeting a saved audience/group). POST /api/v1/campaigns/from-audience. Docs: https://docs.sequenzy.com/api-reference/campaigns/from-audience
* **Create Campaign Goal** `createCampaignGoal`: Create Campaign Goal. POST /api/v1/campaigns/{campaignId}/goals. Docs: https://docs.sequenzy.com/api-reference/campaigns/goals
* **Create Campaign Share Link** `createCampaignShareLink`: Create Campaign Share Link. POST /api/v1/campaigns/{campaignId}/share-link. SECURITY: produces a PUBLIC unauthenticated URL exposing the campaign content. Docs: https://docs.sequenzy.com/api-reference/campaigns/share-link-create
* **Create Company** `createCompany`: Create Company (new Sequenzy workspace). POST /api/v1/companies. WARNING: creates a billable workspace; there is no delete-company route in this API.
* **Create Email** `createEmail`: Create Email (standalone email object used by sequences and A/B tests). POST /api/v1/emails.
* **Create Email Component** `createEmailComponent`: Create Email Component. POST /api/v1/email-components.
* **Create Image Upload URL** `createImageUploadUrl`: Create a pre-signed Image Upload URL. POST /api/v1/media/upload-url.
* **Create Landing Page** `createLandingPage`: Create Landing Page (draft). POST /api/v1/landing-pages.
* **Create or Update Account** `createOrUpdateAccount`: Create or Update Account (upsert a B2B account by externalId). POST /api/v1/accounts. Docs: https://docs.sequenzy.com/api-reference/accounts/upsert
* **Create Outbound Webhook** `createOutboundWebhook`: Create an Outbound Webhook endpoint for campaign, email, SMS, subscriber and sequence lifecycle events. POST /api/v1/webhooks. SECURITY: the response contains the endpoint's signing secret.
* **Create Popup** `createPopup`: Create Popup. POST /api/v1/popups.
* **Create Product Delivery Upload URL** `createProductDeliveryUploadUrl`: Create a pre-signed upload URL for a digital product delivery file. POST /api/v1/products/delivery/upload-url.
* **Create Saved Form** `createSavedForm`: Create Saved Form. POST /api/v1/forms.
* **Create Segment** `createSegment`: Create Segment with a filter tree. POST /api/v1/segments.
* **Create Sequence** `createSequence`: Create Sequence (created inactive/draft). POST /api/v1/sequences. WARNING: activating a sequence later sends real email on a schedule.
* **Create Sequence Goal** `createSequenceGoal`: Create Sequence Goal. POST /api/v1/sequences/{sequenceId}/goals.
* **Create Subscriber** `createSubscriber`: Create Subscriber. POST /api/v1/subscribers. Creates or upserts a contact. Docs: https://docs.sequenzy.com/api-reference/subscribers/create
* **Create Subscriber Import** `createSubscriberImport`: Create a Subscriber Import job. POST /api/v1/subscribers/imports. WARNING: imported contacts can be enrolled in welcome sequences.
* **Create Subscriber List** `createSubscriberList`: Create Subscriber List. POST /api/v1/lists.
* **Create Tag** `createTag`: Create Tag. POST /api/v1/tags.
* **Create Template** `createTemplate`: Create an Email Template. POST /api/v1/templates.
* **Create Template Share Link** `createTemplateShareLink`: Create a Template's public share link. POST /api/v1/templates/{templateId}/share-link. SECURITY: produces a PUBLIC unauthenticated URL exposing the template.
* **Create Transactional Email** `createTransactionalEmail`: Create a Transactional Email template. POST /api/v1/transactional.
* **Create Web Tracking Key** `createWebTrackingKey`: Create a Web Tracking Key. POST /api/v1/web-tracking-keys. SECURITY: the response contains the new key.
* **Delete A/B Test** `deleteABTest`: Delete A/B Test. DELETE /api/v1/ab-tests/{abTestId}. Docs: https://docs.sequenzy.com/api-reference/ab-tests/delete
* **Delete A/B Test Variant** `deleteABTestVariant`: Delete A/B Test Variant. DELETE /api/v1/ab-tests/{abTestId}/variants/{variantId}. Docs: https://docs.sequenzy.com/api-reference/ab-tests/delete-variant
* **Delete Account** `deleteAccount`: Delete Account and its memberships. DELETE /api/v1/accounts/{externalId}. Docs: https://docs.sequenzy.com/api-reference/accounts/delete
* **Delete Audience Sync** `deleteAudienceSync`: Delete Audience Sync. DELETE /api/v1/audience-syncs/{syncId}. Docs: https://docs.sequenzy.com/api-reference/audience-syncs/delete
* **Delete Campaign** `deleteCampaign`: Delete Campaign. DELETE /api/v1/campaigns/{campaignId}. Docs: https://docs.sequenzy.com/api-reference/campaigns/delete
* **Delete Campaign Goal** `deleteCampaignGoal`: Delete Campaign Goal. DELETE /api/v1/campaigns/{campaignId}/goals/{goalId}. Docs: https://docs.sequenzy.com/api-reference/campaigns/goals
* **Delete Email Component** `deleteEmailComponent`: Delete Email Component. DELETE /api/v1/email-components/{componentId}.
* **Delete Landing Page** `deleteLandingPage`: Delete Landing Page. DELETE /api/v1/landing-pages/{landingPageId}.
* **Delete Outbound Webhook** `deleteOutboundWebhook`: Delete an Outbound Webhook endpoint and its delivery history. DELETE /api/v1/webhooks/{webhookId}.
* **Delete Popup** `deletePopup`: Delete Popup. DELETE /api/v1/popups/{popupId}.
* **Delete Product** `deleteProduct`: Delete Product. DELETE /api/v1/products/{productId}.
* **Delete Segment** `deleteSegment`: Delete Segment. DELETE /api/v1/segments/{segmentId}.
* **Delete Sender Profile** `deleteSenderProfile`: Delete Sender Profile. DELETE /api/v1/sender-profiles/{id}.
* **Delete Sequence** `deleteSequence`: Delete Sequence. DELETE /api/v1/sequences/{sequenceId}.
* **Delete Sequence Goal** `deleteSequenceGoal`: Delete Sequence Goal. DELETE /api/v1/sequences/{sequenceId}/goals/{goalId}.
* **Delete Subscriber** `deleteSubscriber`: Delete a Subscriber by email. DELETE /api/v1/subscribers/{email}.
* **Delete Subscriber by External ID** `deleteSubscriberByExternalId`: Delete a Subscriber by your external id. DELETE /api/v1/subscribers/external. Undocumented route proven live (400 "externalId is required").
* **Delete Subscriber List** `deleteSubscriberList`: Delete Subscriber List. DELETE /api/v1/lists/{listId}.
* **Delete Tag** `deleteTag`: Delete Tag. DELETE /api/v1/tags/{tagId}.
* **Delete Template** `deleteTemplate`: Delete an Email Template. DELETE /api/v1/templates/{templateId}.
* **Delete Transactional Email** `deleteTransactionalEmail`: Delete a Transactional Email template. DELETE /api/v1/transactional/{idOrSlug}.
* **Delete Web Tracking Key** `deleteWebTrackingKey`: Delete a Web Tracking Key. DELETE /api/v1/web-tracking-keys/{id}.
* **Detect Organization IDs** `detectOrganizationIds`: Detect Organization IDs. GET /api/v1/account-suggestions/organization-ids. Docs: https://docs.sequenzy.com/api-reference/accounts/organization-ids-detect
* **Disable Sequence** `disableSequence`: Disable (deactivate) a Sequence so it stops sending. POST /api/v1/sequences/{sequenceId}/disable.
* **Disconnect Integration** `disconnectIntegration`: Disconnect Integration and remove its managed webhook. POST /api/v1/integrations/{id}/disconnect.
* **Discover Migration Source** `discoverMigrationSource`: Discover resources on the Migration Source. POST /api/v1/migrations/{runId}/discover.
* **Duplicate Campaign** `duplicateCampaign`: Duplicate Campaign into a new draft. POST /api/v1/campaigns/{campaignId}/duplicate. Docs: https://docs.sequenzy.com/api-reference/campaigns/duplicate
* **Duplicate Landing Page** `duplicateLandingPage`: Duplicate Landing Page into a new draft. POST /api/v1/landing-pages/{landingPageId}/duplicate.
* **Duplicate Popup** `duplicatePopup`: Duplicate Popup. POST /api/v1/popups/{popupId}/duplicate.
* **Duplicate Sequence** `duplicateSequence`: Duplicate Sequence into an independent draft. POST /api/v1/sequences/{sequenceId}/duplicate.
* **Enable Sequence** `enableSequence`: Enable (activate) a Sequence. POST /api/v1/sequences/{sequenceId}/enable. WARNING: an active sequence dispatches real email to enrolled subscribers on a schedule.
* **Enroll Audience in Sequence** `enrollAudienceInSequence`: Enroll a whole audience (segment or list) in a Sequence. POST /api/v1/sequences/{sequenceId}/enroll-audience. WARNING: can start mass email delivery.
* **Enroll Subscribers in Sequence** `enrollSubscribersInSequence`: Enroll Subscribers in a Sequence. POST /api/v1/sequences/{sequenceId}/enroll. WARNING: on an active sequence this starts real email delivery to those addresses.
* **Estimate Sequence Audience Enrollment** `estimateSequenceAudienceEnrollment`: Estimate how many subscribers an audience enrollment would add. POST /api/v1/sequences/{sequenceId}/enroll-audience/estimate. Read-only preview.
* **Generate Email with AI** `generateEmailWithAi`: Generate Email with AI. POST /api/v1/generate/email. Consumes AI generation quota.
* **Generate Sequence with AI** `generateSequenceWithAi`: Generate Sequence with AI (deprecated by the vendor in favour of Create Sequence). POST /api/v1/generate/sequence. Consumes AI generation quota.
* **Generate SMS Messages with AI** `generateSmsMessagesWithAi`: Generate SMS Messages with AI. POST /api/v1/generate/sms. Generates copy only, sends nothing.
* **Generate Subject Lines with AI** `generateSubjectLinesWithAi`: Generate Subject Lines with AI. POST /api/v1/generate/subjects.
* **Get A/B Test** `getABTest`: Get A/B Test. GET /api/v1/ab-tests/{abTestId}. Docs: https://docs.sequenzy.com/api-reference/ab-tests/get
* **Get A/B Test Stats** `getABTestStats`: Get A/B Test Stats. GET /api/v1/ab-tests/{abTestId}/stats. Docs: https://docs.sequenzy.com/api-reference/ab-tests/stats
* **Get Account** `getAccount`: Get Account. GET /api/v1/account. Returns the workspaces (companies) the key can reach, the current company id and the active API key's permission preset. Docs: https://docs.sequenzy.com/api-reference/account/get
* **Get Account by External ID** `getAccountByExternalId`: Get Account by External ID. GET /api/v1/accounts/{externalId}. Docs: https://docs.sequenzy.com/api-reference/accounts/get
* **Get Account Metrics** `getAccountMetrics`: Get Account Metrics (sends, opens, clicks, bounces) for a period. GET /api/v1/metrics.
* **Get Attio List Mapping** `getAttioListMapping`: Get Attio List Mapping for an integration. GET /api/v1/integrations/{id}/attio.
* **Get Campaign** `getCampaign`: Get Campaign. GET /api/v1/campaigns/{campaignId}. Docs: https://docs.sequenzy.com/api-reference/campaigns/get
* **Get Campaign Audience** `getCampaignAudience`: Get Campaign Audience (resolved recipient set). GET /api/v1/campaigns/{campaignId}/audience. Docs: https://docs.sequenzy.com/api-reference/campaigns/audience
* **Get Campaign Metrics** `getCampaignMetrics`: Get Campaign Metrics. GET /api/v1/metrics/campaigns/{campaignId}.
* **Get Campaign Stats** `getCampaignStats`: Get Campaign Stats. GET /api/v1/campaigns/{campaignId}/stats. Undocumented route proven live (404 "Campaign not found").
* **Get Company** `getCompany`: Get Company settings and branding. GET /api/v1/companies/{companyId}.
* **Get Conversation** `getConversation`: Get Conversation with its messages. GET /api/v1/conversations/{conversationId}. Returns subscriber PII.
* **Get Current API Key Identity** `getCurrentApiKeyIdentity`: Get the identity and permissions of the calling API key. GET /api/v1/subscribers/me.
* **Get Default Email Component** `getDefaultEmailComponent`: Get Default Email Component for a slot. GET /api/v1/email-components/defaults/{slot}.
* **Get Email Block Type** `getEmailBlockType`: Get Email Block Type schema (required/optional fields). GET /api/v1/email-blocks/{type}.
* **Get Email Component** `getEmailComponent`: Get Email Component. GET /api/v1/email-components/{componentId}.
* **Get Email Design System** `getEmailDesignSystem`: Get Email Design System (composition spine and design code). GET /api/v1/email-design-system.
* **Get Email Send** `getEmailSend`: Get Email Send record. GET /api/v1/email-sends/{emailSendId}. Returns recipient PII.
* **Get Event Schemas** `getEventSchemas`: Get Event Schemas that Sequenzy can receive. GET /api/v1/events/schemas.
* **Get Integration** `getIntegration`: Get Integration detail. GET /api/v1/integrations/{id}.
* **Get Integration Guide** `getIntegrationGuide`: Get Integration Guide for a framework and use case. POST /api/v1/integration-guide.
* **Get Landing Page** `getLandingPage`: Get Landing Page with its content document. GET /api/v1/landing-pages/{landingPageId}.
* **Get Landing Page Custom Domain** `getLandingPageCustomDomain`: Get a Landing Page's dedicated custom domain. GET /api/v1/landing-pages/{landingPageId}/domain.
* **Get Landing Page Domain** `getLandingPageDomain`: Get workspace-level Landing Page Domain. GET /api/v1/landing-pages/domain.
* **Get Landing Page Stats** `getLandingPageStats`: Get Landing Page Stats. GET /api/v1/landing-pages/{landingPageId}/stats.
* **Get Live Sequence Test** `getLiveSequenceTest`: Get a Live Sequence Test run. GET /api/v1/sequences/{sequenceId}/test-runs/{runId}.
* **Get Migration Agent Package** `getMigrationAgentPackage`: Get Migration Agent Package. GET /api/v1/migrations/{runId}/agent-package. SECURITY: may include provider credentials for the source platform.
* **Get Migration Run** `getMigrationRun`: Get Migration Run status. GET /api/v1/migrations/{runId}.
* **Get Notification Preferences** `getNotificationPreferences`: Get account notification preferences. GET /api/v1/notification-preferences.
* **Get Organization ID Job** `getOrganizationIdJob`: Get Organization ID Job. GET /api/v1/account-suggestions/organization-ids/jobs/{jobId}. Docs: https://docs.sequenzy.com/api-reference/accounts/organization-ids-job
* **Get Popup** `getPopup`: Get Popup. GET /api/v1/popups/{popupId}.
* **Get Popup Embed** `getPopupEmbed`: Get Popup Embed snippet. GET /api/v1/popups/embed/{popupId}.
* **Get Popup Widget Runtime** `getPopupWidgetRuntime`: Get the popup widget JavaScript runtime. GET /api/v1/widgets/popup.js. Returns JS, not JSON.
* **Get Preferences Widget Token** `getPreferencesWidgetToken`: Mint a token for the subscriber preferences widget. POST /api/v1/widgets/preferences/token. SECURITY: the response contains a token that grants access to that subscriber's preferences.
* **Get Product** `getProduct`: Get Product. GET /api/v1/products/{productId}.
* **Get Received Event Sample** `getReceivedEventSample`: Get Received Event Sample (latest inbound event payload seen). GET /api/v1/events/sample.
* **Get Recipient Metrics** `getRecipientMetrics`: Get Recipient Metrics (per-contact engagement). GET /api/v1/metrics/recipients. Returns recipient PII.
* **Get Recipient Suppression** `getRecipientSuppression`: Get a recipient's suppression record. GET /api/v1/suppressions/{email}.
* **Get Saved AI Email Style** `getSavedAiEmailStyle`: Get Saved AI Email Style. GET /api/v1/email-ai-style.
* **Get Saved Form Embed** `getSavedFormEmbed`: Get Saved Form Embed snippet. GET /api/v1/forms/embed/{formId}.
* **Get Saved Form Embed Script** `getSavedFormEmbedScript`: Get Saved Form Embed Script (JavaScript). GET /api/v1/forms/{formId}/embed.js. Returns JS, not JSON.
* **Get Segment Count** `getSegmentCount`: Get Segment member count. GET /api/v1/segments/{segmentId}/count.
* **Get Sending Domain** `getSendingDomain`: Get a sending domain and its DNS records. GET /api/v1/websites/{domain}.
* **Get Sending Status** `getSendingStatus`: Get workspace Sending Status (whether sending is paused). GET /api/v1/sending-status.
* **Get Sequence** `getSequence`: Get Sequence with its graph. GET /api/v1/sequences/{sequenceId}.
* **Get Sequence Audience Enrollment Run** `getSequenceAudienceEnrollmentRun`: Get one Sequence Audience Enrollment run. GET /api/v1/sequences/{sequenceId}/audience-enrollments/{runId}. Undocumented route proven live (404 "Audience enrollment not found").
* **Get Sequence Enrollment** `getSequenceEnrollment`: Get one Sequence Enrollment. GET /api/v1/sequences/{sequenceId}/enrollments/{enrollmentId}. Returns subscriber PII.
* **Get Sequence Inbound Webhook** `getSequenceInboundWebhook`: Get a sequence's inbound-webhook URL, mapping and sample payload. GET /api/v1/sequences/{sequenceId}/inbound-webhook. SECURITY: the response contains the secret webhook URL.
* **Get Sequence Metrics** `getSequenceMetrics`: Get Sequence Metrics. GET /api/v1/metrics/sequences/{sequenceId}.
* **Get Sequence Realign Job** `getSequenceRealignJob`: Get a Sequence sending-window realign job. GET /api/v1/sequences/{sequenceId}/enrollments/realign-sending-window/jobs/{jobId}. Undocumented route proven live.
* **Get Sequence Stats** `getSequenceStats`: Get Sequence Stats. GET /api/v1/sequences/{sequenceId}/stats.
* **Get Shopify Automation Settings** `getShopifyAutomationSettings`: Get Shopify automation settings. GET /api/v1/shopify/automation-settings.
* **Get SMS Settings** `getSmsSettings`: Get SMS Settings. GET /api/v1/sms/settings.
* **Get SMS Usage** `getSmsUsage`: Get SMS Usage and quota. GET /api/v1/sms/usage.
* **Get Storefront Pixel** `getStorefrontPixel`: Get Storefront Pixel status for an integration. GET /api/v1/integrations/{id}/pixel.
* **Get Subscriber** `getSubscriber`: Get a Subscriber by email. GET /api/v1/subscribers/{email}. Returns subscriber PII.
* **Get Subscriber by External ID** `getSubscriberByExternalId`: Get a Subscriber by your external id. GET /api/v1/subscribers/external. Returns subscriber PII.
* **Get Subscriber Import** `getSubscriberImport`: Get a Subscriber Import job. GET /api/v1/subscribers/imports/{importId}.
* **Get Subscriber Operation** `getSubscriberOperation`: Get a bulk Subscriber Operation. GET /api/v1/subscribers/operations/{id}.
* **Get Sync Rules** `getSyncRules`: Get integration sync rules. GET /api/v1/sync-rules.
* **Get Template** `getTemplate`: Get an Email Template. GET /api/v1/templates/{templateId}.
* **Get Tracking Settings** `getTrackingSettings`: Get open/click tracking settings. GET /api/v1/tracking-settings.
* **Get Transactional Email** `getTransactionalEmail`: Get a Transactional Email template. GET /api/v1/transactional/{idOrSlug}.
* **Get Transactional Email Metrics** `getTransactionalEmailMetrics`: Get Transactional Email Metrics. GET /api/v1/metrics/transactional/{idOrSlug}.
* **Get Transactional Email Stats by Slug** `getTransactionalEmailStatsBySlug`: Get stats for one Transactional Email template. GET /api/v1/transactional/{idOrSlug}/stats. Undocumented route proven live.
* **Get Web Tracking Key** `getWebTrackingKey`: Get a Web Tracking Key. GET /api/v1/web-tracking-keys/{id}.
* **Get Workspace Stats** `getWorkspaceStats`: Get Workspace Stats summary. GET /api/v1/stats. Undocumented route proven live (200).
* **Import Events for Many Subscribers** `importEventsForManySubscribers`: Import historical events for many subscribers. POST /api/v1/subscribers/events/imports.
* **Invite Team Member** `inviteTeamMember`: Invite a Team Member. POST /api/v1/team/invitations. WARNING: this SENDS a real invitation email to the address given.
* **List A/B Tests** `listABTests`: List A/B Tests. GET /api/v1/ab-tests. Docs: https://docs.sequenzy.com/api-reference/ab-tests/list
* **List Account Events** `listAccountEvents`: List Account Events. GET /api/v1/accounts/{externalId}/events. Docs: https://docs.sequenzy.com/api-reference/accounts/events-list
* **List Account Members** `listAccountMembers`: List Account Members. GET /api/v1/accounts/{externalId}/members. Undocumented route proven live (404 "Account not found"). Returns subscriber PII.
* **List Account Suggestions** `listAccountSuggestions`: List Account Suggestions. GET /api/v1/account-suggestions. Docs: https://docs.sequenzy.com/api-reference/accounts/suggestions-list
* **List Accounts** `listAccounts`: List Accounts. GET /api/v1/accounts. Docs: https://docs.sequenzy.com/api-reference/accounts/list
* **List Ad Accounts** `listAdAccounts`: List Ad Accounts available for audience syncs. GET /api/v1/ad-accounts. Docs: https://docs.sequenzy.com/api-reference/audience-syncs/ad-accounts
* **List API Keys** `listApiKeys`: List API Keys for the workspace. GET /api/v1/api-keys. SECURITY: returns key metadata and prefixes - treat its output as sensitive. Docs: https://docs.sequenzy.com/api-reference/api-keys/list
* **List Audience Syncs** `listAudienceSyncs`: List Audience Syncs (segment to ad-platform audience syncs). GET /api/v1/audience-syncs. Docs: https://docs.sequenzy.com/api-reference/audience-syncs/list
* **List Campaign Events** `listCampaignEvents`: List Campaign Events (delivery, open, click). GET /api/v1/metrics/campaigns/{campaignId}/events. Returns recipient PII.
* **List Campaign Goals** `listCampaignGoals`: List Campaign Goals (persisted conversion goals). GET /api/v1/campaigns/{campaignId}/goals. Docs: https://docs.sequenzy.com/api-reference/campaigns/goals
* **List Campaign Poll Responses** `listCampaignPollResponses`: List Campaign Poll Responses. GET /api/v1/metrics/campaigns/{campaignId}/poll-responses. Returns recipient PII.
* **List Campaigns** `listCampaigns`: List Campaigns. GET /api/v1/campaigns. Docs: https://docs.sequenzy.com/api-reference/campaigns/list
* **List Capture Submissions** `listCaptureSubmissions`: List form/popup/landing-page capture submissions. GET /api/v1/submissions/{sourceType}/{sourceId}. Returns subscriber PII.
* **List Companies** `listCompanies`: List Companies (workspaces the key can reach). GET /api/v1/companies.
* **List Conversations** `listConversations`: List Conversations (inbound reply inbox). GET /api/v1/conversations. Returns subscriber PII.
* **List Email Block Types** `listEmailBlockTypes`: List Email Block Types available for campaign and template content. GET /api/v1/email-blocks.
* **List Email Components** `listEmailComponents`: List Email Components (reusable header/footer blocks). GET /api/v1/email-components.
* **List Integration Activity** `listIntegrationActivity`: List Integration Activity (recent webhook and sync events). GET /api/v1/integrations/activity.
* **List Integration Catalog** `listIntegrationCatalog`: List Integration Catalog (providers and their capabilities). GET /api/v1/integrations/catalog.
* **List Integrations** `listIntegrations`: List Integrations connected to this workspace. GET /api/v1/integrations.
* **List Landing Pages** `listLandingPages`: List Landing Pages. GET /api/v1/landing-pages.
* **List Outbound Webhook Deliveries** `listOutboundWebhookDeliveries`: List an Outbound Webhook's deliveries. GET /api/v1/webhooks/{webhookId}/deliveries.
* **List Outbound Webhook Delivery Attempts** `listOutboundWebhookDeliveryAttempts`: List attempts for one Outbound Webhook delivery. GET /api/v1/webhooks/{webhookId}/deliveries/{deliveryId}/attempts.
* **List Outbound Webhooks** `listOutboundWebhooks`: List Outbound Webhook endpoints. GET /api/v1/webhooks.
* **List Per-Email Metrics** `listPerEmailMetrics`: List Per-Email Metrics across campaigns and sequences. GET /api/v1/metrics/emails.
* **List Poll Responses by Campaign** `listPollResponsesByCampaign`: List Poll Responses by Campaign. GET /api/v1/campaigns/{campaignId}/poll-responses. Undocumented route proven live (404 "Campaign not found"). Returns subscriber PII.
* **List Popups** `listPopups`: List Popups. GET /api/v1/popups.
* **List Products** `listProducts`: List Products. GET /api/v1/products.
* **List Saved Forms** `listSavedForms`: List Saved Forms. GET /api/v1/forms.
* **List Segments** `listSegments`: List Segments. GET /api/v1/segments.
* **List Sender Profiles** `listSenderProfiles`: List Sender Profiles. GET /api/v1/sender-profiles.
* **List Sending Domains** `listSendingDomains`: List sending domains (websites). GET /api/v1/websites.
* **List Sent Emails** `listSentEmails`: List Sent Emails (delivery log). GET /api/v1/email-sends. Returns recipient PII.
* **List Sequence Audience Enrollments** `listSequenceAudienceEnrollments`: List Sequence Audience Enrollment runs. GET /api/v1/sequences/{sequenceId}/audience-enrollments.
* **List Sequence Enrollments** `listSequenceEnrollments`: List Sequence Enrollments. GET /api/v1/sequences/{sequenceId}/enrollments. Returns subscriber PII.
* **List Sequence Events** `listSequenceEvents`: List Sequence Events. GET /api/v1/metrics/sequences/{sequenceId}/events. Returns recipient PII.
* **List Sequence Goals** `listSequenceGoals`: List Sequence Goals. GET /api/v1/sequences/{sequenceId}/goals.
* **List Sequences** `listSequences`: List Sequences. GET /api/v1/sequences.
* **List Subscriber Lists** `listSubscriberLists`: List Subscriber Lists. GET /api/v1/lists.
* **List Subscriber Notes** `listSubscriberNotes`: List notes on a Subscriber. GET /api/v1/subscribers/{email}/notes. Returns subscriber PII.
* **List Subscribers** `listSubscribers`: List Subscribers. GET /api/v1/subscribers with pagination and optional filtering by status, list, attribute or opt-out date. Docs: https://docs.sequenzy.com/api-reference/subscribers/list
* **List Suppressed Recipients** `listSuppressedRecipients`: List suppressed recipients (bounces, complaints). GET /api/v1/suppressions. Returns recipient PII.
* **List Tags** `listTags`: List Tags. GET /api/v1/tags.
* **List Team Members** `listTeamMembers`: List Team Members. GET /api/v1/team. Returns team member PII.
* **List Templates** `listTemplates`: List Email Templates. GET /api/v1/templates.
* **List Transactional Emails** `listTransactionalEmails`: List Transactional Email templates. GET /api/v1/transactional.
* **List Web Tracking Keys** `listWebTrackingKeys`: List Web Tracking Keys. GET /api/v1/web-tracking-keys. SECURITY: returns public tracking keys.
* **Mark Conversation Read** `markConversationRead`: Mark Conversation Read. POST /api/v1/conversations/{conversationId}/read.
* **Mint Web Tracking Identity** `mintWebTrackingIdentity`: Mint a signed web-tracking identity for a visitor. POST /api/v1/web-tracking-identities. SECURITY: returns a signed identity token.
* **Move Sequence Enrollments** `moveSequenceEnrollments`: Move Sequence Enrollments to another node (supports dryRun). POST /api/v1/sequences/{sequenceId}/enrollments/move.
* **Pause Campaign** `pauseCampaign`: Pause Campaign sending. POST /api/v1/campaigns/{campaignId}/pause. Docs: https://docs.sequenzy.com/api-reference/campaigns/pause
* **Pause Sequence Enrollments** `pauseSequenceEnrollments`: Pause all enrollments in a Sequence. POST /api/v1/sequences/{sequenceId}/pause-enrollments.
* **Preview Accounts From Organization ID** `previewAccountsFromOrganizationId`: Preview Accounts From Organization ID. GET /api/v1/account-suggestions/organization-ids/preview. Docs: https://docs.sequenzy.com/api-reference/accounts/organization-ids-preview
* **Preview Campaign Personalized Lists** `previewCampaignComputedData`: Preview Campaign Personalized Lists (computed data for one subscriber). POST /api/v1/campaigns/{campaignId}/preview-computed-data. Docs: https://docs.sequenzy.com/api-reference/campaigns/preview-computed-data
* **Preview Default Email Component** `previewDefaultEmailComponent`: Preview Default Email Component (e.g. footer) rendering. POST /api/v1/email-components/defaults/{slot}/preview.
* **Preview Line Item Block** `previewLineItemBlock`: Preview Line Item (cart) Block rendering. POST /api/v1/email-blocks/line-items/assist.
* **Publish Landing Page** `publishLandingPage`: Publish Landing Page. POST /api/v1/landing-pages/{landingPageId}/publish. SECURITY: makes the page publicly reachable without authentication.
* **Push Order** `pushOrder`: Push an ecommerce Order into Sequenzy. POST /api/v1/orders. WARNING: can trigger post-purchase sequences that send email.
* **Realign Sequence Enrollments** `realignSequenceEnrollments`: Realign Sequence Enrollments to the sending window (supports dryRun). POST /api/v1/sequences/{sequenceId}/enrollments/realign-sending-window.
* **Register Back-in-Stock Request** `registerBackInStockRequest`: Register Back-in-Stock Request for a product/variant. POST /api/v1/back-in-stock. Docs: https://docs.sequenzy.com/api-reference/products/back-in-stock
* **Remove Account Members** `removeAccountMembers`: Remove Account Members. DELETE /api/v1/accounts/{externalId}/members with a body naming the members to detach. Undocumented route proven live (422 validation "Expected object").
* **Remove Landing Page Custom Domain** `removeLandingPageCustomDomain`: Remove a Landing Page's dedicated custom domain. DELETE /api/v1/landing-pages/{landingPageId}/domain.
* **Remove Outbound Webhook Signing Secret** `removeOutboundWebhookSigningSecret`: Remove a signing secret from an Outbound Webhook. DELETE /api/v1/webhooks/{webhookId}/secrets/{secretId}.
* **Remove Product Delivery File** `removeProductDeliveryFile`: Remove a Product's digital delivery file. DELETE /api/v1/products/{productId}/delivery.
* **Remove Recipient Suppression** `removeRecipientSuppression`: Remove a recipient from the suppression list. DELETE /api/v1/suppressions/{email}. WARNING: makes a previously blocked address eligible for delivery again.
* **Remove SMS Number** `removeSmsNumber`: Remove an SMS sending number. DELETE /api/v1/sms/numbers/{numberId}.
* **Remove Subscribers from List** `removeSubscribersFromList`: Remove Subscribers from a List. POST /api/v1/lists/{listId}/subscribers/remove.
* **Remove Tag from Subscriber** `removeTagFromSubscriber`: Remove one tag from a subscriber. POST /api/v1/subscribers/tags/remove.
* **Remove Tags from Many Subscribers** `removeTagsFromManySubscribers`: Bulk remove tags from subscribers. POST /api/v1/subscribers/bulk/tags/remove.
* **Rename Reply-To Profile** `renameReplyToProfile`: Rename a Reply-To Profile. PATCH /api/v1/reply-profiles/{id}.
* **Rename Sender Profile** `renameSenderProfile`: Rename Sender Profile. PATCH /api/v1/sender-profiles/{id}.
* **Render Campaign HTML** `renderCampaignHtml`: Render Campaign HTML for a given subscriber context (no email is sent). POST /api/v1/campaigns/{campaignId}/render. Docs: https://docs.sequenzy.com/api-reference/campaigns/render
* **Render Landing Page Preview** `renderLandingPagePreview`: Render Landing Page Preview HTML. POST /api/v1/landing-pages/{landingPageId}/render.
* **Render Sequence Step HTML** `renderSequenceStepHtml`: Render a Sequence step's HTML (no email sent). POST /api/v1/sequences/{sequenceId}/nodes/{nodeId}/render.
* **Render Template HTML** `renderTemplateHtml`: Render a Template to HTML for a subscriber context (no email sent). POST /api/v1/templates/{templateId}/render.
* **Replay Outbound Webhook Delivery** `replayOutboundWebhookDelivery`: Replay one Outbound Webhook delivery. POST /api/v1/webhooks/{webhookId}/deliveries/{deliveryId}/replay.
* **Reply to Conversation** `replyToConversation`: Reply to Conversation. POST /api/v1/conversations/{conversationId}/messages. WARNING: this SENDS a real email to the subscriber who replied.
* **Request API Key Handoff** `requestApiKeyHandoff`: Request API Key Handoff. POST /api/v1/api-key-handoff. SECURITY: the response contains a NEWLY MINTED live Sequenzy API key in plaintext. Any consumer of this action receives a credential - do not log or persist its output. Docs: https://docs.sequenzy.com/api-reference/api-keys/handoff
* **Resend Campaign to Non-Openers** `resendCampaignToNonOpeners`: Resend Campaign to Non-Openers. POST /api/v1/campaigns/{campaignId}/resend-to-non-openers. WARNING: this SENDS real email to real recipients and consumes sending quota. Docs: https://docs.sequenzy.com/api-reference/campaigns/resend-to-non-openers
* **Restart A/B Test** `restartABTest`: Restart A/B Test. POST /api/v1/ab-tests/{abTestId}/restart. Docs: https://docs.sequenzy.com/api-reference/ab-tests/restart
* **Resume Campaign** `resumeCampaign`: Resume Campaign sending. POST /api/v1/campaigns/{campaignId}/resume. WARNING: resuming restarts real delivery to recipients. Docs: https://docs.sequenzy.com/api-reference/campaigns/resume
* **Resume Sequence Enrollments** `resumeSequenceEnrollments`: Resume paused enrollments in a Sequence. POST /api/v1/sequences/{sequenceId}/resume-enrollments. WARNING: resumes scheduled email delivery.
* **Resume Workspace Sending** `resumeWorkspaceSending`: Resume Workspace Sending after a deliverability pause. POST /api/v1/sending-status/resume. WARNING: this lifts a sending block and lets queued email go out.
* **Revoke API Key** `revokeApiKey`: Revoke API Key. DELETE /api/v1/api-keys/{apiKeyId}. WARNING: revoking the key your own connection uses breaks this connector. Docs: https://docs.sequenzy.com/api-reference/api-keys/revoke
* **Revoke Campaign Share Link** `revokeCampaignShareLink`: Revoke Campaign Share Link. DELETE /api/v1/campaigns/{campaignId}/share-link. Docs: https://docs.sequenzy.com/api-reference/campaigns/share-link-revoke
* **Revoke Template Share Link** `revokeTemplateShareLink`: Revoke a Template's public share link. DELETE /api/v1/templates/{templateId}/share-link.
* **Rotate Sequence Inbound Webhook Secret** `rotateSequenceInboundWebhookSecret`: Rotate a sequence's inbound-webhook secret. POST /api/v1/sequences/{sequenceId}/inbound-webhook/rotate-secret. SECURITY: returns a new secret URL and invalidates the old one.
* **Run Audience Sync Now** `runAudienceSyncNow`: Run Audience Sync Now (push the segment to the ad platform immediately). POST /api/v1/audience-syncs/{syncId}/sync. Docs: https://docs.sequenzy.com/api-reference/audience-syncs/sync
* **Save AI Email Style** `saveAiEmailStyle`: Save AI Email Style from an existing email. PUT /api/v1/email-ai-style.
* **Schedule Campaign** `scheduleCampaign`: Schedule Campaign. POST /api/v1/campaigns/{campaignId}/schedule. WARNING: this queues a real send at scheduledAt. Docs: https://docs.sequenzy.com/api-reference/campaigns/schedule
* **Select A/B Test Winner** `selectABTestWinner`: Select A/B Test Winner. POST /api/v1/ab-tests/{abTestId}/select-winner. Promotes a variant; on a live campaign/sequence this affects what recipients receive. Docs: https://docs.sequenzy.com/api-reference/ab-tests/select-winner
* **Send Campaign Test Email** `sendCampaignTestEmail`: Send Campaign Test Email. POST /api/v1/campaigns/{campaignId}/test. WARNING: this SENDS a real email to the address in "to" and consumes sending quota. Docs: https://docs.sequenzy.com/api-reference/campaigns/send-test
* **Send Outbound Webhook Test Event** `sendOutboundWebhookTestEvent`: Send a test event to an Outbound Webhook endpoint. POST /api/v1/webhooks/{webhookId}/test. Delivers only to your own HTTPS endpoint; sends no email.
* **Send Sequence Step Test Email** `sendSequenceStepTestEmail`: Send a test of one Sequence step. POST /api/v1/sequences/{sequenceId}/nodes/{nodeId}/test. WARNING: this SENDS real email to the given recipients.
* **Send Test SMS** `sendTestSms`: Send a Test SMS. POST /api/v1/sms/test. WARNING: sends a real SMS to a real phone number and costs money.
* **Send Transactional Email** `sendTransactionalEmail`: Send a Transactional Email. POST /api/v1/transactional/send. WARNING: this SENDS a real email to the address in "to" and consumes sending quota.
* **Set Default Email Component** `setDefaultEmailComponent`: Set Default Email Component for a slot. PUT /api/v1/email-components/defaults/{slot}.
* **Set Landing Page Custom Domain** `setLandingPageCustomDomain`: Set a Landing Page's dedicated custom domain. POST /api/v1/landing-pages/{landingPageId}/domain.
* **Set Template Localization** `setTemplateLocalization`: Set one locale's content on a Template. PUT /api/v1/templates/{templateId}/localizations/{locale}.
* **Simulate Sequence for Subscriber** `simulateSequenceForSubscriber`: Simulate how a Sequence would run for one subscriber (no email sent). GET /api/v1/sequences/{sequenceId}/simulate.
* **Start Live Sequence Test** `startLiveSequenceTest`: Start a Live Sequence Test run. POST /api/v1/sequences/{sequenceId}/test-runs. WARNING: a live test dispatches real email to the test recipients.
* **Start Migration** `startMigration`: Start Migration run. POST /api/v1/migrations/{runId}/start. WARNING: imports subscribers and can activate automations that send email.
* **Start Subscriber Operation** `startSubscriberOperation`: Start a bulk Subscriber Operation. POST /api/v1/subscribers/operations. "operation" is required and must be one of the vendor's operation kinds (e.g. add_tags). WARNING: operates on many real contacts. Note: there is no GET /api/v1/subscribers/operations list route - that path is swallowed by GET /api/v1/subscribers/{email}.
* **Submit Product Feedback** `submitProductFeedback`: Submit Product Feedback to Sequenzy. POST /api/v1/feedback.
* **Submit Saved Form** `submitSavedForm`: Submit Saved Form (create a subscriber from a saved form). POST /api/v1/forms/{formId}. May trigger a welcome sequence.
* **Submit Saved Popup** `submitSavedPopup`: Submit Saved Popup (create a subscriber from a popup submission). POST /api/v1/forms/popups/{popupId}. May trigger a welcome sequence.
* **Submit Signup Form by Company** `submitSignupFormByCompany`: Submit Signup Form by Company id. POST /api/v1/forms/{companyId}. Same wire route as Submit Saved Form; the path segment is a company id here. May trigger a welcome sequence.
* **Subscribe to WooCommerce Back-in-Stock** `subscribeWooCommerceBackInStock`: Subscribe to WooCommerce Back-in-Stock alerts. POST /api/woocommerce/back-in-stock/subscribe (note: NOT under /api/v1). Docs: https://docs.sequenzy.com/api-reference/woocommerce/back-in-stock-subscribe
* **Sync Integration Now** `syncIntegrationNow`: Sync Integration Now (manual backfill). POST /api/v1/integrations/{id}/sync. May import subscribers and start welcome sequences.
* **Sync Products from Provider** `syncProductsFromProvider`: Sync Products from a connected provider (e.g. Stripe). POST /api/v1/products/sync.
* **Sync Template Localizations** `syncTemplateLocalizations`: Sync a Template's localizations. POST /api/v1/templates/{templateId}/localizations/sync.
* **Track Checkout Started** `trackCheckoutStarted`: Track Checkout Started (abandoned-cart signal). POST /api/v1/checkouts. WARNING: can trigger an abandoned-cart sequence that emails the customer.
* **Trigger Account Event** `triggerAccountEvent`: Trigger Account Event. POST /api/v1/accounts/{externalId}/events. WARNING: an account event can start a sequence that sends email to the account's members. Docs: https://docs.sequenzy.com/api-reference/accounts/events-trigger
* **Trigger Subscriber Event** `triggerSubscriberEvent`: Trigger a Subscriber Event. POST /api/v1/subscribers/events. WARNING: an event can start a sequence that sends email.
* **Trigger Subscriber Events in Bulk** `triggerSubscriberEventsBulk`: Trigger several events for one subscriber. POST /api/v1/subscribers/events/bulk. WARNING: events can start sequences that send email.
* **Unarchive Sequence** `unarchiveSequence`: Unarchive Sequence. POST /api/v1/sequences/{sequenceId}/unarchive.
* **Unpublish Landing Page** `unpublishLandingPage`: Unpublish Landing Page. POST /api/v1/landing-pages/{landingPageId}/unpublish.
* **Unschedule Campaign** `unscheduleCampaign`: Unschedule Campaign (return a scheduled campaign to draft). POST /api/v1/campaigns/{campaignId}/unschedule.
* **Update A/B Test** `updateABTest`: Update A/B Test. PATCH /api/v1/ab-tests/{abTestId}. Docs: https://docs.sequenzy.com/api-reference/ab-tests/update
* **Update A/B Test Variant** `updateABTestVariant`: Update A/B Test Variant. PATCH /api/v1/ab-tests/{abTestId}/variants/{variantId}. Docs: https://docs.sequenzy.com/api-reference/ab-tests/update-variant
* **Update Account** `updateAccount`: Update Account attributes. PATCH /api/v1/accounts/{externalId}. Docs: https://docs.sequenzy.com/api-reference/accounts/update
* **Update API Key** `updateApiKey`: Update API Key name or permission preset. PATCH /api/v1/api-keys/{apiKeyId}. Docs: https://docs.sequenzy.com/api-reference/api-keys/update
* **Update Attio List Mapping** `updateAttioListMapping`: Update Attio List Mapping for an integration. PATCH /api/v1/integrations/{id}/attio.
* **Update Audience Sync** `updateAudienceSync`: Update Audience Sync frequency or active state. PATCH /api/v1/audience-syncs/{syncId}. Docs: https://docs.sequenzy.com/api-reference/audience-syncs/update
* **Update Campaign** `updateCampaign`: Update Campaign content, labels and target lists. PUT /api/v1/campaigns/{campaignId}. Docs: https://docs.sequenzy.com/api-reference/campaigns/update
* **Update Campaign Goal** `updateCampaignGoal`: Update Campaign Goal. PATCH /api/v1/campaigns/{campaignId}/goals/{goalId}. Docs: https://docs.sequenzy.com/api-reference/campaigns/goals
* **Update Company** `updateCompany`: Update Company branding, sender defaults and reply tracking. PATCH /api/v1/companies/{companyId}.
* **Update Conversation Status** `updateConversationStatus`: Update Conversation Status (open/closed). POST /api/v1/conversations/{conversationId}/status.
* **Update Email** `updateEmail`: Update Email. PATCH /api/v1/emails/{emailId}.
* **Update Email Blocks** `updateEmailBlocks`: Update Email Blocks (structured content). PATCH /api/v1/emails/{emailId}/blocks.
* **Update Email Component** `updateEmailComponent`: Update Email Component. PATCH /api/v1/email-components/{componentId}.
* **Update Email Design System** `updateEmailDesignSystem`: Update Email Design System. PATCH /api/v1/email-design-system.
* **Update Integration List Targeting** `updateIntegrationListTargeting`: Update Integration sync settings and list targeting. PATCH /api/v1/integrations/{id}.
* **Update Landing Page** `updateLandingPage`: Update Landing Page. PUT /api/v1/landing-pages/{landingPageId}. Sending content replaces the whole document.
* **Update Landing Page Domain Settings** `updateLandingPageDomainSettings`: Update workspace Landing Page Domain settings. PUT /api/v1/landing-pages/domain.
* **Update Notification Preferences** `updateNotificationPreferences`: Update account notification preferences. PATCH /api/v1/notification-preferences.
* **Update Outbound Webhook** `updateOutboundWebhook`: Update an Outbound Webhook endpoint (url, events, enabled/disabled). PATCH /api/v1/webhooks/{webhookId}.
* **Update Popup** `updatePopup`: Update Popup content, targeting or status. PATCH /api/v1/popups/{popupId}.
* **Update Saved Form** `updateSavedForm`: Update Saved Form. PATCH /api/v1/forms/{formId}.
* **Update Segment** `updateSegment`: Update Segment name or filter tree. PATCH /api/v1/segments/{segmentId}.
* **Update Sequence** `updateSequence`: Update Sequence settings, steps, branches or graph. PUT /api/v1/sequences/{sequenceId}. WARNING: structural changes on an active sequence affect live sends.
* **Update Sequence Goal** `updateSequenceGoal`: Update Sequence Goal. PATCH /api/v1/sequences/{sequenceId}/goals/{goalId}.
* **Update Shopify Automation Settings** `updateShopifyAutomationSettings`: Update Shopify automation settings (price drop, browse abandonment). PUT /api/v1/shopify/automation-settings.
* **Update Subscriber** `updateSubscriber`: Update a Subscriber by email. PATCH /api/v1/subscribers/{email}.
* **Update Subscriber by External ID** `updateSubscriberByExternalId`: Update a Subscriber by your external id. PATCH /api/v1/subscribers/external.
* **Update Subscriber List** `updateSubscriberList`: Update Subscriber List. PATCH /api/v1/lists/{listId}.
* **Update Sync Rules** `updateSyncRules`: Replace integration sync rules. PUT /api/v1/sync-rules. WARNING: this replaces the whole rule set.
* **Update Tag** `updateTag`: Update Tag colour. PATCH /api/v1/tags/{tagId}.
* **Update Template** `updateTemplate`: Update an Email Template. PUT /api/v1/templates/{templateId}.
* **Update Tracking Settings** `updateTrackingSettings`: Update open/click tracking settings. PATCH /api/v1/tracking-settings.
* **Update Transactional Email** `updateTransactionalEmail`: Update a Transactional Email template. PATCH /api/v1/transactional/{idOrSlug}.
* **Update Web Tracking Key** `updateWebTrackingKey`: Update a Web Tracking Key's allowed origins. PATCH /api/v1/web-tracking-keys/{id}.
* **Upload Image Bytes** `uploadImageBytes`: Upload Image Bytes to a pre-signed key. PUT /api/v1/media/upload-bytes?key=&filename=&contentType=&fileSizeBytes= - the host reads all four from the QUERY STRING, not the body. BLOCKED BY A FASTN ENGINE BUG: the engine drops query params on PUT (both the queryParams map and an inline ?query in the url), so the host always answers 422 "Expected property 'key' to be string but found: undefined". Binary payloads are a second engine gap here. Use Create Image Upload URL and PUT to the returned uploadUrl directly instead.
* **Upsert Products** `upsertProducts`: Upsert Products in bulk. POST /api/v1/products.
* **Verify Landing Page Custom Domain** `verifyLandingPageCustomDomain`: Verify a Landing Page's dedicated custom domain. POST /api/v1/landing-pages/{landingPageId}/domain/verify.
* **Verify Landing Page Domain** `verifyLandingPageDomain`: Verify the workspace Landing Page Domain DNS. POST /api/v1/landing-pages/domain/verify.
* **Verify Sending Domain** `verifySendingDomain`: Verify a sending domain's DNS. POST /api/v1/websites/{domain}/verify.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Campaign Sent | `campaign.sent` | A campaign finished sending. Not in the default set - request it explicitly. |
| Email Bounced | `email.bounced` | The message hard- or soft-bounced. |
| Email Complained | `email.complained` | The recipient marked the message as spam. |
| Email Delivered | `email.delivered` | The receiving mail server accepted the message. |
| Email Delivery Delayed | `email.delivery_delayed` | Delivery was deferred and will be retried. |
| Email Failed | `email.failed` | Sequenzy could not send the message. |
| Email Link Clicked | `email.clicked` | Click tracking fired. Not in the default set - request it explicitly. |
| Email Opened | `email.opened` | Open tracking fired. Not in the default set - request it explicitly. |
| Email Replied | `email.replied` | An inbound reply was received. Not in the default set. |
| Email Sent | `email.sent` | Sequenzy accepted an email for delivery. |

<details>

<summary>See 15 more events</summary>

* **Email Unsubscribed** `email.unsubscribed`: The recipient unsubscribed from an email.
* **Poll Answered** `poll.answered`: A recipient answered a poll block. Not in the default set.
* **Sequence Failed** `sequence.failed`: A sequence run failed. Not in the default set.
* **Sequence Finished** `sequence.finished`: A subscriber completed a sequence. Not in the default set.
* **SMS Delivered** `sms.delivered`: An SMS was delivered.
* **SMS Failed** `sms.failed`: An SMS failed to send.
* **SMS Opted Out** `sms.opted_out`: The recipient opted out of SMS.
* **SMS Sent** `sms.sent`: An SMS was accepted for delivery.
* **Subscriber Created** `subscriber.created`: A new subscriber was created.
* **Subscriber Import Completed** `subscriber_import.completed`: A subscriber import finished. Not in the default set.
* **Subscriber Invalid** `subscriber.invalid`: The subscriber address was found invalid.
* **Subscriber Joined List** `subscriber.list_subscribed`: Per-list consent was granted. Not in the default set.
* **Subscriber Left List** `subscriber.list_unsubscribed`: Per-list consent was withdrawn. Not in the default set.
* **Subscriber Unsubscribed** `subscriber.unsubscribed`: A subscriber opted out.
* **Subscriber Updated** `subscriber.updated`: A subscriber profile changed. Not in the default set.

</details>
