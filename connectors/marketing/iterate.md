---
description: "Iterate (iteratehq.com) in-product, email and mobile surveys: surveys, questions, responses, response groups, stats, metrics, AI reports, themes, topics,…"
hidden: true
---

# Iterate

<img src="../../.gitbook/assets/connectors/iterate.png" alt="Iterate logo" width="64">

Iterate (iteratehq.com) in-product, email and mobile surveys: surveys, questions, responses, response groups, stats, metrics, AI reports, themes, topics, recipients, projects, tags, permission groups, users and webhooks. REST API at https://iteratehq.com/api/v1 authenticated with an X-Api-Key header.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [iteratehq.com](https://iteratehq.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `iterate` |

## Use it

Add Iterate from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.iterate.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Survey Recipient | `addSurveyRecipient` | Add a user as an email recipient of a survey. This only queues them - nothing is sent until Send Survey is called. |
| Add Survey Theme Topics | `addSurveyThemeTopics` | Attach topic keywords to a theme. topics is a JSON array of plain strings, e.g. ["pricing","support"]. Returns the theme. |
| Anonymize Respondent | `anonymizeRespondent` | GDPR: strip the personally identifying fields from one respondent, keeping their responses. Set include_response_properties to also scrub properties attached to their responses. Irreversible. |
| Anonymize Respondents In Bulk | `anonymizeRespondentsInBulk` | GDPR: anonymize every respondent matching the given identifiers. The field names are SINGULAR but each holds an ARRAY, and all three must be present - omitting one makes Iterate answer 200 with {"error":"(BadValue) $in needs an array"}. Returns users_anonymized. Irreversible. |
| Cancel Survey Schedule | `cancelSurveySchedule` | Cancel a pending scheduled send for a survey. There is no per-schedule delete route - the survey id alone identifies the schedule. Returns the survey. |
| Create Company Tag | `createCompanyTag` | Create a response tag on the account. Returns the new tag id. |
| Create Company Webhook | `createCompanyWebhook` | Register an account-wide webhook that Iterate POSTs survey responses to. Returns id, url and secret. |
| Create Permission Group | `createPermissionGroup` | Create a permission group. Iterate has no update route for permission groups (PUT returns 405) - to rename one, delete it and create another. |
| Create Project | `createProject` | Create a project to group surveys. Returns the new project including its id. |
| Create Question | `createQuestion` | Add a question to a survey. question_type must be one of csat, date, emoji, file_upload, freeform, legal, matrix, maxdiff, multiselect, nps_rating, number, ranking, rating, select, statement, user_info. options is a JSON string of type-specific settings. |

<details>

