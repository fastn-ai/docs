---
description: "Endorsal is testimonial and review collection software."
hidden: true
---

# Endorsal

<img src="../../.gitbook/assets/connectors/lg/endorsal.png" alt="Endorsal logo">

Endorsal is testimonial and review collection software. This connector wraps the Endorsal Public REST API v1 (https://api.endorsal.io) and covers testimonials, contacts, tags, widgets, the Wall of Love, AutoRequest campaigns and properties.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [endorsal.io](https://endorsal.io) |
| **Authentication** | Bearer token |
| **Slug** | `endorsal` |

## Use it

Add Endorsal from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.endorsal.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Contact | `archiveContact` | Archive an Endorsal contact by id. The contact is removed from the active contact list and stops receiving AutoRequest campaign messages. Returns a confirmation message. |
| Check API Status | `checkApiStatus` | Health-check the Endorsal API v1 root. Returns a fixed {"hello":"world"} payload. This route is unauthenticated, so a success here proves the API is reachable but says nothing about whether the API key is valid; use List Properties for that. |
| Check Incoming Webhook | `checkIncomingWebhook` | Reachability check for an Endorsal incoming webhook endpoint. The Endorsal dashboard calls this before sending test data. WARNING: this route always answers HTTP 200 {"success":true}, including for ids that do not exist, so it proves the endpoint is reachable but NOT that the webhook id is valid. Use Send To Incoming Webhook to verify an id for real. |
| Create Contact | `createContact` | Create a contact on the Endorsal property. Either email or phone is required. Creating a contact on its own does NOT message anyone; testimonial requests are only sent when a contact is added to a live AutoRequest campaign inside Endorsal. Returns the created Contact object. Note: on success Endorsal sets success to the string 'Contact created' rather than a boolean. |
| Create Tag | `createTag` | Create a new tag or product tag on the Endorsal property. Product tags carry an image, link and SKU so testimonials can be grouped per product. Returns the created Tag object including its id and generated slug. Note: on success Endorsal sets success to the string 'Tag added' rather than a boolean. |
| Create Testimonial | `createTestimonial` | Create a new testimonial on an Endorsal property. Use this to import a review collected elsewhere. Returns the created Testimonial object including its new id. Note: Endorsal replies with HTTP 200 and success=false plus an error message when a required field is missing. |
| Delete Tag | `deleteTag` | Permanently delete an Endorsal tag or product tag by id. Testimonials themselves are not deleted. Returns a confirmation message. |
| Delete Testimonial | `deleteTestimonial` | Permanently delete an Endorsal testimonial by id. This cannot be undone. Returns a confirmation message. |
| Get AutoRequest Campaign | `getCampaign` | Retrieve a single Endorsal AutoRequest campaign by id, including its delivery channel, live state, include and exclude rules and the message sequence it sends. Read-only. |
| Get Contact | `getContact` | Retrieve a single Endorsal contact by its id, including custom attributes and engagement activity timestamps such as when the contact was last contacted, opened or clicked a request. |
| Get Property | `getProperty` | Retrieve a single Endorsal property by id, returning its name, domain and owning user id. Undocumented but live route. The API key is scoped to one property; requesting another property's id returns HTTP 200 with success=false and 'Invalid credentials'. |
| Get Tag | `getTag` | Retrieve a single Endorsal tag or product tag by its id. Returns the Tag object with name, type, slug, description, image, link and sku. |
| Get Testimonial | `getTestimonial` | Retrieve a single Endorsal testimonial by its id. Returns the full Testimonial object including rating, comments, avatar image URLs, approval state, featured flag, tag ids and the linked contact id. |
| Get Wall Of Love | `getWallOfLove` | Retrieve the Endorsal property's Wall of Love widget and the testimonials it displays. Set Render to true to receive fully rendered HTML that can be inserted straight into a page. Returns an empty data object when the property has no Wall of Love configured in the Endorsal dashboard. |
| Get Widget | `getWidget` | Retrieve a single Endorsal testimonial widget and the testimonials it displays. Set Render to true to receive fully rendered HTML that can be inserted straight into a page instead of the JSON widget object. |
| List AutoRequest Campaigns | `listCampaigns` | List every AutoRequest campaign on the Endorsal property. AutoRequest campaigns are the email and SMS sequences Endorsal uses to ask contacts for a testimonial. The public API is read-only for campaigns: they are created, edited and switched live only in the Endorsal dashboard. |
| List Contacts | `listContacts` | List every contact on the Endorsal property the API key is scoped to. Contacts are the customers Endorsal can request testimonials from. Returns Contact objects with name, email, phone, company, custom attributes and engagement activity timestamps. |
| List Properties | `listProperties` | List the Endorsal properties the API key can reach. A property is one brand or website collecting testimonials. Use this to obtain the Property ID required by Create Testimonial. Undocumented but live route. |
| List Tags | `listTags` | List every tag and product tag defined on the Endorsal property the API key is scoped to. Returns Tag objects with name, type, slug, description, image, link and sku. |
| List Testimonials | `listTestimonials` | Retrieve every testimonial belonging to the Endorsal property the API key is scoped to. Returns a list of Testimonial objects with name, comments, rating, avatar image URLs, approval and featured flags and tag ids. |
| List Testimonials For Contact | `listContactTestimonials` | Retrieve every testimonial left by a given Endorsal contact. Endorsal links a testimonial to a contact when the testimonial's email matches the contact's email, which sets contactID on the testimonial. |
| List Testimonials For Property | `listPropertyTestimonials` | Retrieve every testimonial belonging to a specific Endorsal property id. Undocumented but live route; useful when an account has more than one property. Returns the same Testimonial objects as List Testimonials. |
| List Testimonials For Tag | `listTagTestimonials` | Retrieve every testimonial carrying a given Endorsal tag or product tag, for example all reviews for one product. Note: Endorsal only returns testimonials whose tags were set when the testimonial was created; tags added afterwards with Tag Testimonial are stored on the testimonial but do not appear in this list. |
| List Widgets | `listWidgets` | List every testimonial widget configured on the Endorsal property, with its theme, layout, carousel and grid settings and the testimonials it displays. Widgets are created in the Endorsal dashboard; the API is read-only for them. |
| Search Contacts | `searchContacts` | Search the property's contacts with one or more field/operator/value conditions, combined with AND. Values are compared as strings. Returns the matching Contact objects. |
| Search Testimonials | `searchTestimonials` | Search the property's testimonials with one or more field/operator/value conditions, combined with AND. Values are compared as strings, so numeric fields such as rating, approved and featured cannot be matched. Returns the matching Testimonial objects. |
| Send To Incoming Webhook | `sendToIncomingWebhook` | Push a contact into Endorsal through one of the property's INCOMING webhook endpoints. Endorsal mints the endpoint in the dashboard (Account &gt; Webhooks &gt; New webhook &gt; Incoming, Category Contacts, Action created or updated) and shows the URL as https://api.endorsal.io/v1/webhooks/{webhookId}; pass that trailing id as Webhook ID. For a 'contact.updated' webhook, use the search object to identify the existing contact by email or phone. Endorsal replies HTTP 200 with {"error":"Webhook is invalid"} when the id is not a live incoming webhook. Creating incoming webhooks is a paid-plan feature. |
| Tag Testimonial | `tagTestimonial` | Attach one or more tags or products to an existing testimonial. Each entry is a New Tag object; Endorsal creates the tag if it does not already exist on the property and then links it. Returns the updated Testimonial object with its tags array. |
| Update Contact | `updateContact` | Update an existing Endorsal contact. Supply only the keys you want to change inside the fields object. Returns a confirmation message; follow with Get Contact to read the new values. |
| Update Tag | `updateTag` | Update an existing Endorsal tag or product tag. Supply only the keys you want to change inside the fields object. Returns a confirmation message; follow with Get Tag to read the new values. |
| Update Testimonial | `updateTestimonial` | Update an existing Endorsal testimonial. Supply only the fields you want to change inside the fields object, for example to approve a testimonial (approved = 1) or feature it (featured = 1). Returns a confirmation message rather than the updated object; follow with Get Testimonial to read the new values. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Testimonial Created | `testimonial.created` | Fires when a new testimonial is submitted to the Endorsal property. REGISTRATION IS UI-ONLY - the Endorsal public API v1 exposes no webhook registration route (POST /v1/webhooks, /v1/hooks, /v1/subscriptions and /v1/triggers all return 404 'Cannot POST'); webhooks are managed by the dashboard's private api/webhooks/save endpoint. EXACT CLICK PATH: sign in at https://app.endorsal.io, open Account &gt; Webhooks (https://app.endorsal.io/account/webhooks), pick the property in the property selector, click the + New webhook button, choose OUTGOING, set Category = Testimonials and Action = created, paste the fastn trigger URL into the destination URL field, name it, then Save. Endorsal POSTs unsigned application/json with no signature header. NOTE: the webhooks feature is PLAN-GATED - lower tiers show 'upgrade your plan to a higher tier in order to use the webhooks feature' instead of the form. Endorsal lists testimonial 'updated', 'deleted' and 'tag_added' as coming soon, so 'created' is the only outgoing event it emits today. |
