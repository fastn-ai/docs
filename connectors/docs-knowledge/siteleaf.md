---
description: "Siteleaf is a Git-friendly, Jekyll-based content management system."
hidden: true
---

# Siteleaf

<img src="../../.gitbook/assets/connectors/lg/siteleaf.png" alt="Siteleaf logo">

Siteleaf is a Git-friendly, Jekyll-based content management system. This connector wraps the Siteleaf v2 REST API so you can manage sites, pages, collections, documents, collection files, raw Jekyll source files, site users and roles, publish jobs, tags and categories.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [siteleaf.com](https://siteleaf.com) |
| **Authentication** | Basic auth |
| **Slug** | `siteleaf` |

## Use it

Add Siteleaf from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.siteleaf.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Job | `cancelJob` | Aborts an active Siteleaf job such as a running publish, preview or sync. Returns 200 when the job was cancelled, or 410 Gone when the job id has already expired. |
| Create API Credentials | `createApiCredentials` | Mints the Siteleaf API Key and Secret for an account. SECURITY WARNING: the response contains live API credentials, so restrict who may run it. This is the only Siteleaf endpoint authenticated with the account email and password rather than an API key, so it must be run on a connection whose API Key field holds the account email and whose API Secret field holds the account password; a normal key-and-secret connection is rejected with 401 Unauthorized. |
| Create Collection | `createCollection` | Creates a collection on a site. Title is required; path defaults to a URL-safe version of the title and becomes the Jekyll collection directory. Returns the created collection. |
| Create Collection File | `createCollectionFile` | Uploads a static file into a collection as a multipart/form-data attachment. Collection files must not contain YAML front matter - use Create Document for content with front matter. The file content is sent as text, so this action suits text formats such as .txt, .csv, .svg, .json or .md without front matter; true binary uploads are not supported by the connector runtime. |
| Create Document | `createDocument` | Creates a document inside a collection, for example a blog post in the posts collection. Title is required; tags, categories and metadata are written into the document's YAML front matter. |
| Create Or Replace Source File | `createOrReplaceSourceFile` | Uploads a raw Jekyll source file at the given path, replacing it if it already exists. Siteleaf parses the upload and creates the matching page, document or file resource. The content is sent as a text multipart attachment, so this suits text formats such as .html, .md, .scss, .yml and .json; true binary uploads are not supported by the connector runtime. |
| Create Page | `createPage` | Creates a page on a site. A page is a standalone Jekyll file outside any collection. Title is required; supply path to control the filename, otherwise Siteleaf derives one from the title. |
| Create Role | `createRole` | Grants an existing Siteleaf user a role on a site, making them a collaborator. Pass the user's id and the role kind. Returns the created role including its id. |
| Create Site | `createSite` | Creates a new Siteleaf site. Title and domain are required; the domain must be unique across Siteleaf (a free siteleaf.net subdomain such as my-site.siteleaf.net is accepted). Returns the created site including its id. |
| Delete Collection | `deleteCollection` | Permanently deletes a collection and every document and file inside it. Returns the deleted collection id with deleted set to true. |

<details>

<summary>See 29 more actions</summary>

* **Delete Document** `deleteDocument`: Permanently deletes a document and its underlying source file. Returns the deleted document id with deleted set to true.
* **Delete Page** `deletePage`: Permanently deletes a page and its underlying source file. Returns the deleted page id with deleted set to true.
* **Delete Role** `deleteRole`: Revokes a site role, removing that user's access to the site. Take care when deleting a role that belongs to the authenticated account, as it can remove your own access.
* **Delete Site** `deleteSite`: Permanently deletes a Siteleaf site and all of its pages, collections, documents and files. This cannot be undone. Returns the deleted site id with deleted set to true.
* **Delete Source File** `deleteSourceFile`: Permanently deletes a file from the site's Jekyll source tree and removes the page, document or file resource behind it. Directories and _config.yml cannot be deleted. Returns the deleted file's metadata.
* **Download Source File** `downloadSourceFile`: Downloads the raw contents of a file in the site's Jekyll source tree, including its YAML front matter. The runtime returns the file as a reference object whose data field holds the base64 encoded contents.
* **Get Collection** `getCollection`: Retrieves a single collection of a site by its path, including its permalink style, output flag and metadata.
* **Get Current User** `getCurrentUser`: Returns the Siteleaf user account the API credentials belong to, including id, email and name. Useful as a connection health check.
* **Get Document** `getDocument`: Retrieves a single document by id, including its body, tags, categories, front-matter metadata and rendered URL.
* **Get Job Status** `getJobStatus`: Reads the status of a long-running Siteleaf job such as a publish, preview or sync. Job ids come from the jobs object on a site. The endpoint streams Server-Sent Events and closes when the job completes or fails; a job id expires 30 minutes after its last event, after which the endpoint answers 410 Gone with a Job not found event.
* **Get Page** `getPage`: Retrieves a single page by id, including its body, front-matter metadata, path, permalink and rendered URL.
* **Get Role** `getRole`: Retrieves a single site role by id, showing which user it belongs to, which site it grants access to and the level of access.
* **Get Site** `getSite`: Retrieves a single Siteleaf site by id, including its domain, timezone, Jekyll defaults, metadata and the ids of its most recent preview, publish and sync jobs.
* **Get Source File** `getSourceFile`: Returns metadata for a single file in the site's Jekyll source tree, or the listing of a sub-directory when the name is a directory. Pass a path such as index.html, css/main.scss or _layouts.
* **List Collection Files** `listCollectionFiles`: Lists the static files stored in a collection, such as images uploaded into the uploads collection. Each entry carries the filename, content type, file size and a download URL.
* **List Collections** `listCollections`: Lists the collections of a site. A collection is a Jekyll collection such as posts or uploads and groups documents under a directory. Use the returned path value as the collectionPath input of the collection and document actions.
* **List Documents** `listDocuments`: Lists the documents of a collection, for example the posts of a blog. Supports searching by title or path, sorting, visibility filtering and file-extension filtering.
* **List Pages** `listPages`: Lists the pages of a site. Pages are standalone Jekyll files that live outside a collection, such as index.html or about.md. Supports searching by title or path, sorting, visibility filtering and file-extension filtering.
* **List Post Categories** `listPostCategories`: Lists every category used by the posts of a site. Returns a plain array of category names.
* **List Post Tags** `listPostTags`: Lists every tag used by the posts of a site. Returns a plain array of tag names.
* **List Site Users** `listSiteUsers`: Lists the users who have access to a site, with the role each one holds on it.
* **List Sites** `listSites`: Lists every Siteleaf site the authenticated account can access. Returns an array of site objects with id, title, domain, timezone, metadata and Jekyll defaults. Use the returned id as the siteId input of the other site-scoped actions.
* **List Source Directory** `listSourceDirectory`: Lists the contents of the site's Jekyll source tree at its root, as if you were looking at the repository locally. Returns files and directories with their type, size and SHA. Use Get Source File to inspect a single file or a sub-directory.
* **Publish Site** `publishSite`: Starts a publish job that builds the site with Jekyll and deploys it to its configured hosting or sync target. Returns the queued job; poll it with Get Job Status. Warning: this makes content live on the site's public domain.
* **Update Collection** `updateCollection`: Updates a collection identified by its current path. Only the fields you supply are changed; changing path renames the collection directory. Returns the updated collection.
* **Update Document** `updateDocument`: Updates a document by id. Only the fields you supply are changed, so you can edit just the body, the tags or the front-matter metadata. Returns the updated document.
* **Update Page** `updatePage`: Updates a page by id. Only the fields you supply are changed, so you can edit just the body or just the front-matter metadata. Returns the updated page.
* **Update Role** `updateRole`: Changes the level of access a site role grants. Take care when changing a role that belongs to the authenticated account, as lowering it can remove your own access to the site.
* **Update Site** `updateSite`: Updates an existing Siteleaf site. Only the fields you supply are changed. Returns the updated site object.

</details>
