---
description: "Winston AI detects AI content and plagiarism. Check text for plagiarism and AI writing, detect AI images, compare texts and fact check."
hidden: true
---

# Winston AI

<img src="../../.gitbook/assets/connectors/lg/winston-ai.png" alt="Winston AI logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [gowinston.ai](https://gowinston.ai) |
| **Authentication** | Access token |
| **Slug** | `winstonAi` |

## Setup

Your customers enter their access token for Winston AI when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Winston AI from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Winston AI**.
2. Select **Connect** on the Winston AI card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Winston AI's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Call MCP Tool</td><td><code>callMcpTool</code></td><td>Invokes one of the Winston AI hosted Model Context Protocol tools (ai-text-detection, ai-image-detection or plagiarism-detection) through a JSON-RPC 2.0 tools/call request and returns the detection result as MCP content. The same credit costs as the REST endpoints apply: one credit per word for text detection, two credits per word for plagiarism and 300 credits per image. Never place the API key in the arguments; it is sent as an Authorization Bearer header.</td></tr><tr><td>Check Text For Plagiarism</td><td><code>checkPlagiarism</code></td><td>Scans text, a public document URL or a public web page against internet sources and returns a plagiarism score with every matching source, the matched word counts and the plagiarised sequences. Supply exactly one of Text, File or Website; a website takes priority over a file, and a file takes priority over text. Metered: two credits per word scanned, so this is the most expensive text endpoint.</td></tr><tr><td>Check Text For Plagiarism (Legacy v1)</td><td><code>checkPlagiarismV1</code></td><td>Legacy version 1 of the plagiarism endpoint, kept live by Winston AI but absent from the published documentation. It accepts raw text only, with no file or website input, and requires at least 16 words. Prefer Check Text For Plagiarism, which is the supported version 2 route; use this only for backwards compatibility with existing v1 integrations. Metered: two credits per word scanned.</td></tr><tr><td>Compare Two Texts</td><td><code>compareTexts</code></td><td>Compares two texts and returns an overall similarity score plus the matching segments, word counts and similarity percentage for each side. Metered: this endpoint consumes half a credit per word across both texts combined.</td></tr><tr><td>Detect AI Generated Image</td><td><code>detectAiImage</code></td><td>Analyses an image and returns a Human Score from 0 to 100 together with the AI and human probabilities, C2PA provenance metadata, EXIF data and any detected AI watermark issuers. Supply either a public image URL or a base64-encoded image. Accepted formats are JPG, JPEG, PNG and WEBP, minimum 256x256 pixels and about 4 MB or less. Metered: 300 credits per image.</td></tr><tr><td>Detect AI Generated Image (Legacy v1)</td><td><code>detectAiImageV1</code></td><td>Legacy version 1 of the AI image detection endpoint, kept live by Winston AI but absent from the published documentation. It analyses a public image URL or a base64-encoded image and returns a Human Score with the AI and human probabilities. Prefer Detect AI Generated Image, which is the supported version 2 route; use this only for backwards compatibility with existing v1 integrations. Metered: 300 credits per image.</td></tr><tr><td>Detect AI Generated Text</td><td><code>detectAiText</code></td><td>Scans text, a public document URL or a public web page and returns a Human Score from 0 to 100, where a low score means the content is likely AI generated. Supply exactly one of Text, File or Website; a website takes priority over a file, and a file takes priority over text. Metered: one credit per word scanned.</td></tr><tr><td>Detect AI Generated Text (Legacy v1)</td><td><code>detectAiTextV1</code></td><td>Legacy version 1 of the AI text detection endpoint, kept live by Winston AI but absent from the published documentation. It scans text, a public document URL or a public web page and returns a Human Score. Prefer Detect AI Generated Text, which is the supported version 2 route; use this only for backwards compatibility with existing v1 integrations. Metered: one credit per word scanned.</td></tr><tr><td>Fact Check Text</td><td><code>factCheckText</code></td><td>Extracts the factual claims from text, a public document URL or a public web page and verifies each one against trusted sources, returning a per-claim verdict, confidence score, explanation and supporting links plus an overall accuracy score. Supply exactly one of Text, File or Website. At most 12 claims are checked per request. Metered: two credits per word scanned.</td></tr><tr><td>Get Developer Account</td><td><code>getDeveloperAccount</code></td><td>Retrieves the Winston AI developer-dashboard account that owns the API key, including the user id, name, email, team id, locale, country, role and currency. This is the only non-metered read on the platform and consumes no credits; use it to validate a stored API key.</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Initialize MCP Session</td><td><code>initializeMcpSession</code></td><td>Performs the JSON-RPC 2.0 initialize handshake with the Winston AI hosted Model Context Protocol server and returns the negotiated protocol version, the server capabilities and the server name and version. Consumes no credits.</td></tr><tr><td>List MCP Tools</td><td><code>listMcpTools</code></td><td>Lists the tools exposed by the Winston AI hosted Model Context Protocol server, with each tool's title, description, credit cost and JSON Schema for its arguments. This is a JSON-RPC 2.0 tools/list call and consumes no credits.</td></tr><tr><td>Ping MCP Server</td><td><code>pingMcpServer</code></td><td>Sends a JSON-RPC 2.0 ping to the Winston AI hosted Model Context Protocol server to confirm it is reachable and the API key is accepted. Returns an empty result object and consumes no credits.</td></tr><tr><td>Run Advanced Image Forensics</td><td><code>runAdvancedImageForensics</code></td><td>Runs a deep forensic analysis on a public image URL using error-level analysis, residual noise maps, edge anomaly heat maps, CFA pattern analysis and metadata extraction, and returns a classification label, confidence, authenticity assessment, a written conclusion and the per-tool findings. The URL must be a public HTTP or HTTPS image address; localhost, private or reserved IP addresses and URLs carrying embedded credentials are rejected. SECURITY NOTE: the per-tool results for the image-rendering tools are returned as time-limited presigned Amazon S3 links that require no authentication, so anyone holding the link can view the forensic renderings of the submitted image until they expire. Metered: 500 credits per successful analysis, the most expensive endpoint on the platform.</td></tr></tbody></table>

</details>

