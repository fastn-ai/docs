---
description: "Cloudmersive is a multi-API platform providing document/data conversion, OCR, data validation, image recognition, virus scanning, NLP, and barcode generation…"
hidden: true
---

# Cloudmersive

<img src="../../.gitbook/assets/connectors/lg/cloudmersive.png" alt="Cloudmersive logo">

Cloudmersive is a multi-API platform providing document/data conversion, OCR, data validation, image recognition, virus scanning, NLP, and barcode generation through a single unified REST API.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [cloudmersive.com](https://cloudmersive.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `cloudmersive` |

## Use it

Add Cloudmersive from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cloudmersive.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Convert HTML to Text</td><td><code>convertHtmlToText</code></td><td>Converts an HTML string into extracted plain text, stripping tags and markup while preserving the readable content.</td></tr><tr><td>Generate Code-128 Barcode</td><td><code>generateCode128Barcode</code></td><td>Generates a Code-128 1D barcode image (PNG) encoding the given value, commonly used for shipping labels and inventory tracking.</td></tr><tr><td>Generate QR Code</td><td><code>generateQrCode</code></td><td>Generates a QR code image (PNG) encoding the given text, such as a URL, contact card, or plain message.</td></tr><tr><td>Validate Domain</td><td><code>validateDomain</code></td><td>Checks whether a domain name is syntactically valid and has valid DNS records (MX or A records), useful for validating a domain before sending email or provisioning a service.</td></tr><tr><td>Validate Email Address</td><td><code>validateEmailAddress</code></td><td>Performs a full validation of an email address, checking syntax, domain, and live SMTP mailbox verification, and reports whether the domain is a free provider or a disposable/temporary email service.</td></tr><tr><td>Validate Phone Number</td><td><code>validatePhoneNumber</code></td><td>Validates a phone number and returns its type (mobile, landline, VOIP, etc.), country, and normalized formats (E.164, international, national).</td></tr><tr><td>Validate VAT Number</td><td><code>validateVatNumber</code></td><td>Looks up a European Union VAT number and returns whether it is valid along with the registered business name and address.</td></tr></tbody></table>
