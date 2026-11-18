---
description: "Helpjuice knowledge base platform."
hidden: true
---

# Helpjuice

<img src="../../.gitbook/assets/connectors/lg/helpjuice.png" alt="Helpjuice logo">

Helpjuice knowledge base platform. Manage articles, categories, users, groups, webhooks and account settings, run knowledge base searches, and read activity feeds, backups and the full analytics surface (searches, keywords, articles, categories, users and groups) through the Helpjuice API v3.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [helpjuice.com](https://helpjuice.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `helpjuice` |

## Use it

Add Helpjuice from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.helpjuice.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate User | `activateUser` | Reactivates a previously deactivated Helpjuice user, restoring their access to the knowledge base. |
| Create Article | `createArticle` | Creates a new article in the Helpjuice knowledge base. The article fields are sent inside the article envelope object that the Helpjuice API requires. |
| Create Category | `createCategory` | Creates a new category in the Helpjuice knowledge base, optionally nested under a parent category and restricted to selected users or groups. The fields are sent inside the category envelope, which is required for the access lists to be applied. |
| Create Group | `createGroup` | Creates a new user group on the Helpjuice account, optionally seeding it with members or automatic membership rules. The fields are sent inside the group envelope, which is required for member lists to be applied. |
| Create User | `createUser` | Creates a new user on the Helpjuice account and assigns their role and group memberships. The role identifier must be one provisioned on the account; plans without additional user seats reject every value with a 422. |
| Create Webhook | `createWebhook` | Registers a webhook that posts to the given URL whenever the selected Helpjuice event occurs. Each webhook covers exactly one event, so register one per event you need. |
| Deactivate User | `deactivateUser` | Deactivates a Helpjuice user, revoking their access to the knowledge base while keeping their account and authored content. |
| Delete Article | `deleteArticle` | Permanently deletes an article from the Helpjuice knowledge base. Helpjuice returns HTTP 204 with an empty body on success. |
| Delete Category | `deleteCategory` | Deletes a category from the Helpjuice knowledge base. Articles that belonged to the category are not deleted. Helpjuice returns HTTP 204 with an empty body on success. |
| Delete Group | `deleteGroup` | Deletes a user group from the Helpjuice account. By default the group's members are kept and only their group membership is removed; set Delete Users to also delete the member accounts themselves. |

<details>

<summary>See 30 more actions</summary>

* **Delete User** `deleteUser`: Permanently deletes a user from the Helpjuice account. Use Deactivate User instead to revoke access while keeping the account.
* **Delete Webhook** `deleteWebhook`: Removes a registered webhook from the Helpjuice account so it stops receiving event deliveries.
* **Downvote Article** `downvoteArticle`: Registers a negative rating on a Helpjuice article. Helpjuice returns an empty body on success; read the dislike count back with Get Article Analytics.
* **Get Account Settings** `getAccountSettings`: Retrieves the Helpjuice account settings, including the account name and subdomain, contact form configuration and knowledge base visibility options.
* **Get Activity** `getActivity`: Retrieves a single entry from the Helpjuice activity feed by its identifier.
* **Get Article** `getArticle`: Retrieves a single Helpjuice article by its identifier, including its body, author and keywords.
* **Get Backup** `getBackup`: Retrieves a single Helpjuice knowledge base backup by its identifier.
* **Get Category** `getCategory`: Retrieves a single Helpjuice category by its identifier, including its published and draft articles, sub-categories and hierarchy.
* **Get Group** `getGroup`: Retrieves a single Helpjuice user group by its identifier, including its members.
* **Get User** `getUser`: Retrieves a single Helpjuice user by their identifier, including their role and group memberships.
* **Get Webhook** `getWebhook`: Retrieves a single registered Helpjuice webhook by its identifier, including the status code returned by the most recent delivery.
* **List Activities** `listActivities`: Lists the activity feed for the Helpjuice account, recording who created, updated or deleted articles, categories, users and groups. Supports filtering by owner and resource, and cursor paging backwards through the feed.
* **List Articles** `listArticles`: Lists articles in the Helpjuice knowledge base, with optional filtering by category, publication state, accessibility, language and created/updated date ranges. Returns a paginated collection.
* **List Backups** `listBackups`: Lists the knowledge base backups Helpjuice has generated for the account. Backups are produced by Helpjuice on its own schedule and cannot be created through the API.
* **List Categories** `listCategories`: Lists the categories in the Helpjuice knowledge base, each with its published and draft articles, sub-categories and hierarchy. Returns a paginated collection.
* **List Group Users** `listGroupUsers`: Lists the users who belong to a Helpjuice group. Returns a paginated collection.
* **List Groups** `listGroups`: Lists the user groups defined on the Helpjuice account. Returns a paginated collection.
* **List Search Analytics** `listSearchAnalytics`: Lists the searches visitors ran against the Helpjuice knowledge base over a date range, with filters for searches that found no answer, bounced or dead-ended.
* **List Users** `listUsers`: Lists the users on the Helpjuice account, with optional filtering by email, name, group membership or role. Returns a paginated collection.
* **List Webhooks** `listWebhooks`: Lists the webhooks registered on the Helpjuice account. Note that Helpjuice returns the collection under an articles key rather than webhooks.
* **Search Knowledge Base** `searchKnowledgeBase`: Searches the Helpjuice knowledge base and returns the matching articles with answer snippets and their category, optionally restricted to a single category.
* **Test Webhook** `testWebhook`: Sends a test delivery to a registered Helpjuice webhook and records the status code the target URL returned in Last Response Code. Helpjuice returns HTTP 200 even when the target rejects the delivery, so check that field to confirm the endpoint accepted it.
* **Toggle Webhook** `toggleWebhook`: Enables or disables a Helpjuice webhook by flipping its current state. A disabled webhook returns a null Enabled At and stops receiving deliveries.
* **Update Account Settings** `updateAccountSettings`: Updates the Helpjuice account settings. Only the fields supplied inside the settings envelope are sent, so omitted settings keep their current values. Read the result back with Get Account Settings.
* **Update Article** `updateArticle`: Updates an existing Helpjuice article. Only the fields supplied inside the article envelope are sent, so omitted fields keep their current values.
* **Update Category** `updateCategory`: Updates an existing Helpjuice category. Only the fields supplied inside the category envelope are sent, so omitted fields keep their current values.
* **Update Group** `updateGroup`: Updates a Helpjuice user group, including renaming it and replacing its member list. The fields are sent inside the group envelope, which is required for member lists to be applied.
* **Update User** `updateUser`: Updates a Helpjuice user's name, email address, role or group memberships. Only the fields supplied inside the user envelope are sent.
* **Update Webhook** `updateWebhook`: Updates a registered Helpjuice webhook, changing the URL it posts to or the event that triggers it.
* **Upvote Article** `upvoteArticle`: Registers a positive rating on a Helpjuice article. Helpjuice returns an empty body on success; read the like count back with Get Article Analytics.

</details>
