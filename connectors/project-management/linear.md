---
description: "Linear issue tracking connector (GraphQL API) — issues (CRUD/search/archive), comments, projects & milestones, initiatives, teams, users, labels, cycles,…"
hidden: true
---

# Linear

<img src="../../.gitbook/assets/connectors/lg/linear.png" alt="Linear logo">

Linear issue tracking connector (GraphQL API) — issues (CRUD/search/archive), comments, projects & milestones, initiatives, teams, users, labels, cycles, workflow states, attachments, documents, customers & needs, favorites, reactions, plus webhook management (webhookCreate/Update/Delete). Single endpoint https://api.linear.app/graphql.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [linear.app](https://linear.app) |
| **Authentication** | API key |
| **Slug** | `linear` |

## Use it

Add Linear from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.linear.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Issue | `archiveIssue` | Archive an issue by id. Required: id. |
| Archive Project | `archiveProject` | Archive a project by id. Required: id. |
| Create Attachment | `createAttachment` | Create an attachment (link) on an issue. Required: issueId, title, url. Optional: subtitle, iconUrl, commentBody, metadata (reconciled at verify). |
| Create Comment | `createComment` | Create a comment on an issue. Required: issueId, body. |
| Create Customer | `createCustomer` | Create a customer. Required: name. Optional: domains, externalIds, ownerId, revenue, size, logoUrl, slackChannelId (reconciled at verify). Plan-gated. |
| Create Customer Need | `createCustomerNeed` | Create a customer need. Required: body. Optional: customerId, customerExternalId, issueId, projectId, attachmentUrl, priority (reconciled at verify). Plan-gated. |
| Create Document | `createDocument` | Create a document. Required: title. Optional: content, projectId, initiativeId, issueId, icon, color (reconciled at verify). At least one association (projectId/initiativeId/issueId) is typically required by the API. |
| Create Favorite | `createFavorite` | Create a favorite. Provide exactly ONE target id (issueId, projectId, documentId, cycleId, customViewId, etc). Required here: issueId is templated; for other target types use updateFavorite or reconcile at verify. |
| Create Initiative | `createInitiative` | Create an initiative. Required: name. Optional: description, content, ownerId, color, icon, targetDate, status (reconciled at verify). |
| Create Issue | `createIssue` | Create an issue. Required: teamId, title. Optional: description, priority, assigneeId, stateId, labelIds, projectId, cycleId, estimate, dueDate, parentId - each is sent only when provided. |

<details>

<summary>See 53 more actions</summary>

