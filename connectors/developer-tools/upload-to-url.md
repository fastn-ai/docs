---
description: "Upload to URL (uploadtourl.com) turns any file into an instant public CDN link."
hidden: true
---

# Upload to URL

Upload to URL (uploadtourl.com) turns any file into an instant public CDN link. Covers the API-key surface of https://uploadtourl.com/api - upload a file and get a CDN URL, get a file by id, delete it, check custom-filename availability, verify the key and read remaining credits, list supported formats, publish a standalone HTML page - plus the credential-free surface: service info and health, the anonymous upload-token and upload flow, the live OpenAPI document and the discovery documents. Dashboard, API-key management and billing endpoints are excluded on purpose: they accept only a Clerk end-user session and answer an API key with 401 'Not authenticated'. SECURITY: every uploaded file and published page is served from an unauthenticated public URL, and a published page cannot be unpublished - set a retention period instead. The vendor publishes no customer-facing webhook or event API, so this connector is poll-only.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [uploadtourl.com](https://uploadtourl.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 20 |
| **Events** | 0 |
| **Slug** | `uploadToUrl` |

## Use it

Add Upload to URL from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.uploadToUrl.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Custom Filename Availability | `checkFilenameAvailability` | Checks whether a custom file name is still free before uploading with it. Custom file naming is a paid feature: on Free accounts this returns HTTP 403 with 'Custom file naming is exclusive to Pro and Business plans.' |
| Delete File | `deleteFile` | Permanently deletes one uploaded file by id: the stored object is removed and Get File By Id then returns 404 'File not found'. Verified live. Note that a copy already cached at the CDN edge can still be served from the public URL for a short window after the delete, so this is not an instant revocation of a link that has already been shared. |
| Get Agent Skills Index | `getAgentSkillsIndex` | Returns the Agent Skills discovery index (schema v0.2.0) that Upload to URL advertises, listing each skill's name, type, description, URL and content digest. Needs no credential. |
| Get Anonymous Upload Token | `getPublicUploadToken` | Issues a single-use, short-lived token for the anonymous upload flow, which needs no API key and spends no account credits. Pass the returned token to Upload File Anonymously. Rate limited by caller IP: returns HTTP 429 once the anonymous quota is used up. |
| Get API Catalog Document | `getApiCatalogDocument` | Returns the RFC 9727 api-catalog linkset for Upload to URL, pointing at the OpenAPI document, the human docs page and the health endpoint. |
| Get API Service Info | `getApiServiceInfo` | Returns the Upload to URL API root banner message. A no-credential reachability check for the API host. |
| Get Bot Auth Signature Directory | `getBotAuthDirectory` | Returns the Web Bot Auth HTTP Message Signatures directory (a JWKS of Ed25519 public keys) that Upload to URL publishes so callers can verify signed requests. Public keys only - no private material. Needs no credential. |
| Get File By Id | `getFileById` | Looks up one previously uploaded file by its id and returns its public CDN URL, stored file name, size in bytes, upload time and expiry time. Returns 404 'File not found' when the id does not belong to the connected API key. |
| Get MCP Server Card | `getMcpServerCard` | Returns the Model Context Protocol server card for Upload to URL: the MCP version, server name, transport endpoint and the tools the MCP server exposes (upload_file, get_file_status). |
| Get OAuth Authorization Server Metadata | `getOauthServerMetadata` | Returns the RFC 8414 OAuth 2.0 authorization server metadata for Upload to URL, naming the Clerk issuer and its authorization, token and userinfo endpoints and the supported grant types. |
| Get OAuth Protected Resource Metadata | `getProtectedResourceMetadata` | Returns the RFC 9728 protected-resource metadata for the Upload to URL API: the resource identifier, the authorization servers that may issue tokens for it, and the supported scopes. |
| Get OpenAPI Specification | `getOpenapiSpecification` | Returns the live OpenAPI 3.1 document describing every Upload to URL API operation, its parameters and its schemas. Useful for discovering endpoints added after this connector was built. |
| Get OpenID Connect Discovery Document | `getOpenidDiscoveryDocument` | Returns the OpenID Connect discovery document for the Clerk identity provider that backs Upload to URL user sign-in, including issuer, JWKS, authorization, token and userinfo endpoints. |
| Get Service Health | `getServiceHealth` | Reports whether the Upload to URL service and its database are up. Returns status and database. Needs no credential. |
| List Supported File Formats | `listSupportedFormats` | Lists every file extension Upload to URL accepts, grouped by category (documents, images, audio, video, archives, code, other), together with the maximum file size. Call it before an upload to validate an extension. |
| Publish HTML Page | `publishHtmlPage` | Publishes a block of HTML as a standalone web page and returns its live URL. Consumes one credit. The page is served from the public CDN at https://cdn.uploadtourl.com/published/{your account id}/root/{page_path}.html - note that the URL therefore embeds your Upload to URL account identifier. SECURITY: the published page is world-readable with no authentication, and the API offers NO route to unpublish it, so always set a retention period through Retention Days. The vendor's own docs page names this field 'slug'; the API actually requires 'page_path' and rejects 'slug' with HTTP 422. |
| Upload File | `uploadFile` | Uploads a text-based file (txt, csv, json, xml, html, md, svg, yaml, code, ...) to Upload to URL and returns an instant public CDN URL. Consumes one upload credit. SECURITY: the returned CDN URL is served with no authentication whatsoever - anyone holding the link can read the file, and the URL is only a short random prefix plus your own file name - so never upload confidential content. Deleting the file does remove the stored object, but a copy already cached at the CDN edge can still be served for a short window afterwards. Call List Supported File Formats first to check an extension. |
| Upload File Anonymously | `uploadFileAnonymously` | Uploads a text-based file without an API key, using a single-use token from Get Anonymous Upload Token, and returns a public CDN URL. Spends no account upload credits but is rate limited by caller IP. WARNING: an anonymous upload is not owned by any account, so Get File By Id and Delete File cannot see or remove it - the file stays public until its retention period expires. The returned URL is served with no authentication; never send confidential content. |
| Upload File With Custom Name | `uploadFileWithCustomName` | Uploads a text-based file under a custom, human-readable name instead of the random prefixed name, optionally overwriting an existing file of the same name. Custom file naming is a paid feature: Free accounts get HTTP 403 'Custom file naming is exclusive to Pro and Business plans.' SECURITY: a custom name makes the unauthenticated public CDN URL fully predictable. |
| Verify API Key And Get Credits | `verifyApiKey` | Validates the connected Upload to URL API key and returns the account's remaining upload credits. Use it as a health check before an upload run and to read how many credits are left. Returns valid, credits and credits_used. |
