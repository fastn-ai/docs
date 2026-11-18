---
description: "Senja is a testimonial collection, management and sharing platform."
hidden: true
---

# Senja

Senja is a testimonial collection, management and sharing platform. This connector covers the full Senja REST API v1: listing, creating, retrieving, updating and deleting testimonials, retrieving shareable link URLs for forms, widgets, walls of love, case studies, quick links and sizzle reels, and sending form invite emails to customers.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [senja.io](https://senja.io) |
| **Authentication** | Bearer token |
| **Actions** | 7 |
| **Events** | 3 |
| **Slug** | `senja` |

## Use it

Add Senja from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.senja.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Testimonial | `createTestimonial` | Creates a new text or video testimonial in your Senja project. Returns a confirmation message and the identifier of the new testimonial. |
| Delete Testimonial | `deleteTestimonial` | Permanently deletes a testimonial from your Senja project. This action is irreversible. |
| Get Testimonial | `getTestimonial` | Returns a single testimonial from your Senja project by its unique identifier, including its text, rating, customer details, tags, media, translations and shareable links. |
| List Links | `listLinks` | Returns all shareable links in your Senja project, grouped by type: case studies, collection forms, quick links, sizzle reels, walls of love and widgets. Each entry carries its identifier, name and public URL. Use it to obtain the Form ID needed by Send Form Invites. |
| List Testimonials | `listTestimonials` | Returns testimonials from your Senja project. Supports filtering by approval status, rating, type, integration, tags and language, full-text search across testimonial text, title, customer name, customer email and customer tagline, plus sorting and pagination. The response field total is the number of results on the current page, not a global count, so keep paginating until total is lower than limit. |
| Send Form Invites | `sendFormInvites` | Sends testimonial collection invite emails to a list of recipients for one of your Senja forms. The email content and follow-up sequence come from that form's email sequence settings in the Senja dashboard. Returns the number of invites sent and the recipients that were skipped with a reason. |
| Update Testimonial | `updateTestimonial` | Updates a testimonial's approval status or its tags. At least one of Approved, Add Tags or Remove Tags must be supplied. Text, rating and customer details cannot be changed through the API; edit those in the Senja dashboard. Returns the updated testimonial. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Testimonial Created | `testimonial_created` | Fires when a new testimonial is created in your Senja project, from a collection form, an import or the API. Senja has no webhook registration API, so the endpoint must be registered by hand: in Senja, open the Automate tab in the left sidebar (or Project Settings), scroll to Webhooks, click to add a webhook, paste this trigger URL into Webhook URL, optionally set a Secret, tick the testimonial_created event and save. Payload schema is modelled from Senja's published sample payload in the Webhook Integration help article, not from a captured delivery. |
| Testimonial Deleted | `testimonial_deleted` | Fires when a testimonial is deleted from your Senja project. The payload carries the deleted testimonial under data.old. Senja has no webhook registration API, so the endpoint must be registered by hand: in Senja, open the Automate tab in the left sidebar (or Project Settings), scroll to Webhooks, add a webhook, paste this trigger URL into Webhook URL, optionally set a Secret, tick the testimonial_deleted event and save. Payload schema is modelled from Senja's published sample payload in the Webhook Integration help article, not from a captured delivery. |
| Testimonial Updated | `testimonial_updated` | Fires when an existing testimonial is updated in your Senja project, for example when it is approved, edited or retagged. The payload carries both the previous (old) and the new state. Senja has no webhook registration API, so the endpoint must be registered by hand: in Senja, open the Automate tab in the left sidebar (or Project Settings), scroll to Webhooks, add a webhook, paste this trigger URL into Webhook URL, optionally set a Secret, tick the testimonial_updated event and save. Payload schema is modelled from Senja's published sample payload in the Webhook Integration help article, not from a captured delivery. |
