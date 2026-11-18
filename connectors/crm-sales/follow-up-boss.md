---
description: "Follow Up Boss is a real-estate CRM (Zillow Group) for lead follow-up, agent assignment and deal tracking."
hidden: true
---

# Follow Up Boss

<img src="../../.gitbook/assets/connectors/follow-up-boss.png" alt="Follow Up Boss logo" width="64">

Follow Up Boss is a real-estate CRM (Zillow Group) for lead follow-up, agent assignment and deal tracking. This connector covers the Follow Up Boss REST API v1 at https://api.followupboss.com/v1: people (contacts) with search, duplicate checking, unclaimed-lead claiming, relationships and attachments; lead activity events; notes; calls; text messages; tasks; appointments with their types and outcomes; deals, deal attachments, deal custom fields and pipelines; lead stages and custom fields; users, teams, groups, ponds and team inboxes; smart lists, action plans, automations and timeframes; email and text message templates with merge; email marketing campaigns and events; reactions and threaded replies; identity and current-user lookups; rate-limit introspection; and full webhook subscription management for every Follow Up Boss event type.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [followupboss.com](https://followupboss.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `followUpBoss` |

## Use it

Add Follow Up Boss from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.followUpBoss.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Reaction | `addReaction` | Adds an emoji reaction to a note or threaded reply. refType names the kind of object and refId its id. Beta feature. |
| Apply Action Plan To Person | `applyActionPlanToPerson` | Enrols a contact in an Action Plan, starting its follow-up sequence. Note that setting contacted to true on the person pauses running action plans, so apply the plan after any such update. |
| Check Duplicate Person | `checkDuplicatePerson` | Checks whether a person already exists in Follow Up Boss by email address or phone number, without creating anything. Supply at least one of email or phone. Use before Create Person when you need to decide between create and update yourself rather than relying on the deduplicate flag. |
| Claim Person | `claimPerson` | Claims an unclaimed lead for the user whose API key is authenticating the request, assigning the person to them and closing the claim window. Get candidate ids from List Unclaimed People. |
| Create Appointment | `createAppointment` | Creates an appointment. Title, start and end are required. Attach people and agents through invitees, categorise it with typeId from List Appointment Types, and set sendInvitation to true to email the invitees. Only appointments created here fire the appointmentsCreated webhook - calendar-synced ones do not. |
| Create Appointment Outcome | `createAppointmentOutcome` | Adds an appointment outcome to the account. orderWeight controls where it appears in the outcome picker - lower values sort first. |
| Create Appointment Type | `createAppointmentType` | Adds an appointment type to the account. orderWeight controls where it appears in the type picker - lower values sort first. |
| Create Call | `createCall` | Logs a call against a contact. Use this to push call activity from an external phone or dialer system into the contact timeline, optionally with a note, disposition, duration and recording link. |
| Create Custom Field | `createCustomField` | Defines a new custom field on people. Supply choices when type is a dropdown, and set isRecurring for an annually repeating date such as a birthday. Follow Up Boss derives the machine name from the label - read it back from the response before writing values to people. |
| Create Deal | `createDeal` | Creates a deal (transaction). Name and stageId are required - the stage determines which pipeline the deal lands in, so read it from List Pipelines. Attach contacts with peopleIds and agents with userIds. Deal custom fields are set with their customField keys - see List Deal Custom Fields. |

<details>

