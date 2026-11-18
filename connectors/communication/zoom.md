---
description: "Zoom Meetings, Webinars, Cloud Recordings, Phone, Chat, Users, Groups, Roles, Reports and Tracking Fields via the Zoom REST API v2."
hidden: true
---

# Zoom

<img src="../../.gitbook/assets/connectors/zoom.png" alt="Zoom logo" width="64">

Zoom Meetings, Webinars, Cloud Recordings, Phone, Chat, Users, Groups, Roles, Reports and Tracking Fields via the Zoom REST API v2. OAuth 2.0 authorization-code auth.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [zoom.us](https://zoom.us) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `zoom` |

## Use it

Add Zoom from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zoom.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Group Members | `addGroupMembers` | Add members to a group. |
| Add Meeting Registrant | `addMeetingRegistrant` | Register a participant for a meeting. |
| Add Role Members | `addRoleMembers` | Assign members to a role. |
| Add Webinar Panelists | `addWebinarPanelists` | Add panelists to a webinar. |
| Add Webinar Registrant | `addWebinarRegistrant` | Register a participant for a webinar. |
| Create Chat Channel | `createChatChannel` | Create a chat channel for a user. |
| Create Group | `createGroup` | Create a group on the account. |
| Create Meeting | `createMeeting` | Create/schedule a meeting for a user. |
| Create Meeting Poll | `createMeetingPoll` | Create a poll for a meeting. |
| Create Role | `createRole` | Create a role on the account. |

<details>

<summary>See 79 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Tracking Field | `createTrackingField` | Create a tracking field. |
| Create User | `createUser` | Create (add) a user on the account. action: create, autoCreate, custCreate, or ssoCreate. |
| Create Webinar | `createWebinar` | Schedule a webinar for a user. |
| Delete Chat Channel | `deleteChatChannel` | Delete a chat channel. |
| Delete Chat Message | `deleteChatMessage` | Delete a chat message. |
| Delete Group | `deleteGroup` | Delete a group. |
| Delete Group Member | `deleteGroupMember` | Remove a member from a group. |
| Delete Meeting | `deleteMeeting` | Delete a meeting. |
| Delete Meeting Poll | `deleteMeetingPoll` | Delete a meeting poll. |
| Delete Meeting Recordings | `deleteMeetingRecordings` | Delete all recordings of a meeting (trash or permanent). |
| Delete Meeting Registrant | `deleteMeetingRegistrant` | Delete a meeting registrant. |
| Delete One Recording File | `deleteRecordingFile` | Delete a single recording file from a meeting. |
| Delete Role | `deleteRole` | Delete a role. |
| Delete Role Member | `deleteRoleMember` | Unassign a member from a role. |
| Delete Tracking Field | `deleteTrackingField` | Delete a tracking field. |
| Delete User | `deleteUser` | Delete or disassociate a user from the account. |
| Delete Webinar | `deleteWebinar` | Delete a webinar. |
| Get Chat Channel | `getChatChannel` | Get information about a chat channel. |
| Get Group | `getGroup` | Get a group's details. |
| Get Meeting | `getMeeting` | Get the details of a meeting by meetingId. |
| Get Meeting Invitation | `getMeetingInvitation` | Retrieve the invitation note for a meeting. |
| Get Meeting Live Stream Details | `getMeetingLiveStream` | Get a meeting's live stream configuration. |
| Get Meeting Poll | `getMeetingPoll` | Get a meeting poll by pollId. |
| Get Meeting Recording Settings | `getRecordingSettings` | Get the cloud recording settings (passcode/sharing) for a meeting. |
| Get Meeting Recordings | `getMeetingRecordings` | Get all cloud recordings of a meeting or webinar by meetingId/UUID. |
| Get Phone User | `getPhoneUser` | Get a Zoom Phone user's profile. |
| Get Role | `getRole` | Get a role's information and privileges. |
| Get Tracking Field | `getTrackingField` | Get a tracking field's details. |
| Get User | `getUser` | Get a single user's information by userId or email. |
| Get User Settings | `getUserSettings` | Retrieve a user's meeting/recording/telephony/feature settings. |
| Get Webinar | `getWebinar` | Get a webinar's details. |
| Get Webinar Q&A Report | `listWebinarQa` | Retrieve the question-and-answer report for a past webinar. The previous path /webinars/{webinarId}/qa is not a Zoom route; the Q&A data is served by the report API. |
| List Account Phone Call Logs | `listPhoneCallLogs` | Get the account's Zoom Phone call logs for a date range. |
| List Chat Channels | `listChatChannels` | List the current user's chat channels. |
| List Chat Messages | `listChatMessages` | List a user's chat messages for a given date. Zoom requires exactly one of to_contact or to_channel to be supplied; the call returns 400 "Must provide either to_contact or to_channel parameter." if both are omitted. |
| List Group Members | `listGroupMembers` | List a group's members. |
| List Groups | `listGroups` | List all groups on the account. |
| List Meeting Polls | `listMeetingPolls` | List polls of a meeting. |
| List Meeting Registrants | `listMeetingRegistrants` | List registrants of a meeting. |
| List Meetings | `listMeetings` | List a user's scheduled/upcoming/previous meetings. |
| List Phone User Call Logs | `listPhoneUserCallLogs` | Get a Zoom Phone user's call logs for a date range. |
| List Phone Users | `listPhoneUsers` | List all Zoom Phone users on the account. |
| List Role Members | `listRoleMembers` | List members assigned to a role. |
| List Roles | `listRoles` | List the account's roles. |
| List Tracking Fields | `listTrackingFields` | List all tracking fields on the account. |
| List User Recordings | `listRecordings` | List all cloud recordings for a user. |
| List Users | `listUsers` | List the account's users. Supports status, role, pagination. |
| List Webinar Panelists | `listWebinarPanelists` | List a webinar's panelists. |
| List Webinar Registrants | `listWebinarRegistrants` | List a webinar's registrants. |
| List Webinars | `listWebinars` | List a user's webinars. |
| Recover Meeting Recordings | `recoverMeetingRecordings` | Recover a meeting's recordings from trash. |
| Remove All Webinar Panelists | `removeWebinarPanelists` | Remove all panelists from a webinar. |
| Remove Webinar Panelist | `removeWebinarPanelist` | Remove a single panelist from a webinar. |
| Report: Daily Usage | `reportDaily` | Get daily usage report (new users, meetings, participants, meeting minutes) for a month. |
| Report: Meeting Participants | `reportMeetingParticipants` | Get participant report for a past meeting. |
| Report: Meetings | `reportMeetings` | Get a user's past meeting reports for a date range. |
| Report: Users | `reportUsers` | Get active/inactive host report for a date range. |
| Report: Webinar Details | `reportWebinarDetails` | Get details report for a past webinar. |
| Report: Webinar Participants | `reportWebinarParticipants` | Get participant report for a past webinar. |
| Send Chat Message | `sendChatMessage` | Send a chat message to a contact or channel. |
| Update Chat Channel | `updateChatChannel` | Rename or update a chat channel (PATCH). |
| Update Chat Message | `updateChatMessage` | Edit a chat message (PUT). |
| Update Group | `updateGroup` | Update (rename) a group (PATCH). |
| Update Meeting | `updateMeeting` | Update a meeting's details (PATCH). |
| Update Meeting Live Stream | `updateMeetingLiveStream` | Configure a meeting's live stream (PATCH). |
| Update Meeting Live Stream Status | `updateMeetingLiveStreamStatus` | Start or stop a meeting's live stream. |
| Update Meeting Poll | `updateMeetingPoll` | Update a meeting poll (PUT). |
| Update Meeting Recording Settings | `updateRecordingSettings` | Update a meeting's cloud recording settings (PATCH). |
| Update Meeting Registrant Status | `updateMeetingRegistrantStatus` | Approve, deny, or cancel meeting registrants. |
| Update Meeting Status | `updateMeetingStatus` | End a meeting or recover a deleted meeting. |
| Update Role | `updateRole` | Update a role (PATCH). |
| Update Tracking Field | `updateTrackingField` | Update a tracking field (PATCH). |
| Update User | `updateUser` | Update a user's information (PATCH). Send only the fields to change. |
| Update User Settings | `updateUserSettings` | Update a user's settings (PATCH). Provide a settings object such as schedule_meeting, in_meeting, recording, etc. |
| Update User Status | `updateUserStatus` | Activate or deactivate a user. |
| Update Webinar | `updateWebinar` | Update a webinar (PATCH). |
| Update Webinar Q&A Settings | `updateWebinarQa` | Update the question-and-answer settings of a webinar. Zoom exposes these as the settings.question_and_answer object on the webinar itself; there is no /webinars/{webinarId}/qa route. |
| Update Webinar Registrant Status | `updateWebinarRegistrantStatus` | Approve, deny, or cancel webinar registrants. |
| Update Webinar Status | `updateWebinarStatus` | End a webinar. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Chat Message Sent | `chat_message.sent` | A chat message was sent. |
| Endpoint URL Validation (CRC) | `endpoint.url_validation` | Sent by Zoom when you add/validate the event-notification endpoint URL in the Zoom App Marketplace. Respond 200 with {plainToken, encryptedToken} where encryptedToken = HMAC-SHA256(secretToken, payload.plainToken) hex-encoded. |
| Meeting Created | `meeting.created` | A meeting was scheduled. |
| Meeting Deleted | `meeting.deleted` | A meeting was deleted. |
| Meeting Ended | `meeting.ended` | A meeting has ended. |
| Meeting Participant Joined | `meeting.participant_joined` | A participant joined a meeting. |
| Meeting Participant Left | `meeting.participant_left` | A participant left a meeting. |
| Meeting Registration Created | `meeting.registration_created` | A registrant registered for a meeting. |
| Meeting Started | `meeting.started` | A meeting has started. |
| Meeting Updated | `meeting.updated` | A meeting was updated. |

<details>

<summary>See 14 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Phone Call Answered | `phone.callee_answered` | A Zoom Phone call was answered. |
| Phone Recording Completed | `phone.recording_completed` | A Zoom Phone call recording completed. |
| Recording Completed | `recording.completed` | A cloud recording finished processing and is available. |
| Recording Started | `recording.started` | Cloud recording started. |
| Recording Stopped | `recording.stopped` | Cloud recording stopped. |
| User Created | `user.created` | A user was added to the account. |
| User Deleted | `user.deleted` | A user was removed from the account. |
| User Updated | `user.updated` | A user's profile was updated. |
| Webinar Created | `webinar.created` | A webinar was scheduled. |
| Webinar Ended | `webinar.ended` | A webinar has ended. |
| Webinar Participant Joined | `webinar.participant_joined` | A participant joined a webinar. |
| Webinar Participant Left | `webinar.participant_left` | A participant left a webinar. |
| Webinar Registration Created | `webinar.registration_created` | A registrant registered for a webinar. |
| Webinar Started | `webinar.started` | A webinar has started. |

</details>
