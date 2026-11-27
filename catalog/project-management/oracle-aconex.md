---
description: "Oracle Aconex is a construction project management platform. Read projects, users, organizations, document metadata and event logs, and mail threads."
hidden: true
---

# Oracle Aconex

<img src="../../.gitbook/assets/connectors/lg/oracle-aconex.png" alt="Oracle Aconex logo">

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [aconex.com](https://aconex.com) |
| **Authentication** | Username and password |
| **Slug** | `oracleAconex` |

## Setup

Your customers enter their username and password for Oracle Aconex when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Oracle Aconex from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Oracle Aconex**.
2. Select **Connect** on the Oracle Aconex card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Oracle Aconex's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Get the connected Aconex user's own details: UserId, username, name, email, organization. Good connection check.</td></tr><tr><td>Get Document Event Log</td><td><code>getDocumentEventLog</code></td><td>Get the event log (who viewed, changed, sent it and when) of a document family</td></tr><tr><td>Get Document Metadata</td><td><code>getDocumentMetadata</code></td><td>Get full metadata of one document</td></tr><tr><td>Get Document Schema</td><td><code>getDocumentSchema</code></td><td>Get a project's document register schema: the fields you can search, sort, return and the fields needed to register a document.</td></tr><tr><td>Get Mail</td><td><code>getMail</code></td><td>Get one mail's metadata and body, Mail API v2).</td></tr><tr><td>Get Mail Schema</td><td><code>getMailSchema</code></td><td>Get a project's mail schema: searchable and returnable fields, mail types and fields needed to create mail.</td></tr><tr><td>Get Mail Thread</td><td><code>getMailThread</code></td><td>Get all mails in a thread</td></tr><tr><td>Get Open Task Count</td><td><code>getTaskCount</code></td><td>Get the number of tasks for the connected user across projects</td></tr><tr><td>Get Organization</td><td><code>getOrganization</code></td><td>Get an organization's details Use OrganizationId from Get Current User.</td></tr><tr><td>Get Project User</td><td><code>getProjectUser</code></td><td>Get one user's details as seen in a project directory</td></tr></tbody></table>

<details>

<summary>View 10 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Documents</td><td><code>listDocuments</code></td><td>Search a project's document register search_query is Lucene (e.g. doctype:Drawing). return_fields picks fields (e.g. docno,title,revision,statusid). Use search_type PAGED with page_number and page_size.</td></tr><tr><td>List Mail</td><td><code>listMail</code></td><td>Search a project mailbox, Mail API v2). mail_box is inbox, sentbox or draftbox. search_query is Lucene (e.g. corrtypeid:23). return_fields e.g. subject,fromuserfullname,sentdate,docno,corrtypeid. Use search_type PAGED with page_number and page_size.</td></tr><tr><td>List Organization Users</td><td><code>listOrganizationUsers</code></td><td>List users of an organization Needs organization admin rights.</td></tr><tr><td>List Projects</td><td><code>listProjects</code></td><td>List the Aconex projects the connected user can access Returns XML ProjectResults with ProjectId, ProjectName, status and dates. Use the ProjectId in other actions.</td></tr><tr><td>List Workflows</td><td><code>listWorkflows</code></td><td>List a project's document review workflows Filter by update time; page_size is a multiple of 25.</td></tr><tr><td>Mark Mail As Read</td><td><code>markMailRead</code></td><td>Mark a mail as read for the connected user</td></tr><tr><td>Mark Mail As Unread</td><td><code>markMailUnread</code></td><td>Mark a mail as unread for the connected user</td></tr><tr><td>Search Global Directory</td><td><code>searchGlobalDirectory</code></td><td>Search users in the Aconex global directory Filters are optional wildcard matches; email is exact. Paged with page_number and page_size.</td></tr><tr><td>Search Project Directory</td><td><code>searchProjectDirectory</code></td><td>Search users and groups in one Aconex project's directory Filters are optional; set show_groups false to return users only.</td></tr><tr><td>Search Workflows By Number</td><td><code>searchWorkflows</code></td><td>Find workflows by number workflow_number is a comma-separated list of up to 10, e.g. WF-000020,WF-000021.</td></tr></tbody></table>

</details>

