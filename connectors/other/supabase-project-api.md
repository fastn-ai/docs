---
description: "Supabase project data-plane API (https://<projectRef>.supabase.co): PostgREST table CRUD + RPC, Storage buckets/objects, and Auth Admin user management."
---

# Supabase

Supabase project data-plane API (https://&lt;projectRef&gt;.supabase.co): PostgREST table CRUD + RPC, Storage buckets/objects, and Auth Admin user management. Authenticates with the project reference + secret/service_role key. Management API operations (edge functions, SQL/DDL, project config) live in the separate supabaseManagementApi connector.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [supabase.co](https://supabase.co) |
| **Authentication** | Credentials you enter |
| **Actions** | 38 |
| **Events** | 3 |
| **Slug** | `supabaseProjectApi` |

## Use it

Add Supabase from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.supabaseProjectApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Call RPC | `callRpc` | Call a Postgres stored function (RPC) exposed via the Data API. Pass the function name and an args JSON object string (use '{}' for no-arg functions). |
| Copy Object | `copyObject` | Copy an object to a new path within or across buckets. |
| Create Bucket | `createBucket` | Create a new storage bucket. |
| Create Signed URL | `createSignedUrl` | Create a time-limited signed URL to download a private object. |
| Create SSO Provider (Auth Admin) | `createSsoProvider` | Auth Admin: register a new SAML SSO identity provider. Provide the IdP metadata URL (or use metadata XML via metadata_url alternative). Requires SAML SSO enabled (paid plans). |
| Create User | `createUser` | Create a new user via Auth Admin. Can auto-confirm email/phone and attach metadata. |
| Delete Bucket | `deleteBucket` | Delete a storage bucket. The bucket must be empty first (use Empty Bucket). |
| Delete Object | `deleteObject` | Delete one or more objects from a bucket by exact path. Uses the Storage bulk-delete endpoint. |
| Delete Rows | `deleteRows` | Delete rows matching a filter (filterColumn + operator + filterValue, REQUIRED to avoid deleting every row). Returns the deleted rows. |
| Delete SSO Provider (Auth Admin) | `deleteSsoProvider` | Auth Admin: remove a SAML SSO provider by ID. Requires SAML SSO enabled (paid plans). |
| Delete User | `deleteUser` | Delete an auth user by id. Optionally soft-delete. |
| Delete User MFA Factor | `deleteUserFactor` | Auth Admin: delete (unenroll) an MFA factor from a user. |
| Download Object | `downloadObject` | Download an object's contents from a bucket (authenticated). |
| Empty Bucket | `emptyBucket` | Delete all objects in a storage bucket without deleting the bucket itself. |
| Generate Link | `generateLink` | Generate an action link (signup, magiclink, recovery, invite, email change) for a user via Auth Admin. |
| Get Auth Audit Log | `getAuthAuditLog` | Auth Admin: retrieve the authentication audit log (sign-ins, sign-ups, token refreshes, user modifications). Paginated. |
| Get Auth Settings | `getAuthSettings` | Get the public auth settings for the project (enabled providers, signup config). |
| Get Bucket | `getBucket` | Get details of a single storage bucket by id. |
| Get Object Info | `getObjectInfo` | Get metadata about an object (size, mimetype, etag, last modified) without downloading it. |
| Get SSO Provider (Auth Admin) | `getSsoProvider` | Auth Admin: get a single SAML SSO provider by ID. Requires SAML SSO enabled (paid plans). |
| Get User | `getUser` | Get a single auth user by their user id. |
| Insert Rows | `insertRows` | Insert one or more rows into a table via the PostgREST Data API. Pass the row(s) as a JSON string — either a single object {\"col\":\"val\"} or an array of objects. Returns the inserted rows. |
| Invite User by Email | `inviteUser` | Auth Admin: invite a new user by email. Creates the user and sends an invite email with a magic link. |
| List Buckets | `listBuckets` | List all storage buckets in the project. |
| List Objects | `listObjects` | List objects in a bucket, optionally filtered by a path prefix. |
| List SSO Providers (Auth Admin) | `listSsoProviders` | Auth Admin: list all SAML SSO providers configured on the project's auth server. Requires SAML SSO to be enabled on the project (paid plans); returns 404/error if SAML is disabled. |
| List User MFA Factors | `listUserFactors` | Auth Admin: list all MFA factors registered for a user. |
| List Users | `listUsers` | List users in the project's auth system (Auth Admin). Supports pagination. |
| Move Object | `moveObject` | Move/rename an object within or across buckets. |
| Query Rows | `queryRows` | Query rows from a table or view via the PostgREST Data API. Supports column selection, ordering, limit and offset. Additional PostgREST filters (e.g. id=eq.5) can be appended as query params. |
| Update Bucket | `updateBucket` | Update a storage bucket's settings (public flag, size limit, allowed MIME types). |
| Update Rows | `updateRows` | Update rows matching a filter (filterColumn + operator + filterValue, REQUIRED to avoid updating every row). Pass the columns to set as a JSON object string. Returns the updated rows. |
| Update SSO Provider (Auth Admin) | `updateSsoProvider` | Auth Admin: update a SAML SSO provider's domains and/or metadata URL. Requires SAML SSO enabled (paid plans). |
| Update User | `updateUser` | Update an auth user by id (email, password, phone, metadata, ban duration). |
| Update User MFA Factor | `updateUserFactor` | Auth Admin: update an MFA factor's friendly name for a user. |
| Upload Object | `uploadObject` | Upload a text object to a bucket at the given path. For binary files use the storage SDK; this action sends UTF-8 text content. |
| Upsert Rows | `upsertRows` | Insert rows, updating existing ones on primary-key/unique conflict (merge-duplicates). Pass the row(s) as a JSON string (object or array of objects). Returns the affected rows. |
| Upsert Rows On Conflict | `upsertRowsOnConflict` | Upsert rows with explicit on_conflict columns. Returns the affected rows. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Row Deleted | `DELETE` | Fired by a Supabase Database Webhook when a row is deleted. 'old_record' holds the deleted row. |
| Row Inserted | `INSERT` | Fired by a Supabase Database Webhook when a row is inserted into the watched table. The payload's 'record' holds the new row. |
| Row Updated | `UPDATE` | Fired by a Supabase Database Webhook when a row is updated. 'record' is the new row, 'old_record' is the previous row. |
