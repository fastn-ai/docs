---
description: "OKZest generates personalised images from design templates. List designs, read their fields and create images."
hidden: true
---

# OKZest

<img src="../../.gitbook/assets/connectors/lg/okzest.png" alt="OKZest logo">

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [okzest.com](https://okzest.com) |
| **Authentication** | API key |
| **Slug** | `okzest` |

## Setup

Your customers enter their API key for OKZest when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect OKZest from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **OKZest**.
2. Select **Connect** on the OKZest card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use OKZest's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Image</td><td><code>createImage</code></td><td>Renders a personalised image from an existing OKZest design and returns the image itself as binary data (JPEG by default, or PNG/WebP via format). The layer overrides are applied to that single render only and never change the stored design. Call Get Design Fields first to discover the design's valid layer_id values and properties. NOTE: each call consumes one image from the account's monthly allowance, and an unrecognised layer_id is silently ignored by OKZest rather than rejected.</td></tr><tr><td>Get Design</td><td><code>getDesign</code></td><td>Fetches a single OKZest design by its design_id. The response body is an array containing the one matching design, with its name, public render URL, project, accepted URL parameters, open counts and timestamps. An unknown or malformed design_id'</td></tr><tr><td>Get Design Fields</td><td><code>getDesignFields</code></td><td>Lists every editable field of an OKZest design: the canvas size, background and output settings, plus one entry per editable property of each layer (keyed as layers[].text, layers[].color, layers[].image_url and so on, labelled with the owning layer's id). Call this before Create Image to discover the exact layer_id values and properties a design supports. An unknown design_id'</td></tr><tr><td>List Designs</td><td><code>listDesigns</code></td><td>Lists every design (image template) in the OKZest account. Returns an array of designs, each with its design_id, name, public render URL, project, the optional URL parameters the design accepts, open counts and timestamps. Use the returned design_id with Get Design, Get Design Fields or Create Image. Takes no inputs: the OKZest REST API ignores filtering and pagination parameters on this route.</td></tr></tbody></table>