<summary>See 135 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Deal Attachment | `createDealAttachment` | Attaches a file to a deal by reference. Follow Up Boss does not accept a file upload here - host the file yourself and pass a publicly reachable uri. Note that the dealsUpdated webhook does not fire for file changes. Requires the X-System and X-System-Key headers, which the connection supplies automatically. |
| Create Deal Custom Field | `createDealCustomField` | Defines a new custom field on deals. Supply choices when type is a dropdown. Follow Up Boss derives the machine name from the label - read it back from the response before writing values to deals. |
| Create Email Marketing Campaign | `createEmCampaign` | Registers an email marketing campaign in Follow Up Boss so that marketing events can be attributed to it. Set origin to your system's name and originId to your own campaign id, which is how you find it again with List Email Marketing Campaigns. |
| Create Email Marketing Events | `createEmEvents` | Notifies Follow Up Boss about marketing emails your system sent and what happened to them - sends, opens, clicks, bounces, unsubscribes and spam reports. This endpoint takes a batch, so send an array rather than one call per event. Unsubscribe events flow through to the contact's marketing opt-out state. |
| Create Email Template | `createTemplate` | Creates an email template. The body may contain Follow Up Boss merge fields so the template personalises per recipient. Set isShared to true to make it available to the whole account rather than just the authenticated user. |
| Create Event | `createEvent` | Sends a lead or a lead activity into Follow Up Boss. This is the correct entry point for new leads - unlike Create Person it records the inquiry, runs lead routing and assignment, and fires the account's new-lead notifications. Follow Up Boss matches the person block to an existing contact by email or phone and creates one if there is no match. This endpoint is not rate limited (POST.events context). |
| Create Group | `createGroup` | Creates a lead distribution group. users is the rotation membership and distribution picks the strategy. For a first-to-claim group set claimWindow to the number of seconds a lead stays claimable, and use defaultUserId, defaultPondId or defaultGroupId to say where an unclaimed lead falls through to. |
| Create Note | `createNote` | Adds a note to a contact. Set isHtml to true when body contains HTML markup. Notes sit in their own strict rate-limit context: 10 requests per 10 seconds. There is no list endpoint for notes - read them through the notesCreated webhook or Get Note by id. |
| Create People Relationship | `createPeopleRelationship` | Adds a relationship to a contact - for example a spouse, partner or assistant - with their own name, emails, phones and addresses. This is the only endpoint that can set the relationshipId on an email or phone; Update Person cannot. |
| Create Person | `createPerson` | Manually creates a contact (person) in Follow Up Boss. Use Create Event instead when a lead arrives from a lead source, so Follow Up Boss records the inquiry and runs lead routing. Set deduplicate=true to merge into an existing person that matches on email or phone rather than creating a duplicate. Custom fields are set with their customFieldName keys - see List Custom Fields. Returns the created person. |
| Create Person Attachment | `createPersonAttachment` | Attaches a file to a contact by reference. Follow Up Boss does not accept a file upload here - host the file yourself and pass a publicly reachable uri that Follow Up Boss fetches. Requires the X-System and X-System-Key headers, which the connection supplies automatically. |
| Create Pipeline | `createPipeline` | Creates a deal pipeline along with its stages. Pass stages as an ordered array of stage objects; the ids Follow Up Boss returns are the stageId values used when creating deals. |
| Create Pond | `createPond` | Creates a pond. userId is the pond owner and userIds are the agents who can work its contacts. Once it exists, set assignedPondId on a person to move them into it. |
| Create Stage | `createStage` | Adds a lead stage to the account. Once it exists, its name can be set on a person's stage field. orderWeight controls where it appears in the stage list - lower values sort first. |
| Create Task | `createTask` | Creates a task against a contact. Use dueDate for an all-day task or dueDateTime for one with a specific time. Assign it with either assignedUserId or the assignee's full name in assignedTo; if neither is given the task goes to the contact's assigned agent. |
| Create Team | `createTeam` | Creates a team from a set of users. userIds are the members; leaderIds is the subset who lead it and see the team's contacts and reporting. |
| Create Text Message | `createTextMessage` | Records a text message that was sent or received outside Follow Up Boss, so it appears on the contact timeline. This logs an existing message - it does not send one. Requires the X-System and X-System-Key headers, which the connection supplies automatically. |
| Create Text Message Template | `createTextMessageTemplate` | Creates a text message template. The message may contain Follow Up Boss merge fields. Set isShared to true to make it available to the whole account rather than just the authenticated user. |
| Create Webhook | `createWebhook` | Subscribes to a Follow Up Boss event by registering an HTTPS callback URL. One registration covers exactly one event, so subscribe once per event you need. Requires an Owner-level API key and the X-System header, both supplied by the connection - Admin and Broker keys are rejected. Limits: two webhooks per event per system, HTTPS only, and the endpoint must answer 2xx within 10 seconds or Follow Up Boss retries for up to 8 hours and eventually disables the hook. |
| Delete Appointment | `deleteAppointment` | Deletes an appointment by id. Fires the appointmentsDeleted webhook. |
| Delete Appointment Outcome | `deleteAppointmentOutcome` | Deletes an appointment outcome. assignOutcomeId is required - Follow Up Boss reassigns every appointment currently using this outcome to the one you name, so nothing is orphaned. |
| Delete Appointment Type | `deleteAppointmentType` | Deletes an appointment type. assignTypeId is required - Follow Up Boss reassigns every appointment currently using this type to the type you name, so nothing is orphaned. |
| Delete Custom Field | `deleteCustomField` | Deletes a person custom field definition by id. This removes the field and its stored values from every contact in the account, and is irreversible. To clear a single contact's value instead, set that custom field to null with Update Person. |
| Delete Deal | `deleteDeal` | Deletes a deal by id. Fires the dealsDeleted webhook. Deleted deals can still be read back through List Deals with includeDeleted set to true. |
| Delete Deal Attachment | `deleteDealAttachment` | Removes a deal attachment by id. Only the Follow Up Boss reference is deleted - the file at the original uri is untouched. Requires the X-System and X-System-Key headers, which the connection supplies automatically. |
| Delete Deal Custom Field | `deleteDealCustomField` | Deletes a deal custom field definition by id. This removes the field and its stored values from every deal in the account, and is irreversible. |
| Delete Email Template | `deleteTemplate` | Deletes an email template by id. Action plans that reference the template stop being able to send that step, so check usage first. |
| Delete Group | `deleteGroup` | Deletes a lead distribution group by id. Any lead source still routing to it must be repointed first, or new leads will stop being assigned. |
| Delete Note | `deleteNote` | Deletes a note by id. Fires the notesDeleted webhook. Notes sit in their own strict rate-limit context: 10 requests per 10 seconds. |
| Delete People Relationship | `deletePeopleRelationship` | Deletes a person relationship by id, removing the related party and any emails, phones and addresses that belonged to that relationship rather than to the contact. |
| Delete Person | `deletePerson` | Deletes a contact (person) by id. All associated records - notes, calls, text messages, tasks, appointments - are deleted with them, and no per-resource delete webhooks fire for those, only peopleDeleted. This is irreversible; move the person to the Trash stage instead if you may need them back. |
| Delete Person Attachment | `deletePersonAttachment` | Removes a person attachment by id. Only the Follow Up Boss reference is deleted - the file at the original uri is untouched. Requires the X-System and X-System-Key headers, which the connection supplies automatically. |
| Delete Pipeline | `deletePipeline` | Deletes a pipeline by id, together with its stages. Move or delete any deals still in it first. Fires the pipelineDeleted webhook. |
| Delete Pond | `deletePond` | Deletes a pond by id. Reassign the contacts it holds first, or they are left without an owner. |
| Delete Reaction | `deleteReaction` | Removes the authenticated user's reaction from a note or threaded reply. Pass emoji to target one specific reaction when more than one was left. Beta feature. |
| Delete Stage | `deleteStage` | Deletes a lead stage by id. People currently in that stage fall back to the account's default stage. Fires the stageDeleted webhook. |
| Delete Task | `deleteTask` | Deletes a task by id. Fires the tasksDeleted webhook. To close a task without removing it from history, use Update Task with isCompleted true instead. |
| Delete Team | `deleteTeam` | Deletes a team by id. The users themselves are not removed from the account, only the team grouping. |
| Delete Text Message Template | `deleteTextMessageTemplate` | Deletes a text message template by id. Action plans that reference the template stop being able to send that step, so check usage first. |
| Delete User | `deleteUser` | Removes a user from the Follow Up Boss account. Their contacts are not deleted but become unassigned - reassign anything important first. Requires an Owner-level API key. |
| Delete Webhook | `deleteWebhook` | Unsubscribes from a Follow Up Boss event by deleting the webhook registration. Do this for hooks you no longer need - the limit is two per event per registered system, so stale registrations block new ones. Restricted to the account owner and the registered system that created it. |
| Get Appointment | `getAppointment` | Retrieves a single appointment by id, including its type, outcome and invitees. Use this to hydrate an appointmentsCreated or appointmentsUpdated webhook notification, which only carries resource ids. |
| Get Appointment Outcome | `getAppointmentOutcome` | Retrieves a single appointment outcome by id. |
| Get Appointment Type | `getAppointmentType` | Retrieves a single appointment type by id. |
| Get Automation | `getAutomation` | Retrieves a single automation by id, including whether it is enabled and whether it can be triggered manually. |
| Get Automation Person | `getAutomationPerson` | Retrieves a single automation-to-person pairing by id, showing the automation, the contact and the current run status. |
| Get Call | `getCall` | Retrieves a single call record by id, including its note, outcome, duration and recording URL. |
| Get Current User | `getCurrentUser` | Returns the user the API key or access token belongs to, including their id, role, whether they are the account Owner (isOwner - required for webhook management), the account id and the feature flags enabled on the account. Takes no input, so it is the cheapest way to verify a connection. |
| Get Custom Field | `getCustomField` | Retrieves a single person custom field definition by id, including its type and any dropdown choices. Use this to hydrate a customFieldsCreated or customFieldsUpdated webhook notification. |
| Get Deal | `getDeal` | Retrieves a single deal by id, including its pipeline, stage, price, commission split, key dates and the people and agents attached to it. Use this to hydrate a dealsCreated or dealsUpdated webhook notification, which only carries resource ids. |
| Get Deal Attachment | `getDealAttachment` | Retrieves a deal attachment by id, returning its metadata and the uri the file is served from. Requires the X-System and X-System-Key headers, which the connection supplies automatically. |
| Get Deal Custom Field | `getDealCustomField` | Retrieves a single deal custom field definition by id, including its type and any dropdown choices. |
| Get Email Template | `getTemplate` | Retrieves an email template by id. Pass personId to have Follow Up Boss resolve the template's merge fields against that contact and return ready-to-send subject and body. |
| Get Event | `getEvent` | Retrieves a single lead activity event by id, including any property or property-search detail attached to it. |
| Get Group | `getGroup` | Retrieves a single lead distribution group by id, with its members, distribution strategy and fallback assignment settings. |
| Get Identity | `getIdentity` | Returns the account and user the credential resolves to - account id, account domain, account owner name and email, plus the authenticated user. Takes no input and returns a small payload, which makes it the natural connection-verification call and the way to key a multi-account integration by Follow Up Boss account id. |
| Get Note | `getNote` | Retrieves a note by id. Set includeReactions or includeThreadedReplies to true to hydrate the beta reaction and threaded-reply collections, which is what the reactionCreated and threadedReplyCreated webhook payloads point at. |
| Get People Relationship | `getPeopleRelationship` | Retrieves a single person relationship by id, including the related party's name, relationship type and their own emails, phones and addresses. |
| Get Person | `getPerson` | Retrieves a single contact (person) by id. Custom fields and relationship data are omitted unless requested through the fields parameter (use fields=allFields to see everything available). |
| Get Person Attachment | `getPersonAttachment` | Retrieves a person attachment by id, returning its metadata and the uri the file is served from. Requires the X-System and X-System-Key headers, which the connection supplies automatically. |
| Get Pipeline | `getPipeline` | Retrieves a single pipeline by id, including its ordered stages. Use this to hydrate a pipelineCreated or pipelineUpdated webhook notification, which only carries resource ids. |
| Get Pond | `getPond` | Retrieves a single pond by id, with its owner and the agents who work it. |
| Get Rate Limit Limits | `getRateLimitLimits` | Returns only the rate limits currently configured for the calling system, per context. Cheaper than Get Rate Limit Usage because it does no aggregation. Limits are per sliding 10-second window and are roughly halved when requests carry no valid X-System-Key. |
| Get Rate Limit Usage | `getRateLimitUsage` | Returns the calling system's rolling 24-hour request volume, how many of those requests were rate limited, and the limits currently configured for it. Use Get Rate Limit Limits instead when you only need the limit values - this endpoint aggregates and is more expensive. |
| Get Reaction | `getReaction` | Retrieves a single reaction by id. Reactions are a beta feature - emoji responses users leave on notes and threaded replies. Use this to hydrate a reactionCreated webhook, whose data block names the refType and refId the reaction is attached to. |
| Get Smart List | `getSmartList` | Retrieves a single Smart List by id, including its definition. To get its members, pass the id as smartListId on List People. |
| Get Stage | `getStage` | Retrieves a single lead stage by id. Use this to hydrate a stageCreated or stageUpdated webhook notification, which fires when stage definitions change in admin - not when a lead's stage changes. |
| Get Task | `getTask` | Retrieves a single task by id, including its due date, assignee and completion state. Use this to hydrate a tasksCreated or tasksUpdated webhook notification, which only carries resource ids. |
| Get Team | `getTeam` | Retrieves a single team by id, with its member and leader lists. |
| Get Text Message | `getTextMessage` | Retrieves a single text message by id. Use this to hydrate a textMessagesCreated or textMessagesUpdated webhook notification, which only carries resource ids. |
| Get Text Message Template | `getTextMessageTemplate` | Retrieves a text message template by id, with its raw message text including any unresolved merge fields. |
| Get Threaded Reply | `getThreadedReply` | Retrieves a single threaded reply by id. Threaded replies are a beta feature that lets users reply in-line to data entities such as notes. Use this to hydrate a threadedReplyCreated webhook, whose data block names the refType and refId the reply hangs off. |
| Get User | `getUser` | Retrieves a single Follow Up Boss user by id, including their role, email, phone and time zone. |
| Get Webhook | `getWebhook` | Retrieves a single webhook registration by id, including its event, callback URL and status. Requires an Owner-level API key and the X-System header, both supplied by the connection. |
| Get Webhook Event | `getWebhookEvent` | Replays a single webhook delivery by its event id. Use this to recover events your endpoint missed while it was unavailable, including deliveries older than three days that are past the retry window. The id is the eventId from the delivery payload, not a numeric webhook id. Requires the X-System and X-System-Key headers, which the connection supplies automatically. |
| Ignore Unclaimed Person | `ignoreUnclaimedPerson` | Declines an unclaimed lead on behalf of the authenticating user, removing it from their unclaimed queue so it can route on to the next agent in the group. Get candidate ids from List Unclaimed People. |
| List Action Plans | `listActionPlans` | Lists the Action Plans configured in the account - multi-step follow-up sequences of emails, texts and tasks. Use the ids with Apply Action Plan To Person. Agent-level API keys have restricted access to action plans. |
| List Action Plans People | `listActionPlansPeople` | Lists Action Plan enrolments. Pass personId to see which plans a contact is on, or actionPlanId to see who is enrolled in a plan. Each row carries the enrolment id needed by Update Action Plan Person Status. |
| List Appointment Outcomes | `listAppointmentOutcomes` | Lists the appointment outcomes configured in the account - the dispositions an appointment can be closed with, such as Showed, No Show or Cancelled. Use the ids as outcomeId on Update Appointment. |
| List Appointment Types | `listAppointmentTypes` | Lists the appointment types configured in the account - the categories an appointment can be filed under, such as Showing, Listing Presentation or Buyer Consultation. Use the ids as typeId on Create Appointment. |
| List Appointments | `listAppointments` | Searches appointments, optionally scoped to a contact or an agent and to a date window with start and end. Includes appointments synced in from connected Google or Office 365 calendars as well as ones created in Follow Up Boss. |
| List Automations | `listAutomations` | Lists the automations configured in the account - rule-driven sequences that run against contacts. Use enabledOnly to skip disabled ones and manualOnly to find the ones that can be fired on demand through Trigger Automation For Person. |
| List Automations People | `listAutomationsPeople` | Lists automation-to-person pairings - which automations have run or are scheduled to run against which contacts. Filter by personId, automationId or status. Each row carries the pairing id needed by Pause Or Resume Automation For Person. |
| List Calls | `listCalls` | Searches call records logged against contacts, including calls placed through Follow Up Boss dialer and calls pushed in from an external phone system. Filter by contact or by any of the numbers involved. |
| List Custom Fields | `listCustomFields` | Lists the custom fields defined on people, with the machine name each one is read and written under on a person object. Read this before setting custom values on Create Person or Update Person, and before filtering List People by a custom field. Person custom fields only appear in people responses when you ask for them through the fields parameter. |
| List Deal Custom Fields | `listDealCustomFields` | Lists the custom fields defined on deals, with the machine name each one is read and written under on a deal object. Read this before setting custom values on Create Deal or Update Deal. |
| List Deals | `listDeals` | Searches deals (transactions) across pipelines. Filter by pipeline, agent, contact or status. Deleted and archived deals are excluded unless you opt in. The _metadata block includes totalByStageId, which is what a pipeline board uses for its per-column counts. |
| List Email Marketing Campaigns | `listEmCampaigns` | Lists email marketing campaigns registered in Follow Up Boss. Filter by origin and originId to find the campaign that corresponds to a campaign in your own system. |
| List Email Marketing Events | `listEmEvents` | Lists email marketing events recorded against contacts - sends, opens, clicks, bounces, unsubscribes and spam reports pushed in from an external email marketing system. These are distinct from lead activity events on the events endpoint. |
| List Email Templates | `listTemplates` | Lists the email templates in the account, with their subject and body. Templates can contain Follow Up Boss merge fields, which are resolved by Get Email Template with a person id or by Merge Email Template. |
| List Events | `listEvents` | Searches lead activity events - inquiries, property views, saved searches, page visits and similar actions recorded against a contact. This endpoint sits in its own stricter rate-limit context: 20 requests per 10 seconds with a registered system key, 10 without. |
| List Groups | `listGroups` | Lists lead distribution groups - the routing rules that decide which agent a new lead goes to, by round robin, first to claim or a fixed assignment. Distinct from teams, which are a reporting grouping. |
| List Groups With Round Robin | `listGroupsRoundRobin` | Lists lead distribution groups including their live round-robin state - the rotation order and which agent is next in line for a lead. Use this rather than List Groups when you need to know where the rotation currently stands. |
| List People | `listPeople` | Searches contacts (people) in Follow Up Boss. All filters combine with AND. Results are returned newest-first by id; use limit (max 100) with offset, or the keyset cursor from _metadata.next for deep paging. Custom fields and relationships are not returned unless requested through the fields parameter (fields=allFields during development). People in the Trash stage are excluded unless includeTrash is true. |
| List People Relationships | `listPeopleRelationships` | Lists relationships between people - spouse, partner, child, assistant and similar links attached to a contact. You can avoid this call entirely when reading people by including relationships in the fields parameter of List People. |
| List Pipelines | `listPipelines` | Lists deal pipelines with their stages. This is where stageId values for Create Deal and Update Deal come from - a deal's pipeline is implied by the stage it sits in. |
| List Ponds | `listPonds` | Lists ponds - shared pools that hold contacts nobody owns individually, worked by a set of agents. A person sitting in a pond has assignedPondId set instead of an individual assignee. |
| List Smart Lists | `listSmartLists` | Lists the Smart Lists configured in the account - saved, dynamic contact segments such as Stay In Touch or IDX Activity. Feed a smart list id into the smartListId filter on List People to pull that segment's members. |
| List Stages | `listStages` | Lists the lead stages configured in the account, such as Lead, Hot Prospect, Nurture, Past Client and Trash. These are the values the stage field on a person takes - they are not pipeline stages, which live on pipelines. |
| List Tasks | `listTasks` | Lists tasks, filterable by contact, assignee, completion state and due date. Use due for a named window, or dueStart and dueEnd for an explicit date range. |
| List Team Inboxes | `listTeamInboxes` | Lists the shared team inboxes on the account. Their ids are what assignedInboxId refers to when routing a conversation to a shared inbox rather than an individual agent. |
| List Teams | `listTeams` | Lists the teams configured on the account, with their members and team leaders. Teams group agents for reporting and visibility; they are distinct from groups, which control lead distribution. |
| List Text Message Templates | `listTextMessageTemplates` | Lists the text message templates in the account. Like email templates they can contain Follow Up Boss merge fields, resolved by Merge Text Message Template. |
| List Text Messages | `listTextMessages` | Lists text messages for a contact or for a specific phone number. Supply personId, toNumber or fromNumber to scope the result. |
| List Timeframes | `listTimeframes` | Lists the buying or selling timeframes configured in the account, such as 0-3 months or 6-12 months. Their ids are what timeframeId refers to on a person. |
| List Unclaimed People | `listUnclaimedPeople` | Lists unclaimed leads - people routed to a first-to-claim group whose claim window is still open and who no agent has taken yet. Follow with Claim Person to assign one to the authenticated user, or Ignore Unclaimed Person to pass on it. |
| List Users | `listUsers` | Lists the agents, lenders, admins and owners on the Follow Up Boss account. Use this to resolve assignedUserId values for people, tasks and deals. Deleted users are excluded unless includeDeleted is true. |
| List Webhooks | `listWebhooks` | Lists the webhooks registered by the calling system. Requires an Owner-level API key and the X-System header, both supplied by the connection. Follow Up Boss allows only two webhooks per event per registered system, so list and clean up before registering more. |
| Merge Email Template | `mergeTemplate` | Resolves an email template's merge fields for one or many recipients in a single call, returning the personalised subject and body per recipient without sending anything. Use mergePersonId for a single contact, or recipients for a batch. |
| Merge Text Message Template | `mergeTextMessageTemplate` | Resolves a text message template's merge fields for one or many recipients in a single call, returning the personalised message per recipient without sending anything. Use personId for a single contact, or recipients for a batch. |
| Pause Or Resume Automation For Person | `pauseResumeAutomationForPerson` | Pauses or resumes a running automation for a contact. The id is the pairing id from List Automations People, not the automation id or the person id. |
| Trigger Automation For Person | `triggerAutomationForPerson` | Manually starts an automation against a contact. Only automations that are enabled and flagged as manual can be fired this way - use List Automations with manualOnly to find eligible ones. |
| Update Action Plan Person Status | `updateActionPlanPersonStatus` | Pauses, resumes or ends a contact's Action Plan enrolment. The id is the enrolment id from List Action Plans People, not the plan id or the person id. |
| Update Appointment | `updateAppointment` | Updates an appointment by id - reschedule it, change the location, or record how it went by setting outcomeId. Only the supplied fields change. |
| Update Appointment Outcome | `updateAppointmentOutcome` | Renames an appointment outcome or changes its display order. Only the supplied fields change. |
| Update Appointment Type | `updateAppointmentType` | Renames an appointment type or changes its display order. Only the supplied fields change. |
| Update Call | `updateCall` | Updates a logged call by id - typically to attach the note, outcome, duration or recording URL once the call has finished. Only the supplied fields change. Follow Up Boss has no delete endpoint for calls. |
| Update Custom Field | `updateCustomField` | Updates a person custom field definition by id - relabel it, change its dropdown choices or its display order. Only the supplied fields change. This changes the field configuration, not the values stored on people. Changing the order weight can cascade customFieldsUpdated webhooks for other fields whose weights shift. |
| Update Deal | `updateDeal` | Updates a deal by id - move it to another stage with stageId, adjust the price, key dates or commission, or change who is on it. Only the supplied fields change. Follow Up Boss spells two of these fields inconsistently on update: agentCommision and teamComission each drop a letter, which is the API's own naming and is reproduced here so the request is accepted. |
| Update Deal Attachment | `updateDealAttachment` | Updates a deal attachment by id. Follow Up Boss requires dealId, uri and fileName on every update, so resend the current values for anything you are not changing. Requires the X-System and X-System-Key headers, which the connection supplies automatically. |
| Update Deal Custom Field | `updateDealCustomField` | Updates a deal custom field definition by id - relabel it, change its dropdown choices or its display order. Only the supplied fields change. Changing the order weight can cascade dealCustomFieldsUpdated webhooks for other fields whose weights shift. |
| Update Email Marketing Campaign | `updateEmCampaign` | Updates an email marketing campaign by id. Only the supplied fields change. |
| Update Email Template | `updateTemplate` | Updates an email template by id. Only the supplied fields change. |
| Update Group | `updateGroup` | Updates a lead distribution group by id - rename it, change the rotation membership, switch the distribution strategy or adjust the claim window and fallback assignment. users replaces the existing membership rather than adding to it. |
| Update Note | `updateNote` | Edits an existing note by id. Only the supplied fields change. Notes sit in their own strict rate-limit context: 10 requests per 10 seconds. |
| Update People Relationship | `updatePeopleRelationship` | Updates a person relationship by id. Only the supplied fields change. Emails and phones replace the existing lists for the related party. |
| Update Person | `updatePerson` | Updates a contact (person) by id. Only the supplied fields change. Two overwrite traps: tags replaces the whole tag list unless mergeTags is true, and phones/emails replace the whole list including numbers attached to relationships - send the existing entries alongside the new one. Setting contacted to true pauses action plans. Set a custom field to null to clear it. Rate limited to 25 requests per 10 seconds (PUT.people context). |
| Update Person Attachment | `updatePersonAttachment` | Updates a person attachment by id. Follow Up Boss requires personId, uri and fileName on every update, so resend the current values for anything you are not changing. Requires the X-System and X-System-Key headers, which the connection supplies automatically. |
| Update Pipeline | `updatePipeline` | Updates a pipeline by id - rename it, change its description, reorder it, or rewrite its stage list. Include the id of each existing stage you want to keep, otherwise it is treated as new. Changing a stage's order weight can cascade pipelineStageUpdated webhooks for other stages whose weights shift. |
| Update Pond | `updatePond` | Updates a pond by id - rename it, change its owner or change which agents work it. userIds replaces the existing list rather than adding to it. |
| Update Stage | `updateStage` | Renames a lead stage or changes its display order. Renaming updates every person currently in that stage. Fires the stageUpdated webhook. |
| Update Task | `updateTask` | Updates a task by id - reschedule it, reassign it, or mark it complete by setting isCompleted to true. Only the supplied fields change. |
| Update Team | `updateTeam` | Updates a team by id - rename it or change its membership. userIds and leaderIds replace the existing lists rather than adding to them, so send the full intended membership. |
| Update Text Message Template | `updateTextMessageTemplate` | Updates a text message template by id. Only the supplied fields change. |
| Update Webhook | `updateWebhook` | Updates a webhook registration by id - typically to repoint it at a new HTTPS callback URL. Restricted to the account owner and to the registered system that created it. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Appointment Created | `appointmentsCreated` | An appointment was created in Follow Up Boss. Does NOT fire for appointments synced in from a connected Google or Office 365 calendar. |
| Appointment Deleted | `appointmentsDeleted` | An appointment was deleted. uri is null. |
| Appointment Updated | `appointmentsUpdated` | An appointment was rescheduled or given an outcome. Calendar-synced appointments do not fire this event. |
| Call Created | `callsCreated` | A call was logged against a contact. Hydrate with Get Call. |
| Call Deleted | `callsDeleted` | A logged call was removed. uri is null. Note that Follow Up Boss exposes no REST delete for calls, so this fires from in-app deletion. |
| Call Updated | `callsUpdated` | A logged call changed - typically when the note, outcome, duration or recording URL is attached after the call ends. |
| Deal Created | `dealsCreated` | A deal was created. Hydrate with Get Deal. |
| Deal Custom Field Created | `dealCustomFieldsCreated` | A custom field DEFINITION was added to deals. Field configuration only, not values. Hydrate with Get Deal Custom Field. |
| Deal Custom Field Deleted | `dealCustomFieldsDeleted` | A deal custom field definition was deleted, removing its values from every deal. |
| Deal Custom Field Updated | `dealCustomFieldsUpdated` | A deal custom field definition changed. Changing its order weight can cascade extra dealCustomFieldsUpdated events for other fields whose weights shift. |

