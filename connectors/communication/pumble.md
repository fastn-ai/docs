---
description: "Pumble is a team messaging platform by CAKE.com."
hidden: true
---

# Pumble

Pumble is a team messaging platform by CAKE.com. This connector wraps the Pumble API addon, covering channels, channel membership, messages, threaded replies, message editing and deletion, emoji reactions, scheduled messages, workspace users, and custom status.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [pumble.com](https://pumble.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 20 |
| **Events** | 0 |
| **Slug** | `pumble` |

## Use it

Add Pumble from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pumble.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Reaction | `addReaction` | Adds an emoji reaction to a Pumble message on behalf of the user that owns the API key. |
| Add Users To Channel | `addUsersToChannel` | Adds one or more workspace users to an existing Pumble channel. The endpoint returns HTTP 200 with an empty response body; confirm membership with Get Channel. |
| Create Channel | `createChannel` | Creates a new public or private channel in the Pumble workspace and returns its id and name. The Pumble API addon offers no endpoint to delete or archive a channel, so a channel created here must be removed from the Pumble app. |
| Create Scheduled Message | `createScheduledMessage` | Schedules a message to be posted to a Pumble channel at a future time and returns the scheduled message id. |
| Delete Message | `deleteMessage` | Permanently deletes a message from a Pumble channel. Only messages posted by the API key owner or the addon bot can be deleted, the deletion cannot be undone, and the endpoint returns HTTP 200 with an empty response body. |
| Delete Scheduled Message | `deleteScheduledMessage` | Cancels a scheduled Pumble message by its id so that it is never posted. The cancellation cannot be undone and the endpoint returns HTTP 200 with an empty response body. |
| Edit Message | `editMessage` | Replaces the text of an existing message in a Pumble channel and marks it as edited. Only messages posted by the API key owner or the addon bot can be edited. The endpoint returns HTTP 200 with an empty response body. |
| Edit Scheduled Message | `editScheduledMessage` | Updates the text and delivery time of an existing scheduled Pumble message and returns the updated record. |
| Get Channel | `getChannel` | Retrieves a single Pumble channel by its id or by its name, together with its member list and pinned messages. Supply either Channel ID or Channel Name; when both are given the id takes precedence. |
| Get Current User | `getCurrentUser` | Retrieves the profile of the Pumble workspace user that owns the API key, including their id, name, email, role, status, time zone, and current custom status. |
| Get Scheduled Message | `getScheduledMessage` | Retrieves a single scheduled Pumble message by its id, including its text, target channel, and delivery time. |
| List Channels | `listChannels` | Lists every channel and direct message conversation visible to the user that owns the API key, along with each conversation's members and pinned messages. |
| List Messages | `listMessages` | Lists messages in a Pumble channel, newest page first, with cursor pagination. Supply either Channel ID or Channel Name. For a private channel the API addon bot must be a member. |
| List Scheduled Messages | `listScheduledMessages` | Lists messages scheduled by the user that owns the API key, either across the whole workspace or restricted to a single channel, with cursor pagination. |
| List Users | `listUsers` | Lists every user in the Pumble workspace, including people, addon bots, and the built-in Pumble bot, with their id, name, email, role, and account status. |
| Remove Reaction | `removeReaction` | Removes an emoji reaction previously added by the user that owns the API key from a Pumble message. |
| Remove User From Channel | `removeUserFromChannel` | Removes a single workspace user from a Pumble channel. The endpoint returns HTTP 200 with an empty response body; confirm membership with Get Channel. |
| Send Message | `sendMessage` | Posts a message to a Pumble channel or direct message conversation, either as the user who owns the API key or as the API addon bot. Supply either Channel ID or Channel Name. |
| Send Reply | `sendReply` | Posts a threaded reply to an existing message in a Pumble channel, either as the user who owns the API key or as the API addon bot. Supply either Channel ID or Channel Name. |
| Set Custom Status | `setCustomStatus` | Sets the custom status of the Pumble user that owns the API key, consisting of an emoji, optional status text, and an expiry time. |
