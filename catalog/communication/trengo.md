---
description: "Trengo is a multichannel customer engagement platform. Manage contacts, labels, teams and webhooks, and read SMS messages."
hidden: true
---

# Trengo

<img src="../../.gitbook/assets/connectors/lg/trengo.png" alt="Trengo logo">

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [trengo.com](https://trengo.com) |
| **Authentication** | API token |
| **Slug** | `trengo` |

## Setup

Your customers enter their API token for Trengo when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Trengo from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Trengo**.
2. Select **Connect** on the Trengo card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Trengo's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Contact</td><td><code>createContact</code></td><td>Create a new contact.</td></tr><tr><td>Create Label</td><td><code>createLabel</code></td><td>Create a new label.</td></tr><tr><td>Create Team</td><td><code>createTeam</code></td><td>Create a new team.</td></tr><tr><td>Create Webhook</td><td><code>createWebhook</code></td><td>Register a new webhook subscription. Trengo will POST an event payload to the given URL when the specified event type occurs, signed with a 'Trengo-Signature' header ({timestamp};{hex_hmac_sha256} over '{timestamp}.{body}' using the returned signing_secret).</td></tr><tr><td>Delete Contact</td><td><code>deleteContact</code></td><td>Delete a contact by id.</td></tr><tr><td>Delete Label</td><td><code>deleteLabel</code></td><td>Delete a label by id.</td></tr><tr><td>Delete Team</td><td><code>deleteTeam</code></td><td>Delete a team by id.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Delete a registered webhook subscription by its id. Returns an empty object on success.</td></tr><tr><td>Get Contact</td><td><code>getContact</code></td><td>Get a single contact by id, including profile, channels, and notes.</td></tr><tr><td>Get Ticket</td><td><code>getTicket</code></td><td>Get a single ticket (conversation) by id.</td></tr></tbody></table>

<details>

<summary>View 22 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get User</td><td><code>getUser</code></td><td>Get a single user (agent) by id.</td></tr><tr><td>Get Webhook</td><td><code>getWebhook</code></td><td>Get a single registered webhook subscription by its id, including its title, target URL, event type and signing secret.</td></tr><tr><td>List Boards</td><td><code>listBoards</code></td><td>List all boards (kanban-style task boards) in the Trengo account.</td></tr><tr><td>List Business Hours</td><td><code>listBusinessHours</code></td><td>List all business hours schedules configured in the Trengo account.</td></tr><tr><td>List Contact Groups</td><td><code>listContactGroups</code></td><td>List all contact groups in the Trengo account.</td></tr><tr><td>List Contacts</td><td><code>listContacts</code></td><td>List all contacts in the Trengo account.</td></tr><tr><td>List CSAT Ratings</td><td><code>listCsat</code></td><td>List customer satisfaction (CSAT) ratings collected in the Trengo account.</td></tr><tr><td>List Custom Fields</td><td><code>listCustomFields</code></td><td>List all custom fields defined for tickets, contacts, or profiles.</td></tr><tr><td>List Help Centers</td><td><code>listHelpCenters</code></td><td>List all help center articles/pages configured in the Trengo account.</td></tr><tr><td>List Labels</td><td><code>listLabels</code></td><td>List all labels available in the Trengo account.</td></tr><tr><td>List Profiles</td><td><code>listProfiles</code></td><td>List all profiles (merged contact identities) in the Trengo account.</td></tr><tr><td>List Quick Replies</td><td><code>listQuickReplies</code></td><td>List all quick replies (canned responses) in the Trengo account.</td></tr><tr><td>List SMS Messages</td><td><code>getSmsBalance</code></td><td>List all outbound SMS messages sent from the Trengo account.</td></tr><tr><td>List Teams</td><td><code>listTeams</code></td><td>List all teams in the Trengo account.</td></tr><tr><td>List Ticket Messages</td><td><code>listTicketMessages</code></td><td>List all messages within a ticket (conversation).</td></tr><tr><td>List Ticket Results</td><td><code>listTicketResults</code></td><td>List ticket results (outcome tags used when closing tickets).</td></tr><tr><td>List Tickets</td><td><code>listTickets</code></td><td>List tickets (conversations) in the Trengo account.</td></tr><tr><td>List Users</td><td><code>listUsers</code></td><td>List all users (agents) in the Trengo account. Supports pagination and sorting.</td></tr><tr><td>List Webhooks</td><td><code>listWebhooks</code></td><td>List all registered webhook subscriptions in the Trengo account.</td></tr><tr><td>Update Contact</td><td><code>updateContact</code></td><td>Update an existing contact's name.</td></tr><tr><td>Update Label</td><td><code>updateLabel</code></td><td>Update an existing label's name or color.</td></tr><tr><td>Update Webhook</td><td><code>updateWebhook</code></td><td>Update the name, target URL and event type of an existing webhook subscription. All three body fields are required by Trengo.</td></tr></tbody></table>

</details>

