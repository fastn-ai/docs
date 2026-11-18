---
description: "Winston AI is an AI-content-detection and plagiarism platform."
hidden: true
---

# Winston AI

<img src="../../.gitbook/assets/connectors/lg/winston-ai.png" alt="Winston AI logo">

Winston AI is an AI-content-detection and plagiarism platform. This connector covers the full public v2 REST API (AI text detection, AI image detection, advanced image forensics, plagiarism, fact checking and text comparison), the legacy v1 detection routes, the hosted Model Context Protocol server, and the developer-dashboard account endpoint. All endpoints are metered in credits.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [gowinston.ai](https://gowinston.ai) |
| **Authentication** | Bearer token |
| **Slug** | `winstonAi` |

## Use it

Add Winston AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.winstonAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Call MCP Tool | `callMcpTool` | Invokes one of the Winston AI hosted Model Context Protocol tools (ai-text-detection, ai-image-detection or plagiarism-detection) through a JSON-RPC 2.0 tools/call request and returns the detection result as MCP content. The same credit costs as the REST endpoints apply: one credit per word for text detection, two credits per word for plagiarism and 300 credits per image. Never place the API key in the arguments; it is sent as an Authorization Bearer header. |
| Check Text For Plagiarism | `checkPlagiarism` | Scans text, a public document URL or a public web page against internet sources and returns a plagiarism score with every matching source, the matched word counts and the plagiarised sequences. Supply exactly one of Text, File or Website; a website takes priority over a file, and a file takes priority over text. Metered: two credits per word scanned, so this is the most expensive text endpoint. |
| Check Text For Plagiarism (Legacy v1) | `checkPlagiarismV1` | Legacy version 1 of the plagiarism endpoint, kept live by Winston AI but absent from the published documentation. It accepts raw text only, with no file or website input, and requires at least 16 words. Prefer Check Text For Plagiarism, which is the supported version 2 route; use this only for backwards compatibility with existing v1 integrations. Metered: two credits per word scanned. |
| Compare Two Texts | `compareTexts` | Compares two texts and returns an overall similarity score plus the matching segments, word counts and similarity percentage for each side. Metered: this endpoint consumes half a credit per word across both texts combined. |
| Detect AI Generated Image | `detectAiImage` | Analyses an image and returns a Human Score from 0 to 100 together with the AI and human probabilities, C2PA provenance metadata, EXIF data and any detected AI watermark issuers. Supply either a public image URL or a base64-encoded image. Accepted formats are JPG, JPEG, PNG and WEBP, minimum 256x256 pixels and about 4 MB or less. Metered: 300 credits per image. |
| Detect AI Generated Image (Legacy v1) | `detectAiImageV1` | Legacy version 1 of the AI image detection endpoint, kept live by Winston AI but absent from the published documentation. It analyses a public image URL or a base64-encoded image and returns a Human Score with the AI and human probabilities. Prefer Detect AI Generated Image, which is the supported version 2 route; use this only for backwards compatibility with existing v1 integrations. Metered: 300 credits per image. |
| Detect AI Generated Text | `detectAiText` | Scans text, a public document URL or a public web page and returns a Human Score from 0 to 100, where a low score means the content is likely AI generated. Supply exactly one of Text, File or Website; a website takes priority over a file, and a file takes priority over text. Metered: one credit per word scanned. |
| Detect AI Generated Text (Legacy v1) | `detectAiTextV1` | Legacy version 1 of the AI text detection endpoint, kept live by Winston AI but absent from the published documentation. It scans text, a public document URL or a public web page and returns a Human Score. Prefer Detect AI Generated Text, which is the supported version 2 route; use this only for backwards compatibility with existing v1 integrations. Metered: one credit per word scanned. |
| Fact Check Text | `factCheckText` | Extracts the factual claims from text, a public document URL or a public web page and verifies each one against trusted sources, returning a per-claim verdict, confidence score, explanation and supporting links plus an overall accuracy score. Supply exactly one of Text, File or Website. At most 12 claims are checked per request. Metered: two credits per word scanned. |
| Get Developer Account | `getDeveloperAccount` | Retrieves the Winston AI developer-dashboard account that owns the API key, including the user id, name, email, team id, locale, country, role and currency. This is the only non-metered read on the platform and consumes no credits; use it to validate a stored API key. |
| Initialize MCP Session | `initializeMcpSession` | Performs the JSON-RPC 2.0 initialize handshake with the Winston AI hosted Model Context Protocol server and returns the negotiated protocol version, the server capabilities and the server name and version. Consumes no credits. |
| List MCP Tools | `listMcpTools` | Lists the tools exposed by the Winston AI hosted Model Context Protocol server, with each tool's title, description, credit cost and JSON Schema for its arguments. This is a JSON-RPC 2.0 tools/list call and consumes no credits. |
| Ping MCP Server | `pingMcpServer` | Sends a JSON-RPC 2.0 ping to the Winston AI hosted Model Context Protocol server to confirm it is reachable and the API key is accepted. Returns an empty result object and consumes no credits. |
| Run Advanced Image Forensics | `runAdvancedImageForensics` | Runs a deep forensic analysis on a public image URL using error-level analysis, residual noise maps, edge anomaly heat maps, CFA pattern analysis and metadata extraction, and returns a classification label, confidence, authenticity assessment, a written conclusion and the per-tool findings. The URL must be a public HTTP or HTTPS image address; localhost, private or reserved IP addresses and URLs carrying embedded credentials are rejected. SECURITY NOTE: the per-tool results for the image-rendering tools are returned as time-limited presigned Amazon S3 links that require no authentication, so anyone holding the link can view the forensic renderings of the submitted image until they expire. Metered: 500 credits per successful analysis, the most expensive endpoint on the platform. |
