---
description: "Zulip is an open-source team chat application organised by topic."
---

# Zulip

Zulip is an open-source team chat application organised by topic. This connector covers the Zulip REST API: messages (send, fetch, edit, delete, react, flag, schedule, remind, render, read receipts), channels and their subscriptions, topics and topic preferences, users, bots, user groups and their members and subgroups, drafts and saved snippets, invitations, real-time event queues, presence and status, attachments, navigation views, channel folders, and organization settings including custom emoji, linkifiers, code playgrounds, allowed domains, custom profile fields and data exports. Works with both Zulip Cloud and self-hosted servers; authentication is HTTP Basic with your email address as the username and your Zulip API key as the password.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [zulip.com](https://zulip.com) |
| **Authentication** | Basic auth |
| **Actions** | 159 |
| **Events** | 0 |
| **Slug** | `zulip` |

## Use it

Add Zulip from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zulip.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Alert Words | `addAlertWords` | Adds words or phrases to the acting user's alert words. Zulip then notifies them whenever one appears in a message. Returns the user's complete alert word list after the addition. |
| Add Allowed Domain | `addRealmDomain` | Adds an email domain to the list of domains allowed to join the organization. |
| Add APNs Device Token | `addApnsToken` | Registers an Apple APNs device token so the device receives push notifications. Deprecated since Zulip 11.0 (feature level 406) in favour of Register E2EE Push Device. |
| Add Code Playground | `addCodePlayground` | Adds a code playground, which puts a "view in playground" link on code blocks written in a given language. Returns the new playground's ID. |
| Add Default Channel | `addDefaultStream` | Marks a channel as a default channel, so new users in the organization are subscribed to it automatically when they join. |
| Add FCM Registration Token | `addFcmToken` | Registers an Android FCM token so the device receives push notifications. Deprecated since Zulip 11.0 (feature level 406) in favour of Register E2EE Push Device. |
| Add Linkifier | `addLinkifier` | Creates a linkifier, a rule that turns text matching a regular expression into a link built from a URL template. Returns the new linkifier's ID. |
| Add Navigation View | `addNavigationView` | Adds a left-sidebar navigation view for the acting user. Use it either to add a custom view pointing at any Zulip narrow, or to record a preference for one of the built-in views. Built-in views cannot be given a custom name. |
| Add Reaction | `addReaction` | Adds an emoji reaction to a message on behalf of the current user. For standard Unicode emoji, supplying just the emoji name is enough; Zulip fills in the code and reaction type. |
| Archive Channel | `archiveChannel` | Archives a channel, removing it from the active channel list while preserving its message history. Archived channels can be unarchived with Update Channel by setting Is Archived to false. |
| Bulk Update Subscription Settings | `updateSubscriptionSettings` | Changes several personal subscription settings across several channels in one request. |
| Check If Messages Match Narrow | `checkMessagesMatchNarrow` | Checks which of the given messages match a narrow, and returns search-highlighted versions of the matching ones. Clients use it to decide whether a newly arrived message belongs in the view they are showing. |
| Check Thumbnail Status | `checkThumbnailStatus` | Reports whether Zulip has finished generating thumbnails for an uploaded image. Clients poll this after uploading to know when the thumbnail is ready. Split the attachment's path_id the same way as for Get File Temporary URL. |
| Create BigBlueButton Video Call | `createBigBlueButtonVideoCall` | Creates a BigBlueButton meeting and returns the join link to paste into a message. Requires the organization's video call provider to be configured as BigBlueButton. |
| Create Channel | `createChannel` | Creates a new channel and optionally subscribes users to it. The permission group settings each take a JSON-encoded value: either a user group ID, or an object such as {"direct_members":[9],"direct_subgroups":[4]}. |
| Create Channel Folder | `createChannelFolder` | Creates a channel folder, a named grouping that channels can be filed under in the left sidebar. Returns the new folder's ID. |
| Create Constructor Groups Video Call | `createConstructorGroupsVideoCall` | Creates a Constructor Groups room and returns its link. Requires the organization's video call provider to be configured as Constructor Groups. |
| Create Custom Profile Field | `createCustomProfileField` | Adds a custom profile field to the organization. Returns the new field's ID. |
| Create Data Export | `exportRealm` | Starts preparing a downloadable archive of the organization's data. Exports are rate limited by Zulip and take time to build, so poll Get Data Exports until the entry stops being pending. |
| Create Drafts | `createDrafts` | Creates one or more message drafts for the acting user. Zulip synchronises them to the user's other devices. Returns the IDs assigned to the new drafts, in the order submitted. |
| Create Invitation Link | `createInviteLink` | Creates a reusable invitation link that anyone can use to join the organization. Returns the shareable URL. No email is sent. |
| Create Message Reminder | `createMessageReminder` | Schedules a reminder that Zulip will send to the acting user at a chosen time, linking back to a specific message. The reminder goes only to the user who created it, never to anyone else. |
| Create Nextcloud Talk Video Call | `createNextcloudTalkVideoCall` | Creates a Nextcloud Talk conversation and returns its call link. Requires the organization's video call provider to be configured as Nextcloud Talk. |
| Create Saved Snippet | `createSavedSnippet` | Creates a reusable saved snippet for the acting user, which they can then insert into any message from the compose box. |
| Create Scheduled Message | `createScheduledMessage` | Schedules a message to be sent at a future time. Addressing works exactly as for Send Message: for a channel message set Type to 'channel' with the channel ID or name in To and a Topic; for a direct message set Type to 'direct' with a JSON array of recipient user IDs in To. |
| Create User | `createUser` | Creates a new user account in the organization directly, without sending an invitation. The caller must be an organization administrator. Returns the new user's ID. |
| Create User Group | `createUserGroup` | Creates a user group with an initial membership. Each permission setting takes a group-setting value: either a user group ID, or a JSON object such as {"direct_members":[9],"direct_subgroups":[4]}. |
| Create Webex Video Call | `createWebexVideoCall` | Creates a Webex meeting and returns its join link. Requires the organization's video call provider to be configured as Webex. |
| Deactivate Custom Emoji | `deactivateCustomEmoji` | Deactivates a custom emoji by name so it can no longer be used in new messages and reactions. Existing uses are preserved. |
| Deactivate Organization | `deactivateRealm` | Deactivates the entire Zulip organization. Every user is logged out immediately and nobody can sign in again. Reactivation is only possible through a server management command, and is impossible once the data has been purged. This is the most destructive call in the API. |
| Deactivate User | `deactivateUser` | Deactivates another user's account, logging them out and preventing them from signing in again. The account and its message history are preserved and can be restored with Reactivate User. Optional actions can also delete the user's bots or transfer them. |
| Deactivate User Group | `deactivateUserGroup` | Deactivates a user group, which is Zulip's equivalent of deleting it. The group can be brought back with Update User Group by setting Deactivated to false. |
| Deactivate Your Own Account | `deactivateOwnUser` | Deactivates the acting user's own account, logging them out and preventing them from signing in again. Destructive: an organization administrator must reactivate the account afterwards, and the last owner of an organization cannot deactivate themselves. |
| Delete Attachment | `removeAttachment` | Permanently deletes an uploaded file by its attachment ID. Files that are linked from at least one message are deleted automatically when the last such message is deleted, and files never used in a message are cleaned up after a few weeks, so this is mainly for removing an upload immediately. |
| Delete Custom Profile Field | `deleteCustomProfileField` | Removes a custom profile field from the organization along with every user's value for it. |
| Delete Data Export | `deleteRealmExport` | Deletes a prepared export archive so its download link stops working. The export's record remains, with a deletion timestamp. |
| Delete Draft | `deleteDraft` | Deletes one of the acting user's drafts. The removal is synchronised to their other devices. |
| Delete Event Queue | `deleteQueue` | Releases a registered event queue. Clients should call this when they stop polling so the server can free the queue rather than waiting for it to be garbage collected. |
| Delete Message | `deleteMessage` | Permanently deletes a message. This cannot be undone. The acting user must be able to access the message's content, and the organization's message deletion permissions apply. |
| Delete Reminder | `deleteReminder` | Cancels a previously scheduled reminder so it is never delivered. |
| Delete Saved Snippet | `deleteSavedSnippet` | Permanently deletes one of the acting user's saved snippets. |
| Delete Scheduled Message | `deleteScheduledMessage` | Cancels a scheduled message so it is never sent. |
| Delete Topic | `deleteTopic` | Permanently deletes every message in a topic, which removes the topic itself since topics are a property of messages. Zulip deletes in batches, so a success response with Complete set to false means the request timed out partway and should be repeated. |
| Delete Your Profile Picture | `deleteAvatar` | Removes the acting user's uploaded avatar, so Zulip falls back to the organization's default avatar scheme such as Gravatar or generated initials. |
| Edit Draft | `editDraft` | Replaces an existing draft with a new version. The whole draft object is replaced, so include every field you want the draft to keep, not only the ones you are changing. |
| Edit Message | `updateMessage` | Edits a message's content, its topic, or the channel it lives in. Moving a message between topics or channels uses Propagate Mode to decide whether just this message, this and later messages, or the whole topic moves. Resolve a topic by setting Topic to the original name prefixed with a check mark and Propagate Mode to change_all. |
| Edit Navigation View | `editNavigationView` | Updates a navigation view's name or whether it is pinned. Built-in views cannot be given a custom name. |
| Edit Saved Snippet | `editSavedSnippet` | Updates the title or body of one of the acting user's saved snippets. Only the fields you supply are changed. |
| Edit Scheduled Message | `updateScheduledMessage` | Edits a message that is still waiting to be sent: its content, recipients, topic or delivery time. Only the fields you supply are changed. |
| Fetch API Key | `fetchApiKey` | Exchanges a username and password for that user's Zulip API key. Used by clients implementing a login screen. The response contains a credential, so handle it as a secret and never log it. |
| Fetch API Key With JWT | `jwtFetchApiKey` | Exchanges a JSON Web Token for the target user's Zulip API key, for organizations that have JWT authentication configured. The response contains a credential, so handle it as a secret and never log it. |
| Get A User's Subscribed Channels | `getUserChannels` | Returns the IDs of the channels another user is subscribed to. The caller must be an organization administrator, and only channels the caller can see are included. |
| Get Alert Words | `getAlertWords` | Fetches every alert word the acting user has configured. Zulip notifies the user whenever one of these words or phrases appears in a message they can see, the same way an @-mention would. |
| Get All Channels | `getStreams` | Lists every channel the acting user has access to, with each channel's ID, name, description, privacy settings and permission groups. The include flags widen or narrow which categories of channel are returned. |
| Get Allowed Domains | `getRealmDomains` | Lists the email domains that are allowed to join the organization, and whether each one also permits subdomains. |
| Get Attachments | `getAttachments` | Lists metadata for every file the acting user has uploaded, including each file's size, upload time and which messages currently link to it. Also reports the total storage the user is using. |
| Get Bot API Key | `getBotApiKey` | Returns a bot user's API key. Only the bot's owner and organization administrators may read it. Treat the returned key as a secret. |
| Get Bot Storage | `getBotStorage` | Retrieves the key-value data an interactive bot has stored on the Zulip server. This endpoint is only available to bot user accounts; a human account receives a permission error. |
| Get Channel By ID | `getStreamById` | Fetches the full configuration of a single channel by its ID, including its description, privacy and history settings, folder, retention policy and permission groups. |
| Get Channel Email Address | `getStreamEmailAddress` | Returns the special email address that forwards incoming email into a channel as Zulip messages. Only users with permission to post in the channel can read it. |
| Get Channel Folders | `getChannelFolders` | Lists the organization's channel folders, the groupings used to organize channels in the left sidebar, sorted by their display order. |
| Get Channel ID | `getStreamId` | Looks up a channel's numeric ID from its name. Useful when you only know the channel name but need the ID that the other channel actions take. |
| Get Channel Subscribers | `getSubscribers` | Returns the user IDs of everyone subscribed to a channel. |
| Get Custom Emoji | `getCustomEmoji` | Lists the organization's custom emoji, keyed by emoji ID, including deactivated ones. |
| Get Custom Profile Fields | `getCustomProfileFields` | Lists the organization's custom profile fields in display order, with each field's type, hint and configuration. |
| Get Data Export Consent State | `getRealmExportConsents` | Reports which users have consented to having their private data included in a full-with-consent export. |
| Get Data Exports | `getRealmExports` | Lists the organization's data exports, including who requested each one, whether it is still being prepared, and the download URL once it is ready. |
| Get Drafts | `getDrafts` | Fetches all of the acting user's unsent message drafts, which Zulip synchronises across their devices. |
| Get Events From Event Queue | `getEvents` | Long-polls a registered event queue for new events. Pass the highest event ID you have already processed as Last Event ID to acknowledge it; the server then returns only newer events. Set Dont Block to true for a non-blocking poll, otherwise the request waits until an event arrives or the server's long-poll timeout expires. A BAD_EVENT_QUEUE_ID error means the queue was garbage collected and the client must register a new one. |
| Get File Temporary URL | `getFileTemporaryUrl` | Returns a short-lived URL that grants access to an uploaded file without authentication, typically valid for about 60 seconds. Request it immediately before use and never store it. Split the attachment's path_id: the part before the first slash is the Realm ID and everything after it is the Filename. |
| Get Invitations | `getInvites` | Lists the organization's pending invitations, both single-use email invitations and reusable invitation links. |
| Get Linkifiers | `getLinkifiers` | Lists the organization's linkifiers, the pattern-to-URL rules that turn things like issue references into links in message text, in the order they are applied. |
| Get Message | `getMessage` | Fetches a single message by its ID. The response includes a raw_content field with the original Zulip-flavoured Markdown, which is useful for prefilling an edit box or showing the message source. |
| Get Message Edit History | `getMessageHistory` | Returns a message's edit history, oldest first. The first entry is the original message; each later entry records what changed, including the previous content and topic and an HTML diff. |
| Get Message Read Receipts | `getReadReceipts` | Returns the user IDs of everyone who has read a message. Users who have turned read receipts off for themselves are never listed, and the organization can disable the feature entirely. |
| Get Messages | `getMessages` | Fetches messages, optionally filtered by a narrow. This is the primary way to read message history. Anchor the fetch on a message ID or one of the special anchors, then ask for a number of messages before and after it. Supply Narrow as a JSON-encoded array of filter objects, for example [{"operator":"channel","operand":9}]. |
| Get Navigation Views | `getNavigationViews` | Fetches the acting user's configured left-sidebar navigation views, both the built-in ones they have customized and any custom views they have added. |
| Get Own User | `getOwnUser` | Retrieves the profile of the Zulip user the API key belongs to, including their user ID, email, full name, role, time zone and whether the account is an administrator, owner, guest or bot. |
| Get Presence Of All Users | `getPresence` | Returns presence information for every user in the organization, showing whether each was recently active or idle and when their presence was last updated. |
| Get Reminders | `getReminders` | Fetches all of the acting user's pending message reminders. A reminder is a message Zulip will send to the user at a future time, linking back to the message they wanted to be reminded about. |
| Get Saved Snippets | `getSavedSnippets` | Fetches all of the acting user's saved snippets, the reusable blocks of message text they can insert into any message. |
| Get Scheduled Messages | `getScheduledMessages` | Fetches every message the acting user has scheduled to be sent later. These are not yet delivered and can still be edited or cancelled. |
| Get Server Settings | `getServerSettings` | Fetches a Zulip server's global settings: its version and feature level, which authentication methods are enabled, and the organization's name, icon and login presentation. This endpoint requires no authentication, so it is also how a client checks whether a URL is a Zulip server before prompting for credentials. |
| Get Subscribed Channels | `getSubscriptions` | Lists the channels the acting user is subscribed to, with their personal subscription settings such as colour, pinning, muting and notification preferences. |
| Get Subscription Status | `getSubscriptionStatus` | Reports whether a given user is subscribed to a given channel. |
| Get Topics In Channel | `getStreamTopics` | Lists the topics the acting user can see in a channel, most recently active first, each with the ID of its newest message. |
| Get User | `getUser` | Fetches a single user's profile by their user ID. |
| Get User By Email | `getUserByEmail` | Fetches a single user's profile by email address. Both the user's real delivery email and their Zulip API email are accepted. |
| Get User Group Members | `getUserGroupMembers` | Returns the user IDs belonging to a user group, either only its direct members or everyone reachable through its subgroups too. |
| Get User Group Membership Status | `getIsUserGroupMember` | Reports whether a particular user belongs to a user group, optionally counting only direct membership. |
| Get User Group Subgroups | `getUserGroupSubgroups` | Returns the IDs of a user group's subgroups, either only its direct subgroups or the whole nested set. |
| Get User Groups | `getUserGroups` | Lists the organization's user groups, including Zulip's built-in system groups such as role:owners and role:members, with each group's members, subgroups and permission settings. |
| Get User Presence | `getUserPresence` | Returns one user's presence: whether they are active, idle or offline, and when that was last updated. The user can be identified by user ID or by Zulip API email. |
| Get User Status | `getUserStatus` | Fetches a user's status message and status emoji. The returned status object is empty if the user has no status set. |
| Get Users | `getUsers` | Lists the users in the organization that the acting user can see, including bots and deactivated accounts. User IDs can be supplied to fetch only specific users. |
| Mark All Messages As Read | `markAllAsRead` | Marks every message the acting user can see as read. Zulip works in batches, so a success with Complete set to false means the request timed out partway and should be repeated. |
| Mark Channel As Read | `markStreamAsRead` | Marks every message in one channel as read for the acting user. |
| Mark Topic As Read | `markTopicAsRead` | Marks every message in one topic as read for the acting user. |
| Mute Or Unmute Topic (Legacy) | `muteTopic` | Mutes or unmutes a topic for the acting user. Deprecated since Zulip 7.0 (feature level 170) in favour of Update Personal Topic Preference, which covers the same behaviour plus following a topic. Provide either Channel ID or Channel Name, not both. |
| Mute User | `muteUser` | Mutes another user for the acting user only. Muted users' messages are hidden and their name is replaced in the interface. The mute is personal and is not visible to the muted user. |
| Reactivate User | `reactivateUser` | Restores a previously deactivated user account so the person can sign in again. |
| Regenerate Bot API Key | `regenerateBotApiKey` | Issues a bot user a new API key and immediately invalidates the old one. Anything still using the previous key stops working. |
| Regenerate Your API Key | `regenerateApiKey` | Issues the acting user a new API key and immediately invalidates the old one. Every integration still using the previous key stops working, including this connector's own stored credential, so treat it as a destructive operation and update the connection with the returned key straight away. |
| Register Client Device | `registerClientDevice` | Registers the calling client as a device for the acting user and returns a device ID, which the mobile push endpoints then use to identify it. |
| Register E2EE Push Device | `registerPushDevice` | Registers a device for end-to-end-encrypted push notifications. The client generates an encryption key and sends an encrypted registration payload, so the push bouncer never sees the notification contents. This is the modern replacement for the FCM and APNs token endpoints. |
| Register E2EE Push Device To Bouncer | `registerRemotePushDevice` | Forwards an end-to-end-encrypted push registration on to Zulip's push notification bouncer. A self-hosted Zulip server calls this against the bouncer; it is not normally called by ordinary clients. |
| Register Event Queue | `registerQueue` | Allocates a long-poll event queue and returns a snapshot of the initial state the client asked for. This is the first step of Zulip's real-time protocol: register a queue here, then repeatedly call Get Events with the returned Queue ID, and call Delete Event Queue when finished. Zulip has no outbound webhook subscription API, so this queue is the only way to receive Zulip events. |
| Remove Alert Words | `removeAlertWords` | Removes words or phrases from the acting user's alert words. Matching is case insensitive. Returns the user's complete alert word list after the removal. |
| Remove Allowed Domain | `deleteRealmDomain` | Removes an email domain from the organization's allowed-domains list. |
| Remove APNs Device Token | `removeApnsToken` | Unregisters an Apple APNs device token so the device stops receiving push notifications. |
| Remove Bot Storage | `removeBotStorage` | Deletes keys from an interactive bot's server-side storage, or wipes the storage entirely when no keys are given. This endpoint is only available to bot user accounts. |
| Remove Client Device | `removeClientDevice` | Removes a previously registered client device, for example when the user signs out of that client. |
| Remove Code Playground | `removeCodePlayground` | Deletes a code playground so its link no longer appears on code blocks. |
| Remove Default Channel | `removeDefaultStream` | Stops a channel being a default channel, so new users are no longer subscribed to it automatically. Existing subscriptions are untouched. |
| Remove FCM Registration Token | `removeFcmToken` | Unregisters an Android FCM token so the device stops receiving push notifications. |
| Remove Linkifier | `removeLinkifier` | Deletes a linkifier so its pattern no longer produces links in message text. |
| Remove Navigation View | `removeNavigationView` | Removes one of the acting user's navigation views. |
| Remove Reaction | `removeReaction` | Removes the current user's emoji reaction from a message. Identify the reaction the same way it was added, normally by emoji name alone for standard Unicode emoji. |
| Remove Your Profile Data | `removeProfileData` | Clears the acting user's values for the given custom profile fields. |
| Render Message | `renderMessage` | Renders Zulip-flavoured Markdown to the HTML that Zulip would display, without sending anything. Useful for previewing message content before sending it. |
| Reorder Channel Folders | `reorderChannelFolders` | Sets the order in which channel folders appear in the sidebar. The list must contain every channel folder in the organization, archived ones included, or Zulip rejects it as an invalid order mapping. |
| Reorder Custom Profile Fields | `reorderCustomProfileFields` | Sets the display order of the organization's custom profile fields. The list must contain every field defined in the organization. |
| Reorder Linkifiers | `reorderLinkifiers` | Sets the order in which linkifiers are applied to message text. The list must contain every linkifier in the organization. |
| Report Message | `reportMessage` | Reports a message to the organization's moderators. Requires the organization to have a moderation request channel configured. |
| Resend Email Invitation | `resendEmailInvite` | Sends a pending email invitation again to the same address. |
| Revoke Email Invitation | `revokeEmailInvite` | Revokes a pending single-use email invitation so the link in that email stops working. |
| Revoke Invitation Link | `revokeInviteLink` | Revokes a reusable invitation link so it can no longer be used to join the organization. |
| Send E2EE Test Push Notification | `e2eeTestNotify` | Sends an end-to-end-encrypted test push notification to the acting user's registered devices. Without Device ID every E2EE-registered device is notified. |
| Send Invitations | `sendInvites` | Emails invitations to join the organization. Each invitee is subscribed to the given channels once they accept. This sends real email to every address supplied. |
| Send Message | `sendMessage` | Sends a channel message or a direct message. For a channel message set Type to 'channel' (or the legacy alias 'stream'), put the channel ID or name in To and supply a Topic. For a direct message set Type to 'direct' and put a JSON array of recipient user IDs in To, for example [9, 10]; Topic is ignored. Returns the ID of the new message. |
| Send Test Push Notification | `testNotify` | Sends a test push notification to the acting user's mobile devices, so they can confirm notifications are working. Without Token every registered device is notified. |
| Set Typing Status | `setTypingStatus` | Tells other users that the acting user has started or stopped composing a message. Clients send 'start' when composing begins, repeat it every few seconds while the user is still active, and send 'stop' when the message is sent or the compose box is closed. |
| Set Typing Status For Message Edit | `setTypingStatusForMessageEdit` | Tells other users that the acting user has started or stopped editing an existing message, so clients can show an editing indicator on that message. |
| Subscribe To Channel | `subscribe` | Subscribes users to one or more channels. If a named channel does not exist, this endpoint creates it, and the creation parameters below then apply. Without Principals it subscribes the acting user; with Principals it subscribes the users listed, which requires permission to add subscribers. |
| Test Welcome Bot Custom Message | `testWelcomeBotCustomMessage` | Sends the acting user a preview of the custom welcome message that Welcome Bot would send to new members, so an administrator can check the wording before saving it. The preview goes only to the caller. |
| Unmute User | `unmuteUser` | Removes a personal mute the acting user had placed on another user. |
| Unsubscribe From Channel | `unsubscribe` | Unsubscribes the acting user, or the users named in Principals, from the given channels. Removing other people requires permission to remove subscribers. |
| Update Allowed Domain | `patchRealmDomain` | Changes whether an already-allowed email domain also permits subdomains. |
| Update Another User's Status | `updateStatusForUser` | Sets or clears another user's status message and status emoji. The caller must have permission to administer that user. |
| Update Bot Storage | `updateBotStorage` | Adds or updates key-value data in an interactive bot's server-side storage. Existing keys are overwritten, other keys are left alone. This endpoint is only available to bot user accounts. |
| Update Channel | `updateStream` | Updates a channel's configuration: its name, description, privacy, history visibility, folder, retention policy and permission groups. Also used to unarchive a channel by setting Is Archived to false. Only the fields you supply are changed. |
| Update Channel Folder | `updateChannelFolder` | Changes a channel folder's name or description, or archives and unarchives it. Only the fields you supply are changed. |
| Update Custom Profile Field | `updateCustomProfileField` | Changes a custom profile field's label, hint or configuration. The field's type cannot be changed. Only the fields you supply are altered. |
| Update Linkifier | `updateLinkifier` | Replaces a linkifier's pattern and URL template. Both are required even if only one is changing. |
| Update Message Flags | `updateMessageFlags` | Adds or removes a personal flag such as read, starred or collapsed on a list of messages. Flags are per-user and invisible to everyone else. |
| Update Message Flags For Narrow | `updateMessageFlagsForNarrow` | Adds or removes a personal flag across a range of messages selected by a narrow rather than by listing IDs. The range is an anchor plus a number of messages before and after it; the server may shrink that range, so repeat the call using Last Processed ID until Found Newest is true. |
| Update Organization Default User Settings | `updateRealmUserSettingsDefaults` | Changes the organization-wide defaults for personal user settings, which apply to users who have not overridden the setting themselves and to new accounts. Only the fields you supply are changed. Requires organization administrator permission. |
| Update Personal Topic Preference | `updateUserTopic` | Sets the acting user's personal visibility policy for one channel-and-topic pair. This is how topics are muted, unmuted, followed or marked unmuted-within-a-muted-channel. The request succeeds whether or not any message has been sent to the topic. |
| Update Settings | `updateSettings` | Changes the acting user's own personal settings: profile details, display preferences, notification preferences and privacy options. Only the fields you supply are changed. An organization administrator may instead apply the same changes to a set of users by supplying Target Users. Changing the email address starts a confirmation flow rather than taking effect immediately, and changing the password requires the old password as well. |
| Update Subscription Setting | `updateSubscriptionProperty` | Changes one personal subscription setting for one channel, such as its colour, whether it is pinned, or its notification preferences. |
| Update Subscriptions | `updateSubscriptions` | Subscribes to and unsubscribes from channels for the acting user in a single request. |
| Update User | `updateUser` | Updates another user's name, organization role or custom profile data, identified by user ID. Changing a user's email additionally requires the caller to be an organization owner with the special permission to change user emails. |
| Update User By Email | `updateUserByEmail` | Updates a user's name, organization role or custom profile data, identified by email address rather than user ID. The same email forms are accepted as for Get User By Email. |
| Update User Group | `updateUserGroup` | Changes a user group's name, description or permission settings, and reactivates a deactivated group by passing Deactivated as false. Permission settings here take an update value, a JSON object with new_value and optionally old_value. |
| Update User Group Members | `updateUserGroupMembers` | Adds and removes members, and optionally subgroups, of a user group in a single request. |
| Update User Group Subgroups | `updateUserGroupSubgroups` | Adds and removes subgroups of a user group. Members of a subgroup count as members of the parent group. |
| Update Your Presence | `updatePresence` | Reports the acting user's presence on this client as active or idle, and in the same round trip returns the organization's current presence data. Clients call this periodically as their presence heartbeat. |
| Update Your Profile Data | `updateProfileData` | Sets values for the acting user's custom profile fields. Field IDs come from Get Custom Profile Fields. |
| Update Your Status | `updateStatus` | Sets or clears the acting user's own status message and status emoji. Sending an empty status text clears the status. |
