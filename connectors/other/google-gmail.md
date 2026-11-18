---
description: "Google Gmail API connector for managing emails, drafts, labels, threads, history, attachments, settings, and push notifications via the Gmail REST API v1."
---

# Google Gmail

Google Gmail API connector for managing emails, drafts, labels, threads, history, attachments, settings, and push notifications via the Gmail REST API v1.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [gmail.com](https://gmail.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 60 |
| **Events** | 1 |
| **Slug** | `googleGmail` |

## Use it

Add Google Gmail from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleGmail.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Delete Messages | `batchDeleteMessages` | Permanently delete multiple messages at once |
| Batch Modify Messages | `batchModifyMessages` | Add or remove labels on multiple messages at once |
| Create Delegate | `createDelegate` | Adds a delegate to the signed-in user's mailbox via Gmail users.settings.delegates.create, giving another user in the same Google Workspace organization access to read, send and delete the user's mail. The delegate is added directly with status accepted (no confirmation email). Google scope: gmail.settings.delegates (or gmail.settings.sharing). Google Workspace only; limited to 25 delegates per user; Gmail documents this method for clients with domain-wide authority. Remove it again with Delete Delegate. Returns the created delegate. |
| Create Draft | `createDraft` | Create a new draft message |
| Create Filter | `createFilter` | Create a new mail filter rule |
| Create Label | `createLabel` | Create a new label in the user's mailbox |
| Create Send-As Alias | `createSendAs` | Creates a custom "from" send-as alias on the signed-in user's Gmail account via users.settings.sendAs.create. If the address needs ownership verification Google emails a verification link to it and the alias stays pending (re-send with Verify Send-As Alias). If smtpMsa is given, Gmail validates the SMTP relay first. Google scope: gmail.settings.sendas (or gmail.settings.sharing); Gmail documents this method for Google Workspace clients with domain-wide authority. Remove it with Delete Send-As Alias. Returns the created SendAs resource. |
| Delete Delegate | `deleteDelegate` | Removes a delegate from the signed-in user's mailbox via Gmail users.settings.delegates.delete, revoking that user's access to the mailbox. Google scope: gmail.settings.delegates (or gmail.settings.sharing). Google Workspace only. Returns an empty body on success. |
| Delete Draft | `deleteDraft` | Permanently delete a draft message |
| Delete Filter | `deleteFilter` | Permanently delete a mail filter |
| Delete Label | `deleteLabel` | Permanently delete a user-created label and remove it from all messages |
| Delete Message | `deleteMessage` | Permanently delete a message (cannot be undone) |
| Delete Send-As Alias | `deleteSendAs` | Deletes a custom send-as alias from the signed-in user's Gmail account via users.settings.sendAs.delete (the primary address cannot be deleted) and revokes any verification it needed. Google scope: gmail.settings.sendas (or gmail.settings.sharing). Returns an empty body on success. |
| Delete Thread | `deleteThread` | Permanently delete a thread and all its messages |
| Get Attachment | `getAttachment` | Download a message attachment by its ID |
| Get Auto-Forwarding Settings | `getAutoForwarding` | Get the auto-forwarding settings for the mailbox |
| Get Delegate | `getDelegate` | Gets one delegate of the signed-in user's mailbox by the delegate's primary email address via Gmail users.settings.delegates.get. Read-only. Google scope: gmail.settings.delegates.readonly (gmail.settings.basic or gmail.readonly also work). Google Workspace mailboxes only. Returns the delegateEmail and its verificationStatus (accepted, pending, rejected or expired). |
| Get Draft | `getDraft` | Get a specific draft message by ID |
| Get Filter | `getFilter` | Get a specific mail filter by ID |
| Get IMAP Settings | `getImapSettings` | Get the IMAP settings for the user's mailbox |
| Get Label | `getLabel` | Get a specific label by ID including message and thread counts |
| Get Language Settings | `getLanguageSettings` | Get the language settings for the user's Gmail display |
| Get Message | `getMessage` | Get a specific message by ID with full payload including headers and body |
| Get OpenID User Info (email) | `getOpenIdUserInfo` | Google OpenID Connect userinfo endpoint. Returns the email and email_verified claims, which are only present when the userinfo.email scope is granted. |
| Get POP Settings | `getPopSettings` | Get the POP settings for the user's mailbox |
| Get Profile | `getProfile` | Get the current user's Gmail profile including email address and mailbox statistics |
| Get Send-As Alias | `getSendAs` | Gets one send-as alias of the signed-in user's Gmail account by its email address via users.settings.sendAs.get (use the primary address to read the main signature and display name). Read-only. Google scope: gmail.settings.sendas.readonly (gmail.settings.basic or gmail.readonly also work). Returns the SendAs resource. |
| Get Thread | `getThread` | Get a specific thread with all its messages |
| Get User Info Profile | `getUserInfoProfile` | Google OAuth2 v2 userinfo endpoint. Returns the profile claims (name, given_name, family_name, picture), which are only present when the userinfo.profile scope is granted. |
| Get Vacation Settings | `getVacationSettings` | Get the vacation auto-reply settings |
| Import Message | `importMessage` | Import a message into the mailbox with standard email delivery scanning and classification |
| Insert Message | `insertMessage` | Insert a message into a mailbox directly (bypasses sending). Useful for importing. |
| List Delegates | `listDelegates` | Lists the delegates on the signed-in user's mailbox (users who can read, send and delete mail on the user's behalf) via Gmail users.settings.delegates.list. Read-only and safe. Google scope: gmail.settings.delegates.readonly (gmail.settings.basic or gmail.readonly also work). Note: Google only serves delegate settings for Google Workspace mailboxes, and the Gmail API documents this method as available to clients with domain-wide authority, so a consumer account can get a 403. Returns delegates[] with delegateEmail and verificationStatus. |
| List Drafts | `listDrafts` | List all draft messages in the user's mailbox |
| List Filters | `listFilters` | List all mail filters in the user's mailbox |
| List Forwarding Addresses | `listForwardingAddresses` | List all forwarding addresses for the user's mailbox |
| List History | `listHistory` | List mailbox history changes since a given historyId |
| List Labels | `listLabels` | List all labels in the user's mailbox (system and user-created) |
| List Messages | `listMessages` | List messages in the authenticated user's mailbox matching optional filters |
| List Send-As Aliases | `listSendAs` | Lists the send-as aliases of the signed-in user's Gmail account via users.settings.sendAs.list: the primary address plus any custom "from" addresses, with display name, reply-to, signature, default flag and verification status. Read-only and safe; works for consumer and Workspace accounts. Google scope: gmail.settings.sendas.readonly (gmail.settings.basic or gmail.readonly also work). Returns sendAs[]. |
| List Threads | `listThreads` | List email threads in the user's mailbox |
| Modify Message | `modifyMessage` | Add or remove labels on a specific message |
| Modify Thread | `modifyThread` | Add or remove labels from all messages in a thread |
| Patch Label | `patchLabel` | Partially update a label (only provided fields are changed) |
| Send Draft | `sendDraft` | Send an existing draft message |
| Send Message | `sendMessage` | Send an email. Provide the message as a base64url-encoded RFC 2822 string in the 'raw' field |
| Stop Watch | `stopWatch` | Stop receiving push notifications for the mailbox |
| Trash Message | `trashMessage` | Move a message to the TRASH label |
| Trash Thread | `trashThread` | Move a thread and all its messages to TRASH |
| Untrash Message | `untrashMessage` | Remove a message from the TRASH label |
| Untrash Thread | `untrashThread` | Remove a thread from TRASH |
| Update Draft | `updateDraft` | Replace an existing draft's content |
| Update IMAP Settings | `updateImapSettings` | Update the IMAP settings for the user's mailbox |
| Update Label | `updateLabel` | Update all properties of a label (full replace) |
| Update Language Settings | `updateLanguageSettings` | Update the language settings for the user's Gmail display |
| Update POP Settings | `updatePopSettings` | Update the POP settings for the user's mailbox |
| Update Send-As Alias | `patchSendAs` | Partially updates a send-as alias of the signed-in user's Gmail account via users.settings.sendAs.patch; only the fields you send change. Use it to change the display name, reply-to address or HTML signature (also works on the primary address), or to make an alias the default. Google scope: gmail.settings.sendas (gmail.settings.basic or gmail.settings.sharing also work). Returns the updated SendAs resource. |
| Update Vacation Settings | `updateVacationSettings` | Update the vacation auto-reply settings |
| Verify Send-As Alias | `verifySendAs` | Re-sends the ownership verification email for a pending custom send-as alias via users.settings.sendAs.verify. Google emails a verification link to the alias address, so only use it on an address you control. Google scope: gmail.settings.sendas (or gmail.settings.sharing). Returns an empty body on success. |
| Watch Mailbox | `watchMailbox` | Starts (or renews) Gmail push notifications for the signed-in user's mailbox via users.watch. Gmail publishes a message to the given Cloud Pub/Sub topic whenever the mailbox changes (optionally only for certain labels). The topic must grant roles/pubsub.publisher to gmail-api-push@system.gserviceaccount.com. Watches expire after 7 days; call again to renew. Use Stop Watch to end notifications. Google scope: gmail.notifications (also accepted: gmail.readonly, gmail.modify, mail.google.com). Returns the current historyId and the expiration time in epoch ms. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Mailbox changed (new or changed email) | `mailboxChanged` | Fires when the connected Gmail mailbox changes (by default only the INBOX label: new mail, label or read-state changes). Gmail push sends only the mailbox address and the new historyId, so call List History with startHistoryId = the historyId you stored last time to get the actual messages. Setup (fastn side, once): Gmail push goes through Google Cloud Pub/Sub. The topic must be in the same Google Cloud project as fastn's Gmail OAuth app (fastn-442814), grant roles/pubsub.publisher to gmail-api-push@system.gserviceaccount.com, and add a PUSH subscription to this connector's webhook URL with 'Enable payload unwrapping' turned on, so the body is the decoded JSON. Each trigger runs users.watch on subscribe and users.stop on unsubscribe. Google ends a watch after 7 days; it has to be renewed by running subscribe again. |
