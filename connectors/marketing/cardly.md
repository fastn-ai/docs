---
description: "Cardly is a print-and-post greeting card platform."
hidden: true
---

# Cardly

<img src="../../.gitbook/assets/connectors/cardly.png" alt="Cardly logo" width="64">

Cardly is a print-and-post greeting card platform. Use this connector to manage artwork, contact lists and contacts, generate card previews, place card orders, manage organisation users and invitations, inspect account credit balance and history, and register webhooks for order and delivery events. Wraps the Cardly v2 REST API at https://api.card.ly/v2.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [card.ly](https://card.ly) |
| **Authentication** | API key |
| **Slug** | `cardly` |

## Use it

Add Cardly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cardly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Artwork | `createArtwork` | Upload a new piece of card artwork to your Cardly organisation. Each page image must be a base64-encoded image at the exact pixel size the chosen media requires; Cardly returns a 422 naming the required size if it does not match. For A4 Letter media the required size is 3401x4771 pixels. |
| Create Contact | `createContact` | Add a new contact with a postal address to a Cardly contact list. Region and postcode are conditionally required depending on the country's addressing format. Returns the created contact including its ID. |
| Create Contact List | `createContactList` | Create a new contact list in your Cardly organisation, optionally defining custom fields that each contact in the list can carry. Returns the created list including its ID. |
| Create Invitation | `createInvitation` | Invite a person to join your Cardly organisation by email and grant them a set of permissions that take effect once they accept. Cardly emails the invitee an acceptance link. |
| Create Webhook | `createWebhook` | Register a webhook so Cardly POSTs near-real-time notifications to your URL when the events you subscribe to occur. The response carries the full signing secret, which is only ever returned once, so store it if you intend to verify postback signatures. |
| Delete Artwork | `deleteArtwork` | Permanently delete a piece of artwork from your Cardly organisation. Orders already placed with this artwork are unaffected. |
| Delete Contact | `deleteContact` | Permanently delete a contact from a Cardly contact list by its unique contact ID. This cannot be undone. |
| Delete Contact By Identifier | `deleteContactByIdentifier` | Permanently delete a contact from a Cardly contact list by its email address or your own external identifier, without needing the Cardly contact ID. Supply exactly one of the two. |
| Delete Contact List | `deleteContactList` | Permanently delete a Cardly contact list and every contact it holds. This cannot be undone, so confirm the list ID before calling. |
| Delete Invitation | `deleteInvitation` | Revoke a pending Cardly organisation invitation by its unique ID. The acceptance link stops working immediately. |

<details>

