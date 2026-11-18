---
description: "AltTextLab generates accessible, SEO-friendly alt text for images with AI."
hidden: true
---

# AltTextLab

<img src="../../.gitbook/assets/connectors/lg/alt-text-lab.png" alt="AltTextLab logo">

AltTextLab generates accessible, SEO-friendly alt text for images with AI. This connector covers the AltTextLab REST API: generate alt text for a public image URL or for base64 image data, in 130+ languages, with configurable writing style, SEO keywords, e-commerce product metadata, page context and pass-through custom fields.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [alttextlab.com](https://alttextlab.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `altTextLab` |

## Use it

Add AltTextLab from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.altTextLab.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate Alt Text from Image Data</td><td><code>generateAltTextFromImageData</code></td><td>Generates AI alt text for an image supplied inline as base64-encoded data instead of a public URL, which suits images that are private or not yet published. AltTextLab stores the upload temporarily and returns a signed URL for it in imageUrl. Accepts the same language, writing style, keyword, e-commerce, context and custom-field options as the URL variant. Credits are deducted only when the response status is "generated".</td></tr><tr><td>Generate Alt Text from Image URL</td><td><code>generateAltTextFromUrl</code></td><td>Generates AI alt text for an image at a publicly accessible URL, in the requested language and writing style, optionally guided by SEO keywords, e-commerce product metadata and surrounding page context. The image must be fetchable without authentication or redirects; if AltTextLab cannot fetch or process the image it returns a 500 AI_INTERNAL_SERVER_ERROR and no credits are used. Credits are deducted only when the response status is "generated".</td></tr></tbody></table>
