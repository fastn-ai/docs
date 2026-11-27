---
description: "Supabase is a hosted Postgres backend. Read and write table rows, call functions, manage storage buckets and auth users."
hidden: true
---

# Supabase

<img src="../../.gitbook/assets/connectors/lg/supabase-project-api.png" alt="Supabase logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [supabase.co](https://supabase.co) |
| **Authentication** | Project reference and service role key |
| **Slug** | `supabaseProjectApi` |

## Setup

Your customers enter their project reference and service role key for Supabase when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Supabase from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Supabase**.
2. Select **Connect** on the Supabase card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Supabase's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Call RPC</td><td><code>callRpc</code></td><td>Call a Postgres stored function (RPC) exposed via the Data API. Pass the function name and an args JSON object string (use '{}' for no-arg functions).</td></tr><tr><td>Copy Object</td><td><code>copyObject</code></td><td>Copy an object to a new path within or across buckets.</td></tr><tr><td>Create Bucket</td><td><code>createBucket</code></td><td>Create a new storage bucket.</td></tr><tr><td>Create Signed URL</td><td><code>createSignedUrl</code></td><td>Create a time-limited signed URL to download a private object.</td></tr><tr><td>Create SSO Provider (Auth Admin)</td><td><code>createSsoProvider</code></td><td>Auth Admin: register a new SAML SSO identity provider. Provide the IdP metadata URL (or use metadata XML via metadata_url alternative). Requires SAML SSO enabled (paid plans).</td></tr><tr><td>Create User</td><td><code>createUser</code></td><td>Create a new user via Auth Admin. Can auto-confirm email/phone and attach metadata.</td></tr><tr><td>Delete Bucket</td><td><code>deleteBucket</code></td><td>Delete a storage bucket. The bucket must be empty first (use Empty Bucket).</td></tr><tr><td>Delete Object</td><td><code>deleteObject</code></td><td>Delete one or more objects from a bucket by exact path. Uses the Storage bulk-delete endpoint.</td></tr><tr><td>Delete Rows</td><td><code>deleteRows</code></td><td>Delete rows matching a filter (filterColumn + operator + filterValue, REQUIRED to avoid deleting every row). Returns the deleted rows.</td></tr><tr><td>Delete SSO Provider (Auth Admin)</td><td><code>deleteSsoProvider</code></td><td>Auth Admin: remove a SAML SSO provider by ID. Requires SAML SSO enabled (paid plans).</td></tr></tbody></table>

<details>