<summary>See 38 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Invitation By Email | `deleteInvitationByEmail` | Revoke a pending Cardly organisation invitation by the email address it was sent to, without needing the invitation ID. |
| Delete User | `deleteUser` | Revoke a user's access to your Cardly organisation by their unique user ID. The call succeeds with an empty data object whether or not a matching user existed, so confirm the user first with Retrieve User. Do not call this for the only administrator, as that would lock the organisation out. |
| Delete User By Email | `deleteUserByEmail` | Revoke a user's access to your Cardly organisation by their email address. The call succeeds with an empty data object whether or not a matching user existed, so confirm the user first with Find User. Do not call this for the only administrator, as that would lock the organisation out. |
| Delete Webhook | `deleteWebhook` | Permanently delete a Cardly webhook by its unique ID so it stops receiving event postbacks. Take care with webhooks flagged protected, as they were created by a third party such as Zapier. |
| Echo Request | `echoRequest` | Send a request to Cardly's diagnostic echo endpoint and have the method, URL, query string, headers and body returned to you. Useful for validating connectivity and authentication without touching account data or consuming credits. Cardly masks the API-Key header in the reflected output. |
| Edit Artwork | `editArtwork` | Update the name, description or page images of an existing piece of Cardly artwork. Supplying new page images creates a new revision of the artwork. At least one of name, description or artwork must be supplied. |
| Edit Contact | `editContact` | Replace the details of an existing contact in a Cardly contact list. This is a full replace, not a merge: any optional field you omit, such as externalId, email, company or address2, is cleared on the stored contact. Send every value you want to keep. |
| Find Invitation | `findInvitation` | Find a Cardly organisation invitation by the email address it was sent to. Returns the matching invitation, or a 404 when no invitation exists for that address. |
| Find User | `findUser` | Find a Cardly organisation user by their email address. Returns the matching user, or a 404 when no user in the organisation has that address. |
| Generate Order Preview | `previewOrder` | Generate a preview of a single card before ordering it. Returns the credit cost, the estimated dispatch and delivery window, and temporary PDF URLs for the rendered card and envelope. No card is printed and no credits are consumed, so use this to validate artwork, message and address before calling Place Order. |
| List Artwork | `listArtwork` | List the card artwork available to your Cardly organisation, including both your own uploaded artwork and artwork shared with you. Use the returned artwork ID when generating a preview or placing an order. |
| List Contact Lists | `listContactLists` | List the contact lists in your Cardly organisation, with contact counts, custom field definitions and address validation status for each. |
| List Contacts | `listContacts` | List the contacts stored in a Cardly contact list, with their postal addresses, custom field values and address validation state. |
| List Credit History | `listCreditHistory` | List card credit history records for your Cardly organisation, including both credits and debits with the reason for each. Supports paging and filtering by effective time. |
| List Doodles | `listDoodles` | List the doodles (small hand-drawn illustrations) available to add to a Cardly card message. Returns each doodle's ID, slug, preview image path and pixel dimensions. |
| List Fonts | `listFonts` | List the handwriting and print fonts available for Cardly card messages. Use a returned font ID in the style object of a preview or order to set the message typeface. |
| List Gift Credit History | `listGiftCreditHistory` | List gift credit history records for your Cardly organisation, including both credits and debits with the reason for each. Gift credit is the monetary balance used to fund gift cards attached to orders. |
| List Invitations | `listInvitations` | List the invitations sent to join your Cardly organisation. Accepted invitations are filtered out by default; use the filters to include or isolate accepted or expired invitations. |
| List Media | `listMedia` | List the physical card media formats Cardly can print, such as A4 Letter, Portrait Card, Landscape Notecard and Postcard. The returned media ID is required when creating artwork. |
| List Orders | `listOrders` | List the card orders placed on your Cardly organisation, with their status, origin, costs, timings and line items. |
| List Templates | `listTemplates` | List the reusable card message templates saved in your Cardly organisation. Use a returned template ID when generating a preview or placing an order so the saved copy, styling and variables are applied. |
| List Users | `listUsers` | List the users who have accepted an invitation to your Cardly organisation, with their status and permission flags. |
| List Webhooks | `listWebhooks` | List the webhooks registered on your Cardly organisation, with their target URL, subscribed events, status and delivery statistics. Webhook secrets are masked in this listing. |
| List Writing Styles | `listWritingStyles` | List the handwriting styles Cardly can apply to a card message, from neat to natural. Use a returned writing style ID in the style object of a preview or order. |
| Place Order | `placeOrder` | Place a real Cardly order. Every line is physically printed, enveloped and posted to the recipient, and card credits are deducted from your organisation immediately. There is no undo. Validate the payload with Generate Order Preview first, and use a test-mode API key (prefixed test_) to exercise this endpoint without printing or posting anything. |
| Resend Invitation | `resendInvitation` | Resend a pending Cardly organisation invitation email by the invitation's unique ID. Returns the refreshed invitation record. |
| Resend Invitation By Email | `resendInvitationByEmail` | Resend a pending Cardly organisation invitation email by the address it was sent to, without needing the invitation ID. Returns the refreshed invitation record. |
| Retrieve Account Balance | `getAccountBalance` | Retrieve the current card credit balance and gift credit balance for your Cardly organisation. Use this before placing an order to confirm enough credits are available, since each card consumes credits. |
| Retrieve Artwork | `getArtwork` | Retrieve full details for a single piece of Cardly artwork by its unique ID, including the media format it targets, its current revision and the rendered page image URLs. |
| Retrieve Contact | `getContact` | Retrieve a single contact from a Cardly contact list by its unique contact ID, including the full postal address and custom field values. |
| Retrieve Contact List | `getContactList` | Retrieve a single Cardly contact list by its unique ID, including its custom field definitions, contact counts and address validation summary. |
| Retrieve Invitation | `getInvitation` | Retrieve a single Cardly organisation invitation by its unique ID, including its status, granted permissions, expiry and acceptance link. |
| Retrieve Order | `getOrder` | Retrieve a single Cardly card order by its unique ID, including overall costs and timings plus each line item's recipient, sender, delivery estimate and tracking details. |
| Retrieve User | `getUser` | Retrieve a single Cardly organisation user by their unique ID, including status and permission flags. |
| Retrieve Webhook | `getWebhook` | Retrieve a single Cardly webhook by its unique ID, including its target URL, subscribed events, status and delivery statistics. The signing secret is masked. |
| Search Contacts | `searchContacts` | Find a single contact inside a Cardly contact list by its email address or your own external identifier. Returns the matching contact, or a 404 when nothing in the list matches. |
| Sync Contact | `syncContact` | Upsert a contact into a Cardly contact list: the contact is matched on externalId or email and updated if it already exists, or created if it does not. At least one of externalId or email must be supplied. |
| Update Webhook | `updateWebhook` | Update an existing Cardly webhook's target URL, subscribed events, description or metadata, or enable and disable it. The events list replaces the current subscription rather than adding to it. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Card Order Created | `contact.order.created` | Fires when a card order is created for a contact. Cardly does not publish the postback payload shape anywhere in its v2 API documentation, and no delivery could be captured during build because emitting one requires placing a billable order, so no payloadSchema is declared. Capture one real delivery and add the schema before relying on field paths. |
| Card Order Refunded | `contact.order.refunded` | Fires when a contact's card order is refunded. Payload shape is not documented by Cardly and was not captured during build, so no payloadSchema is declared. |
| Card Order Sent | `contact.order.sent` | Fires when a contact's card has been printed and dispatched. Payload shape is not documented by Cardly and was not captured during build, so no payloadSchema is declared. |
| Consignment Change Of Address | `consignment.changeOfAddress` | Fires when a change of address is reported against a consignment. Payload shape is not documented by Cardly and was not captured during build, so no payloadSchema is declared. |
| Consignment Undeliverable | `consignment.undeliverable` | Fires when a consignment is returned as undeliverable. Payload shape is not documented by Cardly and was not captured during build, so no payloadSchema is declared. |
| Contact Change Of Address | `contact.changeOfAddress` | Fires when the postal service reports a change of address for a contact, so you can update your own records. Payload shape is not documented by Cardly and was not captured during build, so no payloadSchema is declared. |
| Contact Undeliverable | `contact.undeliverable` | Fires when mail addressed to a contact is returned as undeliverable. Payload shape is not documented by Cardly and was not captured during build, so no payloadSchema is declared. |
| Gift Card Redeemed | `giftCard.redeemed` | Fires when a gift card attached to one of your cards is redeemed by its recipient. Payload shape is not documented by Cardly and was not captured during build, so no payloadSchema is declared. |
| QR Code Scanned | `qrCode.scanned` | Fires when a QR code printed on one of your cards is scanned. Payload shape is not documented by Cardly and was not captured during build, so no payloadSchema is declared. |
