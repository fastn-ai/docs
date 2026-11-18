---
description: "Hootsuite is a social media management platform for scheduling, approving, and publishing content across connected social profiles."
hidden: true
---

# Hootsuite

<img src="../../.gitbook/assets/connectors/lg/hootsuite.png" alt="Hootsuite logo">

Hootsuite is a social media management platform for scheduling, approving, and publishing content across connected social profiles. This connector covers the Hootsuite Platform REST API 1.0: outbound message scheduling and approval workflows, comment approvals, media uploads, social profiles, the authenticated member, organizations, teams, members and their permissions, and SCIM 2.0 user and group provisioning.

| | |
| --- | --- |
| **Category** | [Social media](README.md) |
| **Website** | [hootsuite.com](https://hootsuite.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `hootsuite` |

## Use it

Add Hootsuite from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.hootsuite.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Member To Team | `addMemberToTeam` | Add member to team. Adds a member to a team. |
| Approve Comment | `approveComment` | Approve comment. Approve a comment. |
| Approve Message | `approveMessage` | Approve message. Approve a message. |
| Create Media Upload URL | `createMediaUploadUrl` | Create media upload url. Creates an Amazon S3 upload URL that can be used to transfer media to Hootsuite which ensures the media is available when a scheduled message is sent to the social network. Hootsuite will generate thumbnails and key frames and return a unique media identifier that can be passed when creating a message. Subsequent uploads to an upload URL will be accepted by Amazon but immediately deleted by Hootsuite and only the first valid media file uploaded will be used. The MIME type and size provided in this call must match the MIME type and size of the media uploaded. After requesting an upload URL, make a `PUT` request to the `uploadUrl` returned, an example cURL request would look like the following, replace the fields as appropriate: ``` curl --location --request PUT 'https://hootsuite-video.s3.amazonaws.com/production/12255244_01942650-3d42-42b8-a191-aa84eb45d105.mp4?AWSAccessKeyId=AKIAIM7ASX2JTE3ZFAAA&Expires=1471978770&Signature=b%2B196oEHxySdmE%2FC34ZRL6pXSAI%3... |
| Create Member | `createMember` | Create member. Creates a member in a Hootsuite organization. Requires organization manage members permission. |
| Create SCIM Group | `createScimGroup` | Create Group. Creates a Hootsuite team using the SCIM 2.0 protocol. |
| Create SCIM User | `createScimUser` | Create User. Creates a Hootsuite user using the SCIM 2.0 protocol. |
| Create Team | `createTeam` | Create team. Creates a team in an organization. |
| Delete Message | `deleteMessage` | Delete message. Deletes a message. A message is always associated with a single social profile. |
| List Member Organizations | `listMemberOrganizations` | Retrieve member's organizations. Retrieves the organizations that the member is in. |

<details>

<summary>See 36 more actions</summary>

* **List My Ad Accounts** `retrieveMyAdAccounts`: Retrieve authenticated member's ad accounts. Retrieves the ad accounts that the authenticated user has permissions on.
* **List My Organizations** `retrieveMyOrganizations`: Retrieve authenticated member's organizations. Retrieves the organizations that the authenticated member is in.
* **List My Social Profiles** `retrieveMySocialProfiles`: Retrieve authenticated member's social profiles. Retrieves the social media profiles that the authenticated user has BASIC_USAGE permissions on.
* **List Organization Member Social Profiles** `listOrganizationMemberSocialProfiles`: Retrieve org member’s social profiles. Retrieves the organization's social profiles that an organization member can access.
* **List Organization Member Teams** `listOrganizationMemberTeams`: Retrieve org member's teams. Retrieves the teams an organization member is in.
* **List Organization Members** `listOrganizationMembers`: Retrieve organization members. Retrieves the members in an organization
* **List Organization Teams** `listOrganizationTeams`: Retrieve organization teams. Retrieves a list of teams for a given organization.
* **List Outbound Messages** `listMessages`: Retrieve outbound messages. Outbound messages are messages that are scheduled or were previously sent. This endpoint returns outbound messages sorted by increasing scheduled send time. Messages pending approval, including those created by and/or actionable by the given user, will also be returned via this API. Messages returned can be filtered by social profile or the current state of the message. If more than 50 results are returned a cursor will be automatically created to paginate the results. Query Parameters must be [URL encoded](https://en.wikipedia.org/wiki/Percent-encoding). For example: ``` ?startTime=2020-01-01T00%3A00%3A00Z &endTime=2020-01-15T17%3A55%3A01Z &socialProfileIds=1234 &state=SCHEDULED &limit=5 ``` To specify multiple social profiles, use the following [syntax](http://stackoverflow.com/questions/6243051/how-to-pass-an-array-within-a-query-string): ``` ?socialProfileIds=1234&socialProfileIds=5678 ```
* **List SCIM Groups** `listScimGroups`: Get Groups. Retrieves Hootsuite teams using the SCIM 2.0 protocol. Support equals filtering on displayName.
* **List SCIM Resource Types** `listScimResourceTypes`: Get Resource Types. Retrieves the configuration for all supported SCIM resource types
* **List SCIM Users** `listScimUsers`: Get Users. Retrieves Hootsuite users using the SCIM 2.0 protocol. Support equals filtering on username.
* **List Social Profile Teams** `listSocialProfileTeams`: Retrieve social profile's teams. Retrieves a list of team IDs with access to a social profile. Requires BASIC_USAGE permission on the social profile or ORG_MANAGE_SOCIAL_PROFILE permission on the organization that owns the social profile.
* **List Social Profiles** `listSocialProfiles`: Retrieve social profiles. Retrieves the social profiles that the authenticated user has access to.
* **List Team Members** `listTeamMembers`: Retrieve team members. Retrieves the members in a team.
* **List Team Social Profiles** `listTeamSocialProfiles`: Retrieve org team’s social profiles. Retrieves the organization's social profiles that an organization team can access.
* **Modify SCIM Group** `modifyScimGroup`: Modify Group. Modify one or more attributes of a Hootsuite team. For a complete example request, see the [SCIM specification](https://tools.ietf.org/html/rfc7644#section-3.5.2).
* **Modify SCIM User** `modifyScimUser`: Modify User. Modify one or more attributes of a Hootsuite user. For a complete example request, see the [SCIM specification](https://tools.ietf.org/html/rfc7644#section-3.5.2).
* **Reject Comment** `rejectComment`: Reject comment. Reject a comment.
* **Reject Message** `rejectMessage`: Reject message. Reject a message.
* **Remove Member From Organization** `removeMemberFromOrganization`: Remove member from organization. Removes a member from an organization.
* **Replace SCIM Group** `replaceScimGroup`: Replace Group. Updates a Hootsuite team using the SCIM 2.0 protocol. For a complete example request, see the [SCIM specification](https://tools.ietf.org/html/rfc7644#section-3.5.1)
* **Replace SCIM User** `replaceScimUser`: Replace User. Updates a Hootsuite user using the SCIM 2.0 protocol. To see the JSON object attributes required by the PUT endpoint, call the /Schemas endpoint. For a complete example request, see the [SCIM specification](https://tools.ietf.org/html/rfc7644#section-3.5.1)
* **Retrieve Authenticated Member** `retrieveMe`: Retrieve authenticated member. Retrieves authenticated member.
* **Retrieve Comment** `retrieveComment`: Retrieve comment. Retrieves a comment if it's been through the approvals workflow.
* **Retrieve Media Upload Status** `retrieveMediaStatus`: Retrieve media upload status. Retrieves the status of a media upload to Hootsuite.
* **Retrieve Member** `retrieveMember`: Retrieve member. Retrieves a member
* **Retrieve Message** `retrieveMessage`: Retrieve message. Retrieves a message. A message is always associated with a single social profile. Messages might be unavailable for a brief time during upload to social networks.
* **Retrieve Message Review History** `retrieveMessageHistory`: Get message review history. Gets a message's prescreening review history.
* **Retrieve Organization Member Permissions** `retrieveOrganizationMemberPermissions`: Retrieve org member's organization permissions. Retrieves an organization member’s permissions for the organization.
* **Retrieve Organization Member Social Profile Permissions** `retrieveOrganizationMemberSocialProfilePermissions`: Retrieve org member’s social profile permissions. Retrieves an organization member’s permissions for a social profile.
* **Retrieve SCIM Group** `retrieveScimGroup`: Get Group. Retrieves a Hootsuite team using the SCIM 2.0 protocol.
* **Retrieve SCIM User** `retrieveScimUser`: Get User. Retrieves a Hootsuite user using the SCIM 2.0 protocol.
* **Retrieve Social Profile** `retrieveSocialProfile`: Retrieve social profile. Retrieve a social profile. Requires BASIC_USAGE permission on the social profile.
* **Retrieve Team** `retrieveTeam`: Retrieve team. Retrieves a team with a given team ID.
* **Retrieve Team Member Permissions** `retrieveTeamMemberPermissions`: Retrieve team member's permissions. Retrieves team member's team permissions.
* **Schedule Message** `scheduleMessage`: Schedule messages. Schedules a message to send on one or more social profiles (except Pinterest). Returns an array of uniquely identifiable messages (one per social profile requested).&lt;br/&gt;&lt;br/&gt;Scheduling a message to Pinterest can not be bundled with any other social profiles.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| App Installed Or Uninstalled | `com.hootsuite.apps.event.v1` | Fires when a member or organization installs or uninstalls the Hootsuite app this connector authenticates as. Delivery requires the callback URL to be set on the app in the Hootsuite dashboard under My Apps &gt; (your app) &gt; Webhooks. This event carries no seq_no. |
| Comment State Changed | `com.hootsuite.comments.event.v1` | Fires whenever a comment moving through the Hootsuite approvals workflow changes state. Hootsuite has no webhook-subscription REST API: the customer must set the callback URL on the app in the Hootsuite dashboard under My Apps &gt; (your app) &gt; Webhooks. Use seq_no to de-duplicate redeliveries. |
| Message State Changed | `com.hootsuite.messages.event.v1` | Fires whenever a scheduled message changes publishing state (for example SCHEDULED to SENT, or to SEND_FAILED_PERMANENTLY). Hootsuite has no webhook-subscription REST API, so delivery must be enabled by the customer in one of two ways: (1) per message, by passing this trigger's URL in the webhookUrls array when calling the Schedule Message action; or (2) for all events of the installed app, by setting the callback URL on the app in the Hootsuite dashboard under My Apps &gt; (your app) &gt; Webhooks. Use seq_no to de-duplicate redeliveries. Endpoints must answer within 10 seconds with a 2xx and a body of 32KB or less. |
| Ping | `com.hootsuite.ping.event.v1` | A connectivity test event Hootsuite sends to confirm a callback URL is reachable and responding. It carries an empty data object and no seq_no. Use it to verify the callback URL configured on the app in the Hootsuite dashboard under My Apps &gt; (your app) &gt; Webhooks before relying on the other events. |
