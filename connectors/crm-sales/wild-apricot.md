---
description: "WildApricot is a membership management platform for associations, clubs and non-profits."
hidden: true
---

# WildApricot

<img src="../../.gitbook/assets/connectors/wild-apricot.png" alt="WildApricot logo" width="64">

WildApricot is a membership management platform for associations, clubs and non-profits. This connector covers the WildApricot Admin API v2.3: accounts, contacts and members, contact and donation fields, saved searches, membership levels, bundles and member groups, pending membership approvals, events, event registration types and registrations, check-in and waitlists, invoices, payments, refunds, tenders and allocations, donations, CEU records, audit log, email log, drafts and sending, attachments and pictures, and the online store (products and orders).

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [wildapricot.com](https://wildapricot.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `wildApricot` |

## Use it

Add WildApricot from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.wildApricot.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Terms Of Use | `acceptTermsOfUse` | Accepts the WildApricot Terms of Use on behalf of the currently signed-in user. Does nothing if already accepted. Requires a token issued for a WildApricot user; API-key tokens receive 403. |
| Allocate Invoice To Payment | `allocateInvoiceToPayment` | Allocates a WildApricot invoice, in whole or in part, to a payment so that the invoice is settled by that payment. |
| Allocate Refund To Donation | `allocateRefundToDonation` | Allocates a WildApricot refund against a donation, recording that the refund returns money given as that donation. The path identifier is the donation's payment document ID (the Payment.Id on the donation), not the donation's own ID. |
| Allocate Refund To Payment | `allocateRefundToPayment` | Allocates a WildApricot refund to a payment, recording that the refund returns money taken by that payment. |
| Approve Pending Membership | `approvePendingMembership` | Approves a contact's pending membership application in WildApricot. Only allowed when the contact's extended membership info lists ApprovePendingMembership among its allowed actions; otherwise WildApricot returns 400. |
| Check In Event Attendee | `checkInEventAttendee` | Checks a WildApricot event registrant in or out at the door. For registrations carrying anonymous guests, the number of guests checked in can also be recorded. |
| Clone Event | `cloneEvent` | Duplicates an existing WildApricot event, copying its settings and registration types into a new event whose title can be given a prefix. |
| Count Unique Email Draft Recipients | `countUniqueEmailDraftRecipients` | Returns how many unique email addresses a WildApricot email draft would reach, so the audience size can be checked before sending. The published OpenAPI document specifies a bare integer request body, but the live endpoint rejects a bare integer with HTTP 400 and only accepts a JSON object, so the connector sends the draft identifier as an object in the same shape the other email-draft operations use. |
| Count Unique Email Recipients | `countUniqueEmailRecipients` | Returns how many unique email addresses a given WildApricot recipient selection resolves to, so the audience size of an email can be checked before it is composed. |
| Create CEU Record | `createCeuRecord` | Creates a continuing education unit (CEU) record in WildApricot for a contact, recording the activity, the credits earned and the period the credits cover. |

<details>

<summary>See 113 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Contact | `createContact` | Creates a new contact or member record in WildApricot. Provide first name, last name and email (must be unique in the account); optionally a membership level, membership status and field values. Note that WildApricot ignores the top-level Organization property on create - set organization, phone, notes and other fields through Field Values using their System Code (for example Organization, Phone, Notes). |
| Create Contact Field | `createContactField` | Creates a new custom contact or membership field in WildApricot and returns the new field ID. Field name must be unique; choice fields take their options from Allowed Values. |
| Create Donation | `createDonation` | Records a donation in WildApricot and returns the new donation ID. Link it to a contact, or supply the donor's name and email for an anonymous donation, and set values for any custom donation fields. |
| Create Donation Field | `createDonationField` | Creates a new custom donation field in WildApricot and returns the new field ID. Field name and field type are required; choice fields take their options from Allowed Values. |
| Create Event | `createEvent` | Creates a new event in WildApricot and returns the new event ID. Name, event type and start date are required; registration, location, tags, sessions and extended details are optional. |
| Create Event Registration | `createEventRegistration` | Registers a contact for a WildApricot event. The event, the contact and the registration type are required. Optionally create the entry on the waitlist, supply registration field values, or add a memo. |
| Create Event Registration Type | `createEventRegistrationType` | Creates a new registration type (ticket type) for a WildApricot event and returns its ID. The event ID is required; price, availability, membership level restrictions, guest policy and waitlist behaviour are optional. |
| Create Invoice | `createInvoice` | Creates a manual invoice in WildApricot for a contact and returns the new invoice ID. The contact is required; supply one or more order lines to give the invoice a value. |
| Create Payment | `createPayment` | Records a payment in WildApricot against a contact and returns the created payment. The contact is required; supply invoice identifiers to settle those invoices with this payment. |
| Create Refund | `createRefund` | Records a refund in WildApricot for a contact. The contact is required and the amount must be negative; WildApricot rejects a positive value with 'Value should be less than zero'. |
| Create Store Product | `createStoreProduct` | Creates a product in the WildApricot online store. A title and a regular price are required; inventory tracking, options, variants and digital or e-course delivery can all be configured. |
| Create Tender | `createTender` | Creates a custom payment type (tender) in WildApricot, for example Cash or Cheque, so that manual payments can be recorded against it. The name is required. |
| Delete CEU Record | `deleteCeuRecord` | Permanently deletes a WildApricot continuing education unit (CEU) record by ID. |
| Delete Contact | `deleteContact` | Permanently deletes a WildApricot contact. Only archived contacts can be deleted; archive the contact first with Update Contact (IsArchived = true). |
| Delete Contact Field | `deleteContactField` | Deletes a custom contact or membership field definition from WildApricot by ID. System fields cannot be deleted. |
| Delete Donation Field | `deleteDonationField` | Deletes a custom donation field definition from WildApricot by ID. System donation fields cannot be deleted. |
| Delete Email Draft | `deleteEmailDraft` | Deletes a WildApricot email draft by ID. A scheduled draft is cancelled as well as deleted. |
| Delete Event | `deleteEvent` | Permanently deletes a WildApricot event together with its registration types and registrations. |
| Delete Event Registration | `deleteEventRegistration` | Deletes a WildApricot event registration, removing the registrant from the event. |
| Delete Event Registration Type | `deleteEventRegistrationType` | Deletes a registration type (ticket type) from a WildApricot event. A registration type that already has registrations cannot be deleted. |
| Delete Invoice | `deleteInvoice` | Permanently deletes a WildApricot invoice. Use Void Invoice instead when the invoice must remain on the financial record. |
| Delete Payment | `deletePayment` | Permanently deletes a WildApricot payment record and releases any invoices it had settled. |
| Delete Refund | `deleteRefund` | Permanently deletes a WildApricot refund record and releases any allocations it had. |
| Delete Store Product | `deleteStoreProduct` | Deletes a product from the WildApricot online store by its product ID. |
| Delete Store Product By Source | `deleteStoreProductBySource` | Deletes a WildApricot online store product matched by its external source reference ID rather than by its WildApricot product ID. |
| Delete Tender | `deleteTender` | Deletes a custom WildApricot payment type (tender). Built-in gateway tenders and tenders already used by payments cannot be deleted. |
| Generate Invoice For Event Registration | `generateInvoiceForEventRegistration` | Generates the invoice for a WildApricot event registration, or updates the existing one when Update If Exists is set. |
| Generate Invoice For Pending Membership | `generateInvoiceForPendingMembership` | Generates, or optionally updates, the invoice for a contact's pending membership application in WildApricot. Only allowed when the contact's allowed membership actions include GenerateInvoiceForPendingMembership. |
| Get Account | `getAccount` | Retrieves the connected WildApricot account: its ID, name, primary domain, contact limit, currency, time zone, localization settings and the API resources available to it. |
| Get Attachment Content | `getAttachmentContent` | Downloads the content of a WildApricot file attachment. For image attachments a resized variant can be requested, and the content can be returned Base64 encoded. |
| Get Attachment Infos | `getAttachmentInfos` | Retrieves metadata for one or more WildApricot file attachments by their identifiers, including file name, size and content type. |
| Get Audit Log Item | `getAuditLogItem` | Retrieves a single WildApricot audit log entry by ID, including what changed, when, and which contact or administrator initiated it. |
| Get CEU Record | `getCeuRecord` | Retrieves a single WildApricot continuing education unit (CEU) record by ID, including the contact, activity, credits earned and validity dates. |
| Get Contact | `getContact` | Retrieves a single WildApricot contact or member by ID, including membership level and status and all field values. Optionally includes extended membership information such as allowed membership actions and pending invoice. |
| Get Current Contact | `getCurrentContact` | Retrieves the contact record of the user the access token was issued for. Only available when the token represents a signed-in WildApricot user; API-key tokens are not tied to a contact and receive 403. |
| Get Donation | `getDonation` | Retrieves a single WildApricot donation by ID, including the amount, date, donor details, related payment and any custom donation field values. |
| Get Email Draft | `getEmailDraft` | Retrieves a single WildApricot email draft by ID, including its subject, body, sender, recipient selection and delivery schedule. |
| Get Email Draft Preview | `getEmailDraftPreview` | Returns a rendered preview of a WildApricot email draft, with macros resolved, so the message can be checked before it is sent. |
| Get Event | `getEvent` | Retrieves full details of a single WildApricot event by ID, including schedule, location, registration settings, tags, sessions and registration counts. |
| Get Event Registration | `getEventRegistration` | Retrieves a single WildApricot event registration by ID, including the event, registrant, registration type, fee, payment status, check-in state and registration field values. |
| Get Event Registration Type | `getEventRegistrationType` | Retrieves a single WildApricot event registration type (ticket type) by ID, including its price, availability, restrictions and cancellation policy. |
| Get Feature Availability | `getFeatureAvailability` | Checks whether a specific WildApricot feature is available for the connected account. WildApricot reserves this for internal use and returns Allowed true for any unknown feature ID. |
| Get Invoice | `getInvoice` | Retrieves a single WildApricot invoice by ID, including its number, total, paid amount, order lines, taxes, memo and the contact it was raised for. |
| Get Member Group | `getMemberGroup` | Retrieves a WildApricot ad hoc member group by ID with its name, description and the IDs of contacts in the group. |
| Get Membership Bundle | `getMembershipBundle` | Retrieves a single WildApricot membership bundle by ID, including its administrator, membership level, participants and member limit. |
| Get Membership Level | `getMembershipLevel` | Retrieves a single WildApricot membership level by ID, including fee, level type, bundle size, renewal period and application review settings. |
| Get Payment | `getPayment` | Retrieves a single WildApricot payment by ID, including its amount, tender, payer, allocation and refund totals and payment progress. |
| Get Picture Content | `getPictureContent` | Downloads a picture stored in WildApricot by its picture ID. A full size version can be requested, and the image can be returned Base64 encoded. |
| Get Refund | `getRefund` | Retrieves a single WildApricot refund by ID, including its amount, settled amount, tender, recipient and comments. |
| Get Saved Search | `getSavedSearch` | Retrieves a WildApricot saved search and the IDs of the contacts it currently finds, optionally excluding archived contacts or narrowing the result with an additional filter. |
| Get Sent Email | `getSentEmail` | Retrieves a single entry from the WildApricot email log by ID, including the message subject, body, sender, type and delivery statistics. |
| Get Store Order | `getStoreOrder` | Retrieves a single WildApricot online store order by its order number, including the buyer, the ordered items, totals, shipping address and related invoice. |
| Get Store Product | `getStoreProduct` | Retrieves a single WildApricot online store product by ID, including its price, stock, options, variants and digital or e-course details. |
| Get Tender | `getTender` | Retrieves a single WildApricot payment type (tender) by ID, including its name, display position and whether it is a custom tender. |
| Get Unique Email Draft Recipient Addresses | `getUniqueEmailDraftRecipientAddresses` | Returns the list of unique email addresses a WildApricot email draft would reach, so the audience can be inspected before sending. The published OpenAPI document specifies a bare integer request body, but the live endpoint rejects a bare integer with HTTP 400 and only accepts a JSON object, so the connector sends the draft identifier as an object in the same shape the other email-draft operations use. |
| Get Unique Email Recipient Addresses | `getUniqueEmailRecipientAddresses` | Returns the distinct email addresses a given WildApricot recipient selection resolves to, so the audience of an email can be reviewed before it is composed. |
| List Accounts | `listAccounts` | Lists the WildApricot accounts available to the current access token. Typically this returns a single account with its ID, name, primary domain, currency, time zone and available API resources. |
| List API Resources | `listApiResources` | Lists the top-level WildApricot API resources that can be reached directly without an account ID, with their URLs and allowed HTTP operations. |
| List Audit Log Items | `listAuditLogItems` | Lists WildApricot audit log entries recording changes made to contacts, events, registrations and financial documents. Narrow the result to an object type, a specific object or a date range. |
| List CEU Records | `listCeuRecords` | Lists the continuing education unit (CEU) records held in WildApricot, optionally restricted to one contact or to specific record identifiers. |
| List Contact Fields | `listContactFields` | Lists all contact and membership field definitions in the WildApricot account, both system fields and administrator-defined custom fields, with their type, access level, allowed values and system code. |
| List Contacts | `listContacts` | Searches contacts and members in the WildApricot account. Set $async to false for an immediate list of contacts; with the default asynchronous mode WildApricot returns a ResultId that you pass back as resultId to fetch the finished result. Supports filtering, field selection, sorting, simple text search, paging, counting and IDs-only results. |
| List Donation Fields | `listDonationFields` | Lists the donation field definitions in the WildApricot account, both system fields and administrator-defined custom fields, with their type, display type, allowed values and system code. |
| List Donations | `listDonations` | Lists WildApricot donations. A start date and an end date are required to bound the search; paging, count-only and IDs-only results are supported. |
| List Email Drafts | `listEmailDrafts` | Lists the email drafts saved in the WildApricot account, including scheduled drafts, with their subject, sender, schedule and recipient selection. |
| List Event Registration Types | `listEventRegistrationTypes` | Lists the registration types (ticket types) defined for a WildApricot event, with their price, availability window, membership level restrictions, guest policy and waitlist settings. |
| List Event Registrations | `listEventRegistrations` | Lists WildApricot event registrations for a specific event or contact. At least one of Event ID or Contact ID must be supplied. Waitlist entries and cancelled registrations can be included, and registration field values can be returned with each record. |
| List Events | `listEvents` | Lists events in the WildApricot account. Supports filtering by name, tags, start and end date or upcoming status, sorting, paging, count-only and IDs-only results. Set $async to false to receive the events directly instead of a ResultId. |
| List Invoices | `listInvoices` | Lists WildApricot invoices, optionally narrowed to a contact, an event, an event registration or a date range, and filtered to unpaid or paid invoices only. Voided invoices are excluded unless explicitly included. |
| List Member Groups | `listMemberGroups` | Lists the ad hoc member groups in WildApricot with their name, description and contact count. Supports paging, count-only, IDs-only and filtering by group IDs. |
| List Membership Bundles | `listMembershipBundles` | Lists membership bundles (group memberships such as corporate or family memberships) for a given bundle membership level, with their administrator, members and size limit. |
| List Membership Levels | `listMembershipLevels` | Lists the membership levels configured in WildApricot, including fee, type (individual or bundle), renewal period and application review settings. Supports paging, count-only, IDs-only and filtering by level IDs. |
| List Payment Allocations | `listPaymentAllocations` | Lists how WildApricot payments are allocated among invoices and refunds. Supply an invoice, payment or refund identifier to scope the result; a single payment can settle several invoices and a single invoice can be settled by several payments. |
| List Payments | `listPayments` | Lists WildApricot payments, optionally narrowed to a contact, an event, a date range, specific payment identifiers, a payment type or unsettled payments only. |
| List Refunds | `listRefunds` | Lists WildApricot refunds, optionally narrowed to a contact, an event, a date range, specific refund identifiers or unsettled refunds only. |
| List Saved Searches | `listSavedSearches` | Lists the saved contact searches defined in the WildApricot admin view, with optional paging, count-only and IDs-only results. |
| List Sent Email Recipients | `listSentEmailRecipients` | Lists the recipients of a logged WildApricot email, optionally restricted to those who did or did not receive or open it, and optionally including the links each recipient clicked. |
| List Sent Emails | `listSentEmails` | Lists entries from the WildApricot email log, showing the emails the system has sent with their subject, sender, recipient counts and delivery statistics. Supports filtering by sent date and email type. |
| List Store Orders | `listStoreOrders` | Lists orders placed in the WildApricot online store, optionally filtered by fulfilment status, payment status or a date range. |
| List Store Products | `listStoreProducts` | Lists the products in the WildApricot online store, optionally filtered by specific identifiers or by the external source a product was imported from. |
| List Tenders | `listTenders` | Lists the payment types (tenders) configured in the WildApricot account, both the built-in gateway tenders and any custom ones added by an administrator. |
| Register From Waitlist | `registerFromWaitlist` | Promotes a WildApricot event waitlist entry into a confirmed registration, optionally generating the invoice for the newly confirmed registrant. |
| Reject Pending Membership | `rejectPendingMembership` | Rejects a contact's pending membership application in WildApricot. Only allowed when the contact's extended membership info lists RejectPendingMembership among its allowed actions; otherwise WildApricot returns 400. |
| Send Email | `sendEmail` | Composes and sends a new email to WildApricot contacts, members, event attendees or a saved search, and returns the identifier of the resulting email log entry. The message is delivered immediately to real recipients. |
| Send Email Draft | `sendEmailDraft` | Sends a saved WildApricot email draft immediately to the recipients selected on the draft. The message is delivered to real recipients. |
| Send Invoice Email | `sendInvoiceEmail` | Emails a WildApricot invoice to a recipient using the supplied subject and body. The address, subject and body are all required by WildApricot; macros such as {Invoice_Number} and {Contact_FullName} are expanded. The message is delivered to a real recipient. Returns the identifier of the email log entry. |
| Send Payment Email | `sendPaymentEmail` | Emails a payment receipt for a WildApricot payment to a recipient using the supplied subject and body. The address, subject and body are all required by WildApricot; macros such as {Payment_Amount} and {Contact_FullName} are expanded. The message is delivered to a real recipient. Returns the identifier of the email log entry. |
| Send Refund Email | `sendRefundEmail` | Emails a refund notification for a WildApricot refund to a recipient using the supplied subject and body. The address, subject and body are all required by WildApricot; macros such as {Refund_Amount} and {Contact_FullName} are expanded. The message is delivered to a real recipient. Returns the identifier of the email log entry. |
| Send Two-Factor Code | `sendTwoFactorCode` | Sends a two-factor authentication code to the currently signed-in WildApricot user by email or SMS. Requires a token issued for a WildApricot user; API-key tokens receive 403. |
| Set Email Draft Schedule | `setEmailDraftSchedule` | Schedules a WildApricot email draft for delivery at a given date and time, or pauses a scheduled draft by clearing the scheduled flag. |
| Set Store Order Status | `setStoreOrderStatus` | Sets the fulfilment status of a WildApricot online store order, marking it fulfilled, unfulfilled or cancelled. |
| Unallocate Document From Donation | `unallocateFromDonation` | Removes a previously allocated finance document from a WildApricot donation, releasing the allocated amount. The path identifier is the donation's payment document ID (the Payment.Id on the donation), not the donation's own ID. |
| Unallocate Document From Payment | `unallocateFromPayment` | Removes a previously allocated invoice or refund from a WildApricot payment, releasing the allocated amount. |
| Update CEU Record | `updateCeuRecord` | Updates a WildApricot continuing education unit (CEU) record identified by its record ID. |
| Update CEU Record By External ID | `updateCeuRecordByExternalId` | Updates a WildApricot continuing education unit (CEU) record matched by its external source type and reference ID rather than by its WildApricot record ID. Useful when syncing CEU credits from a learning management system. |
| Update Contact | `updateContact` | Updates an existing WildApricot contact or member. Send only the fields you want to change. Organization, Phone and every custom field are set through Field Values by system code, not as top-level properties; to archive a contact set the IsArchived system field to true in Field Values. |
| Update Contact Field | `updateContactField` | Updates an existing custom contact or membership field definition in WildApricot. The field type cannot be changed, and a contact field cannot be converted into a membership field or vice versa. |
| Update Donation | `updateDonation` | Updates an existing WildApricot donation, for example to correct its amount, date, donor details, comments or custom field values. |
| Update Donation Field | `updateDonationField` | Updates an existing custom donation field definition in WildApricot. The field type cannot be changed after creation. |
| Update Event | `updateEvent` | Updates an existing WildApricot event. Send the event ID in the path and only the fields you want to change; WildApricot requires Id, Name, EventType and StartDate in the body. |
| Update Event Registration | `updateEventRegistration` | Updates an existing WildApricot event registration, for example to change the registration type, edit registration field values, toggle public visibility or amend the memo. WildApricot treats omitted booleans as false on this PUT (an update without IsCheckedIn clears an existing check-in), so resend the values you want to keep; use Check In Event Attendee for check-in changes. |
| Update Event Registration Type | `updateEventRegistrationType` | Updates an existing WildApricot event registration type (ticket type). WildApricot requires the registration type ID and the owning event ID in the body alongside the fields being changed. |
| Update Invoice | `updateInvoice` | Updates an existing WildApricot invoice, for example to amend its memo, date or order lines. Paid or settled invoices may be rejected by WildApricot. |
| Update Payment | `updatePayment` | Updates an existing WildApricot payment, for example to correct its amount, date, tender or comments. |
| Update Refund | `updateRefund` | Updates an existing WildApricot refund, for example to correct its amount, date, tender or comments. |
| Update Store Product | `updateStoreProduct` | Updates a WildApricot online store product identified by its product ID, for example to change its title, price, stock or visibility. |
| Update Store Product By Source | `updateStoreProductBySource` | Updates a WildApricot online store product matched by its external source reference ID rather than by its WildApricot product ID. Useful when syncing a catalogue from an external system. |
| Update Tender | `updateTender` | Updates a custom WildApricot payment type (tender), for example to rename it or change its position in the list. Built-in gateway tenders cannot be changed. |
| Upload Attachments | `uploadAttachments` | Uploads one or more files to WildApricot file attachment storage and returns their attachment identifiers, which can then be set as the value of a file attachment contact field. Pass the files as a JSON array string; each entry carries the file name, MIME type and Base64 encoded data. |
| Upload Picture | `uploadPicture` | Uploads a picture to WildApricot picture storage and returns its picture ID, which must be set as the value of a custom picture contact field within 30 minutes. WildApricot accepts this endpoint only as a multipart/form-data upload. |
| Upload Store Product Pictures | `uploadStoreProductPictures` | Uploads product images to the WildApricot online store and returns their identifiers, which can then be set in the Pictures list of a store product. Pass the images as a JSON array string; each entry carries the file name, MIME type and Base64 encoded data. |
| Verify Two-Factor Code | `verifyTwoFactorCode` | Verifies a two-factor authentication code that was sent to the currently signed-in WildApricot user, returning true when the code is valid. Requires a token issued for a WildApricot user; API-key tokens receive 403. |
| Void Invoice | `voidInvoice` | Voids a WildApricot invoice, cancelling it while keeping it on the financial record. Voided invoices are excluded from List Invoices unless Include Voided is set. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Contact Changed | `Contact` | Fires on any change to any tab of a contact's details, and on any change to contact field settings. SETUP (required, per WildApricot account): in the WildApricot admin view go to Apps &gt; Integrations &gt; Webhooks &gt; Add webhook, enter a name and paste the fastn webhook URL, set Authorization type to None, tick the Contact notification type, turn Enable webhook on and click Save. |
| Email Logged | `LoggedEmail` | Fires when an email is added to the WildApricot email log. Email.EmailType and Email.OriginType are numeric codes documented in the WildApricot webhooks article. SETUP (required, per WildApricot account): in the WildApricot admin view go to Apps &gt; Integrations &gt; Webhooks &gt; Add webhook, enter a name and paste the fastn webhook URL, set Authorization type to None, tick the Logged email letter notification type, turn Enable webhook on and click Save. |
| Event Changed | `Event` | Fires when an event is created, changed or deleted. Changes to registration forms, ticket types and event email settings do not trigger it. SETUP (required, per WildApricot account): in the WildApricot admin view go to Apps &gt; Integrations &gt; Webhooks &gt; Add webhook, enter a name and paste the fastn webhook URL, set Authorization type to None, tick the Event notification type, turn Enable webhook on and click Save. |
| Event Registration Changed | `EventRegistration` | Fires on any change to an event registration, including a new registration, a cancelled registration and an RSVP response. SETUP (required, per WildApricot account): in the WildApricot admin view go to Apps &gt; Integrations &gt; Webhooks &gt; Add webhook, enter a name and paste the fastn webhook URL, set Authorization type to None, tick the Event registration notification type, turn Enable webhook on and click Save. |
| Invoice Changed | `Invoice` | Fires when an invoice is created, modified, voided or deleted. SETUP (required, per WildApricot account): in the WildApricot admin view go to Apps &gt; Integrations &gt; Webhooks &gt; Add webhook, enter a name and paste the fastn webhook URL, set Authorization type to None, tick the Invoice notification type, turn Enable webhook on and click Save. |
| Membership Changed | `Membership` | Fires on any change to a member's membership settings or to membership field settings. Changes to membership level settings do not trigger it. SETUP (required, per WildApricot account): in the WildApricot admin view go to Apps &gt; Integrations &gt; Webhooks &gt; Add webhook, enter a name and paste the fastn webhook URL, set Authorization type to None, tick the Membership notification type, turn Enable webhook on and click Save. |
| Membership Level Changed | `MembershipLevel` | Fires when a membership level is created, deleted, renamed, repriced or has its renewal strategy changed. SETUP (required, per WildApricot account): in the WildApricot admin view go to Apps &gt; Integrations &gt; Webhooks &gt; Add webhook, enter a name and paste the fastn webhook URL, set Authorization type to None, tick the Membership level notification type, turn Enable webhook on and click Save. |
| Membership Renewed | `MembershipRenewed` | Fires when an existing membership is renewed. SETUP (required, per WildApricot account): in the WildApricot admin view go to Apps &gt; Integrations &gt; Webhooks &gt; Add webhook, enter a name and paste the fastn webhook URL, set Authorization type to None, tick the Renewal notification type, turn Enable webhook on and click Save. |
| Payment Changed | `Payment` | Fires when a payment is created, adjusted or cancelled. SETUP (required, per WildApricot account): in the WildApricot admin view go to Apps &gt; Integrations &gt; Webhooks &gt; Add webhook, enter a name and paste the fastn webhook URL, set Authorization type to None, tick the Payment notification type, turn Enable webhook on and click Save. |
| Refund Changed | `Refund` | Fires when a refund is created, adjusted or cancelled. SETUP (required, per WildApricot account): in the WildApricot admin view go to Apps &gt; Integrations &gt; Webhooks &gt; Add webhook, enter a name and paste the fastn webhook URL, set Authorization type to None, tick the Refund notification type, turn Enable webhook on and click Save. |
