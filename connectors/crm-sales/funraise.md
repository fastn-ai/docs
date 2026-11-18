---
description: "Funraise is a nonprofit fundraising platform with a built-in donor CRM: donation forms, peer-to-peer campaign sites, recurring giving, fundraising-event…"
hidden: true
---

# Funraise

Funraise is a nonprofit fundraising platform with a built-in donor CRM: donation forms, peer-to-peer campaign sites, recurring giving, fundraising-event auctions, and supporter records. This connector wraps the public Funraise REST API at https://api.funraise.io (Swagger 2.0, /api/v1 and /api/v2 paths) and covers supporters, donations/transactions, recurring subscriptions, payment methods, addresses, households, notes, interactions, tasks, supporter relationships, campaign sites, forms, custom questions, auction bids, and user notifications. Authentication is a single organization API key sent in the X-Api-Key header.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [funraise.io](https://funraise.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `funraise` |

## Use it

Add Funraise from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.funraise.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Household Member | `addHouseholdMember` | Add a supporter to a household. transactionReconciliation controls how that member's giving rolls up into the household totals. Returns the household membership record. |
| Batch Update Notifications | `batchUpdateNotifications` | Update several in-app notifications for the current Funraise user in one call - typically marking a set of them read. Funraise's Swagger declares no parameters at all, yet its description for this same operation states "The body must contain details about which notifications to update and how", so the previous no-body build could never have worked. The body is therefore taken as a caller-supplied JSON string: Funraise documents that one is required but not what goes in it. Returns HTTP 204 with an empty body on success. NOT verified against a live Funraise tenant - no credentials exist for this connector. |
| Cancel Subscription | `cancelSubscription` | Cancel a recurring giving subscription immediately. To schedule a future end date instead, use Set Subscription Cancel Date. Returns HTTP 204 with an empty body on success. |
| Charge Auction Item | `chargeAuctionItem` | Close out an auction item by charging the winning bid, creating a donation for it. Pass bidId to charge a specific bid, or omit it to charge the item's current winner. Returns the created donation id. |
| Complete Task | `completeTask` | Mark a task as complete. Sends no request body. Returns the updated task. |
| Create Auction Bid | `createAuctionBid` | Place a bid on a fundraising-event auction item on behalf of a supporter, using one of that supporter's stored payment methods. Returns the created bid. |
| Create Custom Question | `createCustomQuestion` | Create a custom question that can then be attached to donation forms, campaign sites or event tickets. questionType is required. Supply options for choice-style question types. Returns the created question. |
| Create Donation | `createDonation` | Record a new donation (transaction) against an existing supporter. amount, donationDate, donorId and paymentMethod are required. Use offline=true plus paymentMethod cash/check for gifts taken outside Funraise, and recurring/recurringSequence to attach the gift to a subscription. Returns the created donation. |
| Create Household | `createHousehold` | Create a household - the grouping Funraise uses for supporters who share an address or a giving history. name, primaryContact, salutation and transactionReconciliation are required. Returns the created household. |
| Create Household Note | `createHouseholdNote` | Attach a note to a household. title, body and important are all required by Funraise. Returns the created note. |

<details>

