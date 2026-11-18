---
description: "Oracle Aconex construction project management REST API (XML responses): projects, project and global directory, own user, document register search, document…"
hidden: true
---

# Oracle Aconex

<img src="../../.gitbook/assets/connectors/lg/oracle-aconex.png" alt="Oracle Aconex logo">

Oracle Aconex construction project management REST API (XML responses): projects, project and global directory, own user, document register search, document metadata, schema and event log. Auth: Basic Auth with an Aconex login + Integration ID (X-Application-Key header) on the user's Aconex instance host. Lobby OAuth (https://constructionandengineering.oraclecloud.com, resource https://api.aconex.com) needs an OAuth client registered by an Aconex customer or Oracle partner and is not added yet.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [aconex.com](https://aconex.com) |
| **Authentication** | Basic auth |
| **Slug** | `oracleAconex` |

## Use it

Add Oracle Aconex from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.oracleAconex.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Get the connected Aconex user's own details (GET /api/user): UserId, username, name, email, organization. Good connection check.</td></tr><tr><td>Get Document Event Log</td><td><code>getDocumentEventLog</code></td><td>Get the event log (who viewed, changed, sent it and when) of a document family (GET /api/projects/{projectId}/register/{documentId}/eventlog).</td></tr><tr><td>Get Document Metadata</td><td><code>getDocumentMetadata</code></td><td>Get full metadata of one document (GET /api/projects/{projectId}/register/{documentId}/metadata).</td></tr><tr><td>Get Document Schema</td><td><code>getDocumentSchema</code></td><td>Get a project's document register schema (GET /api/projects/{projectId}/register/schema): the fields you can search, sort, return and the fields needed to register a document.</td></tr><tr><td>Get Mail</td><td><code>getMail</code></td><td>Get one mail's metadata and body (GET /api/projects/{projectId}/mail/{mailId}, Mail API v2).</td></tr><tr><td>Get Mail Schema</td><td><code>getMailSchema</code></td><td>Get a project's mail schema (GET /api/projects/{projectId}/mail/schema): searchable and returnable fields, mail types and fields needed to create mail.</td></tr><tr><td>Get Mail Thread</td><td><code>getMailThread</code></td><td>Get all mails in a thread (GET /api/projects/{projectId}/mail/{threadId}/thread).</td></tr><tr><td>Get Open Task Count</td><td><code>getTaskCount</code></td><td>Get the number of tasks for the connected user across projects (GET /api/tasks/count).</td></tr><tr><td>Get Organization</td><td><code>getOrganization</code></td><td>Get an organization's details (GET /api/organizations/{organizationId}). Use OrganizationId from Get Current User.</td></tr><tr><td>Get Project User</td><td><code>getProjectUser</code></td><td>Get one user's details as seen in a project directory (GET /api/projects/{projectId}/users/{userId}).</td></tr></tbody></table>

<details>

<summary>View 10 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Documents</td><td><code>listDocuments</code></td><td>Search a project's document register (GET /api/projects/{projectId}/register). search_query is Lucene (e.g. doctype:Drawing). return_fields picks fields (e.g. docno,title,revision,statusid). Use search_type PAGED with page_number and page_size.</td></tr><tr><td>List Mail</td><td><code>listMail</code></td><td>Search a project mailbox (GET /api/projects/{projectId}/mail, Mail API v2). mail_box is inbox, sentbox or draftbox. search_query is Lucene (e.g. corrtypeid:23). return_fields e.g. subject,fromuserfullname,sentdate,docno,corrtypeid. Use search_type PAGED with page_number and page_size.</td></tr><tr><td>List Organization Users</td><td><code>listOrganizationUsers</code></td><td>List users of an organization (GET /api/organizations/{organizationId}/users). Needs organization admin rights.</td></tr><tr><td>List Projects</td><td><code>listProjects</code></td><td>List the Aconex projects the connected user can access (GET /api/projects). Returns XML ProjectResults with ProjectId, ProjectName, status and dates. Use the ProjectId in other actions.</td></tr><tr><td>List Workflows</td><td><code>listWorkflows</code></td><td>List a project's document review workflows (GET /api/projects/{projectId}/workflows). Filter by update time; page_size is a multiple of 25.</td></tr><tr><td>Mark Mail As Read</td><td><code>markMailRead</code></td><td>Mark a mail as read for the connected user (PUT /api/projects/{projectId}/mail/{mailId}/markRead).</td></tr><tr><td>Mark Mail As Unread</td><td><code>markMailUnread</code></td><td>Mark a mail as unread for the connected user (PUT /api/projects/{projectId}/mail/{mailId}/markUnread).</td></tr><tr><td>Search Global Directory</td><td><code>searchGlobalDirectory</code></td><td>Search users in the Aconex global directory (GET /api/directory). Filters are optional wildcard matches; email is exact. Paged with page_number and page_size.</td></tr><tr><td>Search Project Directory</td><td><code>searchProjectDirectory</code></td><td>Search users and groups in one Aconex project's directory (GET /api/projects/{projectId}/directory). Filters are optional; set show_groups false to return users only.</td></tr><tr><td>Search Workflows By Number</td><td><code>searchWorkflows</code></td><td>Find workflows by number (GET /api/projects/{projectId}/workflows/search). workflow_number is a comma-separated list of up to 10, e.g. WF-000020,WF-000021.</td></tr></tbody></table>

</details>
