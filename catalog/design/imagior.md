---
description: "Imagior generates images from design templates. Render images from a template and list templates and their editable elements."
hidden: true
---

# Imagior

<img src="../../.gitbook/assets/connectors/lg/imagior.png" alt="Imagior logo">

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [imagior.com](https://imagior.com) |
| **Authentication** | API key |
| **Slug** | `imagior` |

## Setup

Your customers enter their API key for Imagior when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Imagior from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Imagior**.
2. Select **Connect** on the Imagior card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Imagior's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate Image</td><td><code>generateImage</code></td><td>Renders an image from an Imagior design template, optionally overriding element properties (text, fill colour, image src, size, opacity...) supplied in the elements object. WARNING: this action SPENDS ACCOUNT CREDITS - one credit per generated image. Omit elements to render the template with its saved defaults. templateId must be a template that belongs to the authenticated account.</td></tr><tr><td>Retrieve Account Details</td><td><code>retrieveAccountDetails</code></td><td>Retrieves the authenticated Imagior account's details, including the account name, email address and the number of image-generation credits remaining. Consumes no credits. Call this before generating images to check the remaining credit balance.</td></tr><tr><td>Retrieve All Templates</td><td><code>retrieveAllTemplates</code></td><td>Retrieves every design template belonging to the authenticated Imagior account, optionally sorted by creation or last-update date. Returns an array of templates with their id, name, createdAt and updatedAt. Use the returned id as the templateId for Generate Image. Consumes no credits.</td></tr><tr><td>Retrieve Basic Template Elements</td><td><code>retrieveBasicTemplateElements</code></td><td>Fetches only the primary property of each element in one Imagior design template - src for image elements, text for text elements and fill for path elements. A lighter alternative to Retrieve Template Elements when you only need the values you intend to override. Consumes no credits.</td></tr><tr><td>Retrieve Template Elements</td><td><code>retrieveTemplateElements</code></td><td>Fetches every element of one Imagior design template together with all of its properties (position, size, scale, angle, opacity, fill, stroke, font, text, image src). Returns a map keyed by element name. Use it to discover the exact element names and property keys to pass in the elements object of Generate Image. Consumes no credits.</td></tr></tbody></table>

