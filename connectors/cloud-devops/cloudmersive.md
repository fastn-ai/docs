---
description: "Cloudmersive is a multi-API platform providing document/data conversion, OCR, data validation, image recognition, virus scanning, NLP, and barcode generation…"
---

# Cloudmersive

Cloudmersive is a multi-API platform providing document/data conversion, OCR, data validation, image recognition, virus scanning, NLP, and barcode generation through a single unified REST API.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [cloudmersive.com](https://cloudmersive.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 7 |
| **Events** | 0 |
| **Slug** | `cloudmersive` |

## Use it

Add Cloudmersive from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cloudmersive.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert HTML to Text | `convertHtmlToText` | Converts an HTML string into extracted plain text, stripping tags and markup while preserving the readable content. |
| Generate Code-128 Barcode | `generateCode128Barcode` | Generates a Code-128 1D barcode image (PNG) encoding the given value, commonly used for shipping labels and inventory tracking. |
| Generate QR Code | `generateQrCode` | Generates a QR code image (PNG) encoding the given text, such as a URL, contact card, or plain message. |
| Validate Domain | `validateDomain` | Checks whether a domain name is syntactically valid and has valid DNS records (MX or A records), useful for validating a domain before sending email or provisioning a service. |
| Validate Email Address | `validateEmailAddress` | Performs a full validation of an email address, checking syntax, domain, and live SMTP mailbox verification, and reports whether the domain is a free provider or a disposable/temporary email service. |
| Validate Phone Number | `validatePhoneNumber` | Validates a phone number and returns its type (mobile, landline, VOIP, etc.), country, and normalized formats (E.164, international, national). |
| Validate VAT Number | `validateVatNumber` | Looks up a European Union VAT number and returns whether it is valid along with the registered business name and address. |
