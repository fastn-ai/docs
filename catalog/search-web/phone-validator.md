---
description: "Phone Validator checks phone numbers worldwide. Validate a number and get its line type, carrier and location."
hidden: true
---

# Phone Validator

<img src="../../.gitbook/assets/connectors/lg/phone-validator.png" alt="Phone Validator logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [phonevalidator.com](https://phonevalidator.com) |
| **Authentication** | API key |
| **Slug** | `phoneValidator` |

## Setup

Your customers enter their API key for Phone Validator when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Phone Validator from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Phone Validator**.
2. Select **Connect** on the Phone Validator card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Phone Validator's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Validate Phone Number</td><td><code>validatePhoneNumber</code></td><td>Look up a phone number worldwide using Phone Validator API v4 (the current version). Set type=basic for line type, carrier, location, country and fake-number detection, or type=fake for a stand-alone fake-number check. The HTTP status is always 200 - read the StatusCode field in the body: "200" means OK, "501" bad request, "502" account not active, "503" unauthorized, "504" insufficient funds, "500" unexpected error or access denied. The test number 7029270000 is free and is not billed.</td></tr><tr><td>Validate Phone Number (API v1)</td><td><code>validatePhoneNumberV1</code></td><td>Look up a U.S. or Canadian phone number using the original Phone Validator API v1. Superseded by v2 on 2020-07-10 but kept online indefinitely for existing integrations; new work should use Validate Phone Number (v4). v1 offers the basic, detail (area code prefix status and wireless flag) and deactivation lookups, combined with a comma-separated type. The HTTP status is always 200 - read the StatusCode field in the body. The test number 7029270000 is free and is not billed.</td></tr><tr><td>Validate Phone Number (API v2)</td><td><code>validatePhoneNumberV2</code></td><td>Look up a U.S. or Canadian phone number using Phone Validator API v2. Superseded by v3 on 2021-11-24 but kept online indefinitely for existing integrations; new work should use Validate Phone Number (v4). v2 is the only generation besides v1 that offers the detail (ported) and deactivation lookups. Combine lookups by passing a comma-separated type, e.g. basic,detail,deactivation. The HTTP status is always 200 - read the StatusCode field in the body. The test number 7029270000 is free and is not billed.</td></tr><tr><td>Validate Phone Number (API v3)</td><td><code>validatePhoneNumberV3</code></td><td>Look up a U.S. or Canadian phone number using Phone Validator API v3. Superseded by v4 on 2026-03-18 but kept online indefinitely for existing integrations; use Validate Phone Number (v4) for new work and for numbers outside the U.S. and Canada. Set type=basic for line type, carrier, location and fake-number information, or type=fake for a stand-alone fake-number check. The HTTP status is always 200 - read the StatusCode field in the body. The test number 7029270000 is free and is not billed.</td></tr></tbody></table>

