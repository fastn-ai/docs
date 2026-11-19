---
description: "ButterCMS is a headless content management system. Create and read posts, pages and content items, and list authors and categories."
hidden: true
---

# ButterCMS

<img src="../../.gitbook/assets/connectors/lg/butter-cms.png" alt="ButterCMS logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [buttercms.com](https://buttercms.com) |
| **Authentication** | API token |
| **Slug** | `butterCms` |

## Setup

Your customers enter their API token for ButterCMS when they connect. Nothing else needs setting up.

## Use it

Add ButterCMS from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.butterCms.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Content Item</td><td><code>createContentItem</code></td><td>Add one or more items to an existing collection via the Write API. Provide the collection key and a flat array of item objects matching the collection's field schema. Writes are processed asynchronously and return a pending status.</td></tr><tr><td>Create Page</td><td><code>createPage</code></td><td>Create a new page of an existing page type via the Write API. The page type must already be defined in ButterCMS. Single (type-less) pages cannot be created through the API. Writes are processed asynchronously and return a pending status.</td></tr><tr><td>Create Post</td><td><code>createPost</code></td><td>Create a new blog post via the Write API. Requires a title and an author object. Writes are processed asynchronously and return a pending status. Optional fields (body, status, categories, tags, SEO metadata) are only sent when provided.</td></tr><tr><td>Delete Post</td><td><code>deletePost</code></td><td>Permanently delete a blog post by its slug via the Write API. Returns an empty 204 response on success.</td></tr><tr><td>Get Atom Feed</td><td><code>getAtomFeed</code></td><td>Retrieve the blog's Atom feed as an XML document (returned as a string), listing recent published posts.</td></tr><tr><td>Get Content</td><td><code>getContent</code></td><td>Retrieve a collection or content field by its key. Returns the collection items or content field values under the requested key. Supports pagination, ordering, and locale for collections.</td></tr><tr><td>Get RSS Feed</td><td><code>getRssFeed</code></td><td>Retrieve the blog's RSS feed as an XML document (returned as a string), listing recent published posts.</td></tr><tr><td>Get Sitemap</td><td><code>getSitemap</code></td><td>Retrieve the blog's XML sitemap (returned as a string) listing published post URLs.</td></tr><tr><td>List Authors</td><td><code>listAuthors</code></td><td>Retrieve all blog authors. Optionally include each author's recent posts.</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>Retrieve all blog categories. Optionally include each category's recent posts.</td></tr></tbody></table>

<details>

<summary>View 12 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Pages</td><td><code>listPages</code></td><td>Retrieve a paginated list of pages of a given page type. Use '*' as the page type to list pages of all types.</td></tr><tr><td>List Posts</td><td><code>listPosts</code></td><td>Retrieve a paginated list of published blog posts, sorted by publication date (newest first). Supports filtering by author, category, or tag slug.</td></tr><tr><td>List Tags</td><td><code>listTags</code></td><td>Retrieve all blog tags. Optionally include each tag's recent posts.</td></tr><tr><td>Retrieve Author</td><td><code>retrieveAuthor</code></td><td>Retrieve a single blog author by slug, including profile details and optionally their recent posts.</td></tr><tr><td>Retrieve Category</td><td><code>retrieveCategory</code></td><td>Retrieve a single blog category by slug, optionally including its recent posts.</td></tr><tr><td>Retrieve Page</td><td><code>retrievePage</code></td><td>Retrieve a single page by its page type and page slug, including all field values. Use '*' as the page type when the type is unknown.</td></tr><tr><td>Retrieve Post</td><td><code>retrievePost</code></td><td>Retrieve a single blog post by its slug, including full body HTML, author, tags, categories, and SEO metadata.</td></tr><tr><td>Retrieve Tag</td><td><code>retrieveTag</code></td><td>Retrieve a single blog tag by slug, optionally including its recent posts.</td></tr><tr><td>Search Pages</td><td><code>searchPages</code></td><td>Full-text search across all pages by keyword. Returns a paginated list of matching pages.</td></tr><tr><td>Search Posts</td><td><code>searchPosts</code></td><td>Full-text search of published blog posts by keyword across title and body. Returns a paginated list of matching posts.</td></tr><tr><td>Update Page</td><td><code>updatePage</code></td><td>Update an existing page's field values via the Write API, identified by page type and page slug. Use '*' as the page type for single (type-less) pages. The write is processed asynchronously and returns a pending status.</td></tr><tr><td>Update Post</td><td><code>updatePost</code></td><td>Update an existing blog post identified by its slug via the Write API. Only the fields provided are changed; the write is processed asynchronously and returns a pending status.</td></tr></tbody></table>

</details>

## Events

ButterCMS has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
