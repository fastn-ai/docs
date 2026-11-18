---
description: "Open-source Experience Management platform for surveys, forms, and in-product feedback."
hidden: true
---

# Formbricks

<img src="../../.gitbook/assets/connectors/lg/formbricks.png" alt="Formbricks logo">

Open-source Experience Management platform for surveys, forms, and in-product feedback. Manage surveys, responses, contacts, action classes, webhooks, teams, and contact attributes via the Formbricks Management API.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [formbricks.com](https://formbricks.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `formbricks` |

## Use it

Add Formbricks from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.formbricks.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Upload Contacts | `bulkUploadContacts` | Creates or updates up to 250 contacts at once. Each contact must include an email attribute; userId is used to de-duplicate against existing contacts. Contacts is an Enterprise Edition feature and requires an upgraded plan. |
| Create Action Class | `createActionClass` | Creates a new action class - a user action (code-triggered or no-code, e.g. click/page view/exit intent) that can be used to trigger surveys. |
| Create Contact | `createContact` | Creates a new contact with a flat map of attributes. An email attribute is required and must be a valid email address. Contacts is an Enterprise Edition feature and requires an upgraded plan. |
| Create Contact Attribute Key | `createContactAttributeKey` | Defines a new custom contact attribute key that can then be set as a value on individual contacts. Contacts is an Enterprise Edition feature and requires an upgraded plan. |
| Create Response | `createResponse` | Submits a new response to a survey. The data object maps question IDs to the respondent's answers. |
| Create Survey | `createSurvey` | Creates a new survey in a workspace. Requires a name and at least one question. Surveys are created in draft status by default and can be published by updating their status to inProgress. |
| Create Team | `createTeam` | Creates a new team within an organization, used to group members and grant them access to specific workspaces. |
| Create Webhook | `createWebhook` | Registers a new webhook that posts a notification to your URL when survey response events occur. The response includes a one-time signing secret used to verify deliveries. |
| Delete Action Class | `deleteActionClass` | Deletes an action class. Fails if it is still referenced as a trigger on any survey. |
| Delete Contact | `deleteContact` | Deletes a contact. Contacts is an Enterprise Edition feature and requires an upgraded plan. |
| Delete Contact Attribute Key | `deleteContactAttributeKey` | Deletes a contact attribute key definition and removes it from all contacts. Contacts is an Enterprise Edition feature and requires an upgraded plan. |
| Delete Response | `deleteResponse` | Permanently deletes a single survey response. |
| Delete Survey | `deleteSurvey` | Permanently deletes a survey and its responses. |
| Delete Team | `deleteTeam` | Deletes a team from an organization. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook so it stops receiving event notifications. |
| Get Action Class | `getActionClass` | Retrieves a single action class (user action/trigger) by its ID. |
| Get API Key Info | `getApiKeyInfo` | Returns the workspace and project that this API key belongs to. Useful for verifying which environment a connection is scoped to. |
| Get Contact | `getContact` | Retrieves a single contact by its ID, including its attributes. Contacts is an Enterprise Edition feature and requires an upgraded plan. |
| Get Contact Attribute Key | `getContactAttributeKey` | Retrieves a single contact attribute key by its ID. Contacts is an Enterprise Edition feature and requires an upgraded plan. |
| Get Current Permissions | `getCurrentPermissions` | Returns this API key's workspace and organization-level permissions, including which workspaces it can manage and its organization access level. |
| Get Response | `getResponse` | Retrieves a single survey response by its ID. |
| Get Survey | `getSurvey` | Retrieves a single survey by its ID, including its full question/block structure, welcome card, endings, and settings. |
| Get Survey Single-Use Links | `getSurveySingleUseLinks` | Generates single-use survey links for a link survey, each usable for exactly one response. Useful for sending personalized, one-time survey invitations. |
| Get Team | `getTeam` | Retrieves a single team within an organization by its ID. |
| Get Webhook | `getWebhook` | Retrieves a single webhook by its ID. |
| List Action Classes | `listActionClasses` | Lists all action classes (user actions/triggers that can start a survey) across every workspace the API key can access. |
| List Contact Attribute Keys | `listContactAttributeKeys` | Lists all contact attribute keys (definitions used to segment contacts, e.g. email, plan, company) across every workspace the API key can access. Contacts is an Enterprise Edition feature and requires an upgraded plan. |
| List Contact Attributes | `listContactAttributes` | Lists all contact attribute values (the actual data stored per contact) across every workspace the API key can access. Read-only. Contacts is an Enterprise Edition feature and requires an upgraded plan. |
| List Contacts | `listContacts` | Lists contacts (survey respondents) across every workspace the API key can access. Contacts is an Enterprise Edition feature and requires an upgraded plan. |
| List Organization Users | `listOrganizationUsers` | Lists the members of an organization. Note: on Formbricks Cloud, inviting or removing organization members via the API is not available - use the dashboard for member management. |
| List Responses | `listResponses` | Lists survey responses, optionally filtered by survey, contact, or a date range, with sorting and pagination. |
| List Roles | `listRoles` | Lists the organization role identifiers available to assign to members (e.g. owner, manager, member, billing). |
| List Surveys | `listSurveys` | Lists all surveys the API key can access, across every workspace it has permission for. Supports pagination via limit and offset. |
| List Teams | `listTeams` | Lists all teams within an organization. |
| List Webhooks | `listWebhooks` | Lists webhooks across every workspace the API key can access, optionally filtered to specific surveys. |
| Update Action Class | `updateActionClass` | Updates the name, description, or configuration of an existing action class. |
| Update Contact Attribute Key | `updateContactAttributeKey` | Updates the display name, description, or uniqueness constraint of a contact attribute key. Contacts is an Enterprise Edition feature and requires an upgraded plan. |
| Update Response | `updateResponse` | Fully replaces an existing survey response. Formbricks treats this as a full PUT replace, not a partial patch: every field below must be sent (use null for fields with no value) or the API returns 422 for the missing ones. |
| Update Survey | `updateSurvey` | Replaces an existing survey's fields, such as its name, status, or questions. Use status to publish (inProgress), pause, or complete a survey. |
| Update Team | `updateTeam` | Renames an existing team within an organization. |
| Update Webhook | `updateWebhook` | Fully replaces a webhook's name, URL, source, triggers, and survey scoping (PUT is a full replace, not a partial patch). |
| Upload File | `uploadFile` | Requests a signed upload URL for a public file (such as a survey image or logo) in a workspace's file storage. |
