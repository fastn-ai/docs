---
description: "remove.bg removes image backgrounds. Remove the background from an image and check your account credits."
hidden: true
---

# remove.bg

<img src="../../.gitbook/assets/connectors/lg/remove-bg.png" alt="remove.bg logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [remove.bg](https://remove.bg) |
| **Authentication** | API key |
| **Slug** | `removeBg` |

## Setup

Your customers enter their API key for remove.bg when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect remove.bg from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **remove.bg**.
2. Select **Connect** on the remove.bg card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use remove.bg's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Account Info</td><td><code>getAccountInfo</code></td><td>Fetches the remove.bg account credit balance and the number of free API calls remaining. Returns the subscription, pay-as-you-go, enterprise and total credit amounts together with the monthly free API call allowance. Balance changes can be delayed by several seconds, so remove.bg recommends calling this only on initial load or a manual refresh and otherwise tracking the balance locally using the X-Credits-Charged response header of each background removal. The 'sizes' field is always 'all' and is deprecated.</td></tr><tr><td>Remove Image Background</td><td><code>removeImageBackground</code></td><td>Removes the background from a JPG, PNG or WebP image and returns the cut-out as a base64-encoded string together with the foreground bounding box. Supply exactly one image source: image_url or image_file_b64. Input limits are 22 MB file size and 50 megapixels. Output size 'preview' (up to 0.25 MP) is free and consumes one of the monthly free API calls; 'full' (up to 25 MP) and 'auto' consume account credits. Supports foreground type hints, output format, region of interest, cropping, scaling, positioning, alpha-only output, AI shadows, semitransparency and solid-colour or image backgrounds. Errors are returned as an 'errors' array; no credits are charged on 4xx.</td></tr><tr><td>Remove Image Background As Binary File</td><td><code>removeImageBackgroundBinary</code></td><td>Same endpoint as Remove Image Background, but requests the raw image bytes instead of the JSON envelope. remove.bg returns the cut-out as a binary PNG, JPG, WebP or ZIP file; the Fastn engine wraps those bytes as a file envelope with name, mime, size and base64 'data'. Use this when you want to hand the result straight to a file store or upload step; use Remove Image Background instead when you also need the foreground bounding box. Supply exactly one image source: image_url or image_file_b64. Output size 'preview' is free; 'full' and 'auto' charge account credits.</td></tr><tr><td>Submit Image To Improvement Program</td><td><code>submitImageToImprovementProgram</code></td><td>Submits an image to the remove.bg Improvement Program so remove.bg can train on images it currently handles poorly and produce better results for similar images in future. Returns the id of the submitted image. Supply exactly one image source: image_url or image_file_b64. Limits are 22 MB file size, 50 megapixels input resolution and 100 files per day. Submitting through the API constitutes agreement to the Improvement Program Conditions at https://www.remove.bg/ipc; submissions are used on a best-effort basis and improvements typically take several weeks to take effect. This call consumes no credits.</td></tr></tbody></table>

