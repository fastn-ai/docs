---
description: "AbstractAPI Image Processing compresses and resizes images. Optimize an image from a URL."
hidden: true
---

# AbstractAPI Image Processing

<img src="../../.gitbook/assets/connectors/lg/abstract-api-image-processing.png" alt="AbstractAPI Image Processing logo">

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiImageProcessing` |

## Setup

Your customers enter their API key for AbstractAPI Image Processing when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AbstractAPI Image Processing from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AbstractAPI Image Processing**.
2. Select **Connect** on the AbstractAPI Image Processing card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AbstractAPI Image Processing's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Optimize Image From URL</td><td><code>optimizeImageFromUrl</code></td><td>Compresses an image hosted at a public URL (up to 32 MB) using lossless or lossy compression, and returns the original and final size and dimensions, the bytes saved, and a URL to download the optimized image. Quality and resize options are not exposed by this action.</td></tr></tbody></table>

