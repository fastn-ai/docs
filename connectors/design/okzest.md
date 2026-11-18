---
description: "OKZest generates personalised images from visual design templates."
hidden: true
---

# OKZest

OKZest generates personalised images from visual design templates. Use it to list the designs in your OKZest account, inspect the editable layers and URL parameters a design accepts, and render a personalised JPEG, PNG or WebP image from a design by overriding its text, colour, image and background layers at request time. Renders count against the account's monthly image allowance.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [okzest.com](https://okzest.com) |
| **Authentication** | API key |
| **Actions** | 4 |
| **Events** | 0 |
| **Slug** | `okzest` |

## Use it

Add OKZest from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.okzest.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Image | `createImage` | Renders a personalised image from an existing OKZest design and returns the image itself as binary data (JPEG by default, or PNG/WebP via format). The layer overrides are applied to that single render only and never change the stored design. Call Get Design Fields first to discover the design's valid layer_id values and properties. NOTE: each call consumes one image from the account's monthly allowance, and an unrecognised layer_id is silently ignored by OKZest rather than rejected. |
| Get Design | `getDesign` | Fetches a single OKZest design by its design_id. The response body is an array containing the one matching design, with its name, public render URL, project, accepted URL parameters, open counts and timestamps. An unknown or malformed design_id returns 400 with the plain-text body 'Invalid design id provided.' |
| Get Design Fields | `getDesignFields` | Lists every editable field of an OKZest design: the canvas size, background and output settings, plus one entry per editable property of each layer (keyed as layers[].text, layers[].color, layers[].image_url and so on, labelled with the owning layer's id). Call this before Create Image to discover the exact layer_id values and properties a design supports. An unknown design_id returns 400 with the plain-text body 'Invalid design id provided.' |
| List Designs | `listDesigns` | Lists every design (image template) in the OKZest account. Returns an array of designs, each with its design_id, name, public render URL, project, the optional URL parameters the design accepts, open counts and timestamps. Use the returned design_id with Get Design, Get Design Fields or Create Image. Takes no inputs: the OKZest REST API ignores filtering and pagination parameters on this route. |
