---
description: "Passcreator — Apple Wallet and Google Wallet pass platform."
hidden: true
---

# Passcreator

<img src="../../.gitbook/assets/connectors/lg/passcreator.png" alt="Passcreator logo">

Passcreator — Apple Wallet and Google Wallet pass platform. Manage pass templates, create/update/void/delete passes, bundles, push notifications, distribution links, app-scan validation, statistics and webhooks over the v1/v2/v3 REST API at app.passcreator.com.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [passcreator.com](https://passcreator.com) |
| **Authentication** | API key |
| **Slug** | `passcreator` |

## Use it

Add Passcreator from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.passcreator.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Acknowledge Webhook Payloads | `acknowledgeWebhookPayloads` | Marks every unacknowledged pull-mode payload up to and including the given payload id as processed, so the pull endpoint stops returning them. Idempotent. POST /api/v3/webhook-payload/acknowledge. |
| Bulk Patch Passes (V3) | `bulkPatchPassesV3` | Updates only the supplied properties on many passes at once, selected by identifiers, a segmentId or a query-language filter. Returns a process identifier you can poll with Get Bulk Process Status. PATCH /api/v3/pass/bulk. |
| Bulk Replace Passes (V3) | `bulkReplacePassesV3` | Replaces data on many passes at once, selected by a list of identifiers, a segmentId or a query-language filter. Properties left out are deleted. Returns a process identifier you can poll with Get Bulk Process Status. POST /api/v3/pass/bulk. |
| Check Pass By Auto Id | `checkPassByUserProvidedId` | Looks a pass up by its Passcreator-generated auto id (the generatedId field of a pass, not the userProvidedId). Returns the pass identifier and template, or 404 "AutoID not known." Deprecated v1 route. GET /api/pass/checkbyid/{id}. |
| Copy Pass Template | `copyPassTemplate` | Copies a pass template inside your own account and returns 201 with the new identifier. name is mandatory; without it the route silently answers 200 with a null body and copies nothing. POST /api/pass-template/copy/{identifier}. |
| Copy Pass Template To Customer | `copyPassTemplateToCustomer` | Copies a pass template into a sub-customer account you created through the API (reseller / white-label). name is mandatory; without it the route silently answers 200 with a null body and copies nothing. POST /api/pass-template/copy/{identifier}/{targetCustomerId}. |
| Create App Configuration | `createAppConfiguration` | Creates a scanner-app configuration for a pass template. Note that the Passcreator API exposes no delete route for app configurations, so a configuration created here can only be removed in the web UI. POST /api/appconfiguration. |
| Create App Scan | `createAppScan` | Records a pass validation scan against an app configuration, as the Passcreator scanner app does, optionally voiding the pass. The API has no delete route for scans, so a scan written here is permanent. POST /api/appscan. |
| Create iFrame Integration | `createIframeIntegration` | Creates an embeddable iFrame integration for a pass template so visitors can self-issue a pass. Returns 201 with integrationId. POST /api/integration/iframe/{template}. |
| Create Or Update Pass Bundle | `upsertPassBundle` | Puts a set of passes into a bundle so they share one download link. Creates the bundle if the bundleId is new. POST /api/v2/pass-bundle/{bundleId}. |
| Create Pass | `createPass` | Creates a pass from a template using the legacy v1 route. Returns 201 with the pass identifier, the pkpass link and the pass page link. Any extra key you pass is forwarded as a template additional-property value (zapierStyle), e.g. "Points": "10". POST /api/pass?passtemplate={passtemplate}&zapierStyle=true. |
| Create Pass (V3) | `createPassV3` | Creates a pass with the v3 API. The pass properties go inside a data object; extra keys inside data are template additional-property values. Set async=false to get the real barcodeValue back in the response. POST /api/v3/pass. |
| Create Pass Template | `createPassTemplate` | Creates a new pass template. Requires name, description, organizationName, type, passTypeId, fields (at least one front field and one back field), barcode, images (logo and icon must be URLs, not null) and colors. Returns 201 with data.identifier. POST /api/v2/pass-template. |
| Create URL Integration | `createUrlIntegration` | Creates (or returns the existing) URL integration for a pass template and hands back a public create-pass URL with a query placeholder per template field. 201 when created, 200 when one already existed. POST /api/integration/url/{template}. |
| Delete Pass | `deletePass` | Permanently deletes a pass. DELETE /api/pass/{pass}. |
| Delete Pass (V3) | `deletePassV3` | Deletes a pass with the v3 API and returns the deleted identifier inside the standard v3 envelope. DELETE /api/v3/pass/{identifier}. |
| Delete Pass Bundle | `deletePassBundle` | Deletes a pass bundle. The passes themselves stay, only the grouping is removed. DELETE /api/v2/pass-bundle/{bundleId}. |
| Delete Pass Template | `deletePassTemplate` | Permanently deletes a pass template and every pass issued from it. DELETE /api/pass-template/{identifier}. Returns 200 with a null body. |
| Delete Scheduled Push Notification | `deleteScheduledPushNotification` | Cancels a scheduled push notification that has not been delivered yet. Returns 200 with an empty array; an already-executed notification returns 400. DELETE /api/pass-template/notification/{notificationId}. |
| Delete Webhook Subscription | `deleteWebhookSubscription` | DELETE variant of the unsubscribe route, identifying the subscription by its target_url. DELETE /api/hook/unsubscribe. |
| Describe Pass Template | `describePassTemplate` | Returns the complete v2 structure of a pass template (fields, barcode, images, colors, additionalProperties, locations, beacons). Use its data object as the starting point for Create/Update Pass Template. GET /api/v2/pass-template/{identifier}/describe. |
| Download Pass PDF | `getPassPdf` | Downloads a printable PDF version of a pass as binary application/pdf. The PDF download feature has to be switched on by Passcreator support; otherwise the route answers 403 "API PDF download feature is not enabled for this customer". GET /api/v3/pass/{identifier}/pdf. |
| Enable Pass Download | `enablePassDownload` | Temporarily re-enables downloading an already-active pass when the template blocks re-download. Returns 204 with no body. POST /api/pass/{pass}/enabledownload. |
| Get Account Info | `getAccountInfo` | Returns the Passcreator customer account the API key belongs to (customer name and account email). Undocumented but live route GET /api/ping. Useful as a credential check. |
| Get Active Pass History | `getPassActiveHistory` | Returns the day-by-day total of active and inactive passes for a template from startingday until today. Omit startingday for the last seven days. GET /api/pass/statistics/{template}/activehistory/{startingday}. |
| Get App Configuration | `getAppConfiguration` | Returns one scanner-app configuration in full, including scan mode, validation places and the extra properties the scanner collects. GET /api/appconfiguration/{configurationId}. |
| Get Bulk Process Status | `getBulkProcessStatus` | Returns the progress, state and any errors of a bulk operation started by one of the v3 bulk endpoints. GET /api/v3/process/{identifier}. |
| Get Customer Accounts | `getCustomerAccounts` | Undocumented reseller route that returns sub-customer accounts. On a normal (non-reseller) API key it answers HTTP 400 with an empty array rather than data. GET /api/customer. |
| Get Pass | `getPass` | Returns one pass by its UUID, userProvidedId or barcode value, including its field data, template, links and activation counters. GET /api/pass/{pass}. |
| Get Pass Bundle | `getPassBundle` | Returns the passes contained in a bundle and the bundle download link. GET /api/v2/pass-bundle/{bundleId}. |
| Get Pass Download URIs | `getPassUris` | Returns the direct Apple Wallet pkpass URI and the Android/Google Pay URI for a pass, for building your own delivery flow. GET /api/pass/geturis/{pass}. |
| Get Pass Template | `getPassTemplate` | Returns full information about one pass template (legacy v1 shape). GET /api/pass-template/{identifier}. |
| Get Pass Template Fields | `getPassTemplateFields` | Returns the field list of one pass template in Zapier style (flat list of the properties a pass created from this template accepts). GET /api/pass-template/{identifier}?zapierStyle=true. |
| Get Pass Usage Statistics | `getPassStatistics` | Returns timelines of pass creations, updates, deactivations and device saves for a template over a day, week, month or year, broken down by operating system. GET /api/pass/statistics/{template}?timeFrame=&day=. |
| Get Placeholder Signing Public Key | `getSigningPublicKey` | Returns the public key needed to verify signatures produced by the {sign()} placeholder function on a pass. GET /api/v3/signing/publickey. |
| Get Webhook Public Key | `getWebhookPublicKey` | Returns the PEM public key used to verify the SHA1 signature Passcreator attaches to signed webhook deliveries. GET /api/hook/publickey. |
| List All Passes | `listAllPasses` | Returns every pass in the account across all templates, as an array with identifier, uri, linkToPassPage and barcode value. Undocumented but live route GET /api/pass. |
| List App Configurations | `listAppConfigurations` | Lists the scanner-app configurations in the account, each describing which templates the Passcreator validation app may scan and how. GET /api/appconfiguration. |
| List App Scans | `listAppScans` | Returns the scans recorded by the Passcreator validation app for one app configuration, paged with start and pageSize. GET /api/appscan/list/{appConfigurationId}. |
| List App Scans (Deprecated) | `listAppScansDeprecated` | Deprecated unpaged variant that returns app scans via the appConfigurationId query parameter. Prefer List App Scans. GET /api/appscan?appConfigurationId=. |
| List Pass Templates | `listPassTemplates` | Lists every pass template the API key has access to, as an array of {identifier, name}. GET /api/pass-template. |
| List Passes (V3) | `listPassesV3` | Lists or searches passes with the v3 API. Supports pageSize, a comma-separated fields list, a saved segmentId and a base64 url-safe encoded query-language filter. GET /api/v3/pass. |
| List Passes By Template Query | `listPassesByTemplateQuery` | Deprecated v1 route that lists the passes of a template using the passId query parameter instead of a path segment. Prefer List Passes Of Template. GET /api/pass/?passId={passId}. |
| List Passes Of Template | `listPassesOfTemplate` | Returns the passes of one template ordered by creation date, with start/pageSize paging (pageSize max 100) and optional createdSince/modifiedSince filters. GET /api/pass/list/{template}. |
| List Scheduled Push Notifications | `listTemplatePushNotifications` | Lists every past and pending scheduled push notification and scheduled template publication for a pass template, under scheduledTasks. A scheduled entry without notificationText is a pending template publication. GET /api/pass-template/{template}/notification. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | Lists the active webhook subscriptions of the account, with their event type and target URL. GET /api/hook/list. |
| Move Pass To Another Template | `movePassToTemplate` | Moves an existing pass to a different pass template, keeping its identifier. Preconditions enforced by Passcreator: the pass must belong to a project, the target template must be in the same project, and both templates must use the same signing certificate. Projects are created in the Passcreator web app; a pass outside a project returns 400 "This pass can't be moved because it is not part of a project." POST /api/v2/pass/{identifier}/movetotemplate/{targetTemplateIdentifier}. |
| Patch Pass (V3) | `patchPassV3` | Updates only the supplied properties of one pass and leaves everything else untouched. PATCH /api/v3/pass/{identifier}. |
| Patch Pass Template | `patchPassTemplate` | Partially updates a pass template: only the supplied properties change, everything else is kept. PATCH /api/v2/pass-template/{identifier}. |
| Publish Pass Template Changes | `publishPassTemplate` | Publishes the pending draft changes of a pass template at the given publicationDate, pushing them to passes already issued from it. POST /api/v2/pass-template/{identifier}/publish. |
| Pull Webhook Payloads | `pullWebhookPayloads` | Returns the pull-mode webhook payloads that have not been acknowledged yet, oldest first, optionally narrowed by webhookId, limit or an ISO 8601 since timestamp. GET /api/v3/webhook-payload. |
| Replace Pass (V3) | `replacePassV3` | Replaces the data of one pass with the v3 API. Properties you leave out are deleted from the pass; use Patch Pass (V3) to change only some fields. POST /api/v3/pass/{identifier}. |
| Schedule Push Notification | `scheduleTemplatePushNotification` | Schedules a push notification to every device that holds a pass of the given template. Sends to real devices at sendOn, so only use it on templates you control. POST /api/pass-template/{template}/notification. |
| Search Passes | `searchPasses` | Fuzzy-searches the passes of one template by any content they carry, such as a name or an email address. GET /api/pass/search/{template}/{searchString}. |
| Send Pass By Email | `sendPassByEmail` | Emails a pass to a recipient using the ad-hoc email template configured on the pass template. Returns 400 if the template has no ad-hoc email template. POST /api/pass/deliver/{pass}/email/{recipientMail}. |
| Send Push Notification To Many Passes | `sendPushNotificationToPasses` | Sends one push notification to up to 500 passes at once, listed by identifier. POST /api/pass/sendpushnotifications. |
| Send Push Notification To Pass | `sendPushNotificationToPass` | Sends a push notification to the devices holding one active pass. 204 on success, 304 if the same text was already sent, 400 if the pass has no device registration. POST /api/pass/{pass}/sendpushnotification. |
| Set Pass Voided | `setPassVoided` | Marks a pass voided or un-voided. A voided pass shows a greyed-out barcode on the holder's device and can no longer be used. PUT /api/pass/{pass}. |
| Subscribe Webhook | `subscribeWebhook` | Subscribes a target URL to one Passcreator event across the whole account. Returns 201. Set pullMode true to store events for polling instead of pushing them. POST /api/hook/subscribe. |
| Subscribe Webhook For Template | `subscribeWebhookForTemplate` | Subscribes a target URL to one Passcreator event limited to a single pass template. Returns 201, or 404 if the template is unknown. POST /api/hook/subscribe/{templateIdentifier}. |
| Unsubscribe Webhook | `unsubscribeWebhook` | Removes a webhook subscription, identified by the target_url it was created with. Pull-mode subscriptions have no target URL and can only be removed in the web UI. POST /api/hook/unsubscribe. |
| Update Pass | `updatePass` | Updates an existing pass on the legacy v1 route. Any extra key is treated as a template additional-property value (zapierStyle). POST /api/pass/{pass}?zapierStyle=true. |
| Update Pass Template | `updatePassTemplate` | Replaces a pass template with the supplied configuration; omitted properties are reset. Same body shape as Create Pass Template. POST /api/v2/pass-template/{identifier}. |
| Update Pass Template (Legacy) | `updatePassTemplateLegacy` | Deprecated v1 route that updates a pass template's name, description or images. Prefer Patch Pass Template. POST /api/pass-template/{identifier}. |
| Void Pass Bundle | `voidPassBundle` | Voids or un-voids every pass in a bundle in one call. PUT /api/v2/pass-bundle/void/{bundleId}. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| App Scan Created | `app_scan_created` | A pass was scanned with the Passcreator companion app or a scan was written through the API. scanStatus: 0 known and now voided, 1 already voided, 2 known and still valid. Schema modelled from the vendor's documented sample. |
| Message Failed | `message_failed` | An email or SMS failed to send, bounced, was skipped or marked spam. Schema modelled from the vendor's documented sample. |
| Message Sent | `message_sent` | An email or SMS carrying a pass was sent or delivered. Schema modelled from the vendor's documented sample. |
| Pass Created | `pass_created` | A pass was created from one of your templates. Payload carries identifier, passId, uniqueIdentifier, createdOn, passTemplate, passTemplateGuid, userProvidedId, barcodeValue, linkToPassPage, the buyer fields and one key per personalised template property. Schema captured from a real Passcreator delivery. |
| Pass Removed From A Device | `pushnotification_unregistered` | A device removed the pass or turned its notifications off. Same payload as Pass Saved To A Device. Schema modelled from the vendor's documented sample. |
| Pass Saved For The First Time | `first_pushnotification_registered` | The pass was saved to any device for the very first time. Same payload as Pass Saved To A Device. Schema modelled from the vendor's documented sample. |
| Pass Saved To A Device | `pushnotification_registered` | A device saved the pass and registered for push notifications. Payload adds noOfActivePasses, noOfInactivePasses and operatingSystem. Schema modelled from the vendor's documented sample. |
| Pass Template Created | `pass_template_created` | A new pass template was created in the account. Schema modelled from the vendor's documented sample. |
| Pass Template Updated | `pass_template_updated` | An existing pass template was changed. Schema modelled from the vendor's documented sample. |
| Pass Updated | `pass_updated` | An existing pass was updated. Same payload shape as Pass Created, plus the personalised template properties in their new state. Schema modelled on the captured pass_created delivery and the vendor's documented sample. |
| Pass Voided | `pass_voided` | A pass was marked voided through an update. It does not fire when a pass merely expires. Same payload shape as Pass Updated. Schema modelled from the vendor's documented sample. |
