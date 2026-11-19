---
description: "Imagior automated image generation."
hidden: true
---

# Imagior

<img src="../../.gitbook/assets/connectors/lg/imagior.png" alt="Imagior logo">

Render images from a design template created in the Imagior dashboard, applying dynamic element modifications (text, colours, image sources) at request time. Also exposes account/credit details and template element introspection. Base URL https://api.imagior.com. Image generation consumes one account credit per generated image.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [imagior.com](https://imagior.com) |
| **Authentication** | API key |
| **Slug** | `imagior` |

## Use it

Add Imagior from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.imagior.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate Image</td><td><code>generateImage</code></td><td>Renders an image from an Imagior design template, optionally overriding element properties (text, fill colour, image src, size, opacity...) supplied in the elements object. WARNING: this action SPENDS ACCOUNT CREDITS - one credit per generated image. Omit elements to render the template with its saved defaults. templateId must be a template that belongs to the authenticated account.</td></tr><tr><td>Retrieve Account Details</td><td><code>retrieveAccountDetails</code></td><td>Retrieves the authenticated Imagior account's details, including the account name, email address and the number of image-generation credits remaining. Consumes no credits. Call this before generating images to check the remaining credit balance.</td></tr><tr><td>Retrieve All Templates</td><td><code>retrieveAllTemplates</code></td><td>Retrieves every design template belonging to the authenticated Imagior account, optionally sorted by creation or last-update date. Returns an array of templates with their id, name, createdAt and updatedAt. Use the returned id as the templateId for Generate Image. Consumes no credits.</td></tr><tr><td>Retrieve Basic Template Elements</td><td><code>retrieveBasicTemplateElements</code></td><td>Fetches only the primary property of each element in one Imagior design template - src for image elements, text for text elements and fill for path elements. A lighter alternative to Retrieve Template Elements when you only need the values you intend to override. Consumes no credits.</td></tr><tr><td>Retrieve Template Elements</td><td><code>retrieveTemplateElements</code></td><td>Fetches every element of one Imagior design template together with all of its properties (position, size, scale, angle, opacity, fill, stroke, font, text, image src). Returns a map keyed by element name. Use it to discover the exact element names and property keys to pass in the elements object of Generate Image. Consumes no credits.</td></tr></tbody></table>
