---
description: "Vatlayer is an EU VAT service. Validate VAT numbers, look up VAT rates and calculate VAT-compliant prices."
hidden: true
---

# Vatlayer

<img src="../../.gitbook/assets/connectors/lg/vatlayer.png" alt="Vatlayer logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [vatlayer.com](https://vatlayer.com) |
| **Authentication** | API key |
| **Slug** | `vatlayer` |

## Setup

Your customers enter their API key for Vatlayer when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Vatlayer from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Vatlayer**.
2. Select **Connect** on the Vatlayer card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Vatlayer's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Calculate VAT Compliant Price</td><td><code>calculateVatPrice</code></td><td>Calculates a VAT-compliant price for a given amount and EU country. Locate the country with exactly one of country_code, ip_address, or use_client_ip. Optionally restrict to a reduced-rate goods type (from Get Reduced VAT Rate Types), and optionally set incl=1 to treat the supplied amount as already VAT-inclusive and reverse-calculate the pre-VAT price.</td></tr><tr><td>Get All EU VAT Rates</td><td><code>getAllVatRates</code></td><td>Returns standard and reduced VAT rates for all 28 EU member states in a single call. The response is significantly larger than the single-country rate endpoint.</td></tr><tr><td>Get Reduced VAT Rate Types</td><td><code>getVatRateTypes</code></td><td>Returns the full list of reduced-VAT-rate goods/services category names usable as the 'type' parameter on the price calculation action. Calling this endpoint does not count against the monthly API request quota.</td></tr><tr><td>Get VAT Rate</td><td><code>getVatRate</code></td><td>Returns the standard and reduced VAT rates for a single country, located either by 2-letter EU country code, a custom IP address, or the calling client's own IP address. Provide exactly one of country_code, ip_address, or use_client_ip. A non-EU country/IP returns a rate of 0 rather than an error.</td></tr><tr><td>Validate VAT Number</td><td><code>validateVatNumber</code></td><td>Validates an EU VAT number against the VIES registry and returns the associated company name and address when valid.</td></tr></tbody></table>

