---
description: "Discourse is an open-source community discussion platform."
hidden: true
---

# Discourse

<img src="../../.gitbook/assets/connectors/lg/discourse.png" alt="Discourse logo">

Discourse is an open-source community discussion platform. This connector covers the Discourse REST API: topics, posts, categories, tags and tag groups, users and user preferences, groups and memberships, badges, invites, notifications, private messages, search, site settings, uploads, backups, admin user management and web hooks.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [discourse.org](https://discourse.org) |
| **Authentication** | Credentials you enter |
| **Slug** | `discourse` |

## Use it

Add Discourse from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.discourse.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Abort Multipart Upload | `abortMultipart` | Cancels a multipart upload started with Create Multipart Upload and discards any chunks already sent to external storage. Use it to clean up an upload that will not be finished. Requires the site to have external (S3) file storage with direct uploads enabled. |
| Activate User | `activateUser` | Activates a user account on the person's behalf, so they can sign in without clicking the activation link that was emailed to them. |
| Add Group Members | `addGroupMembers` | Adds one or more users to a group by username or user ID. |
| Anonymize User | `anonymizeUser` | Replaces a user's personal details with anonymous ones, keeping their posts but severing the link to the person. Use it for privacy requests where the content should stay. This cannot be undone. Returns the new anonymous username. |
| Batch Presign Multipart Parts | `batchPresignMultipartParts` | Returns a presigned upload URL for each requested chunk of a multipart upload, keyed by part number. Upload each chunk with a PUT to its URL and keep the ETag the storage provider returns, since Complete Multipart Upload needs every part number and ETag. Part numbers must be between 1 and 10000. Requires the site to have external (S3) file storage with direct uploads enabled. |
| Bookmark Topic | `bookmarkTopic` | Bookmarks a topic on behalf of the user the API key acts as. |
| Change Password | `changePassword` | Sets a new password using the one-time token from a password reset email. The token is single-use and expires, so each reset needs a fresh link. |
| Complete External Upload | `completeExternalUpload` | Finishes a direct external upload started with Generate Presigned Put. Moves the file from its temporary location to permanent external storage, verifies the size and optional checksum, and creates the Discourse upload record that is returned. Requires the site to have external (S3) file storage with direct uploads enabled. |
| Complete Multipart Upload | `completeMultipart` | Finishes a multipart upload once every chunk has been sent, assembles the file in external storage and creates the Discourse upload record that is returned. Supply every part number with the ETag the storage provider returned for it. Requires the site to have external (S3) file storage with direct uploads enabled. |
| Create Backup | `createBackup` | Starts a backup of the site. The backup runs in the background and appears in List Backups when it finishes. Requires an admin API key. |

<details>

<summary>See 90 more actions</summary>

* **Create Badge** `createBadge`: Creates a new badge. Requires an admin API key.
* **Create Category** `createCategory`: Creates a new category on the site.
* **Create Group** `createGroup`: Creates a new group. Requires an admin API key.
* **Create Invite** `createInvite`: Creates an invite to the community. Supply an email address to send an email invite, or omit it to generate a shareable invite link. Set skip_email to true to create an email invite without sending mail.
* **Create Multipart Upload** `createMultipartUpload`: Starts a multipart upload in external storage for a large file, returning the identifiers needed to upload the file in chunks. Follow with Batch Presign Multipart Parts to get a URL per chunk, then Complete Multipart Upload. Requires the site to have external (S3) file storage with direct uploads enabled.
* **Create Multiple Invites** `createMultipleInvites`: Creates several invites in one call, one per email address supplied. Every invite shares the other properties.
* **Create Tag Group** `createTagGroup`: Creates a tag group, a named set of tags that can be restricted to categories or groups. Requires an admin API key.
* **Create Topic Post Or Message** `createTopicPostPM`: Creates a new topic, a reply to an existing topic, or a private message. Supply title and raw for a new topic, topic_id and raw for a reply, or archetype private_message with target_recipients for a message.
* **Create Topic Timer** `createTopicTimer`: Schedules an action on a topic, such as closing, opening, deleting or publishing it at a future time.
* **Create Upload** `createUpload`: Uploads a file to Discourse and returns the stored upload record, including its id, URL and short URL for embedding in posts. Set "type" to describe what the file is for (composer, avatar, profile_background, card_background or custom_emoji). Note: Discourse expects the file itself as a multipart/form-data part, which a JSON request cannot carry, so this action reaches the route and authenticates but cannot deliver binary content. For programmatic uploads to an S3-backed site, use Generate Presigned Put followed by Complete External Upload instead.
* **Create User** `createUser`: Creates a new user account. By default the account is created inactive and Discourse emails the person an activation link; set "active" to true to skip activation, and "approved" to true on sites that require staff approval. Returns whether the account was created along with the new user id.
* **Create Web Hook** `createWebHook`: Creates a web hook that posts selected Discourse events to a payload URL. Requires an admin API key.
* **Deactivate User** `deactivateUser`: Deactivates a user account. The person is signed out and cannot sign in again until they reactivate by confirming their email address.
* **Delete Backup** `deleteBackup`: Permanently removes a backup file from the site, freeing the storage it used. Identify the backup by the full filename shown in List Backups, including its .sql.gz or .tar.gz extension. This cannot be undone.
* **Delete Badge** `deleteBadge`: Deletes a badge. Requires an admin API key.
* **Delete Group** `deleteGroup`: Deletes a group. Automatic groups managed by Discourse cannot be deleted. Requires an admin API key.
* **Delete Post** `deletePost`: Deletes a single post. Staff can recover a deleted post from the topic page.
* **Delete Tag Group** `deleteTagGroup`: Deletes a tag group. The tags themselves are not deleted. Requires an admin API key. This endpoint is not in the vendor OpenAPI document but is live on Discourse.
* **Delete User** `deleteUser`: Permanently deletes a user account. Optionally deletes everything they posted and blocks their email address, the URLs they posted and their IP address from being used again. Discourse refuses to delete accounts that are too old or have too many posts unless the site settings allow it.
* **Delete Web Hook** `deleteWebHook`: Deletes a web hook by ID so that Discourse stops posting events to its payload URL. Requires an admin API key.
* **Download Backup** `downloadBackup`: Downloads a backup file using the token from the backup download email. Requires an admin API key. The response is a binary archive, which the fastn executor cannot stream; use the emailed link directly for large backups.
* **Export Calendar Events As ICS** `exportEventsICS`: Exports the calendar events created with the Discourse Post Event plugin as an iCalendar document.
* **Generate Presigned Put** `generatePresignedPut`: Starts a direct external upload and returns a presigned PUT URL that the file can be sent straight to, bypassing Discourse. Upload the binary to the returned URL, then call Complete External Upload with the returned unique identifier to register the file. Requires the site to have external (S3) file storage with direct uploads enabled.
* **Get Group** `getGroup`: Returns a single group addressed by its name.
* **Get Group By ID** `getGroupById`: Returns a single group addressed by its numeric ID.
* **Get Notifications** `getNotifications`: Returns the notifications belonging to the user the API key acts as.
* **Get Post** `getPost`: Returns a single post by ID.
* **Get Posts From Topic** `getSpecificPostsFromTopic`: Returns specific posts from a topic by their post IDs.
* **Get Site Basic Info** `getSiteBasicInfo`: Returns basic public information about the Discourse site, including its title, description, locale and logo URLs.
* **Get Site Info** `getSite`: Returns the full site configuration, including every category, group, trust level, post action type and notification type the community uses.
* **Get Tag** `getTag`: Returns a single tag by name together with the topics that carry it.
* **Get Tag Group** `getTagGroup`: Returns a single tag group by ID. Requires an admin API key.
* **Get Topic** `getTopic`: Returns a single topic by ID, including its post stream and metadata.
* **Get Topic By External ID** `getTopicByExternalId`: Returns a single topic addressed by the external ID that was set on it.
* **Get User** `getUser`: Returns a single user by username, including their profile, stats and group memberships.
* **Get User As Admin** `adminGetUser`: Returns a single user by ID with the administrative fields, such as email, IP address and moderation state. Requires an admin API key.
* **Get User By External ID** `getUserExternalId`: Returns a user addressed by the single sign-on external ID associated with their account.
* **Get User By Provider External ID** `getUserIdentiyProviderExternalId`: Returns a user addressed by the external ID assigned by a named identity provider, for example google_oauth2 or github.
* **Get User Emails** `getUserEmails`: Returns the email addresses belonging to a specified user. Requires an admin API key and is recorded in the staff action logs.
* **Get Web Hook** `getWebHook`: Returns a single web hook by ID, including the event types it subscribes to. Requires an admin API key.
* **Invite Group To Topic** `inviteGroupToTopic`: Invites a whole group into a topic, typically a private message.
* **Invite User To Topic** `inviteToTopic`: Invites an existing user or an email address into a topic, typically a private message.
* **List Backups** `getBackups`: Returns the backups stored for the site. Requires an admin API key.
* **List Badges** `adminListBadges`: Returns every badge defined on the site, together with the badge types and groupings. Requires an admin API key.
* **List Calendar Events** `listEvents`: Returns the calendar events created with the Discourse Post Event plugin, optionally filtered by category, post, attendee or date range.
* **List Categories** `listCategories`: Returns the list of categories on the site, optionally including their subcategories.
* **List Category Topics** `listCategoryTopics`: Returns the topics in a specified category, addressed by the category slug and ID.
* **List Group Members** `listGroupMembers`: Returns the members and owners of a group addressed by its name.
* **List Groups** `listGroups`: Returns the groups on the site that the API user can see.
* **List Latest Topics** `listLatestTopics`: Returns the latest topics on the site, optionally ordered and paginated.
* **List Post Replies** `postReplies`: Returns the posts that reply directly to a specified post.
* **List Posts** `listPosts`: Returns the most recent posts across all topics the API user can see.
* **List Tag Groups** `listTagGroups`: Returns every tag group on the site. Requires an admin API key.
* **List Tags** `listTags`: Returns every tag on the site with its usage counts.
* **List Top Topics** `listTopTopics`: Returns the top topics on the site for a given period.
* **List User Actions** `listUserActions`: Returns a user's activity stream, filtered by action type. Common filter values are 4 for topics created, 5 for replies, 1 for likes given and 2 for likes received.
* **List User Badges** `listUserBadges`: Returns the badges granted to a specified user.
* **List User Private Messages** `listUserPrivateMessages`: Returns the private messages a specified user has received.
* **List User Sent Private Messages** `getUserSentPrivateMessages`: Returns the private messages a specified user has sent.
* **List Users As Admin** `adminListUsers`: Returns the site users with administrative fields, optionally filtered by email or IP address. Requires an admin API key.
* **List Users By Flag** `adminListUsersFlag`: Returns the site users filtered by a moderation flag such as active, new, staff, suspended, blocked or suspect. Requires an admin API key.
* **List Users Publicly** `listUsersPublic`: Returns the public user directory, ranked over a period by an activity measure such as likes received or posts created.
* **List Web Hooks** `listWebHooks`: Returns all web hooks configured on the Discourse site, together with the catalogue of event types that can be subscribed to. Requires an admin API key.
* **Lock Post** `lockPost`: Locks or unlocks a post so that it can no longer be edited by its author.
* **Log Out User** `logOutUser`: Ends every active session for a user, signing them out everywhere. The account stays enabled and they can sign in again.
* **Mark Notifications As Read** `markNotificationsAsRead`: Marks a single notification as read, or every notification when no ID is supplied.
* **Perform Post Action** `performPostAction`: Performs an action on a post, such as liking it or raising a flag. Use List Site Info to read the available post action type IDs; 2 is Like.
* **Refresh Gravatar** `refreshGravatar`: Re-fetches a user's Gravatar image so a picture they changed on gravatar.com shows up on the forum. Returns the refreshed upload id and avatar URL template.
* **Remove Group Members** `removeGroupMembers`: Removes one or more users from a group by username or user ID.
* **Remove Topic** `removeTopic`: Deletes a topic. Staff can recover a deleted topic from the topic page.
* **Search** `search`: Searches the community for a term. The query string supports Discourse search operators such as @username, #category, in:title and after:date.
* **Send Backup Download Email** `sendDownloadBackupEmail`: Emails a time limited download link for a backup to the admin the API key acts as. Requires an admin API key.
* **Send Password Reset Email** `sendPasswordResetEmail`: Emails a password reset link to the account matching the given username or email address. To avoid revealing who has an account, Discourse always reports success; the "user_found" field tells staff whether a matching account existed.
* **Set Topic Notification Level** `setNotificationLevel`: Sets the notification level that the API user has on a topic.
* **Show Category** `getCategory`: Returns a single category by ID.
* **Silence User** `silenceUser`: Silences a user until the given date. They can still read and sign in but cannot post, reply or send messages. The reason is recorded in the staff log, and the optional message is emailed to the person.
* **Suspend User** `suspendUser`: Suspends a user until the given date, blocking them from signing in. The reason is recorded in the staff log, and the optional message is emailed to the person to explain the suspension. Returns the suspension details.
* **Update Avatar** `updateAvatar`: Sets which image a user's avatar comes from. Pass the id of an existing upload together with the source type: "uploaded" for a custom picture, "gravatar" for their Gravatar, or "system" for the default letter avatar.
* **Update Badge** `updateBadge`: Updates an existing badge. The name and badge type are required by the API even when unchanged. Requires an admin API key.
* **Update Category** `updateCategory`: Updates an existing category. The name is required by the API even when it is unchanged.
* **Update Email** `updateEmail`: Starts changing a user's email address. Discourse emails a confirmation link to the new address and only applies the change once the person clicks it, so the account keeps its current email until then.
* **Update Group** `updateGroup`: Updates an existing group, for example its display name, bio, visibility or notification defaults.
* **Update Post** `updatePost`: Updates the body of a single post. Discourse requires the new body to be wrapped in a post envelope.
* **Update Tag Group** `updateTagGroup`: Updates an existing tag group. Requires an admin API key.
* **Update Topic** `updateTopic`: Updates the title or category of a topic.
* **Update Topic Status** `updateTopicStatus`: Closes, pins, archives or hides a topic by setting one of its status flags.
* **Update Topic Timestamp** `updateTopicTimestamp`: Rewrites the creation timestamp of a topic and its posts. Requires staff permissions.
* **Update User** `updateUser`: Updates a user's profile, identified by username. Use it to change the display name or the identifiers linking the account to an external authentication provider. Returns the updated user record.
* **Update Username** `updateUsername`: Renames a user. The new username must be available and meet the site's format rules; links and mentions using the old name are updated automatically. Returns the account's id and its new username.
* **Update Web Hook** `updateWebHook`: Updates an existing web hook, for example its payload URL, subscribed event types or active state. Requires an admin API key.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Accepted Solution | `accepted_solution` | A post was marked as the accepted solution of a topic. Requires the Discourse Solved plugin. |
| Category Created | `category_created` | A category was created. |
| Category Destroyed | `category_destroyed` | A category was deleted. |
| Category Updated | `category_updated` | A category was updated. |
| Chat Message Created | `chat_message_created` | A chat message was created. Requires the Discourse Chat plugin. |
| Chat Message Edited | `chat_message_edited` | A chat message was edited. Requires the Discourse Chat plugin. |
| Chat Message Restored | `chat_message_restored` | A deleted chat message was restored. Requires the Discourse Chat plugin. |
| Chat Message Trashed | `chat_message_trashed` | A chat message was deleted. Requires the Discourse Chat plugin. |
| Group Created | `group_created` | A group was created. |
| Group Destroyed | `group_destroyed` | A group was deleted. |

<details>

<summary>See 33 more events</summary>

* **Group Updated** `group_updated`: A group was updated.
* **Notification Created** `notification_created`: A notification was created for a user.
* **Post Created** `post_created`: A new post was created in a topic.
* **Post Destroyed** `post_destroyed`: A post was deleted.
* **Post Edited** `post_edited`: A post was edited.
* **Post Liked** `post_liked`: A post was liked.
* **Post Recovered** `post_recovered`: A deleted post was recovered.
* **Reviewable Created** `reviewable_created`: An item entered the review queue.
* **Reviewable Updated** `reviewable_updated`: A reviewable item in the review queue was updated.
* **Tag Created** `tag_created`: A tag was created.
* **Tag Destroyed** `tag_destroyed`: A tag was deleted.
* **Tag Updated** `tag_updated`: A tag was updated.
* **Topic Created** `topic_created`: A new topic was created.
* **Topic Destroyed** `topic_destroyed`: A topic was deleted.
* **Topic Edited** `topic_edited`: A topic title, category or tags were edited.
* **Topic Recovered** `topic_recovered`: A deleted topic was recovered.
* **Topic Revised** `topic_revised`: A topic was revised.
* **Unaccepted Solution** `unaccepted_solution`: A post was unmarked as the accepted solution of a topic. Requires the Discourse Solved plugin.
* **User Added To Group** `user_added_to_group`: A user was added to a group.
* **User Anonymized** `user_anonymized`: A user account was anonymized.
* **User Approved** `user_approved`: A user account was approved by staff.
* **User Badge Granted** `user_badge_granted`: A badge was granted to a user.
* **User Badge Revoked** `user_badge_revoked`: A badge was revoked from a user.
* **User Confirmed Email** `user_confirmed_email`: A user confirmed their email address.
* **User Created** `user_created`: A new user account was created.
* **User Destroyed** `user_destroyed`: A user account was deleted.
* **User Logged In** `user_logged_in`: A user logged in.
* **User Logged Out** `user_logged_out`: A user logged out.
* **User Promoted** `user_promoted`: A user was promoted to a new trust level.
* **User Removed From Group** `user_removed_from_group`: A user was removed from a group.
* **User Suspended** `user_suspended`: A user was suspended.
* **User Unsuspended** `user_unsuspended`: A suspended user was unsuspended.
* **User Updated** `user_updated`: A user profile was updated.

</details>
