---
description: "Chili Piper is a demand conversion and meeting scheduling platform."
hidden: true
---

# Chili Piper

<img src="../../.gitbook/assets/connectors/chili-piper.png" alt="Chili Piper logo" width="64">

Chili Piper is a demand conversion and meeting scheduling platform. This connector uses the Chili Piper Edge API to manage workspaces, teams, users, distributions, routers, meeting types, meetings, availability, scheduling links, rules, and webhooks.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [chilipiper.com](https://chilipiper.com) |
| **Authentication** | Bearer token |
| **Slug** | `chiliPiper` |

## Use it

Add Chili Piper from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.chiliPiper.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Distro Router | `activateDistroRouter` | Activates a distribution router so it begins evaluating and routing records. |
| Add Users To Team | `addUsersToTeam` | Adds one or more users to a team. |
| Add Users To Workspace | `addUsersToWorkspace` | Adds one or more users to a workspace. |
| Cancel CRM Event | `cancelCrmEvent` | Cancels a meeting identified by its CRM event ID. |
| Cancel Meeting | `cancelMeeting` | Cancels a meeting by its meeting ID, optionally redirecting to a URL on success or failure. |
| Create Admin One-on-One Scheduling Link | `createAdminOneOnOneSchedulingLink` | Creates a one-on-one admin scheduling link for a specific meeting type. meetingTypeIds must reference real, existing meeting types on a real team workspace — blocked on tenants with no team workspace (see Create Meeting Type). |
| Create Concierge Router | `createConciergeRouter` | Creates a Concierge router that qualifies inbound form submissions and books meetings or redirects visitors in real time. The workspaceId must be a team (managed) workspace of the tenant — personal workspaces are rejected with edge.router-workspace-not-manageable. routing.routes (required, may be an empty array) lists ordered rule-matched rows; routing.catchAll (required) is the fallback outcome, either {type:"Redirect", url} or {type:"Schedule", assignment, meetingTypeId}. |
| Create Distribution | `createDistribution` | Creates and immediately publishes a distribution — a reusable assignment pool for round-robin/ownership routing. workspaceId and teamId must be a real team workspace/team of this tenant (edge.access-denied 401 for a personal or foreign workspace — use List Workspaces / List Teams to find real ids). |
| Create Distro Router | `createDistroRouter` | Creates and publishes a Distro router (lead/record routing), left INACTIVE until Activate Distro Router is called. workspaceId must be a real team (managed) workspace of this tenant — personal workspaces are rejected with edge.router-workspace-not-manageable. Distro routes CRM records, not meetings: routing.catchAll needs a real distributionId (from Create Distribution) plus at least one action; routing.trigger needs objectType + a non-empty eventTypes array. |
| Create Group Scheduling Link | `createGroupSchedulingLink` | Creates a group scheduling link (multiple hosts, one shared calendar) for a real meeting type. Requires hostUserId and real meetingTypeIds — blocked on tenants with no team workspace (see Create Meeting Type). |

<details>

<summary>See 93 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Handoff Router | `createHandoffRouter` | Creates and publishes a Handoff router live in one step. workspaceId must be a real team (managed) workspace of this tenant — personal workspaces are rejected. Handoff routers support ONLY Schedule outcomes (no Redirect): every route/catchAll outcome needs {type:"Schedule", assignment:{type:"User",userId}\|{type:"Distribution",distributionId}, meetingTypeId, crmActions?}, so a real meeting type (from Create Meeting Type, itself workspace-gated) is required even to create the router. |
| Create Meeting Type | `createMeetingType` | Creates a reusable team meeting type with product defaults filled in. workspaceId must be a real team (managed) workspace of this tenant — a personal workspace is rejected with edge.meeting-type-workspace-not-manageable ("Workspace ... is a personal workspace and cannot have managed meeting types"). Creation is NOT atomic: description/inviteTitle/inviteDescription/location alternatives/sharedWith are applied by follow-up calls immediately after create, so a failed follow-up leaves a partially-configured meeting type — fix with Update Meeting Type rather than re-creating. |
| Create Meeting Type Reminder | `createMeetingTypeReminder` | Creates a reminder that fires before or after a booked meeting. workspaceId must be a real team (managed) workspace of this tenant — a personal workspace is rejected the same way Create Meeting Type is (edge.meeting-type-workspace-not-manageable), since reminders live on managed meeting types. |
| Create Ownership Scheduling Link | `createOwnershipSchedulingLink` | Creates an ownership scheduling link that books meetings with the CRM-record owner. Requires ownership and distribution config plus real meetingTypeIds — blocked on tenants with no team workspace (see Create Meeting Type). |
| Create Round Robin Scheduling Link | `createRoundRobinSchedulingLink` | Creates a round-robin scheduling link that distributes bookings across a team. Requires real meetingTypeIds and distributionIds — blocked on tenants with no team workspace (see Create Meeting Type, Create Distribution). |
| Create Rule | `createRule` | Creates a new reusable routing rule that routers can reference; live immediately (revision=1). workspaceId must belong to this tenant (edge.access-denied 401 if it does not — the tenant's personal workspace is rejected too; use a real team workspace id from List Workspaces). Choose dto.type "CreateRuleRequest" for a normal rule, or "CreateOwnershipRuleRequest" (adds an optional teamId) for an ownership rule. |
| Create Team | `createTeam` | Creates a new team within a workspace, optionally seeding it with member user IDs. |
| Create Web Experience | `createWebExperience` | Creates a Web Experience (Chat/Scheduling/Offer/Message widget) from typed playbook content and publishes it live immediately. Verified live 2026-08-07: the vendor's own OpenAPI spec types trigger/conversation as untyped JSON (no schema published), and a real call fails with edge.web-experience-invalid-content "DecodingFailure at .location: Missing required field" — trigger.location is a required, vendor-undocumented discriminated union (an "AllPages"/"Everywhere" type guess was rejected as CNil, i.e. not a valid variant). This action's content shape cannot be certified without a real example from Chili Piper (support, SDK, or an existing Web Experience export). |
| Create Webhook | `createWebhook` | Registers a webhook subscription that notifies the given URL when a meeting is created, updated or deleted. |
| Deactivate Distro Router | `deactivateDistroRouter` | Deactivates a distribution router so it stops evaluating and routing records. |
| Delete Admin One-on-One Scheduling Link | `deleteAdminOneOnOneSchedulingLink` | Removes an admin-managed one-on-one scheduling link by its ID. |
| Delete Concierge Router | `deleteConciergeRouter` | Removes a Concierge router by its ID. |
| Delete Distribution | `deleteDistribution` | Deletes a distribution by its ID. |
| Delete Distro Router | `deleteDistroRouter` | Removes a distribution router by its ID. |
| Delete Group Scheduling Link | `deleteGroupSchedulingLink` | Removes a group scheduling link by its ID. |
| Delete Handoff Router | `deleteHandoffRouter` | Removes a Handoff router by its ID. |
| Delete Meeting Type | `deleteMeetingType` | Removes a meeting type by its ID. |
| Delete Meeting Type Reminder | `deleteMeetingTypeReminder` | Removes a meeting type reminder by its ID within a workspace. |
| Delete Ownership Scheduling Link | `deleteOwnershipSchedulingLink` | Removes an ownership-based scheduling link by its ID. |
| Delete Round Robin Scheduling Link | `deleteRoundRobinSchedulingLink` | Removes a round-robin scheduling link by its ID. |
| Delete Rule | `deleteRule` | Removes a rule by its ID. Requires the current revision number for optimistic concurrency. |
| Delete Team | `deleteTeam` | Deletes a team by its team ID. |
| Delete Web Experience | `deleteWebExperience` | Removes a web experience by its ID. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook subscription identified by its trigger type and URL. |
| Export Meetings | `exportMeetings` | Exports booked meetings within a date range as CSV data, optionally filtered by workspace. |
| Find User | `findUser` | Finds users in the organization by a free-text search query matching name or email. |
| Find Users By Filter | `findUsersByFilter` | Finds users using structured filters such as search text, emails, workspace, admin status and specific user IDs. |
| Find Users By IDs | `findUsersByIds` | Finds multiple users by supplying an array of user IDs. Returns the matching user records. |
| Get Available Slots | `getAvailableSlots` | Gets available meeting start times for a given host, attendees and meeting type configuration. |
| Get Combined User Availability | `getCombinedUserAvailability` | Gets the combined available meeting start times for a specific set of users. |
| Get Concierge Router | `getConciergeRouter` | Retrieves a single Concierge router by its router ID. |
| Get CRM Activity URL | `getCrmActivityUrl` | Returns a URL to view the activity timeline for a meeting identified by its CRM event ID. |
| Get Distro Router | `getDistroRouter` | Retrieves a single distribution router by its router ID. |
| Get Handoff Router | `getHandoffRouter` | Retrieves a single Handoff router by its router ID. |
| Get Integration Connection | `getIntegrationConnection` | Returns the organization-wide connection status for a single Chili Piper integration. Org-credential integrations such as Salesforce, HubSpot, Slack, Gong, Outreach and Salesloft report the single org connection; every other integration reports the roll-up of its per-user statuses. |
| Get Meeting | `getMeeting` | Retrieves a single meeting by its meeting ID. |
| Get Meeting Activity URL | `getMeetingActivityUrl` | Returns a URL to view the activity timeline for a specific meeting. |
| Get Meeting By CRM Event | `getMeetingByCrmEvent` | Retrieves a meeting using its CRM event ID. |
| Get Meeting Type | `getMeetingType` | Retrieves a single meeting type by its ID, including duration, location and invite settings. |
| Get Round Robin Availability | `getRoundRobinAvailability` | Gets available slots for the assignees of a flexible round-robin distribution plus any additional required attendees. |
| Get Rule | `getRule` | Retrieves a single routing rule by its rule ID. |
| Get Tenant | `getTenant` | Retrieves information about the authenticated organization's tenant, including its domains and cluster. |
| Get Tenant By ID | `getTenantById` | Retrieves information about a specific tenant by its tenant ID. |
| Get Web Experience | `getWebExperience` | Retrieves a single web experience by its ID. |
| Get Webhook Signing Secret | `getWebhookSigningSecret` | Retrieves the tenant's webhook signing secret, the single key shared by every webhook the tenant has registered. Verify a delivery by computing HMAC-SHA256 over the string "{X-Chili-Timestamp header}.{raw request body}" with this secret and comparing the lowercase hex digest against the X-Chili-Signature header. The secret is provisioned when the first webhook is created, so this returns 404 on a tenant that has never created one. |
| Invite User | `inviteUser` | Invites a new user to the organization by email, optionally assigning a name, roles, licenses and workspaces. |
| List Admin One-on-One Scheduling Links | `listAdminOneOnOneSchedulingLinks` | Lists admin-managed one-on-one scheduling links, optionally filtered by workspace, slug or meeting type. |
| List Available Slots (Paginated) | `listAvailableSlots` | Lists available meeting start times for a host, attendees and meeting type configuration, with pagination support. |
| List Concierge Routers | `listConciergeRouters` | Lists all Concierge (inbound form scheduling) routers in the organization. |
| List Distribution History | `listDistributionHistory` | Lists the Distribution History assignment trail for a workspace, one entry per routed record or booked meeting. Compare distributionUserId (the rep round-robin selected), hostId (who actually got the meeting) and bookerId (who booked it) to audit round-robin fairness and detect skips. Results are ordered by timestamp. |
| List Distributions | `listDistributions` | Lists all meeting and lead distributions configured in the organization. |
| List Distro Logs | `listDistroLogs` | Lists distribution routing logs for a workspace, showing how leads and meetings were assigned. |
| List Distro Routers | `listDistroRouters` | Lists all distribution (distro) routers configured in the organization. |
| List Group Scheduling Links | `listGroupSchedulingLinks` | Lists group scheduling links, optionally filtered by workspace, slug or meeting type. |
| List Handoff Routers | `listHandoffRouters` | Lists all Handoff routers used to route and schedule meetings between reps. |
| List Meeting Type Reminders | `listMeetingTypeReminders` | Lists all meeting type reminders (email or SMS) configured across the organization. |
| List Meeting Types | `listMeetingTypes` | Lists all meeting types defined across the organization's workspaces. |
| List Ownership Scheduling Links | `listOwnershipSchedulingLinks` | Lists ownership-based scheduling links, optionally filtered by workspace, slug, meeting type or distribution. |
| List Personal Scheduling Links | `listPersonalSchedulingLinks` | Lists a user's personal one-on-one scheduling links. |
| List Round Robin Scheduling Links | `listRoundRobinSchedulingLinks` | Lists round-robin scheduling links, optionally filtered by workspace, slug, meeting type or distribution. |
| List Rules | `listRules` | Lists all routing rules configured for the tenant. |
| List Teams | `listTeams` | Reads all teams across the organization's workspaces. |
| List User Scheduling Links | `listUserSchedulingLinks` | Lists all scheduling links available for a specific user. |
| List Web Experiences | `listWebExperiences` | Lists all web experiences (chat, scheduling, offer or message widgets) in the organization. |
| List Webhooks | `listWebhooks` | Lists all webhook subscriptions registered for the organization. |
| List Workspace Users | `listWorkspaceUsers` | Reads all users in the organization, optionally filtered to a single workspace when a workspace ID is provided. |
| List Workspaces | `listWorkspaces` | Reads all workspaces in the organization. Supports pagination through page and pageSize. |
| Mark CRM Event No-Show | `noShowCrmEvent` | Marks a meeting identified by its CRM event ID as a no-show. |
| Mark Meeting No-Show | `noShowMeeting` | Marks a meeting as a no-show by its meeting ID, optionally redirecting on success or failure. |
| Ping API | `pingApi` | Checks that the Chili Piper API is reachable and the API key is valid. Returns a simple health status. (verified live 2026-08-07) |
| Query Meetings | `queryMeetings` | Queries booked meetings within a start and end date range, optionally filtered by workspace. Dates are ISO-8601 timestamps. |
| Read Chat Logs | `readChatLogs` | Reads chat conversation logs for a workspace within a date range. Dates are ISO-8601 timestamps. |
| Read User | `readUser` | Reads detailed information about a single user by their user ID, including licenses and workspace memberships. |
| Remove Users From All Teams | `removeUsersFromAllTeams` | Removes one or more users from all teams across every workspace. |
| Remove Users From All Workspaces | `removeUsersFromAllWorkspaces` | Removes one or more users from every workspace in the organization. |
| Remove Users From Team | `removeUsersFromTeam` | Removes one or more users from a team. |
| Remove Users From Workspace | `removeUsersFromWorkspace` | Removes one or more users from a workspace. |
| Run Resource Scheduler | `runResourceScheduler` | Triggers an on-demand run of a resource scheduler by its ID. |
| Update Admin One-on-One Scheduling Link | `updateAdminOneOnOneSchedulingLink` | Updates an admin-managed one-on-one scheduling link by its ID. |
| Update Concierge Router | `updateConciergeRouter` | Updates a Concierge router by its ID, changing name, routing, form or branding. |
| Update Distribution | `updateDistribution` | Updates a distribution by its ID and publishes the changes. Supports updating weights, calibration, assignment config, capping and team. |
| Update Distro Router | `updateDistroRouter` | Updates a distribution router by its ID, changing name, description or routing configuration. |
| Update Group Scheduling Link | `updateGroupSchedulingLink` | Updates a group scheduling link by its ID. |
| Update Handoff Router | `updateHandoffRouter` | Updates a Handoff router by its ID, changing its name or routing configuration. |
| Update Meeting | `updateMeeting` | Reschedules or reassigns a meeting by its ID, updating start time, assignees, host or additional guests. |
| Update Meeting Type | `updateMeetingType` | Updates an existing meeting type by its ID, changing name, duration, status, location, buffers and invite details. |
| Update Meeting Type Reminder | `updateMeetingTypeReminder` | Updates a meeting type reminder by its ID within a workspace, changing its name, trigger, title or body. |
| Update Ownership Scheduling Link | `updateOwnershipSchedulingLink` | Updates an ownership-based scheduling link by its ID. |
| Update Round Robin Scheduling Link | `updateRoundRobinSchedulingLink` | Updates a round-robin scheduling link by its ID. |
| Update Rule | `updateRule` | Modifies an existing rule. Requires the rule ID, its current revision number for optimistic concurrency, and the updated rule definition. |
| Update User Licenses | `updateUserLicenses` | Updates product licenses for one or more users. The update object maps user IDs to the licenses they should have. |
| Update Web Experience | `updateWebExperience` | Updates a web experience by its ID, changing its name or enabled state. |
| Update Webhook | `updateWebhook` | Updates an existing webhook subscription identified by its trigger type and URL, changing its enabled state or URL. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Meeting Created | `MeetingCreated` | Fires when a meeting is booked in this ChiliPiper tenant. Registration is per trigger type: ChiliPiper stores one (triggerType, url) pair, so the fastn trigger URL is registered once per event you want and the event type is known from the registration rather than from a field in the payload. Verified live against tenant fastn.ai: POST /api/fire-edge/v1/org/webhook returned 200 with the row echoed back, GET /org/webhook/list showed it, PUT /org/webhook toggled enabled, DELETE /org/webhook removed it and the list read back empty. |
| Meeting Deleted | `MeetingDeleted` | Fires when a meeting is cancelled or deleted. Same per-trigger-type registration model as MeetingCreated. Note ChiliPiper's own help centre has previously described cancellation delivery as limited, so confirm against your tenant before relying on it. |
| Meeting Updated | `MeetingUpdated` | Fires when an existing meeting is rescheduled or otherwise changed. Same per-trigger-type registration model as MeetingCreated. |
