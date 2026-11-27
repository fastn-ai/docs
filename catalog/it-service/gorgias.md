---
description: "Gorgias is a help desk for online stores. Create and read tickets, messages and customers, and manage integrations."
hidden: true
---

# Gorgias

<img src="../../.gitbook/assets/connectors/lg/gorgias.png" alt="Gorgias logo">

| | |
| --- | --- |
| **Category** | [IT and service management](README.md) |
| **Website** | [gorgias.com](https://gorgias.com) |
| **Authentication** | Username and password |
| **Slug** | `gorgias` |

## Setup

Your customers enter their username and password for Gorgias when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Gorgias from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Gorgias**.
2. Select **Connect** on the Gorgias card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Gorgias's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Customer</td><td><code>createCustomer</code></td><td>Create a customer. Requires a channels array.</td></tr><tr><td>Create Integration</td><td><code>createIntegration</code></td><td>Create an HTTP integration (outbound webhook) with event triggers.</td></tr><tr><td>Create Message</td><td><code>createMessage</code></td><td>Create a message on a ticket.</td></tr><tr><td>Create Ticket</td><td><code>createTicket</code></td><td>Create a ticket. Requires a messages array.</td></tr><tr><td>Delete Integration</td><td><code>deleteIntegration</code></td><td>Delete an HTTP integration (webhook) by id.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Get the current Gorgias account (use as whoami/test-connection).</td></tr><tr><td>Get Customer</td><td><code>getCustomer</code></td><td>Get a customer by id.</td></tr><tr><td>Get Ticket</td><td><code>getTicket</code></td><td>Get a ticket by id.</td></tr><tr><td>List Customers</td><td><code>listCustomers</code></td><td>List customers.</td></tr><tr><td>List Integrations</td><td><code>listIntegrations</code></td><td>List HTTP integrations (outbound webhooks).</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Messages</td><td><code>listMessages</code></td><td>List messages, optionally for a ticket.</td></tr><tr><td>List Tags</td><td><code>listTags</code></td><td>List tags.</td></tr><tr><td>List Tickets</td><td><code>listTickets</code></td><td>List tickets (cursor-paginated).</td></tr><tr><td>List Users</td><td><code>listUsers</code></td><td>List agents/users.</td></tr><tr><td>Update Customer</td><td><code>updateCustomer</code></td><td>Update a customer.</td></tr><tr><td>Update Ticket</td><td><code>updateTicket</code></td><td>Update a ticket (status, priority, assignee, tags, subject).</td></tr></tbody></table>

</details>

