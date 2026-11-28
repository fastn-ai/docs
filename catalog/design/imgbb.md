---
description: "ImgBB is an image hosting service. Upload an image and get a link to it."
hidden: true
---

# ImgBB

<img src="../../.gitbook/assets/connectors/lg/imgbb.png" alt="ImgBB logo">

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [imgbb.com](https://imgbb.com) |
| **Authentication** | API key |
| **Slug** | `imgbb` |

## Setup

Your customers enter their API key for ImgBB when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect ImgBB from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **ImgBB**.
2. Select **Connect** on the ImgBB card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use ImgBB's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Upload Image</td><td><code>uploadImage</code></td><td>Uploads an image to ImgBB and returns hosted URLs. Accepts the image as base64-encoded data or as a publicly reachable image URL (max 32MB). Optional 'name' sets the filename; optional 'expiration' (60-15552000 seconds) auto-deletes the image after that many seconds. This is the ONLY endpoint ImgBB's public API documents.</td></tr></tbody></table>

