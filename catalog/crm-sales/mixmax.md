---
description: "Mixmax is a sales engagement platform for Gmail. Manage sequences and recipients, contacts, contact groups, notes and rules."
hidden: true
---

# Mixmax

<img src="../../.gitbook/assets/connectors/lg/mixmax.png" alt="Mixmax logo">

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [mixmax.com](https://mixmax.com) |
| **Authentication** | API key |
| **Slug** | `mixmax` |

## Setup

Your customers enter their API key for Mixmax when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Mixmax from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Mixmax**.
2. Select **Connect** on the Mixmax card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Mixmax's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Contact Group Member</td><td><code>addContactGroupMember</code></td><td>Add a contact to a contact group Provide email or contactId; supports bulk via contacts array.</td></tr><tr><td>Add Sequence Recipients</td><td><code>addSequenceRecipients</code></td><td>Add one or more recipients to a sequence Provide a recipients array of {email, variables, scheduledAt}.</td></tr><tr><td>Create Contact</td><td><code>createContact</code></td><td>Create a contact email is unique; a duplicate email merges.</td></tr><tr><td>Create Contact Group</td><td><code>createContactGroup</code></td><td>Create a contact group Provide a name; optionally contacts.</td></tr><tr><td>Create Contact Note</td><td><code>createContactNote</code></td><td>Add a note to a contact Provide text.</td></tr><tr><td>Create Rule</td><td><code>createRule</code></td><td>Create a Mixmax automation rule record Provide a name.</td></tr><tr><td>Create Snippet Tag</td><td><code>createSnippetTag</code></td><td>Create a snippet tag Provide a name.</td></tr><tr><td>Delete Contact</td><td><code>deleteContact</code></td><td>Delete a contact</td></tr><tr><td>Delete Contact Group</td><td><code>deleteContactGroup</code></td><td>Delete a contact group</td></tr><tr><td>Delete Contact Note</td><td><code>deleteContactNote</code></td><td>Delete a contact note Only the creator can delete.</td></tr></tbody></table>

<details>

<summary>View 33 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Rule</td><td><code>deleteRule</code></td><td>Delete an automation rule</td></tr><tr><td>Delete Snippet Tag</td><td><code>deleteSnippetTag</code></td><td>Delete a snippet tag</td></tr><tr><td>Get Contact</td><td><code>getContact</code></td><td>Retrieve a contact by _id</td></tr><tr><td>Get Contact Group</td><td><code>getContactGroup</code></td><td>Retrieve a specific contact group</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Retrieve the authenticated Mixmax user Returns the user's _id.</td></tr><tr><td>Get Live Feed</td><td><code>getLiveFeed</code></td><td>Get your Mixmax activity/insights live feed with engagement stats</td></tr><tr><td>Get Meeting Transcript</td><td><code>getMeetingTranscript</code></td><td>Retrieve the full transcript for a meeting by its summary id</td></tr><tr><td>Get Meeting Type</td><td><code>getMeetingType</code></td><td>Retrieve a single availability / scheduling link type by id</td></tr><tr><td>Get Message</td><td><code>getMessage</code></td><td>Retrieve a single tracked message by its id</td></tr><tr><td>Get Rule</td><td><code>getRule</code></td><td>Retrieve a single automation rule by id</td></tr><tr><td>Get Snippet</td><td><code>getSnippet</code></td><td>Retrieve a single snippet by id</td></tr><tr><td>Get Snippet Tag</td><td><code>getSnippetTag</code></td><td>Retrieve a single snippet tag by id</td></tr><tr><td>List Contact Group Members</td><td><code>listContactGroupMembers</code></td><td>Return membership for a contact group</td></tr><tr><td>List Contact Groups</td><td><code>listContactGroups</code></td><td>List contact groups you can access</td></tr><tr><td>List Contact Notes</td><td><code>listContactNotes</code></td><td>List notes for a contact Pass expand=userId to include owner name/email.</td></tr><tr><td>List Contacts</td><td><code>listContacts</code></td><td>List your Mixmax contacts Cursor paginated.</td></tr><tr><td>List File Requests</td><td><code>listFileRequests</code></td><td>List file requests you have sent</td></tr><tr><td>List Meeting Types</td><td><code>listMeetingTypes</code></td><td>List your availability / scheduling link types Cursor paginated.</td></tr><tr><td>List Messages</td><td><code>listMessages</code></td><td>List tracked messages you have sent with Mixmax Cursor paginated via next/previous.</td></tr><tr><td>List Rules</td><td><code>listRules</code></td><td>List your Mixmax automation rules</td></tr><tr><td>List Sequence Recipients</td><td><code>listSequenceRecipients</code></td><td>List activated recipients of a sequence Offset paginated; returns an array.</td></tr><tr><td>List Sequences</td><td><code>listSequences</code></td><td>List sequences you have access to Filter by name/folder; pass expand=stages for stage detail.</td></tr><tr><td>List Snippet Tags</td><td><code>listSnippetTags</code></td><td>List snippet tags Cursor paginated.</td></tr><tr><td>List Snippets</td><td><code>listSnippets</code></td><td>List your saved snippets/templates Cursor paginated.</td></tr><tr><td>List Teams</td><td><code>listTeams</code></td><td>List teams you belong to</td></tr><tr><td>Query Contacts</td><td><code>queryContacts</code></td><td>Search contacts across Mixmax, Google directory, and Salesforce</td></tr><tr><td>Remove Contact Group Member</td><td><code>removeContactGroupMember</code></td><td>Remove a contact from a contact group</td></tr><tr><td>Search Meeting Summaries</td><td><code>searchMeetingSummaries</code></td><td>Search meeting (Copilot) summaries Requires the mixmaxApi feature.</td></tr><tr><td>Update Contact</td><td><code>updateContact</code></td><td>Update a contact</td></tr><tr><td>Update Contact Group</td><td><code>updateContactGroup</code></td><td>Edit a contact group</td></tr><tr><td>Update Contact Note</td><td><code>updateContactNote</code></td><td>Edit a contact note Only the creator can edit.</td></tr><tr><td>Update Rule</td><td><code>updateRule</code></td><td>Update an automation rule Provide fields to change (e.g. name).</td></tr><tr><td>Update Snippet Tag</td><td><code>updateSnippetTag</code></td><td>Rename a snippet tag</td></tr></tbody></table>

</details>