<summary>See 75 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Interaction | `createInteraction` | Log an interaction (a call, meeting or touchpoint) against a supporter. Every field is optional in the Funraise schema; supply donorId and subject at minimum. Returns the created interaction. |
| Create Subscription | `createSubscription` | Create a recurring giving subscription for an existing supporter using one of that supporter's stored payment methods. frequency, sourceAmount, supporter and paymentMethod are required. Returns the created subscription. |
| Create Supporter | `createSupporter` | Create a supporter (donor) record. Every field is optional in the Funraise schema; supply at least a name or an email. Institution supporters are created by setting institutionName and institutionCategory. Returns the created supporter. |
| Create Supporter Address | `createSupporterAddress` | Add a new address record to a supporter. Set primary=true to make it the supporter's primary address. Returns the created address. |
| Create Supporter Note | `createSupporterNote` | Attach a note to a supporter. title, body and important are all required by Funraise. Returns the created note. |
| Create Supporter Relationship | `createSupporterRelationship` | Link two supporters with a typed relationship. parentId and childId are supporter IDs; the direction matters for asymmetric types such as PARENT_CHILD, EMPLOYER_EMPLOYEE, TEACHER_STUDENT and MENTOR_MENTEE. Returns the created relationship. |
| Create Task | `createTask` | Create a task for a Funraise staff user, optionally linked to a supporter, a donation or a fundraising event. Every field is optional in the Funraise schema; supply title and assignedTo at minimum. Returns the created task. |
| Delete Address | `deleteAddress` | Delete an address record. Returns HTTP 204 with an empty body on success. |
| Delete Bid | `deleteBid` | Retract an auction bid. Returns HTTP 204 with an empty body on success. |
| Delete Custom Question | `deleteCustomQuestion` | Delete a custom question. Returns HTTP 204 with an empty body on success. |
| Delete Household | `deleteHousehold` | Delete a household. Its members become unhoused supporters. Returns HTTP 204 with an empty body on success. |
| Delete Interaction | `deleteInteraction` | Delete an interaction. Returns HTTP 204 with an empty body on success. |
| Delete Note | `deleteNote` | Delete a note. Returns HTTP 204 with an empty body on success. |
| Delete Notification | `deleteNotification` | Delete an in-app notification. Returns HTTP 204 with an empty body on success. |
| Delete Supporter | `deleteSupporter` | Permanently delete a supporter (donor) record. Returns HTTP 204 with an empty body on success. |
| Delete Supporter Relationship | `deleteSupporterRelationship` | Remove a relationship between two supporters. Returns HTTP 204 with an empty body on success. |
| Delete Task | `deleteTask` | Delete a task. Returns HTTP 204 with an empty body on success. |
| Get Address | `getAddress` | Retrieve a single address record by numeric ID, including the supporter and household it belongs to. |
| Get Auction Item Winner | `getAuctionItemWinner` | Retrieve the winning bid for one auction item of a fundraising event, including the winning supporter and their payment method. |
| Get Campaign Site | `getCampaignSite` | Retrieve a campaign site by UUID. Returns the full site configuration preview - payment options, fundraiser and team permissions, homepage, form, organization details and branding. This is a large response. |
| Get Custom Question | `getCustomQuestion` | Retrieve a single custom question by numeric ID, including its answer options. |
| Get Donation | `getDonation` | Retrieve a single donation (transaction) by numeric ID, including payment, fee, allocation, dedication and supporter detail. |
| Get Household | `getHousehold` | Retrieve a single household by numeric ID, including member count, primary contact, preferred address and combined giving totals. |
| Get Household Member | `getHouseholdMember` | Look up the household membership of a supporter - which household they belong to, if any. |
| Get Interaction | `getInteraction` | Retrieve a single interaction by numeric ID. |
| Get Note | `getNote` | Retrieve a single note by numeric ID, including its full body and the supporter or household it is attached to. |
| Get Notification | `getNotification` | Retrieve a single in-app notification by numeric ID. |
| Get Subscription | `getSubscription` | Retrieve a single recurring giving subscription by numeric ID, including supporter, payment method, schedule and dedication detail. |
| Get Supporter | `getSupporter` | Retrieve a single supporter (donor) by numeric ID, including household, institution, primary address and wealth-screening sub-objects. |
| Get Supporter Relationship | `getSupporterRelationship` | Retrieve a single supporter relationship by numeric ID, including both sides of the link. |
| Get Task | `getTask` | Retrieve a single task by numeric ID, including its assignee and any linked supporter, donation or event. |
| List Active Campaign Sites | `listActiveCampaignSites` | List the organization's active campaign sites (peer-to-peer fundraising sites), paginated. Optionally filter to sites that allow individual fundraisers. |
| List Archived Campaign Sites | `listArchivedCampaignSites` | List the organization's archived campaign sites, paginated. |
| List Auction Item Bids | `listAuctionItemBids` | List the bids placed on one auction item of a fundraising event, paginated. |
| List Donations | `listDonations` | Filter and page through donations (transactions). Use lastUpdated / lastHours / lastId for incremental sync, or transactionId to look up a gateway transaction. Returns a bare JSON array of donations, exposed here under `items`. |
| List Event Ticket Custom Questions | `listEventTicketCustomQuestions` | List the custom questions attached to a fundraising-event ticket type. |
| List Form Custom Questions | `listFormCustomQuestions` | List the custom questions attached to a donation form, in listing order. Returns a bare JSON array, exposed here under `items`. |
| List Forms | `listForms` | List the organization's donation forms, paginated, with optional filtering by form type, version and status. This is the only form endpoint Funraise exposes - there is no create, get-by-id, update or delete. |
| List Household Addresses | `listHouseholdAddresses` | List the address records belonging to a household, paginated and sortable. |
| List Household Notes | `listHouseholdNotes` | List the notes attached to a household, paginated and sortable. |
| List Notifications | `listNotifications` | List the in-app notifications for the Funraise user the API key belongs to, paginated. Filter by read state with the read flag. |
| List Subscriptions | `listSubscriptions` | List recurring giving subscriptions (monthly/recurring donations). Returns a bare JSON array of subscriptions, exposed here under `items`. |
| List Supporter Addresses | `listSupporterAddresses` | List the address records belonging to a supporter, paginated and sortable. |
| List Supporter Interactions | `listSupporterInteractions` | List every interaction logged against a supporter. Returns a bare JSON array, exposed here under `items`. |
| List Supporter Notes | `listSupporterNotes` | List the notes attached to a supporter, paginated and sortable. Note bodies may be omitted from the list projection - fetch a single note with Get Note for the full body. |
| List Supporter Payment Methods | `listSupporterPaymentMethods` | List the stored payment methods (cards and bank accounts) on a supporter. Use the returned id when creating or updating a recurring giving subscription or an auction bid. |
| List Supporters | `listSupporters` | List supporters (donors) in the Funraise organization. Supports paging and filtering by email or by how recently the record changed. Returns a bare JSON array of supporter objects, exposed here under `items`. |
| List User Interactions | `listUserInteractions` | List the interactions assigned to a Funraise staff user. Returns a bare JSON array, exposed here under `items`. |
| Merge Addresses | `mergeAddresses` | Merge two duplicate address records. The loser is folded into the winner and the winner survives. Returns the surviving address. |
| Merge Households | `mergeHouseholds` | Merge two households. The loser's members and giving history are folded into the winner and the winner survives. Returns the surviving household. |
| Move Donation To Supporter | `moveDonationToSupporter` | Reassign a donation (transaction) from its current supporter to a different supporter. Returns HTTP 204 with an empty body on success. |
| Print Supporter Yearly Summary | `printSupporterYearlySummary` | Generate a printable yearly giving summary (tax receipt) for one supporter. Returns the generated document name and a download URL. |
| Publish Campaign Site | `publishCampaignSite` | Publish a campaign site, making its current draft content live. Sends no request body. Returns the published site preview. |
| Reassign Task | `reassignTask` | Reassign a task to a different Funraise staff user. Sends no request body. Returns the updated task. |
| Remove Household Member | `removeHouseholdMember` | Remove a supporter from their household. The supporter record itself is not deleted. Returns the deletion timestamp. |
| Send Subscription Update Payment Email | `sendSubscriptionUpdatePaymentEmail` | Email the supporter a secure link to update the payment method on a recurring giving subscription. Use this to recover a failing card. Returns HTTP 204 with an empty body on success. |
| Set Bid Winner | `setBidWinner` | Mark a bid as the winning bid for its auction item. Sends no request body. Returns HTTP 204 with an empty body on success. |
| Set Campaign Site Custom Questions | `setCampaignSiteCustomQuestions` | Replace the whole set of custom questions attached to a campaign site. The Funraise request body is a raw JSON array, so pass it as a JSON string, e.g. [{"id":12,"listingOrder":1,"required":true}]. Returns the resulting attached questions. |
| Set Note Important | `setNoteImportant` | Flag or unflag a note as important without touching its title or body. Returns the updated note. |
| Set Subscription Cancel Date | `setSubscriptionCancelDate` | Schedule the end date of a recurring giving subscription. The subscription keeps charging until this date and then stops. Returns the updated subscription. |
| Unassign Task | `unassignTask` | Clear the assignee on a task, leaving it unassigned. Sends no request body. Returns the updated task. |
| Uncomplete Task | `uncompleteTask` | Reopen a completed task by marking it incomplete. Sends no request body. Returns the updated task. |
| Update Address | `updateAddress` | Update an existing address record. Only the fields you supply are sent. Returns the updated address. |
| Update Bid | `updateBid` | Change the payment method attached to an auction bid. This is the only mutable field on a bid. Returns the updated bid. |
| Update Campaign Site | `updateCampaignSite` | Update a campaign site's configuration. contents is required by Funraise on every update and carries the site's page content as an arbitrary JSON document - read it first with Get Campaign Site and send it back modified. All other fields are optional and only the ones you supply are sent. Returns the updated site preview. |
| Update Custom Question | `updateCustomQuestion` | Update a custom question. Funraise requires the question id in the URL path AND again in the request body, so pass the same value as both questionId and id. questionType is also required. Returns the updated question. |
| Update Donation | `updateDonation` | Partially update an existing donation (transaction). amount and donationDate must always be supplied. Note that Funraise has no refund endpoint - reversing a gift is done by setting status here. Returns the updated donation. |
| Update Household | `updateHousehold` | Update a household. name, primaryContactId and salutation are all required by Funraise on every update. Returns the updated household. |
| Update Interaction | `updateInteraction` | Update an existing interaction. Only the fields you supply are sent. Returns the updated interaction. |
| Update Note | `updateNote` | Replace the contents of a note. title, body and important are all required - this is a full replacement, not a patch. Returns the updated note. |
| Update Notification | `updateNotification` | Update a single in-app notification - in practice, mark it read or unread. Funraise's Swagger lists no body parameter for this operation, but its own description says the endpoint is for "marking a notification as read or modifying any additional user-specific fields" and it declares a 400 Validation error response, so a body is sent. read is the only field NotificationResponse exposes as mutable; if Funraise accepts more, they are undocumented. Returns the updated notification. NOT verified against a live Funraise tenant - no credentials exist for this connector. |
| Update Subscription | `updateSubscription` | Update a recurring giving subscription - change the amount, the cadence, or the card it charges. Funraise requires the subscription id in the URL path AND again in the request body, so pass the same value as both subscriptionId and id. frequency, sourceAmount and paymentMethod are also required. Returns the updated subscription. |
| Update Supporter | `updateSupporter` | Partially update a supporter (donor). Only the fields you supply are sent, so untouched fields keep their value. Returns the updated supporter. |
| Update Supporter Relationship | `updateSupporterRelationship` | Replace a supporter relationship. parentId, childId and relationship are all required - this is a full replacement, not a patch. Returns the updated relationship. |
| Update Task | `updateTask` | Update an existing task. Only the fields you supply are sent. Returns the updated task. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Donation created or edited | `DONATION` | Fired whenever a Funraise transaction is created or edited. This is the only event type Funraise emits - there are no supporter, subscription, campaign or task events. NO PER-TENANT ROUTING. requiredActions is deliberately EMPTY and this is not an oversight: the delivered body is {sentAt, event, data{...}} and carries no organization identifier anywhere. orgUUID exists on the REST donation list response but Funraise does not put it in the webhook body, so there is no payload field an APP-type requiredActions[].mappedTo could match a connection against. Consequence: routing is by eventKey ('event') ALONE, so EVERY active trigger on this connector receives EVERY delivery that reaches the shared fastn URL. Do not deploy this expecting per-tenant fan-out to be filtered for you - if more than one Funraise organization is ever connected in the same fastn org, each one's triggers will also fire on the other's donations, and the workflow must discriminate itself (for example on data.form.id, data.allocation.id or data.campaignPage.id, which are org-specific values the workflow author can pin). This is acceptable today mainly because Funraise allows exactly ONE webhook per organization. REGISTRATION IS EXPECTED TO FAIL - UNRESOLVED BLOCKER. On Save, Funraise POSTs to the target URL and the endpoint must echo the x-hook-secret REQUEST header back as a RESPONSE header and return 200, or the subscription is not created. fastn's ingest cannot do that: the bodyless handshake support (GetChallengeConfig / pipeline/challenge-echo.ts in the event service) can READ a token from a request header, but it only ever writes the token back into the response BODY as text/plain or JSON - it never sets an arbitrary response header. This is the same class of blocker as Microsoft Graph's validationToken echo. Until fastn's ingest grows a response-header echo, expect Funraise's Save to reject the fastn URL and no event to ever arrive. Not reproduced against a live Funraise org - there are no Funraise credentials - but confirmed on the fastn side by reading the ingest pipeline. SETUP (for when the above is resolved): in Funraise go to Settings &gt; Webhooks, open the Webhook Signing Secret actions menu (3 dots) and click Generate, then click Edit and paste the fastn webhook URL as the Webhook Target URL plus a contact email for delivery failures, and Save. Funraise allows exactly ONE webhook per organization, and retries a failing delivery for about 24 hours before emailing the contact address. |
