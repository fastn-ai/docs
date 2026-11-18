---
description: "Userflow builds in-app onboarding flows, checklists, surveys and resource centres without code."
---

# Userflow

Userflow builds in-app onboarding flows, checklists, surveys and resource centres without code. This connector covers the Userflow REST API: syncing users, groups and group memberships, tracking events, reading event and attribute definitions, and reading content, content versions and content sessions - plus the Personal-API-Key Accounts API for team members.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [userflow.com](https://userflow.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 23 |
| **Events** | 0 |
| **Slug** | `userflow` |

## Use it

Add Userflow from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.userflow.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Or Update Group | `createOrUpdateGroup` | Creates a Userflow group - a company or account - or updates it when one with the same id already exists. Attributes are merged, so you only need to send what changed. |
| Create Or Update User | `createOrUpdateUser` | Creates a Userflow user, or updates it when one with the same id already exists - there is no separate create and update. Attributes are merged, so you only need to send what changed. Attach the user to companies in the same call with either Groups or Memberships: Groups is the shorthand, Memberships lets the membership carry its own attributes such as a role. Sending both at once is rejected with code invalid_params. |
| Delete Group | `deleteGroup` | Permanently deletes a Userflow group - company - and its memberships. The users themselves are left intact. The call is idempotent - deleting a group that does not exist still returns deleted true. |
| Delete User | `deleteUser` | Permanently deletes a Userflow user together with their flow and checklist progress. The call is idempotent - deleting a user who does not exist still returns deleted true. |
| Get Account | `getAccount` | Retrieves a Userflow account - the workspace that owns your environments and team. This is part of the Accounts API and needs a Personal API Key (one starting with pak_); an environment-scoped key is rejected with code invalid_pak. |
| Get Content | `getContent` | Retrieves a single piece of Userflow content - a flow, checklist, launcher, resource centre, banner, NPS survey, announcement or tooltip - by its id. |
| Get Content Session | `getContentSession` | Retrieves a single Userflow content session by its id - one user's run through one flow, checklist or survey. |
| Get Content Version | `getContentVersion` | Retrieves a single saved version of a piece of Userflow content by its id, including its survey questions or checklist tasks. The content version object carries no expandable references - Userflow rejects expand=content with code invalid_expand - so no expand input is offered. |
| Get Group | `getGroup` | Retrieves a single Userflow group - company - by the id you synced it with. Optionally expand its memberships inline. |
| Get Member | `getMember` | Retrieves a single team member of a Userflow account. This is part of the Accounts API and needs a Personal API Key (one starting with pak_); an environment-scoped key is rejected with code invalid_pak. |
| Get User | `getUser` | Retrieves a single Userflow user by the id you synced them with. Optionally expand the user's groups and memberships inline. |
| List Attribute Definitions | `listAttributeDefinitions` | Lists every attribute Userflow knows about in this environment, with its data type and the scope it applies to - user, group, membership or event. Use it to discover the attribute names available for segmentation. |
| List Content | `listContent` | Lists the content built in Userflow - flows, checklists, launchers, resource centres, banners, NPS surveys, announcements and tooltips - with the ids of their draft and published versions. Filter by Type to fetch one kind. |
| List Content Sessions | `listContentSessions` | Lists content sessions - the record of a user actually seeing a flow, checklist or survey, and how far they got. Use it to check whether a specific user has already been shown a specific piece of content. |
| List Content Versions | `listContentVersions` | Lists the saved versions of one piece of Userflow content, including its steps or checklist tasks. Content ID is mandatory - Userflow rejects the call with code invalid_params if you omit it. |
| List Event Definitions | `listEventDefinitions` | Lists every event name Userflow knows about in this environment, including the built-in Userflow events and the custom ones created automatically the first time you tracked them. |
| List Groups | `listGroups` | Lists the groups - companies - synced into the Userflow environment, using cursor pagination. |
| List Members | `listMembers` | Lists the team members of a Userflow account. This is part of the Accounts API and needs a Personal API Key (one starting with pak_); an environment-scoped key is rejected with code invalid_pak. |
| List Users | `listUsers` | Lists the users synced into the Userflow environment, using cursor pagination. Follow next_page_url, or pass the last id you saw as Starting After, to walk the whole list. |
| Remove Member | `removeMember` | Removes a team member from a Userflow account, revoking their access to it. This is part of the Accounts API and needs a Personal API Key (one starting with pak_); an environment-scoped key is rejected with code invalid_pak. This cannot be undone without re-inviting the person. |
| Remove User From Group | `removeUserFromGroup` | Removes a single user from a single Userflow group, leaving both the user and the group intact. The call is idempotent - it succeeds even if the user was not a member. Memberships are created through Create Or Update User, not through this resource. |
| Track Event | `trackEvent` | Records an event a user or company performed, so Userflow can target flows and checklists on it. At least one of User ID and Group ID is required. Userflow creates the matching event definition automatically the first time it sees a new event name. |
| Update Member | `updateMember` | Changes a team member's role or permissions on a Userflow account. This is part of the Accounts API and needs a Personal API Key (one starting with pak_); an environment-scoped key is rejected with code invalid_pak. Changing a role alters what that person can do in Userflow, so check the member before you write. |
