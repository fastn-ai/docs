---
description: "Senja collects and shares customer testimonials. Create, update and list testimonials, and send form invites."
hidden: true
---

# Senja

<img src="../../.gitbook/assets/connectors/lg/senja.png" alt="Senja logo">

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [senja.io](https://senja.io) |
| **Authentication** | Access token |
| **Slug** | `senja` |

## Setup

Your customers enter their access token for Senja when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Senja from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Senja**.
2. Select **Connect** on the Senja card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Senja's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Testimonial</td><td><code>createTestimonial</code></td><td>Creates a new text or video testimonial in your Senja project. Returns a confirmation message and the identifier of the new testimonial.</td></tr><tr><td>Delete Testimonial</td><td><code>deleteTestimonial</code></td><td>Permanently deletes a testimonial from your Senja project. This action is irreversible.</td></tr><tr><td>Get Testimonial</td><td><code>getTestimonial</code></td><td>Returns a single testimonial from your Senja project by its unique identifier, including its text, rating, customer details, tags, media, translations and shareable links.</td></tr><tr><td>List Links</td><td><code>listLinks</code></td><td>Returns all shareable links in your Senja project, grouped by type: case studies, collection forms, quick links, sizzle reels, walls of love and widgets. Each entry carries its identifier, name and public URL. Use it to obtain the Form ID needed by Send Form Invites.</td></tr><tr><td>List Testimonials</td><td><code>listTestimonials</code></td><td>Returns testimonials from your Senja project. Supports filtering by approval status, rating, type, integration, tags and language, full-text search across testimonial text, title, customer name, customer email and customer tagline, plus sorting and pagination. The response field total is the number of results on the current page, not a global count, so keep paginating until total is lower than limit.</td></tr><tr><td>Send Form Invites</td><td><code>sendFormInvites</code></td><td>Sends testimonial collection invite emails to a list of recipients for one of your Senja forms. The email content and follow-up sequence come from that form's email sequence settings in the Senja dashboard. Returns the number of invites sent and the recipients that were skipped with a reason.</td></tr><tr><td>Update Testimonial</td><td><code>updateTestimonial</code></td><td>Updates a testimonial's approval status or its tags. At least one of Approved, Add Tags or Remove Tags must be supplied. Text, rating and customer details cannot be changed through the API; edit those in the Senja dashboard. Returns the updated testimonial.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Testimonial Created</td><td><code>testimonial_created</code></td><td>Fires when a new testimonial is created in your Senja project, from a collection form, an import or the API. Senja has no webhook registration API, so the endpoint must be registered by hand: in Senja, open the Automate tab in the left sidebar (or Project Settings), scroll to Webhooks, click to add a webhook, paste this trigger URL into Webhook URL, optionally set a Secret, tick the testimonial_created event and save.</td></tr><tr><td>Testimonial Deleted</td><td><code>testimonial_deleted</code></td><td>Fires when a testimonial is deleted from your Senja project. The payload carries the deleted testimonial under data.old. Senja has no webhook registration API, so the endpoint must be registered by hand: in Senja, open the Automate tab in the left sidebar (or Project Settings), scroll to Webhooks, add a webhook, paste this trigger URL into Webhook URL, optionally set a Secret, tick the testimonial_deleted event and save.</td></tr><tr><td>Testimonial Updated</td><td><code>testimonial_updated</code></td><td>Fires when an existing testimonial is updated in your Senja project, for example when it is approved, edited or retagged. The payload carries both the previous (old) and the new state. Senja has no webhook registration API, so the endpoint must be registered by hand: in Senja, open the Automate tab in the left sidebar (or Project Settings), scroll to Webhooks, add a webhook, paste this trigger URL into Webhook URL, optionally set a Secret, tick the testimonial_updated event and save.</td></tr></tbody></table>
