---
description: "Postalytics is a direct mail automation platform for sending trackable postcards, letters and self-mailers triggered from marketing and CRM workflows."
hidden: true
---

# Postalytics

<img src="../../.gitbook/assets/connectors/lg/postalytics.png" alt="Postalytics logo">

Postalytics is a direct mail automation platform for sending trackable postcards, letters and self-mailers triggered from marketing and CRM workflows. This connector covers the full Postalytics REST API (v1): accounts and agency sub-accounts, auto-login links, integrations, campaigns and their stats and delivery events, triggered drip sends, multi-touch flows, contact lists and contacts, suppression lists, mail piece templates, and campaign webhooks. Authenticates with the account API key over HTTP Basic auth.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [postalytics.com](https://postalytics.com) |
| **Authentication** | Basic auth |
| **Slug** | `postalytics` |

## Use it

Add Postalytics from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.postalytics.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Account | `createAccount` | Creates a new Postalytics sub-account under the authenticated (agency) account. The response contains the new account id and its API key; store both to make calls on behalf of the sub-account. |
| Create Campaign | `createCampaign` | Creates a new triggered drip direct mail campaign in Postalytics from an existing template, with the media type, postage class and sender return address. The campaign starts in test mode; nothing is mailed until it is set live and mail is sent. Returns the campaign drop id. |
| Create Contact | `createContact` | Adds a new contact with a mailing address and optional personalization fields to a Postalytics contact list. Adding a contact does not mail anything by itself. The response only confirms the creation time; use List Contacts On List to get the new contact id. |
| Create Login Link | `createLoginLink` | Creates a short-lived auto-login URL for a Postalytics account that signs the user in and redirects to a chosen app page, such as the dashboard, template editor, contact import or a specific campaign. Use the link immediately; it expires quickly. |
| Create Suppression List | `createSuppressionList` | Creates a new suppression list in Postalytics, used in campaigns to stop mail going to the contacts on it. Add contacts afterwards with Create Suppression List Contact. |
| Create Suppression List Contact | `createSuppressionListContact` | Adds a contact to a Postalytics suppression list so campaigns using that list will not mail them. Postalytics standardizes the address and returns the list details and the stored contact, including its data id. |
| Create Template | `createTemplate` | Creates a direct mail piece template in Postalytics, either from full-size front and back background image URLs or from full HTML that follows Postalytics template standards. Returns the new template id. |
| Create Webhook | `createWebhook` | Creates the outgoing webhook for a Postalytics campaign so campaign mail tracking events are posted to your URL. Each campaign has one webhook, identified by the campaign drop id. Which events are delivered is chosen by editing the webhook in the Postalytics app. Requires a Pro or higher subscription. |
| Delete Account | `deleteAccount` | Permanently deletes a Postalytics sub-account or sub-user account together with all of its campaigns, templates and lists. Parent accounts cannot be deleted through the API. |
| Delete Campaign | `deleteCampaign` | Deletes a Postalytics campaign by drop id. The contact list created with the campaign is not removed. |

<details>

<summary>See 35 more actions</summary>

* **Delete Contact** `deleteContact`: Deletes a contact from its Postalytics contact list.
* **Delete Suppression List** `deleteSuppressionList`: Deletes a Postalytics suppression list. Returns a confirmation message.
* **Delete Suppression List Contact** `deleteSuppressionListContact`: Removes a contact from a Postalytics suppression list. Returns a confirmation message.
* **Delete Template** `deleteTemplate`: Deletes a Postalytics mail piece template by id.
* **Delete Webhook** `deleteWebhook`: Deletes the webhook of a Postalytics campaign so its mail tracking events are no longer posted.
* **Enroll Contact In Flow** `enrollContactInFlow`: Enrolls a recipient in a Postalytics multi-touch Flow so they receive its scheduled direct mail touches. For an active flow this produces real, billable physical mail. Returns the flow details and the enrollment date.
* **Get Account** `getAccount`: Retrieves a Postalytics account by account id, such as an agency sub-account, including username, API key, contact details and address. The password is never returned.
* **Get Campaign** `getCampaign`: Retrieves basic information for a Postalytics campaign by drop id: name, send endpoint id, status and the contact list the campaign mails to. Use Get Campaign Stats for delivery statistics.
* **Get Campaign Stats** `getCampaignStats`: Retrieves delivery and engagement statistics for a single Postalytics campaign by drop id, including audience, in transit, delivered and returned counts, pURL visits, conversions, campaign type, live mode and status.
* **Get Contact** `getContact`: Retrieves a Postalytics contact by id, including mailing address, address validity, contact details, personalized URL and QR code, list id and custom fields.
* **Get Flow** `getFlow`: Retrieves a Postalytics multi-touch Flow by its endpoint id, with its name, contact list, active flag and dates.
* **Get My Account** `getMyAccount`: Retrieves the account profile of the authenticated Postalytics API key, including account id, username, contact details and address. The password is never returned.
* **Get Suppression List** `getSuppressionList`: Retrieves a single Postalytics suppression list by id, with its name, contact total, country and creation date.
* **Get Suppression List Contact** `getSuppressionListContact`: Retrieves a single contact on a Postalytics suppression list by its data id, together with the list details.
* **Get Template** `getTemplate`: Retrieves a Postalytics mail piece template by id, including its name, size, generated HTML, background images, proofing flag and preview thumbnails.
* **Get Webhook** `getWebhook`: Retrieves the webhook of a Postalytics campaign by webhook id (the campaign drop id), including its target URL and active flag.
* **List Campaign Events** `listCampaignEvents`: Lists the most recent mail tracking events for a Postalytics campaign, paged, such as Mail Piece Created, Addressed, Mailed, In Transit, In Local Area, Processed for Delivery, Returned To Sender, Re-Routed and pURL Opened. Postalytics returns HTTP 400 "Campaign events not found" when the campaign has no events yet.
* **List Campaigns** `listCampaigns`: Lists all direct mail campaigns in the Postalytics account with their delivery stats (audience, in transit, delivered, returned), engagement stats, type, live mode and status. Postalytics returns HTTP 400 "Campaign not found" when the account has no campaigns.
* **List Contact Campaign Events** `listContactCampaignEvents`: Lists the most recent mail tracking events for one contact within a Postalytics campaign, paged, such as Mailed, In Transit, Processed for Delivery, Returned To Sender and pURL Opened.
* **List Contact Lists** `listContactLists`: Lists all contact lists in the Postalytics account with their id, name, contact count and creation date.
* **List Contacts On List** `listContactsOnList`: Lists the contacts on a Postalytics contact list, starting at a given row with up to 100 contacts per call, including address, contact details and custom fields. Postalytics returns HTTP 400 "No contacts received" when the list is empty.
* **List Drip Campaigns** `listDripCampaigns`: Lists all triggered drip campaigns in the Postalytics account with their name and send endpoint id, which Send Mail uses to mail a piece to a recipient.
* **List Flows** `listFlows`: Lists all multi-touch Flows in the Postalytics account with their id, endpoint id, name, contact list, active flag and dates.
* **List Integrations** `listIntegrations`: Lists the Postalytics Connect integrations (CRM and marketing platform connections) set up by the authenticated user, with display name, integration name, plugin ids and whether each is a marketplace app. KNOWN VENDOR BUG (verified 2026-09-21): GET /api/v1/account/integrations is documented but unreachable — the literal segment "integrations" is swallowed by the GET /api/v1/account/{id} route, so the API answers 400 {"errors":{"id":["The value 'integrations' is not valid."]}}. No alternative path exists (/integrations, /account/me/integrations and /account/{id}/integrations all 404). This action matches the vendor documentation and will start working once Postalytics fixes its route ordering.
* **List Suppression List Contacts** `listSuppressionListContacts`: Lists the contacts on a Postalytics suppression list together with the list details, with an offset for paging.
* **List Suppression Lists** `listSuppressionLists`: Lists all suppression lists in the Postalytics account with their id, name, contact total, country and creation date. To fetch a single list use Get Suppression List (the documented id query filter is ignored by the API).
* **List Templates** `listTemplates`: Lists all mail piece templates in the Postalytics account with their id, name, size, HTML, proofing flag and preview thumbnails. Postalytics returns HTTP 400 "Template not found" when the account has no templates.
* **List Webhooks** `listWebhooks`: Lists all campaign webhooks in the Postalytics account with their campaign, target URL, active flag and send endpoint.
* **Send Mail** `sendMail`: Sends a direct mail piece from a Postalytics triggered drip campaign to one recipient. When the campaign is live this produces real, billable physical mail; in test mode no mail is printed. Returns the send date of the created mail piece.
* **Toggle Campaign Live Mode** `toggleCampaignLiveMode`: Switches a Postalytics triggered drip or automated file campaign between test mode and live mode. In live mode, sends to the campaign produce real, billable physical mail.
* **Unenroll Contact From Flow** `unenrollContactFromFlow`: Removes an enrolled contact from a Postalytics multi-touch Flow so no further touches are mailed to them. Returns the unenrollment date.
* **Update Account** `updateAccount`: Updates an existing Postalytics account, either a standalone account or an agency sub-account, including its login username and password, contact details and address.
* **Update Contact** `updateContact`: Updates an existing contact on a Postalytics contact list. Send contact_id and contact_list_id plus any fields to change. KNOWN VENDOR BUG (verified 2026-09-21): PUT /api/v1/contacts always answers 400 "Error updating contact -An unexpected error occurred. Reference: &lt;id&gt;" for a contact that exists, while a non-existent contact_id answers the shorter 400 "Validation error" — so the vendor resolves the contact and then throws inside its own update handler. The request body shape is correct (the API names UpdateContactRequest as the model it binds). Nothing on the connector side fixes this; delete and re-create the contact as a workaround.
* **Update Suppression List Contact** `updateSuppressionListContact`: Replaces the non-address details of a contact on a Postalytics suppression list: name, company, country, email, phone, occupation, website and custom fields. Fields you omit are cleared, so pass every value you want to keep. Address fields cannot be changed; delete and re-add the contact to change its address. Returns the list details and the updated contact.
* **Update Webhook** `updateWebhook`: Updates the webhook of a Postalytics campaign: change the receiving URL or turn event delivery on or off.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Campaign Mail Tracking Event | `campaign_mail_event` | Fires for mail piece tracking events of one Postalytics campaign. Postalytics allows exactly one webhook URL per campaign (identified by the campaign drop id, passed as the dropId input), so all event types for that campaign arrive at the same trigger; the integer eventType field tells them apart: 0 Created, 9 Addressed, 10 Printed, 11 Mailed, 4 In Transit, 5 In Local Area, 6 Processed for Delivery, 2 Re-Routed, 3 Return to Sender, 7 pURL Opened, 8 pURL Completed. Which event types are sent is chosen in the Postalytics app: Username menu &gt; Webhooks &gt; edit (pen icon) on the campaign. Requires a Pro or higher plan. Postalytics does not sign deliveries. The schema below follows the Postalytics webhook documentation (Basic Information, To, From, Piece and Meta sections); field names inside To, From and Piece are not documented and it has not been reconciled against a live delivery, because deliveries only occur for mailed pieces. |