* **Create Issue Label** `createIssueLabel`: Create an issue label. Required: name. Optional: teamId, color, description, parentId, isGroup (reconciled at verify).
* **Create Project** `createProject`: Create a project. Required: name, teamIds (array of team ids). Optional: description, content, leadId, targetDate, startDate, memberIds, color, icon, labelIds — documented, reconciled at verify.
* **Create Project Milestone** `createProjectMilestone`: Create a project milestone. Required: projectId, name. Optional: description, targetDate, sortOrder (reconciled at verify).
* **Create Reaction** `createReaction`: Create an emoji reaction. Required: emoji, and one target id (commentId templated here; issueId/projectUpdateId via reconcile at verify).
* **Create Webhook** `createWebhook`: Register a webhook. Required: url, resourceTypes (array of entity-type strings e.g. ["Issue","Comment"]), allPublicTeams (true for org-wide). Optional: label, secret, teamId. Called by the webhook config subscription code.
* **Delete Attachment** `deleteAttachment`: Delete an attachment by id. Required: id.
* **Delete Comment** `deleteComment`: Delete a comment by id. Required: id.
* **Delete Customer** `deleteCustomer`: Delete a customer by id. Required: id. Plan-gated.
* **Delete Customer Need** `deleteCustomerNeed`: Delete a customer need by id. Required: id. Plan-gated.
* **Delete Document** `deleteDocument`: Delete a document by id. Required: id.
* **Delete Favorite** `deleteFavorite`: Delete a favorite by id. Required: id.
* **Delete Initiative** `deleteInitiative`: Delete an initiative by id. Required: id.
* **Delete Issue** `deleteIssue`: Delete (trash) an issue by id. Required: id.
* **Delete Issue Label** `deleteIssueLabel`: Delete an issue label by id. Required: id.
* **Delete Project** `deleteProject`: Delete (trash) a project by id. Required: id.
* **Delete Project Milestone** `deleteProjectMilestone`: Delete a project milestone by id. Required: id.
* **Delete Reaction** `deleteReaction`: Delete a reaction by id. Required: id.
* **Delete Webhook** `deleteWebhook`: Delete a webhook by id. Required: id. Called by the webhook config unsubscription code.
* **Get Cycle** `getCycle`: Fetch a single cycle by id. Required: id.
* **Get Document** `getDocument`: Fetch a single document by id. Required: id.
* **Get Initiative** `getInitiative`: Fetch a single initiative by id. Required: id.
* **Get Issue** `getIssue`: Fetch a single issue by id (UUID or identifier like LIN-123). Required: id.
* **Get Organization** `getOrganization`: Fetch the workspace organization. No inputs.
* **Get Project** `getProject`: Fetch a single project by id. Required: id.
* **Get Team** `getTeam`: Fetch a single team by id. Required: id.
* **Get User** `getUser`: Fetch a single user by id. Required: id.
* **Get Viewer** `getViewer`: Fetch the current authenticated user (viewer) and their organization. No inputs. Good first validation call.
* **List Comments** `listComments`: List comments (paginated). Required: first (page size).
* **List Customer Needs** `listCustomerNeeds`: List customer needs (paginated). Required: first. Plan-gated.
* **List Customers** `listCustomers`: List customers (paginated). Required: first. Plan-gated — may return an errors envelope on plans without Customer Requests; classified at verify.
* **List Cycles** `listCycles`: List cycles (paginated). Required: first.
* **List Documents** `listDocuments`: List documents (paginated). Required: first.
* **List Favorites** `listFavorites`: List the viewer's favorites (paginated). Required: first.
* **List Initiatives** `listInitiatives`: List initiatives (paginated). Required: first.
* **List Issue Labels** `listIssueLabels`: List issue labels (paginated). Required: first.
* **List Issues** `listIssues`: List issues (paginated). Required: first (page size, default 50). Returns issue nodes plus pageInfo for cursor pagination.
* **List Issues (Paged)** `listIssuesPaged`: List issues newest-first with real cursor pagination. Pass first (page size) and optionally after (pageInfo.endCursor from the previous page). Returns issue nodes with state, team, assignee, creator, priority and timestamps, plus pageInfo { hasNextPage endCursor }.
* **List Project Milestones** `listProjectMilestones`: List project milestones (paginated). Required: first.
* **List Projects** `listProjects`: List projects (paginated). Required: first.
* **List Teams** `listTeams`: List teams (paginated). Required: first.
* **List Users** `listUsers`: List workspace users (paginated). Required: first.
* **List Webhooks** `listWebhooks`: List webhooks registered in the workspace (paginated). Required: first.
* **List Workflow States** `listWorkflowStates`: List workflow states (paginated). Required: first.
* **Run GraphQL Query** `runGraphqlQuery`: Run any Linear GraphQL query or mutation with variables. Use it for fields or operations the other actions do not cover. Returns Linear's raw response ({data, errors}).
* **Search Issues** `searchIssues`: Full-text search for issues by term. Required: term, first (page size).
* **Update Comment** `updateComment`: Update a comment body. Required: id, body.
* **Update Document** `updateDocument`: Update a document. Required: id, title. Optional: content, icon, color, projectId (reconciled at verify).
* **Update Initiative** `updateInitiative`: Update an initiative. Required: id, name. Optional: description, content, ownerId, color, targetDate, status (reconciled at verify).
* **Update Issue** `updateIssue`: Update an issue. Required: id. Optional: title, description, priority, assigneeId, stateId, projectId, cycleId, estimate, dueDate, addedLabelIds, labelIds - only the fields provided are sent; others are left unchanged.
* **Update Issue Label** `updateIssueLabel`: Update an issue label. Required: id, name. Optional: color, description, parentId (reconciled at verify).
* **Update Project** `updateProject`: Update a project. Required: id, name (templated). Other fields (description, content, state, leadId, targetDate, startDate, color, icon) documented optional, reconciled at verify.
* **Update Project Milestone** `updateProjectMilestone`: Update a project milestone. Required: id, name. Optional: description, targetDate, sortOrder (reconciled at verify).
* **Update Webhook** `updateWebhook`: Update a webhook. Required: id, enabled. Optional: url, resourceTypes, label, secret. Used for resubscription (re-enable a disabled webhook).

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Attachment | `Attachment` | Attachment created, updated, or removed. The 'action' field distinguishes the operation; 'data' holds the attachment. |
| Comment | `Comment` | Comment created, updated, or removed. The 'action' field (create\|update\|remove) distinguishes the operation; 'data' holds the comment. |
| Customer | `Customer` | Customer created, updated, or removed (plan-gated). The 'action' field distinguishes the operation; 'data' holds the customer. |
| Customer Need | `CustomerNeed` | Customer need created, updated, or removed (plan-gated). The 'action' field distinguishes the operation; 'data' holds the customer need. |
| Cycle | `Cycle` | Cycle created or updated. The 'action' field distinguishes create\|update; 'data' holds the cycle. |
| Document | `Document` | Document created, updated, or removed. The 'action' field distinguishes the operation; 'data' holds the document. |
| Initiative | `Initiative` | Initiative created, updated, or removed. The 'action' field distinguishes the operation; 'data' holds the initiative. |
| Issue | `Issue` | Issue created, updated, or removed. The payload's 'action' field (create\|update\|remove) distinguishes the operation; 'data' holds the issue. |
| Issue Label | `IssueLabel` | Issue label created, updated, or removed. The 'action' field distinguishes the operation; 'data' holds the label. |
| Project | `Project` | Project created, updated, or removed. The 'action' field distinguishes the operation; 'data' holds the project. |

<details>

<summary>See 2 more events</summary>

* **Project Update** `ProjectUpdate`: Project status update created or updated. The 'action' field distinguishes create|update; 'data' holds the project update.
* **Reaction** `Reaction`: Reaction created or removed. The 'action' field distinguishes create|remove; 'data' holds the reaction.

</details>
