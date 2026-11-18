---
description: "SurveyMonkey API v3."
---

# SurveyMonkey

SurveyMonkey API v3. Create and manage surveys, pages, questions, collectors, invite messages and recipients, responses, contacts and contact lists, webhooks, survey folders, templates, translations, benchmarks, teams/groups, workgroups, roles and organizations. Supports the US, EU and Canadian datacenters via a configurable API access URL.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [surveymonkey.com](https://surveymonkey.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 145 |
| **Events** | 0 |
| **Slug** | `surveymonkey` |

## Use it

Add SurveyMonkey from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.surveymonkey.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Workgroup Member | `addWorkgroupMember` | Add a user to a workgroup. Requires a paid plan (workgroups_members_write scope). |
| Add Workgroup Members In Bulk | `addWorkgroupMembersBulk` | Add several users to a workgroup in a single request. Requires a paid plan (workgroups_members_write scope). |
| Analyze Benchmark Bundle | `analyzeBenchmarkBundle` | Retrieve benchmark analytics for the questions in a benchmark bundle. |
| Copy Contact List | `copyContactList` | Create a copy of a contact list, including its contacts. |
| Create Collector Message | `createCollectorMessage` | Create an invite, reminder or thank you message on an email or SMS collector. |
| Create Collector Response | `createCollectorResponse` | Create a response on a collector. Requires a paid plan (responses_write scope). |
| Create Contact | `createContact` | Create a contact in the user's account. |
| Create Contact In List | `createContactInList` | Create a contact in a contact list. |
| Create Contact List | `createContactList` | Create a contact list. |
| Create Contacts In Bulk | `createContactsBulk` | Create several contacts in the user's account in a single request. |
| Create Contacts In List In Bulk | `createContactsInListBulk` | Create several contacts in a contact list in a single request. |
| Create Message Recipient | `createMessageRecipient` | Add a recipient to an invite message, either by supplying contact details or by referencing an existing contact ID. |
| Create Message Recipients In Bulk | `createMessageRecipientsBulk` | Add several recipients to an invite message in a single request, by contact IDs, contact list IDs, or new contact details. |
| Create Organization | `createOrganization` | Create an organization. Requires an enterprise plan. |
| Create Survey | `createSurvey` | Create a survey. Creates an empty survey, or, when a template ID or existing survey ID is supplied, a survey prepopulated with pages and questions. |
| Create Survey Collector | `createSurveyCollector` | Create a collector for a survey. Creating any collector other than a weblink collector requires a paid plan. |
| Create Survey Folder | `createSurveyFolder` | Create a survey folder, used to group a collection of surveys. |
| Create Survey Page | `createSurveyPage` | Create a page in a survey. |
| Create Survey Question | `createSurveyQuestion` | Create a question on a survey page. The required answers and display_options shape depends on the chosen question family and subtype. |
| Create Survey Results Share | `createSurveyResultsShare` | Create a shared survey results page and return its shared view key. |
| Create Survey Translation | `createSurveyTranslation` | Create a translation for one language of a multilingual survey. |
| Create Webhook | `createWebhook` | Register a webhook so SurveyMonkey sends events to a subscription URL. The subscription URL must be unique across the app's webhooks. |
| Create Workgroup | `createWorkgroup` | Create a workgroup in the organization. Requires a paid plan (workgroups_write scope). |
| Delete All Collector Responses | `deleteCollectorResponses` | Delete every response collected by a collector. Requires a paid plan (responses_write scope). |
| Delete Collector | `deleteCollector` | Delete a collector. |
| Delete Collector Message | `deleteCollectorMessage` | Delete an invite message from a collector. |
| Delete Collector Recipient | `deleteCollectorRecipient` | Delete a recipient from a collector. |
| Delete Collector Response | `deleteCollectorResponse` | Delete a single response from a collector. Requires a paid plan (responses_write scope). |
| Delete Contact | `deleteContact` | Delete a contact. |
| Delete Contact List | `deleteContactList` | Delete a contact list. |
| Delete Survey | `deleteSurvey` | Delete a survey. |
| Delete Survey Folder | `deleteSurveyFolder` | Delete a survey folder. Surveys inside the folder are not deleted. This endpoint is not listed in SurveyMonkey's published API reference but is live and verified against the v3 API. |
| Delete Survey Page | `deleteSurveyPage` | Delete a page from a survey. |
| Delete Survey Question | `deleteSurveyQuestion` | Delete a question from a survey page. |
| Delete Survey Translation | `deleteSurveyTranslation` | Delete a translation from a multilingual survey. |
| Delete Webhook | `deleteWebhook` | Delete a webhook. |
| Delete Workgroup Share | `deleteWorkgroupShare` | Stop sharing a resource with a workgroup. Requires a paid plan (workgroups_shares_write scope). |
| Get API Error | `getError` | Retrieve the description of a single API error code. |
| Get Benchmark Bundle | `getBenchmarkBundle` | Retrieve a single benchmark bundle and the questions it contains. |
| Get Collector | `getCollector` | Retrieve a single collector. |
| Get Collector Message | `getCollectorMessage` | Retrieve a single invite message of a collector. |
| Get Collector Message Stats | `getCollectorMessageStats` | Retrieve delivery and response statistics for a single invite message. |
| Get Collector Recipient | `getCollectorRecipient` | Retrieve a single recipient of a collector. |
| Get Collector Response | `getCollectorResponse` | Retrieve the metadata of a single response collected by a collector. |
| Get Collector Response Details | `getCollectorResponseDetails` | Retrieve a single collector response including all of its answers. Requires a paid plan (responses_read_detail scope). |
| Get Collector Stats | `getCollectorStats` | Retrieve response statistics for a collector, broken down by recipient and response status. |
| Get Contact | `getContact` | Retrieve a single contact. |
| Get Contact Field | `getContactField` | Retrieve a single custom contact field. |
| Get Contact List | `getContactList` | Retrieve a single contact list. |
| Get Current User | `getCurrentUser` | Retrieve the account details of the user who owns the access token, including plan type, available and granted scopes, enabled question types and account features. |
| Get Group | `getGroup` | Retrieve a single group (team), including its name, member count and creation date. Requires a paid plan (groups_read scope). |
| Get Group Activity Summary | `getGroupActivitySummary` | Retrieve a time-bucketed summary of one activity type for a group (team). Requires a paid plan (groups_read scope). |
| Get Group Member | `getGroupMember` | Retrieve a single member of a group (team). Requires a paid plan (groups_read scope). |
| Get Organization | `getOrganization` | Retrieve a single organization, including its default role and workgroup creation policy. Requires an enterprise plan. |
| Get Survey | `getSurvey` | Retrieve a survey's details. To get an expanded version including all pages and questions, use Get Survey Details instead. |
| Get Survey Details | `getSurveyDetails` | Retrieve an expanded survey object containing all of its pages and questions in a single call. |
| Get Survey Folder | `getSurveyFolder` | Retrieve a single survey folder, including how many surveys it holds. This endpoint is not listed in SurveyMonkey's published API reference but is live and verified against the v3 API. |
| Get Survey Page | `getSurveyPage` | Retrieve a single page of a survey. |
| Get Survey Page Rollups | `getPageRollups` | Retrieve aggregated answer counts for every question on a survey page. Requires a paid plan (responses_read_detail scope). |
| Get Survey Page Trends | `getPageTrends` | Retrieve answer trends over time for every question on a survey page. Requires a paid plan (responses_read_detail scope). |
| Get Survey Question | `getSurveyQuestion` | Retrieve a single question from a survey page. |
| Get Survey Question Benchmark | `getQuestionBenchmark` | Retrieve benchmark results for a single survey question, comparing it against industry benchmark data. |
| Get Survey Question Rollups | `getQuestionRollups` | Retrieve aggregated answer counts for a single survey question. Requires a paid plan (responses_read_detail scope). |
| Get Survey Question Trends | `getQuestionTrends` | Retrieve answer trends over time for a single survey question. Requires a paid plan (responses_read_detail scope). |
| Get Survey Response | `getSurveyResponse` | Retrieve the metadata of a single survey response. |
| Get Survey Response Details | `getSurveyResponseDetails` | Retrieve a single survey response including all of its answers. Requires a paid plan (responses_read_detail scope). |
| Get Survey Rollups | `getSurveyRollups` | Retrieve aggregated answer counts for every question in a survey. Requires a paid plan (responses_read_detail scope). |
| Get Survey Translation | `getSurveyTranslation` | Retrieve the existing translations, or the translation structure, for one language of a survey. |
| Get Survey Trends | `getSurveyTrends` | Retrieve answer trends over time for every question in a survey. Requires a paid plan (responses_read_detail scope). |
| Get Webhook | `getWebhook` | Retrieve a single webhook. |
| Get Workgroup | `getWorkgroup` | Retrieve a single workgroup, including its members, share count and default role. Requires a paid plan (workgroups_read scope). |
| Get Workgroup Member | `getWorkgroupMember` | Retrieve a single workgroup member. Requires a paid plan (workgroups_members_read scope). |
| Get Workgroup Share | `getWorkgroupShare` | Retrieve a single workgroup share record, including the privileges it grants. Requires a paid plan (workgroups_shares_read scope). |
| List API Errors | `listErrors` | List the API error codes and their descriptions. |
| List Benchmark Bundles | `listBenchmarkBundles` | List the benchmark bundles available, which group questions that can be benchmarked against industry data. |
| List Collector Messages | `listCollectorMessages` | List the invite messages of a collector. |
| List Collector Recipients | `listCollectorRecipients` | List all recipients of a collector across its messages. |
| List Collector Responses | `listCollectorResponses` | List the responses collected by a collector, returning response metadata without the answers. |
| List Collector Responses In Bulk | `listCollectorResponsesBulk` | List the responses collected by a collector including all of their answers. Requires a paid plan (responses_read_detail scope). |
| List Contact Fields | `listContactFields` | List the custom contact fields in the user's account. |
| List Contact Lists | `listContactLists` | List the contact lists in the user's account. |
| List Contacts | `listContacts` | List the contacts in the user's account. |
| List Contacts In Bulk | `listContactsBulk` | List the contacts in the user's account, returning the full contact object for each in a single call. |
| List Contacts In List | `listContactsInList` | List the contacts in a contact list. |
| List Contacts In List In Bulk | `listContactsInListBulk` | List the contacts in a contact list, returning the full contact object for each in a single call. |
| List Group Activities | `listGroupActivities` | List activity events for a group (team), such as members joining or surveys being created. Requires a paid plan (groups_read scope). |
| List Group Members | `listGroupMembers` | List the members of a group (team). Requires a paid plan (groups_read scope). |
| List Groups | `listGroups` | List the groups (teams) the authenticated user belongs to. Requires a paid plan (groups_read scope). |
| List Message Recipients | `listMessageRecipients` | List the recipients of an invite message. |
| List Organizations | `listOrganizations` | List the organizations the authenticated user belongs to. Requires an enterprise plan. |
| List Question Bank Questions | `listQuestionBankQuestions` | List the questions available in the SurveyMonkey Question Bank, or in a team's custom question bank. |
| List Resources Shared With User | `listUserSharedResources` | List the resources shared with a user across all workgroups. Requires a paid plan (workgroups_shares_read scope). |
| List Roles | `listRoles` | List the workgroup roles available in the organization, such as Analyzer, Collector, Full Access, Viewer and Editor. Requires a paid plan (roles_read scope). |
| List Survey Categories | `listSurveyCategories` | List the survey template categories available, used to filter the survey template list. |
| List Survey Collectors | `listSurveyCollectors` | List the collectors of a survey. |
| List Survey Folders | `listSurveyFolders` | List the survey folders in the user's account. |
| List Survey Languages | `listSurveyLanguages` | List the languages supported for surveys and translations. |
| List Survey Pages | `listSurveyPages` | List the pages of a survey. |
| List Survey Questions | `listSurveyQuestions` | List the questions on a survey page. |
| List Survey Responses | `listSurveyResponses` | List the responses to a survey, returning response metadata without the answers. |
| List Survey Responses In Bulk | `listSurveyResponsesBulk` | List the responses to a survey including all of their answers. Requires a paid plan (responses_read_detail scope). |
| List Survey Results Shares | `getSurveyShareList` | List the shared results pages configured for a survey. |
| List Survey Templates | `listSurveyTemplates` | List the survey templates available to the user, optionally filtered by category and language. |
| List Survey Translations | `listSurveyTranslations` | List the translation languages configured for a multilingual survey. |
| List Surveys | `listSurveys` | List the surveys owned by or shared with the authenticated user. |
| List Team Survey Templates | `listTeamSurveyTemplates` | List the survey templates shared within the user's team. Requires a team plan. |
| List User Workgroups | `listUserWorkgroups` | List the workgroups a given user belongs to, including each workgroup's membership status and default role. Requires a paid plan (workgroups_read scope). |
| List Webhooks | `listWebhooks` | List the webhooks registered by the app for the authenticated user. |
| List Workgroup Members | `listWorkgroupMembers` | List the members of a workgroup. Requires a paid plan (workgroups_members_read scope). |
| List Workgroup Shares | `listWorkgroupShares` | List the resources shared with a workgroup. Requires a paid plan (workgroups_shares_read scope). |
| List Workgroups | `listWorkgroups` | List the workgroups in the organization. Requires a paid plan (workgroups_read scope). |
| Merge Contact List | `mergeContactList` | Merge another contact list into the contact list identified in the path. |
| Remove Workgroup Member | `removeWorkgroupMember` | Remove a member from a workgroup. Requires a paid plan (workgroups_members_write scope). |
| Replace Collector | `replaceCollector` | Replace a collector. Accepts the same arguments as Create Survey Collector, with the addition of status and without type. |
| Replace Collector Message | `replaceCollectorMessage` | Replace an invite message. Only subject, body_text, body_html, is_branding_enabled, and recipient_status for reminder or thank_you messages, can be modified. |
| Replace Collector Response | `replaceCollectorResponse` | Replace a response on a collector. Requires a paid plan (responses_write scope). |
| Replace Contact | `replaceContact` | Replace a contact. Accepts the same arguments as Create Contact. |
| Replace Contact List | `replaceContactList` | Replace a contact list. Accepts the same arguments as Create Contact List. |
| Replace Survey | `replaceSurvey` | Replace a survey. Accepts the same arguments as Create Survey. |
| Replace Survey Folder | `replaceSurveyFolder` | Replace a survey folder. Accepts the same arguments as Create Survey Folder. This endpoint is not listed in SurveyMonkey's published API reference but is live and verified against the v3 API. |
| Replace Survey Page | `replaceSurveyPage` | Replace a survey page. Accepts the same arguments as Create Survey Page. |
| Replace Survey Question | `replaceSurveyQuestion` | Replace a question on a survey page. Accepts the same arguments as Create Survey Question. |
| Replace Survey Response | `replaceSurveyResponse` | Replace a survey response. Requires a paid plan (responses_write scope). |
| Replace Webhook | `replaceWebhook` | Replace a webhook. Accepts the same arguments as Create Webhook. |
| Search Surveys | `searchSurveys` | Search surveys by title or nickname, with filtering by response count, date range, folder, sharing status, survey state and tags. |
| Send Collector Message | `sendCollectorMessage` | Sends an existing invite message on an email collector to its recipients immediately. This delivers email to real people; scheduled sends are not supported by this action (SurveyMonkey requires a JSON body, so an empty object is sent). |
| Share Resource With Workgroup | `createWorkgroupShare` | Share a resource, such as a survey, with a workgroup. Requires a paid plan (workgroups_shares_write scope). |
| Share Resources With Workgroup In Bulk | `createWorkgroupSharesBulk` | Share several resources with a workgroup in a single request. Requires a paid plan (workgroups_shares_write scope). |
| Update Collector | `updateCollector` | Update a collector. Only the supplied fields are modified. |
| Update Collector Message | `updateCollectorMessage` | Update an invite message. Only subject, body_text, body_html, is_branding_enabled, and recipient_status for reminder or thank_you messages, can be modified. |
| Update Collector Response | `updateCollectorResponse` | Update a response on a collector. Requires a paid plan (responses_write scope). |
| Update Contact | `updateContact` | Update a contact. Only the supplied fields are modified. |
| Update Contact Field | `updateContactField` | Update the label of a custom contact field. |
| Update Contact List | `updateContactList` | Update a contact list's name. |
| Update Group Member | `updateGroupMember` | Update a group (team) member's email address. Requires a paid plan (groups_read scope). |
| Update Organization | `updateOrganization` | Update an organization's default role or workgroup creation policy. Requires an enterprise plan. |
| Update Survey | `updateSurvey` | Update a survey's title, nickname, language, button text, custom variables, footer or folder. |
| Update Survey Folder | `updateSurveyFolder` | Update a survey folder's title. This endpoint is not listed in SurveyMonkey's published API reference but is live and verified against the v3 API. |
| Update Survey Page | `updateSurveyPage` | Update a survey page's title, description or position. |
| Update Survey Question | `updateSurveyQuestion` | Update a question on a survey page. Only the supplied fields are modified. |
| Update Survey Response | `updateSurveyResponse` | Update a survey response. Requires a paid plan (responses_write scope). |
| Update Survey Translation | `updateSurveyTranslation` | Update a translation for one language of a multilingual survey. |
| Update Webhook | `updateWebhook` | Update a webhook. Only the supplied fields are modified, but SurveyMonkey re-validates the object filter on every update, so object_type and object_ids must be resent alongside the fields being changed. |
| Update Workgroup | `updateWorkgroup` | Update a workgroup's name, description, visibility or metadata. Requires a paid plan (workgroups_write scope). |
| Update Workgroup Member | `updateWorkgroupMember` | Update a workgroup member, for example to grant or revoke workgroup ownership. Requires a paid plan (workgroups_members_write scope). |
