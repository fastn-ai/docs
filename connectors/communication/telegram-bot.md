---
description: "Telegram Bot API connector."
hidden: true
---

# Telegram Bot API

<img src="../../.gitbook/assets/connectors/telegram-bot.png" alt="Telegram Bot API logo" width="64">

Telegram Bot API connector. Send messages and media, manage chats and members, handle webhooks, and query bot/chat info. Auth via bot token placed in the URL path (https://api.telegram.org/bot{token}/METHOD) — Telegram uses no Authorization header.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [telegram.org](https://telegram.org) |
| **Authentication** | Credentials you enter |
| **Slug** | `telegramBot` |

## Use it

Add Telegram Bot API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.telegramBot.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Answer Callback Query | `answerCallbackQuery` | Send an answer to a callback query from an inline keyboard. Returns True on success. |
| Answer Inline Query | `answerInlineQuery` | Send answers to an inline query. No more than 50 results per query. Returns True on success. |
| Ban Chat Member | `banChatMember` | Ban a user in a group, supergroup or channel. Returns True on success. |
| Copy Message | `copyMessage` | Copy a message without a link to the original. Returns the MessageId of the sent message. |
| Create Chat Invite Link | `createChatInviteLink` | Create an additional invite link for a chat. Returns the new ChatInviteLink object. |
| Delete Message | `deleteMessage` | Delete a message, including service messages. Returns True on success. |
| Delete My Commands | `deleteMyCommands` | Delete the list of the bot's commands for the given scope and language. Returns True on success. |
| Delete Webhook | `deleteWebhook` | Remove webhook integration so the bot can switch back to getUpdates. Returns True on success. |
| Edit Message Caption | `editMessageCaption` | Edit captions of media messages. Returns the edited Message, or True for inline messages. |
| Edit Message Reply Markup | `editMessageReplyMarkup` | Edit only the reply markup (inline keyboard) of messages. Returns the edited Message, or True for inline messages. |

<details>

<summary>See 33 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Edit Message Text | `editMessageText` | Edit text and game messages. Returns the edited Message, or True for inline messages. |
| Forward Message | `forwardMessage` | Forward a message of any kind. Returns the sent Message on success. |
| Get Chat | `getChat` | Get up-to-date information about a chat. Returns a ChatFullInfo object. |
| Get Chat Administrators | `getChatAdministrators` | Get a list of administrators in a chat. Returns an array of ChatMember objects. |
| Get Chat Member | `getChatMember` | Get information about a member of a chat. Returns a ChatMember object. |
| Get Chat Member Count | `getChatMemberCount` | Get the number of members in a chat. Returns an integer. |
| Get File | `getFile` | Get basic info about a file and prepare it for downloading. Returns a File object with file_path. |
| Get Me | `getMe` | Returns basic information about the bot (id, name, username). Free, no-parameter smoke test for the bot token. |
| Get My Commands | `getMyCommands` | Get the current list of the bot's commands. Returns an array of BotCommand objects. |
| Get Updates | `getUpdates` | Receive incoming updates using long polling. Returns an array of Update objects. Cannot be used while a webhook is set. |
| Get Webhook Info | `getWebhookInfo` | Get current webhook status. Returns a WebhookInfo object. If no webhook is set, url is empty. |
| Leave Chat | `leaveChat` | Use this method for the bot to leave a group, supergroup or channel. Returns True on success. |
| Pin Chat Message | `pinChatMessage` | Add a message to the list of pinned messages in a chat. Returns True on success. |
| Promote Chat Member | `promoteChatMember` | Promote or demote a user in a supergroup or channel. Pass False for all boolean params to demote. Returns True on success. |
| Restrict Chat Member | `restrictChatMember` | Restrict a user in a supergroup. The bot must be an admin with appropriate rights. Returns True on success. |
| Send Audio | `sendAudio` | Send an audio file to be displayed in the music player. Returns the sent Message on success. |
| Send Chat Action | `sendChatAction` | Tell the user that something is happening on the bot side (e.g. typing). Returns True on success. |
| Send Contact | `sendContact` | Send a phone contact. Returns the sent Message on success. |
| Send Dice | `sendDice` | Send an animated emoji that displays a random value. Returns the sent Message on success. |
| Send Document | `sendDocument` | Send a general file by file_id, URL, or upload. Returns the sent Message on success. |
| Send Location | `sendLocation` | Send a point on the map. Returns the sent Message on success. |
| Send Message | `sendMessage` | Send a text message. Returns the sent Message object on success. |
| Send Photo | `sendPhoto` | Send a photo by file_id, URL, or upload. Returns the sent Message on success. |
| Send Poll | `sendPoll` | Send a native poll. Returns the sent Message on success. |
| Send Video | `sendVideo` | Send a video (MP4) by file_id, URL, or upload. Returns the sent Message on success. |
| Send Voice | `sendVoice` | Send an audio file as a playable voice message (OGG/OPUS). Returns the sent Message on success. |
| Set Chat Description | `setChatDescription` | Change the description of a group, supergroup or channel. Returns True on success. |
| Set Chat Photo | `setChatPhoto` | Set a new profile photo for the chat. Photo must be uploaded as multipart. Returns True on success. |
| Set Chat Title | `setChatTitle` | Change the title of a chat. Returns True on success. |
| Set My Commands | `setMyCommands` | Change the list of the bot's commands. Returns True on success. |
| Set Webhook | `setWebhook` | Specify a URL to receive incoming updates via an outgoing webhook. Returns True on success. |
| Unban Chat Member | `unbanChatMember` | Unban a previously banned user in a supergroup or channel. Returns True on success. |
| Unpin Chat Message | `unpinChatMessage` | Remove a message from the list of pinned messages in a chat. Returns True on success. |

</details>
