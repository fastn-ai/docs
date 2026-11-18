---
description: "ButterCMS headless CMS."
hidden: true
---

# ButterCMS

ButterCMS headless CMS. Content API (read) for blog posts, authors, categories, tags, pages, collections, and feeds, plus the Write API for creating and managing blog posts, pages, and collection content.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [buttercms.com](https://buttercms.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 22 |
| **Events** | 0 |
| **Slug** | `butterCms` |

## Use it

Add ButterCMS from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.butterCms.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Content Item | `createContentItem` | Add one or more items to an existing collection via the Write API. Provide the collection key and a flat array of item objects matching the collection's field schema. Writes are processed asynchronously and return a pending status. |
| Create Page | `createPage` | Create a new page of an existing page type via the Write API. The page type must already be defined in ButterCMS. Single (type-less) pages cannot be created through the API. Writes are processed asynchronously and return a pending status. |
| Create Post | `createPost` | Create a new blog post via the Write API. Requires a title and an author object. Writes are processed asynchronously and return a pending status. Optional fields (body, status, categories, tags, SEO metadata) are only sent when provided. |
| Delete Post | `deletePost` | Permanently delete a blog post by its slug via the Write API. Returns an empty 204 response on success. |
| Get Atom Feed | `getAtomFeed` | Retrieve the blog's Atom feed as an XML document (returned as a string), listing recent published posts. |
| Get Content | `getContent` | Retrieve a collection or content field by its key. Returns the collection items or content field values under the requested key. Supports pagination, ordering, and locale for collections. |
| Get RSS Feed | `getRssFeed` | Retrieve the blog's RSS feed as an XML document (returned as a string), listing recent published posts. |
| Get Sitemap | `getSitemap` | Retrieve the blog's XML sitemap (returned as a string) listing published post URLs. |
| List Authors | `listAuthors` | Retrieve all blog authors. Optionally include each author's recent posts. |
| List Categories | `listCategories` | Retrieve all blog categories. Optionally include each category's recent posts. |
| List Pages | `listPages` | Retrieve a paginated list of pages of a given page type. Use '*' as the page type to list pages of all types. |
| List Posts | `listPosts` | Retrieve a paginated list of published blog posts, sorted by publication date (newest first). Supports filtering by author, category, or tag slug. |
| List Tags | `listTags` | Retrieve all blog tags. Optionally include each tag's recent posts. |
| Retrieve Author | `retrieveAuthor` | Retrieve a single blog author by slug, including profile details and optionally their recent posts. |
| Retrieve Category | `retrieveCategory` | Retrieve a single blog category by slug, optionally including its recent posts. |
| Retrieve Page | `retrievePage` | Retrieve a single page by its page type and page slug, including all field values. Use '*' as the page type when the type is unknown. |
| Retrieve Post | `retrievePost` | Retrieve a single blog post by its slug, including full body HTML, author, tags, categories, and SEO metadata. |
| Retrieve Tag | `retrieveTag` | Retrieve a single blog tag by slug, optionally including its recent posts. |
| Search Pages | `searchPages` | Full-text search across all pages by keyword. Returns a paginated list of matching pages. |
| Search Posts | `searchPosts` | Full-text search of published blog posts by keyword across title and body. Returns a paginated list of matching posts. |
| Update Page | `updatePage` | Update an existing page's field values via the Write API, identified by page type and page slug. Use '*' as the page type for single (type-less) pages. The write is processed asynchronously and returns a pending status. |
| Update Post | `updatePost` | Update an existing blog post identified by its slug via the Write API. Only the fields provided are changed; the write is processed asynchronously and returns a pending status. |
