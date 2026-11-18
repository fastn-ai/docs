---
description: "SurveySparrow experience management platform."
---

# SurveySparrow

SurveySparrow experience management platform. Wraps the complete SurveySparrow REST API v3: surveys, sections, questions, variables and expressions, responses and batch response import, contacts, contact lists and contact properties, share channels and reminders, NPS/CES/CSAT metrics and reports, tickets, ticket comments, ticket fields and templates, users, roles and teams, survey folders, translations and languages, audit logs, reputation management, Employee 360 invites, and webhooks. Authenticates with a private-app access token sent as a Bearer token, against the regional API host for the account's data center.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [surveysparrow.com](https://surveysparrow.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 116 |
| **Events** | 0 |
| **Slug** | `surveySparrow` |

## Use it

Add SurveySparrow from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.surveySparrow.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Response Answers | `addResponseAnswers` | Adds answers to an in-progress response created by Start Response, so a partial submission can be built up question by question. |
| Clone Channel | `cloneChannel` | Creates a copy of an existing share channel on the same survey. |
| Clone Survey | `cloneSurvey` | Creates a copy of an existing survey, optionally under a new name and converted to a different survey type. |
| Complete Response | `completeResponse` | Marks an in-progress response as complete so it counts as a finished submission. |
| Create Audit Log Event Subscription | `createAuditLogEventSubscription` | Subscribes an endpoint to one or more audit log events, so SurveySparrow calls it whenever those account changes happen. |
| Create Channel | `createChannel` | Creates a share channel on a survey. Use schedule only when the mode is RECURRING and relative_schedule only when it is RELATIVE_RECURRING; supply the sms, email or link object matching the channel type, and animation_direction under offline for OFFLINE channels. |
| Create Channel Reminder | `createChannelReminder` | Adds a reminder to a share channel so recipients who have not responded, or only partly responded, are chased after a delay. Applies to Classic, customer experience and chat surveys shared over email or SMS. |
| Create Contact | `createContact` | Creates a contact or employee record that surveys can be shared with. |
| Create Contact List | `createContactList` | Creates a contact list that contacts can be grouped into for sharing surveys. |
| Create Contact Property | `createContactProperty` | Creates a custom contact property so extra data can be stored against contacts. |
| Create Contacts | `createContacts` | Imports a batch of contacts asynchronously, optionally adding each one to contact lists. Returns a token to poll with Get Contact Batch Status. |
| Create Custom Language | `createCustomLanguage` | Creates a custom language in the account so surveys can be translated into a dialect SurveySparrow does not ship by default. |
| Create Question | `createQuestion` | Adds a question to a survey, optionally inside a specific section. The question object carries the text, type, answer choices, matrix rows and columns, type-specific display properties and display logic. |
| Create Response | `createResponse` | Records a completed survey response with its answers, optionally attributing it to a contact and share channel and attaching custom variables and device metadata. |
| Create Responses | `createResponses` | Imports up to two hundred survey responses in one asynchronous job. Returns a token to poll with Get Response Batch Status. |
| Create Survey | `createSurvey` | Creates a survey of the given type in the account, optionally placing it in a survey folder and applying a theme, welcome screen, thank-you screens and response settings. |
| Create Survey Folder | `createSurveyFolder` | Creates a survey folder to organise surveys, optionally nested under a parent folder and restricted to specific teams and users. |
| Create Survey Invite | `createSurveyInvite` | Sets up an Employee 360 review for one subject: who is reviewed, who evaluates them and under which relationship, who approves the nominations, and whether the review goes out now or on a schedule. |
| Create Survey Sections | `createSurveySections` | Adds up to twenty sections to a survey in one call. Each section can carry presentation properties, display logic and an initial set of questions defined the same way as in Create Question. |
| Create Survey Variable | `createSurveyVariable` | Creates a custom variable on a survey so external values can be passed into the survey link and stored with each response. |
| Create Survey Variables | `createSurveyVariables` | Creates up to fifty custom variables on a survey in a single call. |
| Create Team | `createTeam` | Creates a team of account users for sharing surveys or handling tickets, optionally with round-robin ticket assignment. |
| Create Ticket | `createTicket` | Raises a support ticket for a contact, optionally linking it to a survey response, a template, a parent ticket and custom field values. File attachments are not supported through this connector. |
| Create Ticket Comment | `createTicketComment` | Adds a public reply or internal note to a support ticket. File attachments are not supported through this connector. |
| Create Tickets | `createTickets` | Creates a batch of support tickets asynchronously. Returns a token to poll with Get Ticket Batch Status. |
| Create Translation | `createTranslation` | Adds one or more languages to a survey, optionally filling the translations automatically with Google Translate. |
| Create Unique Survey Links | `createUniqueSurveyLinks` | Generates a personalised survey link for each supplied contact on a link channel, so responses can be attributed without sending an email or SMS. |
| Create User | `createUser` | Invites a new user to the SurveySparrow account with the given role. |
| Create Webhook | `createWebhook` | Registers a webhook on a survey so SurveySparrow posts each matching event to the given endpoint. |
| Delete Audit Log Event Subscription | `deleteAuditLogEventSubscription` | Removes an audit log event subscription so SurveySparrow stops calling its endpoint. |
| Delete Channel | `deleteChannel` | Deletes a share channel from a survey. |
| Delete Channel Reminder | `deleteChannelReminder` | Removes a reminder from a share channel. |
| Delete Contact | `deleteContact` | Permanently deletes a contact from the account. |
| Delete Contact List | `deleteContactList` | Deletes a contact list. The contacts it grouped remain in the account. |
| Delete Contact Property | `deleteContactProperty` | Deletes a custom contact property and the values stored under it. |
| Delete Question | `deleteQuestion` | Permanently removes a question from its survey. |
| Delete Response | `deleteResponse` | Deletes a survey response, optionally releasing the quota slot it occupied. |
| Delete Survey Folder | `deleteSurveyFolder` | Deletes a survey folder from the account. |
| Delete Survey Section | `deleteSurveySection` | Deletes a section from a survey along with the questions it contains. |
| Delete Survey Variable | `deleteSurveyVariable` | Deletes a custom variable from its survey. |
| Delete Ticket | `deleteTicket` | Moves a support ticket to the trash. |
| Delete Translation | `deleteTranslation` | Removes a language and its translated content from a survey. |
| Delete User | `deleteUser` | Removes a user from the SurveySparrow account. |
| Delete Webhook | `deleteWebhook` | Removes a webhook so SurveySparrow stops delivering events to its endpoint. |
| Export Translation | `exportTranslation` | Generates a spreadsheet of a survey's content in one language and returns a signed download link. The link expires 60 seconds after it is issued. |
| Get Audit Log | `getAuditLog` | Retrieves a single audit log entry by its identifier. |
| Get Channel | `getChannel` | Retrieves a single share channel of a survey with its type-specific configuration. |
| Get Channel Reminder | `getChannelReminder` | Retrieves a single reminder configured on a share channel. |
| Get Channel Summary | `getChannelSummary` | Returns the analytics summary for a share channel, covering how many recipients were sent, opened and responded to the survey. |
| Get Contact | `getContact` | Retrieves a single contact with its profile fields, subscription status and contact list membership. |
| Get Contact Batch Status | `getContactBatchStatus` | Returns the progress and per-record outcome of a batch contact import started by Create Contacts. |
| Get Contact List | `getContactList` | Retrieves a single contact list by its identifier. |
| Get Experience Metrics | `getExperienceMetrics` | Returns the NPS, CES or CSAT score for a customer experience survey over an optional date range. When no survey is given, metrics for every customer experience survey in the account are returned as an array. |
| Get Question Report | `getQuestionReport` | Returns the aggregated report for one question of a survey, including every answer given and how many respondents answered or skipped it. |
| Get Reputation App Platform | `getReputationAppPlatform` | Retrieves a single connected review platform with the page reviews are collected from. Requires the Reputation Management feature on the account. |
| Get Reputation Platform | `getReputationPlatform` | Retrieves a single review platform supported by Reputation Management. Requires the Reputation Management feature on the account. |
| Get Reputation Review | `getReputationReview` | Retrieves a single collected review. Requires the Reputation Management feature on the account. |
| Get Response | `getResponse` | Retrieves a single survey response with its answers, contact, share channel and metadata. |
| Get Response Batch Status | `getResponseBatchStatus` | Returns the progress and per-record outcome of a batch response import started by Create Responses. |
| Get Responses Report Link | `getResponsesReportLink` | Returns the public link to a survey's responses report, which can be shared with people who do not have a SurveySparrow account. |
| Get Survey | `getSurvey` | Retrieves a single survey by its identifier, including its type, folder and the full set of survey settings. |
| Get Survey Folder | `getSurveyFolder` | Retrieves a single survey folder, optionally expanded to include its subfolders, surveys and echoes. |
| Get Survey Subject Report | `getSurveySubjectReport` | Returns the consolidated 360-degree feedback report for one subject of an Employee 360 survey. |
| Get Ticket | `getTicket` | Retrieves a single support ticket with its requester, priority, status, assignment, SLA due dates and custom field values. |
| Get Ticket Batch Status | `getTicketBatchStatus` | Returns the progress and per-record outcome of a batch ticket creation started by Create Tickets. |
| Get Ticket Field | `getTicketField` | Retrieves a single ticket field with its type and selectable options. |
| Get User | `getUser` | Retrieves a single account user with their role and administrator flags. |
| Import Reputation Review | `importReputationReview` | Imports a review into a custom Reputation Management location, so reviews gathered outside SurveySparrow appear alongside the collected ones. Requires the Reputation Management feature on the account. |
| List Audit Log Event Subscriptions | `listAuditLogEventSubscriptions` | Returns the audit log events the account has subscribed to, each with the endpoint SurveySparrow calls when the event fires. |
| List Audit Logs | `listAuditLogs` | Returns the account's audit log entries, showing who changed what and when, optionally filtered by event type and date range. |
| List Channel Reminders | `listChannelReminders` | Returns the reminders configured on a share channel. Applies to Classic, customer experience and chat surveys shared over email or SMS. |
| List Channels | `listChannels` | Returns the share channels configured on a survey, such as email, SMS, web link, embed, QR code and kiosk shares, optionally filtered by channel type. |
| List Contact Lists | `listContactLists` | Returns every contact list in the account. |
| List Contact Properties | `listContactProperties` | Returns every contact property defined in the account, both the built-in ones and the custom fields, together with the property group each belongs to. |
| List Contacts | `listContacts` | Returns the contacts in the account, with filters for contact list membership, subscription status, contact type, free-text search and creation date range. |
| List Email Themes | `listEmailThemes` | Returns the email themes available for survey invitation emails, both the SurveySparrow defaults and any custom themes in the account. |
| List Languages | `listLanguages` | Returns the languages a survey can be translated into, covering both the standard SurveySparrow languages and any custom languages created in the account. |
| List Metric Responses | `listMetricResponses` | Returns the responses of a customer experience survey that fall into one metric category, such as NPS promoters or CES low-effort respondents. |
| List Questions | `listQuestions` | Returns the questions of a survey, optionally filtered by question tag and returned in a specific survey language. |
| List Reputation App Platforms | `listReputationAppPlatforms` | Returns the review platforms connected to this account, each tying a review source to one business location. Requires the Reputation Management feature on the account. |
| List Reputation Platforms | `listReputationPlatforms` | Returns the review platforms SurveySparrow Reputation Management can collect reviews from, such as Google or Agoda. Requires the Reputation Management feature on the account. |
| List Reputation Reviews | `listReputationReviews` | Returns the reviews collected from a connected review platform, with optional rating and review date filters. Requires the Reputation Management feature on the account. |
| List Response Properties | `listResponseProperties` | Returns the metadata properties stored against every response, such as browser, operating system, time zone, device type and IP address, mapped to their display labels. |
| List Responses | `listResponses` | Returns the responses collected for a survey, with filters for contact, submission state, completion and creation date ranges, and ordering. |
| List Roles | `listRoles` | Returns the roles available in the account, such as Account Owner, Admin and Survey Admin, with the identifiers needed when creating or updating a user. |
| List Survey Approvers | `listSurveyApprovers` | Returns the approvers of an Employee 360 survey along with how many nominations each has approved, declined or still has pending. |
| List Survey Expressions | `listSurveyExpressions` | Returns the calculation expressions defined on a survey, which compute values from answers and variables. |
| List Survey Folders | `listSurveyFolders` | Returns the survey folders in the account, optionally expanded to include their subfolders, surveys and echoes. |
| List Survey Relations | `listSurveyRelations` | Returns the evaluator relationships defined on an Employee 360 survey, such as manager, peer or direct report, for use when nominating evaluators. |
| List Survey Subject Evaluators | `listSurveySubjectEvaluators` | Returns the people nominated to evaluate one subject of an Employee 360 survey, with the status of each nomination. |
| List Survey Subjects | `listSurveySubjects` | Returns the people being reviewed in an Employee 360 survey, with their approver and self-evaluation settings. |
| List Survey Variables | `listSurveyVariables` | Returns the custom variables defined on a survey, which carry values passed into the survey link and are stored with each response. |
| List Surveys | `listSurveys` | Returns the surveys in the SurveySparrow account, optionally filtered by survey type, archived state, survey folder and creation or update date range. |
| List Targets | `listTargets` | Returns the SMS sending targets configured in the account, which decide the number surveys are sent from. |
| List Teams | `listTeams` | Returns the teams in the account, optionally filtered to survey teams or ticketing teams. |
| List Ticket Comments | `listTicketComments` | Returns the comments on a support ticket. The private filter must be supplied to select public or internal comments; omitting it returns an empty list. |
| List Ticket Fields | `listTicketFields` | Returns the ticket fields in the account, including the built-in Priority, Status and Source dropdowns with the option identifiers needed when creating or updating a ticket. |
| List Ticket Templates | `listTicketTemplates` | Returns the ticket templates in the account together with the fields each template exposes. |
| List Tickets | `listTickets` | Returns the support tickets in the account, with filters for requester, assignee, team, priority, status, trash state and creation or update date range. |
| List Users | `listUsers` | Returns the users of the SurveySparrow account with their roles and administrator flags. |
| List Webhooks | `listWebhooks` | Returns the webhooks registered in the account, optionally narrowed to a single survey. |
| Start Response | `startResponse` | Opens a new in-progress response so answers can be added incrementally. The survey must have partial submissions enabled. |
| Update Channel | `updateChannel` | Updates a share channel. Supported for LINK, SMS, EMAIL and OFFLINE channels only. Use schedule when the mode is RECURRING and relative_schedule when it is RELATIVE_RECURRING, and supply the sms, email, link or offline object matching the channel type. |
| Update Contact | `updateContact` | Updates the profile fields of an existing contact. |
| Update Contact List | `updateContactList` | Renames a contact list or changes its description. |
| Update Contact Property | `updateContactProperty` | Updates a custom contact property's label, description, data type or property group. |
| Update Question | `updateQuestion` | Updates an existing survey question: its text, description, mandatory flag and type-specific properties. |
| Update Response | `updateResponse` | Replaces the answers stored on an existing survey response and can reassign it to a different contact. |
| Update Survey | `updateSurvey` | Updates an existing survey. Only the properties supplied in the request are changed, so the survey can be renamed, moved, re-themed, archived or have individual response settings adjusted. |
| Update Survey Folder | `updateSurveyFolder` | Renames a survey folder or changes which teams and users can see it. |
| Update Survey Invite | `updateSurveyInvite` | Replaces the evaluators nominated for one subject of an Employee 360 survey. |
| Update Survey Section | `updateSurveySection` | Updates a survey section's name, description, position, presentation properties and display logic. |
| Update Ticket | `updateTicket` | Updates a support ticket's priority, status, assignment, requester, parent and child links or custom field values. |
| Update Translation | `updateTranslation` | Re-runs the automatic translation of a survey language. The endpoint also accepts an uploaded translation spreadsheet, but binary file uploads are not supported through this connector, so only the Google Translate path is available here. SurveySparrow accepts this endpoint only as multipart/form-data, optionally with an Excel translation file. Sent as multipart/form-data text fields; the optional Excel translation file (binary) cannot be sent by this action. |
| Update User | `updateUser` | Renames an account user or changes the role assigned to them. |
| Update Webhook | `updateWebhook` | Changes a webhook's endpoint, name, delivery method, custom headers or payload template. |
