---
description: "Buttondown is newsletter software for writers and creators."
---

# Buttondown

Buttondown is newsletter software for writers and creators. This connector covers subscriber management, draft email lifecycle, tags, automations (read-only), registration forms, newsletter settings, and webhook event subscriptions via the Buttondown v1 REST API.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [buttondown.com](https://buttondown.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 28 |
| **Events** | 0 |
| **Slug** | `buttondown` |

## Use it

Add Buttondown from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.buttondown.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Email | `createEmail` | Create an email on the connected Buttondown newsletter. Set status to 'draft' to keep it from being picked up by the sending pipeline - this connector never sends or publishes an email on your behalf; use Buttondown's dashboard or the Publish Email endpoint separately when you are ready to send. |
| Create Subscriber | `createSubscriber` | Add a new subscriber to the connected Buttondown newsletter by email address. Optionally set tags, notes, UTM attribution, and a lifecycle type. By default, an existing subscriber with the same email returns an error (control this via collisionBehavior). |
| Create Tag | `createTag` | Create a new tag on the connected Buttondown newsletter. Tags can be applied to subscribers and used to filter which subscribers receive an email. |
| Create Webhook | `createWebhook` | Register a new webhook on the connected Buttondown newsletter. Buttondown will POST a JSON payload to the given URL whenever one of the subscribed event types occurs. |
| Delete Email | `deleteEmail` | Permanently delete an email from the connected Buttondown newsletter by its id. This is destructive and cannot be undone. |
| Delete Subscriber | `deleteSubscriber` | Permanently delete a subscriber from the connected Buttondown newsletter, identified by their id or email address. This is destructive and cannot be undone. |
| Delete Tag | `deleteTag` | Permanently delete a tag from the connected Buttondown newsletter by its id. This removes the tag from any subscribers it was applied to. |
| Delete Webhook | `deleteWebhook` | Permanently delete a webhook from the connected Buttondown newsletter by its id. |
| Get Automation | `getAutomation` | Retrieve a single automation on the connected Buttondown newsletter by its id, including its trigger, actions, and filters. Read-only. |
| Get Automation Analytics | `getAutomationAnalytics` | Retrieve aggregate analytics (e.g. runs, opens, clicks) for a single automation on the connected Buttondown newsletter by its id. |
| Get Email | `getEmail` | Retrieve a single email on the connected Buttondown newsletter by its id. |
| Get Form | `getForm` | Retrieve a single registration form on the connected Buttondown newsletter by its id. |
| Get Newsletter | `getNewsletter` | Retrieve the current settings for a single newsletter on the connected Buttondown account by its id, including branding, template, timezone, and delivery configuration. |
| Get Subscriber | `getSubscriber` | Retrieve a single subscriber on the connected Buttondown newsletter, identified by their id or email address. |
| Get Tag | `getTag` | Retrieve a single tag on the connected Buttondown newsletter by its id. |
| Get Webhook | `getWebhook` | Retrieve a single webhook on the connected Buttondown newsletter by its id. |
| List Automations | `listAutomations` | List automations configured on the connected Buttondown newsletter. Automations are event-triggered email sequences and are read-only through this connector - use the Buttondown dashboard to create, edit, enable, or invoke them. |
| List Emails | `listEmails` | List emails (drafts, scheduled, and sent) on the connected Buttondown newsletter, with optional filters for status, subject, and creation/publish date ranges. Returns a paginated page of email objects. |
| List Forms | `listForms` | List registration forms configured on the connected Buttondown newsletter, with subscriber and page-view counts for each. Returns a paginated page of form objects. |
| List Newsletters | `listNewsletters` | List the newsletters on the connected Buttondown account, including branding, template, and delivery settings for each. Most accounts have exactly one newsletter. |
| List Subscribers | `listSubscribers` | List subscribers on the connected Buttondown newsletter, with optional filters for tag, type (e.g. regular, unsubscribed, blocked), email address, and other engagement/date fields. Returns a paginated page of subscriber objects. |
| List Tags | `listTags` | List tags defined on the connected Buttondown newsletter. Returns a paginated page of tag objects. |
| List Webhooks | `listWebhooks` | List webhooks registered on the connected Buttondown newsletter, showing their target URL, status, and subscribed event types. |
| Test Webhook | `testWebhook` | Send a sample event payload to a webhook's configured URL on the connected Buttondown newsletter, to verify the endpoint is reachable and correctly configured. Does not affect real subscribers or emails. |
| Update Email | `updateEmail` | Partially update a draft or scheduled email on the connected Buttondown newsletter by its id. Only supplied fields are changed. Use this to edit content while an email is still in draft status. |
| Update Subscriber | `updateSubscriber` | Partially update a subscriber on the connected Buttondown newsletter, identified by their id or email address. Only supplied fields are changed. |
| Update Tag | `updateTag` | Partially update a tag on the connected Buttondown newsletter by its id. Only supplied fields are changed. |
| Update Webhook | `updateWebhook` | Update a webhook on the connected Buttondown newsletter by its id. Buttondown's API treats this as a full replacement of the webhook's url and event_types, so both must be supplied even though the HTTP method is PATCH. |
