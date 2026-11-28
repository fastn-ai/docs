---
description: "Upload to URL turns files into public download links. Upload, look up and delete files, and check custom file names."
hidden: true
---

# Upload to URL

<img src="../../.gitbook/assets/connectors/lg/upload-to-url.png" alt="Upload to URL logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [uploadtourl.com](https://uploadtourl.com) |
| **Authentication** | API key |
| **Slug** | `uploadToUrl` |

## Setup

Your customers enter their API key for Upload to URL when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Upload to URL from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Upload to URL**.
2. Select **Connect** on the Upload to URL card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Upload to URL's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Custom Filename Availability</td><td><code>checkFilenameAvailability</code></td><td>Checks whether a custom file name is still free before uploading with it. Custom file naming is a paid feature: on Free accounts this'</td></tr><tr><td>Delete File</td><td><code>deleteFile</code></td><td>Permanently deletes one uploaded file by id: the stored object is removed and Get File By Id then Verified live. Note that a copy already cached at the CDN edge can still be served from the public URL for a short window after the delete, so this is not an instant revocation of a link that has already been shared.</td></tr><tr><td>Get Agent Skills Index</td><td><code>getAgentSkillsIndex</code></td><td>Returns the Agent Skills discovery index (schema v0.2.0) that Upload to URL advertises, listing each skill's name, type, description, URL and content digest. Needs no credential.</td></tr><tr><td>Get Anonymous Upload Token</td><td><code>getPublicUploadToken</code></td><td>Issues a single-use, short-lived token for the anonymous upload flow, which needs no API key and spends no account credits. Pass the returned token to Upload File Anonymously. Rate limited by caller IP</td></tr><tr><td>Get API Catalog Document</td><td><code>getApiCatalogDocument</code></td><td>Returns the RFC 9727 api-catalog linkset for Upload to URL, pointing at the OpenAPI document, the human docs page and the health endpoint.</td></tr><tr><td>Get API Service Info</td><td><code>getApiServiceInfo</code></td><td>Returns the Upload to URL API root banner message. A no-credential reachability check for the API host.</td></tr><tr><td>Get Bot Auth Signature Directory</td><td><code>getBotAuthDirectory</code></td><td>Returns the Web Bot Auth HTTP Message Signatures directory (a JWKS of Ed25519 public keys) that Upload to URL publishes so callers can verify signed requests. Public keys only - no private material. Needs no credential.</td></tr><tr><td>Get File By Id</td><td><code>getFileById</code></td><td>Looks up one previously uploaded file by its id and returns its public CDN URL, stored file name, size in bytes, upload time and expiry time.</td></tr><tr><td>Get MCP Server Card</td><td><code>getMcpServerCard</code></td><td>Returns the Model Context Protocol server card for Upload to URL: the MCP version, server name, transport endpoint and the tools the MCP server exposes (upload_file, get_file_status).</td></tr><tr><td>Get OAuth Authorization Server Metadata</td><td><code>getOauthServerMetadata</code></td><td>Returns the RFC 8414 OAuth 2.0 authorization server metadata for Upload to URL, naming the Clerk issuer and its authorization, token and userinfo endpoints and the supported grant types.</td></tr></tbody></table>

<details>

<summary>View 10 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get OAuth Protected Resource Metadata</td><td><code>getProtectedResourceMetadata</code></td><td>Returns the RFC 9728 protected-resource metadata for the Upload to URL API: the resource identifier, the authorization servers that may issue tokens for it, and the supported scopes.</td></tr><tr><td>Get OpenAPI Specification</td><td><code>getOpenapiSpecification</code></td><td>Returns the live OpenAPI 3.1 document describing every Upload to URL API operation, its parameters and its schemas. Useful for discovering endpoints added after this connector was built.</td></tr><tr><td>Get OpenID Connect Discovery Document</td><td><code>getOpenidDiscoveryDocument</code></td><td>Returns the OpenID Connect discovery document for the Clerk identity provider that backs Upload to URL user sign-in, including issuer, JWKS, authorization, token and userinfo endpoints.</td></tr><tr><td>Get Service Health</td><td><code>getServiceHealth</code></td><td>Reports whether the Upload to URL service and its database are up. Returns status and database. Needs no credential.</td></tr><tr><td>List Supported File Formats</td><td><code>listSupportedFormats</code></td><td>Lists every file extension Upload to URL accepts, grouped by category (documents, images, audio, video, archives, code, other), together with the maximum file size. Call it before an upload to validate an extension.</td></tr><tr><td>Publish HTML Page</td><td><code>publishHtmlPage</code></td><td>Publishes a block of HTML as a standalone web page and returns its live URL. Consumes one credit. The page is served from the public CDN at https://cdn.uploadtourl.com/published/{your account id}/root/{page_path}.html - note that the URL therefore embeds your Upload to URL account identifier. SECURITY: the published page is world-readable with no authentication, and the API offers NO route to unpublish it, so always set a retention period through Retention Days. The vendor's own docs page names this field 'slug'; the API actually requires 'page_path' and rejects 'slug' with HTTP 422.</td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td>Uploads a text-based file (txt, csv, json, xml, html, md, svg, yaml, code,...) to Upload to URL and returns an instant public CDN URL. Consumes one upload credit. SECURITY: the returned CDN URL is served with no authentication whatsoever - anyone holding the link can read the file, and the URL is only a short random prefix plus your own file name - so never upload confidential content. Deleting the file does remove the stored object, but a copy already cached at the CDN edge can still be served for a short window afterwards. Call List Supported File Formats first to check an extension.</td></tr><tr><td>Upload File Anonymously</td><td><code>uploadFileAnonymously</code></td><td>Uploads a text-based file without an API key, using a single-use token from Get Anonymous Upload Token, and returns a public CDN URL. Spends no account upload credits but is rate limited by caller IP. WARNING: an anonymous upload is not owned by any account, so Get File By Id and Delete File cannot see or remove it - the file stays public until its retention period expires. The returned URL is served with no authentication; never send confidential content.</td></tr><tr><td>Upload File With Custom Name</td><td><code>uploadFileWithCustomName</code></td><td>Uploads a text-based file under a custom, human-readable name instead of the random prefixed name, optionally overwriting an existing file of the same name. Custom file naming is a paid feature: Free accounts get HTTP 403 'Custom file naming is exclusive to Pro and Business plans.' SECURITY: a custom name makes the unauthenticated public CDN URL fully predictable.</td></tr><tr><td>Verify API Key And Get Credits</td><td><code>verifyApiKey</code></td><td>Validates the connected Upload to URL API key and returns the account's remaining upload credits. Use it as a health check before an upload run and to read how many credits are left. Returns valid, credits and credits_used.</td></tr></tbody></table>

</details>

