---
description: "Telegram is a messaging app. Send and edit messages as a bot, manage chats, members and invite links, and answer callback and inline queries."
hidden: true
---

# Telegram Bot API

<img src="../../.gitbook/assets/connectors/lg/telegram-bot.png" alt="Telegram Bot API logo">

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [telegram.org](https://telegram.org) |
| **Authentication** | Bot token |
| **Slug** | `telegramBot` |

## Setup

Your customers enter their bot token for Telegram Bot API when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Telegram Bot API from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Telegram Bot API**.
2. Select **Connect** on the Telegram Bot API card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Telegram Bot API's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Answer Callback Query</td><td><code>answerCallbackQuery</code></td><td>Send an answer to a callback query from an inline keyboard. Returns True on success.</td></tr><tr><td>Answer Inline Query</td><td><code>answerInlineQuery</code></td><td>Send answers to an inline query. No more than 50 results per query. Returns True on success.</td></tr><tr><td>Ban Chat Member</td><td><code>banChatMember</code></td><td>Ban a user in a group, supergroup or channel. Returns True on success.</td></tr><tr><td>Copy Message</td><td><code>copyMessage</code></td><td>Copy a message without a link to the original. Returns the MessageId of the sent message.</td></tr><tr><td>Create Chat Invite Link</td><td><code>createChatInviteLink</code></td><td>Create an additional invite link for a chat. Returns the new ChatInviteLink object.</td></tr><tr><td>Delete Message</td><td><code>deleteMessage</code></td><td>Delete a message, including service messages. Returns True on success.</td></tr><tr><td>Delete My Commands</td><td><code>deleteMyCommands</code></td><td>Delete the list of the bot's commands for the given scope and language. Returns True on success.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Remove webhook integration so the bot can switch back to getUpdates. Returns True on success.</td></tr><tr><td>Edit Message Caption</td><td><code>editMessageCaption</code></td><td>Edit captions of media messages. Returns the edited Message, or True for inline messages.</td></tr><tr><td>Edit Message Reply Markup</td><td><code>editMessageReplyMarkup</code></td><td>Edit only the reply markup (inline keyboard) of messages. Returns the edited Message, or True for inline messages.</td></tr></tbody></table>

<details>

<summary>View 33 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Edit Message Text</td><td><code>editMessageText</code></td><td>Edit text and game messages. Returns the edited Message, or True for inline messages.</td></tr><tr><td>Forward Message</td><td><code>forwardMessage</code></td><td>Forward a message of any kind. Returns the sent Message on success.</td></tr><tr><td>Get Chat</td><td><code>getChat</code></td><td>Get up-to-date information about a chat. Returns a ChatFullInfo object.</td></tr><tr><td>Get Chat Administrators</td><td><code>getChatAdministrators</code></td><td>Get a list of administrators in a chat. Returns an array of ChatMember objects.</td></tr><tr><td>Get Chat Member</td><td><code>getChatMember</code></td><td>Get information about a member of a chat. Returns a ChatMember object.</td></tr><tr><td>Get Chat Member Count</td><td><code>getChatMemberCount</code></td><td>Get the number of members in a chat. Returns an integer.</td></tr><tr><td>Get File</td><td><code>getFile</code></td><td>Get basic info about a file and prepare it for downloading. Returns a File object with file_path.</td></tr><tr><td>Get Me</td><td><code>getMe</code></td><td>Returns basic information about the bot (id, name, username). Free, no-parameter smoke test for the bot token.</td></tr><tr><td>Get My Commands</td><td><code>getMyCommands</code></td><td>Get the current list of the bot's commands. Returns an array of BotCommand objects.</td></tr><tr><td>Get Updates</td><td><code>getUpdates</code></td><td>Receive incoming updates using long polling. Returns an array of Update objects. Cannot be used while a webhook is set.</td></tr><tr><td>Get Webhook Info</td><td><code>getWebhookInfo</code></td><td>Get current webhook status. Returns a WebhookInfo object. If no webhook is set, url is empty.</td></tr><tr><td>Leave Chat</td><td><code>leaveChat</code></td><td>Use this method for the bot to leave a group, supergroup or channel. Returns True on success.</td></tr><tr><td>Pin Chat Message</td><td><code>pinChatMessage</code></td><td>Add a message to the list of pinned messages in a chat. Returns True on success.</td></tr><tr><td>Promote Chat Member</td><td><code>promoteChatMember</code></td><td>Promote or demote a user in a supergroup or channel. Pass False for all boolean params to demote. Returns True on success.</td></tr><tr><td>Restrict Chat Member</td><td><code>restrictChatMember</code></td><td>Restrict a user in a supergroup. The bot must be an admin with appropriate rights. Returns True on success.</td></tr><tr><td>Send Audio</td><td><code>sendAudio</code></td><td>Send an audio file to be displayed in the music player. Returns the sent Message on success.</td></tr><tr><td>Send Chat Action</td><td><code>sendChatAction</code></td><td>Tell the user that something is happening on the bot side (e.g. typing). Returns True on success.</td></tr><tr><td>Send Contact</td><td><code>sendContact</code></td><td>Send a phone contact. Returns the sent Message on success.</td></tr><tr><td>Send Dice</td><td><code>sendDice</code></td><td>Send an animated emoji that displays a random value. Returns the sent Message on success.</td></tr><tr><td>Send Document</td><td><code>sendDocument</code></td><td>Send a general file by file_id, URL, or upload. Returns the sent Message on success.</td></tr><tr><td>Send Location</td><td><code>sendLocation</code></td><td>Send a point on the map. Returns the sent Message on success.</td></tr><tr><td>Send Message</td><td><code>sendMessage</code></td><td>Send a text message. Returns the sent Message object on success.</td></tr><tr><td>Send Photo</td><td><code>sendPhoto</code></td><td>Send a photo by file_id, URL, or upload. Returns the sent Message on success.</td></tr><tr><td>Send Poll</td><td><code>sendPoll</code></td><td>Send a native poll. Returns the sent Message on success.</td></tr><tr><td>Send Video</td><td><code>sendVideo</code></td><td>Send a video (MP4) by file_id, URL, or upload. Returns the sent Message on success.</td></tr><tr><td>Send Voice</td><td><code>sendVoice</code></td><td>Send an audio file as a playable voice message (OGG/OPUS). Returns the sent Message on success.</td></tr><tr><td>Set Chat Description</td><td><code>setChatDescription</code></td><td>Change the description of a group, supergroup or channel. Returns True on success.</td></tr><tr><td>Set Chat Photo</td><td><code>setChatPhoto</code></td><td>Set a new profile photo for the chat. Photo must be uploaded as multipart. Returns True on success.</td></tr><tr><td>Set Chat Title</td><td><code>setChatTitle</code></td><td>Change the title of a chat. Returns True on success.</td></tr><tr><td>Set My Commands</td><td><code>setMyCommands</code></td><td>Change the list of the bot's commands. Returns True on success.</td></tr><tr><td>Set Webhook</td><td><code>setWebhook</code></td><td>Specify a URL to receive incoming updates via an outgoing webhook. Returns True on success.</td></tr><tr><td>Unban Chat Member</td><td><code>unbanChatMember</code></td><td>Unban a previously banned user in a supergroup or channel. Returns True on success.</td></tr><tr><td>Unpin Chat Message</td><td><code>unpinChatMessage</code></td><td>Remove a message from the list of pinned messages in a chat. Returns True on success.</td></tr></tbody></table>

</details>

