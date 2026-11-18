---
description: "Zoho Contracts is Zoho's contract lifecycle management (CLM) application."
hidden: true
---

# Zoho Contracts

Zoho Contracts is Zoho's contract lifecycle management (CLM) application. This connector wraps the Zoho Contracts REST API v1 (contracts.zoho.com/api/v1): organization info, active users, departments, contract types and template fields, counterparties, counterparty types and counterparty contacts, contracts (create, import, draft completion, update, delete, ownership transfer and the contract lists), collaborators, approval, negotiation, signature, attachments and links, document downloads, obligation categories and obligations with their tasks.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [contracts.zoho.com](https://contracts.zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 86 |
| **Events** | 0 |
| **Slug** | `zohoContracts` |

## Use it

Add Zoho Contracts from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoContracts.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Collaborators | `addCollaborators` | Adds one or more collaborators to a contract in Zoho Contracts, granting each a document permission and optionally sending them a notification email. |
| Add Link | `addLink` | Attaches one or more web links to a contract in Zoho Contracts. |
| Add New Negotiators And Notify | `addNegotiators` | Adds further negotiators to a contract already in negotiation in Zoho Contracts and notifies them. Offline delivery requires a password of at least eight characters. |
| Add Signature Details | `addSignatureDetails` | Configures the signers of a contract in Zoho Contracts, covering organization and counterparty representatives, other representatives, receivers, in-person signer hosts, signing order and per-signer authentication. |
| Attach File | `attachFile` | Attaches one or more previously uploaded files to a contract in Zoho Contracts, using the upload IDs returned by the Upload Contract Attachment action. |
| Complete Contract Draft | `completeContractDraft` | Marks a contract's draft as complete in Zoho Contracts, moving it to the Draft Completed stage. Requires the ZohoWriter document editor scope. |
| Create Contract | `createContract` | Creates a contract in Zoho Contracts. Field values are supplied through the inputfields array, where each entry names a template field (metaApiName) and carries one or more inputApiName and inputValue pairs. Use Get Contract Type Template Fields to discover the valid API names. |
| Create Contract Type | `createContractType` | Creates a contract type in the Zoho Contracts organization, defining its intent, contracting parties, categories and approval workflow. Requires admin privilege. |
| Create Contract With Document Field Values | `createContractWithDocumentFields` | Creates a contract in Zoho Contracts and populates the fields embedded in the contract document as well as the form fields. Custom date fields in the document must be supplied as a timestamp in milliseconds. Requires the ZohoWriter document editor scope when the contract type template is an uploaded one. |
| Create Counterparty | `createCounterparty` | Creates a counterparty in Zoho Contracts with its address, website and counterparty type, optionally seeding its counterparty contacts. |
| Create Counterparty Contact | `createCounterpartyContact` | Creates a contact under an existing counterparty in Zoho Contracts. Counterparty contacts are the people who can be added as negotiators or signers on a contract. |
| Create Counterparty Type | `createCounterpartyType` | Creates a counterparty type in the Zoho Contracts organization, used to categorise counterparties such as Procurement or Sales. Requires admin privilege. |
| Create Department | `createDepartment` | Creates a department in the Zoho Contracts organization. Requires admin privilege. |
| Create Obligation | `createObligation` | Creates an obligation on a contract in Zoho Contracts. When the obligation is a task, supply either the oneTime or the recurring object; when it is not, omit both. |
| Create Obligation Category | `createObligationCategory` | Creates an obligation category in the Zoho Contracts organization, used to group contract obligations. Requires admin privilege. |
| Delete Attachment | `deleteAttachment` | Removes a file or link attachment from a contract in Zoho Contracts. |
| Delete Collaborator | `deleteCollaborator` | Removes a collaborator from a contract in Zoho Contracts. |
| Delete Contract | `deleteContract` | Deletes a contract from Zoho Contracts, identified by its API name. |
| Delete Contract Type | `deleteContractType` | Deletes a contract type from the Zoho Contracts organization. Requires admin privilege. |
| Delete Counterparty | `deleteCounterparty` | Deletes a counterparty from Zoho Contracts, identified by its organization API name. |
| Delete Counterparty Contact | `deleteCounterpartyContact` | Deletes a counterparty contact from Zoho Contracts, optionally anonymising the contact's details wherever they are still displayed. |
| Delete Counterparty Type | `deleteCounterpartyType` | Deletes a counterparty type from the Zoho Contracts organization. Requires admin privilege. |
| Delete Department | `deleteDepartment` | Deletes a department from the Zoho Contracts organization. Requires admin privilege. |
| Delete Negotiator | `deleteNegotiator` | Removes a negotiator from a contract in Zoho Contracts. Applies while the contract is in the Negotiation Review Pending status. |
| Delete Obligation | `deleteObligation` | Deletes an obligation from a contract in Zoho Contracts. |
| Delete Obligation Category | `deleteObligationCategory` | Deletes an obligation category from the Zoho Contracts organization. Requires admin privilege. |
| Download Active Document | `downloadActiveDocument` | Downloads the currently active document of a contract from Zoho Contracts in DOCX format. The response is a binary file rather than JSON. |
| Download Attached File | `downloadAttachedFile` | Downloads a file attached to a contract in Zoho Contracts. The response is a binary file rather than JSON. |
| Download Signature Completion Certificate | `downloadSignatureCompletionCertificate` | Downloads the signature completion certificate of a contract from Zoho Contracts. The response is a binary file rather than JSON. |
| Download Signed Document | `downloadSignedDocument` | Downloads the signed PDF document of a contract from Zoho Contracts. The response is a binary file rather than JSON. |
| Edit Link | `editLink` | Updates the display name or target URL of a link attached to a contract in Zoho Contracts. |
| Edit Signature Details | `editSignatureDetails` | Updates the signer configuration of a contract in Zoho Contracts before it is sent for signature, including signer order, authentication and the signing deadline. |
| Get Active Users | `getActiveUsers` | Returns the active users of the Zoho Contracts organization, with their display name, email address and user ID. |
| Get All Attachments | `getAllAttachments` | Returns the files and links attached to a contract in Zoho Contracts. |
| Get All Contracts List | `getAllContractsList` | Returns every contract in the Zoho Contracts organization. Requires admin privilege. Use Get Contracts List for the contracts owned by the current user. |
| Get All Obligations List | `getAllObligationsList` | Returns the obligations owned by the current Zoho Contracts user across all contracts, with their task instances. |
| Get Collaborators | `getCollaborators` | Returns the collaborators on a contract in Zoho Contracts along with the document permission each one holds. |
| Get Contract | `getContract` | Returns the metadata of a single contract in Zoho Contracts, including its owner, contract type, counterparty, term, renewal settings, amount and amendment history. |
| Get Contract Document Fields With Values | `getContractDocumentFields` | Returns the fields embedded in a contract's document along with their current values and data types. |
| Get Contract Type | `getContractType` | Returns the details of a single contract type available to the current Zoho Contracts user, identified by its API name. |
| Get Contract Type Template All Fields | `getContractTypeTemplateAllFields` | Returns every field defined on a contract type's template in Zoho Contracts, including fields that are not currently enabled. |
| Get Contract Type Template Fields | `getContractTypeTemplateFields` | Returns the fields enabled on a contract type's template in Zoho Contracts. Use the returned API names as the metaApiName and inputApiName values when creating or updating a contract. |
| Get Contract Type Using Admin Privilege | `getContractTypeAdmin` | Returns the details of a single contract type in the Zoho Contracts organization, identified by its API name. Requires admin privilege. |
| Get Contract Types List | `getContractTypesList` | Returns the contract types available to the current Zoho Contracts user. Use Get Contract Types List Using Admin Privilege to list every contract type in the organization. |
| Get Contract Types List Using Admin Privilege | `getContractTypesListAdmin` | Returns every contract type configured in the Zoho Contracts organization. Requires admin privilege. |
| Get Contracts List | `getContractsList` | Returns the contracts owned by the current Zoho Contracts user. |
| Get Counterparties List | `getCounterpartiesList` | Returns the counterparties (contracting organizations) recorded in Zoho Contracts, with their address details and counterparty type. |
| Get Counterparty | `getCounterparty` | Returns the details of a single counterparty in Zoho Contracts, identified by its organization API name. |
| Get Counterparty Contacts | `getCounterpartyContacts` | Returns the contacts belonging to a counterparty in Zoho Contracts. Their IDs are the values used when adding negotiators or signers to a contract. |
| Get Counterparty Types List | `getCounterpartyTypesList` | Returns the counterparty types available to the current Zoho Contracts user. Use Get Counterparty Types List Using Admin Privilege to list every counterparty type in the organization. |
| Get Counterparty Types List Using Admin Privilege | `getCounterpartyTypesListAdmin` | Returns every counterparty type configured in the Zoho Contracts organization. Requires admin privilege. |
| Get Departments List | `getDepartmentsList` | Returns the departments available to the current Zoho Contracts user. Use Get Departments List Using Admin Privilege to list every department in the organization. |
| Get Departments List Using Admin Privilege | `getDepartmentsListAdmin` | Returns every department configured in the Zoho Contracts organization. Requires admin privilege. |
| Get Obligation Categories List | `getObligationCategoriesList` | Returns the obligation categories available to the current Zoho Contracts user. |
| Get Obligation Categories List Using Admin Privilege | `getObligationCategoriesListAdmin` | Returns every obligation category configured in the Zoho Contracts organization. Requires admin privilege. |
| Get Obligation Contracts List | `getObligationContractsList` | Returns the contracts on which the current Zoho Contracts user owns at least one obligation. |
| Get Obligations List | `getObligationsList` | Returns the obligations recorded against a single contract in Zoho Contracts. |
| Get Organization Info | `getOrganizationInfo` | Returns the profile of the connected Zoho Contracts organization, including its name, API name, address, currency and account owner. |
| Get Pending Obligations List | `getPendingObligationsList` | Returns the obligations still pending for the current Zoho Contracts user across all contracts. |
| Get Shared Contracts List | `getSharedContractsList` | Returns the contracts that have been shared with the current Zoho Contracts user as a collaborator. |
| Get Sign Settings | `getSignSettings` | Returns the signing configuration of a contract in Zoho Contracts, including reminder days, the number of days allowed for completion and the paper type used for signing. |
| Get Signers List | `getSignersList` | Returns the signers configured on a contract in Zoho Contracts, including organization and counterparty representatives, other representatives and receivers. |
| Get Tasks List Of A Pending Obligation | `getPendingObligationTasks` | Returns the task instances of a pending obligation for the current Zoho Contracts user. |
| Get Tasks List Of An Obligation | `getObligationTasks` | Returns the task instances of an obligation owned by the current Zoho Contracts user. |
| Go Back For Negotiation | `goBackForNegotiation` | Reverts a contract in Zoho Contracts back to the negotiation stage. |
| Import Contract | `importContract` | Imports an existing contract into Zoho Contracts in a Draft, Signed, Active or Expired state, using the upload IDs returned by the Upload Contract File action. Importing signed or expired contracts together with their amendment or renewal history is not supported. |
| Rename Attached File | `renameAttachedFile` | Renames a file attached to a contract in Zoho Contracts. |
| Send Contract For Negotiation | `sendForNegotiation` | Sends a contract for negotiation in Zoho Contracts to a set of counterparty negotiators, by email or offline delivery. Offline delivery requires a password of at least eight characters. Requires the ZohoWriter document editor scope. |
| Send Contract For Signature | `sendForSignature` | Sends a contract for signature in Zoho Contracts, moving it to the Sign Pending stage. Signature fields must already be placed in the document for every signer, and the call consumes Zoho Sign credits. |
| Skip Negotiation | `skipNegotiation` | Skips the negotiation stage of a contract in Zoho Contracts, advancing it without sending the document to counterparty negotiators. |
| Submit Contract For Approval | `submitForApproval` | Submits a contract for approval in Zoho Contracts, moving it to the Approval Pending stage. |
| Transfer Contract Ownership | `transferContractOwnership` | Transfers ownership of one or more contracts in Zoho Contracts to new owners, identified by their email addresses. Requires admin privilege. |
| Update Collaborators | `updateCollaborators` | Changes the document permission held by one or more existing collaborators on a contract in Zoho Contracts. |
| Update Contract | `updateContract` | Updates the field values of an existing contract in Zoho Contracts. Only the fields named in the inputfields array are changed; every other value on the contract is left untouched. |
| Update Contract Type | `updateContractType` | Renames an existing contract type in the Zoho Contracts organization. Requires admin privilege. |
| Update Counterparty | `updateCounterparty` | Updates an existing counterparty in Zoho Contracts, changing its counterparty type or address details. Only the fields supplied are sent. |
| Update Counterparty Contact | `updateCounterpartyContact` | Updates the name or email address of an existing counterparty contact in Zoho Contracts. Only the fields supplied are sent. |
| Update Counterparty Type | `updateCounterpartyType` | Renames an existing counterparty type in the Zoho Contracts organization. Requires admin privilege. |
| Update Department | `updateDepartment` | Renames an existing department in the Zoho Contracts organization. Requires admin privilege. |
| Update Negotiators | `updateNegotiators` | Updates the delivery mode, access permission or offline password of the negotiators on a contract in Zoho Contracts. |
| Update Obligation | `updateObligation` | Updates an existing obligation on a contract in Zoho Contracts, changing its name or its recurrence schedule. Only the fields supplied are sent. |
| Update Obligation Category | `updateObligationCategory` | Renames an existing obligation category in the Zoho Contracts organization. Requires admin privilege. |
| Update Obligation Status | `updateObligationStatus` | Updates the status of a task instance within an obligation on a contract in Zoho Contracts, for example marking it completed or paused. |
| Update Organization Info | `updateOrganizationInfo` | Updates the profile of a Zoho Contracts organization, including its name, address, website and phone number. Only the fields supplied are sent. |
| Upload Contract Attachment | `uploadContractAttachment` | Uploads a file against a contract in Zoho Contracts and returns the upload ID used by the Attach File action. Each file is uploaded separately and the combined size of a contract's attachments must not exceed 100 MB. The request is multipart/form-data. |
| Upload Contract File | `uploadContractFile` | Uploads a contract document to Zoho Contracts and returns the upload ID used by the Import Contract action. Each document is uploaded separately and the module query parameter names which document type is being sent. The request is multipart/form-data. |
