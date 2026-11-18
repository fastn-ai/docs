---
description: "Handwrytten sends real handwritten notes and cards on your behalf, written by robots holding real pens."
hidden: true
---

# Handwrytten

<img src="../../.gitbook/assets/connectors/lg/handwrytten.png" alt="Handwrytten logo">

Handwrytten sends real handwritten notes and cards on your behalf, written by robots holding real pens. This connector covers the Handwrytten v2 API: the card, font, template, insert, bundle, gift-card and stamp catalogue, custom card design and QR codes, sender and recipient address books, basket and order management, outbound prospecting, and account, credit-card and subscription information.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [handwrytten.com](https://handwrytten.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `handwrytten` |

## Use it

Add Handwrytten from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.handwrytten.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Order To Basket | `addOrderToBasket` | Adds a note to the account's basket for one saved recipient, a list of saved recipients, or a batch of addresses supplied inline. Nothing is charged or mailed until Send Basket is called. |
| Add Recipient Address | `addRecipientAddress` | Saves a recipient in the account's address book and returns its address id, so later orders can reference the contact instead of repeating the full address. |
| Add Sender Address | `addSenderAddress` | Saves a return address on the account and returns the created address record. Use its id as the Return Address ID when placing an order. |
| Calculate Outbound Targets | `calculateOutboundTargets` | Counts how many residential or business prospects match a geographic and demographic search, so an outbound handwritten-note campaign can be sized before it is ordered. Supply exactly one search locus - Postal Code, City, Address or a Latitude/Longitude pair - because Handwrytten rejects the request with 'Please fill out the form before continuing' when several are combined. Counting targets does not create an order and does not charge the account. |
| Cancel Order | `cancelOrder` | Cancels an order that has not yet been written and mailed. Orders already in production cannot be cancelled. |
| Check Authentication | `checkAuthentication` | Confirms that the stored Handwrytten API key is valid and reports the login it belongs to, whether a password is set, the last sign-in method and whether the account is in test mode. |
| Check Custom Image Quality | `checkCustomImageQuality` | Checks whether an uploaded logo or cover image is high enough resolution to print well on a given card, returning a warning or an error before the design is used. |
| Clear Basket | `clearBasket` | Empties the account's basket, discarding every order in it before payment, and returns the items that were removed. |
| Create Custom Card | `createCustomCard` | Designs a branded card from an uploaded or preset cover image plus header, footer, inside and back text or logos, and saves it to the account's private Custom Cards category. Set Is Update with a Card ID to change an existing design. |
| Create Outbound Order | `createOutboundOrder` | Places an outbound prospecting campaign into the basket: Handwrytten buys the matching prospect addresses and queues a handwritten note for each. The basket is charged and mailed when Send Basket is called. |

<details>

<summary>See 48 more actions</summary>

* **Create QR Code** `createQrCode`: Creates a trackable QR code that redirects to the URL you supply and returns its id, ready to be placed on a custom card design.
* **Create Single Step Order** `createSingleStepOrder`: Creates and immediately submits a handwritten note in one call, supplying the card, message, handwriting style and both addresses inline. This charges the account and physically mails a real letter.
* **Delete Custom Card** `deleteCustomCard`: Deletes a custom card design from the account's private Custom Cards category.
* **Delete Custom Image** `deleteCustomImage`: Deletes an uploaded logo or cover image from the account's custom image library.
* **Delete QR Code** `deleteQrCode`: Permanently deletes a QR code from the account. Cards already printed with this code will no longer redirect.
* **Delete Recipient Address** `deleteRecipientAddress`: Removes one or several recipients from the account's address book. Supply either a single address id or a list of ids.
* **Delete Sender Address** `deleteSenderAddress`: Removes one or several return addresses from the account. Supply Address IDs; the single Address ID form currently fails inside Handwrytten with a 500 (WHERE parameter "return_address_id" has invalid "undefined" value), so pass a one-element list instead.
* **Get Basket Count** `getBasketCount`: Returns how many orders are currently waiting in the account's basket, before they are paid for and sent.
* **Get Card** `getCard`: Retrieves the full detail of one Handwrytten card, including its price, physical dimensions, writable margins, character limit and front, inside, envelope and back images.
* **Get Default Sender And Billing Info** `getBillingInfo`: Returns the account's default return address together with the billing address held on file. Use it to find the Return Address ID that orders fall back to.
* **Get Message Template** `getTemplate`: Retrieves one saved message template by id, returning its full body, closing wishes and any signatures attached to it.
* **Get Order** `getOrder`: Retrieves one order in full, including the message written, the handwriting style used, the sender and recipient addresses and the current status.
* **Get QR Code Statistics** `getQrCodeStatistics`: Returns scan analytics for the account's QR codes: totals, a daily scan chart and the most recent scans with their approximate location and the card they came from.
* **Get User Info** `getUser`: Retrieves the profile of the Handwrytten account the API key belongs to, including the account id, display name, e-mail, remaining credits and enabled features.
* **List Bundles** `listBundles`: Lists the gift bundles, such as cookie boxes, that can be shipped alongside a handwritten note, with their price, weight and remaining stock.
* **List Card Dimensions** `listCardDimensions`: Lists the card sizes and formats available for a custom design, such as A7 flat landscape or A2 folded portrait. Pass the chosen id as Dimension ID on Create Custom Card.
* **List Cards** `listCards`: Lists the Handwrytten cards available to the account, optionally filtered to one category and paged. Use the returned card id when placing an order or designing a custom card.
* **List Cards By Category** `listCardsByCategory`: Lists the available Handwrytten cards grouped into their categories, so a whole catalogue section can be rendered in one call. This endpoint always returns every section; to fetch one category's cards use List Cards with its Category ID.
* **List Categories** `listCategories`: Lists the card categories available to the account, such as Thank You, Birthday and Holiday, for use as the Category ID filter on List Cards.
* **List Countries** `listCountries`: Lists every country Handwrytten can deliver to, with the country id used on address records and the per-piece international delivery cost.
* **List Credit Cards** `listCreditCards`: Lists the payment cards stored on the account, together with the prepaid credit balances that orders can draw on. Use a card id as the Credit Card ID when sending the basket.
* **List Custom Images** `listCustomImages`: Lists the logo and cover images the account has uploaded for use on custom cards, optionally filtered to one image type.
* **List Customizer Fonts** `listCustomizerFonts`: Lists the typeset fonts available for the header, footer, inside and back text of a custom card design. These are different from the handwriting styles returned by List Fonts; use the ids here for the font fields on Create Custom Card.
* **List Fonts** `listFonts`: Lists the handwriting styles available for the note text, with a sample image and the font's machine name. Use the font label when placing a single-step order and the font id elsewhere.
* **List Gift Cards** `listGiftCards`: Lists the gift cards that can be enclosed with a note, each with the denominations available and their prices. Pass a denomination id when placing the order to include the gift card.
* **List Inserts** `listInserts`: Lists the printed inserts, such as business cards or flyers, that the account has stocked with Handwrytten and can enclose with a note.
* **List Message Templates** `listTemplates`: Lists the saved message templates available to the account, including Handwrytten's stock wording for thank-you, follow-up and holiday notes. Use a template's message as the note body when placing an order.
* **List Notifications** `listNotifications`: Lists the in-app notifications Handwrytten has raised for the account, such as low stock or order problems.
* **List Orders** `listOrders`: Lists the orders placed on the account, newest first, so their progress from queued to mailed can be followed.
* **List Preset Cover Images** `listPresetCoverImages`: Lists Handwrytten's ready-made front and back cover artwork for a given card size, so a custom card can be designed without uploading an image. Pass an id as Preset Cover ID on Create Custom Card.
* **List QR Code Frames** `listQrCodeFrames`: Lists the decorative frames a QR code can be printed inside on a custom card, with each frame's artwork and the position and size of the code within it.
* **List QR Codes** `listQrCodes`: Lists the trackable QR codes saved on the account, each with the destination URL it points to. A QR code can be placed on a custom card so scans are attributed back to the note.
* **List Recipient Addresses** `listRecipientAddresses`: Lists the recipient addresses saved in the account's address book, with the address id to use when sending a note to a saved contact.
* **List Sender Addresses** `listSenderAddresses`: Lists the return addresses saved on the account, with the id to use as the Return Address ID when ordering, and which one the account is forced to use if a return address is enforced.
* **List Shipping Methods** `listShippingMethods`: Lists the shipping methods Handwrytten can use for an order, such as mailing the card normally or shipping it addressed, sealed and stamped back to the sender. Pass the chosen id as Shipping Method ID on the outbound order actions.
* **List Signatures** `listSignatures`: Lists the handwritten signatures saved on the account, with a preview image of each. Pass a signature id when ordering so the note is signed with it.
* **List Stamp Options** `listStampOptions`: Lists the postage options available for US orders, such as First Class or Forever stamps, with their per-piece delivery cost. Pass the chosen id as Stamp Option ID when ordering.
* **List States** `listStates`: Lists the states or provinces of one country, with the two-letter code to use in the State field of an address. Required for United States and Canadian addresses.
* **List Subscription Plans** `listSubscriptions`: Lists the Handwrytten subscription plans, grouped into the ones on offer and the hidden legacy ones, with each plan's price, included cards and per-card rate.
* **List Team Members** `listTeamMembers`: Lists the members of the Handwrytten team the account belongs to. Only accounts on a team plan with administrator rights may call this; others receive a permission error.
* **Log Out** `logOut`: Ends a session created by Sign In With Password. Pass the session token that call returned; the account's API key is unaffected.
* **Preview Outbound Order** `previewOutboundOrder`: Prices an outbound prospecting campaign before it is placed, breaking the total down into cards, postage, inserts, shipping and tax. This is a quote only; nothing is ordered or charged.
* **Send Basket** `sendBasket`: Pays for every order in the basket and releases it for writing and mailing. This charges the account and physically mails the notes, so call it only when the basket has been reviewed.
* **Set Default Sender Address** `setDefaultSenderAddress`: Marks one of the account's saved return addresses as the default, so orders that do not name a return address use it.
* **Set Test Mode** `setTestMode`: Turns the account's test mode on or off. While test mode is on, orders are simulated rather than written, charged and mailed, which makes it the safe way to exercise the ordering endpoints.
* **Sign In With Password** `signInWithPassword`: Exchanges a Handwrytten e-mail address and password for a session token. Most integrations should use an API key instead; this is for flows that sign a user in on their behalf.
* **Update Recipient Address** `updateRecipientAddress`: Updates a saved recipient in the account's address book. Only the fields you supply are changed.
* **Update Sender Address** `updateSenderAddress`: Updates a saved return address on the account and returns the account's addresses after the change.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Order Status Changed | `order_status_change` | Handwrytten reports a change in the state of an order it is writing and mailing. There is no webhook-registration API, so the customer supplies this trigger's URL themselves, in one of two places: per order, as the Webhook URL input on the Create Single Step Order action; or for every order, by setting a default webhook URL in the Handwrytten dashboard under Account &gt; Settings (it is then returned as Default Webhook URL by Get User Info). IMPORTANT: no payload schema is declared because Handwrytten documents none and a real delivery could not be captured - triggering one requires placing an order, which physically mails a card and charges the account. Treat the incoming body as untyped until a live delivery has been inspected. |
