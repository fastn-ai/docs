---
description: "Certifier is a platform for issuing digital certificates and badges."
hidden: true
---

# Certifier

Certifier is a platform for issuing digital certificates and badges. This connector covers the full Certifier REST API v1: creating, listing, searching, retrieving, updating, issuing, sending and deleting credentials, reading a credential's design template previews, listing and creating credential interaction events, full CRUD on credential templates (groups), and reading certificate and badge design templates.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [certifier.io](https://certifier.io) |
| **Authentication** | Bearer token |
| **Actions** | 19 |
| **Events** | 0 |
| **Slug** | `certifier` |

## Use it

Add Certifier from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.certifier.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Credential | `createCredential` | Creates a new credential with status draft against a credential template (group). Issue it afterwards with Issue Credential to make it active and visible in the digital wallet, then deliver it with Send Credential. |
| Create Credential Interaction | `createCredentialInteraction` | Records a credential interaction event, such as the credential being viewed, downloaded, verified or shared to a social network, against a credential. |
| Create Credential Template | `createCredentialTemplate` | Creates a credential template (group) from one or more existing design templates. Design templates themselves are created in the Certifier dashboard, so obtain their IDs from List Design Templates first. |
| Create Issue And Send Credential | `createIssueAndSendCredential` | Creates, issues and emails a credential in one call. The recipient receives the credential by email immediately, so only call this with a real recipient address you intend to contact. |
| Delete Credential | `deleteCredential` | Permanently deletes a credential. This cannot be undone. |
| Delete Credential Template | `deleteCredentialTemplate` | Permanently deletes a credential template (group). This cannot be undone. |
| Get Credential | `getCredential` | Returns a single credential by its unique identifier, including its status, recipient, issue and expiry dates, attributes and custom attributes. |
| Get Credential Design Templates | `getCredentialDesignTemplates` | Returns the ordered design templates used by a credential together with their PNG and PDF preview URLs. Preview URLs are immutable and versioned by a digest of the design template and the credential's rendered attribute values, so fetch this again after any change to get the newest preview. |
| Get Credential Template | `getCredentialTemplate` | Returns a single credential template (group) by its unique identifier, including its name, associated design template IDs and learning event URL. |
| Get Design Template | `getDesignTemplate` | Returns a single certificate or badge design template by its unique identifier, including its name, type and PNG preview URL. |
| Issue Credential | `issueCredential` | Issues a draft credential, changing its status from draft to issued and making it active and accessible in the digital wallet. Only credentials with status draft can be issued. Deliver it afterwards with Send Credential. |
| List Credential Interactions | `listCredentialInteractions` | Returns a cursor-paginated list of credential interaction events such as views, downloads, verifications and social shares, optionally narrowed to a single credential. |
| List Credential Templates | `listCredentialTemplates` | Returns a cursor-paginated list of the credential templates (groups) in your workspace. A credential template ties together the design templates and settings used when a credential is issued. |
| List Credentials | `listCredentials` | Returns a cursor-paginated list of the credentials in your Certifier workspace, each with its status, recipient, issue and expiry dates and attributes. |
| List Design Templates | `listDesignTemplates` | Returns a cursor-paginated list of all certificate and badge design templates available in your workspace, each with a direct PNG preview URL. Design templates are created in the Certifier dashboard, not through the API. |
| Search Credentials | `searchCredentials` | Finds credentials using a structured filter expression with AND, OR and NOT operators, optional sorting and cursor pagination. Filterable fields are id, publicId, groupId, status, recipientId, recipient.name, recipient.email, issueDate, expiryDate, createdAt and updatedAt. |
| Send Credential | `sendCredential` | Delivers an already issued credential to its recipient by email. Only credentials with status issued can be sent, and the recipient must have an email address. This sends a real email, so only call it for recipients you intend to contact. |
| Update Credential | `updateCredential` | Updates a credential's recipient, issue date, expiry date or custom attributes. Only the fields you supply are changed; set Expiry Date to null to clear it. |
| Update Credential Template | `updateCredentialTemplate` | Updates a credential template (group). Only the fields you supply are changed; supplying Design Template IDs replaces the whole ordered list. |
