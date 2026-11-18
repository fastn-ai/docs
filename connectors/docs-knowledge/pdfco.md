---
description: "PDF.co is a document-automation API for converting, editing, splitting, merging, securing and extracting data from PDF and Office documents."
hidden: true
---

# PDF.co

PDF.co is a document-automation API for converting, editing, splitting, merging, securing and extracting data from PDF and Office documents. This connector covers the whole PDF.co v1 API: PDF conversion to and from every supported format, merge and split, page editing, text and image search-and-replace, rotation, optimisation and compression, form field reading, barcode generation and reading, OCR (make searchable/unsearchable), the document parser and its templates, the AI invoice parser, document classification, attachments, email decoding, attachment extraction and sending, file upload and storage, presigned upload URLs, file hashing and deletion, HTML templates, background job status checks and the account credit balance.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [pdf.co](https://pdf.co) |
| **Authentication** | API key |
| **Actions** | 68 |
| **Events** | 2 |
| **Slug** | `pdfco` |

## Use it

Add PDF.co from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pdfco.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Password to PDF | `addPasswordToPDF` | Encrypts a PDF with an owner and user password and applies security limitations such as blocking printing, editing or content extraction. |
| Add Text and Images to PDF | `pdfAdd` | Adds text annotations, images, links and other PDF content on top of an existing PDF, and fills existing form fields. Works on both native and scanned PDFs and returns the edited document. |
| AI Invoice Parser | `aiInvoiceParser` | Extracts structured data from an invoice document using PDF.co's AI invoice parser, regardless of the invoice layout. Returns the parsed fields as JSON. |
| Auto-Rotate PDF Pages with AI | `autoRotatePagesWithAI` | Corrects the rotation of pages in a scanned PDF automatically by analysing the text on each page with AI. |
| Check Background Job | `backgroundJobCheck` | Returns the status of a background job started by any action run with Run Asynchronously set to true. Poll it with the jobId until the status is success. |
| Classify Document | `documentClassifier` | Determines the class of a PDF, JPG or PNG document by analysing its content with built-in AI or with your own CSV classification rules. |
| Compress PDF | `pdfCompress` | Reduces the file size of a PDF using a preset compression profile or a detailed configuration, and returns a link to the smaller document. |
| Convert Excel to CSV | `excelToCSV` | Converts one worksheet of an XLS or XLSX workbook into a CSV file, with a configurable separator and quotation symbol. |
| Convert Excel to HTML | `excelToHtml` | Converts one worksheet of an XLS, XLSX or CSV file into HTML and returns a link to the result. |
| Convert Excel to JSON | `excelToJson` | Converts one worksheet of an XLS, XLSX or CSV file into JSON and returns a link to the result. |
| Convert Excel to PDF | `excelToPDF` | Converts one worksheet of an XLS, XLSX or CSV file into a PDF, optionally sizing pages automatically to fit the content. |
| Convert Excel to Text | `excelToText` | Converts one worksheet of an XLS, XLSX or CSV file into plain text and returns a link to the result. |
| Convert Excel to XML | `excelToXML` | Converts one worksheet of an XLS, XLSX or CSV file into XML and returns a link to the result. |
| Convert PDF to CSV | `pdfToCSV` | Converts a PDF or scanned image into CSV, preserving the document's columns, rows and tables. Uses OCR for scanned input. |
| Convert PDF to HTML | `pdfToHtml` | Converts a PDF or scanned image into HTML, either as rich HTML and CSS that keeps the original design or as plain HTML. |
| Convert PDF to JPG | `pdfToJPG` | Renders each selected page of a PDF as a high-quality JPEG image and returns the image links. |
| Convert PDF to JSON | `pdfToJson` | Converts a PDF or scanned image into a JSON representation that preserves text, fonts, images, vectors and formatting. |
| Convert PDF to JSON with AI | `pdfToJsonWithAI` | Converts a PDF or scanned image into structured JSON using PDF.co's AI layout analysis, producing cleaner semantic output than the plain JSON converter. |
| Convert PDF to PNG | `pdfToPNG` | Renders each selected page of a PDF as a high-quality PNG image and returns the image links. |
| Convert PDF to Text | `pdfToText` | Converts a PDF or scanned image to plain text with the page layout preserved, using AI layout analysis and OCR where needed. |
| Convert PDF to Text (Simple) | `pdfToTextSimple` | Extracts the raw text layer from a PDF without AI layout analysis or OCR. Faster and cheaper than Convert PDF to Text, but it cannot read scanned documents. |
| Convert PDF to TIFF | `pdfToTiff` | Renders a PDF as a high-quality TIFF image and returns the image link. |
| Convert PDF to WebP | `pdfToWebp` | Renders each selected page of a PDF as a high-quality WebP image and returns the image links. |
| Convert PDF to XLS | `pdfToXLS` | Converts a PDF or scanned image into a legacy Excel (.xls) workbook with the document's layout and fonts preserved. |
| Convert PDF to XLSX | `pdfToXlsx` | Converts a PDF or scanned image into an Excel (.xlsx) workbook with the document's layout and fonts preserved. |
| Convert PDF to XML | `pdfToXML` | Converts a PDF into XML carrying text values, tables, fonts, images and the position of each object on the page. |
| Create PDF from Document | `pdfFromDOC` | Converts a DOC, DOCX, RTF, TXT or XPS document into a PDF and returns a link to the result. |
| Create PDF from Email | `pdfFromEmail` | Converts an .eml or .msg email message into a PDF, optionally embedding or converting the message's attachments. |
| Create PDF from HTML | `pdfFromHtml` | Renders HTML markup, or a saved HTML template filled with Mustache data, into a PDF. Supply either HTML or a Template ID. |
| Create PDF from Image | `pdfFromImage` | Converts one or more JPG, PNG or TIFF images into a single PDF and returns a link to the result. |
| Create PDF from Spreadsheet | `pdfFromCSV` | Converts a CSV, XLS or XLSX spreadsheet into a PDF and returns a link to the result. |
| Create PDF from Web Page | `pdfFromURL` | Renders a web page to PDF, running the page's JavaScript before capture. Supports paper size, orientation, margins and custom page headers and footers. |
| Delete PDF Pages | `pdfDeletePages` | Removes the selected pages from a PDF and returns the shortened document. |
| Delete Temporary File | `deleteTemporaryFile` | Deletes a temporary file from PDF.co storage, whether it was uploaded by you or generated by another action. |
| Extract Data from Email File | `extractDataFromEmailFile` | Decodes an .eml or .msg email file and returns its parts: sender, recipients, subject, date, body and attachment list. |
| Extract Email Attachments | `extractEmailAttachment` | Extracts the files attached to an .eml or .msg email message and returns them inline or as download links. |
| Extract PDF Attachments | `extractAttachment` | Extracts the files attached inside a PDF document and returns them inline or as download links. |
| Find Tables in PDF with AI | `findTextInTableWithAI` | Scans a document with AI and returns every table it detects, with each table's page, coordinates and detected columns. |
| Find Text in PDF | `pdfFindText` | Finds text in a PDF and returns the page number and coordinates of every match. Supports regular-expression search. |
| Generate Barcode | `barcodesGenerator` | Generates a high-quality barcode image from a value. Supports QR Code, Data Matrix, Code 39, Code 128, PDF417 and many other symbologies. |
| Generate Pre-signed Upload URL | `generatePreSignedURL` | Returns a pre-signed URL to PUT a local file to, plus the URL the uploaded file will then be readable at. Use it for files too large for the direct upload actions. |
| Get Account Balance Info | `getAccountBalanceInfo` | Returns the number of API credits remaining on the PDF.co account. Free and does not consume credits. |
| Get File MD5 Hash | `getMD5HashOfFileByURL` | Returns a content hash of the file at a given URL, so you can detect whether a source document has changed. PDF.co currently returns a 64-character SHA-256 hash from this endpoint despite its MD5 name. |
| Get PDF Info | `pdfInfoReader` | Returns detailed information about a PDF document, including page count, author, title, creation and modification dates, page size, encryption status and security permissions. |
| List Document Parser Templates | `listAllTemplates` | Returns every Document Parser data-extraction template available to the account. |
| List HTML Templates | `returnAllTemplates` | Returns every HTML-to-PDF template available to the account, including the sample templates PDF.co ships with. |
| Make PDF Text Searchable | `makeTextSearchable` | Runs OCR over a scanned PDF or image and adds an invisible text layer, producing a PDF whose text can be searched, selected and copied. |
| Make PDF Text Unsearchable | `makeTextUnsearchable` | Flattens a PDF into images so its text can no longer be searched, selected or copied, producing a scan-like document. |
| Merge Mixed Documents into PDF | `mergeVariousDocumentType` | Merges a mixed set of documents into one PDF. Accepts PDF, DOC, DOCX, XLS, XLSX, RTF, images and ZIP archives of documents and images. |
| Merge PDF Files | `mergePDF` | Merges two or more PDF files into a single PDF document and returns a link to the result. |
| Optimize PDF (Retired) | `pdfOptimizeRetired` | Retired PDF size-optimization endpoint, kept for existing integrations. New work should use Compress PDF instead. |
| Parse Document | `parseDocument` | Extracts structured data from a document using a Document Parser extraction template, covering custom areas, form fields, tables and multi-page documents. Returns the extracted fields as JSON, YAML, XML or CSV. |
| Read Barcodes | `barcodesReader` | Reads barcodes from an image or PDF and returns each decoded value with its type, page and position. Supports QR Code, Code 128, EAN, Data Matrix, PDF417, GS1 and many other symbologies. |
| Read PDF Form Fields | `pdfFormsInfoReader` | Returns the fillable form fields found inside a PDF, with their names, types, current values and positions. Use it to discover field names before filling a form. |
| Remove Password from PDF | `removePasswordFromPDF` | Removes the password and security limitations from a protected PDF, given the password that opens it. |
| Retrieve Document Parser Template | `retrieveTemplateById` | Returns the full definition of a single Document Parser template by its identifier. |
| Retrieve HTML Template | `returnHtmlTemplateByID` | Returns a single HTML-to-PDF template by its identifier, including the template source and its sample data. |
| Rotate PDF Pages | `rotateSelectedPages` | Rotates the selected pages of a PDF by a given angle and returns the edited document. |
| Search and Delete Text in PDF | `pdfSearchAndDeleteText` | Finds one or more strings in a PDF and removes the matching text, optionally covering it with a solid patch, and returns the edited document. |
| Search and Replace Text in PDF | `searchAndReplaceWithText` | Finds text in a PDF and replaces it with new text, optionally using regular expressions, and returns the edited document. |
| Search and Replace Text with Image | `searchAndReplaceWithImage` | Finds text in a PDF and replaces each match with an image, for example stamping a signature image over a placeholder. |
| Send Email with Attachment | `sendEmailWithFile` | Sends an email through your own SMTP server, optionally attaching a file by URL. The message is delivered to real recipients, so use it only with addresses you control. |
| Split PDF by Pages | `splitPDF` | Splits a PDF into several PDF files using page indices or page ranges, and returns a link for each generated document. |
| Split PDF by Text Search | `splitPDFByTextSearch` | Splits a PDF wherever a search string appears, for example to break a batch scan apart on a barcode or an invoice heading. |
| Upload File from URL | `uploadFileFromURL2` | Downloads a file from a source URL and stores it as a PDF.co temporary file, using the POST form of the endpoint. Temporary files are deleted automatically after one hour. |
| Upload File from URL (GET) | `uploadFileFromURL` | Downloads a file from a source URL and stores it as a PDF.co temporary file, using the GET form of the endpoint. Temporary files are deleted automatically after one hour. |
| Upload File Using Base64 | `uploadFileUsingBase64` | Stores a file supplied as Base64 content in PDF.co storage and returns a URL other actions can read. Temporary files are deleted automatically after one hour unless stored permanently. |
| Upload Small File | `uploadSmallFile` | Stores a small file (up to 100 KB) in PDF.co temporary storage. This endpoint accepts multipart/form-data only, which the fastn executor cannot emit, so it answers 400 'No attached file found' when called from a workflow. Use Upload File Using Base64 or Upload File from URL instead; both return the same kind of temporary file URL. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Job Completed | `success` | Fires when a PDF.co job that was started asynchronously finishes successfully. PDF.co has NO webhook registration API: the only way to receive this event is to pass the fastn trigger URL as the Callback URL on the action itself. Setup: (1) copy this trigger's URL, (2) in the PDF.co action you want to be notified about, set Run Asynchronously to true and paste the URL into Callback URL, (3) run the action. PDF.co then POSTs the finished job to the trigger URL. This is per request, not per account, so it has to be done on every action you want events from. The callback endpoint must answer within 20-30 seconds or PDF.co retries up to 3 times. Payload schema captured from a real delivery on 2026-09-16. |
| Job Failed | `failed` | Fires when a PDF.co job that was started asynchronously fails, for example because the source file could not be downloaded. PDF.co has NO webhook registration API: the only way to receive this event is to pass the fastn trigger URL as the Callback URL on the action itself. Setup: (1) copy this trigger's URL, (2) in the PDF.co action, set Run Asynchronously to true and paste the URL into Callback URL, (3) run the action. This is per request, not per account. Note that a failed delivery carries no jobId and no output url, only the failure message. Payload schema captured from a real delivery on 2026-09-16. |
