---
description: "thanks.io is a direct-mail automation platform for sending handwritten-style postcards, letters, notecards, magnacards and gift cards."
---

# thanks.io

thanks.io is a direct-mail automation platform for sending handwritten-style postcards, letters, notecards, magnacards and gift cards. This connector covers the full thanks.io v2 REST API: recipients, mailing lists and radius search, the six send-mailer endpoints, orders with tracking, items, cancel and replay, message and image templates, sub-accounts, handwriting styles, gift card brands, image building and webhooks.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [thanks.io](https://thanks.io) |
| **Authentication** | Credentials you enter |
| **Actions** | 44 |
| **Events** | 4 |
| **Slug** | `thanksIo` |

## Use it

Add thanks.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.thanksIo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Build Image Template | `buildImageTemplate` | Renders a dynamic image from one of thanks.io's built-in dynamic layouts, merging header and sub-header text, a logo, a background and a trackable QR code, and returns the rendered PNG. It does not create an order - upload the PNG and pass its URL as Front Image URL on a send endpoint. Text fields accept dynamic tags, the background accepts ~MAP_VIEW~ and the logo accepts ~YOUR_LOGO~ or ~YOUR_SYMBOL~. |
| Buy Radius Search | `buyRadiusSearch` | Buys a nearest-neighbour mailing list around an address and adds it to the account. This charges the account $0.05 per record the moment it is bought and cannot be cancelled, so treat it as a purchase. While API Test Mode is on, a purchase through this endpoint is capped at 5 records. |
| Cancel Order | `cancelOrder` | Cancels an order that is still in Reviewing status and refunds its credits to the account. Orders that have moved further into fulfillment cannot be cancelled. |
| Create Mailing List | `createMailingList` | Creates a new manual mailing list. If a QR code URL is supplied it becomes the default QR code URL for orders placed against this list. |
| Create Message Template | `createMessageTemplate` | Creates a reusable message template for a given mailer type, including its handwriting style, colour, QR code and, for gift cards, the brand and amount. |
| Create Multiple Recipients | `createMultipleRecipients` | Adds many recipients at once. The request body is a top-level JSON array, so pass the recipients as a JSON string, for example [{"mailing_list":1,"name":"Jane Doe","address":"987 Main Street","city":"Lenexa","province":"KS","postal_code":"66216","country":"US"}]. Each entry needs a mailing list plus either a mailing address or an email address. The response repeats each recipient and adds an error field to any that could not be added. |
| Create Recipient | `createRecipient` | Adds a single recipient to a mailing list. Supply either a full mailing address or an email address; if only an email is supplied thanks.io can look up a street address for an additional fee. |
| Create Sub-Account | `createSubAccount` | Creates a sub-account with its own return address, so an agency can keep a client's mailing lists, templates and orders separate. |
| Create Webhook | `createWebhook` | Registers a webhook destination so thanks.io posts real-time events - order status changes, mail piece status changes, deliveries and QR code scans - to your URL. Webhooks are available on paid subscriptions only. |
| Delete Mailing List | `deleteMailingList` | Permanently deletes a mailing list and the recipients it contains. |
| Delete Message Template | `deleteMessageTemplate` | Permanently deletes a message template from the account. |
| Delete Recipient | `deleteRecipient` | Permanently deletes a recipient from its mailing list by recipient id. |
| Delete Recipient By Address | `deleteRecipientByAddress` | Deletes a recipient from a mailing list by matching their mailing address or email address instead of their recipient id. |
| Delete Sub-Account | `deleteSubAccount` | Deletes a sub-account. Its orders and mailing lists are moved to the main account, and its image templates, message templates and campaigns are deleted permanently. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook destination so thanks.io stops posting events to it. Webhooks are available on paid subscriptions only. |
| Get Account | `getAccount` | Returns the thanks.io account the API token belongs to, including the default return address and the current plan. Use it to verify credentials and to read the account's default return address. |
| Get Mailing List | `getMailingList` | Returns a single mailing list by its id, including recipient count, QR scan totals and send totals. |
| Get Message Template | `getMessageTemplate` | Returns a single message template by its id, including its content, handwriting settings and any gift card configuration. |
| Get Recipient | `getRecipient` | Returns a single recipient by its id, including the mailing list it belongs to. |
| Get Sub-Account | `getSubAccount` | Returns a single sub-account by its id, including its return address and branding fields. |
| List Gift Card Brands | `listGiftcardBrands` | Returns the gift card brands available for giftcard mailers, grouped into categories such as Featured and Food, each brand with its supported face values in cents. |
| List Gift Card Brands Flat | `listGiftcardBrandsFlat` | Returns every gift card brand as a single flat array, each entry carrying its category group name. Use this instead of List Gift Card Brands when you want one list to iterate over. |
| List Handwriting Styles | `listHandwritingStyles` | Returns the handwriting styles available for mailers, each with a sample image. Use the returned ids for the Handwriting Style ID field on the send endpoints and on message templates. |
| List Image Templates | `listImageTemplates` | Returns the image templates saved on the account, which can be used as the creative on any send endpoint through the Image Template ID field. |
| List Mailing List Recipients | `listMailingListRecipients` | Returns the recipients on a specific mailing list, optionally limited to those updated since a given date and time. |
| List Mailing Lists | `listMailingLists` | Returns a paginated list of the mailing lists on the account, each with its recipient count, QR scan totals and send totals. |
| List Message Templates | `listMessageTemplates` | Returns the message templates saved on the account, which can be used as the handwritten content on any send endpoint through the Message Template ID field. |
| List Order Items | `listOrderItems` | Returns the individual mail pieces in an order, one entry per recipient, each with its delivery status, delivery date, QR scan count, failure reason and recipient address. |
| List Orders | `listOrders` | Returns recent mail orders with their type, size, recipient counts, credit totals, status and any metadata you attached when sending. |
| List Sub-Accounts | `listSubAccounts` | Returns the sub-accounts on the account. Sub-accounts let an agency keep each client's mailing lists, templates and orders separate under one thanks.io login. |
| List Webhooks | `listWebhooks` | Returns the webhook destinations configured on the account, each with its event type, target URL, HTTP verb and invocation count. Webhooks are available on paid subscriptions only. |
| Preview Handwriting | `previewHandwriting` | Renders a message in a handwriting style and returns the URL of the generated handwriting image, without creating an order. Use it to show customers what their message will look like before they send. This endpoint is live on the thanks.io API but is not covered by the published OpenAPI specification. |
| Replay Order | `replayOrder` | Submits a copy of a previous order as a brand-new order, charging and mailing the same creative again while leaving the original untouched. By default it goes to the recipients the original actually reached; supply Recipients to send the same creative to a different audience. This action places a real, chargeable order. |
| Send Giftcard | `sendGiftcard` | Places an order for a folded 4.25x5.5 giftcard in an envelope, carrying a digital gift card from a supported brand. Use List Gift Card Brands for valid brand codes and amounts. Set Preview to true to have thanks.io return preview images instead of placing a real order - this charges nothing and mails nothing. |
| Send Magnacard | `sendMagnacard` | Places an order for a magnacard - a postcard with a detachable magnet. Choose the audience with Mailing List IDs, Recipients or Radius Search. Set Preview to true to have thanks.io return preview images instead of placing a real order - this charges nothing and mails nothing. |
| Send Notecard | `sendNotecard` | Places an order for a folded 4.25x5.5 notecard in an envelope. The creative sets the exterior and the message is handwritten on the interior. Set Preview to true to have thanks.io return preview images instead of placing a real order - this charges nothing and mails nothing. |
| Send Postcard | `sendPostcard` | Places an order for a 4x6, 6x9 or 6x11 postcard. Choose the audience with Mailing List IDs, Recipients or Radius Search, and the creative with an image template or a front image URL. Set Preview to true to have thanks.io return preview images instead of placing a real order - this charges nothing and mails nothing. |
| Send Windowed Letter | `sendWindowedLetter` | Places an order for a letter in a windowed envelope. Supply a cover-letter message or a message template, and optionally extra PDF pages or a PDF that replaces the cover letter entirely. Set Preview to true to have thanks.io return preview images instead of placing a real order - this charges nothing and mails nothing. |
| Send Windowless Letter | `sendWindowlessLetter` | Places an order for a letter in a windowless envelope, where the recipient address is printed on the envelope rather than showing through a window. Set Preview to true to have thanks.io return preview images instead of placing a real order - this charges nothing and mails nothing. |
| Track Order | `trackOrder` | Returns a delivery summary for an order as aggregate counts per status - delivered, in transit, returned to sender, failed and QR scans. Use List Order Items instead when you need per-mailpiece detail. |
| Update Message Template | `updateMessageTemplate` | Updates an existing message template. Only the fields supplied are sent, so untouched settings keep their current values. |
| Update Recipient | `updateRecipient` | Updates the details of an existing recipient. Only the fields supplied are sent, so untouched fields keep their current values. |
| Update Sub-Account | `updateSubAccount` | Updates a sub-account's title and return address. Branding can only be changed in the thanks.io dashboard. |
| Update Webhook | `updateWebhook` | Updates an existing webhook destination's URL, event type, HTTP verb or description. Webhooks are available on paid subscriptions only. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Order Item Delivered | `order_item.delivered` | Fires when an individual mail piece is confirmed delivered. Use it to trigger follow-up workflows on final delivery. Payload shape is modelled from the thanks.io Order Item Delivered documentation; no delivery was captured because webhooks require a paid thanks.io plan. |
| Order Item Status Change | `order_item.status_update` | Fires whenever an individual mail piece changes delivery status, for example In Transit or Returned To Sender. Use it to track USPS progress per recipient. Payload shape is modelled from the thanks.io Order Item Status Change documentation; no delivery was captured because webhooks require a paid thanks.io plan. |
| Order Status Change | `order.status_update` | Fires whenever an order changes status, for example from Reviewing to Fulfilled or Cancelled. The payload carries the order together with the metadata object you supplied when sending, as order.metadata. Payload shape is modelled from the thanks.io Order Status Change documentation; no delivery was captured because webhooks require a paid thanks.io plan. |
| QR Code Scan | `scans.scan_update` | Fires whenever a recipient scans the trackable QR code printed on one of your mailers. Payload shape is modelled from the thanks.io QR Code Scans documentation; no delivery was captured because webhooks require a paid thanks.io plan. |
