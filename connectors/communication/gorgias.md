---
description: "Gorgias helpdesk connector: tickets, messages, customers, tags, users, account, and HTTP integration (webhook) management."
hidden: true
---

# Gorgias

<img src="../../.gitbook/assets/connectors/lg/gorgias.png" alt="Gorgias logo">

Gorgias helpdesk connector: tickets, messages, customers, tags, users, account, and HTTP integration (webhook) management. Subdomain-based (https://{subdomain}.gorgias.com/api). HTTP Basic auth (email + API key) primary.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [gorgias.com](https://gorgias.com) |
| **Authentication** | Basic auth |
| **Slug** | `gorgias` |

## Use it

Add Gorgias from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.gorgias.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Customer</td><td><code>createCustomer</code></td><td>Create a customer. Requires a channels array.</td></tr><tr><td>Create Integration</td><td><code>createIntegration</code></td><td>Create an HTTP integration (outbound webhook) with event triggers.</td></tr><tr><td>Create Message</td><td><code>createMessage</code></td><td>Create a message on a ticket.</td></tr><tr><td>Create Ticket</td><td><code>createTicket</code></td><td>Create a ticket. Requires a messages array.</td></tr><tr><td>Delete Integration</td><td><code>deleteIntegration</code></td><td>Delete an HTTP integration (webhook) by id.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Get the current Gorgias account (use as whoami/test-connection).</td></tr><tr><td>Get Customer</td><td><code>getCustomer</code></td><td>Get a customer by id.</td></tr><tr><td>Get Ticket</td><td><code>getTicket</code></td><td>Get a ticket by id.</td></tr><tr><td>List Customers</td><td><code>listCustomers</code></td><td>List customers.</td></tr><tr><td>List Integrations</td><td><code>listIntegrations</code></td><td>List HTTP integrations (outbound webhooks).</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Messages</td><td><code>listMessages</code></td><td>List messages, optionally for a ticket.</td></tr><tr><td>List Tags</td><td><code>listTags</code></td><td>List tags.</td></tr><tr><td>List Tickets</td><td><code>listTickets</code></td><td>List tickets (cursor-paginated).</td></tr><tr><td>List Users</td><td><code>listUsers</code></td><td>List agents/users.</td></tr><tr><td>Update Customer</td><td><code>updateCustomer</code></td><td>Update a customer.</td></tr><tr><td>Update Ticket</td><td><code>updateTicket</code></td><td>Update a ticket (status, priority, assignee, tags, subject).</td></tr></tbody></table>

</details>
