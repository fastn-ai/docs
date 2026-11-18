---
description: "Readwise saves, organizes and resurfaces the highlights you take across books, articles, podcasts and tweets, and its Reader companion is a read-later app for…"
hidden: true
---

# Readwise

<img src="../../.gitbook/assets/connectors/lg/readwise.png" alt="Readwise logo">

Readwise saves, organizes and resurfaces the highlights you take across books, articles, podcasts and tweets, and its Reader companion is a read-later app for articles, RSS, email newsletters, PDFs, EPUBs and videos. This connector covers the full Readwise v2 API (highlights, books, tags, export, daily review, user info) and the Reader v3 API (documents, bulk updates, document tags).

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [readwise.io](https://readwise.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `readwise` |

## Use it

Add Readwise from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.readwise.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Update Documents | `bulkUpdateDocuments` | Updates up to 50 Readwise Reader documents in one request, each with its own set of fields. Returns a per-item result; HTTP 207 means some items failed while the payload itself was valid. Rate limited by Readwise to 20 requests per minute. |
| Complete Daily Review | `completeDailyReview` | Marks the current Readwise daily review as complete and returns the review id with its completed flag. |
| Create Book Tag | `createBookTag` | Attaches a tag to a Readwise source, creating the tag if the source does not already carry it. Returns the tag with its id. |
| Create Highlight Tag | `createHighlightTag` | Attaches a tag to a Readwise highlight, creating the tag if the highlight does not already carry it. Returns the tag with its id. |
| Create Highlights | `createHighlights` | Saves one or more highlights into the Readwise library, creating the source book/article/podcast automatically when it does not yet exist. Highlights are de-duplicated on title, author, text and source URL. Returns the created or updated sources, each carrying the ids of the highlights the request touched in modified_highlights. |
| Delete Book Tag | `deleteBookTag` | Removes a tag from a Readwise source. Readwise answers HTTP 204 with an empty body on success. |
| Delete Document | `deleteDocument` | Permanently deletes a document from Readwise Reader. Readwise answers HTTP 204 with an empty body on success. Highlight and note documents cannot be deleted this way - Readwise answers HTTP 400 "Deleting 'highlight' documents is not supported."; delete the parent document instead. Rate limited by Readwise to 20 requests per minute. |
| Delete Highlight | `deleteHighlight` | Permanently deletes a highlight from the Readwise library. Readwise answers HTTP 204 with an empty body on success. |
| Delete Highlight Tag | `deleteHighlightTag` | Removes a tag from a Readwise highlight. Readwise answers HTTP 204 with an empty body on success. |
| Export Highlights | `exportHighlights` | Exports every source in the Readwise library together with its highlights, ready for syncing into a note-taking app or a backup. Call it with no parameters for a full export, then page with the returned cursor; later pass Updated After to fetch only what changed. |

<details>

<summary>See 20 more actions</summary>

* **Get Book** `getBook`: Retrieves a single Readwise source - a book, article, tweet or podcast - by its id, including its title, author, category, highlight count and tags.
* **Get Book Tag** `getBookTag`: Retrieves a single tag attached to a Readwise source by the source id and the tag id.
* **Get Daily Review** `getDailyReview`: Returns the highlights in the most recent Readwise daily review, along with the review id and whether it has been completed. Readwise answers HTTP 404 with "Review not found." when no daily review has been generated yet.
* **Get Highlight** `getHighlight`: Retrieves a single Readwise highlight by its id, including its text, note, colour, location, tags and the id of the book it belongs to.
* **Get Highlight Tag** `getHighlightTag`: Retrieves a single tag attached to a Readwise highlight by the highlight id and the tag id.
* **Get User Info** `getUserInfo`: Returns the Readwise account that owns the access token, including the user id, the sign-in email address and the associated profile id. Useful for confirming which account a connection is bound to.
* **List All Tags** `listAllTags`: Lists every tag used anywhere in the Readwise library, across all books and highlights. Readwise returns this as a bare JSON array.
* **List Book Tags** `listBookTags`: Lists the tags attached to a single Readwise source. Readwise returns this endpoint as a bare JSON array with no pagination, so all tags on the source come back in one call.
* **List Books** `listBooks`: Lists the sources in the Readwise library - books, articles, tweets, supplementals and podcasts - with pagination metadata. Optionally filter by category, import source or update/highlight timestamps. Rate limited by Readwise to 20 requests per minute.
* **List Document Tags** `listDocumentTags`: Lists every tag used across Readwise Reader documents, returning the tag key to pass to the Tag filter on List Documents. Rate limited by Readwise to 20 requests per minute.
* **List Documents** `listDocuments`: Lists documents in Readwise Reader with pagination metadata. Highlights and notes made in Reader are documents too and carry a parent id. Filter by id, location, category, tag or last-updated time. Rate limited by Readwise to 20 requests per minute.
* **List Highlight Tags** `listHighlightTags`: Lists the tags attached to a single Readwise highlight, with pagination metadata.
* **List Highlights** `listHighlights`: Lists the highlights in the Readwise library, newest first, with pagination metadata. Optionally filter by the source book/article, by last-updated time or by the time the highlight was taken. Rate limited by Readwise to 20 requests per minute.
* **Save Document** `saveDocument`: Saves a document into Readwise Reader. Supply the HTML yourself or let Reader scrape the URL. Setting Parent ID instead turns the request into a highlight on an existing document, in which case Content is required. Rate limited by Readwise to 50 requests per minute.
* **Update Book** `updateBook`: Overrides the title, author and category of a Readwise source. The category override is required by the API on every call. Returns the updated source.
* **Update Book Tag** `updateBookTag`: Renames a tag attached to a Readwise source. Returns the updated tag.
* **Update Document** `updateDocument`: Updates a single document in Readwise Reader. Only the fields you supply are changed; omitted fields keep their current values. Rate limited by Readwise to 50 requests per minute.
* **Update Highlight** `updateHighlight`: Updates an existing Readwise highlight. Only the fields you supply are changed; omitted fields keep their current values. Returns the updated highlight.
* **Update Highlight Tag** `updateHighlightTag`: Renames a tag attached to a Readwise highlight. Returns the updated tag.
* **Validate Access Token** `validateAccessToken`: Checks that the configured Readwise access token is valid. Readwise answers HTTP 204 with an empty body for a valid token and HTTP 401 for an invalid one.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Any Document Created | `reader.any_document.created` | Fires when any new document is added to Readwise Reader, whether an article, PDF, email or feed item. Registration is manual: sign in at https://readwise.io, open https://readwise.io/webhooks, click Create New Webhook, paste this trigger's URL into URL, click Test Endpoint, tick 'reader.any_document.created' under Event Types, enter a Name, then click Create. Readwise puts a 32-character shared secret in the payload's secret field rather than signing a header, so fastn cannot verify the signature. Payload modelled from Readwise's documented sample at https://docs.readwise.io/readwise/docs/webhooks, not from a captured delivery. |
| Document Archived | `reader.document.archived` | Fires when a Readwise Reader document is archived. Registration is manual: sign in at https://readwise.io, open https://readwise.io/webhooks, click Create New Webhook, paste this trigger's URL into URL, click Test Endpoint, tick 'reader.document.archived' under Event Types, enter a Name, then click Create. Readwise sends its secret in the payload body rather than a signature header, so fastn cannot verify the signature. Payload modelled from Readwise's documented sample, not from a captured delivery. |
| Document Finished | `reader.document.finished` | Fires when a Readwise Reader document is marked as finished or read. Registration is manual: sign in at https://readwise.io, open https://readwise.io/webhooks, click Create New Webhook, paste this trigger's URL into URL, click Test Endpoint, tick 'reader.document.finished' under Event Types, enter a Name, then click Create. Readwise sends its secret in the payload body rather than a signature header, so fastn cannot verify the signature. Payload modelled from Readwise's documented sample, not from a captured delivery. |
| Document Moved To Inbox | `reader.document.moved_to_inbox` | Fires when a Readwise Reader document is moved back into the inbox. Registration is manual: sign in at https://readwise.io, open https://readwise.io/webhooks, click Create New Webhook, paste this trigger's URL into URL, click Test Endpoint, tick 'reader.document.moved_to_inbox' under Event Types, enter a Name, then click Create. Readwise sends its secret in the payload body rather than a signature header, so fastn cannot verify the signature. Payload modelled from Readwise's documented sample, not from a captured delivery. |
| Document Moved To Later | `reader.document.moved_to_later` | Fires when a Readwise Reader document is moved into the Later queue. Registration is manual: sign in at https://readwise.io, open https://readwise.io/webhooks, click Create New Webhook, paste this trigger's URL into URL, click Test Endpoint, tick 'reader.document.moved_to_later' under Event Types, enter a Name, then click Create. Readwise sends its secret in the payload body rather than a signature header, so fastn cannot verify the signature. Payload modelled from Readwise's documented sample, not from a captured delivery. |
| Document Shortlisted | `reader.document.shortlisted` | Fires when a Readwise Reader document is added to the shortlist or favourites. Registration is manual: sign in at https://readwise.io, open https://readwise.io/webhooks, click Create New Webhook, paste this trigger's URL into URL, click Test Endpoint, tick 'reader.document.shortlisted' under Event Types, enter a Name, then click Create. Readwise sends its secret in the payload body rather than a signature header, so fastn cannot verify the signature. Payload modelled from Readwise's documented sample, not from a captured delivery. |
| Document Tags Updated | `reader.document.tags_updated` | Fires when tags are added to, removed from or changed on a Readwise Reader document. Registration is manual: sign in at https://readwise.io, open https://readwise.io/webhooks, click Create New Webhook, paste this trigger's URL into URL, click Test Endpoint, tick 'reader.document.tags_updated' under Event Types, enter a Name, then click Create. Readwise sends its secret in the payload body rather than a signature header, so fastn cannot verify the signature. Payload modelled from Readwise's documented sample, not from a captured delivery. |
| Feed Document Created | `reader.feed_document.created` | Fires when a new document arrives in Readwise Reader from an RSS feed or a newsletter subscription. Registration is manual: sign in at https://readwise.io, open https://readwise.io/webhooks, click Create New Webhook, paste this trigger's URL into URL, click Test Endpoint, tick 'reader.feed_document.created' under Event Types, enter a Name, then click Create. Readwise sends its secret in the payload body rather than a signature header, so fastn cannot verify the signature. Payload modelled from Readwise's documented sample, not from a captured delivery. |
| Highlight Created | `readwise.highlight.created` | Fires when a new highlight is created in the Readwise library. Registration is manual: sign in at https://readwise.io, open https://readwise.io/webhooks, click Create New Webhook, paste this trigger's URL into URL, click Test Endpoint (Readwise refuses to save a webhook whose endpoint has not answered a successful test), tick 'readwise.highlight.created' under Event Types, enter a Name, then click Create. Readwise puts a 32-character shared secret in the payload's secret field rather than signing a header, so fastn cannot verify the signature - compare the secret field yourself in the workflow. Payload modelled from Readwise's documented sample at https://docs.readwise.io/readwise/docs/webhooks, not from a captured delivery. |
| Non-Feed Document Created | `reader.non_feed_document.created` | Fires when a document is added to Readwise Reader manually rather than from a feed. Registration is manual: sign in at https://readwise.io, open https://readwise.io/webhooks, click Create New Webhook, paste this trigger's URL into URL, click Test Endpoint, tick 'reader.non_feed_document.created' under Event Types, enter a Name, then click Create. Readwise sends its secret in the payload body rather than a signature header, so fastn cannot verify the signature. Payload modelled from Readwise's documented sample, not from a captured delivery. |
