---
description: "Slite is a team knowledge base. Create, update, search and archive notes, flag outdated ones and ask questions of your docs."
hidden: true
---

# Slite

<img src="../../.gitbook/assets/connectors/lg/slite.png" alt="Slite logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [slite.com](https://slite.com) |
| **Authentication** | API key |
| **Slug** | `slite` |

## Setup

Your customers enter their API key for Slite when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Slite from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Slite**.
2. Select **Connect** on the Slite card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Slite's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Archive Note</td><td><code>archiveNote</code></td><td>Archive or unarchive a note. Update the archived state of a note</td></tr><tr><td>Ask a Question</td><td><code>ask</code></td><td>Ask a question. Ask a question to your notes in natural language. The scope of the notes used to answer the question is restricted to the authenticated user. Various optional filters are available to restrict the scope of the notes even more.</td></tr><tr><td>Create Note</td><td><code>createNote</code></td><td>Create a note. Create a note from markdown, html, or sliteml content, with a templateId or just an empty one. If no parentNoteId is specified, it will be created in your personal channel.</td></tr><tr><td>Delete Note</td><td><code>deleteNote</code></td><td>Delete a note and its children. Delete a note and its children by id. !!! It's irreversible !!!</td></tr><tr><td>Flag Note as Outdated</td><td><code>flagNoteAsOutdated</code></td><td>Flag note as outdated. Set Outdated status on a note with optional reason</td></tr><tr><td>Get Group</td><td><code>getGroup</code></td><td>Get group by ID. Get a group by ID</td></tr><tr><td>Get Me</td><td><code>getMe</code></td><td>Return the authenticated user information.. Return authenticated user information.</td></tr><tr><td>Get Note</td><td><code>getNote</code></td><td>Return a note. Return a note by id</td></tr><tr><td>Get Note Children</td><td><code>getNoteChildren</code></td><td>Return note children by parent note id. Return note children by parent note id</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Get user by ID. Get a user by ID</td></tr></tbody></table>

<details>

<summary>View 15 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>KM List Empty Notes</td><td><code>kmListEmptyNotes</code></td><td>List empty notes for knowledge management. List empty notes for knowledge management.</td></tr><tr><td>KM List Inactive Notes</td><td><code>kmListInactiveNotes</code></td><td>List inactive notes for knowledge management. List inactive notes for knowledge management.</td></tr><tr><td>KM List Notes</td><td><code>kmListNotes</code></td><td>List notes for knowledge management. List notes for knowledge management.</td></tr><tr><td>KM List Public Notes</td><td><code>kmListPublicNotes</code></td><td>List public notes for knowledge management. List public notes for knowledge management.</td></tr><tr><td>List Notes</td><td><code>listNotes</code></td><td>List notes. List notes with optional filtering by owner</td></tr><tr><td>Read a change request</td><td><code>getChangeRequest</code></td><td>Read a change request. Read a change request you opened or review. While the agent is still working the response is `202` with `status: "processing"` — check again after `retryAfterSeconds` / the `Retry-After` header. **Beta:** change requests are not yet available to every workspace: contact support to have them enabled. Reviewers can read a request they take part in either way.</td></tr><tr><td>Read a thread</td><td><code>getThread</code></td><td>Read a thread. Read an ask/agent thread back as question / answer rounds. This is both the poll endpoint for a `processing` answer (` returns the `threadId` to poll) and a general way to read a past conversation: it returns every round's question and answer, without the intermediate events. While the run is still working the response is `202` with `status: "processing"` — poll again after `retryAfterSeconds` / the `Retry-After` header.</td></tr><tr><td>Request a change</td><td><code>createChangeRequest</code></td><td>Request a change. Open a change request: an agent reads the docs you name, turns your command into proposed changes, and leaves them for review. Nothing is applied until a reviewer approves it in Slite. The response comes back as soon as the request is queued, with `status: "processing"` and the `url` to hand to the reviewers. **Beta:** change requests are not yet available to every workspace. Where they are not enabled, calls fail with `403` and the error id `change-request/not-enabled`: contact support to have them enabled.</td></tr><tr><td>Search Groups</td><td><code>searchGroups</code></td><td>Search groups. Search for groups by name</td></tr><tr><td>Search Notes</td><td><code>searchNotes</code></td><td>Search notes. Search notes based on a query. The scope of the notes is restricted to the authenticated user. Various optional filters are available to restrict the scope of the search even more.</td></tr><tr><td>Search Users</td><td><code>searchUsers</code></td><td>Search users. Search for users by email, name, or username</td></tr><tr><td>Update Note</td><td><code>updateNote</code></td><td>Update a note. Update note content with markdown, html, or sliteml and/or title</td></tr><tr><td>Update Note Owner</td><td><code>updateNoteOwner</code></td><td>Update note owner. Update the owner of a note, it can be a user or a group</td></tr><tr><td>Update Tile</td><td><code>updateTile</code></td><td>Update a tile in a note. Update or create tile. A tile is rendered with a structured header and a markdown content. You can create a tile by copying a tile id from Slite by clicking on `Copy block id` on an empty line setting in the editor.</td></tr><tr><td>Verify Note</td><td><code>verifyNote</code></td><td>Verify a note. Set Verified status on a note with optional verification expiration</td></tr></tbody></table>

</details>

