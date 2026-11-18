---
description: "Figma REST API connector."
hidden: true
---

# Figma

<img src="../../.gitbook/assets/connectors/lg/figma.png" alt="Figma logo">

Figma REST API connector. Read and manage files, comments, versions, components, styles, variables, dev resources, projects, and webhooks (v2). Base URL https://api.figma.com/v1.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [figma.com](https://figma.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Slug** | `figma` |

## Use it

Add Figma from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.figma.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create / Modify / Delete Variables | `postVariables` | Bulk create, update, and delete variables, variable collections, variable modes, and variable mode values in a file. ENTERPRISE-ONLY: requires the file to belong to an Enterprise org and a token with file_variables:write scope. Each array holds action objects whose 'action' field is CREATE, UPDATE, or DELETE. Returns a tempIdToRealId map resolving any temporary ids you supplied to the real ids assigned. |
| Create Dev Resources | `postDevResources` | Bulk create dev resources across multiple files. A dev resource must have a name, url, file_key, and node_id. Returns which links were created and any errors. |
| Create Webhook | `createWebhook` | Creates a new webhook (Webhooks V2) which will call the specified endpoint when the named event fires within a given context (team, project, or file). |
| Create Webhook | `postWebhook` | Creates a new webhook V2 which will call the specified endpoint when the chosen event triggers in the given context (team, project, or file). The passcode is echoed back in each delivered payload for verification. |
| Delete Comment | `deleteComment` | Deletes a specific comment. Only the person who made a comment is allowed to delete it. |
| Delete Comment Reaction | `deleteCommentReaction` | Removes a reaction from a specific comment in a file. The emoji to remove is passed as a required query parameter. |
| Delete Dev Resource | `deleteDevResource` | Delete a single dev resource from a file by its file key and dev resource id. Returns an empty 200 response on success. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook V2 by its ID. Returns the deleted webhook object. |
| Get Activity Logs | `getActivityLogs` | Returns a list of activity log events for the organization. Org/Enterprise plan-gated. Requires a PlanAccessToken (or OrgOAuth2 org:activity_log_read) — a standard PAT will not work. |
| Get Comment Reactions | `getCommentReactions` | Gets a paginated list of reactions left on a specific comment in a file. |
| Get Comments | `getComments` | Gets a list of comments left on the file referenced by file key. Set as_md to true to return comment text as markdown. |
| Get Component | `getComponent` | Returns metadata for a single published component referenced by its key. |
| Get Component Set | `getComponentSet` | Returns metadata for a single published component set referenced by its key. |
| Get Dev Resources | `getDevResources` | Get dev resources in a file. Returns all dev resources attached to nodes in the file, optionally filtered by node IDs. |
| Get Developer Logs | `getDeveloperLogs` | Returns developer (API/MCP) usage logs filtered by the body criteria. This is a POST that reads logs (all filters in the body are optional). Org plan-gated — requires a PlanAccessToken only. |
| Get File | `getFile` | Returns the document referred to by file key as a JSON object, including the node tree, components, styles, and metadata. |
| Get File Component Sets | `getFileComponentSets` | Returns a list of all published component sets within a file library, referenced by file key. |
| Get File Components | `getFileComponents` | Returns a list of all published components within a file library, referenced by file key. |
| Get File Metadata | `getFileMeta` | Returns the metadata for a file referenced by file key. Lighter than getFile; returns name, folder, last touched info, creator, thumbnail, editor type, role, link access, and URL. |
| Get File Nodes | `getFileNodes` | Returns the nodes referenced by the ids as a JSON object. The nodes are retrieved from the Figma file referenced by file key. |
| Get File Styles | `getFileStyles` | Returns a list of all published styles within a file library, referenced by file key. |
| Get File Versions | `getFileVersions` | Returns a list of the version history of a file. The version history consists of versions, manually-saved additions to the version history of a file. |
| Get Image Fills | `getImageFills` | Returns download links for all images present in image fills in a document. Image fills are how Figma represents any user-supplied images. |
| Get Image Renders | `getImages` | Renders images from a file. Returns a map of node IDs to URLs of rendered images for the given nodes. |
| Get Library Analytics Component Actions | `getLibraryAnalyticsComponentActions` | Returns a list of library analytics component actions data within a date range. Enterprise Library Analytics (plan-gated, requires library_analytics:read). group_by is required. |
| Get Library Analytics Component Usages | `getLibraryAnalyticsComponentUsages` | Returns a list of library analytics component usage data. Enterprise Library Analytics (plan-gated, requires library_analytics:read). group_by is required. |
| Get Library Analytics Style Actions | `getLibraryAnalyticsStyleActions` | Returns a list of library analytics style actions data within a date range. Enterprise Library Analytics (plan-gated, requires library_analytics:read). group_by is required. |
| Get Library Analytics Style Usages | `getLibraryAnalyticsStyleUsages` | Returns a list of library analytics style usage data. Enterprise Library Analytics (plan-gated, requires library_analytics:read). group_by is required. |
| Get Library Analytics Variable Actions | `getLibraryAnalyticsVariableActions` | Returns a list of library analytics variable actions data within a date range. Enterprise Library Analytics (plan-gated, requires library_analytics:read). group_by is required. |
| Get Library Analytics Variable Usages | `getLibraryAnalyticsVariableUsages` | Returns a list of library analytics variable usage data. Enterprise Library Analytics (plan-gated, requires library_analytics:read). group_by is required. |
| Get Local Variables | `getLocalVariables` | Returns the local variables created in a file. ENTERPRISE-ONLY: requires the file to belong to an Enterprise org and a token with file_variables:read scope. Returns variables and variableCollections defined locally in the file (not published). |
| Get Me (Current User) | `getMe` | Returns the user information for the currently authenticated user. |
| Get oEmbed | `getOEmbed` | Get oEmbed data for a public Figma file or prototype URL. Returns rich-embed metadata (oEmbed rich type) including embeddable HTML and thumbnail. |
| Get Payments | `getPayments` | Returns the payment information for a user in the context of a plugin, widget, or Community file. Requires either a plugin_payment_token or the user_id + resource ID combination. |
| Get Project Files | `getProjectFiles` | Returns a list of all the files within the specified project. |
| Get Project Metadata | `getProjectMeta` | Returns the metadata for a project referenced by project ID: name, thumbnail, file count, created/updated timestamps. |
| Get Published Variables | `getPublishedVariables` | Returns the variables published from a file as a library. ENTERPRISE-ONLY: requires the file to belong to an Enterprise org and a token with file_variables:read scope. Published variables expose subscribed_id and updatedAt instead of valuesByMode. |
| Get Style | `getStyle` | Returns metadata for a single published style referenced by its key. |
| Get Team Component Sets | `getTeamComponentSets` | Returns a paginated list of all published component sets within a team library. |
| Get Team Components | `getTeamComponents` | Returns a paginated list of all published components within a team library. Use page_size with after/before cursors to paginate. |
| Get Team Projects | `getTeamProjects` | Returns a list of all the projects within the specified team. |
| Get Team Styles | `getTeamStyles` | Returns a paginated list of all published styles within a team library. |
| Get Team Webhooks | `getTeamWebhooks` | [Deprecated] Returns all webhooks registered under the specified team. Prefer Get Webhooks with context=team. Returns an array of webhooks. |
| Get Webhook | `getWebhook` | Returns a single webhook V2 by its ID. |
| Get Webhook Requests | `getWebhookRequests` | Returns the delivery log (most recent requests) sent for a webhook, including request info, response info, and any error messages. Useful for debugging webhook delivery. |
| Get Webhooks | `getWebhooks` | Returns all webhooks for the authenticated user, optionally filtered by context (team\|project\|file) and context_id, or by plan_api_id. Supports cursor pagination. |
| Post Comment | `postComment` | Adds a new comment to the file referenced by file key. Can be a top-level comment or a reply to an existing comment (via comment_id). Optionally pins the comment using client_meta. |
| Post Comment Reaction | `postCommentReaction` | Adds a reaction to a specific comment in a file. The emoji is a shortcode string such as :heart: or :eyes:. |
| Update Dev Resources | `putDevResources` | Bulk update dev resources across multiple files. Each item must include the dev resource id; name and url are optional fields to change. Returns which links were updated and any errors. |
| Update Webhook | `putWebhook` | Updates an existing webhook V2. The event_type, endpoint and passcode are required; status and description are optional. The context cannot be changed after creation. Partial update: only the fields you send are changed. |
| Update Webhook | `updateWebhook` | Updates an existing webhook by ID. Replaces the event type, endpoint, passcode, and optionally status/description. Partial update: only the fields you send are changed. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Dev Mode Status Update | `DEV_MODE_STATUS_UPDATE` | Triggered when the Dev Mode status of a node/section changes (e.g. marked Ready for dev or Completed). |
| Dev Mode Status Update | `DEV_MODE_STATUS_UPDATE` | Sent when the Dev Mode status of a node changes (e.g. marked ready for dev). Carries node and status info. |
| File Comment | `FILE_COMMENT` | Triggered when a comment is posted in a file under the webhook context. |
| File Comment | `FILE_COMMENT` | Sent when a comment is posted in a file. Carries the comment text, comment_id, file info, and the commenting user. |
| File Delete | `FILE_DELETE` | Triggered when a file under the webhook context is deleted. |
| File Delete | `FILE_DELETE` | Sent when a file is deleted. Carries file_key, file_name, and the user who deleted it. |
| File Update | `FILE_UPDATE` | Triggered (debounced ~30 min) when a file under the webhook context is edited and saved. |
| File Update | `FILE_UPDATE` | Sent when there is a change to a file (debounced ~30 minutes after the last edit). Carries file_key, file_name, and triggered_by user. |
| File Version Update | `FILE_VERSION_UPDATE` | Triggered when a named version is created in the file's version history. |
| File Version Update | `FILE_VERSION_UPDATE` | Sent when a named version is created in the version history of a file. Carries version metadata. |
| Library Publish | `LIBRARY_PUBLISH` | Triggered when library components/styles are published from a file. |
| Library Publish | `LIBRARY_PUBLISH` | Sent when a library file is published. Carries created/modified/deleted components and styles. |
| Ping | `PING` | Sent immediately when a webhook is created, to confirm the endpoint is reachable. Carries no resource data. |
| Ping | `PING` | Sent once when a webhook is created or pinged. Confirms the webhook endpoint is reachable. |
