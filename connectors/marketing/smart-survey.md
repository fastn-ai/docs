---
description: "SmartSurvey is a UK-based online survey and feedback platform."
hidden: true
---

# SmartSurvey

SmartSurvey is a UK-based online survey and feedback platform. This connector covers the documented SmartSurvey Public API v2: surveys and survey folders, pages, responses, tracking links and collectors, invitations and their recipients, contact lists and contacts, exports and downloads, filter groups, sharing permissions, themes, the file library, account users, API keys, and webhook registration.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Authentication** | Basic auth |
| **Actions** | 89 |
| **Events** | 0 |
| **Slug** | `smartSurvey` |

## Use it

Add SmartSurvey from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.smartSurvey.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Contact To List | `createContactListContact` | Adds a new contact to the specified contact list. |
| Close Survey | `closeSurvey` | Closes a survey to new responses by closing every one of its tracking links. |
| Close Survey Tracking Link | `closeSurveyTrackingLink` | Closes a single tracking link so that it stops accepting responses. |
| Copy Survey | `copySurvey` | Copies a survey into a new survey, optionally placing it in a folder or on a sub-user account. |
| Copy Survey Tracking Link | `copySurveyTrackingLink` | Copies a tracking link into a new tracking link on the same survey. |
| Copy Theme | `copyTheme` | Copies an existing or template theme into a new theme on the account. |
| Create API Key | `createApiKey` | Creates a new API key on the SmartSurvey account and returns the key together with its secret. |
| Create Contact List | `createContactList` | Creates a new email contact list on the account. |
| Create Contact List With Custom Columns | `createContactListWithColumns` | Creates a new email contact list together with the custom columns its contacts will carry. |
| Create File Library Folder | `createFileLibraryFolder` | Creates a new folder in the account file library. |
| Create Survey | `createSurvey` | Creates a new survey on the account. |
| Create Survey Folder | `createSurveyFolder` | Creates a new survey folder on the account. |
| Create Survey Page | `createSurveyPage` | Adds a new page to the end of a survey. |
| Create Survey Response | `createSurveyResponse` | Records a survey response programmatically, marked as completed, partial or disqualified. |
| Create Survey Tracking Link | `createSurveyTrackingLink` | Creates a new tracking link of the given type on a survey. |
| Create Webhook | `createWebhook` | Registers a new webhook so SmartSurvey posts survey events to the supplied endpoint URL. |
| Delete All Survey Permissions | `deleteAllSurveyPermissions` | Removes every sharing permission from a survey, leaving only the owner with access. |
| Delete API Key | `deleteApiKey` | Permanently deletes an API key from the account by its identifier. |
| Delete Contact List | `deleteContactList` | Permanently deletes a contact list and all of the contacts it holds. |
| Delete Survey | `deleteSurvey` | Permanently deletes a survey and all of its responses without confirmation. |
| Delete Survey Export | `deleteSurveyExport` | Permanently deletes a generated survey export. |
| Delete Survey Page | `deleteSurveyPage` | Permanently deletes a survey page and the questions on it. |
| Delete Survey Permission For Member | `deleteSurveyPermission` | Removes all sharing permissions held by a single account member on a survey. |
| Delete Survey Response | `deleteSurveyResponse` | Permanently deletes a single survey response. |
| Delete Survey Tracking Link | `deleteSurveyTrackingLink` | Permanently deletes a survey tracking link and the responses collected through it. |
| Delete Theme | `deleteTheme` | Permanently deletes a survey theme from the account. |
| Delete Webhook | `deleteWebhook` | Permanently deletes a registered webhook so SmartSurvey stops delivering events to it. |
| Download Latest Survey Export | `downloadLatestSurveyExport` | Downloads the most recently generated export for a survey. Responses are cached for ten seconds, so avoid polling this endpoint. |
| Download Latest Survey Export By Type | `downloadLatestSurveyExportByType` | Downloads the most recent export of a given report type for a survey. Responses are cached for ten seconds, so avoid polling this endpoint. |
| Download Survey Export | `downloadSurveyExport` | Downloads a previously generated survey export as a file. |
| Get Account User | `getAccountUser` | Retrieves a single user on the SmartSurvey account by its identifier. |
| Get API Key | `getApiKey` | Retrieves a single API key on the account by its identifier. |
| Get Contact In List | `getContactListContact` | Retrieves a single contact from a contact list by its mail user identifier. |
| Get Contact In List With Details | `getContactListContactDetailed` | Retrieves a single contact from a contact list including its custom column values. |
| Get Contact List | `getContactList` | Retrieves the summary information for a single contact list. |
| Get Contact List Details | `getContactListDetailed` | Retrieves the full detail record for a single contact list, including its custom columns. |
| Get Current Account User | `getCurrentAccountUser` | Retrieves the account user that owns the API key making the request. |
| Get File Library Folder | `getFileLibraryFolder` | Retrieves the summary information for a single file library folder. |
| Get File Library Folder Details | `getFileLibraryFolderDetailed` | Retrieves a file library folder together with its child folders and files. |
| Get Survey | `getSurvey` | Retrieves the summary information for a single survey. |
| Get Survey Details | `getSurveyDetailed` | Retrieves the full detail record for a survey, including its pages and settings. |
| Get Survey Export | `getSurveyExport` | Retrieves the status and metadata of a single survey export. |
| Get Survey Folder | `getSurveyFolder` | Retrieves a single survey folder by its identifier. |
| Get Survey Folder Details | `getSurveyFolderDetailed` | Retrieves a survey folder together with the surveys it contains. |
| Get Survey Invitation | `getSurveyInvitation` | Retrieves a single survey invitation by its identifier. |
| Get Survey Owner Information | `getSurveyOwnerInfo` | Retrieves the account details of the survey owner alongside basic survey metadata. |
| Get Survey Page | `getSurveyPage` | Retrieves a single survey page by its identifier. |
| Get Survey Page Details | `getSurveyPageDetailed` | Retrieves a survey page together with the questions and answer options it contains. |
| Get Survey Response | `getSurveyResponse` | Retrieves a single survey response and its answers by identifier. |
| Get Survey Tracking Link | `getSurveyTrackingLink` | Retrieves the full detail of a single survey tracking link. |
| Get Theme | `getTheme` | Retrieves a single survey theme by its identifier. |
| Get Webhook | `getWebhook` | Retrieves a single registered webhook by its identifier. |
| List Account Users | `listAccountUsers` | Retrieves every user on the SmartSurvey account, one page at a time. |
| List API Keys | `listApiKeys` | Retrieves every API key configured on the SmartSurvey account. |
| List Contact Lists | `listContactLists` | Retrieves every email contact list on the account, one page at a time. |
| List Contacts In List | `listContactListContacts` | Retrieves the contacts held in a contact list, one page at a time. |
| List Contacts In List With Details | `listContactListContactsDetailed` | Retrieves the contacts in a contact list including their custom column values, one page at a time. |
| List File Library Files | `listFileLibraryFiles` | Retrieves every file in the account file library, one page at a time. |
| List File Library Folders | `listFileLibraryFolders` | Retrieves every folder in the account file library, one page at a time. |
| List Files In Folder | `listFileLibraryFolderFiles` | Retrieves the files held in a single file library folder. |
| List Shared Themes | `listSharedThemes` | Retrieves the themes shared with the account by its parent account. Returns an empty list when the account has no parent. |
| List Survey Exports | `listSurveyExports` | Retrieves the exports generated for a survey, one page at a time. |
| List Survey Filter Groups | `listSurveyFilterGroups` | Retrieves the response filter groups defined on a survey. |
| List Survey Folders | `listSurveyFolders` | Retrieves every survey folder on the account. |
| List Survey Invitation Fields | `listSurveyInvitationFields` | Retrieves the custom contact-list fields available to an invitation for personalisation. |
| List Survey Invitation Recipients | `listSurveyInvitationRecipients` | Retrieves the recipients of an invitation and their delivery status, one page at a time. |
| List Survey Invitations | `listSurveyInvitations` | Retrieves the email invitations configured on a survey, one page at a time. |
| List Survey Pages | `listSurveyPages` | Retrieves the pages of a survey, one page of results at a time. |
| List Survey Permissions | `listSurveyPermissions` | Retrieves the sharing permissions granted on a survey. |
| List Survey Responses | `listSurveyResponses` | Retrieves the responses submitted to a survey, one page at a time. |
| List Survey Tracking Links | `listSurveyTrackingLinks` | Retrieves the tracking links, or collectors, on a survey, one page at a time. |
| List Surveys | `listSurveys` | Retrieves every survey on the account, one page at a time. |
| List Theme Templates | `listThemeTemplates` | Retrieves the SmartSurvey theme templates that any account can copy as a starting point. |
| List Themes | `listThemes` | Retrieves every survey theme on the account. |
| List Webhooks | `listWebhooks` | Retrieves every webhook registered on the account. |
| Open Survey | `openSurvey` | Opens a survey for responses by opening its default tracking link. |
| Open Survey Tracking Link | `openSurveyTrackingLink` | Opens a single tracking link so that it accepts responses. |
| Print Survey | `printSurvey` | Renders a survey as HTML, Word or PDF for printing or offline review. |
| Replace Survey Export Email Addresses | `replaceSurveyExportEmails` | Finds and replaces a recipient email address across all future scheduled exports on a survey. |
| Send Survey Invitation | `sendSurveyInvitation` | Sends a survey invitation email to one or more recipients. This is a premium endpoint and it delivers real email, so call it only against recipients who have consented. |
| Send Survey Invitation To One Recipient | `sendSurveyInvitationToOne` | Sends a survey invitation email to a single recipient. This is a premium endpoint and it delivers real email, so call it only against recipients who have consented. |
| Set Survey Permissions | `setSurveyPermissions` | Grants or updates the sharing permissions held by an account member on a survey. Only the fields supplied are changed. |
| Update API Key | `updateApiKey` | Updates the name, permissions or expiry of an existing API key. |
| Update Survey Page | `updateSurveyPage` | Updates the title, description or CSS class of an existing survey page. |
| Update Survey Results Sharing | `updateSurveyResultSharing` | Turns public results sharing on or off for a survey and sets the sharing options. |
| Update Survey Tracking Link | `updateSurveyTrackingLink` | Updates the title of an existing survey tracking link. |
| Update Survey Tracking Link Auto Close Date | `updateSurveyTrackingLinkAutoCloseDate` | Sets the date on which a tracking link closes itself automatically. |
| Update Survey Tracking Link Text | `updateSurveyTrackingLinkText` | Changes the vanity text of a web tracking link, provided the new text is available. |
| Update Webhook | `updateWebhook` | Updates the endpoint URL, events or state of a registered webhook. |
