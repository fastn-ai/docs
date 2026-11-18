---
description: "Curated is a newsletter publishing platform for curating links into email issues."
hidden: true
---

# Curated

<img src="../../.gitbook/assets/connectors/lg/curated.png" alt="Curated logo">

Curated is a newsletter publishing platform for curating links into email issues. This connector wraps the Curated public API v3: listing publications and their settings, listing and fetching issues (with open/click stats), creating and deleting draft issues, managing collected links (create, read, update, delete, and moving a link into a draft issue), retrieving publication categories, and managing email subscribers and unsubscribers.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [curated.co](https://curated.co) |
| **Authentication** | Credentials you enter |
| **Slug** | `curated` |

## Use it

Add Curated from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.curated.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Collected Link | `createLink` | Collects a link into the publication's collected items, ready to be added to a future issue. Only the destination URL is required; a title, description, category code and an image URL to upload can be supplied. Returns the created link with its id. Curated collects links only, not free text items. |
| Create Draft Issue | `createDraftIssue` | Creates a new empty draft issue in the publication using its default issue settings, and returns the draft with its database id. The Curated API cannot publish or schedule an issue: a draft must be reviewed and sent from the Curated web app. Collected links can be moved into the returned draft with Update Collected Link. |
| Delete Collected Link | `deleteLink` | Permanently removes a collected link from the publication by its id. Returns success true when the link was deleted. A link that belongs to a published issue cannot be removed this way. |
| Delete Draft Issue | `deleteDraftIssue` | Permanently deletes a draft issue by its database id. Only unpublished drafts can be deleted; the id must come from List Issues or Create Draft Issue, not the public issue number. Published issues cannot be removed through the API. |
| Delete Email Subscriber | `deleteEmailSubscriber` | Removes an email subscriber from the publication's list by subscriber id. This deletes the subscriber record outright rather than moving the address to the unsubscribe list; use Unsubscribe Email Address for an opt-out. Undocumented endpoint, verified live against the Curated API v3. |
| Get Collected Link | `getLink` | Retrieves one collected link by id, returning its destination URL, title, description, image URL and the id of the draft issue it belongs to (null while it is still in collected items). |
| Get Email Subscriber | `getEmailSubscriber` | Retrieves a single email subscriber of the publication by subscriber id, returning the id and email address. Only confirmed subscribers are visible here: an address still pending double opt-in returns 404 'Record not found' even though Subscribe Email Address created it and returned its id. |
| Get Issue | `getIssue` | Retrieves one issue with its full contents: every category and the text and link items inside it, including item descriptions rendered to HTML, short URLs and embedded links. Accepts the issue number for published issues; a draft issue must be fetched by its database id. Set stats to true for open and click rates on a published issue. |
| Get Publication Settings | `getPublication` | Retrieves the settings of a single Curated publication: display name, subdomain key, sending schedule (type, day and hour), sender name and email, inquiry email and UTM tracking defaults. Undocumented endpoint, verified live against the Curated API v3. |
| List Categories | `listCategories` | Lists the categories configured for a publication. Each category returns its code, display name, whether it is a sponsored category and, for sponsored categories, the number of sponsored links allowed per issue. The category code is what Create Collected Link and Update Collected Link expect. |
| List Collected Links | `listLinks` | Lists the collected links of a publication that are not yet attached to an issue. Returns each link's id, destination URL, title, description and image URL. Links moved into a draft issue no longer appear here. |
| List Email Subscribers | `listEmailSubscribers` | Lists the confirmed email subscribers of a publication, with paging. Returns the page number, total pages, total results and an array of subscribers with their id and email address. Addresses still pending double opt-in are not included, so a list can read empty just after Subscribe Email Address succeeded. |
| List Email Unsubscribers | `listEmailUnsubscribers` | Lists the addresses that have unsubscribed from the publication, with paging. Returns the page number, total pages, total results and an array of unsubscribed addresses. Use it to keep an external list in step with Curated's opt-outs. |
| List Issues | `listIssues` | Lists the issues of a publication, newest first, with paging. Each issue summary carries its id, issue number, title, summary, public URL and publish/update timestamps. Filter to published or draft issues with state, and set stats to true to include open and click rates. |
| List Publications | `listPublications` | Lists every Curated publication owned by the authenticated account. Returns an array of publications, each with its numeric id, display name and Curated subdomain key. Use this first: the publication id is required by every other action in this connector. |
| Patch Collected Link | `patchLink` | Partially updates a collected link using HTTP PATCH, which Curated accepts as an alias of the documented PUT update route. Send only the fields to change: url, title, description, category, or issue_id to move the link into or out of a draft issue. |
| Subscribe Email Address | `subscribeEmail` | Subscribes an email address to the publication's list and returns the created subscriber record with its id. The address receives the publication's welcome email exactly as if it had signed up on the site, so use this only where the person has clearly consented. By default the publication's double opt-in setting is respected, so the address stays pending until it confirms; set sync to true for an address that has already opted in elsewhere. A rejected address comes back with success false, error_message and errors instead. |
| Unsubscribe Email Address | `unsubscribeEmail` | Opts an email address out of the publication so it no longer receives issues, and returns the affected subscriber record with its id. There is no route to lift an unsubscribe, but Delete Email Subscriber removes the underlying record by that id. A rejected request comes back with success false, error_message and errors instead. |
| Update Collected Link | `updateLink` | Updates a collected link's URL, title, description or category, and can move it into a draft issue by setting issue_id to that draft's id. Send issue_id as an empty string to move the link back to collected items. A link that already belongs to a published issue cannot be updated. Returns the updated link. |
