---
description: "Oracle Aconex construction project management REST API (XML responses): projects, project and global directory, own user, document register search, document…"
---

# Oracle Aconex

Oracle Aconex construction project management REST API (XML responses): projects, project and global directory, own user, document register search, document metadata, schema and event log. Auth: Basic Auth with an Aconex login + Integration ID (X-Application-Key header) on the user's Aconex instance host. Lobby OAuth (https://constructionandengineering.oraclecloud.com, resource https://api.aconex.com) needs an OAuth client registered by an Aconex customer or Oracle partner and is not added yet.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [aconex.com](https://aconex.com) |
| **Authentication** | Basic auth |
| **Actions** | 20 |
| **Events** | 0 |
| **Slug** | `oracleAconex` |

## Use it

Add Oracle Aconex from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.oracleAconex.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Current User | `getCurrentUser` | Get the connected Aconex user's own details (GET /api/user): UserId, username, name, email, organization. Good connection check. |
| Get Document Event Log | `getDocumentEventLog` | Get the event log (who viewed, changed, sent it and when) of a document family (GET /api/projects/{projectId}/register/{documentId}/eventlog). |
| Get Document Metadata | `getDocumentMetadata` | Get full metadata of one document (GET /api/projects/{projectId}/register/{documentId}/metadata). |
| Get Document Schema | `getDocumentSchema` | Get a project's document register schema (GET /api/projects/{projectId}/register/schema): the fields you can search, sort, return and the fields needed to register a document. |
| Get Mail | `getMail` | Get one mail's metadata and body (GET /api/projects/{projectId}/mail/{mailId}, Mail API v2). |
| Get Mail Schema | `getMailSchema` | Get a project's mail schema (GET /api/projects/{projectId}/mail/schema): searchable and returnable fields, mail types and fields needed to create mail. |
| Get Mail Thread | `getMailThread` | Get all mails in a thread (GET /api/projects/{projectId}/mail/{threadId}/thread). |
| Get Open Task Count | `getTaskCount` | Get the number of tasks for the connected user across projects (GET /api/tasks/count). |
| Get Organization | `getOrganization` | Get an organization's details (GET /api/organizations/{organizationId}). Use OrganizationId from Get Current User. |
| Get Project User | `getProjectUser` | Get one user's details as seen in a project directory (GET /api/projects/{projectId}/users/{userId}). |
| List Documents | `listDocuments` | Search a project's document register (GET /api/projects/{projectId}/register). search_query is Lucene (e.g. doctype:Drawing). return_fields picks fields (e.g. docno,title,revision,statusid). Use search_type PAGED with page_number and page_size. |
| List Mail | `listMail` | Search a project mailbox (GET /api/projects/{projectId}/mail, Mail API v2). mail_box is inbox, sentbox or draftbox. search_query is Lucene (e.g. corrtypeid:23). return_fields e.g. subject,fromuserfullname,sentdate,docno,corrtypeid. Use search_type PAGED with page_number and page_size. |
| List Organization Users | `listOrganizationUsers` | List users of an organization (GET /api/organizations/{organizationId}/users). Needs organization admin rights. |
| List Projects | `listProjects` | List the Aconex projects the connected user can access (GET /api/projects). Returns XML ProjectResults with ProjectId, ProjectName, status and dates. Use the ProjectId in other actions. |
| List Workflows | `listWorkflows` | List a project's document review workflows (GET /api/projects/{projectId}/workflows). Filter by update time; page_size is a multiple of 25. |
| Mark Mail As Read | `markMailRead` | Mark a mail as read for the connected user (PUT /api/projects/{projectId}/mail/{mailId}/markRead). |
| Mark Mail As Unread | `markMailUnread` | Mark a mail as unread for the connected user (PUT /api/projects/{projectId}/mail/{mailId}/markUnread). |
| Search Global Directory | `searchGlobalDirectory` | Search users in the Aconex global directory (GET /api/directory). Filters are optional wildcard matches; email is exact. Paged with page_number and page_size. |
| Search Project Directory | `searchProjectDirectory` | Search users and groups in one Aconex project's directory (GET /api/projects/{projectId}/directory). Filters are optional; set show_groups false to return users only. |
| Search Workflows By Number | `searchWorkflows` | Find workflows by number (GET /api/projects/{projectId}/workflows/search). workflow_number is a comma-separated list of up to 10, e.g. WF-000020,WF-000021. |
