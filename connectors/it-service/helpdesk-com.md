---
description: "HelpDesk.com is a ticketing and customer support platform from Text (LiveChat)."
hidden: true
---

# HelpDesk.com

<img src="../../.gitbook/assets/connectors/lg/helpdesk-com.png" alt="HelpDesk.com logo">

HelpDesk.com is a ticketing and customer support platform from Text (LiveChat). This connector wraps the full HelpDesk.com REST API v1: tickets and ticket events, transactions and attachments, agents, teams, tags, views, macros, rules, canned responses, templates, custom fields, mailboxes, licenses, email domains, reply addresses, trusted and blocked emails, subscriptions, imported tickets, the audit log, webhooks and the full reporting suite.

| | |
| --- | --- |
| **Category** | [IT and service management](README.md) |
| **Website** | [helpdesk.com](https://helpdesk.com) |
| **Authentication** | Basic auth |
| **Slug** | `helpdeskCom` |

## Use it

Add HelpDesk.com from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.helpdeskCom.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Followers to Ticket | `ticketUpdateAddFollower` | Add one or more agents as followers of a HelpDesk.com ticket so they are notified about its activity. |
| Add Tags to Ticket | `ticketUpdateAddTag` | Add one or more existing tags to a HelpDesk.com ticket without replacing the tags already on it. |
| Batch Update Agents | `agentUpdateBatch` | Apply the same set of field changes to several HelpDesk.com agents at once, identified by their agent identifiers. |
| Batch Update Teams | `teamUpdateBatch` | Apply the same set of field changes to several HelpDesk.com teams at once, identified by their team identifiers. |
| Block Email | `blockedEmailsCreate` | Block an email address or whole domain so its messages no longer create tickets. |
| Create Agent | `agentCreate` | Invite a new agent to the HelpDesk.com account with the given email address, roles and optional profile details. |
| Create Canned Response | `cannedResponsesCreate` | Create a canned response that agents can insert into a ticket reply using one of its shortcuts. |
| Create Contact Form | `contactFormsCreate` | Create an embeddable contact form whose submissions become tickets on the chosen team. |
| Create Custom Field | `customFieldsCreate` | Create a ticket custom field. The API key you choose is how the field is addressed in the customFields object on a ticket. |
| Create Custom Report | `reportsCreate` | Generate a raw ticket export for a date range and email the recipients a link to the resulting CSV file. |

<details>

<summary>See 135 more actions</summary>

* **Create Email Domain** `emailDomainsCreate`: Register an email domain for outgoing replies. Supplying only a prefix creates a hosted prefix.helpdesk.com domain; supplying a full domain triggers ownership verification against a CNAME record during the call.
* **Create Imported Ticket** `importedTicketsCreate`: Import a historical ticket from another helpdesk, including its past events with their original timestamps.
* **Create Imported Ticket Transaction** `importedTicketsTransactionCreate`: Open a transaction that attachments for an imported ticket are uploaded into before the ticket itself is imported.
* **Create Integration** `integrationsCreate`: Connect a Shopify store or an OpenWidget installation to the HelpDesk.com account. The body is polymorphic: an OpenWidget integration takes only the type, while a Shopify integration also requires the store identifier and its settings.
* **Create License** `licensesCreate`: Provision a new HelpDesk.com license (account) on the given billing plan. This starts a paid subscription, so use it only in a deliberate provisioning flow.
* **Create Macro** `macroCreate`: Create a macro that applies a fixed list of actions to a ticket, such as changing status or priority, assigning a team, adding tags or sending a message.
* **Create Mailbox** `mailboxesCreate`: Create a forwarding mailbox that routes incoming email to a team, and optionally auto-assigns an agent.
* **Create Reply Address** `replyAddressesCreate`: Create a reply address on a verified email domain, used as the From address on outgoing ticket replies.
* **Create Rule** `rulesCreate`: Create an automation rule that watches ticket conditions and performs actions such as assigning, tagging, changing status or sending a message.
* **Create Subscription** `subscriptionsCreate`: Start a billing subscription on the account for the given plan and number of agent seats. This is a paid action.
* **Create Tag** `tagsCreate`: Create a new ticket tag in the HelpDesk.com account and optionally scope it to a single team.
* **Create Team** `teamsCreate`: Create a new team in the HelpDesk.com account and optionally set its reply address, from name, default template and auto-assignment pool.
* **Create Template** `templatesCreate`: Create an email template used to wrap outgoing ticket messages, in raw HTML or visual-editor form.
* **Create Ticket** `ticketsCreate`: Create a ticket in HelpDesk.com on behalf of a requester, with a first message and optional assignment, tags, followers, teams and custom field values. The requester is emailed a copy of the ticket.
* **Create Transaction** `transactionsCreate`: Open a transaction that attachments are uploaded into before they are referenced by a ticket, agent avatar, template logo or canned response.
* **Create View** `viewCreate`: Create a saved ticket view from a set of ticket filters. Shared views are visible to every agent and may only be created by administrators.
* **Create Webhook** `webhookCreate`: Register a webhook so HelpDesk.com posts the chosen ticket event to your URL. One webhook listens to exactly one event type.
* **Delete Agent** `agentDelete`: Remove an agent from the HelpDesk.com account. The agent loses access immediately and their tickets stay in the account.
* **Delete Canned Response** `cannedResponseDelete`: Permanently delete a canned response from the HelpDesk.com account.
* **Delete Contact Form** `contactFormDelete`: Delete a contact form so it can no longer be embedded or submitted.
* **Delete Custom Field** `customFieldDelete`: Permanently delete a ticket custom field from the HelpDesk.com account. Values already stored on tickets are removed with it.
* **Delete Email Domain** `emailDomainDelete`: Remove an email domain from the account. Accepts either the domain identifier or the domain name.
* **Delete Integration** `integrationDelete`: Disconnect a third-party integration from the HelpDesk.com account.
* **Delete Macro** `macroDelete`: Permanently delete a macro from the HelpDesk.com account.
* **Delete Mailbox** `mailboxDelete`: Delete a forwarding mailbox so email sent to it no longer creates tickets.
* **Delete Reply Address** `replyAddressDelete`: Delete a reply address so it is no longer used on outgoing ticket replies.
* **Delete Rule** `ruleDelete`: Permanently delete an automation rule from the HelpDesk.com account.
* **Delete Tag** `tagDelete`: Permanently delete a ticket tag from the HelpDesk.com account. The tag is removed from every ticket that carries it.
* **Delete Team** `teamDelete`: Permanently delete a team from the HelpDesk.com account. Tickets assigned to the team stay in the account and lose their team assignment.
* **Delete Template** `templateDelete`: Delete an email template from the account.
* **Delete Ticket** `ticketDelete`: Move a HelpDesk.com ticket to the trash silo. Use Move Ticket to Silo to restore it.
* **Delete Ticket Attachment** `ticketEventAttachmentDelete`: Remove a file attached to a message event on a ticket.
* **Delete Transaction Attachment** `transactionAttachmentDelete`: Remove a file that was uploaded into an attachment transaction.
* **Delete View** `viewDelete`: Permanently delete a saved ticket view from the HelpDesk.com account.
* **Delete Webhook** `webhookDelete`: Remove a registered webhook so HelpDesk.com stops posting that event. The webhook can be addressed by its identifier or by its name.
* **Get Agent** `agentsRead`: Retrieve a single HelpDesk.com agent by identifier, including roles, teams, signature and notification settings.
* **Get Audit Log** `auditLogList`: Return audit log events recording who created, updated or deleted configuration objects in the account, optionally narrowed by date range, action, target resource or author.
* **Get Billing** `billingGet`: Return the billing information for the HelpDesk.com account. This route is not in the vendor's published API reference but is live: it answers 403 {"error":{"type":"auth","message":"Insufficient privileges"}}, which is a privilege response rather than the router's plain-text 404, so the route exists. A Personal Access Token needs the billing privilege on the account before it returns data; without it every call is refused and no response shape is observable.
* **Get Canned Response** `cannedResponsesRead`: Retrieve a single canned response by its unique identifier.
* **Get Contact Form** `contactFormRead`: Retrieve a single contact form by its identifier, including all of its wording settings.
* **Get Custom Field** `customFieldsRead`: Retrieve a single ticket custom field by its unique identifier.
* **Get Email Domain** `emailDomainRead`: Retrieve a single email domain by its identifier, including verification status and expected DNS records.
* **Get Integration** `integrationRead`: Retrieve a single third-party integration by its identifier.
* **Get License** `licenseRead`: Retrieve a single HelpDesk.com license (account) by its numeric identifier.
* **Get Macro** `macroRead`: Retrieve a single HelpDesk.com macro by its unique identifier, including the actions it performs.
* **Get Mailbox** `mailboxRead`: Retrieve a single forwarding mailbox by its identifier.
* **Get Original Message Content** `ticketEventOriginalContentRead`: Return the original, unprocessed content of a message event on a ticket, before HelpDesk.com stripped quoting and signatures.
* **Get Reply Address** `replyAddressRead`: Retrieve a single reply address by its identifier.
* **Get Rule** `ruleRead`: Retrieve a single HelpDesk.com automation rule by its unique identifier.
* **Get Tag** `tagRead`: Retrieve a single HelpDesk.com ticket tag by its unique identifier.
* **Get Team** `teamRead`: Retrieve a single HelpDesk.com team by its unique identifier.
* **Get Template** `templateRead`: Retrieve a single email template by its identifier.
* **Get Ticket** `ticketRead`: Retrieve a single HelpDesk.com ticket by its unique identifier, including its full event history.
* **Get Transaction** `transactionRead`: Retrieve an attachment transaction and the files uploaded into it.
* **Get View** `viewRead`: Retrieve a single saved ticket view by its unique identifier.
* **Get Webhook** `webhookRead`: Retrieve a single registered webhook by its unique identifier.
* **List Agents** `agentsList`: List every agent in the HelpDesk.com account together with their roles, team memberships, status and notification settings.
* **List Blocked Emails** `blockedEmailsList`: List every email address or domain that is blocked from creating tickets.
* **List Canned Responses** `cannedResponsesList`: List every canned response in the HelpDesk.com account, including its shortcuts, body text and attachments.
* **List Contact Forms** `contactFormsList`: List the embeddable contact forms configured on the account, with the team they file tickets into and their wording.
* **List Custom Fields** `customFieldsList`: List every ticket custom field defined in the HelpDesk.com account with its API key, type and edit privileges.
* **List Email Domains** `emailDomainsList`: List the email domains registered on the account, with their verification status and the DNS records HelpDesk.com expects.
* **List Integrations** `integrationsList`: List the third-party integrations connected to the account, such as LiveChat, Shopify and OpenWidget.
* **List Licenses** `licensesList`: List the HelpDesk.com licenses (accounts) reachable with the current credentials, including their default team, default template and account settings.
* **List Macros** `macrosList`: List every macro in the HelpDesk.com account, including the actions each macro performs and the teams it is available to.
* **List Mailboxes** `mailboxesList`: List the forwarding mailboxes configured on the account, each routing incoming email to a team and optionally an agent.
* **List Reply Addresses** `replyAddressesList`: List the reply addresses configured on the account, each built from a prefix and a verified email domain.
* **List Rules** `rulesList`: List every automation rule in the HelpDesk.com account, including its triggers, actions, execution order and use counter.
* **List Subscriptions** `subscriptionsList`: List the billing subscriptions on the account, optionally narrowed to particular plan codes or a subscription state.
* **List Tags** `tagsList`: List every ticket tag defined in the HelpDesk.com account, including the team each tag belongs to and how many tickets currently use it.
* **List Teams** `teamsList`: List every team in the HelpDesk.com account with its reply address, default template and notification settings.
* **List Templates** `templatesList`: List the email templates that wrap outgoing ticket messages.
* **List Tickets** `ticketList`: List tickets in the HelpDesk.com account with optional filtering by status, priority, team, tags, requester, assignment, rating, silo and date ranges, plus cursor pagination.
* **List Trusted Emails** `trustedEmailsList`: List every email address or domain that is trusted, so messages from it never land in spam.
* **List Unsubscriptions** `unsubscriptionsList`: List requesters who unsubscribed from ticket notification emails, newest first.
* **List Views** `viewsList`: List every saved ticket view in the HelpDesk.com account together with the filters each view applies.
* **List Webhooks** `webhooksList`: List every webhook registered on the HelpDesk.com account with the event type each one listens to and the URL it posts to.
* **Merge Ticket** `ticketChildTicketAdd`: Merge another ticket into this one as a child ticket, so both conversations are handled together.
* **Move Ticket To Silo** `ticketSiloSet`: Move a ticket between the main ticket list, the archive, the trash and the spam folder.
* **Preview Template** `templatesPreview`: Render an email template with its appearance values applied and return the resulting text and HTML, without saving anything.
* **Remove Blocked Email** `blockedEmailDelete`: Unblock an email address or domain that was previously blocked.
* **Remove Follower from Ticket** `ticketUpdateRemoveFollower`: Stop notifying a single agent about a HelpDesk.com ticket by removing them from its followers.
* **Remove Tag from Ticket** `ticketUpdateRemoveTag`: Remove a single tag from a HelpDesk.com ticket. The tag itself is not deleted from the account.
* **Remove Trusted Email** `trustedEmailDelete`: Remove an email address or domain from the trusted list.
* **Report Agent Rating** `reportsAgentRating`: Return the ratings each agent received in each time bucket over the requested range.
* **Report Failed Emails** `reportsFailedEmails`: List outgoing emails that HelpDesk.com could not deliver, with the address and ticket involved.
* **Report New Tickets** `reportsNewTickets`: Return how many tickets were created in each time bucket over the requested range.
* **Report New Tickets By Hour** `reportsNewTickets24`: Return how many tickets were created in each hour of the day, aggregated across the requested range.
* **Report Rating Per Agent** `reportsRatingPerAgent`: Return the total ratings received, broken down per agent, over the requested range.
* **Report Rating Per Team** `reportsRatingPerTeam`: Return the total ratings received, broken down per team, over the requested range.
* **Report Resolution Time** `reportsResolutionTime`: Return how long tickets took to resolve, measured from creation and from assignment, in each time bucket.
* **Report Resolution Time By Hour** `reportsResolutionTime24`: Return how long tickets took to resolve, broken down by hour of the day.
* **Report Resolution Time Per Agent** `reportsResolutionTimePerAgent`: Return average resolution times, broken down per agent, over the requested range.
* **Report Resolution Time Per Team** `reportsResolutionTimePerTeam`: Return average resolution times, broken down per team, over the requested range.
* **Report Response Time** `reportsResponseTime`: Return how long tickets waited for assignment and for a first response, in each time bucket over the requested range.
* **Report Response Time By Hour** `reportsResponseTime24`: Return how long tickets waited for assignment and for a first response, broken down by hour of the day.
* **Report Response Time Per Agent** `reportsResponseTimePerAgent`: Return average assignment and first-response times, broken down per agent, over the requested range.
* **Report Response Time Per Team** `reportsResponseTimePerTeam`: Return average assignment and first-response times, broken down per team, over the requested range.
* **Report Status Duration** `reportsStatusDuration`: Return how long tickets spent in the open, pending and on-hold states in each time bucket over the requested range.
* **Report Status Duration Per Agent** `reportsStatusDurationPerAgent`: Return how long tickets spent in each state, broken down per agent, over the requested range.
* **Report Status Duration Per Team** `reportsStatusDurationPerTeam`: Return how long tickets spent in each state, broken down per team, over the requested range.
* **Report Ticket Rating** `reportsRating`: Return how requesters rated their tickets in each time bucket over the requested range.
* **Report Ticket Rating By Hour** `reportsRating24`: Return how requesters rated their tickets in each hour of the day, aggregated across the requested range.
* **Report Ticket Sources** `reportsTicketSources`: Return how many tickets arrived through each channel in each time bucket over the requested range.
* **Report Ticket Sources By Hour** `reportsTicketSources24`: Return how many tickets arrived through each channel in each hour of the day, aggregated across the requested range.
* **Report Ticket Status** `reportsStatus`: Return how many tickets were in the requested status in each time bucket over the requested range.
* **Report Ticket Status By Hour** `reportsStatus24`: Return how many tickets were in the requested status in each hour of the day, aggregated across the requested range.
* **Report Ticket Status Per Agent** `reportsStatusPerAgent`: Return how many tickets were in the requested status, broken down per agent, over the requested range.
* **Report Ticket Status Per Team** `reportsStatusPerTeam`: Return how many tickets were in the requested status, broken down per team, over the requested range.
* **Report Total Status Duration** `reportsStatusDurationTotal`: Return the total time tickets spent in the open, pending and on-hold states across the whole requested range.
* **Send Forwarding Instructions** `licenseForwardingInstructionsSend`: Email the mailbox forwarding setup instructions for a license to the given address.
* **Send Rating Request** `ticketRatingRequestSend`: Email the ticket requester asking them to rate the support they received.
* **Send Template Test Message** `templatesSendTestMessage`: Send a rendered preview of an email template to the given recipient addresses so the layout can be checked in a real inbox.
* **Test Email Forwarding** `forwardingEmailsTest`: Register an external address for forwarding verification and return the forwarding record HelpDesk.com created for it.
* **Trust Email** `trustedEmailsCreate`: Add an email address or whole domain to the trusted list so its messages are never treated as spam.
* **Unmerge Ticket** `ticketChildTicketRemove`: Detach a merged child ticket from its parent so it becomes an independent ticket again.
* **Update Agent** `agentUpdate`: Update a single HelpDesk.com agent. Only the fields supplied are changed; omitted fields keep their current values.
* **Update Canned Response** `cannedResponseUpdate`: Update a canned response. Only the fields supplied are changed; omitted fields keep their current values.
* **Update Contact Form** `contactFormUpdate`: Change the name, destination team, visibility or wording of a contact form. Only the fields supplied are changed.
* **Update Custom Field** `customFieldUpdate`: Update a ticket custom field. The API key and type of an existing field cannot be changed; only the label, teams, edit privileges and status.
* **Update Integration** `integrationUpdate`: Change the configuration of a connected third-party integration, such as the team its tickets are filed into.
* **Update License** `licenseUpdate`: Change account-wide settings on a license, such as the default team, the default email template and the company name shown to requesters.
* **Update Macro** `macroUpdate`: Update an existing HelpDesk.com macro. Only the fields supplied are changed; omitted fields keep their current values.
* **Update Mailbox** `mailboxUpdate`: Change the team and auto-assigned agent of a forwarding mailbox. HelpDesk.com requires both values together on every update.
* **Update Rule** `ruleUpdate`: Update a HelpDesk.com automation rule. Only the fields supplied are changed; omitted fields keep their current values.
* **Update Subscription** `subscriptionUpdate`: Change the plan, the number of agent seats or the coupon on an existing billing subscription. The plan code must be sent on every call even when unchanged. This changes what the account is charged.
* **Update Tag** `tagUpdate`: Update an existing HelpDesk.com ticket tag. Only the fields supplied are changed; omitted fields keep their current values.
* **Update Team** `teamUpdate`: Update a single HelpDesk.com team. Only the fields supplied are changed; omitted fields keep their current values.
* **Update Template** `templateUpdate`: Change the name, bodies or embedded logo of an email template. Only the fields supplied are changed.
* **Update Ticket** `ticketUpdate`: Update a HelpDesk.com ticket: change status, priority, subject, teams, requester, tags, followers, assignment or custom fields, add a new message, or apply macro actions. Only the fields supplied are changed.
* **Update View** `viewUpdate`: Update a saved ticket view. Only the fields supplied are changed; omitted fields keep their current values.
* **Update Webhook** `webhookUpdate`: Update a registered webhook. HelpDesk.com replaces the whole subscription, so the URL and event type must be supplied on every call even when unchanged. The webhook name is set at creation and cannot be changed here.
* **Upload Imported Ticket Attachment** `importedTicketsAttachmentsCreate`: Upload one text file into an imported-ticket transaction. Attachments must be uploaded here before an imported ticket that references them is created. The file is sent as a multipart/form-data part named attachments, alongside the transactionID part. Text content only: give the file's text in File Content and its name in File Name.
* **Upload Transaction Attachment** `transactionAttachmentUpload`: Upload one text file into an attachment transaction, so it can be referenced by a ticket, agent avatar, template logo or canned response. The file is sent as a multipart/form-data part named attachments. Text content only: give the file's text in File Content and its name in File Name.
* **Verify Email Domain** `emailDomainVerify`: Re-run ownership and DNS verification for an email domain and return its refreshed status.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Ticket Assignment Event | `tickets.events.assignment` | Fires when a ticket is reassigned to another team or agent. The payload carries both the ticket and the assignment event. |
| Ticket Created | `tickets.create` | Fires when a new ticket is created on the account. The payload carries the whole new ticket under payload. |
| Ticket Custom Fields Event | `tickets.events.customFields` | Fires when a ticket's custom field values change. The payload carries both the ticket and the custom fields event. |
| Ticket Followers Event | `tickets.events.followers` | Fires when a ticket's followers change. The payload carries both the ticket and the followers event. |
| Ticket Message Event | `tickets.events.message` | Fires when a new message is added to a ticket. The payload carries both the ticket and the message event. |
| Ticket Priority Event | `tickets.events.priority` | Fires when a ticket's priority changes. The payload carries both the ticket and the priority event. |
| Ticket Status Changed (Deprecated) | `tickets.statusChange` | Fires when a ticket's status changes. HelpDesk.com marks this event deprecated and recommends Ticket Status Event instead. |
| Ticket Status Event | `tickets.events.status` | Fires when a status event is appended to a ticket. The payload carries both the ticket and the event. |
| Ticket Tags Event | `tickets.events.tags` | Fires when a ticket's tags change. The payload carries both the ticket and the tags event. |
| Ticket Updated | `tickets.update` | Fires when any field of a ticket is modified. The payload carries the whole updated ticket under payload. |
