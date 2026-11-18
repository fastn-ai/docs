---
description: "Microsoft Outlook Mail via Microsoft Graph v1.0 (https://graph.microsoft.com/v1.0)."
hidden: true
---

# Microsoft Outlook Mail

<img src="../../.gitbook/assets/connectors/lg/microsoft-outlook-mail.png" alt="Microsoft Outlook Mail logo">

Microsoft Outlook Mail via Microsoft Graph v1.0 (https://graph.microsoft.com/v1.0). Messages (list, get, create draft, update, delete, copy, move, send), replies and forwards, MIME content, delta sync, attachments, mail folders, message rules, Outlook categories, Focused Inbox overrides and mailbox settings.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [graph.microsoft.com](https://graph.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `microsoftOutlookMail` |

## Use it

Add Microsoft Outlook Mail from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.microsoftOutlookMail.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add File Attachment | `addFileAttachment` | Adds a base64-encoded file attachment to an existing message or draft. This endpoint supports files up to 3 MB; larger files require an upload session, which this connector does not expose. |
| Copy Mail Folder | `copyMailFolder` | Copies a mail folder and its contents into another mail folder, returning the new copy. The destination must not already contain a folder with the same name, otherwise Graph returns ErrorMoveCopyFailed. |
| Copy Message | `copyMessage` | Copies a message to another mail folder, leaving the original message in place. |
| Create Child Folder | `createChildFolder` | Creates a new mail folder nested under an existing mail folder. |
| Create Draft Message | `createDraftMessage` | Creates a draft message in the signed-in user's Drafts folder. Additional recipients and properties can be set afterwards with Update Message, and the draft is delivered with Send Draft Message. |
| Create Focused Inbox Override | `createInferenceClassificationOverride` | Creates a Focused Inbox override so that all future messages from a sender are always delivered to the Focused or the Other tab. |
| Create Forward Draft | `createForwardDraft` | Creates a draft that forwards a message to a recipient without sending it, so it can be edited and sent later with Send Draft Message. |
| Create Mail Folder | `createMailFolder` | Creates a new top-level mail folder in the signed-in user's mailbox. |
| Create Message Rule | `createMessageRule` | Creates an inbox rule that moves incoming messages from a given sender into a destination folder. Outlook applies the rule to messages arriving in the Inbox. |
| Create Outlook Category | `createOutlookCategory` | Creates an Outlook category that can then be applied to messages. Category display names must be unique within the mailbox. |

<details>

<summary>See 42 more actions</summary>

* **Create Reply All Draft** `createReplyAllDraft`: Creates a draft reply to the sender and all other recipients of a message without sending it, so it can be edited and sent later with Send Draft Message.
* **Create Reply Draft** `createReplyDraft`: Creates a draft reply to the sender of a message without sending it, so it can be edited and sent later with Send Draft Message.
* **Delete Attachment** `deleteAttachment`: Removes an attachment from a message.
* **Delete Focused Inbox Override** `deleteInferenceClassificationOverride`: Removes a Focused Inbox override, so Outlook resumes classifying that sender's messages automatically.
* **Delete Mail Folder** `deleteMailFolder`: Deletes a mail folder and everything it contains. Deleting a folder cannot be undone from the API.
* **Delete Message** `deleteMessage`: Deletes a message from the signed-in user's mailbox, moving it to the Deleted Items folder.
* **Delete Message Rule** `deleteMessageRule`: Deletes an inbox rule from the signed-in user's mailbox.
* **Delete Outlook Category** `deleteOutlookCategory`: Deletes an Outlook category from the signed-in user's mailbox.
* **Forward Message** `forwardMessage`: Forwards a message to a recipient with a comment and sends it immediately. The forwarded message is saved in the Sent Items folder.
* **Get Attachment** `getAttachment`: Retrieves a single attachment of a message, including its base64-encoded content for file attachments.
* **Get Automatic Replies Setting** `getAutomaticRepliesSetting`: Retrieves only the automatic replies (out of office) configuration from the signed-in user's mailbox settings.
* **Get Mail Folder** `getMailFolder`: Retrieves a single mail folder, including its total and unread item counts.
* **Get Mailbox Settings** `getMailboxSettings`: Retrieves the full mailbox settings for the signed-in user, including time zone, date and time formats, language, working hours and automatic replies. The endpoint always returns the complete settings object.
* **Get Message** `getMessage`: Retrieves a single message from the signed-in user's mailbox by its message id.
* **Get Message MIME Content** `getMessageMimeContent`: Retrieves the full MIME (RFC 822) content of a message as raw text, suitable for archiving or re-importing. The response is a plain text body, not a JSON object.
* **Get Message Rule** `getMessageRule`: Retrieves a single inbox rule, including its conditions, actions and exceptions.
* **Get My Profile** `getMyProfile`: Retrieves the profile of the signed-in user, including the display name and the primary email address used by the mailbox.
* **Get Outlook Category** `getOutlookCategory`: Retrieves a single Outlook category by its id.
* **List Attachments** `listAttachments`: Lists the attachments of a message, including file, item and reference attachments.
* **List Child Folders** `listChildFolders`: Lists the child folders nested directly under a mail folder.
* **List Focused Inbox Overrides** `listInferenceClassificationOverrides`: Lists the Focused Inbox overrides for the signed-in user, each pinning messages from a sender to the Focused or Other tab.
* **List Mail Folders** `listMailFolders`: Lists the top-level mail folders in the signed-in user's mailbox.
* **List Mail Folders Delta** `listMailFoldersDelta`: Returns the mail folders that were added, deleted or updated since the previous synchronisation round. Call it without a token to start tracking, then reuse the token from the deltaLink of the previous response.
* **List Message Rules** `listMessageRules`: Lists the inbox rules defined for the signed-in user, in the order Outlook evaluates them.
* **List Messages** `listMessages`: Lists the messages in the signed-in user's mailbox across all folders, including Deleted Items. Use the OData parameters to page, filter, sort and trim the response.
* **List Messages Delta** `listMessagesDelta`: Returns the messages that were added, deleted or updated in a mail folder since the previous synchronisation round. Call it without a token to start tracking, then reuse the token from the deltaLink of the previous response.
* **List Messages In Folder** `listMessagesInFolder`: Lists the messages contained in a specific mail folder of the signed-in user's mailbox.
* **List Outlook Categories** `listOutlookCategories`: Lists all Outlook categories defined for the signed-in user, each with its display name and colour preset. The endpoint returns the complete set and does not support OData paging, filtering or sorting.
* **Move Mail Folder** `moveMailFolder`: Moves a mail folder and its contents into another mail folder. The destination must not already contain a folder with the same name, otherwise Graph returns ErrorMoveCopyFailed.
* **Move Message** `moveMessage`: Moves a message to another mail folder. The move creates a new message id in the destination folder and the original id stops resolving, so downstream calls must use the id returned here.
* **Reply All To Message** `replyAllToMessage`: Replies to the sender and all other recipients of a message with a comment and sends it immediately. The reply is saved in the Sent Items folder.
* **Reply To Message** `replyToMessage`: Replies to the sender of a message with a comment and sends it immediately. The reply is saved in the Sent Items folder.
* **Send Draft Message** `sendDraftMessage`: Sends an existing draft message. The message is saved in the Sent Items folder.
* **Send Mail** `sendMail`: Composes and sends a message in one call from the signed-in user's mailbox. To address more than one recipient, create a draft with Create Draft Message, set the full recipient collection with Update Message, then call Send Draft Message.
* **Set Automatic Replies** `setAutomaticReplies`: Turns automatic replies (out of office) on or off for the signed-in user and sets the internal and external reply messages.
* **Set Mailbox Date And Time Format** `setMailboxDateTimeFormat`: Sets the date and time display formats on the signed-in user's mailbox. Both values must be formats supported by the mailbox's display language.
* **Set Mailbox Time Zone** `setMailboxTimeZone`: Sets the default time zone of the signed-in user's mailbox, given as a Windows or IANA time zone name.
* **Update Focused Inbox Override** `updateInferenceClassificationOverride`: Changes which Inbox tab an existing Focused Inbox override delivers a sender's messages to.
* **Update Mail Folder** `updateMailFolder`: Renames a mail folder. Only the display name of a folder is writeable.
* **Update Message** `updateMessage`: Updates writeable properties of a message. Only the properties you supply are sent, so untouched properties keep their current values. Draft messages accept subject, body and recipient changes; delivered messages accept only properties such as isRead, categories and flag.
* **Update Message Rule** `updateMessageRule`: Updates the name, order or enabled state of an inbox rule. Only the properties you supply are sent, so the rule's conditions and actions are preserved.
* **Update Outlook Category** `updateOutlookCategory`: Changes the colour of an Outlook category. The display name of an existing category cannot be changed through the API.

</details>
