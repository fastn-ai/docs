---
description: "AltTextLab writes accessible alt text for images with AI. Generate alt text from an image link or from uploaded image data."
hidden: true
---

# AltTextLab

<img src="../../.gitbook/assets/connectors/lg/alt-text-lab.png" alt="AltTextLab logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [alttextlab.com](https://alttextlab.com) |
| **Authentication** | API key |
| **Slug** | `altTextLab` |

## Setup

Your customers enter their API key for AltTextLab when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AltTextLab from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AltTextLab**.
2. Select **Connect** on the AltTextLab card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AltTextLab's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate Alt Text from Image Data</td><td><code>generateAltTextFromImageData</code></td><td>Generates AI alt text for an image supplied inline as base64-encoded data instead of a public URL, which suits images that are private or not yet published. AltTextLab stores the upload temporarily and returns a signed URL for it in imageUrl. Accepts the same language, writing style, keyword, e-commerce, context and custom-field options as the URL variant. Credits are deducted only when the response status is "generated".</td></tr><tr><td>Generate Alt Text from Image URL</td><td><code>generateAltTextFromUrl</code></td><td>Generates AI alt text for an image at a publicly accessible URL, in the requested language and writing style, optionally guided by SEO keywords, e-commerce product metadata and surrounding page context. The image must be fetchable without authentication or redirects; if AltTextLab cannot fetch or process the image it Credits are deducted only when the response status is "generated".</td></tr></tbody></table>

