---
description: "Copyleaks is an AI-powered content authenticity platform: plagiarism detection, AI-generated text, image and video detection, grammar checking, text…"
---

# Copyleaks

Copyleaks is an AI-powered content authenticity platform: plagiarism detection, AI-generated text, image and video detection, grammar checking, text moderation, object detection and image plagiarism search. This connector covers the Copyleaks REST API (https://api.copyleaks.com): account login, credit balance and usage history, submitting files, URLs and OCR images for authenticity scans, starting, deleting and re-notifying scans, exporting reports, the synchronous AI text, AI image, image plagiarism, object detection, grammar and text moderation checks, the asynchronous AI image and video detectors, supported languages and file types, and Private Cloud Hub repository information.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [copyleaks.com](https://copyleaks.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 23 |
| **Events** | 4 |
| **Slug** | `copyleaks` |

## Use it

Add Copyleaks from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.copyleaks.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Grammar | `checkGrammar` | Synchronously generates grammar, spelling, mechanics, sentence-structure and word-choice corrections plus readability and overall writing scores for a text of up to 25,000 characters, under a scan ID you choose. Set sandbox to true for free mock results. |
| Delete Scans | `deleteScans` | Deletes up to 10,000 scans by ID. With purge set to true every trace is permanently removed from Copyleaks servers, including Shared Data Hubs and Private Cloud Hubs. An optional completion webhook is called when the removal finishes. Returns 202 Accepted with an empty body; deletion runs asynchronously. |
| Detect AI Image | `detectAiImage` | Synchronously checks whether an image (base64-encoded, 512x512 to 6000x4500 px, under 32 MB) is AI-generated or partially AI-generated, under a scan ID you choose. Returns AI/human summary scores, flagged region ranges and any content-credential metadata found. Set sandbox to true for free mock results. |
| Detect AI Text | `detectAiGeneratedText` | Synchronously classifies a text of 255 to 100,000 characters as human-written or AI-generated under a scan ID you choose, with optional language hint, AI Logic explanation and sensitivity. Set sandbox to true for free mock results. Returns per-segment classifications with probabilities and an overall summary. |
| Export Scan | `exportScan` | Starts an export of a completed scan's raw data to your own servers: individual results, the PDF report and the crawled version are each pushed to the endpoint you specify, and a completion webhook is fired when all tasks finish. Returns 204 on acceptance, 404 for an unknown scan, 409 for a duplicate export ID. |
| Get AI Detector Credits | `getAiDetectorCredits` | Returns the number of AI Text Detector credits available in the account wallet. |
| Get Correction Types | `getCorrectionTypes` | Lists the correction types the Grammar Checker can report, with their identifiers, categories (1 sentence structure, 2 grammar, 3 word choice, 4 mechanics) and display texts in the requested language. |
| Get Credit Balance | `getCreditBalance` | Returns the number of scan credits currently available in the account. |
| Get Repository Information | `getRepositoryInformation` | Returns information about a Private Cloud Hub repository: name, description, permission, status, credit consumption and masking policy. The repository ID comes from the Copyleaks admin dashboard. |
| Get Usage History | `getUsageHistory` | Returns the account's scan usage history between two dates (inclusive) as a CSV file (columns Time, ScanID, Product, Units, Price), surfaced as a file object with base64 data. |
| List AI Text Detection File Types | `listAiTextDetectionFileTypes` | Lists the file extensions accepted by the AI text detection features (Detect AI Text file submissions and authenticity scans with aiGeneratedText.detect). |
| List Cross-Language Pairs | `listCrossLanguagePairs` | Lists the source and target languages supported for cross-language plagiarism detection (properties.scanning.crossLanguages). |
| List OCR Languages | `listOcrLanguages` | Lists the languages the Copyleaks OCR engine supports for extracting text from images and scanned documents, with the language codes accepted by Submit OCR Scan. |
| List Plagiarism File Types | `listPlagiarismFileTypes` | Lists the file formats accepted by plagiarism scans, grouped by category. |
| Login | `login` | Exchanges the connection's account email and API key for a Copyleaks login token (access_token) that is valid for 48 hours. Run it to obtain the token, then store the access_token in the connection's Login Token field; run it again to refresh before the token expires. This call itself needs no Bearer token. |
| Moderate Text | `moderateText` | Synchronously flags hateful, explicit, toxic or otherwise risky content in a text of up to 25,000 characters under a scan ID you choose, using the moderation labels you select (for example toxic-v1, profanity-v1, hate-speech-v1). Set sandbox to true for free mock results. Returns character ranges with their matched label index. |
| Resend Scan Webhook | `resendScanWebhook` | Asks Copyleaks to resend the status webhook for an existing scan, for example after your endpoint was unavailable. Returns 202 Accepted with an empty body. |
| Start Scans | `startScans` | Starts full scans for up to 100 scan IDs that were previously submitted in check-credits mode (properties.action 1). Scans not started within 48 hours of the price check are deleted. Returns the IDs that started and those that failed. |
| Submit AI Image Detection | `submitAiImageDetection` | Submits a publicly accessible image URL for asynchronous AI-generated content detection under a scan ID you choose, optionally with a pixel mask overlay and object detection. Results are delivered to the webhook URL you provide. Set sandbox to true for free mock results. Returns an empty body on acceptance. |
| Submit AI Video Detection | `submitAiVideoDetection` | Submits a publicly accessible video URL (mp4, avi, mov, mkv, webm) for asynchronous AI-generated content detection under a scan ID you choose. Results are delivered to the webhook URL you provide. Set sandbox to true for free mock results. Returns an empty body on acceptance. |
| Submit File Scan | `submitFileScan` | Submits a base64-encoded file (or plain text encoded as base64) for an authenticity scan under a scan ID you choose, with a file name that determines the file type. Progress and results are reported to the webhook URLs in properties.webhooks (status 0 completed / 1 error / 2 creditsChecked / 3 indexed); set properties.sandbox to true for free mock results. Returns 201 with an empty body on acceptance, or 409 when the scan ID already exists. |
| Submit OCR Scan | `submitOcrScan` | Submits a base64-encoded image containing text (pdf, docx, gif, png, bmp, jpg, jpeg) for an OCR authenticity scan under a scan ID you choose, with the language of the text. Progress and results are reported to the webhook URLs in properties.webhooks (status 0 completed / 1 error / 2 creditsChecked / 3 indexed); set properties.sandbox to true for free mock results. Returns 201 with an empty body on acceptance, or 409 when the scan ID already exists. |
| Submit URL Scan | `submitUrlScan` | Submits a public URL for an authenticity scan (plagiarism, AI-generated text detection, grammar feedback and more) under a scan ID you choose. Copyleaks crawls the URL and reports progress and results to the webhook URLs in properties.webhooks (status webhook payload: status 0 completed / 1 error / 2 creditsChecked / 3 indexed with scannedDocument and results); set properties.sandbox to true for free mock results. Returns 201 with an empty body on acceptance, or 409 when the scan ID already exists. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Credits Checked | `2` | Fired when a scan submitted with properties.action 1 (check credits) has been priced. Pass this trigger's URL as properties.webhooks.status when submitting. The payload carries status 2 and the number of credits the full scan will cost; call Start Scans within 48 hours to run it. |
| Document Indexed | `3` | Fired when a document submitted with properties.action 2 (index only) has been indexed in the Shared Data Hub or a repository. Pass this trigger's URL as properties.webhooks.status when submitting. The payload carries status 3. |
| Scan Completed | `0` | Fired when an authenticity scan finishes successfully. Copyleaks has no webhook registration API: when you submit a scan (Submit URL Scan, Submit File Scan or Submit OCR Scan) pass this trigger's URL as properties.webhooks.status, e.g. https://&lt;fastn-trigger-url&gt;?event={STATUS}. The status webhook payload carries status 0 for completed scans; the scanned document, results and score are in the body. |
| Scan Error | `1` | Fired when a scan ends with an error. Pass this trigger's URL as properties.webhooks.status when submitting the scan. The payload carries status 1 and an error object with type, id, code and message. |