<summary>See 83 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Question Branch | `createQuestionBranch` | Add a conditional branch to a question, used for skip logic. Takes no body; returns the question with its branches array, each branch carrying the new branch id. |
| Create Survey | `createSurvey` | Create a new (unpublished, draft) survey in a project. type is one of general, nps, csat. Returns the survey including its channel_id, which is the id required to delete it later. |
| Create Survey Reminder | `createSurveyReminder` | Schedule a reminder email for recipients who have not answered the survey. delay is the number of days after the original send. Creating a reminder does not send anything on its own. |
| Create Survey Theme | `createSurveyTheme` | Create a response theme on a survey. Themes group free-text answers for topic analysis. Returns the new theme id. |
| Create Survey Webhook | `createSurveyWebhook` | Register a webhook that Iterate POSTs this survey's responses to. Returns id, url and the signing secret. |
| Delete Company Tag | `deleteCompanyTag` | Delete a response tag by id. Returns the deleted tag. |
| Delete Company Webhook | `deleteCompanyWebhook` | Delete an account-wide webhook by id. |
| Delete Permission Group | `deletePermissionGroup` | Delete a permission group by id. Returns 400 if the group is still granted access to any project - revoke or delete those projects first. |
| Delete Project | `deleteProject` | Delete a project and everything in it. Returns the deleted project. |
| Delete Question | `deleteQuestion` | Delete a question from a survey. |
| Delete Question Branch | `deleteQuestionBranch` | Remove a conditional branch from a question. Returns the question with the branch removed. |
| Delete Respondent Data | `deleteRespondentData` | GDPR: permanently delete one respondent and all of their responses. Returns users_deleted and a status. Irreversible. |
| Delete Respondent Data In Bulk | `deleteRespondentDataInBulk` | GDPR: delete every respondent matching the given identifiers. Body shape matches Anonymize Respondents In Bulk (singular field names holding arrays). KNOWN VENDOR DEFECT: this route answers 200 with {"error":"write exception: write errors: [$in needs an array]"} for the exact body its anonymize twin accepts - use Delete Respondent Data per id until Iterate fixes it. |
| Delete Survey (Channel) | `deleteSurveyChannel` | Permanently delete a survey and all of its responses. Iterate has no DELETE /surveys/{id} route (it returns 405); deletion is done by the survey's channel_id, returned as channel_id by Create Survey and Get Survey. |
| Delete Survey AI Prompt | `deleteSurveyPrompt` | Remove the AI generation prompt stored on a survey. Returns an empty object. |
| Delete Survey Reminder | `deleteSurveyReminder` | Cancel and delete a scheduled survey reminder by id. Returns an empty object on success. |
| Delete Survey Theme | `deleteSurveyTheme` | Delete a response theme by id. Returns the deleted theme. |
| Delete Survey Translations | `deleteSurveyTranslations` | Remove one language's translated copy from a survey. Returns the survey. |
| Delete Survey Webhook | `deleteSurveyWebhook` | Delete a survey-scoped webhook by id. Returns the deleted webhook. |
| Duplicate Question | `duplicateQuestion` | Duplicate a question within the same survey. Returns the new question. |
| Duplicate Survey | `duplicateSurvey` | Duplicate an existing survey. Returns the new survey with its own id and channel_id. |
| Export Channel Responses | `exportChannelResponses` | Start a CSV export of a channel's responses. Returns fileKey (the S3 object key of the generated CSV), shouldEmail and responseCount. It does not return the file itself. |
| Export Question File Uploads | `exportQuestionFileUploads` | Export the files respondents uploaded to a file_upload question. The question must be of type file_upload (otherwise 400 "Question is not a file upload type") and must already have at least one upload (otherwise 400 "No file uploads to export for this question."). |
| Get Background Task Status | `getBackgroundTaskStatus` | Poll the status of the account's current long-running background task, such as a recipient import or a CSV export. Returns an empty status string when nothing is running. |
| Get Channel | `getChannel` | Get a channel - the delivery wrapper around a survey - including its name, type and the full survey record under detail. |
| Get Channel Feedback Group | `getChannelFeedbackGroup` | Get the feedback group for one question on a channel. The final path segment is a QUESTION id, not a group id - passing anything else returns 400 "Invalid question id". Returns end-user personal data. |
| Get Company | `getCompany` | SECURITY WARNING - THIS RESPONSE CONTAINS THE ACCOUNT'S OWN API KEY. Get the connected company/account: plan limits, account status, feature flags, projects, tags and branding. Iterate also returns an access_token field holding the account's live API key in plaintext, so every caller of this action receives a working credential for the whole account. Removing the field from the output contract does NOT stop it being returned - the contract is documentation, the raw vendor body is what reaches the caller. Do not expose this action to untrusted users, do not log its output, and rotate the API key if the response leaks. |
| Get Company Report Stats | `getCompanyReportStats` | Reporting rollup for the account: report counts per author and the number of active recurring reports. |
| Get Company Usage Stats | `getCompanyUsageStats` | Account usage against plan limits, e.g. email surveys sent in the last thirty days versus the plan limit. |
| Get Help Article | `getHelpArticle` | Fetch one article from Iterate's in-product help centre by id. Article ids come from Iterate's own help index; an unknown id returns 200 with {"error":"mongo: no documents in result"}, so check body.error rather than the status code. |
| Get Survey | `getSurvey` | Get detailed information about a specific survey, including its questions, copy, branding and web settings. |
| Get Survey AI Prompt | `getSurveyPrompt` | Read the AI generation prompt stored on a survey. Returns results:null when no prompt has been set. |
| Get Survey CSAT Metrics | `getSurveyCsatMetrics` | Customer satisfaction over time: satisfied, neutral, unsatisfied and response counts per bucket. All three of period, start_date and end_date are required. The survey must contain a csat question, otherwise Iterate returns 400 code 119 'CSAT question not found in survey'. |
| Get Survey Email Embed Code | `getSurveyEmailEmbedCode` | Get the HTML embed code for embedding the survey's first question in an email. |
| Get Survey NPS Metrics | `getSurveyNpsMetrics` | Net Promoter Score over time: promoters, passives, detractors and response counts per bucket. All three of period, start_date and end_date are required. The survey must contain an nps_rating question, otherwise Iterate returns 400 code 118 'NPS question not found in survey'. |
| Get Survey Overview | `getSurveyOverview` | SECURITY WARNING - THIS RESPONSE CONTAINS THE ACCOUNT'S OWN CREDENTIALS. Iterate returns the survey's install/embed overview, and its api_path field embeds the connected account's live API key in plaintext as an access_token query parameter, while embed_script embeds an in-app JWT. Every caller of this action, and anything the response is logged into or passed to, receives a working credential for the whole account. Do not expose this action to untrusted users, do not log its output, and rotate the API key if the response leaks. |
| Get Survey Response Groups | `getSurveyResponseGroups` | Get survey responses grouped by respondent. Each group is one user's complete response set. 10 per page. |
| Get Survey Responses | `getSurveyResponses` | Get individual survey responses in reverse chronological order, 100 per page. Use the cursor from links.next for the next page. |
| Get Survey Stats | `getSurveyStats` | Retrieve stats about a survey: total_responses, users_responded, sent, response_rate, web_displayed_count, web_response_rate. |
| Get Survey Topics | `getSurveyTopics` | Get AI-detected topics, themes and sentiment counts for a survey, optionally scoped to one question. KNOWN VENDOR BLOCKER: Iterate answers HTTP 200 but the body is its own MySQL error ("Error 1064 (42000): You have an error in your SQL syntax ... as themes FROM ... feedback WHERE questio"). Reproduced with and without question_id. Check body.error before using the result. |
| Get Team Member | `getTeamMember` | Get one team member by id, including their emails, role and invite status. |
| Grant Project Access To Permission Group | `grantProjectAccessToPermissionGroup` | Give a permission group access to a project. access_level must be "read" - admin, full, edit and view are all rejected with {"error":"Invalid access level: ..."}. Returns the project with its permission_group_access map. |
| Import Survey Recipients | `importSurveyRecipients` | Bulk-add email recipients to a survey. users is a comma-separated list of email addresses. Importing only queues recipients - nothing is emailed until the survey is sent or scheduled. Returns the imported users with a count. |
| Invalidate Survey Translations | `invalidateSurveyTranslations` | Mark every stored translation on a survey as stale so it will be regenerated. Returns the survey. Note the verb is PUT - POST to this path returns 405. |
| List Channel Feedback Groups | `listChannelFeedbackGroups` | List the grouped free-text feedback collected on a channel. Returns end-user personal data. |
| List Company Reports | `listCompanyReports` | List the account's saved reports, split into recurring and one_off. Reports are created in the Iterate web app - there is no create route on the API (POST returns 405). |
| List Company Surveys | `listCompanySurveys` | List the account's surveys through the company-scoped route. Returns the same surveys as List Surveys but with each survey's full record. |
| List Company Tags | `listCompanyTags` | List the response tags defined on the account. |
| List Company Webhooks | `listCompanyWebhooks` | List the account-wide webhooks. Each has id, url and a signing secret. |
| List Permission Groups | `listPermissionGroups` | List the account's permission groups. The built-in Administrator group is flagged administrator:true. |
| List Projects | `listProjects` | List the account's projects, each with the channels (surveys) inside it. A project id is required to create a survey. |
| List Survey Recipients | `listSurveyRecipients` | List the email recipients added to a survey, with a count and cursor pagination. |
| List Survey Themes | `listSurveyThemes` | List response themes. Note: Iterate scopes this listing to the whole ACCOUNT, not to the survey in the path - it returns every theme in the company, each carrying its own survey_id. Pass any valid survey id. |
| List Survey Webhooks | `listSurveyWebhooks` | List the webhooks registered on one survey. Each has id, url and a signing secret. These are survey-scoped and separate from the account-wide company webhooks. |
| List Surveys | `listSurveys` | List all surveys in the connected Iterate account. Returns results as an array of survey objects. |
| List Team Members | `listTeamMembers` | List the account's team members. The role query parameter is REQUIRED and the only value Iterate accepts is "admin" - omitting it returns 400 code 106 and any other value returns 400 "invalid role". |
| List Templates | `listTemplates` | List Iterate's built-in survey templates with their categories, fields and questions. |
| List Unsubscribed Respondents | `listUnsubscribedRespondents` | List respondents who have unsubscribed from this account's survey emails. Returns end-user personal data - handle accordingly. |
| Remove Survey Recipient | `removeSurveyRecipient` | Remove an email recipient from a survey. Pass the USER id (results.user.id from Add Survey Recipient or List Survey Recipients), NOT the recipient-record id - the record id returns 200 with {"error":"mongo: no documents in result"}. |
| Schedule Survey Send | `scheduleSurveySend` | Schedule the survey to be emailed to its recipients at a future time. date is a Unix timestamp and must be in the future, otherwise Iterate answers 200 with {"error":"date must be a time in the future"}. Returns the schedule id. Use Cancel Survey Schedule to undo it before it fires. |
| Search Users | `searchUsers` | Search for a respondent by email, external id or user property and get their survey participation totals. |
| Send Survey | `sendSurvey` | SENDS A REAL EMAIL. Emails the survey to one recipient immediately, or after delay seconds, or at date (Unix timestamp). This is irreversible once delivered - do not call it against an address you do not control. |
| Send Survey Reminder Now | `sendSurveyReminderNow` | SENDS REAL EMAILS. Immediately dispatches a stored reminder to every survey recipient who has not yet responded, ignoring its schedule. Irreversible. |
| Send Survey Test Email | `sendSurveyTestEmail` | SENDS A REAL EMAIL. Delivers a preview copy of the survey to the given address so an author can check rendering. Use only with an address you control. |
| Set Survey AI Prompt | `setSurveyPrompt` | Store the AI generation prompt for a survey. All three of prompt, project_id and type are required - sending prompt alone makes Iterate return 500. |
| Set Survey Translations | `setSurveyTranslations` | Store the translated copy for one language on a survey. language is an ISO code such as es or fr. translations is a JSON object keyed by copy field. |
| Test Company Webhook | `testCompanyWebhook` | Ask Iterate to send a test delivery to an account-wide webhook. |
| Test Survey Webhook | `testSurveyWebhook` | Ask Iterate to send a sample response delivery to a survey-scoped webhook. Returns the webhook. |
| Translate Survey | `translateSurvey` | Ask Iterate to machine-translate a survey's copy into a language. KNOWN VENDOR BLOCKER: on a trial account this returns 400 code 1 'failed to parse translation response' - the route and request are correct but Iterate's own translation backend fails. |
| Update Channel | `updateChannel` | Rename a channel. This is the name shown in the Iterate web app for the survey. |
| Update Company | `updateCompany` | Update the connected company's settings, such as its display name. Returns the company record. Unlike Get Company, this PUT response does NOT include the account's access_token - verified live. |
| Update Company Tag | `updateCompanyTag` | Rename a response tag. Returns the updated tag. |
| Update Company Webhook | `updateCompanyWebhook` | Change the delivery URL of an account-wide webhook. KNOWN VENDOR DEFECT: Iterate answers 200 but does not persist the new URL - the response echoes the old URL and a follow-up list still shows it. To change a URL, delete the webhook and create a new one. |
| Update Project | `updateProject` | Rename a project. Note the path segment is /p/ and the body must be JSON - a form-encoded body makes Iterate answer 200 with {"error":"Invalid params"}. |
| Update Question | `updateQuestion` | Update a survey question's prompt, type or options. options is a JSON string. |
| Update Question Bank | `updateQuestionBank` | Replace the account's saved question bank. question_bank is an array of question objects. Iterate has no GET for this path (405). SECURITY WARNING: the response is the full company record, which includes access_token - the account's live API key in plaintext. |
| Update Survey | `updateSurvey` | Update a survey. Send only the fields you want to change, e.g. archive, disabled, subject, color, from_name, web_settings. Setting disabled=false publishes the survey to real end users - leave it true while drafting. |
| Update Survey AI Prompt | `updateSurveyPrompt` | Replace the AI generation prompt stored on a survey. All three of prompt, project_id and type are required. |
| Update Survey Reminder | `updateSurveyReminder` | Change the subject of a scheduled survey reminder. Returns the updated reminder. |
| Update Survey Theme | `updateSurveyTheme` | Rename a response theme. Returns the updated theme. |
| Update Survey Webhook | `updateSurveyWebhook` | Change the delivery URL of a survey webhook. KNOWN VENDOR DEFECT: Iterate answers 200 but does not persist the new URL - the response echoes the old URL and a follow-up list still shows it. To change a URL, delete the webhook and create a new one. |
| Update Team Member | `updateTeamMember` | Update a team member's profile fields, such as their first or last name. Returns the updated user. |
| Verify Klaviyo Connection | `verifyKlaviyoConnection` | Check whether this Iterate account has its Klaviyo integration connected. Returns status "connected" or "disconnected". Connecting Klaviyo itself is a browser OAuth flow in the Iterate web app and cannot be done through the API. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Survey response submitted | `survey_response` | Fired when a respondent completes a survey. Payload schema captured from a REAL Iterate delivery (POST /api/v1/companies/{companyId}/webhooks/{id}/test, 2026-09-22). Deliveries carry an 'iterate-signature' header computed with the webhook's own secret, returned by Create Company Webhook. |
