---
description: "Slite knowledge base and docs API."
---

# Slite

Slite knowledge base and docs API. Create, read, update, delete and search notes (docs), traverse the doc tree, manage note lifecycle (verify, flag outdated, archive, owner, tiles), ask AI questions over the knowledge base, and look up users and groups. Base URL https://api.slite.com/v1.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [slite.com](https://slite.com) |
| **Authentication** | API key |
| **Actions** | 25 |
| **Events** | 0 |
| **Slug** | `slite` |

## Use it

Add Slite from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.slite.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Note | `archiveNote` | Archive or unarchive a note. Update the archived state of a note |
| Ask a Question | `ask` | Ask a question. Ask a question to your notes in natural language. The scope of the notes used to answer the question is restricted to the authenticated user. Various optional filters are available to restrict the scope of the notes even more. |
| Create Note | `createNote` | Create a note. Create a note from markdown, html, or sliteml content, with a templateId or just an empty one. If no parentNoteId is specified, it will be created in your personal channel. |
| Delete Note | `deleteNote` | Delete a note and its children. Delete a note and its children by id. !!! It's irreversible !!! |
| Flag Note as Outdated | `flagNoteAsOutdated` | Flag note as outdated. Set Outdated status on a note with optional reason |
| Get Group | `getGroup` | Get group by ID. Get a group by ID |
| Get Me | `getMe` | Return the authenticated user information.. Return authenticated user information. |
| Get Note | `getNote` | Return a note. Return a note by id |
| Get Note Children | `getNoteChildren` | Return note children by parent note id. Return note children by parent note id |
| Get User | `getUser` | Get user by ID. Get a user by ID |
| KM List Empty Notes | `kmListEmptyNotes` | List empty notes for knowledge management. List empty notes for knowledge management. |
| KM List Inactive Notes | `kmListInactiveNotes` | List inactive notes for knowledge management. List inactive notes for knowledge management. |
| KM List Notes | `kmListNotes` | List notes for knowledge management. List notes for knowledge management. |
| KM List Public Notes | `kmListPublicNotes` | List public notes for knowledge management. List public notes for knowledge management. |
| List Notes | `listNotes` | List notes. List notes with optional filtering by owner |
| Read a change request | `getChangeRequest` | Read a change request. Read a change request you opened or review. While the agent is still working the response is `202` with `status: "processing"` — check again after `retryAfterSeconds` / the `Retry-After` header. **Beta:** change requests are not yet available to every workspace: contact support to have them enabled. Reviewers can read a request they take part in either way. |
| Read a thread | `getThread` | Read a thread. Read an ask/agent thread back as question / answer rounds. This is both the poll endpoint for a `processing` answer (`GET /ask` returns the `threadId` to poll) and a general way to read a past conversation: it returns every round's question and answer, without the intermediate events. While the run is still working the response is `202` with `status: "processing"` — poll again after `retryAfterSeconds` / the `Retry-After` header. |
| Request a change | `createChangeRequest` | Request a change. Open a change request: an agent reads the docs you name, turns your command into proposed changes, and leaves them for review. Nothing is applied until a reviewer approves it in Slite. The response comes back as soon as the request is queued, with `status: "processing"` and the `url` to hand to the reviewers. **Beta:** change requests are not yet available to every workspace. Where they are not enabled, calls fail with `403` and the error id `change-request/not-enabled`: contact support to have them enabled. |
| Search Groups | `searchGroups` | Search groups. Search for groups by name |
| Search Notes | `searchNotes` | Search notes. Search notes based on a query. The scope of the notes is restricted to the authenticated user. Various optional filters are available to restrict the scope of the search even more. |
| Search Users | `searchUsers` | Search users. Search for users by email, name, or username |
| Update Note | `updateNote` | Update a note. Update note content with markdown, html, or sliteml and/or title |
| Update Note Owner | `updateNoteOwner` | Update note owner. Update the owner of a note, it can be a user or a group |
| Update Tile | `updateTile` | Update a tile in a note. Update or create tile. A tile is rendered with a structured header and a markdown content. You can create a tile by copying a tile id from Slite by clicking on `Copy block id` on an empty line setting in the editor. |
| Verify Note | `verifyNote` | Verify a note. Set Verified status on a note with optional verification expiration |
