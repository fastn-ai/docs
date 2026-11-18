---
description: "Basecamp 4 (Basecamp 3 API / bc3-api) connector."
hidden: true
---

# Basecamp

Basecamp 4 (Basecamp 3 API / bc3-api) connector. Project management, to-dos, messages, comments, documents, schedules, campfires, card tables, recordings, and webhooks. OAuth 2.0 via 37signals Launchpad. Account ID is supplied per-request in the URL path; every request requires a User-Agent header.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [basecamp.com](https://basecamp.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 292 |
| **Events** | 0 |
| **Slug** | `basecamp` |

## Use it

Add Basecamp from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.basecamp.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Recording | `archiveRecording` | Archive a recording; bc3 answers 403 for types it never lets be archived, timesheet entries among them |
| ArchiveProject | `archiveProject` | Archive a project, removing it from the active project list (returns 204 No Content). Accounts on the admin pro pack may restrict archiving to admins and the project's creator, which answers 403. |
| Change Card Step Completion | `changeCardStepCompletion` | Set card step completion status (PUT with completion: "on" to complete, "" to uncomplete) |
| Complete To-do | `completeTodo` | Mark a todo as complete |
| CompleteSubtask | `completeSubtask` | Mark a subtask as completed |
| Create a chatbot line | `createChatbotLine` | POST /integrations/{chatbotKey}/buckets/{projectId}/chats/{campfireId}/lines.json - posts a line to a Campfire as a chatbot, authenticated by the chatbot key in the URL (from the chatbot's lines_url). Content is rich text; table/tr/td/th/thead/tbody/details/summary are also allowed. Docs: https://github.com/basecamp/bc3-api/blob/master/sections/chatbots.md |
| Create an external link | `createExternalLink` | POST /buckets/{projectId}/dock/doors.json - creates an external link (door) dock tool. Returns 302 to the project with an empty body; the new id is not returned (find it with List recordings type=Door). Get/rename/trash go through the dock tool actions; the door PUT/GET routes are not JSON APIs per the docs. Docs: https://github.com/basecamp/bc3-api/blob/master/sections/external_links.md |
| Create Attachment | `createAttachment` | Upload raw file bytes to get an attachable_sgid for use in uploads, documents, or rich text. Pass the file name via the name query param; send the binary body with the correct Content-Type. |
| Create Campfire Line | `createCampfireLine` | Create a new line (message) in a campfire |
| Create Card | `createCard` | Create a card in a column |
| Create Card Step | `createCardStep` | Create a step on a card |
| Create Card Table Column | `createCardTableColumn` | Create a column in a card table |
| Create Comment | `createComment` | Create a new comment on a recording |
| Create Document | `createDocument` | Create a new document in a vault |
| Create Lineup Marker | `createLineupMarker` | Create a new lineup marker. Returns the created marker. |
| Create Message | `createMessage` | Create a new message on a message board |
| Create Project | `createProject` | Create a new project |
| Create Schedule Entry | `createScheduleEntry` | Create a new schedule entry |
| Create To-do | `createTodo` | Create a new todo in a todolist |
| Create To-do List | `createTodolist` | Create a new todolist in a todoset |
| Create To-do List Group | `createTodolistGroup` | Create a new group in a todolist |
| Create Upload | `createUpload` | Create a new upload in a vault |
| Create Vault | `createVault` | Create a new vault (subfolder) in a vault |
| Create Webhook | `createWebhook` | Create a new webhook for a project |
| CreateAnswer | `createAnswer` | Create a new answer for a question |
| CreateBookmark | `createBookmark` | Bookmark a recording for the current user. Idempotent: re-bookmarking returns the existing bookmark, never a duplicate. |
| CreateBubbleUp | `createBubbleUp` | Bubble up a recording for the current user, resurfacing it in the current user's readings (the BC5 successor to "save"). Returns 204 No Content with no body. The `at` field controls timing. Send `"now"` to bubble up immediately, or a scheduling keyword (`"today"`, `"tomorrow"`, `"weekend"`, `"next_week"`) or an ISO8601 date (e.g. `"2026-09-10"`) to schedule it to resurface later. NOTE: bc3 currently requires `at` — omitting it raises on the server (`Date.iso8601(nil)`), so send `"now"` for the immediate case. The field is modeled optional (not `@required`) so a future bc3 default (`params[:at] \|\|= "now"`) makes omission mean "now" without an SDK change. Idempotent: bubbling up an already-bubbled recording is set-membership and still returns 204. |
| CreateCampfireUpload | `createCampfireUpload` | Upload a file to a campfire |
| CreateChatbot | `createChatbot` | Create a new chatbot for a campfire |
| CreateCloudFile | `createCloudFile` | Create a new cloud file in a vault. `url` is validated against the selected service's patterns, so it must be a real link for that service; use service "other" for anything that matches no recognized service. Omitting `title` is allowed and reads back as "Untitled". |
| CreateEventBoost | `createEventBoost` | Create a boost on a specific event within a recording. Only boostable events accept one: those whose action is completed, adopted, column_changed or moved_in (their JSON includes boosts_count and boosts_url). Any other event answers 403 Forbidden, as does an event on a recording whose comments are closed; an event on a recording the person cannot see answers 404. |
| CreateFolder | `createFolder` | Create a folder for the authenticated user and file the given projects into it. Returns 201 with the new folder and its expanded `projects`, placed at the top of the home screen. Filing an all-access project the user has not joined **grants** them access to it. Every id is preflighted: if any is archived, trashed, or an invitation-only project the user is not on, the whole request fails with 404 and nothing is created — there is no partial success. |
| CreateGaugeNeedle | `createGaugeNeedle` | Create a gauge needle (progress update) for a project |
| CreateGoogleDocument | `createGoogleDocument` | Create a new Google document in a vault. An unrecognized `document_type` is rejected before validation with the field-keyed 422 {"errors": {"document_type": ["is not a valid document type"]}} — the enum would otherwise raise rather than add an error. Omitting `title` is allowed and reads back as "Untitled". |
| CreateMessageType | `createMessageType` | Create a new message type in a project |
| CreatePing | `createPing` | Create a Ping with people, or return the one that already holds exactly them. The caller is always included. Without `new_group`, an existing active Ping with exactly these people (the oldest, if several) is returned rather than a second one created; with `new_group: true` and more than one other person, a new group is created every time. Either way the answer is `201 Created` with the Ping. Answers `403 Forbidden` (`{"error": "Pings have been disabled"}`) when the caller cannot ping, and a bodiless `422` when nobody in the Ping would be a person who can ping. |
| CreateProjectFromTemplate | `createProjectFromTemplate` | Create a project from a template (asynchronous) |
| CreateQuestion | `createQuestion` | Create a new question in a questionnaire |
| CreateRecordingBoost | `createRecordingBoost` | Create a boost on a recording |
| CreateStreamTicket | `createStreamTicket` | Mint a short-lived stream ticket and the exact WebSocket URL to open a live event stream with. The ticket is signed and lives about two minutes; the response's `url` is the one to connect to. Connect to `url` verbatim — never assemble the WebSocket URL (scheme, host, path, account prefix) client-side; the topology is the server's to change. Mint a fresh ticket for every connection attempt: tickets expire and are not refreshed by an open socket. The mint is a stateless signed capability with no server-side consumption, so a replayed POST is harmless and the operation is marked idempotent (safe to retry) — deliberately not a claim that two mints return the same ticket. The ticket is a replayable bearer credential within its window; `ticket` and `url` are marked sensitive (see StreamTicket). Serves agent principals as well as people: an agent's client-credentials token can mint tickets for its own live stream. A ticket minted on a delegated request carries its agent, so `self` on the... |
| CreateSubtask | `createSubtask` | Create a subtask under a to-do or a card Any other recording answers `403 Forbidden`. |
| CreateTemplate | `createTemplate` | Create a new template |
| CreateTemplateLibraryCardTable | `createTemplateLibraryCardTable` | Create a card table template with the default columns |
| CreateTemplateLibraryCopy | `createTemplateLibraryCopy` | Start copying a to-do list or card table template into a project |
| CreateTemplateLibraryTodolist | `createTemplateLibraryTodolist` | Create an empty to-do list template |
| CreateTemplatification | `createTemplatification` | Templatify a to-do list or card table |
| CreateTimesheetEntry | `createTimesheetEntry` | Create a timesheet entry on a recording |
| CreateTodosetTodo | `createTodosetTodo` | Create a to-do directly under a project's to-do set, outside any to-do list. This form exists only project-scoped (no account-scoped variant); parameters and response match the to-do-list create. Find a project's to-do set id via GetTodoset. |
| CreateTool | `createTool` | Create a tool in a project dock |
| CreateUploadVersion | `createUploadVersion` | Replace an upload's file with a new version The recording keeps its id, its URL and its comments; the previous file becomes a past version. Use this instead of CreateUpload when publishing a new release of the same file, so its published link keeps working. |
| CreateWormhole | `createWormhole` | Add a wormhole to a card table: a standing shortcut that sends cards to a column on another card table, usually in another project. A wormhole is the only mechanism for moving a card to a different project: its id is a valid `column_id` for MoveCard, teleporting the card there. It is not needed for a one-off move within a project; MoveCard goes to any column there directly. A card table holds at most four wormholes. `destinationRecordingId` is the id of a column on another accessible card table. |
| Delete Campfire Line | `deleteCampfireLine` | Delete a campfire line; allowed for the line's creator or an admin. The API responds 403 Forbidden otherwise. |
| Delete Lineup Marker | `deleteLineupMarker` | Delete a lineup marker |
| Delete Webhook | `deleteWebhook` | Delete a webhook |
| DeleteBookmark | `deleteBookmark` | Remove the current user's bookmark from a recording (returns 204 No Content). Idempotent: deleting an absent bookmark also returns 204. |
| DeleteBoost | `deleteBoost` | Delete a boost |
| DeleteBubbleUp | `deleteBubbleUp` | Remove the current user's bubble-up from a recording (returns 204 No Content). Idempotent: popping an absent bubble-up also returns 204. |
| DeleteChatbot | `deleteChatbot` | Delete a chatbot |
| DeleteFolder | `deleteFolder` | Delete a folder and unpin its projects from the home screen (returns 204 No Content). The projects themselves are not deleted and are not moved back out onto the home screen; they simply stop appearing there until pinned again. |
| DeleteMessageType | `deleteMessageType` | Delete a message type |
| DeleteSubtask | `deleteSubtask` | Delete a subtask On accounts where deleting is limited to admins and the creator, everyone else gets `403 Forbidden`. |
| DeleteTemplate | `deleteTemplate` | Delete a template (trash it) |
| DeleteTool | `deleteTool` | Delete a tool (trash it) |
| DeleteWormhole | `deleteWormhole` | Permanently delete a card table's wormhole, the shortcut that sends cards to another card table. It does not go to the trash and cannot be restored. |
| DeprioritizeAssignment | `deprioritizeAssignment` | Remove a recording from Up Next (returns 204 No Content). Exact-target: only the priority carried by the identified recording is cleared, and deleting an absent priority is a no-op 204 — so the DELETE is idempotent and safe to retry (BC3 #12483). Address a surfaced card table step by its priority_recording_id, not its parent card's id. |
| DestroyGaugeNeedle | `destroyGaugeNeedle` | Destroy a gauge needle |
| DestroyTimesheetEntry | `destroyTimesheetEntry` | Permanently delete a timesheet entry, which never appears in the trash and cannot be restored; this is the only way to remove one, since bc3 answers 403 to TrashRecording and ArchiveRecording for every timesheet entry, and it answers 403 when the caller may not remove the entry. |
| DisableOutOfOffice | `disableOutOfOffice` | Disable out of office for a person. Admins on Pro Pack accounts can manage others; otherwise self only. |
| DisableProjectClients | `disableProjectClients` | Disable clients on a project 403 while the project still has any client users — revoke them first with UpdateProjectClientAccess. Naturally idempotent: disabling a project with clients already off re-answers `{"clients_enabled": false}`. |
| DisableTool | `disableTool` | Disable a tool (hide it from the project dock) |
| EnableOutOfOffice | `enableOutOfOffice` | Enable or replace out of office for a person. Admins on Pro Pack accounts can manage others; otherwise self only. |
| EnableProjectClients | `enableProjectClients` | Enable clients on a project so client users can be added to it A deliberate step separate from adding clients: it turns on the project's client-facing surface and applies the default client visibility (the timeline and most docked tools become client-visible; the card table, Campfire, and Doors stay private). UpdateProjectClientAccess never enables clients implicitly — enable first, then add. 403 unless the project can have clients (the account supports clients and the project is a standard project). Naturally idempotent: enabling an enabled project re-answers `{"clients_enabled": true}`. |
| EnableTool | `enableTool` | Enable a tool (show it on the project dock) |
| Enroll people | `enrollPeople` | POST /account/enrollments/people.json - enrolls people on the account (sends invitations unless notify=false) and optionally grants access to projects. All-or-nothing; 422 lists per-entry errors. Docs: https://github.com/basecamp/bc3-api/blob/master/sections/people.md |
| Get a hill chart progress update | `getHillChartVersion` | GET /todosets/{id}/hills/versions/{versionId}.json - one progress update of a hill chart. Docs: https://github.com/basecamp/bc3-api/blob/master/sections/hill_charts.md |
| Get a recording | `getRecording` | GET /recordings/{id}.json - generic JSON of any recording by id; use its type to follow up with a type-specific endpoint. Docs: https://github.com/basecamp/bc3-api/blob/master/sections/recordings.md |
| Get backlinks | `getRecordingBacklinks` | GET /recordings/{id}/backlinks.json - the most recent 20 recordings whose rich text references this recording, newest first. Docs: https://github.com/basecamp/bc3-api/blob/master/sections/backlinks.md |
| Get Campfire | `getCampfire` | Get a campfire by ID |
| Get Campfire Line | `getCampfireLine` | Get a campfire line by ID |
| Get Card | `getCard` | Get a card by ID |
| Get Card Table | `getCardTable` | Get a card table by ID |
| Get Card Table Column | `getCardTableColumn` | Get a card column by ID |
| Get Client Approval | `getClientApproval` | Get a single client approval by id |
| Get Client Correspondence | `getClientCorrespondence` | Get a single client correspondence by id |
| Get Client Reply | `getClientReply` | Get a single client reply by id |
| Get Comment | `getComment` | Get a single comment by id |
| Get Document | `getDocument` | Get a single document by id |
| Get hill chart progress updates | `listHillChartVersions` | GET /todosets/{id}/hills/versions.json - paginated progress updates (description, dots, comments_count, comments_url) of a to-do set's hill chart, newest first. Docs: https://github.com/basecamp/bc3-api/blob/master/sections/hill_charts.md |
| Get Message | `getMessage` | Get a single message by id |
| Get Message Board | `getMessageBoard` | Get a message board |
| Get My Profile | `getMyProfile` | Get the current authenticated user's profile |
| Get Person | `getPerson` | Get a person by ID |
| Get Project | `getProject` | Get a single project by id |
| Get Recording Subscription | `getRecordingSubscription` | Get subscription information for a recording |
| Get Schedule | `getSchedule` | Get a schedule |
| Get Schedule Entry | `getScheduleEntry` | Get a single schedule entry by id. Note: Recurring entries will redirect (302) to their recordable URL. Use GetScheduleEntryOccurrence for recurring entries instead. |
| Get To-do | `getTodo` | Get a single todo by id |
| Get To-do List | `getTodolist` | Get a single todolist or todolist group by id The endpoint is polymorphic, but it answers with one shape: BC3 has no group model, so both variants come back as a flat Todolist (see the Todolist shape). |
| Get To-do Set | `getTodoset` | Get a todoset (container for todolists in a project) |
| Get Upload | `getUpload` | Get a single upload by id |
| Get Vault | `getVault` | Get a single vault by id |
| Get Webhook | `getWebhook` | Get a single webhook by id |
| GetAccount | `getAccount` | Get the account for the current access token |
| GetAnswer | `getAnswer` | Get a single answer by id |
| GetAnswersByPerson | `getAnswersByPerson` | Get all answers from a specific person for a question **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. |
| GetAssignedTodos | `getAssignedTodos` | Get todos assigned to a specific person |
| GetBookmark | `getBookmark` | Report whether the current user has bookmarked the recording. |
| GetBoost | `getBoost` | Get a single boost |
| GetBubbleUps | `getBubbleUps` | Get the current user's current and scheduled bubble-ups (paginated, 50 per page). Current bubble-ups are returned first, ordered by most recently bubbled up; scheduled bubble-ups follow, ordered by scheduled bubble-up time. Each item uses the same notification object shape as GetMyNotifications. |
| GetCalendar | `getCalendar` | Get a calendar by its bucket id. A Calendar is a top-level BC5 bucketable (distinct from a project) exposing display metadata and a link to its underlying schedule resource. Shipped scope is show + update only. |
| GetCardStep | `getCardStep` | Get a step by ID |
| GetChatbot | `getChatbot` | Get a chatbot by ID |
| GetCloudFile | `getCloudFile` | Get a single cloud file by id |
| GetEverythingCheckins | `getEverythingCheckins` | Get every automatic check-in answer across all accessible projects, newest-first. Paginated; each item embeds its `bucket`. |
| GetEverythingComments | `getEverythingComments` | Get every comment across all accessible projects, newest-first (paginated). Each item embeds its `bucket`. |
| GetEverythingCompletedCards | `getEverythingCompletedCards` | Completed cards across all accessible projects, grouped by project (paginated). |
| GetEverythingCompletedTodos | `getEverythingCompletedTodos` | Completed to-dos across all accessible projects, grouped by project (paginated). |
| GetEverythingFiles | `getEverythingFiles` | Get every file recording across all accessible projects, newest-first (paginated). Heterogeneous: uploads and Basecamp documents carry their standard recording shapes, while rich-text attachments are wrapped in a recording envelope plus an `attachable_sgid` and blob metadata. Modeled as an optional-field superset (EverythingFile) so one element type decodes any variant. |
| GetEverythingForwards | `getEverythingForwards` | Get every inbox forward across all accessible projects, newest-first (paginated). Each item embeds its `bucket`. |
| GetEverythingMessages | `getEverythingMessages` | Get every message across all accessible projects, newest-first (paginated). Each item embeds its `bucket` for project context. |
| GetEverythingNoDueDateCards | `getEverythingNoDueDateCards` | Open cards with no due date across all accessible projects, grouped by project (paginated). |
| GetEverythingNoDueDateTodos | `getEverythingNoDueDateTodos` | Open to-dos with no due date across all accessible projects, grouped by project (paginated). |
| GetEverythingNotNowCards | `getEverythingNotNowCards` | Cards parked in a project's "Not now" column across all accessible projects, grouped by project (paginated). |
| GetEverythingOpenCards | `getEverythingOpenCards` | Incomplete cards in active columns across all accessible projects, grouped by project (paginated). Each bucket entry carries the matching cards and their steps. |
| GetEverythingOpenTodos | `getEverythingOpenTodos` | Active, incomplete to-dos across all accessible projects, grouped by project (paginated). Each bucket entry carries the matching to-dos and their steps. |
| GetEverythingOverdueCards | `getEverythingOverdueCards` | Get every overdue card across all accessible projects, oldest-due-date-first. A complete, unpaginated array; each item embeds its `bucket`. |
| GetEverythingOverdueTodos | `getEverythingOverdueTodos` | Get every overdue to-do across all accessible projects, oldest-due-date-first. A complete, unpaginated array; each item embeds its `bucket`. |
| GetEverythingUnassignedCards | `getEverythingUnassignedCards` | Open, unassigned cards across all accessible projects, grouped by project (paginated). |
| GetEverythingUnassignedTodos | `getEverythingUnassignedTodos` | Open, unassigned to-dos across all accessible projects, grouped by project (paginated). |
| GetFolder | `getFolder` | Get one folder, with the projects grouped inside it expanded under `projects`. |
| GetForward | `getForward` | Get a forward by ID |
| GetForwardReply | `getForwardReply` | Get a forward reply by ID |
| GetGaugeNeedle | `getGaugeNeedle` | Get a gauge needle by ID |
| GetGoogleDocument | `getGoogleDocument` | Get a single Google document by id |
| GetHillChart | `getHillChart` | Get the hill chart for a todoset |
| GetInbox | `getInbox` | Get an inbox by ID |
| GetMessageType | `getMessageType` | Get a single message type by id |
| GetMyAssignments | `getMyAssignments` | Get the current user's active assignments grouped into priorities and non_priorities. Card table steps are normalized to their parent card with steps as children. This endpoint is not paginated. |
| GetMyCompletedAssignments | `getMyCompletedAssignments` | Get the current user's completed assignments. Archived and trashed recordings are excluded. This endpoint is not paginated. |
| GetMyDueAssignments | `getMyDueAssignments` | Get the current user's assignments filtered by due date scope. Defaults to overdue when no scope is provided. This endpoint is not paginated. |
| GetMyNote | `getMyNote` | Get the authenticated user's note — a per-person notebook singleton at /my/notes.json. If the user has not yet written anything, the shape is the same with empty content and null id/created_at/updated_at; the record is created on first update. |
| GetMyNotifications | `getMyNotifications` | Get the current user's notifications (the "Hey!" menu in Basecamp 4). Notifications are grouped into unreads, reads, bubble-ups, and scheduled bubble-ups (`memories` remains as an always-empty placeholder on BC5). Reads are paginated (50 per page). Unreads are capped at 100. Bubble-ups are capped per `limit_bubble_ups`. |
| GetMyPreferences | `getMyPreferences` | Get the current user's preferences |
| GetOutOfOffice | `getOutOfOffice` | Get the out of office status for a person |
| GetOverdueTodos | `getOverdueTodos` | Get overdue todos grouped by lateness |
| GetPersonProgress | `getPersonProgress` | Get a person's activity timeline |
| GetPing | `getPing` | Get a Ping by its id, which is its bucket's id. Answers `403 Forbidden` (`{"error": "Pings have been disabled"}`) when the caller cannot ping, and `404 Not Found` for a bucket that is not a Ping the caller is in. |
| GetProgressReport | `getProgressReport` | Get account-wide activity feed (progress report) |
| GetProjectConstruction | `getProjectConstruction` | Get the status of a project construction |
| GetProjectTimeline | `getProjectTimeline` | Get project timeline |
| GetProjectTimesheet | `getProjectTimesheet` | Get timesheet for a specific project |
| GetQuestion | `getQuestion` | Get a single question by id |
| GetQuestionnaire | `getQuestionnaire` | Get a questionnaire (automatic check-ins container) by id |
| GetQuestionReminders | `getQuestionReminders` | Get pending check-in reminders for the current user Returns questions that are pending a response from the authenticated user. **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. |
| GetRecordingTimesheet | `getRecordingTimesheet` | Get timesheet for a specific recording |
| GetScheduleEntryOccurrence | `getScheduleEntryOccurrence` | Get a specific occurrence of a recurring schedule entry |
| GetSearchMetadata | `getSearchMetadata` | Get search metadata (available filter options) |
| GetSubtask | `getSubtask` | Get a subtask by ID |
| GetTemplate | `getTemplate` | Get a single template by id |
| GetTemplateLibraryCardTables | `getTemplateLibraryCardTables` | Get the account's card table templates |
| GetTemplateLibraryCopy | `getTemplateLibraryCopy` | Get the current status of a to-do list template copy |
| GetTemplateLibraryTodolists | `getTemplateLibraryTodolists` | Get the account's to-do list templates |
| GetTemplatification | `getTemplatification` | Get a templatification |
| GetTimesheetEntry | `getTimesheetEntry` | Get a single timesheet entry |
| GetTimesheetReport | `getTimesheetReport` | Get account-wide timesheet report |
| GetTool | `getTool` | Get a dock tool by id |
| GetUpcomingSchedule | `getUpcomingSchedule` | Get upcoming schedule entries and assignable items within a date window. This endpoint is preserved as the canonical API path on BC5; the BC5 `/calendar` web view is HTML-only. The three arrays carry the report's own reduced projections — UpcomingScheduleEntry and UpcomingAssignable — not the shared ScheduleEntry and Todo/Card shapes. BC3 renders this report through `app/views/api/schedules/calendar/_entry.json.jbuilder` and `_assignable.json.jbuilder`, which emit a narrower key set than the per-resource partials, plus keys those partials never emit. See UpcomingScheduleEntry for the full accounting. |
| Join a project | `joinProject` | POST /buckets/{projectId}/admissions.json - joins the current person to a project when its admissions policy (team, employee, invite) lets them in. No body. 201 on join, 302 if already a member, 404 if not admitted. Docs: https://github.com/basecamp/bc3-api/blob/master/sections/people.md |
| List Campfire Lines | `listCampfireLines` | List all lines (messages) in a campfire **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Campfires | `listCampfires` | List all campfires across the account **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Cards In Column | `listCards` | List cards in a column **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Client Approvals | `listClientApprovals` | List all client approvals in a project **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Client Correspondences | `listClientCorrespondences` | List all client correspondences in a project **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Client Replies | `listClientReplies` | List all client replies for a recording (correspondence or approval) **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Comments | `listComments` | List comments on a recording **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Documents | `listDocuments` | List documents in a vault **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Messages | `listMessages` | List messages on a message board **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List People | `listPeople` | List all people visible to the current user **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List People On Project | `listProjectPeople` | List all active people on a project **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Pingable People | `listPingablePeople` | List all account users who can be pinged **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Projects | `listProjects` | List projects (active by default; optionally archived/trashed) **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Recording Events | `listRecordingEvents` | List all events for a recording **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Recordings | `listRecordings` | List recordings of a given type across projects **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Schedule Entries | `listScheduleEntries` | List entries on a schedule **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List To-do List Groups | `listTodolistGroups` | List groups in a todolist **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List To-do Lists | `listTodolists` | List todolists in a todoset **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List To-dos | `listTodos` | List todos in a todolist **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Uploads | `listUploads` | List uploads in a vault **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Vaults | `listVaults` | List vaults (subfolders) in a vault **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| List Webhooks | `listWebhooks` | List all webhooks for a project **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| ListAnswers | `listAnswers` | List all answers for a question **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| ListAssignablePeople | `listAssignablePeople` | List people who can be assigned todos |
| ListCampfireUploads | `listCampfireUploads` | List uploaded files in a campfire **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| ListChatbots | `listChatbots` | List all chatbots for a campfire **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| ListEventBoosts | `listEventBoosts` | List boosts on a specific event within a recording. Only boostable events carry boosts: those whose action is completed, adopted, column_changed or moved_in (their JSON includes boosts_count and boosts_url). Any other event answers 403 Forbidden; an event on a recording the person cannot see answers 404. |
| ListFolders | `listFolders` | List the authenticated user's folders in home-screen order. Returns a bare array with no pagination envelope. Items are the base folder shape: they carry `bucket_ids` but **not** the expanded `projects`, which only the single-folder operations return. |
| ListForwardReplies | `listForwardReplies` | List all replies to a forward **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| ListForwards | `listForwards` | List all forwards in an inbox **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| ListGaugeNeedles | `listGaugeNeedles` | List gauge needles for a project, ordered newest first. |
| ListGauges | `listGauges` | List gauges across all projects the authenticated user has access to. Gauges are sorted by risk level (red, yellow, green), then alphabetically. |
| ListLineupMarkers | `listLineupMarkers` | List all lineup markers for the account |
| ListMessageTypes | `listMessageTypes` | List message types in a project **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| ListMyBookmarks | `listMyBookmarks` | List the current user's bookmarks, most recently bookmarked first (paginated). A bookmark is a personal link between the current user and a single recording, visible only to its creator; each entry wraps the shared recording projection. |
| ListMyDrafts | `listMyDrafts` | List the current user's drafts across their active projects, most recently updated first (paginated, capped at 250 like /my/assignments). Five draft kinds are returned: messages, documents, uploads, client approvals, and client correspondences. Drafts under archived or trashed projects are excluded. |
| ListPings | `listPings` | Get Pings: the caller's active Pings that have a line in them, most recently updated first, in one unpaginated response. Archived Pings, and Pings no one has posted in yet, are not listed; GetPing reads either by id. Answers `403 Forbidden` (`{"error": "Pings have been disabled"}`) when the caller cannot ping. |
| ListQuestionAnswerers | `listQuestionAnswerers` | List all people who have answered a question (answerers) **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. |
| ListQuestions | `listQuestions` | List all questions in a questionnaire **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| ListRecentProjects | `listRecentProjects` | List the projects the current user has most recently visited, most recent visit first. Reads the per-user visit log — capped at the 50 most recent visits, keeping only active projects the user can still access — not the home grid's pinned-exclusion and padding. This endpoint is not paginated. Each entry is the standard project projection plus the current user's bookmarked flag. A visit is recorded when the user opens a project in Basecamp, when they create one, and by RecordProjectVisit. |
| ListRecordingBoosts | `listRecordingBoosts` | List boosts on a recording |
| ListSubtasks | `listSubtasks` | List a recording's subtasks, in position order Only to-dos and cards hold subtasks; check for `subtasks_count` and `subtasks_url` on the parent's JSON. **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| ListTemplates | `listTemplates` | List all templates visible to the current user **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| ListUploadVersions | `listUploadVersions` | List versions of an upload **Pagination**: Uses Link header (RFC5988). Follow the `next` rel URL to fetch additional pages. X-Total-Count header provides total count. |
| MarkAsRead | `markAsRead` | Mark specified items as read A batch is capped at 500 readables; a larger one is refused with 422 before any per-item work (bc3 `f3437f5c732`). |
| Move Card | `moveCard` | Move a card to any column in its project, including on another card table there, or through a linked wormhole to another project (queued: the card gets a new id, and position, if sent, must still be positive but doesn't set placement). `column_id` may be any column in the card's project, including a column on another card table in the same project; the card moves there directly, with no wormhole needed. To send the card to another project, pass the id of a linked wormhole (`linked: true`) the card table already has, listed in GetCardTable's `wormholes`; an unlinked or unreachable one returns not found. A move through a wormhole is queued: the card arrives under a new id and its old id then returns not found. `position` does not control where it lands, but if supplied it must still be a positive integer. |
| Move Card Table Column | `moveCardTableColumn` | Move a column to a slot within its card table. target_id is the card table's own id (the same as cardTableId), not a column; position is the 1-based slot among the columns, not counting Triage, Not Now or Done. |
| MoveRecordingToVault | `moveRecordingToVault` | Move a document, upload or vault into another vault in its project, or reorder it in its own vault. Passing the vault it is already in changes only its position. The recording moves in place: its id, comments, bookmarks and history stay with it, and a vault takes everything inside it along. A destination in another project is 404; moves to another project are not this operation. 404, 403 and some 422s carry no body. 403 when the caller may not move the recording (an account can restrict moves to admins and creators). 422 when position is not a positive whole number, the destination is not a vault or is not active, the recording is not active, or a vault would move into one of its own vaults; only the position and vault-cycle refusals carry an `error` message. |
| PauseQuestion | `pauseQuestion` | Pause a check-in question (stops sending reminders) |
| PinMessage | `pinMessage` | Pin a message to the top of the message board |
| PollEvents | `pollEvents` | Poll the account event feed for events after a position (oldest first, strict event-id order, up to 100 per page). **Entry.** With neither `since` nor `position` the feed begins at the present (equivalent to `since=now`). `since=&lt;event id&gt;` starts after that id and `since=0` replays all served history back to the feed's epoch; `since` is a signed 64-bit integer written in decimal, or the literal `now`. `position` resumes from a token a previous page issued — signed, opaque, bound to the account and the filter set. **Pagination**: cursor style — the body envelope, not the Link header. `position` is the durable cursor (persist it only after processing the page's events); `next` is an absolute continuation URL present only while this walk has more to serve. One call answers one page; no generator emits a walk for the cursor style — see the section note. **Errors.** 400 (FeedRequestError) for a malformed position (resume with `since=`) or a malformed filter (fix the filters; a positio... |
| PollInbox | `pollInbox` | Poll the authenticated agent's inbox for the items that addressed it (oldest first, strict item-id order); people receive 403. The inbox is the low-noise "someone addressed you" lane as its own resource rather than a filter over the account feed. **Agents only for now**: any other principal receives 403. An item is a first-class delivery with its own identity: one event can address the same principal for several reasons, and each reason is its own item. Deduplicate by `addressing_id`, never by event id. Items are never self-addressed, are kept for 30 days, and are dropped at read time when the event is no longer readable. **Entry**: `since=0` replays the earliest retained items, `since=now` enters at the present, `position` resumes. Inbox positions are bound to the account, the principal, and the filter set, and are never interchangeable with feed positions. **Pagination**: cursor style, exactly as PollEvents — the body envelope (`items`, `position`, `next`), not the Link header a... |
| PrioritizeAssignment | `prioritizeAssignment` | Add a recording to Up Next — the current user's ordered list of prioritized assignments (the priorities returned by GetMyAssignments). Identify the item by the recording id that carries the priority; for a card table step surfaced under its parent card, that is the entry's priority_recording_id. Idempotent: re-prioritizing an already-prioritized recording is a no-op. |
| RecordProjectVisit | `recordProjectVisit` | Record that the current user visited a project, moving it to the front of ListRecentProjects (returns 204 No Content). Idempotent: re-recording a visit refreshes the same entry. Visits to archived or trashed projects are accepted but not recorded, and an inaccessible project answers 404. |
| Remove Column On Hold | `removeCardTableColumnOnHold` | Disable on-hold section in a column |
| RemoveAccountLogo | `removeAccountLogo` | Remove the account logo. Only administrators and account owners can use this endpoint. |
| ReorderUpNext | `reorderUpNext` | Move an already-prioritized recording to a new 1-based position in Up Next (returns 204 No Content). NOT idempotent: a positional move's meaning shifts as the list changes, so a retry can land the item somewhere else — no retry gating is declared. Errors: 400 for a missing or non-integer position, 422 (flat {error} body) for an out-of-range position or an unprioritized recording, and a bare bodyless 404 for an inaccessible recording. |
| Reposition Card Step | `repositionCardStep` | Reposition a step within a card |
| Reposition To-do | `repositionTodo` | Reposition a todo within its todolist |
| Reposition To-do List Group | `repositionTodolistGroup` | Reposition a todolist group |
| RepositionSubtask | `repositionSubtask` | Move a subtask to a new position among its siblings |
| RepositionTodolist | `repositionTodolist` | Reposition a to-do list within its to-do set. position is the 1-based index among the to-do lists the caller can see; the server translates it relative to loose to-dos and hidden completed lists. Shifts siblings. |
| RepositionTool | `repositionTool` | Reposition a tool on the project dock |
| ResumeQuestion | `resumeQuestion` | Resume a paused check-in question (resumes sending reminders) |
| Search | `search` | Search for content across the account |
| Set Column On Hold | `setCardTableColumnOnHold` | Enable on-hold section in a column |
| SetClientVisibility | `setClientVisibility` | Set client visibility for a recording |
| SpotlightRecording | `spotlightRecording` | Put a recording's card in the spotlight area on its project or template home page. Idempotent: spotlighting an already-spotlighted recording still returns 201. |
| Subscribe To Recording | `subscribeToRecording` | Subscribe the current user to a recording |
| ToggleGauge | `toggleGauge` | Enable or disable the gauge for a project. Only project admins can toggle gauges. |
| Trash Project | `trashProject` | Trash a project (returns 204 No Content) |
| Trash Recording | `trashRecording` | Trash a recording; bc3 answers 403 for types it never lets be trashed, timesheet entries among them (DestroyTimesheetEntry removes those, permanently) |
| Unarchive Recording | `unarchiveRecording` | Unarchive a recording (restore to active status) |
| UnarchiveProject | `unarchiveProject` | Restore a project to active status from trash as well as from the archive (returns 204 No Content). This is the inverse of both ArchiveProject and TrashProject. Restoring counts against the account's project limit, so it answers 507 when that limit is already reached. |
| Uncomplete To-do | `uncompleteTodo` | Mark a todo as incomplete |
| UncompleteSubtask | `uncompleteSubtask` | Mark a subtask as not completed |
| UnpinMessage | `unpinMessage` | Unpin a message from the message board |
| UnspotlightRecording | `unspotlightRecording` | Remove a recording from the spotlight area. Idempotent: removing an absent spotlight also returns 204. |
| Unsubscribe From Recording | `unsubscribeFromRecording` | Unsubscribe the current user from a recording |
| Unwatch Card Table Column | `unwatchCardTableColumn` | Unsubscribe from a card column (stop watching for changes) |
| Update a vault's view | `updateVaultViewPreference` | PUT /vaults/{id}/view_preference.json - sets how the current user sees this vault in Docs & Files (grid or list). 204 on success. Docs: https://github.com/basecamp/bc3-api/blob/master/sections/vaults.md |
| Update Card | `updateCard` | Update an existing card |
| Update Card Step | `updateCardStep` | Update an existing step |
| Update Card Table Column | `updateCardTableColumn` | Update an existing column |
| Update Column Color | `updateCardTableColumnColor` | Set the color of a column |
| Update Comment | `updateComment` | Update an existing comment |
| Update Document | `updateDocument` | Replace a document with a new complete representation. The request body is the document's full writable state: any writable field omitted from the request is cleared server-side. Omitting content clears it; omitting title clears it too, and the document then reads back as "Untitled" (Document#title falls back when blank). Neither field is required. BC3 builds a brand-new Document from the permitted params and swaps the recordable wholesale, and neither attribute carries a presence validation — so an omission is a 200 that clears, not a 422. What BC3 does require is the wrapping document object, which Rails synthesizes from a flat body, so a request naming neither field is a 400. Publishing a draft (status: "active") is not modeled: the SDK sends only title and content, and BC3 rejects a status-only update for the same reason it 400s an empty body. Subscribers are the one exception to omission-clears. A drafted document keeps its current subscribers when the request addresses neith... |
| Update Lineup Marker | `updateLineupMarker` | Update an existing lineup marker. Returns the updated marker. |
| Update Message | `updateMessage` | Update an existing message |
| Update Project | `updateProject` | Update an existing project |
| Update Project Access | `updateProjectAccess` | Update project access (grant/revoke/create people) |
| Update Recording Subscription | `updateRecordingSubscription` | Update subscriptions by adding or removing specific users |
| Update Schedule | `updateSchedule` | Update schedule settings |
| Update Schedule Entry | `updateScheduleEntry` | Replace a schedule entry with a new complete representation. The request body is the entry's full writable state: a writable field omitted from the request is cleared server-side, because BC3 builds a brand-new Schedule::Entry from the permitted params and swaps the recordable wholesale. Three writable fields are carved out of that swap and preserved when the request does not address them — participant_ids, url and highlighted, as declared by preservedOnOmission. Each is a field a caller could not safely resend from a read-back, which is why the guard is server-side: the response carries participants (objects, not ids) and join_url (the entry's own url key is its Basecamp API URL, a different value under a colliding name). Addressing one applies it normally, so participant_ids: [] clears the participants, url: "" clears the join link and highlighted: false removes the highlight. starts_at and ends_at are required: Schedule::Entry validates their presence and Recording validates th... |
| Update To-do | `updateTodo` | Replace a todo with a new complete representation. The request body is the todo's full writable state: any writable field omitted from the request is cleared server-side (empty/missing assignee_ids clears assignees, missing description clears it, and so on). content is required — a request without it is rejected. To set some fields while preserving the rest, use the SDK's merge-safe update or edit methods, which GET the current todo and PUT the full representation back. Those read-modify-write helpers are not atomic: a concurrent write between the GET and PUT is overwritten (last write wins for the whole representation; the window is one round-trip). |
| Update To-do List | `updateTodolist` | Replace a todolist (or todolist group) with a new complete representation. The endpoint is polymorphic - it addresses a to-do list or a group, and answers with the same flat Todolist shape either way. The request body is the recordable's full writable state: TodolistsController#update builds a brand-new Todolist from the permitted params and swaps it in, so any writable field omitted from the request is cleared server-side (a request that omits description erases the description). name is required - it is presence-validated on the model, so a request without it is rejected. To set some fields while preserving the rest, use the SDK's merge-safe update or edit methods, which GET the current list and PUT the full representation back. Those read-modify-write helpers are not atomic: a concurrent write between the GET and PUT is overwritten (last write wins for the whole representation; the window is one round-trip). |
| Update Upload | `updateUpload` | Update an existing upload |
| Update Vault | `updateVault` | Update an existing vault |
| Update Webhook | `updateWebhook` | Update an existing webhook |
| UpdateAccountLogo | `updateAccountLogo` | Upload or replace the account logo. Accepted formats: PNG, JPEG, GIF, WebP, AVIF, HEIC. Maximum 5 MB. Owners and admins only. |
| UpdateAccountName | `updateAccountName` | Rename the current account. Only account owners can use this endpoint. |
| UpdateAnswer | `updateAnswer` | Update an existing answer |
| UpdateBoost | `updateBoost` | Replace the content of a boost. Only the boost's creator may update it: an admin updating someone else's boost gets 403 Forbidden, as does any caller when comments are closed on the boosted recording. A boost on a deleted recording, or in another account, answers 404. A missing or invalid `content` answers a bodiless 422. There is no bucket-scoped route. |
| UpdateCalendar | `updateCalendar` | Update a calendar's display color. An unknown color returns 422 with a JSON errors payload keyed by field ({"errors": {"color": ["is not a valid color"]}}) — the controller rejects invalid enum values up front. |
| UpdateCampfireLine | `updateCampfireLine` | Update an existing campfire line; the content is always treated as rich text (HTML). The server coerces every edited line to rich text and ignores any content type hint. Only the line's creator may edit it, and only text and rich-text lines are editable. |
| UpdateChatbot | `updateChatbot` | Update an existing chatbot |
| UpdateCloudFile | `updateCloudFile` | Replace a cloud file with a new complete representation. BC3 builds a brand-new CloudFile from the permitted params and swaps the recordable wholesale, so the request body is the full writable state: omitting `title` clears it (and the cloud file then reads back as "Untitled"), and omitting `description` clears it. `url` and `service` carry presence/format validations, so they are required here rather than clearable — a request without them is a 422, not a silent wipe. Updating a drafted cloud file also publishes it. Subscribers are the exception to omission-clears: a drafted cloud file keeps its current subscribers when the request addresses neither `subscriptions` nor `notify`. The creator is always on the list. The legacy bucket-scoped path PUT /buckets/{bucketId}/cloud_files/{id}.json is also accepted by BC3; this flat spelling is the documented one. |
| UpdateFolder | `updateFolder` | Rename a folder. `name` is the only writable attribute; a folder's projects, ordering, and image are managed elsewhere and an image parameter sent here is ignored. |
| UpdateGaugeNeedle | `updateGaugeNeedle` | Update a gauge needle's description. Position and color are immutable. |
| UpdateGoogleDocument | `updateGoogleDocument` | Replace a Google document with a new complete representation. BC3 builds a brand-new GoogleDocument from the permitted params and swaps the recordable wholesale, so the request body is the full writable state: omitting `title` clears it (and the document then reads back as "Untitled"), and omitting `description` clears it. `url` and `document_type` are required here — `document_type` because an absent or unrecognized value is a 422, and `url` because it carries a presence validation. Subscribers are the exception to omission-clears: a drafted document keeps its current subscribers when the request addresses neither `subscriptions` nor `notify`. The creator is always on the list. The legacy bucket-scoped path PUT /buckets/{bucketId}/google_documents/{id}.json is also accepted by BC3; this flat spelling is the documented one. |
| UpdateHillChartSettings | `updateHillChartSettings` | Track or untrack todolists on a hill chart |
| UpdateMessageType | `updateMessageType` | Update an existing message type |
| UpdateMyNote | `updateMyNote` | Replace the note's content, recording a new revision server-side. The first update also creates the underlying notebook if the user did not have one yet. Returns the updated note. Rejections arrive as a field-keyed 422 ({"errors": {"content": ["can't be blank"]}}), not the flat {error} body. |
| UpdateMyPreferences | `updateMyPreferences` | Update the current user's preferences. Rejections arrive as a field-keyed 422 ({"errors": {"time_zone_name": ["is not included in the list"]}}), not the flat {error} body. |
| UpdateMyProfile | `updateMyProfile` | Update the current authenticated user's profile (returns 204 No Content) |
| UpdateProjectClientAccess | `updateProjectClientAccess` | Update project client access (grant/revoke/create client users) The client-side counterpart to UpdateProjectAccess: `grant` adds existing client users by id, `revoke` removes client users, and `create` invites brand-new clients by email (`name` optional, defaulting to the address). Only client users are eligible — a `grant` id belonging to a team member is rejected (omitted from `granted`) rather than cross-graded, and `revoke` never removes a team member. The response mirrors UpdateProjectAccess: `granted` and `revoked` people, each with `client: true`. Requires clients to be enabled on the project (EnableProjectClients); otherwise 403. Invitations are all-or-nothing: an invalid `create` row (including one with no email address) answers 422 with the rejected addresses and nobody is invited; new addresses that would exceed the account's user limit answer 429 and nobody is invited. Addresses already on the account take no seat and a repeated address counts once. The seat-limit 429 ... |
| UpdateQuestion | `updateQuestion` | Update an existing question's title, schedule or both. A schedule replaces the whole schedule, so send every part of it: one without frequency or time_of_day is refused, and one without start_date re-anchors the recurrence on today. Pausing and resuming are PauseQuestion and ResumeQuestion. |
| UpdateQuestionNotificationSettings | `updateQuestionNotificationSettings` | Update notification settings for a check-in question |
| UpdateSubtask | `updateSubtask` | Update a subtask A partial update: every omitted parameter is left unchanged. Clearing a value takes an explicit send — `"due_on": null` clears the due date (an empty string is accepted too, and is what the Ruby, Python and TypeScript SDKs send, since they drop nil, None and undefined from the body); `"assignee_ids": []` removes every assignee. Send at least one parameter: an empty body is refused with `400 Bad Request`. |
| UpdateTemplate | `updateTemplate` | Update an existing template |
| UpdateTimesheetEntry | `updateTimesheetEntry` | Update a timesheet entry |
| UpdateTool | `updateTool` | Update (rename) an existing tool |
| UpdateWormhole | `updateWormhole` | Point a card table's wormhole, its shortcut for sending cards to another card table, at a different destination column |
| Watch Card Table Column | `watchCardTableColumn` | Subscribe to a card column (watch for changes) |
