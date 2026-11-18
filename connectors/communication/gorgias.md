---
description: "Gorgias helpdesk connector: tickets, messages, customers, tags, users, account, and HTTP integration (webhook) management."
---

# Gorgias

Gorgias helpdesk connector: tickets, messages, customers, tags, users, account, and HTTP integration (webhook) management. Subdomain-based (https://{subdomain}.gorgias.com/api). HTTP Basic auth (email + API key) primary.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [gorgias.com](https://gorgias.com) |
| **Authentication** | Basic auth |
| **Actions** | 16 |
| **Events** | 0 |
| **Slug** | `gorgias` |

## Use it

Add Gorgias from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.gorgias.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Customer | `createCustomer` | Create a customer. Requires a channels array. |
| Create Integration | `createIntegration` | Create an HTTP integration (outbound webhook) with event triggers. |
| Create Message | `createMessage` | Create a message on a ticket. |
| Create Ticket | `createTicket` | Create a ticket. Requires a messages array. |
| Delete Integration | `deleteIntegration` | Delete an HTTP integration (webhook) by id. |
| Get Account | `getAccount` | Get the current Gorgias account (use as whoami/test-connection). |
| Get Customer | `getCustomer` | Get a customer by id. |
| Get Ticket | `getTicket` | Get a ticket by id. |
| List Customers | `listCustomers` | List customers. |
| List Integrations | `listIntegrations` | List HTTP integrations (outbound webhooks). |
| List Messages | `listMessages` | List messages, optionally for a ticket. |
| List Tags | `listTags` | List tags. |
| List Tickets | `listTickets` | List tickets (cursor-paginated). |
| List Users | `listUsers` | List agents/users. |
| Update Customer | `updateCustomer` | Update a customer. |
| Update Ticket | `updateTicket` | Update a ticket (status, priority, assignee, tags, subject). |
