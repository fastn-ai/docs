---
description: "Trello connector for boards, lists, cards, checklists, labels, members, organizations, actions, search, and webhooks via the Trello REST API (v1)."
---

# Trello

Trello connector for boards, lists, cards, checklists, labels, members, organizations, actions, search, and webhooks via the Trello REST API (v1). Auth uses an API key + token sent as query parameters on every request.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [trello.com](https://trello.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Actions** | 68 |
| **Events** | 18 |
| **Slug** | `trello` |

## Use it

Add Trello from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.trello.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Attachment To Card | `addAttachmentToCard` | Attach a URL or file reference to a card. |
| Add Comment To Card | `addCommentToCard` | Add a comment to a card. |
| Add Label To Card | `addLabelToCard` | Add an existing label to a card. |
| Add Member To Card | `addMemberToCard` | Assign a member to a card. |
| Add Sticker To Card | `addStickerToCard` | Add a sticker to a card. |
| Archive Or Unarchive List | `archiveList` | Archive (close) or unarchive a list by setting its closed state. |
| Create Board | `createBoard` | Create a new board. |
| Create Card | `createCard` | Create a new card on a list. |
| Create Check Item | `createCheckItem` | Create a check item in a checklist. |
| Create Checklist On Card | `createChecklistOnCard` | Create a new checklist on a card. |
| Create Label | `createLabel` | Create a new label on a board. |
| Create List | `createList` | Create a new list on a board. |
| Create Organization | `createOrganization` | Create a new organization (workspace). |
| Create Webhook | `createWebhook` | Register a webhook that fires when the specified model (board, list, card, member, organization) changes. |
| Delete Board | `deleteBoard` | Delete a board permanently. |
| Delete Card | `deleteCard` | Delete a card permanently. |
| Delete Card Attachment | `deleteCardAttachment` | Delete an attachment from a card. |
| Delete Card Comment | `deleteCardComment` | Delete a comment from a card. |
| Delete Check Item | `deleteCheckItem` | Delete a check item from a checklist. |
| Delete Checklist | `deleteChecklist` | Delete a checklist permanently. |
| Delete Label | `deleteLabel` | Delete a label permanently. |
| Delete Organization | `deleteOrganization` | Delete an organization (workspace) permanently. |
| Delete Sticker From Card | `deleteStickerFromCard` | Remove a sticker from a card. |
| Delete Webhook | `deleteWebhook` | Delete a webhook by ID. |
| Get Action | `getActionById` | Retrieve a single action (activity log entry) by ID. |
| Get Board | `getBoard` | Retrieve a single board by ID. |
| Get Card | `getCard` | Retrieve a single card by ID. |
| Get Card Attachment | `getCardAttachment` | Retrieve a single attachment on a card. |
| Get Check Item On Card | `getCheckItemOnCard` | Retrieve a check item on a card. |
| Get Checklist | `getChecklist` | Retrieve a single checklist by ID. |
| Get Label | `getLabel` | Retrieve a single label by ID. |
| Get List | `getList` | Retrieve a single list by ID. |
| Get Member | `getMember` | Retrieve a member by ID or username (use 'me' for the authenticated user). |
| Get Organization | `getOrganization` | Retrieve an organization (workspace) by ID or name. |
| Get Webhook | `getWebhook` | Retrieve a single webhook by ID. |
| List Board Actions | `getBoardActions` | List the actions (activity feed) on a board. |
| List Board Cards | `getBoardCards` | List the cards on a board. |
| List Board Labels | `getBoardLabels` | List the labels on a board. |
| List Board Lists | `getBoardLists` | List the lists on a board. |
| List Board Members | `getBoardMembers` | List the members of a board. |
| List Boards For Member | `listBoards` | List all boards belonging to a member (use 'me' for the authenticated user). |
| List Card Attachments | `getCardAttachments` | List the attachments on a card. |
| List Card Checklists | `getCardChecklists` | List the checklists on a card. |
| List Card Comments | `getCardComments` | List the comment actions on a card. |
| List Card Members | `getCardMembers` | List the members assigned to a card. |
| List Card Stickers | `getCardStickers` | List the stickers on a card. |
| List Cards In List | `getListCards` | List the cards in a list. |
| List Checklist Check Items | `getChecklistCheckItems` | List the check items in a checklist. |
| List Member Cards | `getMemberCards` | List the cards assigned to a member. |
| List Member Organizations | `getMemberOrganizations` | List the organizations a member belongs to. |
| List Organization Boards | `getOrganizationBoards` | List the boards belonging to an organization. |
| List Organization Members | `getOrganizationMembers` | List the members of an organization. |
| List Token Webhooks | `listWebhooks` | List all webhooks created with the current API token. Works only with the API Key + Token sign-in: Trello's endpoint needs the token in the URL path (/1/tokens/{token}/webhooks), and an OAuth 2.0 connection has no such token, so this action cannot run on OAuth connections. |
| Move All Cards In List | `moveAllCardsInList` | Move all cards in a list to another list/board. |
| Remove Label From Card | `removeLabelFromCard` | Remove a label from a card. |
| Remove Member From Card | `removeMemberFromCard` | Remove a member from a card. |
| Search | `search` | Search Trello for cards, boards, organizations, and members matching a query. |
| Search Members | `searchMembers` | Search for Trello members by name or username. |
| Update Board | `updateBoard` | Update an existing board. |
| Update Card | `updateCard` | Update an existing card. Partial update: only the fields provided are changed (name is optional). |
| Update Card Comment | `updateCardComment` | Update the text of an existing comment on a card. |
| Update Check Item On Card | `updateCheckItemOnCard` | Update a check item on a card (name, state, position). |
| Update Checklist | `updateChecklist` | Update an existing checklist (name/position). |
| Update Label | `updateLabel` | Update an existing label. |
| Update List | `updateList` | Update an existing list. |
| Update Member | `updateMember` | Update the authenticated member's profile fields. |
| Update Organization | `updateOrganization` | Update an existing organization (workspace). |
| Update Webhook | `updateWebhook` | Update an existing webhook (callback URL, model, active state). |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Attachment Added To Card | `addAttachmentToCard` | An attachment was added to a card. |
| Attachment Removed From Card | `deleteAttachmentFromCard` | An attachment was removed from a card. |
| Board Created | `createBoard` | A board was created. |
| Board Updated | `updateBoard` | A board was updated. |
| Card Created | `createCard` | A card was created on the watched model. |
| Card Deleted | `deleteCard` | A card was deleted. |
| Card Updated | `updateCard` | A card was updated (moved, renamed, due date, etc). |
| Check Item State Updated | `updateCheckItemStateOnCard` | A check item was marked complete/incomplete. |
| Checklist Added To Card | `addChecklistToCard` | A checklist was added to a card. |
| Comment Added To Card | `commentCard` | A comment was added to a card. |
| Label Added To Card | `addLabelToCard` | A label was added to a card. |
| Label Removed From Card | `removeLabelFromCard` | A label was removed from a card. |
| List Created | `createList` | A list was created on the watched board. |
| List Updated | `updateList` | A list was updated (renamed, archived, moved). |
| Member Added To Board | `addMemberToBoard` | A member was added to a board. |
| Member Added To Card | `addMemberToCard` | A member was added to a card. |
| Member Removed From Board | `removeMemberFromBoard` | A member was removed from a board. |
| Member Removed From Card | `removeMemberFromCard` | A member was removed from a card. |
