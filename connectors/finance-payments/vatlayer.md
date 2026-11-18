---
description: "Vatlayer is a lightweight EU VAT compliance API by APILayer."
hidden: true
---

# Vatlayer

<img src="../../.gitbook/assets/connectors/lg/vatlayer.png" alt="Vatlayer logo">

Vatlayer is a lightweight EU VAT compliance API by APILayer. It validates EU VAT numbers against VIES and returns company name/address, looks up current VAT rates (standard and reduced) for a single EU member state or all 28 at once, lists the reduced-rate goods categories, and calculates VAT-compliant prices (forward or reverse) for a given amount and country.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [vatlayer.com](https://vatlayer.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `vatlayer` |

## Use it

Add Vatlayer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.vatlayer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Calculate VAT Compliant Price | `calculateVatPrice` | Calculates a VAT-compliant price for a given amount and EU country. Locate the country with exactly one of country_code, ip_address, or use_client_ip. Optionally restrict to a reduced-rate goods type (from Get Reduced VAT Rate Types), and optionally set incl=1 to treat the supplied amount as already VAT-inclusive and reverse-calculate the pre-VAT price. |
| Get All EU VAT Rates | `getAllVatRates` | Returns standard and reduced VAT rates for all 28 EU member states in a single call. The response is significantly larger than the single-country rate endpoint. |
| Get Reduced VAT Rate Types | `getVatRateTypes` | Returns the full list of reduced-VAT-rate goods/services category names usable as the 'type' parameter on the price calculation action. Calling this endpoint does not count against the monthly API request quota. |
| Get VAT Rate | `getVatRate` | Returns the standard and reduced VAT rates for a single country, located either by 2-letter EU country code, a custom IP address, or the calling client's own IP address. Provide exactly one of country_code, ip_address, or use_client_ip. A non-EU country/IP returns a rate of 0 rather than an error. |
| Validate VAT Number | `validateVatNumber` | Validates an EU VAT number against the VIES registry and returns the associated company name and address when valid. |
