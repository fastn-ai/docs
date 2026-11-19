---
description: "Pumble is a team messaging platform by CAKE.com."
hidden: true
---

# Pumble

<img src="../../.gitbook/assets/connectors/lg/pumble.png" alt="Pumble logo">

This connector wraps the Pumble API addon, covering channels, channel membership, messages, threaded replies, message editing and deletion, emoji reactions, scheduled messages, workspace users, and custom status.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [pumble.com](https://pumble.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `pumble` |

## Use it

Add Pumble from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pumble.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Reaction</td><td><code>addReaction</code></td><td>Adds an emoji reaction to a Pumble message on behalf of the user that owns the API key.</td></tr><tr><td>Add Users To Channel</td><td><code>addUsersToChannel</code></td><td>Adds one or more workspace users to an existing Pumble channel. The endpoint returns HTTP 200 with an empty response body; confirm membership with Get Channel.</td></tr><tr><td>Create Channel</td><td><code>createChannel</code></td><td>Creates a new public or private channel in the Pumble workspace and returns its id and name. The Pumble API addon offers no endpoint to delete or archive a channel, so a channel created here must be removed from the Pumble app.</td></tr><tr><td>Create Scheduled Message</td><td><code>createScheduledMessage</code></td><td>Schedules a message to be posted to a Pumble channel at a future time and returns the scheduled message id.</td></tr><tr><td>Delete Message</td><td><code>deleteMessage</code></td><td>Permanently deletes a message from a Pumble channel. Only messages posted by the API key owner or the addon bot can be deleted, the deletion cannot be undone, and the endpoint returns HTTP 200 with an empty response body.</td></tr><tr><td>Delete Scheduled Message</td><td><code>deleteScheduledMessage</code></td><td>Cancels a scheduled Pumble message by its id so that it is never posted. The cancellation cannot be undone and the endpoint returns HTTP 200 with an empty response body.</td></tr><tr><td>Edit Message</td><td><code>editMessage</code></td><td>Replaces the text of an existing message in a Pumble channel and marks it as edited. Only messages posted by the API key owner or the addon bot can be edited. The endpoint returns HTTP 200 with an empty response body.</td></tr><tr><td>Edit Scheduled Message</td><td><code>editScheduledMessage</code></td><td>Updates the text and delivery time of an existing scheduled Pumble message and returns the updated record.</td></tr><tr><td>Get Channel</td><td><code>getChannel</code></td><td>Retrieves a single Pumble channel by its id or by its name, together with its member list and pinned messages. Supply either Channel ID or Channel Name; when both are given the id takes precedence.</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Retrieves the profile of the Pumble workspace user that owns the API key, including their id, name, email, role, status, time zone, and current custom status.</td></tr></tbody></table>

<details>

<summary>View 10 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Scheduled Message</td><td><code>getScheduledMessage</code></td><td>Retrieves a single scheduled Pumble message by its id, including its text, target channel, and delivery time.</td></tr><tr><td>List Channels</td><td><code>listChannels</code></td><td>Lists every channel and direct message conversation visible to the user that owns the API key, along with each conversation's members and pinned messages.</td></tr><tr><td>List Messages</td><td><code>listMessages</code></td><td>Lists messages in a Pumble channel, newest page first, with cursor pagination. Supply either Channel ID or Channel Name. For a private channel the API addon bot must be a member.</td></tr><tr><td>List Scheduled Messages</td><td><code>listScheduledMessages</code></td><td>Lists messages scheduled by the user that owns the API key, either across the whole workspace or restricted to a single channel, with cursor pagination.</td></tr><tr><td>List Users</td><td><code>listUsers</code></td><td>Lists every user in the Pumble workspace, including people, addon bots, and the built-in Pumble bot, with their id, name, email, role, and account status.</td></tr><tr><td>Remove Reaction</td><td><code>removeReaction</code></td><td>Removes an emoji reaction previously added by the user that owns the API key from a Pumble message.</td></tr><tr><td>Remove User From Channel</td><td><code>removeUserFromChannel</code></td><td>Removes a single workspace user from a Pumble channel. The endpoint returns HTTP 200 with an empty response body; confirm membership with Get Channel.</td></tr><tr><td>Send Message</td><td><code>sendMessage</code></td><td>Posts a message to a Pumble channel or direct message conversation, either as the user who owns the API key or as the API addon bot. Supply either Channel ID or Channel Name.</td></tr><tr><td>Send Reply</td><td><code>sendReply</code></td><td>Posts a threaded reply to an existing message in a Pumble channel, either as the user who owns the API key or as the API addon bot. Supply either Channel ID or Channel Name.</td></tr><tr><td>Set Custom Status</td><td><code>setCustomStatus</code></td><td>Sets the custom status of the Pumble user that owns the API key, consisting of an emoji, optional status text, and an expiry time.</td></tr></tbody></table>

</details>
