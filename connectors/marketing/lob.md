---
description: "Lob is a direct-mail and address-verification platform."
hidden: true
---

# Lob

Lob is a direct-mail and address-verification platform. This connector covers the Lob v1 REST API: postcards, letters, checks, self-mailers, snap packs, booklets, cards and buckslips; address book and address verification (US and international, single and bulk, autocompletion, ZIP lookup and reverse geocode); templates and template versions; bank accounts; campaigns, creatives, uploads and QR-code analytics; Informed Delivery campaigns; tracking links and domains; resource proofs; identity validation; billing groups; users; and event, event-type and webhook management.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [lob.com](https://lob.com) |
| **Authentication** | Basic auth |
| **Actions** | 110 |
| **Events** | 70 |
| **Slug** | `lob` |

## Use it

Add Lob from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.lob.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete International Address | `autocompleteInternationalAddress` | Returns international street address suggestions for a partial address, for use in type-ahead address entry. Results can be narrowed by city, state, postal code or country. |
| Autocomplete US Address | `autocompleteUsAddress` | Returns US street address suggestions for a partial address, for use in type-ahead address entry. Results can be narrowed by city, state or ZIP code. |
| Cancel Booklet | `cancelBooklet` | Cancels a booklet that has not yet entered production. Requires the booklet product to be enabled on your Lob account. |
| Cancel Check | `cancelCheck` | Cancels a check that has not yet entered production. Checks can only be cancelled during their cancellation window. |
| Cancel Letter | `cancelLetter` | Cancels a letter that has not yet entered production. Letters can only be cancelled during their cancellation window. |
| Cancel Postcard | `cancelPostcard` | Cancels a postcard that has not yet entered production. Postcards can only be cancelled during their cancellation window, which is until the send date. |
| Cancel Self Mailer | `cancelSelfMailer` | Cancels a self-mailer that has not yet entered production. Requires the self-mailer product to be enabled on your Lob account. |
| Cancel Snap Pack | `cancelSnapPack` | Cancels a snap pack that has not yet entered production. Requires the snap pack product to be enabled on your Lob account. |
| Create Address | `createAddress` | Saves a new address in your Lob address book so it can be reused as the sender or recipient of mail. Supply either a recipient name or a company. US addresses need city, state and ZIP; international addresses need a two-letter country code. |
| Create Bank Account | `createBankAccount` | Registers a US bank account with Lob so that checks can be drawn on it. The account must be verified before it can be used to send checks in live mode. |
| Create Billing Group | `createBillingGroup` | Creates a billing group so mail pieces tagged with it are reported and invoiced separately. Billing groups require an account entitlement that Lob enables on request. |
| Create Booklet | `createBooklet` | Creates and schedules a saddle-stitched booklet for print and mail. With a test API key nothing is printed or mailed and no charge is incurred. Requires the booklet product to be enabled on your Lob account. |
| Create Buckslip | `createBuckslip` | Stocks a new buckslip insert with Lob by supplying front and back artwork and a size. Buckslips require an account entitlement that Lob enables on request. |
| Create Buckslip Order | `createBuckslipOrder` | Places a print order for more copies of a stocked buckslip. This bills the account for the buckslips produced. |
| Create Campaign | `createCampaign` | Creates a print-and-mail campaign that sends one creative to an uploaded audience on a schedule. Campaigns are a live-mode feature; a test API key is rejected. |
| Create Card | `createCard` | Stocks a new card with Lob by supplying front and back artwork and a size. Cards require an account entitlement that Lob enables on request. |
| Create Card Order | `createCardOrder` | Places a print order for more copies of a stocked card. This bills the account for the cards produced. |
| Create Check | `createCheck` | Creates and mails a physical check drawn on a verified bank account. With a test API key nothing is printed, mailed or paid; with a live API key the check is produced, posted and the funds are drawn. Checks cannot be sent internationally. |
| Create Creative | `createCreative` | Creates a reusable creative that defines the artwork and mail product a campaign sends. Creatives are a live-mode feature; a test API key is rejected. |
| Create Letter | `createLetter` | Creates and schedules a letter for print and mail. With a test API key nothing is printed or mailed and no charge is incurred; with a live API key the letter is produced and posted. |
| Create Postcard | `createPostcard` | Creates and schedules a postcard for print and mail. With a test API key nothing is printed or mailed and no charge is incurred; with a live API key the postcard is produced and posted. Addresses and artwork may be given as Lob resource IDs or as inline objects. |
| Create Resource Proof | `createResourceProof` | Requests a physical proof for a class of mail piece so that its print output can be reviewed before production. It is the seeding route for List Resource Proofs and Retrieve Resource Proof. |
| Create Self Mailer | `createSelfMailer` | Creates and schedules a folded self-mailer for print and mail. With a test API key nothing is printed or mailed and no charge is incurred. Lob exposes no list, retrieve or cancel route for self-mailers. |
| Create Snap Pack | `createSnapPack` | Creates and schedules a snap pack for print and mail. With a test API key nothing is printed or mailed and no charge is incurred. Requires the snap pack product to be enabled on your Lob account. |
| Create Template | `createTemplate` | Creates a reusable HTML template whose ID can be passed as the front or back of a postcard, letter, check or self-mailer instead of inline HTML. |
| Create Template Version | `createTemplateVersion` | Adds a new version of an existing HTML template. The new version is not used until it is published with Update Template. |
| Create Tracking Domain | `createTrackingDomain` | Registers a custom short domain so tracking links and QR codes carry your own branding. The domain must then be verified by adding the DNS records Lob returns. |
| Create Tracking Link | `createTrackingLink` | Creates a tracking link that redirects to your destination URL and records every scan or click, so QR codes and personalised URLs printed on mail can be measured. |
| Create Upload | `createUpload` | Creates an upload that holds the recipient audience for a campaign. Once created, attach the recipient CSV to it and Lob validates and maps the rows. |
| Create Upload Export | `createUploadExport` | Starts an export of a campaign audience upload so the processed recipient rows can be downloaded as a file. |
| Create Webhook | `createWebhook` | Registers a webhook so Lob posts the chosen event types to your HTTPS endpoint. The webhook lives in the mode of the API key used to create it, so a test key creates a test-mode webhook. Lob has no update endpoint for webhooks: delete and recreate one to change it. |
| Delete Address | `deleteAddress` | Permanently deletes a saved address from your Lob address book. Mail already created with the address is unaffected. |
| Delete Bank Account | `deleteBankAccount` | Permanently deletes a registered bank account. Checks already created with it are unaffected. |
| Delete Buckslip | `deleteBuckslip` | Permanently removes a stocked buckslip from the account so it can no longer be inserted into mailings. Buckslips require an account entitlement that Lob enables on request. |
| Delete Campaign | `deleteCampaign` | Permanently removes a print-and-mail campaign. Only campaigns that have not yet been sent can be deleted. |
| Delete Card | `deleteCard` | Permanently removes a stocked card from the account so it can no longer be ordered. Cards require an account entitlement that Lob enables on request. |
| Delete Template | `deleteTemplate` | Permanently deletes an HTML template and all of its versions. Mail already created from the template is unaffected. |
| Delete Template Version | `deleteTemplateVersion` | Permanently deletes a version of an HTML template. The currently published version of a template cannot be deleted. |
| Delete Tracking Domain | `deleteTrackingDomain` | Unlinks a custom short domain from the account. Tracking links already built on it stop resolving. |
| Delete Tracking Link | `deleteTrackingLink` | Permanently removes a tracking link. Any printed mail pointing at it stops redirecting. |
| Delete Upload | `deleteUpload` | Permanently removes a campaign audience upload and the recipient rows it holds. Lob answers HTTP 204 with an empty body on success. |
| Delete Webhook | `deleteWebhook` | Permanently removes a registered webhook so Lob stops posting events to its URL. |
| List Addresses | `listAddresses` | Returns a paginated list of the addresses saved in your Lob address book, sorted by creation date with the most recent first. |
| List Bank Accounts | `listBankAccounts` | Returns a paginated list of the bank accounts registered on your Lob account, sorted by creation date with the most recent first. |
| List Billing Groups | `listBillingGroups` | Returns the billing groups on the account. A billing group tags mail pieces so their spend is reported and invoiced separately. |
| List Booklets | `listBooklets` | Returns a paginated list of booklets, with optional filters on render status, mail type, creation date and send date. Requires the booklet product to be enabled on your Lob account. |
| List Buckslip Orders | `listBuckslipOrders` | Returns the print orders placed for a stocked buckslip, newest first, with the quantity and unit price of each run. |
| List Buckslips | `listBuckslips` | Returns the buckslip inserts stocked on the account, each with its artwork, size and remaining inventory. Buckslips require an account entitlement that Lob enables on request. |
| List Campaigns | `listCampaigns` | Returns the print-and-mail campaigns on the account, each with its audience, creatives, schedule and send status. |
| List Card Orders | `listCardOrders` | Returns the print orders placed for a stocked card, newest first, with the quantity and unit price of each run. |
| List Cards | `listCards` | Returns the plastic and paper cards stocked on the account, each with its artwork, size, orientation and remaining inventory. Cards require an account entitlement that Lob enables on request. |
| List Checks | `listChecks` | Returns a paginated list of checks, with optional filters on render status, mail type, creation date and send date. |
| List Event Types | `listEventTypes` | Returns every event type Lob can emit, with the resource family it belongs to and whether it fires in test mode. Use these ids when subscribing a webhook. |
| List Events | `listEvents` | Returns the account's event log, covering every change Lob recorded on mail pieces and other resources. Events are retained for 30 days and can be narrowed by event type, resource or creation date. |
| List Informed Delivery Campaigns | `listInformedDeliveryCampaigns` | Returns the USPS Informed Delivery campaigns on the account, which add a clickable digital ride-along image to the daily mail preview email. |
| List Letters | `listLetters` | Returns a paginated list of letters, with optional filters on render status, colour, mail type, campaign, creation date and send date. |
| List Postcards | `listPostcards` | Returns a paginated list of postcards, with optional filters on render status, size, mail type, campaign, creation date and send date. |
| List QR Code Scans | `listQrCodeScans` | Returns the QR code scan events recorded against mail pieces, so you can attribute responses to the postcards, letters or self-mailers that carried the code. |
| List Resource Proofs | `listResourceProofs` | Returns the physical proofs Lob has produced for mail pieces, each with the resource it proofs and the status of its production. |
| List Self Mailers | `listSelfMailers` | Returns a paginated list of self-mailers, with optional filters on render status, size, mail type, creation date and send date. Requires the self-mailer product to be enabled on your Lob account. |
| List Snap Packs | `listSnapPacks` | Returns a paginated list of snap packs, with optional filters on render status, size, mail type, creation date and send date. Requires the snap pack product to be enabled on your Lob account. |
| List Template Versions | `listTemplateVersions` | Returns a paginated list of every saved version of a given HTML template, sorted by creation date with the most recent first. |
| List Templates | `listTemplates` | Returns a paginated list of the HTML templates saved on your Lob account, sorted by creation date with the most recent first. |
| List Tracking Domains | `listTrackingDomains` | Returns the custom short domains registered on the account for branding tracking links and QR codes, with their DNS verification status. |
| List Tracking Links | `listTrackingLinks` | Returns the tracking links on the account. A tracking link turns a QR code or personalised URL printed on a mail piece into a measurable redirect. |
| List Uploads | `listUploads` | Returns the campaign audience uploads on the account, each with its processing state, row count and column mappings. |
| List Webhooks | `listWebhooks` | Returns the webhooks registered in the mode of the API key in use, each with its target URL and subscribed event types. |
| Look Up US ZIP Code | `lookUpUsZipCode` | Returns the cities, counties and geographic data associated with a five-digit US ZIP code. |
| Retrieve Address | `retrieveAddress` | Retrieves a single saved address from your Lob address book by its address ID. |
| Retrieve Bank Account | `retrieveBankAccount` | Retrieves a single registered bank account by its bank account ID. |
| Retrieve Billing Group | `retrieveBillingGroup` | Retrieves a single billing group by id, with its name and description. |
| Retrieve Booklet | `retrieveBooklet` | Retrieves a single booklet by its ID. Requires the booklet product to be enabled on your Lob account. |
| Retrieve Buckslip | `retrieveBuckslip` | Returns a single stocked buckslip by its identifier, including its artwork URLs and remaining inventory. Buckslips require an account entitlement that Lob enables on request. |
| Retrieve Campaign | `retrieveCampaign` | Retrieves a single print-and-mail campaign by id, including its schedule, attached creatives and current status. |
| Retrieve Card | `retrieveCard` | Returns a single stocked card by its identifier, including its artwork URLs and remaining inventory. Cards require an account entitlement that Lob enables on request. |
| Retrieve Check | `retrieveCheck` | Retrieves a single check by its check ID, including its proof URL, thumbnails and tracking events. |
| Retrieve Creative | `retrieveCreative` | Retrieves a single campaign creative by id, including its mail product, return address and artwork details. |
| Retrieve Event | `retrieveEvent` | Retrieves a single logged event by id, including the full resource body as it existed when the event fired. Events are retained for 30 days. |
| Retrieve Informed Delivery Campaign | `retrieveInformedDeliveryCampaign` | Retrieves a single USPS Informed Delivery campaign by its USPS campaign id, including its ride-along image, click-through target and status. |
| Retrieve Letter | `retrieveLetter` | Retrieves a single letter by its letter ID, including its proof URL, thumbnails and tracking events. |
| Retrieve Postcard | `retrievePostcard` | Retrieves a single postcard by its postcard ID, including its proof URL, thumbnails and tracking events. |
| Retrieve Resource Proof | `retrieveResourceProof` | Retrieves a single physical proof by id, including the mail piece it proofs and its production status. |
| Retrieve Self Mailer | `retrieveSelfMailer` | Retrieves a single self-mailer by its ID. Requires the self-mailer product to be enabled on your Lob account. |
| Retrieve Snap Pack | `retrieveSnapPack` | Retrieves a single snap pack by its ID. Requires the snap pack product to be enabled on your Lob account. |
| Retrieve Template | `retrieveTemplate` | Retrieves a single HTML template by its template ID, including its versions and the currently published version. |
| Retrieve Template Version | `retrieveTemplateVersion` | Retrieves a single version of an HTML template, including its stored HTML body. |
| Retrieve Tracking Domain | `retrieveTrackingDomain` | Retrieves a single custom tracking domain by its identifier, including its registration status and error redirect link. |
| Retrieve Tracking Link | `retrieveTrackingLink` | Retrieves a single tracking link by id, including its destination URL, campaign and custom domain. |
| Retrieve Upload | `retrieveUpload` | Retrieves a single campaign audience upload by id, including its processing state, validated row count and column mappings. |
| Retrieve Upload Export | `retrieveUploadExport` | Retrieves the status of an upload export job and, once it has finished, the signed URL the exported file can be downloaded from. |
| Retrieve Upload Report | `retrieveUploadReport` | Returns the validation report for a campaign audience upload, summarising how many recipient rows were accepted and why any were rejected. |
| Retrieve Webhook | `retrieveWebhook` | Retrieves a single registered webhook by id, including its target URL, subscribed event types and status. |
| Reverse Geocode US Location | `reverseGeocodeUsLocation` | Returns the US ZIP codes and city components closest to a latitude and longitude pair, ordered by distance from the point supplied. |
| Send Campaign | `sendCampaign` | Submits a draft campaign for production so Lob prints and mails it to the uploaded audience. This spends account credit and cannot be undone once the cancellation window closes. |
| Update Billing Group | `updateBillingGroup` | Updates a billing group's name or description. Lob has no delete endpoint for billing groups. |
| Update Buckslip | `updateBuckslip` | Changes the description or automatic reorder settings of a stocked buckslip. Buckslips require an account entitlement that Lob enables on request. |
| Update Campaign | `updateCampaign` | Updates a print-and-mail campaign's name, description, schedule or cancellation settings. Only the fields supplied are modified, and only campaigns that have not yet sent can be changed. |
| Update Card | `updateCard` | Changes the description or automatic reorder settings of a stocked card. Cards require an account entitlement that Lob enables on request. |
| Update Creative | `updateCreative` | Updates a campaign creative's label, return address or artwork details. Creatives are a live-mode feature; a test API key is rejected. |
| Update Template | `updateTemplate` | Updates a template's internal description or switches which of its versions is published and therefore used when the template is referenced. |
| Update Template Version | `updateTemplateVersion` | Updates the internal description, merge engine or required variables of an existing template version. |
| Update Tracking Link | `updateTrackingLink` | Repoints a tracking link at a different destination URL or custom domain without changing the printed short link. |
| Update Upload | `updateUpload` | Updates the column mappings on a campaign audience upload, so Lob reads different CSV headers for the address, metadata or merge variable fields. |
| Upload Campaign Recipient File | `uploadCampaignRecipientFile` | Attaches a CSV of campaign recipients to an existing upload so Lob can validate and process the rows. Supply the CSV as text, with a header row whose column names match the upload's mapping. |
| Validate Identity | `validateIdentity` | Checks whether a named person or company is associated with a given US address, returning a match confidence for identity verification workflows. |
| Verify Bank Account | `verifyBankAccount` | Verifies a registered bank account so it can be used to send checks. Supply either the two microdeposit amounts in cents or the six-character statement descriptor code. In test mode no microdeposits are placed, so any two integers between 1 and 100 are accepted. |
| Verify International Address | `verifyInternationalAddress` | Standardizes and verifies a single non-US address against international postal data, returning the corrected components, deliverability status and coverage level. |
| Verify International Addresses In Bulk | `verifyInternationalAddressesBulk` | Standardizes and verifies up to 1,000 non-US addresses in a single request, returning one verification result per submitted address in the same order. |
| Verify US Address | `verifyUsAddress` | Standardizes and verifies a single US or US-territory address against USPS data, returning the corrected components, deliverability status and geocoding. Supply either the parsed lines or a single unparsed address string. Test-mode keys return simulated results: set Primary Line to deliverable, undeliverable, deliverable_missing_unit, deliverable_incorrect_unit or deliverable_unnecessary_unit and ZIP Code to 11111. |
| Verify US Addresses In Bulk | `verifyUsAddressesBulk` | Standardizes and verifies up to 1,000 US addresses in a single request, returning one verification result per submitted address in the same order. Test-mode keys return simulated results: set each Primary Line to deliverable or undeliverable and each ZIP Code to 11111. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Address Created | `address.created` | Fires when an address book entry is created. Enabled in test mode. |
| Address Deleted | `address.deleted` | Fires when an address book entry is deleted. Enabled in test mode. |
| Bank Account Created | `bank_account.created` | Fires when a bank account is created. Enabled in test mode. |
| Bank Account Deleted | `bank_account.deleted` | Fires when a bank account is deleted. Enabled in test mode. |
| Bank Account Verified | `bank_account.verified` | Fires when a bank account completes micro-deposit verification. Enabled in test mode. |
| Certified Letter Available For Pickup | `letter.certified.pickup_available` | Fires when a certified letter is available for pickup. Live mode only. |
| Certified Letter Delivered | `letter.certified.delivered` | Fires when a certified letter is delivered. Live mode only. |
| Certified Letter In Local Area | `letter.certified.in_local_area` | Fires when a certified letter reaches the recipient's local area. Live mode only. |
| Certified Letter In Transit | `letter.certified.in_transit` | Fires when a certified letter is in transit. Live mode only. |
| Certified Letter Issue | `letter.certified.issue` | Fires when USPS reports a problem with a certified letter. Live mode only. |
| Certified Letter Mailed | `letter.certified.mailed` | Fires when a certified letter is mailed. Live mode only. |
| Certified Letter Processed For Delivery | `letter.certified.processed_for_delivery` | Fires when a certified letter is processed for delivery. Live mode only. |
| Certified Letter Re-Routed | `letter.certified.re-routed` | Fires when a certified letter is re-routed. Live mode only. |
| Certified Letter Returned To Sender | `letter.certified.returned_to_sender` | Fires when a certified letter is returned to sender. Live mode only. |
| Check Billed | `check.billed` | Fires when a check is billed to the account. Enabled in test mode. |
| Check Cancelled | `check.deleted` | Fires when a check is cancelled before printing. Enabled in test mode. |
| Check Created | `check.created` | Fires when a check is created. Enabled in test mode. |
| Check Delivered | `check.delivered` | Fires when USPS reports the check delivered. Live mode only. |
| Check Failed | `check.failed` | Fires when a check fails to render or print. Enabled in test mode. |
| Check In Local Area | `check.in_local_area` | Fires when USPS reports the check in the recipient's local area. Live mode only. |
| Check In Transit | `check.in_transit` | Fires when USPS reports the check in transit. Live mode only. |
| Check Informed Delivery Email Clicked | `check.informed_delivery.email_clicked_through` | Fires when the recipient clicks through the Informed Delivery email. Live mode only. |
| Check Informed Delivery Email Clicked (Legacy) | `check.informed_delivery.when_clicked_through` | Legacy alias of the Informed Delivery click-through event for checks. Live mode only. |
| Check Informed Delivery Email Opened | `check.informed_delivery.email_opened` | Fires when the recipient opens the Informed Delivery email. Live mode only. |
| Check Informed Delivery Email Opened (Legacy) | `check.informed_delivery.when_email_was_opened` | Legacy alias of the Informed Delivery email-opened event for checks. Live mode only. |
| Check Informed Delivery Email Sent | `check.informed_delivery.email_sent` | Fires when USPS sends the Informed Delivery email for the check. Live mode only. |
| Check Informed Delivery Email Sent (Legacy) | `check.informed_delivery.when_email_was_sent` | Legacy alias of the Informed Delivery email-sent event for checks. Live mode only. |
| Check International Exit | `check.international_exit` | Fires when the check leaves the country of origin. Live mode only. |
| Check PDF Rendered | `check.rendered_pdf` | Fires when a check's print-ready PDF has been rendered. Enabled in test mode. |
| Check Processed For Delivery | `check.processed_for_delivery` | Fires when USPS processes the check for delivery. Live mode only. |
| Check Re-Routed | `check.re-routed` | Fires when USPS re-routes the check. Live mode only. |
| Check Rejected | `check.rejected` | Fires when a check is rejected during production. Enabled in test mode. |
| Check Returned To Sender | `check.returned_to_sender` | Fires when USPS returns the check to sender. Live mode only. |
| Check Thumbnails Rendered | `check.rendered_thumbnails` | Fires when a check's preview thumbnails have been rendered. Enabled in test mode. |
| Letter Billed | `letter.billed` | Fires when a letter is billed to the account. Enabled in test mode. |
| Letter Cancelled | `letter.deleted` | Fires when a letter is cancelled before printing. Enabled in test mode. |
| Letter Created | `letter.created` | Fires when a letter is created. Enabled in test mode. |
| Letter Delivered | `letter.delivered` | Fires when USPS reports the letter delivered. Live mode only. |
| Letter Failed | `letter.failed` | Fires when a letter fails to render or print. Enabled in test mode. |
| Letter In Local Area | `letter.in_local_area` | Fires when USPS reports the letter in the recipient's local area. Live mode only. |
| Letter In Transit | `letter.in_transit` | Fires when USPS reports the letter in transit. Live mode only. |
| Letter Informed Delivery Email Clicked | `letter.informed_delivery.email_clicked_through` | Fires when the recipient clicks through the Informed Delivery email. Live mode only. |
| Letter Informed Delivery Email Opened | `letter.informed_delivery.email_opened` | Fires when the recipient opens the Informed Delivery email. Live mode only. |
| Letter Informed Delivery Email Sent | `letter.informed_delivery.email_sent` | Fires when USPS sends the Informed Delivery email for the letter. Live mode only. |
| Letter International Exit | `letter.international_exit` | Fires when the letter leaves the country of origin. Live mode only. |
| Letter PDF Rendered | `letter.rendered_pdf` | Fires when a letter's print-ready PDF has been rendered. Enabled in test mode. |
| Letter Processed For Delivery | `letter.processed_for_delivery` | Fires when USPS processes the letter for delivery. Live mode only. |
| Letter Re-Routed | `letter.re-routed` | Fires when USPS re-routes the letter. Live mode only. |
| Letter Rejected | `letter.rejected` | Fires when a letter is rejected during production. Enabled in test mode. |
| Letter Returned To Sender | `letter.returned_to_sender` | Fires when USPS returns the letter to sender. Live mode only. |
| Letter Thumbnails Rendered | `letter.rendered_thumbnails` | Fires when a letter's preview thumbnails have been rendered. Enabled in test mode. |
| Letter Tracking Page Viewed | `letter.viewed` | Fires when the recipient opens the letter's tracking page. Enabled in test mode. |
| Postcard Billed | `postcard.billed` | Fires when a postcard is billed to the account. Enabled in test mode. |
| Postcard Cancelled | `postcard.deleted` | Fires when a postcard is cancelled before printing. Enabled in test mode. |
| Postcard Created | `postcard.created` | Fires when a postcard is created. Enabled in test mode. |
| Postcard Delivered | `postcard.delivered` | Fires when USPS reports the postcard delivered. Live mode only. |
| Postcard Failed | `postcard.failed` | Fires when a postcard fails to render or print. Enabled in test mode. |
| Postcard In Local Area | `postcard.in_local_area` | Fires when USPS reports the postcard in the recipient's local area. Live mode only. |
| Postcard In Transit | `postcard.in_transit` | Fires when USPS reports the postcard in transit. Live mode only. |
| Postcard Informed Delivery Email Clicked | `postcard.informed_delivery.email_clicked_through` | Fires when the recipient clicks through the Informed Delivery email. Live mode only. |
| Postcard Informed Delivery Email Opened | `postcard.informed_delivery.email_opened` | Fires when the recipient opens the Informed Delivery email. Live mode only. |
| Postcard Informed Delivery Email Sent | `postcard.informed_delivery.email_sent` | Fires when USPS sends the Informed Delivery email for the postcard. Live mode only. |
| Postcard International Exit | `postcard.international_exit` | Fires when the postcard leaves the country of origin. Live mode only. |
| Postcard PDF Rendered | `postcard.rendered_pdf` | Fires when a postcard's print-ready PDF has been rendered. Enabled in test mode. |
| Postcard Processed For Delivery | `postcard.processed_for_delivery` | Fires when USPS processes the postcard for delivery. Live mode only. |
| Postcard Re-Routed | `postcard.re-routed` | Fires when USPS re-routes the postcard. Live mode only. |
| Postcard Rejected | `postcard.rejected` | Fires when a postcard is rejected during production. Enabled in test mode. |
| Postcard Returned To Sender | `postcard.returned_to_sender` | Fires when USPS returns the postcard to sender. Live mode only. |
| Postcard Thumbnails Rendered | `postcard.rendered_thumbnails` | Fires when a postcard's preview thumbnails have been rendered. Enabled in test mode. |
| Postcard Tracking Page Viewed | `postcard.viewed` | Fires when the recipient opens the postcard's tracking page. Enabled in test mode. |