<summary>View 28 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete User</td><td><code>deleteUser</code></td><td>Delete an auth user by id. Optionally soft-delete.</td></tr><tr><td>Delete User MFA Factor</td><td><code>deleteUserFactor</code></td><td>Auth Admin: delete (unenroll) an MFA factor from a user.</td></tr><tr><td>Download Object</td><td><code>downloadObject</code></td><td>Download an object's contents from a bucket (authenticated).</td></tr><tr><td>Empty Bucket</td><td><code>emptyBucket</code></td><td>Delete all objects in a storage bucket without deleting the bucket itself.</td></tr><tr><td>Generate Link</td><td><code>generateLink</code></td><td>Generate an action link (signup, magiclink, recovery, invite, email change) for a user via Auth Admin.</td></tr><tr><td>Get Auth Audit Log</td><td><code>getAuthAuditLog</code></td><td>Auth Admin: retrieve the authentication audit log (sign-ins, sign-ups, token refreshes, user modifications). Paginated.</td></tr><tr><td>Get Auth Settings</td><td><code>getAuthSettings</code></td><td>Get the public auth settings for the project (enabled providers, signup config).</td></tr><tr><td>Get Bucket</td><td><code>getBucket</code></td><td>Get details of a single storage bucket by id.</td></tr><tr><td>Get Object Info</td><td><code>getObjectInfo</code></td><td>Get metadata about an object (size, mimetype, etag, last modified) without downloading it.</td></tr><tr><td>Get SSO Provider (Auth Admin)</td><td><code>getSsoProvider</code></td><td>Auth Admin: get a single SAML SSO provider by ID. Requires SAML SSO enabled (paid plans).</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Get a single auth user by their user id.</td></tr><tr><td>Insert Rows</td><td><code>insertRows</code></td><td>Insert one or more rows into a table via the PostgREST Data API. Pass the row(s) as a JSON string — either a single object {\"col\":\"val\"} or an array of objects. Returns the inserted rows.</td></tr><tr><td>Invite User by Email</td><td><code>inviteUser</code></td><td>Auth Admin: invite a new user by email. Creates the user and sends an invite email with a magic link.</td></tr><tr><td>List Buckets</td><td><code>listBuckets</code></td><td>List all storage buckets in the project.</td></tr><tr><td>List Objects</td><td><code>listObjects</code></td><td>List objects in a bucket, optionally filtered by a path prefix.</td></tr><tr><td>List SSO Providers (Auth Admin)</td><td><code>listSsoProviders</code></td><td>Auth Admin: list all SAML SSO providers configured on the project's auth server. Requires SAML SSO to be enabled on the project (paid plans)</td></tr><tr><td>List User MFA Factors</td><td><code>listUserFactors</code></td><td>Auth Admin: list all MFA factors registered for a user.</td></tr><tr><td>List Users</td><td><code>listUsers</code></td><td>List users in the project's auth system (Auth Admin). Supports pagination.</td></tr><tr><td>Move Object</td><td><code>moveObject</code></td><td>Move/rename an object within or across buckets.</td></tr><tr><td>Query Rows</td><td><code>queryRows</code></td><td>Query rows from a table or view via the PostgREST Data API. Supports column selection, ordering, limit and offset. Additional PostgREST filters (e.g. id=eq.5) can be appended as query params.</td></tr><tr><td>Update Bucket</td><td><code>updateBucket</code></td><td>Update a storage bucket's settings (public flag, size limit, allowed MIME types).</td></tr><tr><td>Update Rows</td><td><code>updateRows</code></td><td>Update rows matching a filter (filterColumn + operator + filterValue, REQUIRED to avoid updating every row). Pass the columns to set as a JSON object string. Returns the updated rows.</td></tr><tr><td>Update SSO Provider (Auth Admin)</td><td><code>updateSsoProvider</code></td><td>Auth Admin: update a SAML SSO provider's domains and/or metadata URL. Requires SAML SSO enabled (paid plans).</td></tr><tr><td>Update User</td><td><code>updateUser</code></td><td>Update an auth user by id (email, password, phone, metadata, ban duration).</td></tr><tr><td>Update User MFA Factor</td><td><code>updateUserFactor</code></td><td>Auth Admin: update an MFA factor's friendly name for a user.</td></tr><tr><td>Upload Object</td><td><code>uploadObject</code></td><td>Upload a text object to a bucket at the given path. For binary files use the storage SDK; this action sends UTF-8 text content.</td></tr><tr><td>Upsert Rows</td><td><code>upsertRows</code></td><td>Insert rows, updating existing ones on primary-key/unique conflict (merge-duplicates). Pass the row(s) as a JSON string (object or array of objects). Returns the affected rows.</td></tr><tr><td>Upsert Rows On Conflict</td><td><code>upsertRowsOnConflict</code></td><td>Upsert rows with explicit on_conflict columns. Returns the affected rows.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Row Deleted</td><td><code>DELETE</code></td><td>Fired by a Supabase Database Webhook when a row is deleted. 'old_record' holds the deleted row.</td></tr><tr><td>Row Inserted</td><td><code>INSERT</code></td><td>Fired by a Supabase Database Webhook when a row is inserted into the watched table. The payload's 'record' holds the new row.</td></tr><tr><td>Row Updated</td><td><code>UPDATE</code></td><td>Fired by a Supabase Database Webhook when a row is updated. 'record' is the new row, 'old_record' is the previous row.</td></tr></tbody></table>
