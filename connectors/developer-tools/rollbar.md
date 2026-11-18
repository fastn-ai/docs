---
description: "Rollbar is a real-time error tracking and crash reporting platform for web, server and mobile applications."
hidden: true
---

# Rollbar

<img src="../../.gitbook/assets/connectors/lg/rollbar.png" alt="Rollbar logo">

Rollbar is a real-time error tracking and crash reporting platform for web, server and mobile applications. This connector covers the complete Rollbar API v1: reporting occurrences and deploys, browsing and updating items and their occurrences, session replays, item and occurrence metrics and reports, environments, code versions, RQL query jobs, source map and symbol uploads, Slack, PagerDuty, email and webhook notification channels and rules, service links, person deletion jobs, and the account-level administration of projects, project access tokens, teams, users and team invitations.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [rollbar.com](https://rollbar.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `rollbar` |

## Use it

Add Rollbar from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rollbar.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add User To Team | `addUserToTeam` | Add an existing account user to a team, granting them the access that team carries. Uses the account access token from the connection. |
| Assign Team To Project | `assignTeamToProject` | Grant a team access to a project. Uses the account access token from the connection. |
| Cancel Invitation | `cancelInvitation` | Cancel a pending team invitation so the invited address can no longer use it. Uses the account access token from the connection. |
| Cancel RQL Job | `cancelRqlJob` | Cancel a Rollbar Query Language job that is still queued or running. Uses the project access token from the connection, so it operates on the project that token belongs to. |
| Check Team Membership | `checkTeamMembership` | Check whether a user is a member of a team. Rollbar answers 200 when the user is a member and 404 when they are not. Uses the account access token from the connection. |
| Check Team Project Assignment | `checkTeamProjectAssignment` | Check whether a team has been assigned to a project. Rollbar answers 200 when it has and 404 when it has not. Uses the account access token from the connection. |
| Configure Email Notifications | `updateEmailIntegration` | Configure the project's email notification channel - whether it is enabled and whether request parameters are included in the emails. Uses the project access token from the connection, so it operates on the project that token belongs to. |
| Configure PagerDuty Notifications | `updatePagerDutyIntegration` | Configure the project's PagerDuty notification channel - whether it is enabled and which PagerDuty service key to use. Uses the project access token from the connection, so it operates on the project that token belongs to. |
| Configure Slack Notifications | `updateSlackIntegration` | Configure the project's Slack notification channel - whether it is enabled, which Slack service account and default channel to use, and whether to show actionable message buttons. Uses the project access token from the connection, so it operates on the project that token belongs to. |
| Configure Webhook Notifications | `updateWebhookIntegration` | Configure the project's outbound webhook notification channel - whether it is enabled and the URL Rollbar posts notifications to. Uses the project access token from the connection, so it operates on the project that token belongs to. |

<details>

<summary>See 90 more actions</summary>

* **Create Email Notification Rules** `createEmailRules`: Add one or more email notification rules to the project, each defining a trigger, filters and the email configuration. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Create PagerDuty Notification Rules** `createPagerDutyRules`: Add one or more PagerDuty notification rules to the project, each defining a trigger, filters and whether it triggers or resolves an incident. Uses the project access token from the connection, so it operates on the project that token belongs to. Rollbar's published OpenAPI document lists this operation at /api/1/notifications/pagerduty, which returns a router-level 404; the live route is /api/1/notifications/pagerduty/rules.
* **Create Project** `createProject`: Create a new project in the Rollbar account, optionally copying the settings of an existing project. Uses the account access token from the connection.
* **Create Project Access Token** `createProjectAccessToken`: Create a new access token for a project with the chosen scopes and optional rate limit. Uses the account access token from the connection.
* **Create RQL Job** `createRqlJob`: Submit a Rollbar Query Language query. RQL runs asynchronously - the job is queued here and its results are collected with Get RQL Job Results. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Create Service Link** `createServiceLink`: Create a service link on the project from a name and a URL template. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Create Slack Notification Rules** `createSlackRules`: Add one or more Slack notification rules to the project, each defining a trigger, filters and the Slack message configuration. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Create Team** `createTeam`: Create a new team in the Rollbar account with the chosen access level. Uses the account access token from the connection.
* **Create Webhook Notification Rules** `createWebhookRules`: Add one or more webhook notification rules to the project, each defining a trigger, filters and the destination URL and payload format. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Delete Email Notification Rule** `deleteEmailRule`: Delete a single email notification rule from the project. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Delete Occurrence** `deleteOccurrence`: Permanently delete a single occurrence from the project. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Delete PagerDuty Notification Rule** `deletePagerDutyRule`: Delete a single PagerDuty notification rule from the project. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Delete Project** `deleteProject`: Permanently delete a project and all of the data it holds. This cannot be undone. Uses the account access token from the connection.
* **Delete Project Access Token** `deleteProjectAccessToken`: Delete a project access token, identifying the token in the URL path. Any client still using the token will immediately stop being able to authenticate. Uses the account access token from the connection.
* **Delete Project Access Token By Body** `deleteProjectAccessTokenByBody`: Delete a project access token, identifying the token in the request body rather than the URL path. Uses the account access token from the connection. Supply either public_id or project_access_token to identify the token.
* **Delete Service Link** `deleteServiceLink`: Delete a service link from the project. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Delete Session Replay** `deleteSessionReplay`: Permanently delete a recorded session replay. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Delete Slack Notification Rule** `deleteSlackRule`: Delete a single Slack notification rule from the project. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Delete Team** `deleteTeam`: Permanently delete a team. Members of the team are not deleted, but they lose the access the team granted them. Uses the account access token from the connection.
* **Delete Webhook Notification Rule** `deleteWebhookRule`: Delete a single webhook notification rule from the project. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Activated Item Counts Report** `getActivatedCountsReport`: Retrieve the number of items activated per day, bucketed in the project timezone. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Code Version** `getCodeVersion`: Retrieve the detail Rollbar holds for one code version in one environment, including item counts by event type. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Deploy** `getDeploy`: Retrieve a single deploy record by its system-wide deploy ID. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Email Notification Rule** `getEmailRule`: Retrieve a single email notification rule by its ID. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Invitation** `getInvitation`: Retrieve a single team invitation by its ID, including its status. Uses the account access token from the connection.
* **Get Item** `getItem`: Retrieve a single item by its system-wide item ID. This is the id field returned by List Items, not the project counter shown in the Rollbar web UI. Uses the project access token from the connection, so it operates on the project that token belongs to. Item IDs are the id field in List Items responses; the number in a Rollbar item URL is the project counter, which Get Item By Project Counter takes instead.
* **Get Item By Occurrence UUID Or Counter** `getItemByUniqueId`: Look up a single item using either the UUID of one of its occurrences or the item's project counter. Exactly one of the two must be supplied. Uses the project access token from the connection, so it operates on the project that token belongs to. Supply exactly one of uuid or counter - Rollbar returns 400 when neither or both are given.
* **Get Item By Project Counter** `getItemByCounter`: Look up an item by its project counter, the number shown in Rollbar item URLs. Rollbar answers with a 301 redirect to the canonical item resource. Uses the project access token from the connection, so it operates on the project that token belongs to. The counter is the number in Rollbar item URLs such as https://rollbar.com/myaccount/myproject/items/456, not the system-wide item ID.
* **Get Item Metrics** `getItemMetrics`: Retrieve aggregated metrics for a list of items identified by their project counters. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Occurrence** `getOccurrence`: Retrieve a single occurrence, including its full reported payload. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Occurrence Counts Report** `getOccurrenceCountsReport`: Retrieve occurrence counts bucketed by minute, hour or day, optionally filtered by environment, level range or item. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Occurrence Metrics** `getOccurrenceMetrics`: Retrieve occurrence counts over a span of time, with optional filtering, grouping, aggregation and time granularity. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get PagerDuty Notification Rule** `getPagerDutyRule`: Retrieve a single PagerDuty notification rule by its ID. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Person Deletion Job** `getPersonDeletionJob`: Retrieve the status of a person deletion job. Uses the account access token from the connection.
* **Get Project** `getProject`: Retrieve a single project by its ID. Uses the account access token from the connection.
* **Get RQL Job** `getRqlJob`: Retrieve the status of a Rollbar Query Language job, optionally including its result set. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get RQL Job Results** `getRqlJobResults`: Retrieve the result rows of a completed Rollbar Query Language job. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Service Link** `getServiceLink`: Retrieve a single service link by its ID. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Session Replay** `getSessionReplay`: Retrieve a recorded session replay, including its rrweb events, timeline events and session attributes. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Slack Notification Rule** `getSlackRule`: Retrieve a single Slack notification rule by its ID. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Team** `getTeam`: Retrieve a single team by its ID. Uses the account access token from the connection.
* **Get Time To Resolution Metrics** `getTimeToResolutionMetrics`: Retrieve time-to-resolution metrics for one or more projects over a span of time. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get Top Active Items Report** `getTopActiveItemsReport`: Retrieve the most active items in the project over a recent window of up to 168 hours. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Get User** `getUser`: Retrieve a single account user by their user ID. Uses the account access token from the connection.
* **Get Webhook Notification Rule** `getWebhookRule`: Retrieve a single webhook notification rule by its ID. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Invite User To Team** `inviteUserToTeam`: Invite an email address to join a team. Rollbar sends an invitation email to the address. Uses the account access token from the connection.
* **List Deploys** `listDeploys`: List the deploys recorded for the project, newest first. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **List Email Notification Rules** `listEmailRules`: List the email notification rules configured on the project. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **List Environments** `listEnvironments`: List every environment Rollbar has detected in the project. Environments are created automatically from the environment field of reported occurrences. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **List Item Occurrences** `listItemOccurrences`: List all occurrences that belong to a single item, newest first. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **List Items** `listItems`: List the items in the project, newest first, with optional filtering by environment, level, status, framework, assignment and free-text search. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **List Items By Code Version** `listItemsByCodeVersion`: List the items associated with one code version in one environment, filtered by the event the version produced on the item. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **List Occurrences** `listOccurrences`: List all occurrences recorded in the project, newest first. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **List PagerDuty Notification Rules** `listPagerDutyRules`: List the PagerDuty notification rules configured on the project. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **List Project Access Tokens** `listProjectAccessTokens`: List the access tokens defined for a project, including their scopes, status and rate limits. Uses the account access token from the connection.
* **List Project Teams** `listProjectTeams`: List the teams that have been granted access to a project, optionally excluding the built-in teams. Uses the account access token from the connection.
* **List Projects** `listProjects`: List every project in the Rollbar account. Uses the account access token from the connection.
* **List RQL Jobs** `listRqlJobs`: List the Rollbar Query Language jobs submitted for the project, newest first. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **List Service Links** `listServiceLinks`: List the service links configured on the project. Service links turn values in an occurrence payload into links to your own tools. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **List Slack Notification Rules** `listSlackRules`: List the Slack notification rules configured on the project. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **List Team Invitations** `listTeamInvitations`: List the outstanding and historical invitations for a team. Uses the account access token from the connection.
* **List Team Projects** `listTeamProjects`: List the projects a team has been granted access to. Uses the account access token from the connection.
* **List Team Users** `listTeamUsers`: List the users who belong to a team. Uses the account access token from the connection.
* **List Teams** `listTeams`: List every team in the Rollbar account, including the built-in Owners and Everyone teams. Uses the account access token from the connection.
* **List User Projects** `listUserProjects`: List the projects a user can access through their team memberships. Uses the account access token from the connection.
* **List User Teams** `listUserTeams`: List the teams a user belongs to. Uses the account access token from the connection.
* **List Users** `listUsers`: List every user in the Rollbar account, optionally filtered to a single email address. Uses the account access token from the connection.
* **List Webhook Notification Rules** `listWebhookRules`: List the webhook notification rules configured on the project. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Remove Team From Project** `removeTeamFromProject`: Revoke a team's access to a project. Uses the account access token from the connection.
* **Remove User From Team** `removeUserFromTeam`: Remove a user from a team. The user keeps their Rollbar account but loses the access the team granted. Uses the account access token from the connection.
* **Replace Email Notification Rules** `replaceEmailRules`: Replace every email notification rule on the project with the supplied set. Rules not included in the request are removed. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Replace PagerDuty Notification Rules** `replacePagerDutyRules`: Replace every PagerDuty notification rule on the project with the supplied set. Rules not included in the request are removed. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Replace Slack Notification Rules** `replaceSlackRules`: Replace every Slack notification rule on the project with the supplied set. Rules not included in the request are removed. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Replace Webhook Notification Rules** `replaceWebhookRules`: Replace every webhook notification rule on the project with the supplied set. Rules not included in the request are removed. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Report Deploy** `createDeploy`: Record a deploy of your application code in Rollbar. Rollbar uses deploys to attribute new items to a revision and to power deploy notifications. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Report Occurrence** `createItem`: Report a new occurrence (an exception, a crash report or a log message) to Rollbar. Rollbar groups occurrences into items automatically, so this action both creates new items and adds occurrences to existing ones. Requires a project access token with the post_server_item scope, or post_client_item when the platform is browser, android, ios, flash or client.
* **Request Person Deletion** `createPersonDeletionJob`: Queue a job that deletes all data Rollbar holds about a person, identified by their ID, username or email. Use this to service data-deletion requests. Uses the account access token from the connection. Supply exactly one of id, username or email to identify the person.
* **Update Deploy** `updateDeploy`: Update the status or comment of a deploy that has already been reported, for example to mark a deploy as succeeded or failed. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Update Email Notification Rule** `updateEmailRule`: Update a single email notification rule - its trigger, status, filters and email configuration. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Update Item** `updateItem`: Update the state of an item - its status, level, title, assigned user or team, resolved-in version, and snooze settings. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Update PagerDuty Notification Rule** `updatePagerDutyRule`: Update a single PagerDuty notification rule - its trigger, status, filters and incident configuration. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Update Project Access Token Rate Limit** `updateProjectAccessTokenRateLimit`: Update the rate limit of a project access token, identifying the token in the URL path. Uses the account access token from the connection.
* **Update Project Access Token Rate Limit By Body** `updateProjectAccessTokenRateLimitByBody`: Update the rate limit of a project access token, identifying the token in the request body rather than the URL path. Uses the account access token from the connection. Supply either public_id or project_access_token to identify the token.
* **Update Service Link** `updateServiceLink`: Replace an existing service link's name and URL template. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Update Slack Notification Rule** `updateSlackRule`: Update a single Slack notification rule - its trigger, status, filters and Slack message configuration. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Update Webhook Notification Rule** `updateWebhookRule`: Update a single webhook notification rule - its trigger, status, filters and destination configuration. Uses the project access token from the connection, so it operates on the project that token belongs to.
* **Upload dSYM Bundle** `uploadDsym`: Upload a zipped iOS dSYM bundle so Rollbar can symbolicate iOS crash reports. Uses the project access token from the connection, so it operates on the project that token belongs to. Send dsym as a file reference produced by a workflow (for example from ctx.files); Rollbar requires a multipart/form-data upload, which the engine builds only when the input carries a file reference.
* **Upload Flutter Symbols** `uploadFlutterSymbols`: Upload a Flutter symbols file so Rollbar can symbolicate Flutter stack traces for a given code version. Uses the project access token from the connection, so it operates on the project that token belongs to. Send flutter_symbols as a file reference produced by a workflow (for example from ctx.files); Rollbar requires a multipart/form-data upload, which the engine builds only when the input carries a file reference.
* **Upload ProGuard Mapping** `uploadProguard`: Upload an Android ProGuard mapping file so Rollbar can de-obfuscate Android stack traces for a given code version. Uses the project access token from the connection, so it operates on the project that token belongs to. Send mapping as a file reference produced by a workflow (for example from ctx.files); Rollbar requires a multipart/form-data upload, which the engine builds only when the input carries a file reference.
* **Upload Source Map** `uploadSourceMap`: Upload a JavaScript source map so Rollbar can de-obfuscate minified stack frames for a given code version. Uses the project access token from the connection, so it operates on the project that token belongs to. Send source_map as a file reference produced by a workflow (for example from ctx.files); Rollbar requires a multipart/form-data upload, which the engine builds only when the input carries a file reference.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Deploy | `deploy` | A deploy was reported to the project. Delivered when a webhook notification rule with the deploy trigger is enabled on the project. |
| High Occurrence Rate | `item_velocity` | An item exceeded a configured occurrence rate. Note the naming difference: the notification rule is created with the trigger occurrence_rate, but Rollbar delivers event_name item_velocity. The payload carries an extra trigger object describing the window. Delivered when a webhook notification rule with the occurrence_rate trigger is enabled on the project. |
| Item Reactivated | `reactivated_item` | An item that had been resolved occurred again and was reactivated. Delivered when a webhook notification rule with the reactivated_item trigger is enabled on the project. |
| Item Reopened | `reopened_item` | An item that had been resolved was reopened. Delivered when a webhook notification rule with the reopened_item trigger is enabled on the project. |
| Item Resolved | `resolved_item` | An item was marked resolved. Delivered when a webhook notification rule with the resolved_item trigger is enabled on the project. |
| New Item | `new_item` | An error or message was seen for the first time and Rollbar created a new item. Delivered when a webhook notification rule with the new_item trigger is enabled on the project. |
| Occurrence | `occurrence` | Every single occurrence of any item. High volume - use rule filters to narrow it. Delivered when a webhook notification rule with the occurrence trigger is enabled on the project. |
| Tenth Power Occurrence | `exp_repeat_item` | An item crossed a 10^nth occurrence threshold - the 10th, 100th, 1000th occurrence and so on. The payload carries an extra occurrences key holding the threshold that was crossed. Delivered when a webhook notification rule with the exp_repeat_item trigger is enabled on the project. |
