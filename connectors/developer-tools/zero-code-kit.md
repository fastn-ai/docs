---
description: "0CodeKit is a utility toolbox API for no-code and low-code automation, exposing stateless helpers for generation, conversion, PDF and image manipulation, text…"
hidden: true
---

# 0CodeKit

<img src="../../.gitbook/assets/connectors/zero-code-kit.png" alt="0CodeKit logo" width="64">

0CodeKit is a utility toolbox API for no-code and low-code automation, exposing stateless helpers for generation, conversion, PDF and image manipulation, text and AI processing, business validation, cryptography, date and time maths, storage bins and code execution.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [0codekit.com](https://0codekit.com) |
| **Authentication** | API key |
| **Slug** | `zeroCodeKit` |

## Use it

Add 0CodeKit from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zeroCodeKit.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add a Global Variable | `storageGlobalvariablesAdd` | Store a named value in the 0CodeKit global variable store so other automations can read it later. |
| Add a JSON Bin | `storageJsonAdd` | Store a JSON document in a new 0CodeKit bin and return the bin id used to read or update it. |
| Add Image Watermark to a PDF | `pdfWatermarkImage` | Lay a translucent image watermark over the pages of a PDF, optionally tiled. Either Width or Height must be supplied. |
| Add PDF Pages | `pdfPagesAdd` | Insert blank pages into a PDF at the given page positions. |
| Add Scheduler Task | `operatorSchedulerAdd` | Schedule 0CodeKit to POST a fixed payload to your webhook URL once, on a cron expression, or at a regular interval. This is the vendor's only outbound push mechanism. |
| Add Text Watermark to a PDF | `pdfWatermarkText` | Lay a translucent text watermark over the pages of a PDF, optionally tiled across each page. |
| Blur an Image | `imageBlur` | Apply a Gaussian blur to an image supplied by URL or Base64 buffer. |
| Build UTM Link | `operatorUtmBuild` | Append UTM campaign parameters to a URL and return the tagged tracking link. |
| Calculate BMI | `calculateBmi` | Calculate body mass index from weight and height, with a classification, desirable body weight, daily calories and macronutrient split. |
| Calculate Geographical Distance | `calculateGeodistanceV2` | Calculate the travel distance and duration between two addresses or coordinate pairs for a given travel mode. |

<details>

<summary>See 159 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Call a 0CodeKit Endpoint | `mcpCall` | Invoke any 0CodeKit endpoint indirectly by naming its path and supplying its request body. |
| Check Auth Status | `saasAuth` | Verify that the stored API key is accepted by 0CodeKit. Useful as a lightweight connection health check. |
| Check Content Policy | `aiCheckcontentpolicy` | Check a piece of text against the AI content policy and report whether it is considered safe. |
| Check for Free Email Provider | `businessIsfreemail` | Tell whether an email address belongs to a free consumer provider such as Gmail rather than a company domain. |
| Check Rate Limit Traffic Light | `operatorTrafficlight` | Throttle a workflow: returns true only once per named counter within the given interval, so later calls in the same window are blocked. |
| Check Whether a Date Is a Weekend | `dateandtimeIsweekend` | Return the weekday for a date and whether it falls on a weekend. |
| Compare Two Strings | `textComparestring` | Measure how similar two strings are, returning a similarity ratio and an edit distance. |
| Compress a PDF | `pdfCompress` | Shrink the file size of a PDF by recompressing its contents. |
| Concatenate Audio Files | `operatorConcatAudio` | Join several audio files into one track, optionally inserting silence between them. |
| Convert an Image | `imageConvert` | Convert an image into another format such as PNG, JPEG or WebP, with codec quality options. |
| Convert CSV to Array | `convertCsvArray` | Turn a CSV document into a two dimensional array of rows and columns. |
| Convert CSV to JSON | `convertCsvJson` | Turn a CSV document into an array of JSON objects keyed by the header row. |
| Convert Currency | `convertCurrency` | Convert an amount from one currency to another at the current or a historical exchange rate. |
| Convert DOCX to PDF | `pdfDocxToPdf` | Convert a Word DOCX document into a PDF. |
| Convert HTML to Image | `imageHtml` | Render HTML markup or a live web page into a screenshot image. |
| Convert HTML to PDF | `pdfHtml` | Render HTML markup or a live web page into a PDF, with page format, margins and header or footer controls. |
| Convert Markdown to PDF | `pdfMarkdownstringtopdf` | Render a Markdown document into a PDF, optionally styled with your own CSS. |
| Convert Nation Name and ISO Code | `convertNationiso` | Translate between a country name and its ISO country code in either direction. Supply whichever one you have. |
| Convert Outlook MSG to JSON | `convertMsgtojson` | Parse an Outlook .msg item file into structured JSON with its headers, body and attachments. |
| Convert PDF to Base64 | `pdfBase64` | Fetch a PDF by URL and return it Base64 encoded, ready to embed in another payload. |
| Convert PDF to Images | `pdfPdfToImage` | Render each page of a PDF as a PNG image and return one hosted URL per page. |
| Count PDF Pages | `pdfCount` | Return how many pages a PDF has. |
| Create an Empty PDF | `pdfCreate` | Create a blank PDF with a chosen number of pages and page size. |
| Create Saved Code | `editor` | Save a named code snippet in the 0CodeKit code editor so it can be executed later by its row key. |
| Create Shortened URL | `generateShortenedurlAdd` | Create a short link that redirects to a destination URL, optionally with a custom identifier. |
| Crop an Image | `imageCrop` | Cut a rectangular region out of an image by offset and size. |
| Decode a Barcode | `generateBarcodeDecode` | Read the value encoded in a barcode image, given the expected symbology. |
| Decode a JSON Web Token | `generateJsonwebtokenDecode` | Read the claims out of a JSON Web Token, optionally verifying its signature against a secret. |
| Decode a QR Code | `generateQrcodeDecode` | Read the text encoded in a QR code image supplied by URL or Base64 buffer. |
| Decrypt a PDF | `pdfDecrypt` | Remove the password protection from a PDF, given the password that opens it. |
| Decrypt Ciphertext | `cryptoDecrypt` | Decrypt a ciphertext produced by Encrypt Plaintext using the same cipher and secret key. |
| Delete a Global Variable | `storageGlobalvariablesDel` | Permanently remove a global variable by its id. |
| Delete a JSON Bin | `storageJsonDel` | Permanently delete a JSON bin and the document it holds. |
| Delete from Permanent Storage | `storagePermDel` | Permanently remove a file from 0CodeKit storage by its file id. |
| Delete Saved Code | `deleteEditor` | Delete a saved code snippet from the 0CodeKit code editor by its row key. |
| Delete Scheduler Task | `operatorSchedulerDel` | Stop and remove a scheduler task by its task id. |
| Delete Shortened URL | `generateShortenedurlDel` | Delete a short link so it stops redirecting. |
| Describe a 0CodeKit Endpoint | `mcpInfo` | Return the summary, description and request body schema of one 0CodeKit endpoint. |
| Detect Adult Content | `aiDetectadultcontent` | Analyse an image and score how likely it is to contain adult, racy or gory content. Consumes 0CodeKit AI credits. |
| Detect Brand | `aiDetectbrand` | Detect well-known commercial brands and logos visible in an image. |
| Detect Email Type | `aiDetectemailtype` | Classify an email into a type such as invoice, newsletter, support or other, from its subject and body. |
| Detect Faces | `aiDetectface` | Count the faces in an image and return the bounding box of each one. |
| Detect Gender from Name | `operatorGender` | Infer the likely gender behind a first name or a full name. |
| Detect Image Colors | `aiDetectcolor` | Return the dominant foreground, background and accent colours of an image and whether it is black and white. |
| Detect Image Labels | `aiPictureobjectrecognition` | Recognise the objects and concepts shown in an image and return them as descriptive labels. |
| Detect Language | `aiLanguagedetection` | Detect which natural language a piece of text is written in and return its ISO 639-1 code. |
| Detect Mood | `aiMooddetection` | Run sentiment analysis on text and return the overall mood, its scores and a per-sentence breakdown. |
| Detect Text Entities | `aiEntitydetection` | Identify named entities such as people, organisations, locations and quantities inside a block of text. |
| Detect Text in an Image | `aiPicturetextrecognition` | Run optical character recognition on an image and return every text string found in it. |
| Download a Stored File | `getFiles` | Download a file that 0CodeKit is hosting, using the file id and file name from the URL another endpoint returned. |
| Draw an Image on a PDF | `pdfDrawImage` | Place an image onto one or more pages of a PDF at a given position, size and rotation. |
| Draw Text on a PDF | `pdfDrawText` | Stamp a line of text onto one or more pages of a PDF at a given position, size, colour and rotation. |
| Edit PDF Metadata | `pdfMetadataEdit` | Write the title, author, subject and keywords into a PDF's document properties. |
| Embed Factur-X XML into a PDF | `businessFacturxEmbed` | Attach a Factur-X or ZUGFeRD invoice XML to an existing PDF so the document becomes a hybrid electronic invoice. The XML must pass Factur-X validation. |
| Encode a JSON Web Token | `generateJsonwebtokenEncode` | Sign a claim set into a JSON Web Token with the chosen algorithm and secret. |
| Encrypt a PDF | `pdfEncrypt` | Password protect a PDF with a user password and an optional owner password. |
| Encrypt Plaintext | `cryptoEncrypt` | Encrypt a plaintext message with a symmetric cipher and a secret key. |
| Evaluate Text Against a Regex | `textRegex` | Run a regular expression against a piece of text and return every match, plus whether the expression itself was valid. |
| Execute Async Python | `codeAsyncPython` | Queue a long-running Python script and get a task id back immediately. Poll Get Async Task Status, or have the result posted to a webhook. |
| Execute JavaScript Code | `codeJavascript` | Run a JavaScript snippet in the 0CodeKit sandbox and return whatever the script returns. |
| Execute Python Code | `codePython` | Run a Python snippet in the 0CodeKit sandbox and return whatever the script assigns to the result variable. |
| Execute Python Code (B2 Runtime) | `codePythonB2` | Run a Python snippet on 0CodeKit's alternative B2 runtime. Same contract as Execute Python Code, different execution backend. |
| Expand a Shortened URL | `operatorUrlexpander` | Follow the redirects of a shortened link and return the final destination URL. |
| Extract Audio from a Video | `operatorExtractAudio` | Strip the audio track out of a video file and return it in the chosen audio format. |
| Extract Contact Information | `aiExtractcontactinformation` | Extract name, phone, email, address and website from free-form text such as an email signature. |
| Extract Custom Object from Text | `aiExtractFromText` | Extract a custom set of named fields out of unstructured text, returning one key per requested field. |
| Extract Text Between Markers | `textExtractor` | Pull out the part of a text that sits between a start marker and an end marker. |
| Extract Text from an Image (Advanced OCR) | `aiAdvancedocr` | Run advanced OCR or structured field extraction on an image using a workflow configured in the 0CodeKit dashboard. The Workflow value must name a workflow that exists on your account. |
| Find Best Fuzzy Match | `aiFuzzyMatch` | Find the closest match for a query string within a list of candidate strings, using AI assisted fuzzy matching. |
| Flip an Image | `imageFlip` | Mirror an image along its horizontal or vertical axis. |
| Generate a Barcode | `generateBarcodeEncode` | Render a value as a barcode image in SVG, PNG or JPEG, with control over the symbology and label styling. |
| Generate a QR Code | `generateQrcodeEncode` | Render text or a URL as a QR code image, with control over size, margin, dot and corner styling and an optional centre logo. |
| Generate a Random City | `generateCity` | Generate a random city and country pair, useful as placeholder or test data. |
| Generate a Random Color | `generateColor` | Generate a random colour in the chosen notation, optionally steered by hue, luminosity, alpha and a seed. |
| Generate a Random Name | `generateName` | Generate a random person name, optionally constrained to a gender, with and without a middle name. |
| Generate Bar Chart | `generateChartBars` | Render a bar chart image from a series of values and their labels. |
| Generate Doughnut Chart | `generateChartDoughnut` | Render a doughnut chart image from a series of values and their labels. |
| Generate Image | `aiGenerateimage` | Generate one or more images from a text prompt. This is a high-cost metered endpoint that consumes a large number of 0CodeKit credits per image. |
| Generate JavaScript Code | `aiGeneratejavascriptcode` | Generate a JavaScript code snippet from a natural-language prompt using the 0CodeKit AI code generator. |
| Generate Line Chart | `generateChartLine` | Render a line chart image from a series of values and their labels, with optional fill and curve tension. |
| Generate Python Code | `aiGeneratepythoncode` | Generate a Python code snippet from a natural-language prompt using the 0CodeKit AI code generator. |
| Generate Random Number | `generateNumber` | Generate a random number within a given range, optionally as an integer, float or decimal rounded to a set number of decimal places. |
| Generate Random String | `generateString` | Generate a random string of a given length from a preset character set or a custom alphabet. |
| Generate User Mock Data | `generateMockdataUser` | Generate fake user records for testing, choosing which fields such as email, address or balance are included. |
| Get a Global Variable | `storageGlobalvariablesGet` | Read the current value of a named global variable. |
| Get a JSON Bin | `storageJsonGet` | Read the JSON document currently stored in a bin. |
| Get All Active Scheduler Tasks | `getResourceSchedulers` | Return every active scheduler task as a flat list, for dropdowns and pickers. |
| Get All Global Variables | `getResourceVariables` | Return every stored global variable as a flat list, for dropdowns and pickers. |
| Get All JSON Bins | `getResourceBin` | Return every JSON bin on the account as a flat list, for dropdowns and pickers. |
| Get All Shortened URLs | `getResourceShortenedUrls` | Return every short link on the account as a flat list, for dropdowns and pickers. |
| Get Async Task Status | `codeTaskstatus` | Poll an async Python task by its task id and read its status and result. |
| Get Code Editor Variables | `getEditorMakeVariables` | List the variable names a saved code snippet expects, so a caller knows what to pass when running it. |
| Get Image EXIF Data | `imageExif` | Read the EXIF metadata embedded in a photo. Images without EXIF data are rejected with a 400. |
| Get Monthly Date Details | `dateandtimeMonth` | Return the length of a month with its first and last day, and the list of workdays, Saturdays and Sundays it contains. |
| Get OpenAPI Documentation (Deprecated) | `getDocs` | Deprecated by 0CodeKit. Return the full OpenAPI document describing the 0CodeKit API. |
| Get PDF Info Metadata (Legacy) | `pdfGetinfometadata` | Legacy metadata reader that takes the PDF as a URL string in the Pdf field. Prefer Get PDF Metadata for new work. |
| Get PDF Metadata | `pdfMetadataInfo` | Read the document metadata of a PDF along with its page count and per-page dimensions. |
| Get Permanent File (Deprecated) | `storagePermGet` | Deprecated by 0CodeKit. Download a file from permanent storage by file id or name; prefer using the public URL returned by List Permanent Files instead. |
| Get Shortened URL | `generateShortenedurlGet` | Read the destination a short link currently points at. |
| Get Video Thumbnail | `operatorThumbnail` | Fetch the preview thumbnail of a video page such as YouTube or Vimeo. |
| Get Website Logo | `operatorLogo` | Find the logo or favicon of a website and return its URL, media type and size. |
| Hash a Message | `cryptoHash` | Hash a message with the selected algorithm, optionally as an HMAC when a secret key is supplied. |
| List 0CodeKit Endpoints | `getMcpList` | List every endpoint path 0CodeKit exposes through its MCP interface. |
| List Global Variables | `storageGlobalvariablesList` | List every global variable stored on the connected 0CodeKit account with its current value. |
| List JSON Bins | `storageJsonList` | List the ids of every JSON bin on the connected 0CodeKit account. |
| List Permanent Files | `storagePermList` | List the files held in permanent 0CodeKit storage together with the storage quota still available. |
| List Saved Code | `getEditor` | List every code snippet saved in the 0CodeKit code editor for this account. |
| List Saved Code by Language | `getEditorMake` | List the saved code snippets of one language, as shown in the automation picker. |
| List Scheduler Tasks | `operatorSchedulerList` | List every scheduler task currently registered on the connected 0CodeKit account. |
| List Shortened URLs | `generateShortenedurlList` | List every short link created on the connected 0CodeKit account. |
| Locate an IP Address | `convertIptogeo` | Resolve an IPv4 or IPv6 address to its country, region, city, coordinates, timezone and network operator. |
| Look Up VAT Rates | `businessLookupvatrates` | Return the standard, reduced, super reduced and parking VAT rates that apply in a country. |
| Merge Audio into a Video | `operatorMergeVideoAudio` | Combine a video file and an audio file into a single output video. This is a high-cost metered endpoint, around 1000 0CodeKit credits per call. |
| Merge PDF Files | `pdfMerge` | Join several PDFs into one document, optionally taking only selected pages from each source. |
| Open MCP SSE Connection | `getMcp` | Open the 0CodeKit MCP server-sent events stream, which hands out the session id used by Send MCP JSON-RPC Message. This is a long-lived stream and will time out in a request/response setting. |
| Overlay Two Images | `imageOverlay` | Composite a foreground image on top of a background image at a chosen position and opacity. |
| Parse HTML with a Selector | `operatorHtmlparserGet` | Extract elements from an HTML document, supplied inline or fetched from a URL, using a CSS, tag, id or class selector. |
| Parse URL Query Parameters | `operatorParseurlquery` | Split the query string of a URL into an object with one key per parameter. |
| Parse UTM Link | `operatorUtmParse` | Read the UTM campaign parameters back out of a tagged tracking link. |
| Put Data into a JSON Bin | `storageJsonPut` | Replace the JSON document held in an existing bin. |
| Read JSON Value by Key Path | `operatorAdvancedswitch` | Look up a value inside a JSON document using a dot-notation key path, either from an inline document or one fetched from a URL. |
| Redact Sensitive Information from a PDF | `aiRedactPdf` | Black out sensitive content in a PDF and return the redacted document. |
| Remove Duplicates from a List | `operatorDuplicate` | Return a copy of a list with duplicate entries removed, preserving the original order. |
| Remove Image Background | `aiRemovebg` | Remove the background from an image supplied by URL or Base64 buffer and return the cut-out image. |
| Remove PDF Pages | `pdfPagesRemove` | Delete the selected pages from a PDF. |
| Resize an Image | `imageResize` | Scale an image to a target width and height with a choice of fit mode, crop position and resampling kernel. |
| Resize PDF Pages | `pdfPagesResize` | Change the page size of the selected pages of a PDF. |
| Resolve Shortened URL | `getGenerateShortenedurlResolve` | Follow a 0CodeKit short link by its identifier and return the page it resolves to. |
| Retrieve Calendar Week | `dateandtimeCalendarweek` | Work out the calendar week for a date, or the first and last day of a given week number and year. |
| Retrieve Credit Balance | `userRetrievecredits` | Return the number of 0CodeKit credits left on the connected account. Call this before running metered endpoints such as AI, OCR or media conversion. |
| Retrieve Date Range Details | `dateandtimeDetailperiod` | Break a period that starts on a date and runs for a number of days into per-month segments with their working day counts. |
| Retrieve Public Holidays | `dateandtimeHolidays` | List the public holidays of a country, and optionally a state or region, for a given year. |
| Rotate an Image | `imageRotate` | Turn an image by a given angle, filling any exposed corners with a background colour. |
| Rotate PDF Pages | `pdfPagesRotate` | Turn the selected pages of a PDF by a multiple of 90 degrees. |
| Run OCR on a PDF | `aiPdfocr` | Run optical character recognition over every page of a PDF and return the recognised text. |
| Run Saved Code Snippet | `editorMake` | Execute a snippet saved in the 0CodeKit code editor, passing values for the variables it declares. |
| Scrape a Website | `generateHtmlScrape` | Fetch a web page and return its markup, or just its visible text when Text Only is set. |
| Search Keywords in Text | `textContains` | Check whether one keyword or a list of keywords appears in a text, and where each one was found. |
| Send MCP JSON-RPC Message | `mcpMessages` | Post a JSON-RPC message to an MCP session that was opened with Open MCP SSE Connection. The Session ID comes from that stream. |
| Sharpen an Image | `imageSharpen` | Increase the local contrast of an image to make its edges look crisper. |
| Split a Full Name | `operatorSplitname` | Split a full name string into its first name and last name parts. |
| Split a PDF | `pdfSplit` | Break a PDF into several documents, either at chosen page ranges or every n pages. |
| Summarize Long Text | `aiToolongtoread` | Produce a short AI summary of a long piece of text ("too long to read"). |
| Switch Timezone | `dateandtimeSwitchtimezone` | Convert a timestamp from one IANA timezone into another. |
| Transcribe Audio | `aiTranscribe` | Transcribe an audio file supplied by URL or Base64 buffer into plain text. |
| Translate Text | `aiTranslate` | Translate a piece of text into a target language given by its ISO 639-1 code. |
| Update a Global Variable | `storageGlobalvariablesUpdate` | Overwrite the value of an existing global variable. |
| Update Saved Code | `putEditor` | Replace the source, variables and language of a saved code snippet identified by its row key. |
| Update Shortened URL | `generateShortenedurlPut` | Point an existing short link at a different destination URL. |
| Upload a Temporary File | `storageTemp` | Upload a Base64 encoded file to short-lived 0CodeKit storage and get a public URL other endpoints can read from. |
| Upload to Permanent Storage | `storagePermAdd` | Copy a file into the account's permanent 0CodeKit storage, from a URL or a Base64 buffer, and return its file id and public URL. |
| Validate a BIC | `businessValidateBic` | Check that a bank identifier code (SWIFT BIC) is well formed. |
| Validate a Factur-X PDF | `businessFacturxValidate` | Check whether a PDF carries a valid embedded Factur-X or ZUGFeRD electronic invoice and report any schema errors. |
| Validate a Phone Number | `businessValidatePhonenumber` | Validate a phone number and return it in national and international formats with its country code. |
| Validate a VAT ID | `businessValidateVat` | Validate an EU VAT identification number against the VIES registry and return the registered name and address when the member state discloses them. |
| Validate an Email Address | `businessValidateEmail` | Check that an email address is well formed and deliverable, and suggest a correction for likely typos. |
| Validate an IBAN | `businessValidateIban` | Check that an IBAN has a valid structure and checksum. |
| Validate Geolocation | `businessValidateGeolocation` | Check that a postal address exists and return it in a normalised form. |
| Verify a Domain | `businessVerifyDomain` | Check that a domain resolves and return its registrable main domain. |

</details>