<details>

<summary>See 43 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Deal Deleted | `dealsDeleted` | A deal was deleted. Still readable through List Deals with includeDeleted set to true. |
| Deal Updated | `dealsUpdated` | A deal changed - stage, price, dates, people or commission. Does NOT fire when only files on the deal change. |
| Email Created | `emailsCreated` | An email was logged against a contact. Follow Up Boss exposes no REST resource for email bodies, so use the resourceIds for correlation only. |
| Email Deleted | `emailsDeleted` | A logged email was deleted. |
| Email Updated | `emailsUpdated` | A logged email changed. |
| Lead Activity Event Created | `eventsCreated` | A contact performed an action on the IDX website - viewed a property, ran a search, visited a page. Hydrate with Get Event. Note the events GET endpoint has a stricter rate limit of 20 requests per 10 seconds. |
| Lead Stage Created | `stageCreated` | A lead stage DEFINITION was added in admin or through the API. This is not a lead moving stage - that is peopleStageUpdated. |
| Lead Stage Deleted | `stageDeleted` | A lead stage definition was removed. Contacts in it fall back to the account default stage. |
| Lead Stage Updated | `stageUpdated` | A lead stage definition was renamed or reordered. Renaming updates every contact in that stage. |
| Marketing Email Clicked | `emEventsClicked` | A contact clicked a link in a marketing email. |
| Marketing Email Opened | `emEventsOpened` | A contact opened a marketing email. Hydrate with List Email Marketing Events. |
| Marketing Email Unsubscribed | `emEventsUnsubscribed` | A contact unsubscribed from marketing emails. Suppress them in your own sending system on this event. |
| Note Created | `notesCreated` | A note was added to a contact. Hydrate with Get Note; pass includeReactions or includeThreadedReplies for the beta collections. |
| Note Deleted | `notesDeleted` | A note was deleted. uri is null. |
| Note Updated | `notesUpdated` | A note was edited. |
| Person Created | `peopleCreated` | A contact was created. Payload carries resourceIds and a uri; hydrate with Get Person or List People. |
| Person Custom Field Created | `customFieldsCreated` | A custom field DEFINITION was added to people. This is about field configuration, not the values stored on contacts. Hydrate with Get Custom Field. |
| Person Custom Field Deleted | `customFieldsDeleted` | A person custom field definition was deleted, removing its values from every contact. |
| Person Custom Field Updated | `customFieldsUpdated` | A person custom field definition changed. Changing its order weight can cascade extra customFieldsUpdated events for other fields whose weights shift. |
| Person Deleted | `peopleDeleted` | A contact was deleted along with all of its notes, calls, text messages, tasks and appointments. No per-resource delete events fire for those. uri is null because the records no longer exist. |
| Person Relationship Created | `peopleRelationshipCreated` | A relationship was added to a contact. Hydrate with Get People Relationship. |
| Person Relationship Deleted | `peopleRelationshipDeleted` | A contact relationship was removed. uri is null. |
| Person Relationship Updated | `peopleRelationshipUpdated` | A contact relationship changed. |
| Person Stage Updated | `peopleStageUpdated` | A contact moved to a different lead stage. The data block names the new stage. This is the lead-level change - stageCreated/Updated/Deleted are about stage definitions in admin. |
| Person Tags Added | `peopleTagsCreated` | One or more tags were added to one or more contacts. The data block names the new tags. Fires again if a tag is removed and re-added. |
| Person Updated | `peopleUpdated` | A contact changed - name, emails, phones, addresses, price, background, assigned agent or lender, contacted flag, stage, source, tags, custom fields, or a relationship. Add fields=allFields to the follow-up GET to see custom field values. Bulk edits are split across multiple deliveries. |
| Pipeline Created | `pipelineCreated` | A deal pipeline was created. Hydrate with Get Pipeline. |
| Pipeline Deleted | `pipelineDeleted` | A pipeline was deleted together with its stages. |
| Pipeline Stage Created | `pipelineStageCreated` | A stage was added to a pipeline. Read it back through Get Pipeline - there is no standalone pipeline-stage endpoint. |
| Pipeline Stage Deleted | `pipelineStageDeleted` | A pipeline stage was removed. |
| Pipeline Stage Updated | `pipelineStageUpdated` | Any pipeline stage property changed. Changing a stage's order weight can cascade extra pipelineStageUpdated events for other stages whose weights shift. |
| Pipeline Updated | `pipelineUpdated` | Any pipeline property changed. Changing a pipeline's order weight can cascade extra pipelineUpdated events for other pipelines whose weights shift. |
| Reaction Created (beta) | `reactionCreated` | A user reacted to a note or threaded reply. The data block names the refType, refId and a refUri that hydrates the parent object with its reactions. |
| Reaction Deleted (beta) | `reactionDeleted` | A reaction was removed from a note or threaded reply. |
| Task Created | `tasksCreated` | A task was created. Hydrate with Get Task. |
| Task Deleted | `tasksDeleted` | A task was deleted. uri is null. |
| Task Updated | `tasksUpdated` | A task was rescheduled, reassigned or completed. |
| Text Message Created | `textMessagesCreated` | A text message was sent or received on a contact. Hydrate with Get Text Message. |
| Text Message Deleted | `textMessagesDeleted` | A text message record was deleted. uri is null. |
| Text Message Updated | `textMessagesUpdated` | A text message record changed, for example its delivery status. |
| Threaded Reply Created (beta) | `threadedReplyCreated` | A user replied in-thread to a note or other entity. The data block names the refType, refId and a refUri that hydrates the parent with its replies. |
| Threaded Reply Deleted (beta) | `threadedReplyDeleted` | A threaded reply was deleted. |
| Threaded Reply Updated (beta) | `threadedReplyUpdated` | A threaded reply was edited. |

</details>
