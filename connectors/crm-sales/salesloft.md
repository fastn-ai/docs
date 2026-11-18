---
description: "Salesloft Revenue Orchestration Platform (sales engagement)."
hidden: true
---

# Salesloft

Salesloft Revenue Orchestration Platform (sales engagement). Wraps the Salesloft Platform REST API v2 at https://api.salesloft.com/v2 — people, accounts, cadences and cadence memberships, steps and step groups, actions, tasks, notes, calls and call data records, emails and email templates, meetings and calendar events, conversations and transcriptions, opportunities, users, teams and groups, custom fields, imports, bulk jobs, saved list views, successes, CRM activities, person/account stages and tiers, data-control (GDPR) operations, and the webhook subscription API. Supports OAuth 2.0 authorization code, OAuth 2.0 client credentials, and customer API keys.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [salesloft.com](https://salesloft.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Actions** | 200 |
| **Events** | 37 |
| **Slug** | `salesloft` |

## Use it

Add Salesloft from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.salesloft.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Cadence | `activateCadence` | Transition a draft cadence to active. Returns an error if the team has the cadence approval flow setting enabled — in that case the cadence must go through review instead. Scope: cadences:write. |
| Bulk Reschedule Tasks | `bulkRescheduleTasks` | Reschedule many Salesloft tasks to a new due date in one call. Scope: tasks:write. |
| Cancel Bulk Job | `cancelBulkJob` | Cancel a bulk job and mark all pending records cancelled. Jobs that have already completed cannot be cancelled. |
| Check Email Missing Tags | `checkEmailMissingTags` | Check an email subject and body against a person for unfilled merge tags. Returns the list of tags that could not be resolved. Scope: emails:read. |
| Create Account | `createAccount` | Create a Salesloft account (company). "domain" must be unique on the current team. Scope: accounts:write. |
| Create Activity | `createActivity` | Create an activity, which marks the associated cadence action or task as completed. Only certain action types support an explicitly created activity. Scope: activities:write. |
| Create Audit Report | `createAuditReport` | Request a new audit report over a record type and set of record ids. The report is generated asynchronously; poll Get Audit Report for status and download_url. Scope: audit_reports:write. |
| Create Bulk Job | `createBulkJob` | Create a bulk job. The type fixes what the job does (for example bulk person upsert). Flow: create the job, POST job data in batches of up to 5,000, then mark it ready_to_execute, then poll results. |
| Create Bulk Job Data | `createBulkJobData` | Upload job data to a bulk job. data is an array of objects, each holding the parameters for one individual call. Up to 5,000 records per request; call repeatedly to load more. |
| Create Cadence Bulk Membership | `createCadenceBulkMembership` | Add many people to a cadence at once. The people are selected by a listing filter (people_filter uses the same parameter shape as List People). Person records that may not be added to the cadence are ignored. Returns the filter that was applied, the number of people found, and the cadence and user. Scope: cadences:write. |
| Create Cadence Collection Export Download | `createCadenceCollectionExportDownload` | Request an asynchronous bulk export of cadence collections and their cadences. The download link is emailed to the requesting user. Scope: cadences:read. |
| Create Cadence Collection Import | `createCadenceCollectionImport` | Create a cadence collection from JSON settings. The import format mirrors the cadence collection export format. Requires team admin access. Scope: cadences:write. |
| Create Cadence Export Download | `createCadenceExportDownload` | Request an asynchronous bulk export of cadences matching the given filters. The download link is emailed to the requesting user. Scope: cadences:read. |
| Create Cadence Import | `createCadenceImport` | Create a new cadence from JSON, or import steps onto an existing cadence that has none. The payload mirrors the Cadence Export format — see Salesloft's cadence-imports docs for the settings, sharing_settings and cadence_content schema. Scope: cadences:write. |
| Create Cadence Membership | `createCadenceMembership` | Add a person to a cadence. person_id and cadence_id are required and must be visible to the authenticated user. user_id defaults to the authenticated user. step_id starts the person on a specific step (defaults to the first step). Scope: cadences:write. |
| Create Calendar Event | `createCalendarEvent` | Create a meeting on the user's calendar. Supports external calendar sync (gmail, azure, nylas, cerebro, external) and internal-only events for CRM tracking (calendar_type "internal"). Scope: meetings:write. |
| Create Call | `createCall` | Log a call against a person. Supplying action_id or task_id completes that cadence action / task and maps the CRM Task correctly. disposition and sentiment may be required per team — read them from List Call Dispositions / List Call Sentiments. crm_params may be required per team — read the field list from List CRM Activity Fields. Scope: calls:write. |
| Create Call Data Record | `createCallDataRecord` | Create a call data record from an external dialer. external_call_id must be unique — reusing one turns the request into an update of the existing record. The recording object takes a "url" property which Salesloft fetches asynchronously. Scope: calls:write. |
| Create Conversations Call | `createConversationsCall` | Push a dialer call recording into Conversations for transcription and analysis. recording is an object carrying the supported audio file (.mp3, .wav, .ogg, .m4a) or its URL. Scope: conversations:write. |
| Create Custom Field | `createCustomField` | Create a custom field definition on people, companies or opportunities. Scope: team:write. |
| Create Email Template | `createEmailTemplate` | Create a new personal email template. Scope: emails:write. |
| Create External Email | `createExternalEmail` | Record an email that was sent outside Salesloft, supplying the raw MIME content base64-encoded. Requires a token with the external_emails:create scope. |
| Create External ID Configuration | `createExternalIdConfiguration` | Declare an External ID configuration, pairing a Salesloft object type with your system-of-record name before mappings can be created. Scope: external_id_configuration:write. |
| Create External ID Mapping | `createExternalIdMapping` | Map a Salesloft record to its identifier in your system of record. A matching External ID configuration must exist first. Scope: external_id:write. |
| Create Group | `createGroup` | Create a Salesloft group, optionally nested under a parent group. Scope: groups:write. |
| Create Import | `createImport` | Create an import batch that people can then be attached to via the import_id field on Create Person. Scope: people:write. |
| Create Live Feed Item | `createLiveFeedItem` | Push a live feed item to a Salesloft user. Only usable by allowlisted Frontend Integrations holding the notifications:write, people:read and accounts:read scopes. The message should start with a lower-case past-tense verb. |
| Create Live Website Tracking Parameter | `createLiveWebsiteTrackingParameter` | Create a Live Website Tracking parameter that identifies a person on your website. Returns the parameters to append to tracked links. |
| Create Note | `createNote` | Create a Salesloft note against a person or an account, optionally linked to a call. Scope: notes:write. |
| Create Ongoing Action | `createOngoingAction` | Mark a cadence action as ongoing — progress has been made towards completion but the action is not finished. Validates that the action is still valid before modifying it. Scope: cadences:write. |
| Create Opportunity Person | `createOpportunityPerson` | Associate a Salesloft person with an opportunity — used to record members of a buying group. Scope: opportunities:write. |
| Create Opportunity Stage | `createOpportunityStage` | Create an opportunity stage. Opportunities cannot be created without valid stages. Scope: opportunities:write. |
| Create Person | `createPerson` | Create a Salesloft person (prospect). Either email_address, or phone plus last_name, must be provided as a unique lookup on the team. Scope: people:write. |
| Create Person Stage | `createPersonStage` | Create a person stage. Scope: people:write. |
| Create Play Registration | `createPlayRegistration` | Create a Salesloft Play for a registered Signal and its indicators. A Play cannot be registered against indicators that do not exist on the Signal Registration. Scope: signal_registrations:write. |
| Create Saved List View | `createSavedListView` | Create a saved list view. view_params is a JSON object serialised to a string. Scope: team:write. |
| Create Signal | `createSignal` | Deliver a Rhythm Signal to Salesloft. The payload must match the structure declared on the matching Signal Registration. idempotency_key is a UUID4 that deduplicates repeated deliveries. Scope: signals:write. |
| Create Signal Registration | `createSignalRegistration` | Register a new Signal type for an integration, declaring its indicators, localized description, data shape and allowed attributions. Scope: signal_registrations:write. |
| Create Task | `createTask` | Create a Salesloft task. Supply an idempotency_key to prevent duplicates. Scope: tasks:write. |
| Create Team Template | `createTeamTemplate` | Create a new team-wide email template. owner_id requires team admin permissions and defaults to the authenticated user. Scope: emails:write. |
| Create Webhook Subscription | `createWebhookSubscription` | Subscribe to a Salesloft event. One subscription per event_type per team. Salesloft POSTs the event to callback_url with an x-salesloft-event header and an x-salesloft-signature header containing the HMAC-SHA1 hex digest of the body keyed on callback_token. A failing delivery is retried 3 more times, 15 seconds apart. Scope: the read scope of the resource being subscribed to. |
| Delete Account | `deleteAccount` | Delete a Salesloft account. NOT reversible without contacting Salesloft support. Idempotent — safe to call more than once. Deleting an account removes all connected people from that account. Scope: accounts:delete. |
| Delete Cadence Membership | `deleteCadenceMembership` | Remove a person from a cadence by deleting their cadence membership. Scope: cadences:delete. |
| Delete Custom Field | `deleteCustomField` | Delete a custom field definition by numeric ID. Scope: team:write. |
| Delete External ID Configuration | `deleteExternalIdConfiguration` | Delete an External ID configuration by numeric ID. Scope: external_id_configuration:delete. |
| Delete External ID Mapping | `deleteExternalIdMapping` | Delete an External ID mapping by numeric ID. Scope: external_id:delete. |
| Delete Group | `deleteGroup` | Delete a Salesloft group by numeric ID. Scope: groups:write. |
| Delete Import | `deleteImport` | Delete an import by numeric ID. The undo parameter controls whether the people in the import are deleted with it. Admins can delete any import on the team; non-admins only their own. Scope: people:delete. |
| Delete Note | `deleteNote` | Delete a Salesloft note owned by the authorized account. NOT reversible without contacting Salesloft support. Idempotent. Scope: notes:delete. |
| Delete Opportunity Person | `deleteOpportunityPerson` | Remove an association between a person and an opportunity. Scope: opportunities:delete. |
| Delete Opportunity Stage | `deleteOpportunityStage` | Delete an opportunity stage by numeric ID. Scope: opportunities:delete. |
| Delete Person | `deletePerson` | Delete a Salesloft person. NOT reversible without contacting Salesloft support. Idempotent. Scope: people:delete. |
| Delete Person Stage | `deletePersonStage` | Delete a person stage. NOT reversible without contacting Salesloft support. Idempotent. Scope: people:write. |
| Delete Play Registration | `deletePlayRegistration` | Delete a Play Registration. Play Registrations that have been enabled cannot be deleted. Scope: signal_registrations:delete. |
| Delete Saved List View | `deleteSavedListView` | Delete a saved list view. NOT reversible without contacting Salesloft support. Idempotent. Scope: team:write. |
| Delete Signal Registration | `deleteSignalRegistration` | Delete a Signal Registration by numeric ID. Scope: signal_registrations:delete. |
| Delete Task | `deleteTask` | Delete a Salesloft task. NOT reversible without contacting Salesloft support. Scope: tasks:delete. |
| Delete Webhook Subscription | `deleteWebhookSubscription` | Delete a webhook subscription. NOT reversible without contacting Salesloft support. Idempotent. Scope: any valid token. |
| Export Cadence | `exportCadence` | Export a cadence as JSON. The returned cadence_content can be fed straight back into Create Cadence Import. Scope: cadences:read. |
| Export Cadence Collection | `exportCadenceCollection` | Export a cadence collection as JSON. The returned content can be fed back into Create Cadence Collection Import. Scope: cadences:read. |
| Get Account | `getAccount` | Fetch a single Salesloft account by its numeric ID. Scope: accounts:read. |
| Get Account Stage | `getAccountStage` | Fetch a single account stage by numeric ID. Scope: accounts:read. |
| Get Account Tier | `getAccountTier` | Fetch a single account tier by numeric ID. Scope: accounts:read. |
| Get Action | `getSalesloftAction` | Fetch a single Salesloft cadence action by numeric ID. Only returns actions that are in_progress or pending_activity — a completed action returns 404. Scope: cadences:read. |
| Get Audit Report | `getAuditReport` | Fetch a single audit report by numeric ID. Scope: audit_reports:read. |
| Get Bulk Job | `getBulkJob` | Fetch a bulk job by numeric ID, including its state and processed/error counts. |
| Get Cadence | `getCadence` | Fetch a single Salesloft cadence by numeric ID. Scope: cadences:read. |
| Get Cadence Collection | `getCadenceCollection` | Fetch a single cadence collection by numeric ID. Scope: cadences:read. |
| Get Cadence Membership | `getCadenceMembership` | Fetch a single cadence membership by numeric ID. Scope: cadences:read. |
| Get Cadence Stats | `getCadenceStats` | Fetch aggregate engagement stats for a cadence — people counts, emails sent/delivered/bounced, calls, replies, clicks, views, meetings booked, opportunities created, and the derived rates. Scope: cadences:read. |
| Get Cadence Step Group | `getCadenceStepGroup` | Fetch a single step group of a cadence. Scope: cadences:read. |
| Get Call | `getCall` | Fetch a single logged call activity by numeric ID, including its recordings. Scope: calls:read. |
| Get Call Data Record | `getCallDataRecord` | Fetch a single call data record by numeric ID. Scope: calls:read. |
| Get Call Disposition | `getCallDisposition` | Fetch a single call disposition by numeric ID. Scope: calls:read. |
| Get Call Instruction | `getCallInstruction` | Fetch a single call instruction record by numeric ID. Scope: cadences:read. |
| Get Call Sentiment | `getCallSentiment` | Fetch a single call sentiment by numeric ID. Scope: calls:read. |
| Get Conversation | `getConversation` | Fetch a single conversation by ID, including its recording and transcription references. Scope: conversations:read. |
| Get Conversation Extensive | `getConversationExtensive` | Fetch an extended conversation including AI-generated features where available — summary, action items, key moments, MEDDPICC, attendees and invitees. Scope: conversations:read. |
| Get Conversation Recording | `getConversationRecording` | Fetch the recording metadata for a conversation, including a signed media URL and content type. Returns JSON pointing at the media rather than the media bytes. Scope: conversations:read (plus dialer_recordings:read for dialer media). |
| Get CRM Activity | `getCrmActivity` | Fetch a single CRM activity by numeric ID. Scope: crm:read. |
| Get Current User | `getMe` | Fetch the authenticated user for the current token. Takes no parameters. Useful as a credential-verification call. Scope: any valid token. |
| Get Custom Field | `getCustomField` | Fetch a single custom field definition by numeric ID. Scope: team:read. |
| Get Custom Role | `getCustomRole` | Fetch a single custom role by ID, including its permission set. Scope: team:read. |
| Get Data Control Request | `getDataControlRequest` | Fetch a single data-control request by numeric ID, including its events. Requires the data_control scope. |
| Get Email | `getEmail` | Fetch a single email activity by numeric ID. Pass scoped_fields to include heavier fields such as body. Scope: emails:read. |
| Get Email Template | `getEmailTemplate` | Fetch a single personal email template by numeric ID. Set include_signature to have the current user's email signature merged into the body. Scope: emails:read. |
| Get Group | `getGroup` | Fetch a single Salesloft group by numeric ID. Scope: team:read. |
| Get Import | `getImport` | Fetch a single import by numeric ID. Admins can read any import on the team; non-admins only their own. Scope: people:read. |
| Get Meeting Reschedule Link | `getMeetingRescheduleLink` | Fetch a meeting reschedule link using its reschedule_guid, e.g. a27659c0-058c-4732-928d-c3ad67670a99. Scope: meetings:read. |
| Get MIME Email Payload | `getMimeEmailPayload` | Fetch the raw MIME content for an email, for sending through an external email client. Scope: emails:read. |
| Get Note | `getNote` | Fetch a single Salesloft note by numeric ID. Scope: notes:read. |
| Get Opportunity | `getOpportunity` | Fetch a single Opportunity by numeric ID. Creating, updating and deleting opportunities is done through Salesloft's separate External Opportunities API, not this endpoint. Scope: opportunities:read. |
| Get Opportunity Stage | `getOpportunityStage` | Fetch a single opportunity stage by numeric ID. Scope: opportunities:read. |
| Get Person | `getPerson` | Fetch a single Salesloft person by numeric ID. Scope: people:read. |
| Get Person Stage | `getPersonStage` | Fetch a single person stage by numeric ID. Scope: people:read. |
| Get Phone Number Assignment | `getPhoneNumberAssignment` | Fetch a single phone number assignment by numeric ID. Scope: calls:read. |
| Get Phone Number Recording Settings | `getRecordingSettings` | Fetch the recording status for a phone number based on the team's Do Not Record list and Recording Governance settings. Phone number must be in E.164 format and is passed as the path id. Scope: calls:read. |
| Get Play Registration | `getPlayRegistration` | Fetch a Play Registration by numeric ID. Deleted play registrations cannot be fetched. Scope: signal_registrations:read. |
| Get Saved List View | `getSavedListView` | Fetch a single saved list view by numeric ID. Scope: team:read. |
| Get Signal Registration | `getSignalRegistration` | Fetch a Signal Registration by numeric ID. Scope: signal_registrations:read. |
| Get Step | `getStep` | Fetch a single cadence step by numeric ID. Scope: cadences:read. |
| Get Task | `getTask` | Fetch a single Salesloft task by numeric ID. Scope: tasks:read. |
| Get Task Counts | `getTaskCounts` | Fetch task counts grouped by task type, using the same filters as List Tasks. Scope: tasks:read. |
| Get Team | `getTeam` | Fetch the team of the authenticated user, including plan, plan features, licence limit, privacy defaults and dialer/email policy settings. Takes no parameters. Scope: team:read. |
| Get Team Template | `getTeamTemplate` | Fetch a single team email template by ID. Set include_signature to merge the current user's email signature into the body. Scope: emails:read. |
| Get Transcription | `getTranscription` | Fetch a single conversation transcription by ID. Scope: conversations:read. |
| Get Transcription Artifact | `getTranscriptionArtifact` | Fetch the artifact for a transcription — a signed URL and content type for the full transcript file. Returns JSON pointing at the file rather than the file bytes. Scope: conversations:read. |
| Get User | `getUser` | Fetch a Salesloft user by numeric ID or by GUID. Scope: team:read. |
| Get Webhook Subscription | `getWebhookSubscription` | Fetch a single webhook subscription by numeric ID. Scope: any valid token. |
| List Account Stages | `listAccountStages` | Fetch the team's account stage records. Scope: accounts:read. |
| List Account Team Member Roles | `listAccountTeamMemberRoles` | Fetch CRM Account Team Member Role records. Scope: accounts:read. |
| List Account Tiers | `listAccountTiers` | Fetch the team's account tier records (account prioritisation bands). Scope: accounts:read. |
| List Account Types | `listAccountTypes` | Fetch the distinct account type values that exist across the team's companies, for use in filter selections. Takes no parameters. Scope: accounts:read. |
| List Accounts | `listAccounts` | Fetch multiple Salesloft account (company) records. Supports filtering by ids, crm_id, tag, domain, website, name, account type/stage/tier, owner, industry, country/state/city, engagement level, archived status and created_at/updated_at/last_contacted ranges, plus paging and sorting. Returns data[] plus paging metadata. Scope: accounts:read. |
| List Actions | `listSalesloftActions` | Fetch multiple Salesloft cadence action records (the work items a user must complete on a cadence step). Only actions currently "in_progress" are returned. Filter by ids, step, type, user, person, cadence, multitouch group, due_on and updated_at ranges. Scope: cadences:read. |
| List Activity Histories | `listActivityHistories` | Fetch the customer's past activities as shown on the Salesloft Activity Feed. Filter by activity type, pinned state, resource type and id, user, ids and occurred_at / updated_at ranges. Scope: activities:read. |
| List Audit Reports | `listAuditReports` | List audit reports requested by the tenant, including status and download URL. Scope: audit_reports:read. |
| List Bulk Job Data | `listBulkJobData` | Fetch the job data records uploaded to a bulk job. Page-number pagination is not supported — poll with the id[gt] cursor, passing the last id seen. |
| List Bulk Job Results | `listBulkJobResults` | Fetch the per-record results of a completed bulk job. Returns an empty data array until the job's state is "done". Poll with the id[gt] cursor. |
| List Bulk Jobs | `listBulkJobs` | Fetch bulk job records. Pagination is cursor-based via the id[gt] filter — pass the highest id seen to fetch the next page. Scope: bulk job read access. |
| List Cadence Collections | `listCadenceCollections` | Fetch cadence collection records — groupings of cadences with shared stage, throttling and removal settings. Scope: cadences:read. |
| List Cadence Memberships | `listCadenceMemberships` | Fetch cadence membership records — the association between a person and their current and historical cadences. Filter by person, cadence, whether they are currently on a cadence, and updated_at range. Scope: cadences:read. |
| List Cadence Step Groups | `listCadenceStepGroups` | Fetch the step groups of a cadence, ordered by day and then by position within the day. Each group carries its automation settings and its steps. Scope: cadences:read. |
| List Cadences | `listCadences` | Fetch multiple Salesloft cadence records. Filter by ids, name, owner, team/shared status, groups, tags, archived state and updated_at range. Scope: cadences:read. |
| List Calendar Availabilities | `listCalendarAvailabilities` | Fetch available time slots on a user's calendar within a date range for a desired meeting duration. Scope: meetings:read. |
| List Calendar Events | `listCalendarEvents` | Fetch calendar events synced into Salesloft, paginated and filtered by date window. Scope: meetings:read. |
| List Calendar Events With Recurring | `listCalendarEventsWithRecurring` | Fetch calendar events including expanded occurrences of recurring series, within a required date window. Scope: meetings:read. |
| List Call Data Records | `listCallDataRecords` | Fetch call data records — the raw records of every inbound and outbound call placed through the Salesloft dialer, whether or not a call activity was logged. Filter by ids, call UUIDs, whether a call is logged, user, person, direction, status, sentiment, disposition, recordings, group and start time. Scope: calls:read. |
| List Call Dispositions | `listCallDispositions` | Fetch the team's configured call dispositions. Dispositions are configured in the Salesloft application, not via the API. Use these values for the disposition field on Create Call. Scope: calls:read. |
| List Call Instructions | `listCallInstructions` | Fetch multiple call instruction records — the scripted instructions attached to phone-type cadence actions. Scope: cadences:read. |
| List Call Sentiments | `listCallSentiments` | Fetch the team's configured call sentiments. Sentiments are configured in the Salesloft application, not via the API. Use these values for the sentiment field on Create Call. Scope: calls:read. |
| List Caller IDs | `listCallerIds` | Look up the possible caller-ID matches for a phone number. Multiple entries are returned when the number is present on more than one person. Phone number must be in E.164 format. Scope: calls:read. |
| List Calls | `listCalls` | Fetch multiple logged call activity records. Filter by ids, user, person, sentiment, disposition, positive/connected flags and created_at/updated_at ranges. Scope: calls:read. |
| List Conversations | `listConversations` | Fetch Salesloft Conversations (recorded and transcribed meetings and calls). Filter by title, owner, participating user, account, person, source platform, media type, language code, API-origin flag and created_at / updated_at / duration ranges. Scope: conversations:read. |
| List CRM Account Team Members | `listCrmAccountTeamMembers` | Fetch CRM Account Team Member records for a company, by the company's CRM id. Scope: accounts:read. |
| List CRM Activities | `listCrmActivities` | Fetch CRM activity records — the activity rows Salesloft has written into the connected CRM, including any sync error. Scope: crm:read. |
| List CRM Activity Fields | `listCrmActivityFields` | Fetch the CRM activity field definitions, including picklist values and which fields are createable or nillable. Consume this before sending crm_params on Create Call. Scope: crm:read. |
| List CRM Team Members With Roles | `listCrmTeamMembersWithRoles` | Fetch CRM Account Team Members with their roles, filtered by a person or a search term over email, name or role. Scope: accounts:read. |
| List CRM Users | `listCrmUsers` | Fetch CRM user records mapped to Salesloft users. Scope: crm:read. |
| List Custom Fields | `listCustomFields` | Fetch the team's custom field definitions for people, companies and opportunities. Scope: team:read. |
| List Custom Roles | `listCustomRoles` | Fetch custom role records. A custom role is any role other than the built-in Admin and User roles; each carries its permission set. Scope: team:read. |
| List Data Control Requests | `listDataControlRequests` | List data-control requests (redaction, soft deletion, right-to-be-forgotten) and their execution events. Requires the data_control scope. |
| List Email Template Attachments | `listEmailTemplateAttachments` | Fetch attachments belonging to personal email templates the authenticated user can view, with a download URL per attachment. Scope: emails:read. |
| List Email Templates | `listEmailTemplates` | Fetch multiple personal email template records. Filter by ids, free-text search over title/subject, tags, groups, cadence, ownership, archived and team-template linkage. Scope: emails:read. |
| List Emails | `listEmails` | Fetch multiple email activity records. Filter by ids, user, person, account, cadence, step, template, recipient address, status, bounced/replies/clicks/views flags, one-off, AI-drafted, and updated_at / sent_at ranges. Scope: emails:read. |
| List External ID Configurations | `listExternalIdConfigurations` | List the team's External ID configurations — the declared pairings of a Salesloft object type with an external system-of-record type. Scope: external_id_configuration:read. |
| List External ID Mappings | `listExternalIdMappings` | List External ID mappings — the links between Salesloft record ids and your system-of-record ids. Scope: external_id:read. |
| List Groups | `listGroups` | Fetch Salesloft group records (the team's org hierarchy). Scope: team:read. |
| List Imports | `listImports` | Fetch import records — the batches people were loaded in. Filter by ids, owning users, import type, partial name match and created_at range. Scope: people:read. |
| List Meetings | `listMeetings` | Fetch meeting records booked through Salesloft. Filter by ids, status, person, account, task, event/iCal UIDs, user, cadence, step, meeting type, no-show and attended/booked metric flags, plus start_time / created_at / updated_at ranges. Scope: meetings:read. |
| List Notes | `listNotes` | Fetch multiple Salesloft note records. Filter by ids, the associated record (person or account) and updated_at range. Scope: notes:read. |
| List Opportunities | `listOpportunities` | List Opportunity records synced from the CRM or created via the external opportunities API. Filter by ids, CRM ids, person, account, owner, name, stage, opportunity type, closed/won flags, most recent cadence, tags and created/updated/close date ranges. Scope: opportunities:read. |
| List Opportunity People | `listOpportunityPeople` | List associations between Salesloft people and opportunities (the buying group on an opportunity). Scope: opportunities:read. |
| List Opportunity Stages | `listOpportunityStages` | List opportunity stages synced from the CRM or created via API. Scope: opportunities:read. |
| List Pending Emails | `listPendingEmails` | Fetch emails that are ready to be sent by an external email service. Only emails configured to send through an External Email Client appear here. Scope: emails:read. |
| List People | `listPeople` | Fetch multiple Salesloft person (prospect) records. Filter by ids, email address, name, company, account, owner, person stage, cadence, tags, CRM id, contactability, engagement flags, locale, title/country/state/city and created/updated/last_contacted ranges. Returns data[] plus paging metadata. Scope: people:read. |
| List Person Stages | `listPersonStages` | Fetch the team's person stage records (the pipeline stages a prospect moves through). Scope: people:read. |
| List Phone Number Assignments | `listPhoneNumberAssignments` | Fetch phone number assignment records — which Salesloft dialer number is assigned to which user. Scope: calls:read. |
| List Play Registrations | `listPlayRegistrations` | List Play Registrations created by the owner of the associated integration. Plays are rulesets that turn Signals into actions when indicator criteria match. Scope: signal_registrations:read. |
| List Saved List Views | `listSavedListViews` | Fetch saved list view records — stored filter/column configurations for the people, companies and records lists. Scope: team:read. |
| List Signal Registrations | `listSignalRegistrations` | List Signal Registrations across all integrations. Scope: signal_registrations:read. |
| List Steps | `listSteps` | Fetch multiple cadence step records. Filter by ids, cadence, step type and whether the step has due actions. Scope: cadences:read. |
| List Successes | `listSuccesses` | Fetch success records — people marked as a success, with the email, call, action, cadence and step that preceded it. Scope: people:read. |
| List Tags | `listTags` | Fetch the tags in use on the team. Tags apply across people, accounts, cadences and templates. Scope: team:read. |
| List Tasks | `listTasks` | Fetch multiple Salesloft task records. Tasks associated with cadence steps are NOT returned. Filter by ids, assigned user, person, account, current state, task type, time interval, idempotency key, locale, source, and updated_at / completed_at ranges. Scope: tasks:read. |
| List Team Template Attachments | `listTeamTemplateAttachments` | Fetch attachments belonging to team email templates, with a download URL per attachment. Scope: emails:read. |
| List Team Templates | `listTeamTemplates` | Fetch team-wide email templates. Admins use these to provide templates to the whole team. Filter by ids, search over title/subject, tags, archived state and updated_at range. Scope: emails:read. |
| List Transcription Sentences | `listTranscriptionSentences` | Fetch a transcription's sentence-level data — speaker, text and timing per utterance. Scope: conversations:read. |
| List Transcriptions | `listTranscriptions` | List conversation transcriptions. Filter by ids, language code and created_at / updated_at ranges. Scope: conversations:read. |
| List Users | `listUsers` | List Salesloft users. A non-admin sees only themselves or the whole team depending on the group visibility policy; a team admin sees all users on the team. Filter by ids, guids, emails, group, role, search keywords, active state, seat package, work country, manager, permissions, CRM mapping and calendar connection. Scope: team:read. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | Fetch all of the customer's webhook subscriptions for the calling application. Scope: any valid token. |
| Redact Account | `redactAccount` | DESTRUCTIVE. Run a workflow that redacts a non-user account across all connected systems. dry_run defaults to true — you must explicitly send dry_run=false to change data. Requires the data_control scope. |
| Redact Account And People | `redactAccountAndPeople` | DESTRUCTIVE. Redact and delete all data for an account and every person related to it. dry_run defaults to true — send dry_run=false to actually change data. Requires the data_control scope. |
| Right To Be Forgotten | `rightToBeForgotten` | DESTRUCTIVE / GDPR. Soft delete people and redact all personally identifiable data from those people and their related activity records. dry_run defaults to true — send dry_run=false to actually change data. Requires the data_control scope. |
| Search Meeting Settings | `searchMeetingSettings` | Fetch multiple meeting-setting records (per-user calendar and booking configuration). Despite being a POST, this is a search/list endpoint; its filters are sent as query parameters. Scope: meetings:read. |
| Soft Delete People | `softDeletePeople` | DESTRUCTIVE. Soft delete multiple people by Salesloft person ID. dry_run defaults to true — send dry_run=false to actually change data. Requires the data_control scope. |
| Update Account | `updateAccount` | Update an existing Salesloft account. "domain" must be unique on the current team. Set archived=true to archive the account. Only supplied fields are sent. Scope: accounts:write. |
| Update Bulk Job | `updateBulkJob` | Rename a bulk job and/or mark it ready_to_execute, which starts processing. Only permitted while the job is still in the "open" state. |
| Update Calendar Event | `updateCalendarEvent` | Update a calendar-event-backed meeting by ID — no-show flag, booking/reschedule status, and the calendar provider's event id / iCalUID. Scope: meetings:write. |
| Update Call Data Record | `updateCallDataRecord` | Update a call data record — status, recording URL, linked person, duration or start/end timestamps. melody_call_id cannot be changed once set. Scope: calls:write. |
| Update Email Template | `updateEmailTemplate` | Update a personal email template. Set archived_at to archive it. Scope: emails:write. |
| Update Group | `updateGroup` | Update a Salesloft group's name or move it under a different parent group. Scope: groups:write. |
| Update Import | `updateImport` | Update an import's name or owning user. Admins can update any import on the team; non-admins only their own. Scope: people:write. |
| Update Meeting | `updateMeeting` | Update a Salesloft meeting — mark it as a no-show, change its booking/reschedule status, or attach the calendar provider's event id / iCalUID. Scope: meetings:write. |
| Update Meeting Setting | `updateMeetingSetting` | Update a user's meeting settings — primary calendar, default meeting title/description/location/length, availability windows and limits, buffers, booking-on-behalf and overlap permissions, calendar sync, reminders and out-of-office automation. Scope: meetings:write. |
| Update Note | `updateNote` | Update a Salesloft note. Changes made here are NOT reflected in the connected CRM. Scope: notes:write. |
| Update Opportunity Stage | `updateOpportunityStage` | Update an opportunity stage's name or order. Scope: opportunities:write. |
| Update Pending Email | `updatePendingEmail` | Report the delivery outcome of an email sent by an External Email Client back to Salesloft. Does not affect lofted emails. Scope: emails:write. |
| Update Person | `updatePerson` | Update an existing Salesloft person. Only supplied fields are sent. Scope: people:write. |
| Update Person Stage | `updatePersonStage` | Rename a person stage. Scope: people:write. |
| Update Play Registration | `updatePlayRegistration` | Update a Play Registration's localized name, label, description, matching indicators or default attributes. Scope: signal_registrations:write. |
| Update Saved List View | `updateSavedListView` | Update a saved list view's name, default flag, sharing or stored parameters. Scope: team:write. |
| Update Signal Registration | `updateSignalRegistration` | Update a Signal Registration's type, name, indicators, description, data shape or attributions. Scope: signal_registrations:write. |
| Update Task | `updateTask` | Update a Salesloft task. Set current_state to "completed" to complete it. Only supplied fields are sent. Scope: tasks:write. |
| Update Team Template | `updateTeamTemplate` | Update a team email template. owner_id transfers ownership and requires team admin permissions. Scope: emails:write. |
| Update User | `updateUser` | Update a Salesloft user — activate or deactivate the account, change role, group, seat package, work country or manager. Scope: team:write. |
| Update Webhook Subscription | `updateWebhookSubscription` | Enable or disable an existing webhook subscription. Only the enabled flag can be changed — the event type, callback URL and token are fixed at creation. Scope: any valid token. |
| Upsert Account | `upsertAccount` | Upsert a Salesloft account. upsert_key selects the match field (id, domain, crm_id, name). Returns upsert_type ("create" or "update") plus the account. Scope: accounts:write. |
| Upsert Calendar Event | `upsertCalendarEvent` | Upsert a calendar event. The upsert key is the combination of id and i_cal_uid scoped to calendar_id (override with upsert_key). Used for bulk calendar synchronisation from an external provider. For an External Calendar connection use calendar_id "external_{salesloft_user_guid}". Scope: meetings:write. |
| Upsert Person | `upsertPerson` | Upsert a Salesloft person. upsert_key selects the match field (id, email_address, phone, crm_id). Create and update behaviour is identical to the individual endpoints. Returns upsert_type ("create" or "update") plus the person. Scope: people:write. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Account Created | `account_created` | An account was created; delivers the new account object. Required scope: accounts:read. |
| Account Deleted | `account_deleted` | An account was deleted; delivers the deleted account object. Required scope: accounts:read. |
| Account Updated | `account_updated` | An account was updated; delivers the updated account object. Required scope: accounts:read. |
| Bulk Job Completed | `bulk_job_completed` | A bulk job finished processing; delivers the completed bulk job object. |
| Cadence Created | `cadence_created` | A cadence was created. Needs Personal Cadences: View & Copy and Public/Team Cadences: View. Required scope: cadences:read. |
| Cadence Deleted | `cadence_deleted` | A cadence was deleted. Needs Personal Cadences: View & Copy and Public/Team Cadences: View. Required scope: cadences:read. |
| Cadence Membership Created | `cadence_membership_created` | A person was added to a cadence. Required scope: cadences:read. |
| Cadence Membership Updated | `cadence_membership_updated` | A cadence membership changed. Required scope: cadences:read. |
| Cadence Updated | `cadence_updated` | A cadence was updated. Needs Personal Cadences: View & Copy and Public/Team Cadences: View. Required scope: cadences:read. |
| Call Created | `call_created` | A call was logged; delivers the new call object. Needs the View Team Calls permission. Required scope: calls:read. |
| Call Data Record Created | `call_data_record_created` | A dialer call data record was created. Needs the View Team Calls permission. Required scope: calls:read. |
| Call Data Record Updated | `call_data_record_updated` | A dialer call data record was updated. Needs the View Team Calls permission. Required scope: calls:read. |
| Call Updated | `call_updated` | A logged call was updated. Needs the View Team Calls permission. Required scope: calls:read. |
| Conversation Created | `conversation_created` | A Conversations recording was created. Required scope: conversations:read. |
| Conversation Recording Created | `conversation_recording_created` | A Conversations recording asset became available. Required scope: conversations:read. |
| Conversation Transcript Created | `conversation_transcript_created` | A Conversations transcript became available. Required scope: conversations:read. |
| Email Updated | `email_updated` | An email activity was updated. Body and subject are NOT delivered by this event. Required scope: emails:read. |
| Email Updated (with body and subject) | `email_with_body_and_subject_updated` | An email activity was updated, including its subject and body. Requires the privileged email_contents scope, which is not granted by default. |
| Link Swap | `link_swap` | An email is being sent; delivers the links found in the body so they can be replaced with new links before send. See the Salesloft link-swap guide. Required scope: emails:read. |
| Meeting Booked | `meeting_booked` | A meeting was created; delivers the new meeting event object. Required scope: meetings:read. |
| Meeting Updated | `meeting_updated` | A meeting was updated; delivers the updated meeting event object. Required scope: meetings:read. |
| Note Created | `note_created` | A note was created. Needs View All People and View Team Calls. Required scope: notes:read. |
| Note Deleted | `note_deleted` | A note was deleted. Needs View All People and View Team Calls. Required scope: notes:read. |
| Note Updated | `note_updated` | A note was updated. Needs View All People and View Team Calls. Required scope: notes:read. |
| Person Created | `person_created` | A person was created; delivers the new person object. Required scope: people:read. |
| Person Deleted | `person_deleted` | A person was deleted; delivers the deleted person object. Required scope: people:read. |
| Person Updated | `person_updated` | A person was updated; delivers the updated person object. Required scope: people:read. |
| Step Created | `step_created` | A cadence step was created. Needs Personal Cadences: View & Copy and Public/Team Cadences: View. Required scope: cadences:read. |
| Step Deleted | `step_deleted` | A cadence step was deleted. Salesloft documents this event as delivering the deleted task object. Needs Personal Cadences: View & Copy and Public/Team Cadences: View. Required scope: cadences:read. |
| Step Updated | `step_updated` | A cadence step was updated. Needs Personal Cadences: View & Copy and Public/Team Cadences: View. Required scope: cadences:read. |
| Success Created | `success_created` | A person was marked as a success. Required scope: people:read. |
| Task Completed | `task_completed` | A task was completed; delivers the completed task object. Required scope: tasks:read. |
| Task Created | `task_created` | A task was created. Required scope: tasks:read. |
| Task Deleted | `task_deleted` | A task was deleted. Required scope: tasks:read. |
| Task Updated | `task_updated` | A task was updated. Required scope: tasks:read. |
| User Created | `user_created` | A user was created on the team. Required scope: team:read. |
| User Updated | `user_updated` | A user was updated. Required scope: team:read. |
