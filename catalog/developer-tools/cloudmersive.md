---
description: "Cloudmersive offers utility services for developers. Validate emails, phone numbers, domains and VAT numbers, convert HTML to text, and generate barcodes."
hidden: true
---

# Cloudmersive

<img src="../../.gitbook/assets/connectors/lg/cloudmersive.png" alt="Cloudmersive logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [cloudmersive.com](https://cloudmersive.com) |
| **Authentication** | API key |
| **Slug** | `cloudmersive` |

## Setup

Your customers enter their API key for Cloudmersive when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Cloudmersive from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Cloudmersive**.
2. Select **Connect** on the Cloudmersive card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Cloudmersive's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Convert HTML to Text</td><td><code>convertHtmlToText</code></td><td>Converts an HTML string into extracted plain text, stripping tags and markup while preserving the readable content.</td></tr><tr><td>Generate Code-128 Barcode</td><td><code>generateCode128Barcode</code></td><td>Generates a Code-128 1D barcode image (PNG) encoding the given value, commonly used for shipping labels and inventory tracking.</td></tr><tr><td>Generate QR Code</td><td><code>generateQrCode</code></td><td>Generates a QR code image (PNG) encoding the given text, such as a URL, contact card, or plain message.</td></tr><tr><td>Validate Domain</td><td><code>validateDomain</code></td><td>Checks whether a domain name is syntactically valid and has valid DNS records (MX or A records), useful for validating a domain before sending email or provisioning a service.</td></tr><tr><td>Validate Email Address</td><td><code>validateEmailAddress</code></td><td>Performs a full validation of an email address, checking syntax, domain, and live SMTP mailbox verification, and reports whether the domain is a free provider or a disposable/temporary email service.</td></tr><tr><td>Validate Phone Number</td><td><code>validatePhoneNumber</code></td><td>Validates a phone number and returns its type (mobile, landline, VOIP, etc.), country, and normalized formats (E.164, international, national).</td></tr><tr><td>Validate VAT Number</td><td><code>validateVatNumber</code></td><td>Looks up a European Union VAT number and returns whether it is valid along with the registered business name and address.</td></tr></tbody></table>

