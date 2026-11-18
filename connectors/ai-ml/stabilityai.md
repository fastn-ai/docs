---
description: "Stability AI generative media API."
hidden: true
---

# Stability AI

<img src="../../.gitbook/assets/connectors/lg/stabilityai.png" alt="Stability AI logo">

Stability AI generative media API. Text-to-image (Stable Image Ultra, Core, SD3.5), image editing (inpaint, outpaint, erase, search-and-replace, search-and-recolor, remove-background, replace-background-and-relight), upscaling (fast, conservative, creative), structural/style control, async results polling, Stable Audio 2 text-to-audio and audio-to-audio, 3D generation (Stable Fast 3D, Stable Point Aware 3D), plus v1 legacy generation and account/balance reads.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [stability.ai](https://stability.ai) |
| **Authentication** | Bearer token |
| **Slug** | `stabilityai` |

## Use it

Add Stability AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.stabilityai.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| 3D - Stable Fast 3D | `stableFast3d` | Generate a 3D asset (GLB) from a single 2D image. Sent as multipart/form-data (raw body with explicit boundary); every field declared in the input contract is now sent. KNOWN LIMITATION: the fastn executor UTF-8-expands binary multipart parts, so the image part cannot be delivered byte-accurately - this action is wired correctly but blocked by that engine gap. |
| 3D - Stable Point Aware 3D (async) | `stablePointAware3d` | Generate a higher-quality, point-aware 3D asset (GLB) from a 2D image. Async - returns 202 with id; poll Get Result. Sent as multipart/form-data (raw body with explicit boundary); every field declared in the input contract is now sent. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Audio - Audio to Audio (async) | `audioAudioToAudio` | Stable Audio 2: transform an input audio clip guided by a prompt. Async - returns 202 with id; poll Get Result. Sent as multipart/form-data (raw body with explicit boundary); every field declared in the input contract is now sent. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Audio - Text to Audio (async) | `audioTextToAudio` | Stable Audio 2: generate music/sound from a text prompt. Async - returns 202 with id; poll Get Result. Sent as multipart/form-data (raw body with explicit boundary); every field declared in the input contract is now sent. |
| Control - Sketch | `controlSketch` | Generate an image guided by the outlines/structure of a sketch input. Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary). NOTE: style_preset is not exposed - Stability rejects the empty enum the engine emits for an unset part. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Control - Structure | `controlStructure` | Generate an image preserving the structure/depth of a control image. Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary). NOTE: style_preset is not exposed - Stability rejects the empty enum the engine emits for an unset part. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Control - Style | `controlStyle` | Generate a new image in the visual style of a reference image, guided by a prompt. Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary); every field declared in the input contract is now sent. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Control - Style Transfer | `controlStyleTransfer` | Apply the visual aesthetic of a style image onto an init (subject) image without generating new content. Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary); every field declared in the input contract is now sent. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Edit - Erase | `editErase` | Remove unwanted objects using the image's alpha channel as the mask. Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary). NOTE: the separate mask file is not exposed - the engine cannot omit an unset multipart part, so an unused mask would be sent as an empty file and rejected. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Edit - Inpaint | `editInpaint` | Intelligently modify images by filling in or replacing the area masked by the image's alpha channel. Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary). NOTE: the separate mask file and style_preset are not exposed - the engine cannot omit an unset multipart part. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Edit - Outpaint | `editOutpaint` | Extend an image in any direction (left/right/up/down). Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary); every field declared in the input contract is now sent. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Edit - Remove Background | `editRemoveBackground` | Segment the foreground subject and remove the background. Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary). KNOWN LIMITATION: the fastn executor UTF-8-expands binary multipart parts, so the image part cannot be delivered byte-accurately. |
| Edit - Replace Background and Relight (async) | `editReplaceBackgroundAndRelight` | Async: replace the background of a subject and relight to match. Returns 202 with an id; poll Get Result. Sent as multipart/form-data (raw body with explicit boundary). NOTE: the optional reference images (light_reference, background_reference), light_source_direction and keep_original_background are not exposed - the engine cannot omit an unset multipart part, and Stability rejects an empty file, enum or boolean. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Edit - Search and Recolor | `editSearchAndRecolor` | Change the color of an object described by select_prompt. Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary); every field declared in the input contract is now sent. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Edit - Search and Replace | `editSearchAndReplace` | Replace an object described by search_prompt with the content of prompt, no mask required. Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary); every field declared in the input contract is now sent. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Generate - v1 Image to Image | `v1ImageToImage` | v1 legacy image-to-image for SDXL/SD1.6 engines. Returns array of base64 artifacts. Sent as multipart/form-data (raw body with explicit boundary); every field declared in the input contract is now sent. NOTE: style_preset is not exposed - Stability rejects the empty enum the engine emits for an unset part. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Generate - v1 Text to Image | `v1TextToImage` | v1 legacy text-to-image for SDXL/SD1.6 engines. JSON body. Returns array of base64 artifacts. |
| Generate Image - Core | `generateCore` | Stable Image Core: fast, affordable text-to-image. Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary). NOTE: style_preset is not settable through this connector - the engine cannot omit an unset multipart part and Stability rejects an empty enum value. |
| Generate Image - SD3 | `generateSd3` | Stable Diffusion 3.5 text-to-image. Model selectable (sd3.5-large/large-turbo/medium). Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary). NOTE: image-to-image mode is not exposed - it needs a binary multipart part, which the fastn executor cannot deliver byte-accurately. |
| Generate Image - Ultra | `generateUltra` | Stable Image Ultra: photorealistic, high-resolution text-to-image (based on SD3.5). Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary). NOTE: the image-to-image variant (image + strength) and style_preset are not exposed - the engine cannot omit an unset multipart part, and Stability rejects an empty image or enum value. |
| Get Account | `getAccount` | v1: get the authenticated account profile (email, id, organizations). FREE read — safe for credential validation. |
| Get Balance | `getBalance` | v1: get the account credit balance. FREE read — safe for credential validation. |
| Get Result (async poll) | `getResult` | Poll for the result of an async generation (creative upscale, replace-background-and-relight, audio, point-aware-3d). 202 = still processing; 200 = ready with base64 result. FREE/no extra credits to poll. |
| List Engines | `listEngines` | v1: list available generation engines/models. FREE read — safe for credential validation. |
| Upscale - Conservative | `upscaleConservative` | Conservative upscale to ~4K preserving original content with minimal alteration. Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary). KNOWN LIMITATION: the fastn executor UTF-8-expands binary multipart parts, so the image part cannot be delivered byte-accurately. |
| Upscale - Creative (async) | `upscaleCreative` | Async creative upscale to 4K, adds detail. Returns 202 with an id; poll Get Result. Sent as multipart/form-data (raw body with explicit boundary). NOTE: style_preset is not exposed - the engine cannot omit an unset multipart part and Stability rejects an empty enum. KNOWN LIMITATION: binary multipart parts are UTF-8-expanded by the executor. |
| Upscale - Fast | `upscaleFast` | Fast 4x upscale (lightweight). Returns base64 image in JSON. Sent as multipart/form-data (raw body with explicit boundary). KNOWN LIMITATION: the fastn executor UTF-8-expands binary multipart parts, so the image part cannot be delivered byte-accurately. |
