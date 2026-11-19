---
description: "Looker Studio (formerly Google Data Studio) — the Data Studio REST API v1 (https://datastudio.googleapis.com/v1)."
hidden: true
---

# Looker Studio

<img src="../../.gitbook/assets/connectors/lg/looker-studio.png" alt="Looker Studio logo">

This is Google's free BI/dashboarding tool, distinct from the enterprise Looker BI platform. Public REST surface is narrow (asset discovery + permission management only; no report/data-source CRUD is exposed): search Data Studio assets (REPORT, DATA_SOURCE) by title/owner/type, and get/patch/addMembers/revokeAllPermissions on an asset's sharing permissions. Report/page/chart authoring is only available via the Linking API (URL-based, not REST) and the Embed API (iframe embedding), not general REST endpoints. Auth: OAuth 2.0 (Google), shared org OAuth client, scope https://www.googleapis.com/auth/datastudio. API requires the connected account to belong to a Google Workspace or Cloud Identity org.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [lookerstudio.google.com](https://lookerstudio.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `lookerStudio` |

## Use it

Add Looker Studio from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.lookerStudio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Permission Members</td><td><code>addPermissionMembers</code></td><td>Adds members to a role on a Looker Studio asset's permissions. Members cannot be added to the OWNER role. POST https://datastudio.googleapis.com/v1/assets/{assetName}/permissions:addMembers</td></tr><tr><td>Get Asset Permissions</td><td><code>getAssetPermissions</code></td><td>Gets the sharing permissions for a Looker Studio asset (report or data source). Returns a map of role (OWNER/EDITOR/VIEWER) to member list plus an etag for concurrency control. GET https://datastudio.googleapis.com/v1/assets/{assetName}/permissions</td></tr><tr><td>Revoke All Permissions</td><td><code>revokeAllPermissions</code></td><td>Removes the given members from all roles on a Looker Studio asset. Owners and the authorized user cannot be removed. Always returns 200 OK, even if a member is invalid or does not belong to the asset. POST https://datastudio.googleapis.com/v1/assets/{assetName}/permissions:revokeAllPermissions</td></tr><tr><td>Search Assets</td><td><code>searchAssets</code></td><td>Searches the caller's Looker Studio (Data Studio) assets — reports and data sources. Exactly one assetTypes value must be specified per request. Supports title/description search, owner filter, trashed filter, sorting, and pagination. GET https://datastudio.googleapis.com/v1/assets:search</td></tr><tr><td>Update Asset Permissions</td><td><code>updateAssetPermissions</code></td><td>Updates (replaces) sharing permissions for a Looker Studio asset. Wiring verified live: auth, URL, and JSON body reach the real API (confirmed via an empty {"permissions":{}} body returning the same 404-no-asset as the other permission actions). KNOWN PLATFORM QUIRK: Google's published reference (developers.google.com/data-studio/integrate/api/reference/types) documents the body as {"permissions":{"EDITOR":{"members":[...]}},"etag":...} with role names as literal map keys, but the live datastudio.googleapis.com endpoint rejects every role-keyed variant tried (EDITOR, editor, editors, roles wrapper, array-of-{role,members}) with 400 "Unknown name ... Cannot find field" / "Proto field is not repeating". Live schema no longer matches its own docs - a Google doc/API drift on this legacy API, not a connector defect. PATCH https://datastudio.googleapis.com/v1/assets/{assetName}/permissions</td></tr></tbody></table>
