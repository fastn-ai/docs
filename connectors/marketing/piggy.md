---
description: "Piggy (now Leat) is a loyalty, marketing and gift-card platform."
---

# Piggy

Piggy (now Leat) is a loyalty, marketing and gift-card platform. This connector wraps the Piggy/Leat Public API v3: contacts and contact identifiers, loyalty programs, credits, rewards, tiers and perks, promotions and vouchers, gift cards and gift-card transactions, prepaid balances, orders, products and categories, shops, shifts, bookings, visits, forms, automations, portal sessions and webhook subscriptions.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [piggy.eu](https://piggy.eu) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Actions** | 152 |
| **Events** | 27 |
| **Slug** | `piggy` |

## Use it

Add Piggy from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.piggy.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Create Product Categories | `batchCreateProductCategories` | Create several Product Categories in a single call, which is the efficient way to import a catalogue. |
| Batch Create Products | `batchCreateProducts` | Create several Products in a single call, which is the efficient way to import a catalogue. |
| Calculate Credits | `calculateCredits` | Preview how many credits a given unit value would award at a Shop under the account's Loyalty Rules, without creating a Credit Reception. |
| Check Voucher Validity | `checkVoucherValidity` | Check whether a Voucher could be redeemed by a Contact at a Shop, without redeeming it. |
| Claim Anonymous Contact | `claimAnonymousContact` | Turn an anonymous Contact into a regular one by replacing its placeholder email address with the Contact's real email address. |
| Create And Process Order | `createAndProcessOrder` | Create an Order and immediately process it, so the resulting loyalty transaction is created in one call. All monetary amounts are in the currency's lowest denomination, so 34.50 euro is 3450. |
| Create And Process Order Return | `createAndProcessOrderReturn` | Create and immediately process an Order Return, reversing all or part of a previously created Order and the loyalty it earned. |
| Create Anonymous Contact | `createAnonymousContact` | Create a Contact without a real email address, identified by an existing Contact Identifier such as a card number. The Contact Identifier must already exist - create it first with Create Contact Identifier, otherwise Piggy answers 'Contact identifier not found'. The Contact can later be claimed with a real email address. |
| Create Automation Run | `createAutomationRun` | Trigger an Automation for a specific Contact. Optional data is passed into the Automation and can be used by its steps. |
| Create Batch Of Vouchers | `createBatchOfVouchers` | Generate many Vouchers from one Promotion in a single call, between 1 and 500 at a time. |
| Create Booking | `createBooking` | Create a Booking in Piggy as a replica of a reservation made in your own reservation system, linked to a Contact and a Shop. |
| Create Contact | `createContact` | Create a Contact from an email address. Optionally pass a referral code so the new Contact is attributed to Piggy's referral programme. |
| Create Contact Asynchronously | `createContactAsync` | Queue the creation of a Contact from an email address. The call returns immediately and Piggy creates the Contact in the background, which suits high-volume imports. |
| Create Contact Attribute | `createContactAttribute` | Define a new Contact Attribute on the account so extra information can be stored against Contacts. Piggy exposes no delete endpoint for Contact Attributes, so a created attribute is permanent. |
| Create Contact Identifier | `createContactIdentifier` | Create a Contact Identifier such as a loyalty card number, optionally linking it to a Contact straight away. Leave the Contact empty to link it later. |
| Create Credit Reception | `createCreditReception` | Award loyalty credits to a Contact at a Shop. Supply credits to set an exact amount and bypass Loyalty Rules, or unit_value to let the Loyalty Rules calculate the credits. |
| Create Credit Reception Portal Session | `createCreditReceptionPortalSession` | Create a Portal Session whose flow awards loyalty credits to the Contact who identifies themselves at the Shop. |
| Create Custom Attribute | `createCustomAttribute` | Define a new Custom Attribute on a Piggy entity. The name is the immutable internal key; the label is what end users see. Piggy exposes no delete endpoint for Custom Attributes, so a created attribute is permanent. |
| Create Custom Attribute Group | `createCustomAttributeGroup` | Create a Custom Attribute Group for one entity type, so Custom Attributes can be grouped into a labelled section. Piggy exposes no delete endpoint for groups, so a created group is permanent. |
| Create Giftcard | `createGiftcard` | Create a Giftcard in a Giftcard Program. Only digital Giftcards, type 1, can be created through the API. |
| Create Giftcard Transaction | `createGiftcardTransaction` | Change a Giftcard's balance at a Shop. A positive amount tops the card up, a negative amount redeems value from it. |
| Create Loyalty Transaction Attribute | `createLoyaltyTransactionAttribute` | Define a new Loyalty Transaction Attribute so custom data can be attached to Credit Receptions and Reward Receptions. Piggy exposes no delete endpoint for these attributes, so a created attribute is permanent. |
| Create Order | `createOrder` | Create an Order in Piggy as a replica of an order from your webshop, app or point of sale. The Order is not yet processed, so no loyalty transaction is created until you call Process Order. All monetary amounts are in the currency's lowest denomination, so 34.50 euro is 3450. |
| Create Pay Prepaid Portal Session | `createPayPrepaidPortalSession` | Create a Portal Session whose flow lets a Contact settle a purchase from their prepaid balance at the Shop. |
| Create Perk | `createPerk` | Create a Perk that can be attached to Tiers. A Perk is either a boolean benefit or a single-select benefit with labelled options. |
| Create Portal Session | `createPortalSession` | Create a general Portal Session for a Shop, the hosted screen a Contact uses to identify themselves at a kiosk or terminal. |
| Create Prepaid Transaction | `createPrepaidTransaction` | Change a Contact's prepaid balance at a Shop. A positive amount tops the balance up, a negative amount settles a purchase. Identify the Contact by UUID or by Contact Identifier. |
| Create Product | `createProduct` | Create a Product, identified by the unique external identifier it carries in your own catalogue, and optionally place it in one or more Categories. |
| Create Product Category | `createProductCategory` | Create a Product Category, identified by the unique external identifier it carries in your own catalogue. |
| Create Promotion | `createPromotion` | Create a Promotion, the campaign definition Vouchers are issued from. Piggy has no endpoint for deleting a Promotion, so a created Promotion is permanent. This endpoint is live on the Piggy API but is not covered by the published documentation. |
| Create Promotion Attribute | `createPromotionAttribute` | Define a new Promotion Attribute so custom data can be stored on Promotions. Piggy exposes no delete endpoint for Promotion Attributes, so a created attribute is permanent. |
| Create Redeem Giftcard Portal Session | `createRedeemGiftcardPortalSession` | Create a Portal Session whose flow lets a Contact pay the given amount with one or more Giftcards at the Shop. |
| Create Review | `createReview` | Record a Review a Contact left, with its rating and the identifier it carries in your review platform. This endpoint is live on the Piggy API but is not covered by the published documentation. |
| Create Reward | `createReward` | Create a Reward that Contacts can redeem their credits for. Piggy has no endpoint for deleting a Reward, so a created Reward is permanent; deactivate it instead with Update Reward. This endpoint is live on the Piggy API but is not covered by the published documentation. |
| Create Reward Reception | `createRewardReception` | Redeem a Reward for a Contact at a Shop, deducting the Reward's required credits from the Contact's balance. |
| Create Shift | `createShift` | Create a Shift in Piggy as a replica of a shift worked in your own scheduling system. The Shift Team and Shift Type must already exist in the Piggy Business Dashboard - Piggy exposes no API for creating them. |
| Create Top Up Giftcard Portal Session | `createTopUpGiftcardPortalSession` | Create a Portal Session whose flow lets a Contact add value to a Giftcard at the Shop. |
| Create Top Up Prepaid Portal Session | `createTopUpPrepaidPortalSession` | Create a Portal Session whose flow lets a Contact add value to their prepaid balance at the Shop. |
| Create Unit | `createUnit` | Create a new Unit on the account. A Unit is the input value credits are calculated from; its name is immutable after creation. |
| Create Visit | `createVisit` | Register a Visit of a Contact to a Shop, optionally with your own external identifier, source and start and end times. |
| Create Voucher | `createVoucher` | Issue a single Voucher from a Promotion, optionally with your own code, a linked Contact and its own validity window and redemption limit. |
| Create Voucher Portal Session | `createVoucherPortalSession` | Create a Portal Session whose flow lets a Contact redeem a Voucher at the Shop. |
| Create Webhook Subscription | `createWebhookSubscription` | Subscribe to a Piggy webhook event so Piggy posts the event data to your endpoint. Choose V2 for batched deliveries, which Piggy recommends, or V1 for one event per request. |
| Delete Contact | `deleteContact` | Delete a Contact. DEFAULT removes the Contact from the account; GDPR additionally erases the Contact's personal data irreversibly. This cannot be undone. |
| Delete Contact Identifier | `deleteContactIdentifier` | Permanently delete a Contact Identifier by its value. KNOWN VENDOR ISSUE: Piggy answers this route with 500 Server Error, linked or unlinked, for a correctly formed request - reproduced outside fastn. Unlink Contact Identifier works and is the practical alternative. |
| Delete Product | `deleteProduct` | Permanently delete a Product by its UUID. |
| Delete Product Category | `deleteProductCategory` | Permanently delete a Product Category by its UUID. Products previously in the Category are not deleted. |
| Delete Webhook Subscription | `deleteWebhookSubscription` | Delete a Webhook Subscription so Piggy stops posting that event to its target URL. |
| Find Contact By Email | `findContactByEmail` | Look up a single Contact by email address. Returns an error if no Contact with that email exists; use Find Or Create Contact to create one on the fly. |
| Find Contact Identifier | `findContactIdentifier` | Look up a Contact Identifier, such as a loyalty card number, and see which Contact it is linked to. |
| Find Contact Session Token | `findContactSessionToken` | Look up a Contact Session Token to identify and validate the Contact it belongs to before acting on their behalf. |
| Find Giftcard By Hash | `findGiftcardByHash` | Look up a Giftcard by the unique hash printed on the card or encoded in its QR code, which is how a card is identified at the point of sale. |
| Find Or Create Contact | `findOrCreateContact` | Look up a Contact by email address and create it if it does not exist yet, returning the Contact either way. |
| Find Or Create Contact Asynchronously | `findOrCreateContactAsync` | Look up a Contact by email address and queue its creation if it does not exist. The call returns immediately, which suits high-volume imports. |
| Find Or Create Product | `findOrCreateProduct` | Look up a Product by its external identifier and create it if it does not exist yet, returning the Product either way. |
| Find Or Create Product Category | `findOrCreateProductCategory` | Look up a Product Category by its external identifier and create it if it does not exist yet, returning the Category either way. |
| Find Order | `findOrder` | Look up an Order by the unique external identifier it carries in your own system. |
| Find Product | `findProduct` | Look up a Product by the unique external identifier it carries in your own catalogue. |
| Find Product Category | `findProductCategory` | Look up a Product Category by the unique external identifier it carries in your own catalogue. |
| Find Shift By External ID | `findShiftByExternalId` | Look up a Shift by the identifier it carries in your own scheduling system. Piggy serves this lookup over PUT, not GET. |
| Find Voucher By Code | `findVoucherByCode` | Look up a Voucher by the unique code printed on it, which is how a Voucher is identified at the point of sale. |
| Get Brand Kit | `getBrandKit` | Retrieve the account's Brand Kit: the logos, colours and typography that express the company identity across Piggy-hosted pages and emails. |
| Get Client | `getClient` | Retrieve the Piggy/Leat Client (account) that the Personal Access Token belongs to, including its numeric id, UUID and company name. Useful as a connection health check. |
| Get Contact | `getContact` | Retrieve a single Contact by UUID, including its attributes, current Tier and communication subscriptions. |
| Get Contact Auth Token | `getContactAuthToken` | Retrieve an authentication token for a Contact, used to sign that Contact into the Contacts Portal. SECURITY: the response contains a live credential for the Contact - never log, store or forward it. |
| Get Contact Credit Balance | `getContactCreditBalance` | Retrieve a Contact's current loyalty credit balance. |
| Get Contact Identifiers | `getContactIdentifiers` | Retrieve all Contact Identifiers linked to a Contact, such as loyalty card numbers or tokens used to recognise the Contact at the point of sale. |
| Get Contact Prepaid Balance | `getContactPrepaidBalance` | Retrieve a Contact's current prepaid balance, the stored value that can be used to settle purchases or refunds. |
| Get Contact Tier | `getContactTier` | Retrieve the Tier a specific Contact currently belongs to, including the Perks that Tier grants. |
| Get Contacts Portal Authenticated URL | `getContactsPortalAuthUrl` | Generate a pre-authenticated URL that signs a Contact straight into the account's Contacts Portal. SECURITY: the returned URL grants access to that Contact's account, so treat it as a secret and never log or share it. |
| Get Giftcard | `getGiftcard` | Retrieve a single Giftcard by its UUID, including its hash, balance and the Giftcard Program it belongs to. |
| Get Giftcard Transaction | `getGiftcardTransaction` | Retrieve a single Giftcard Transaction by its UUID, including the amount and the Shop it took place at. |
| Get Loyalty Program | `getLoyaltyProgram` | Retrieve the account's Loyalty Program settings, including its name, the maximum credit amount, the custom credit name and the default Unit used to calculate credits. |
| Get Perk | `getPerk` | Retrieve a single Perk by its UUID, including its label, data type and options. |
| Get Portal Session | `getPortalSession` | Retrieve a Portal Session by its UUID to read its current state and the Contact it resolved to. |
| Get Product | `getProduct` | Retrieve a single Product by its UUID, including its Categories. |
| Get Product Category | `getProductCategory` | Retrieve a single Product Category by its UUID. |
| Get Promotion | `getPromotion` | Retrieve a single Promotion by its UUID, including its name, settings and attributes. |
| Get Referral Program Settings | `getReferralProgramSettings` | Retrieve the configuration of the account's referral program, such as whether it is active and what the referring and referred Contacts receive. |
| Get Review | `getReview` | Retrieve a single Review by its UUID. This endpoint is live on the Piggy API but is not covered by the published documentation. |
| Get Reward | `getReward` | Retrieve a single Reward by its UUID, including its title, description and the number of credits required to claim it. |
| Get Shop | `getShop` | Retrieve a single Shop (Business Profile) by its UUID, including its name, type and external reference. |
| Get Visit | `getVisit` | Retrieve a single Visit by its UUID, including the visiting Contact, the Shop and the start and end times. |
| Get Webhook Subscription | `getWebhookSubscription` | Retrieve a single Webhook Subscription by its UUID, including its event type, target URL and status. |
| Link Contact Identifier | `linkContactIdentifier` | Link an existing Contact Identifier to a Contact, so scanning that card or token recognises the Contact. |
| List Automations | `listAutomations` | Retrieve all Automations configured on the account. Automations run predefined sequences of tasks and can be triggered for a Contact with Create Automation Run. |
| List Collectable Rewards | `listCollectableRewards` | Retrieve the physical Rewards a Contact has claimed but not yet collected. |
| List Contact Attributes | `listContactAttributes` | Retrieve the Contact Attributes available on the account, including Piggy's standard attributes such as first name, last name, birthdate, email and phone number. |
| List Contact Offers | `listContactOffers` | Retrieve the offers currently available to a Contact at a Business Profile. This endpoint is live on the Piggy API but is not covered by the published documentation. |
| List Contact Subscriptions | `listContactSubscriptions` | Retrieve the communication Subscription Types a Contact is subscribed to or unsubscribed from, with the current status for each. |
| List Contacts | `listContacts` | Retrieve a paginated list of Contacts, the end users of the loyalty program, with optional sorting and filtering on creation date. |
| List Custom Attribute Groups | `listCustomAttributeGroups` | Retrieve the Custom Attribute Groups defined for one entity type. Groups organise Custom Attributes into sections in the Piggy dashboard. |
| List Custom Attributes | `listCustomAttributes` | Retrieve the Custom Attributes defined for one entity type, such as contact, reward or giftcard. Custom Attributes extend Piggy entities with your own fields. |
| List Forms | `listForms` | Retrieve the account's Forms, optionally filtered by status and type. Forms collect information from customers or employees and can be embedded or shared via their public URL. |
| List Giftcard Programs | `listGiftcardPrograms` | Retrieve all Giftcard Programs on the account, including card counts, expiry rules and minimum and maximum amounts. Every Giftcard belongs to one Giftcard Program. |
| List Giftcard Transactions | `listGiftcardTransactions` | Retrieve a paginated list of Giftcard Transactions, with optional filtering by Giftcard, Giftcard Program, Shop and creation date. |
| List Giftcards | `listGiftcards` | Retrieve a paginated list of Giftcards, optionally narrowed to a single Giftcard Program. |
| List Loyalty Transaction Attributes | `listLoyaltyTransactionAttributes` | Retrieve the Loyalty Transaction Attributes defined on the account. These are custom fields that can be attached to Credit Receptions and Reward Receptions. |
| List Loyalty Transactions | `listLoyaltyTransactions` | Retrieve a paginated list of Loyalty Transactions - every Credit Reception and Reward Reception that changed a Contact's credit balance - with optional filtering by type, Shop and creation date, and sorting. |
| List Orders | `listOrders` | Retrieve a paginated list of Orders, optionally narrowed to one Contact or one Business Profile. |
| List Perks | `listPerks` | Retrieve all Perks on the account. Perks are the benefits attached to Tiers that reward loyal Contacts. |
| List Prepaid Transactions | `listPrepaidTransactions` | Retrieve a paginated list of Prepaid Transactions, optionally narrowed to one Contact or one Shop. |
| List Product Categories | `listProductCategories` | Retrieve all Product Categories on the account. Categories group the Products used on Order line items. |
| List Products | `listProducts` | Retrieve a paginated list of Products. Products are what Order line items refer to. |
| List Promotion Attributes | `listPromotionAttributes` | Retrieve the Promotion Attributes defined on the account. Promotion Attributes add custom characteristics to Promotions and the Vouchers issued from them. |
| List Promotions | `listPromotions` | Retrieve all Promotions on the account. A Promotion is the campaign definition that Vouchers are issued against. |
| List Referrals | `listReferrals` | Retrieve a paginated list of Referrals made by Contacts, optionally filtered by the referring Contact and by referral status. |
| List Reviews | `listReviews` | Retrieve a paginated list of the Reviews Contacts have submitted. This endpoint is live on the Piggy API but is not covered by the published documentation. |
| List Rewards | `listRewards` | Retrieve the Rewards a Contact can redeem credits for, optionally narrowed to one Shop or to the Rewards currently claimable by one Contact. |
| List Shops | `listShops` | Retrieve every Shop (also called Business Profile) belonging to the Piggy account. Shops are required on most loyalty transactions, so this is usually the first call in a loyalty flow. |
| List Subscription Types | `listSubscriptionTypes` | Retrieve all Subscription Types on the account. A Subscription Type is a communication category, such as marketing email, that Contacts can subscribe to or unsubscribe from. |
| List Tiers | `listTiers` | Retrieve all Tiers configured on the account, including each Tier's position, media and the Perks attached to it. |
| List Units | `listUnits` | Retrieve all Units configured on the account. A Unit is the input value a Credit Reception is calculated from, such as purchase amount or number of visits. |
| List Visits | `listVisits` | Retrieve a paginated list of Visits registered in Piggy, optionally filtered to a single Contact. Visits are replicas of the visits recorded in your own system. |
| List Vouchers | `listVouchers` | Retrieve a paginated list of Vouchers, optionally filtered by Promotion, Contact and Voucher status. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | Retrieve all Webhook Subscriptions on the account, including the event each one listens for and the URL Piggy posts to. |
| Lock Voucher | `lockVoucher` | Reserve a Voucher so no other terminal can redeem it while a transaction is in progress. The response carries a release key needed to redeem or release it. |
| Merge Contacts | `mergeContacts` | Merge one Contact into another. The source Contact ceases to exist and its data moves to the destination Contact. This cannot be undone. |
| Multi Redeem Voucher | `multiRedeemVoucher` | Redeem a multi-use Voucher several times in one call, between 1 and 50 redemptions at a Shop. |
| Process Order | `processOrder` | Process an Order that was created earlier, converting it into the loyalty transaction its rules produce. |
| Redeem Collectable Reward | `redeemCollectableReward` | Mark a claimed physical Reward as collected, using the UUID of the Loyalty Transaction created when the Contact claimed it. |
| Redeem Voucher | `redeemVoucher` | Redeem a Voucher by its code at a Shop, consuming one of its allowed redemptions. Pass the release key if the Voucher was locked first. |
| Release Voucher | `releaseVoucher` | Release a locked Voucher with the release key returned when it was locked, making it available again without redeeming it. |
| Reverse Collectable Reward Redemption | `reverseCollectableRewardRedemption` | Undo the collection of a physical Reward, putting it back into the Contact's list of uncollected Rewards. |
| Reverse Credit Reception | `reverseCreditReception` | Reverse a Credit Reception, removing the credits it awarded from the Contact's balance. |
| Reverse Giftcard Transaction | `reverseGiftcardTransaction` | Reverse a Giftcard Transaction, undoing its effect on the Giftcard's balance. |
| Reverse Prepaid Transaction | `reversePrepaidTransaction` | Reverse a Prepaid Transaction, undoing its effect on the Contact's prepaid balance. |
| Reverse Reward Reception | `reverseRewardReception` | Reverse a Reward Reception, returning the credits it consumed to the Contact's balance. |
| Reverse Voucher Redemption | `reverseVoucherRedemption` | Reverse a Voucher Redemption, returning the redemption to the Voucher so it can be used again. |
| Send Contact Verification Email | `sendContactVerificationEmail` | Send a login verification email containing a one-time code to a Contact, so they can sign in to the Contacts Portal. This delivers a real email to the address supplied. |
| Send Giftcard By Email | `sendGiftcardByEmail` | Email a digital Giftcard to a Contact, optionally choosing which email template to use and supplying custom merge tags. This delivers a real email to the Contact. |
| Simulate Order Result | `simulateOrderResult` | Preview what loyalty result an Order would produce, without creating the Order. Useful for showing a customer the credits or offers a basket would earn. |
| Subscribe Contact To Subscription Type | `subscribeContact` | Subscribe a Contact to a Subscription Type so they start receiving that category of communication. |
| Unlink Contact Identifier | `unlinkContactIdentifier` | Detach a Contact Identifier from the Contact it is currently linked to, leaving the identifier itself in place. |
| Unsubscribe Contact From Subscription Type | `unsubscribeContact` | Unsubscribe a Contact from a Subscription Type so they stop receiving that category of communication. |
| Update Booking | `updateBooking` | Update an existing Booking, for example to check the party in, change the party size or mark the Booking completed or canceled. |
| Update Contact | `updateContact` | Update a Contact's attributes. Pass an object of attribute names to values, for example firstname and lastname, and only those attributes are changed. |
| Update Contact Identifier | `updateContactIdentifier` | Rename a Contact Identifier or activate and deactivate it. A deactivated identifier no longer recognises its Contact. |
| Update Custom Attribute | `updateCustomAttribute` | Update the label, description, select options or group of an existing Custom Attribute. The attribute is addressed by its immutable internal name and the entity it belongs to. |
| Update Order | `updateOrder` | Update an Order's status or payment status, for example to mark it completed or paid. |
| Update Perk | `updatePerk` | Rename an existing Perk by its UUID. Piggy's update endpoint changes the label only - a Perk's options cannot be changed after creation. |
| Update Product | `updateProduct` | Update a Product's name, description, external identifier or Categories. Only the fields you supply are changed. |
| Update Product Category | `updateProductCategory` | Update a Product Category's name or external identifier. Only the fields you supply are changed. |
| Update Promotion | `updatePromotion` | Update a Promotion's name and description. This endpoint is live on the Piggy API but is not covered by the published documentation. |
| Update Review | `updateReview` | Update a Review's rating, type or submission time. This endpoint is live on the Piggy API but is not covered by the published documentation. |
| Update Reward | `updateReward` | Update the title, description or required credits of an existing Reward. Only the fields you supply are changed. |
| Update Shift | `updateShift` | Update an existing Shift's times, status, Contact, Team or break length. |
| Update Visit | `updateVisit` | Update an existing Visit's external identifier, source or start and end times. Only the fields you supply are changed. |
| Update Voucher | `updateVoucher` | Activate or deactivate a Voucher, change its expiration date or set Custom Attributes on it. The expiration date can only be changed while the Voucher is inactive or active. |
| Update Webhook Subscription | `updateWebhookSubscription` | Update a Webhook Subscription's name, target URL or status, or change which Contact Attributes a contact_updated subscription watches. |
| Use Contact Session Token | `useContactSessionToken` | Consume a Contact Session Token, marking it as used so it cannot be redeemed a second time. |
| Verify Contact Login Code | `verifyContactLoginCode` | Verify the one-time login code a Contact received by email. A valid code confirms the Contact's identity for the Contacts Portal. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Booking Created | `booking_created` | New booking has been created. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Booking Updated | `booking_updated` | Booking has been updated, including when a guest checks in. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Contact Created | `contact_created` | New contact has been created. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Contact Identifier Created | `contact_identifier_created` | New contact identifier created for a contact. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Contact Identifier Updated | `contact_identifier_updated` | Contact identifier has been updated. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Contact Updated | `contact_updated` | Contact has been updated. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Contact Was Subscribed | `contact_was_subscribed` | Contact has been subscribed to a subscription type. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Contact Was Unsubscribed | `contact_was_unsubscribed` | Contact has been unsubscribed from a subscription type. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Credit Reception Created | `credit_reception_created` | New credit reception has been created for a contact. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Form Submission Completed | `form_submission_completed` | Contact has submitted and completed a form. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Giftcard Created | `giftcard_created` | New giftcard has been created. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Giftcard Transaction Created | `giftcard_transaction_created` | New giftcard transaction has been created. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Giftcard Updated | `giftcard_updated` | Giftcard has been updated, including when its balance changes. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Order Created | `order_created` | New order has been created. result describes what the order earned the contact, and is null when the order ran no loyalty action. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Points Transaction Created | `points_transaction_created` | Points have been credited to or debited from a contact. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Prepaid Transaction Created | `prepaid_transaction_created` | New prepaid transaction has been created for a contact. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Promotion Updated | `promotion_updated` | Promotion has been updated. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Referral Completed | `referral_completed` | Contact has completed a referral. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Reward Redeemed | `reward_redeemed` | Contact has redeemed a reward. previous_balance is the balance before the points were deducted. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Reward Updated | `reward_updated` | Reward has been updated. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Tier Dropped | `tier_dropped` | Contact has moved down to a lower tier. to_tier is null when the contact no longer has a tier. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Tier Reached | `tier_reached` | Contact has moved up to a new tier. from_tier is null when the contact had no tier before. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Visit Created | `visit_created` | Contact has visited a business profile. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Voucher Created | `voucher_created` | New voucher has been created. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Voucher Expired | `voucher_expired` | Voucher has passed its expiration date. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Voucher Redeemed | `voucher_redeemed` | Contact has redeemed a voucher. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
| Voucher Updated | `voucher_updated` | Voucher has been updated. Sample is Piggy's documented V1 payload, abridged below level 2; not a captured delivery. |
