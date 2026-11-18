---
description: "Heartbeat is a community platform for creators, coaches and course businesses."
hidden: true
---

# Heartbeat

<img src="../../.gitbook/assets/connectors/lg/heartbeat.png" alt="Heartbeat logo">

Heartbeat is a community platform for creators, coaches and course businesses. This connector covers the full Heartbeat v0 REST API: users and pending users, roles, groups and group memberships, invitations, channels, channel categories and voice channels, threads, comments and chat channel messages, direct chats and direct messages, events with attendance and recurring instances, courses, lessons, documents, videos, notification counts and webhooks.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [heartbeat.chat](https://heartbeat.chat) |
| **Authentication** | Credentials you enter |
| **Slug** | `heartbeat` |

## Use it

Add Heartbeat from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.heartbeat.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Group Members | `addGroupMembers` | Adds users to a Heartbeat group by email address, optionally removing them from sibling groups that share the same parent. |
| Add Users To Invitation | `addUsersToInvitation` | Adds email addresses to an existing Heartbeat invitation, optionally emailing each person an invitation to join the community. |
| Create Channel | `createChannel` | Creates a new channel in a Heartbeat channel category, either a posts channel or a chat channel, and optionally restricts access to named users or groups. |
| Create Channel Category | `createChannelCategory` | Creates a new channel category in the Heartbeat community for grouping channels in the sidebar. |
| Create Comment | `createComment` | Adds a comment to a Heartbeat thread, either as a direct reply to the thread or as a nested reply to an existing comment. |
| Create Direct Chat | `createDirectChat` | Opens a direct chat between two Heartbeat users and returns its chat id. If a direct chat already exists between the pair, the existing one is returned unchanged. |
| Create Event | `createEvent` | Creates a new event in the Heartbeat community. Pass HEARTBEAT as the location to host it inside Heartbeat; leave the invited users and groups empty to invite the whole community. |
| Create Group | `createGroup` | Creates a new group in the Heartbeat community, optionally nested under a parent group and seeded with members by email. |
| Create Invitation | `createInvitation` | Creates a new invitation link for the Heartbeat community. Members joining through the link receive the chosen role and are placed in the chosen groups. |
| Create Lesson | `createLesson` | Creates a new lesson inside a module of a Heartbeat course cohort, with Markdown content, a hero media block, a publish status and optional community embed cards. |
| Create Pending User | `createPendingUser` | Creates a pending user in the Heartbeat community. The person does not yet exist in the community and is converted into a full member once they complete signup. |
| Create Thread | `createThread` | Creates a new thread in a Heartbeat posts channel. The thread is visible to every member of the channel. |
| Create User | `createUser` | Creates a new user in the Heartbeat community with a role and optional group memberships, profile picture and bio. The email address must be unique within the community. |
| Create Voice Channel | `createVoiceChannel` | Creates a new voice channel in a Heartbeat channel category, optionally restricted to named users or groups. |
| Create Webhook | `createWebhook` | Registers a webhook so Heartbeat posts the chosen community action to your endpoint. Several actions accept a filter that narrows the webhook to one group, channel, course or event. |
| Delete Channel | `deleteChannel` | Deletes a channel and its threads from the Heartbeat community. |
| Delete Channel Category | `deleteChannelCategory` | Deletes a channel category from the Heartbeat community. |
| Delete Group | `deleteGroup` | Deletes a group from the Heartbeat community. Members of the group are not removed from the community. |
| Delete User | `deleteUser` | Removes a user from the Heartbeat community by email so they can no longer access it. Their threads, comments and messages are preserved, and the user can be restored with the Reactivate User action. |
| Delete Webhook | `deleteWebhook` | Removes a webhook from the Heartbeat community so it stops receiving events. |
| Find User By Email | `findUserByEmail` | Looks up a Heartbeat community user by their email address and returns the matching user records. |
| Get Document | `getDocument` | Returns a single Heartbeat document by its document id, including its full content. |
| Get Event | `getEvent` | Returns a single Heartbeat event by its event id, including its schedule and invited users and groups. |
| Get Event Attendance | `getEventAttendance` | Returns attendance data for the last ten instances of a Heartbeat event. A non-recurring event returns a single entry. |
| Get Group | `getGroup` | Returns a single Heartbeat group by its group id, including its members. |
| Get Lesson | `getLesson` | Returns a single Heartbeat course lesson by its lesson id, including its Markdown content. |
| Get Notification Count | `getNotificationCount` | Returns how many notifications are pending for a Heartbeat community member, identified by email. |
| Get Thread | `getThread` | Returns a single Heartbeat thread by its thread id, including its content, files and comments. |
| Get User | `getUser` | Returns a single Heartbeat community user by their user id. |
| List Channel Categories | `listChannelCategories` | Returns every channel category in the Heartbeat community. Categories group channels in the sidebar and are required when creating a channel. |
| List Channel Threads | `listChannelThreads` | Returns the twenty most recent threads in a Heartbeat channel, with their content, files and comments. |
| List Channels | `listChannels` | Returns every channel in the Heartbeat community, with its name, emoji and channel type. |
| List Courses | `listCourses` | Returns every course in the Heartbeat community together with its cohorts. |
| List Direct Messages | `listDirectMessages` | Returns the hundred most recent messages in a Heartbeat direct chat. Only conversations that include the API key owner are accessible. |
| List Documents | `listDocuments` | Returns the documents, also called wiki posts, in the Heartbeat community. Results are paginated with a cursor. |
| List Event Instances | `listEventInstances` | Returns every scheduled occurrence of a recurring Heartbeat event. |
| List Events | `listEvents` | Returns every event in the Heartbeat community, optionally narrowed to the events assigned to a single group. |
| List Groups | `listGroups` | Returns every group in the Heartbeat community, with its description, colour, parent group, members and archived state. |
| List Invitations | `listInvitations` | Returns every invitation link in the Heartbeat community, with its code, the role it grants and the groups it assigns. |
| List Roles | `listRoles` | Returns every role defined in the Heartbeat community, for use when creating users, pending users and invitations. |
| List Users | `listUsers` | Returns every user in the Heartbeat community, with their email, name, role, group memberships, bio and onboarding responses. |
| List Videos | `listVideos` | Returns every Heartbeat native video in the community, with its duration, aspect ratio and view count. |
| List Webhooks | `listWebhooks` | Returns every webhook registered for the Heartbeat community, with its destination URL and trigger. |
| Reactivate User | `reactivateUser` | Restores access for a user previously removed from the Heartbeat community, identified by email. |
| Remove Group Members | `removeGroupMembers` | Removes users from a Heartbeat group by email address. The users remain members of the community. |
| Send Chat Channel Message | `sendChatChannelMessage` | Posts a new message into a Heartbeat chat channel. Every member of the channel receives it. |
| Send Direct Message | `sendDirectMessage` | Sends a direct message to a Heartbeat community member. The recipient is notified in the Heartbeat app. |
| Update Channel | `updateChannel` | Updates an existing Heartbeat channel. Only the fields you supply are changed. |
| Update Channel Category | `updateChannelCategory` | Renames an existing channel category in the Heartbeat community. |
| Update Group | `updateGroup` | Updates an existing Heartbeat group. Only the fields you supply are changed. |
| Update Lesson | `updateLesson` | Updates an existing Heartbeat course lesson. Only the fields you supply are changed. |
| Update User | `updateUser` | Updates the profile of an existing Heartbeat community user, identified by email. Only the fields you supply are changed. |
| Update Voice Channel | `updateVoiceChannel` | Updates an existing Heartbeat voice channel. Only the fields you supply are changed. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Course Completed | `COURSE_COMPLETED` | A member completed a course. Supply a filter of {"courseID": "..."} to watch a single course. |
| Direct Message Sent | `DIRECT_MESSAGE` | A direct message was sent in the community. |
| Document Created | `DOCUMENT_CREATE` | A new document, also called a wiki post, was created. |
| Event Created | `EVENT_CREATE` | A new event was created in the community. |
| Event RSVP | `EVENT_RSVP` | Someone responded to an event invitation. Supply a filter of {"eventID": "..."} and optionally {"userType": "HEARTBEAT_USER"} or GUEST. |
| Invitation Link Abandoned | `ABANDONED_CART` | Someone started signing up through an invitation link and did not finish. |
| Member Mentioned | `MENTION` | A member or group was mentioned. Supply a filter of {"userSelection": [...], "channelIDs": [...]} to narrow it. |
| Thread Created | `THREAD_CREATE` | A thread was posted. Supply a filter of {"channelID": "..."} to watch a single channel, optionally with triggerOnMove. |
| User Joined | `USER_JOIN` | A new member joined the Heartbeat community. |
| User Joined Group | `GROUP_JOIN` | A member joined a group. Supply a filter of {"groupID": "..."} to watch a single group. |
| User Updated | `USER_UPDATE` | A community member updated their profile. |
