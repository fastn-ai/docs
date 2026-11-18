---
description: "Coda API (v1) connector — programmatically interact with Coda docs, pages, tables, columns, rows, formulas, controls, permissions (ACL), doc analytics, and…"
hidden: true
---

# Coda

<img src="../../.gitbook/assets/connectors/lg/coda.png" alt="Coda logo">

Coda API (v1) connector — programmatically interact with Coda docs, pages, tables, columns, rows, formulas, controls, permissions (ACL), doc analytics, and automation webhook triggers. Base: https://coda.io/apis/v1

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [coda.io](https://coda.io) |
| **Authentication** | Bearer token |
| **Slug** | `coda` |

## Use it

Add Coda from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.coda.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Permission (ACL) | `addPermission` | Adds a permission to the doc for a principal. The 'principal' object identifies who to share with: for an email principal use {"type": "email", "email": "user@domain.com"}; group/domain/workspace/anyone are also supported. |
| Begin Page Content Export | `beginPageContentExport` | Initiates an export of content for the given page as HTML or Markdown. Returns a requestId to poll for status. |
| Create Doc | `createDoc` | Creates a new Coda doc, optionally copying an existing source doc. |
| Create Page | `createPage` | Creates a new page in the specified doc. |
| Delete Doc | `deleteDoc` | Deletes the specified doc. |
| Delete Page | `deletePage` | Deletes the specified page. |
| Delete Permission (ACL) | `deletePermission` | Deletes a permission (revokes access) from the doc. |
| Delete Row | `deleteRow` | Deletes the specified row from the table. |
| Delete Rows | `deleteRows` | Deletes multiple rows by ID from the specified table. |
| Get ACL Settings | `getAclSettings` | Returns the ACL settings (e.g. comment/copy/share permission policies) of the specified doc. |
| Get Column | `getColumn` | Returns details about a column in a table. |
| Get Control | `getControl` | Returns info on a control in the doc, including its current value. |
| Get Doc | `getDoc` | Returns metadata for the specified doc. |
| Get Folder | `getFolder` | Returns details about a folder. |
| Get Formula | `getFormula` | Returns info on a named formula in the doc, including its computed value. |
| Get Mutation Status | `getMutationStatus` | Returns the status (completed or not) of an asynchronous mutation request, identified by the requestId returned from write operations. |
| Get Page | `getPage` | Returns details about a page in the specified doc. |
| Get Page Content Export Status | `getPageContentExportStatus` | Checks the status of a page content export and returns the download link when complete. |
| Get Permissions (ACL) | `getPermissions` | Returns a list of permissions (ACL) for the specified doc. |
| Get Row | `getRow` | Returns details about a row in a table. |
| Get Sharing Metadata (ACL) | `getSharingMetadata` | Returns metadata about the sharing permissions available for the doc (e.g. which access levels can be granted). |
| Get Table | `getTable` | Returns details about a specific table or view. |
| List Columns | `listColumns` | Returns a list of columns in the specified table. |
| List Controls | `listControls` | Returns a list of controls (buttons, sliders, etc.) in the specified doc. |
| List Doc Analytics | `listDocAnalytics` | Returns analytics data (views, users, etc.) for docs owned/managed by the user over a time range. |
| List Doc Analytics Summary | `listDocAnalyticsSummary` | Returns summarized analytics data for the user's docs. |
| List Docs | `listDocs` | Returns a list of Coda docs accessible by the user, with optional filtering by owner, published state, starred, gallery, workspace, or folder. |
| List Folders | `listFolders` | Returns a list of folders accessible by the user (workspace navigation). |
| List Formulas | `listFormulas` | Returns a list of named formulas in the specified doc. |
| List Page Analytics | `listPageAnalytics` | Returns analytics data for the pages within a specific doc over a time range. |
| List Page Content (Export) | `listPageContent` | Returns the content export request statuses / canvas content listing for a page. |
| List Pages | `listPages` | Returns a list of pages in the specified doc. |
| List Rows | `listRows` | Returns a list of rows in the specified table, with optional query filtering and value formatting. |
| List Tables | `listTables` | Returns a list of tables and views in the specified doc. |
| Publish Doc | `publishDoc` | Updates publication settings of, or publishes, the specified doc. The account must have a maker profile before it can publish. |
| Push Button | `pushButton` | Pushes a button on a row in a table, triggering the button's configured action. |
| Resolve Browser Link | `resolveBrowserLink` | Given a browser link to a Coda object, returns metadata about it (e.g. resolves to a doc/page/table). |
| Search Principals (ACL) | `searchPrincipals` | Searches for users and groups (principals) that can be added to a doc's ACL. |
| Trigger Webhook Automation | `triggerWebhookAutomation` | Triggers a webhook-invoked automation rule in a doc, passing an arbitrary JSON payload that the automation can reference. Use this to programmatically kick off Coda automations. |
| Unpublish Doc | `unpublishDoc` | Unpublishes the specified doc. |
| Update ACL Settings | `updateAclSettings` | Updates the ACL settings of the specified doc. |
| Update Doc | `updateDoc` | Updates metadata (title, icon) for the specified doc. |
| Update Page | `updatePage` | Updates properties of the specified page (name, subtitle, icon, image, hidden state). |
| Update Row | `updateRow` | Updates the specified row in the table. The 'row' object contains a 'cells' array of {column, value} objects. |
| Upsert Rows | `upsertRows` | Inserts rows and/or upserts rows into a table. Each row is an object with a 'cells' array of {column, value} objects. Pass keyColumns to upsert (update rows that match on those columns) instead of always inserting. |
| Who Am I | `whoami` | Returns the user associated with the API token, including name, login id, workspace, and scoped status. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Automation Webhook (Custom Payload) | `automation.webhook` | Generic webhook-invoked automation delivering an arbitrary JSON payload. Use this for any Coda automation whose action is 'Send a webhook' targeting the fastn URL, or as the catch-all for custom payloads pushed via the Trigger Webhook Automation action. |
| Button Pushed | `button.pushed` | A button in the doc was pushed, triggering an automation that posts to the fastn webhook URL. |
| Page Changed | `page.changed` | A page's content changed. Configured via a Coda page-change automation that posts to the fastn webhook URL. |
| Row Changed | `row.changed` | An existing row's values changed. Configured via a 'When a row changes' Coda automation that posts to the fastn webhook URL. |
| Row Created | `row.created` | A new row was added to a table. Configured in Coda via a 'When a row is added' automation that sends a webhook to the fastn URL. |
| Scheduled Time | `time.scheduled` | A time-based Coda automation fired on schedule and posted to the fastn webhook URL. |
