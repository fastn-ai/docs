---
description: "BoldSign is an electronic signature platform for sending, signing and managing legally binding documents."
---

# BoldSign

BoldSign is an electronic signature platform for sending, signing and managing legally binding documents. This connector covers the full BoldSign REST API: documents (send, draft, edit, remind, revoke, download, audit logs, tags, authentication, access codes, recipient changes, prefilled fields, expiry, embedded URLs), templates (create, edit, send, merge and send, share, tags, embedded URLs), contacts and contact groups, custom fields, brands, sender identities, teams, users, identity verification and API credit usage.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [boldsign.com](https://boldsign.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 87 |
| **Events** | 34 |
| **Slug** | `boldSign` |

## Use it

Add BoldSign from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.boldSign.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Document Authentication | `addDocumentAuthentication` | Adds an identity check, such as an access code, email or SMS one-time passcode, identity verification or knowledge-based authentication, to a recipient of a signature request. |
| Add Document Tags | `addDocumentTags` | Adds one or more labels to a document so it can be grouped and found later. |
| Add Template Tags | `addTemplateTags` | Adds labels to a template, either to the template itself or to the documents sent from it. |
| Cancel Document Editing | `cancelDocumentEditing` | Releases a document that is locked in edit mode so it can be worked on again. |
| Cancel User Invitation | `cancelUserInvitation` | Withdraws a pending account invitation so the invited person can no longer join. |
| Change Document Access Code | `changeDocumentAccessCode` | Replaces the access code a recipient must enter before they can open a signature request. |
| Change Document Recipient | `changeDocumentRecipient` | Reassigns a pending signature request to a different person, recording the reason for the change. |
| Change User Team | `changeUserTeam` | Moves a user to a different team, optionally transferring their documents to another user. |
| Create Brand | `createBrand` | Creates a branding profile that controls the logo, colours, disclaimer and email behaviour applied to signature requests. The logo must be supplied as SVG markup; BoldSign also accepts JPG, JPEG and PNG logos, but binary uploads cannot be sent through this connector. |
| Create Contact | `createContact` | Adds a contact to the BoldSign address book so it can be selected as a recipient on future signature requests. |
| Create Contact Group | `createContactGroup` | Creates a contact group so a named set of recipients can be added to signature requests in one step. |
| Create Custom Field | `createCustomField` | Creates a reusable custom form field on a brand so senders can drop the same pre-configured field onto any document or template. BoldSign accepts a background colour only on Label fields. |
| Create Embedded Custom Field URL | `createEmbeddedCustomFieldUrl` | Generates a short-lived URL that embeds the BoldSign custom field designer for a brand inside your own application. |
| Create Embedded Document Clone URL | `createEmbeddedDocumentCloneUrl` | Returns a URL that embeds the BoldSign clone flow, so a sender can start a new signature request from an existing one inside your own application. |
| Create Embedded Document Edit URL | `createEmbeddedDocumentEditUrl` | Returns a URL that embeds the BoldSign document editor for an existing signature request inside your own application. |
| Create Embedded Document Request URL | `createEmbeddedDocumentRequestUrl` | Creates a signature request and returns a URL that embeds the BoldSign preparation and sending experience inside your own application. |
| Create Embedded Identity Verification URL | `createEmbeddedIdentityVerificationUrl` | Returns a URL that embeds manual identity verification for one recipient of a signature request inside your own application. |
| Create Embedded Request URL From Template | `createEmbeddedRequestUrlFromTemplate` | Prepares a signature request from a template and returns a URL that embeds the BoldSign sending experience inside your own application. |
| Create Embedded Template Clone URL | `createEmbeddedTemplateCloneUrl` | Returns a URL that embeds the BoldSign clone flow for a template, so a user can start a new template from an existing one inside your own application. |
| Create Embedded Template Preview URL | `createEmbeddedTemplatePreviewUrl` | Returns a read-only URL that embeds a preview of a template inside your own application. |
| Create Embedded Template URL | `createEmbeddedTemplateUrl` | Returns a URL that embeds the BoldSign template designer inside your own application, so a user can build a new template there. |
| Create Merged Embedded Request URL | `createMergedEmbeddedRequestUrl` | Merges several templates into one signature request and returns a URL that embeds the BoldSign sending experience inside your own application. |
| Create Sender Identity | `createSenderIdentity` | Requests a sender identity so signature requests can be sent on behalf of another email address once that address approves the invitation. |
| Create Team | `createTeam` | Creates a team so users and their documents can be grouped and administered together. |
| Create Template | `createTemplate` | Creates a reusable template with its roles and form fields, so the same document can be sent repeatedly. Supply the files as publicly reachable URLs; binary uploads cannot be sent through this connector. |
| Create User | `createUser` | Invites a person to the BoldSign account with a role and a team. BoldSign emails them an invitation they must accept. |
| Delete Brand | `deleteBrand` | Permanently deletes a branding profile. The account default brand cannot be deleted. |
| Delete Contact | `deleteContact` | Permanently removes a contact from the BoldSign address book. |
| Delete Contact Group | `deleteContactGroup` | Permanently deletes a contact group. Requires a BoldSign plan that includes contact groups. |
| Delete Custom Field | `deleteCustomField` | Permanently deletes a reusable custom form field from its brand. |
| Delete Document | `deleteDocument` | Moves a signature request to the BoldSign trash, or removes it permanently when permanent deletion is requested. |
| Delete Document Tags | `deleteDocumentTags` | Removes one or more labels from a document. |
| Delete Sender Identity | `deleteSenderIdentity` | Removes a sender identity, so requests can no longer be sent on behalf of that email address. |
| Delete Template | `deleteTemplate` | Permanently deletes a template. |
| Delete Template Tags | `deleteTemplateTags` | Removes labels from a template, either from the template itself or from the documents sent from it. |
| Download Document | `downloadDocument` | Downloads the PDF of a signature request. The response arrives as a file reference containing the document bytes. |
| Download Document Attachment | `downloadDocumentAttachment` | Downloads a file that a recipient uploaded into an attachment field on a signature request. |
| Download Document Audit Log | `downloadDocumentAuditLog` | Downloads the audit trail PDF that records every action taken on a signature request. |
| Download Template | `downloadTemplate` | Downloads the PDF of a template. The response arrives as a file reference containing the document bytes. |
| Edit Brand | `editBrand` | Updates an existing branding profile. Every setting is replaced, so supply the complete brand definition. The logo must be supplied as SVG markup; binary JPG or PNG logos cannot be sent through this connector. |
| Edit Custom Field | `editCustomField` | Updates a reusable custom form field. Send the complete definition, because the supplied values replace the stored ones. |
| Edit Document | `editDocument` | Updates an existing signature request, replacing the supplied properties such as title, message, recipients, expiry, branding and labels. Every recipient, file and form field entry must carry an edit action of Add, Update or Remove. Document time zone must be an IANA zone name such as Asia/Kolkata. |
| Edit Template | `editTemplate` | Updates an existing template, replacing the supplied properties such as title, description, roles, branding and sending options. BoldSign requires the signing-order flag to be supplied whenever roles are included. |
| Extend Document Expiry | `extendDocumentExpiry` | Pushes back the expiry of a signature request so pending recipients have more time to sign. |
| Get API Credit Balance | `getApiCreditBalance` | Returns the number of BoldSign API credits remaining on the account. |
| Get Brand | `getBrand` | Retrieves the full configuration of a single branding profile by its brand ID. |
| Get Contact | `getContact` | Retrieves a single address book contact by its contact ID. |
| Get Contact Group | `getContactGroup` | Retrieves a contact group with its members and directories. Requires a BoldSign plan that includes contact groups. |
| Get Document Properties | `getDocumentProperties` | Returns the full summary of a signature request, including its files, recipients, status, history, expiry and labels. |
| Get Embedded Sign Link | `getEmbeddedSignLink` | Returns a signing URL for one recipient so the signing experience can be embedded inside your own application. |
| Get Embedded Template Edit URL | `getEmbeddedTemplateEditUrl` | Returns a URL that embeds the BoldSign template editor for an existing template inside your own application. |
| Get Identity Verification Image | `getIdentityVerificationImage` | Retrieves the identity document or selfie image a recipient uploaded during identity verification. |
| Get Identity Verification Report | `getIdentityVerificationReport` | Returns the identity verification report for one recipient of a signature request, including the verification result and the details read from their identity document. |
| Get Sender Identity | `getSenderIdentity` | Retrieves a single sender identity by its identifier or by its email address. |
| Get Team | `getTeam` | Retrieves a team with its name and the users that belong to it. |
| Get Template Properties | `getTemplateProperties` | Returns the full definition of a template, including its roles, files, form fields and sending options. |
| Get User | `getUser` | Retrieves a single BoldSign user with their team, role and status. |
| List Behalf Documents | `listBehalfDocuments` | Lists signature requests sent on somebody else's behalf, or sent on your behalf by somebody else, with paging and the same filters as the main document list. |
| List Brands | `listBrands` | Lists every branding profile configured in the BoldSign account, including the default brand used for signature request emails and signing pages. |
| List Contact Groups | `listContactGroups` | Lists contact groups with paging, and optionally filters them by a search term matching the group name or a member email address. Requires a BoldSign plan that includes contact groups. |
| List Contacts | `listContacts` | Lists address book contacts with paging, and optionally filters them by a search term matching the contact name or email address. |
| List Custom Fields | `listCustomFields` | Lists every reusable custom form field configured on a brand. |
| List Documents | `listDocuments` | Lists the signature requests visible to the connected user, with paging and filters for status, date range, label, brand, sender and recipient. |
| List Sender Identities | `listSenderIdentities` | Lists the sender identities configured on the account, with paging and an optional search on name or email address. |
| List Team Documents | `listTeamDocuments` | Lists the signature requests belonging to the teams and users the connected account can administer. |
| List Teams | `listTeams` | Lists the teams configured on the account, with paging and an optional search on the team name. |
| List Templates | `listTemplates` | Lists the templates available to the connected user, with paging and filters for ownership, search term, label, brand, creator and date range. |
| List Users | `listUsers` | Lists the users on the BoldSign account, with paging and an optional search. |
| Merge Templates And Send | `mergeTemplatesAndSend` | Combines several templates into a single signature request and sends it, filling each merged role with a real recipient. |
| Prefill Document Fields | `prefillDocumentFields` | Writes values into named form fields of a signature request before the recipient opens it. |
| Re-Request Sender Identity | `reRequestSenderIdentity` | Asks again for approval of a sender identity that was previously denied. |
| Remind Document Recipients | `remindDocumentRecipients` | Sends a reminder to the recipients who have not yet completed a signature request. |
| Remove Document Authentication | `removeDocumentAuthentication` | Removes the identity check previously applied to a recipient of a signature request. |
| Resend Sender Identity Invitation | `resendSenderIdentityInvitation` | Sends the sender identity approval invitation again to an address that has not yet accepted it. |
| Resend User Invitation | `resendUserInvitation` | Sends the account invitation again to a user who has not yet accepted it. |
| Reset Default Brand | `resetDefaultBrand` | Makes the specified branding profile the account default, so new signature requests use it unless another brand is named. |
| Revoke Document | `revokeDocument` | Withdraws a signature request that is still in progress, so recipients can no longer sign it. |
| Send Document | `sendDocument` | Sends a document out for signature. Supply the files as publicly reachable URLs and describe each recipient with the form fields they must complete. BoldSign also accepts uploaded file bytes, but binary uploads cannot be sent through this connector, so use file URLs. |
| Send Document Using Template | `sendDocumentUsingTemplate` | Sends a signature request built from a template, filling each template role with a real recipient. |
| Send Draft Document | `sendDraftDocument` | Sends a document that is currently in draft status out to its recipients for signature. |
| Share Template | `shareTemplate` | Grants or revokes team access to a template, at either use-only or edit level. |
| Update Contact | `updateContact` | Updates an address book contact. Every supplied value replaces the stored one, so send the complete contact definition. |
| Update Contact Group | `updateContactGroup` | Updates the name, directories and membership of a contact group. Requires a BoldSign plan that includes contact groups. |
| Update Sender Identity | `updateSenderIdentity` | Updates the display name, notification settings, redirect URL, locale and metadata of a sender identity. |
| Update Team | `updateTeam` | Renames an existing team. |
| Update User | `updateUser` | Changes a user's role, or activates or deactivates them. When deactivating, their documents can be transferred to another user. |
| Update User Metadata | `updateUserMetadata` | Replaces the custom metadata stored against a BoldSign user. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Delivery Failed | `DeliveryFailed` | Fires when BoldSign cannot deliver the request to a recipient. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Delivery Failed, save. |
| Document Completed | `Completed` | Fires when every recipient has signed and the document is finished. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Completed, save. |
| Document Declined | `Declined` | Fires when a recipient declines to sign. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Declined, save. |
| Document Edit Failed | `EditFailed` | Fires when an edit to a document could not be applied. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Edit Failed, save. |
| Document Edited | `Edited` | Fires when an in-progress document is edited. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Edited, save. |
| Document Expired | `Expired` | Fires when a signature request passes its expiry date unsigned. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Expired, save. |
| Document Reassigned | `Reassigned` | Fires when a recipient passes the request to somebody else. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Reassigned, save. |
| Document Revoked | `Revoked` | Fires when the sender withdraws a signature request. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Revoked, save. |
| Document Send Failed | `SendFailed` | Fires when BoldSign could not send a signature request. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Send Failed, save. |
| Document Sent | `Sent` | Fires when a signature request is sent to its recipients. Setup (per BoldSign account): sign in at https://app.boldsign.com, open Settings &gt; API &gt; Webhooks, select Add Webhook, paste the fastn trigger URL as the endpoint, tick Sent under Document events, and save. Payload schema modelled from BoldSign's published WebhookEvent / DocumentEvent models in its OpenAPI specification, not from a captured delivery. |
| Document Viewed | `Viewed` | Fires when a recipient opens the document for the first time. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Viewed, save. |
| Draft Created | `DraftCreated` | Fires when a document is saved as a draft. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Draft Created, save. |
| Identity Verification Failed | `IdentityVerificationFailed` | Fires when a recipient fails identity verification. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Identity Verification Failed, save. |
| Identity Verification Started | `IdentityVerificationInitiated` | Fires when a recipient begins identity verification. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Identity Verification Initiated, save. |
| Identity Verification Succeeded | `IdentityVerificationSucceeded` | Fires when a recipient passes identity verification. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Identity Verification Succeeded, save. |
| Knowledge-Based Authentication Failed | `KBAFailed` | Fires when a recipient fails knowledge-based authentication. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick KBA Failed, save. |
| Knowledge-Based Authentication Started | `KBAInitiated` | Fires when a recipient begins knowledge-based authentication. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick KBA Initiated, save. |
| Knowledge-Based Authentication Succeeded | `KBASucceeded` | Fires when a recipient passes knowledge-based authentication. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick KBA Succeeded, save. |
| Recipient Authentication Failed | `AuthenticationFailed` | Fires when a recipient fails the access code or one-time passcode check. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Authentication Failed, save. |
| Recipient Progress Saved | `SignerSaved` | Fires when a recipient saves their progress without completing the document. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Signer Saved, save. |
| Recipient Signed | `Signed` | Fires when a recipient completes their part of a signature request. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Signed, save. |
| Recipient Verification | `Verification` | Fires when a recipient completes an identity check on a document. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Verification, save. |
| Reminder Sent | `Reminder` | Fires when a reminder goes out to a pending recipient. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Reminder, save. |
| Sender Identity Created | `SenderIdentityCreated` | Fires when a sender identity is requested. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Sender Identity Created under Sender identity events, save. |
| Sender Identity Deleted | `SenderIdentityDeleted` | Fires when a sender identity is removed. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Sender Identity Deleted, save. |
| Sender Identity Denied | `SenderIdentityDenied` | Fires when an invited address rejects a sender identity. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Sender Identity Denied, save. |
| Sender Identity Revoked | `SenderIdentityRevoked` | Fires when a sender identity's approval is withdrawn. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Sender Identity Revoked, save. |
| Sender Identity Updated | `SenderIdentityUpdated` | Fires when a sender identity is changed. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Sender Identity Updated, save. |
| Sender Identity Verified | `SenderIdentityVerified` | Fires when an invited address approves a sender identity. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Sender Identity Verified, save. |
| Template Created | `TemplateCreated` | Fires when a template is created. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Template Created under Template events, save. |
| Template Creation Failed | `TemplateCreateFailed` | Fires when a template could not be created. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Template Create Failed, save. |
| Template Draft Created | `TemplateDraftCreated` | Fires when a template is saved as a draft. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Template Draft Created, save. |
| Template Edited | `TemplateEdited` | Fires when a template is edited. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Template Edited, save. |
| Template Send Failed | `TemplateSendFailed` | Fires when a document could not be sent from a template. Setup: BoldSign web app &gt; Settings &gt; API &gt; Webhooks &gt; Add Webhook, paste the fastn trigger URL, tick Template Send Failed, save. |
