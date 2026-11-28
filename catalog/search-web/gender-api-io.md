---
description: "GenderAPI.io predicts gender from names, emails and usernames. Look up single or multiple values and validate phone numbers."
hidden: true
---

# GenderAPI.io

<img src="../../.gitbook/assets/connectors/lg/gender-api-io.png" alt="GenderAPI.io logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [genderapi.io](https://genderapi.io) |
| **Authentication** | API key |
| **Slug** | `genderApiIo` |

## Setup

Your customers enter their API key for GenderAPI.io when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect GenderAPI.io from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **GenderAPI.io**.
2. Select **Connect** on the GenderAPI.io card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use GenderAPI.io's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Gender By Email</td><td><code>getGenderByEmail</code></td><td>Extracts a likely first name from a single email address and predicts its gender, returning the extracted name, predicted gender, confidence probability and country. Optionally adds country context and an AI fallback. Costs one credit.</td></tr><tr><td>Get Gender By Multiple Emails</td><td><code>getGenderByMultipleEmails</code></td><td>Extracts a likely first name from each of up to 50 email addresses and predicts its gender in one request, with optional per-record country context and your own record identifiers returned unchanged for correlation. Costs one credit per email.</td></tr><tr><td>Get Gender By Multiple Names</td><td><code>getGenderByMultipleNames</code></td><td>Predicts gender for up to 100 first names in one request, with optional per-record country context and your own record identifiers returned unchanged for correlation. Bulk requests do not use the AI fallback. Costs one credit per name.</td></tr><tr><td>Get Gender By Multiple Usernames</td><td><code>getGenderByMultipleUsernames</code></td><td>Extracts potential first names from up to 50 usernames or handles and predicts their gender in one request, with optional per-record country context and your own record identifiers returned unchanged for correlation. Bulk requests do not use the AI fallback. Costs one credit per username.</td></tr><tr><td>Get Gender By Name</td><td><code>getGenderByName</code></td><td>Predicts the gender of a single first name or full name, returning the predicted gender, confidence probability, most likely country and the number of samples behind the prediction. Optionally adds country context, an AI fallback for names not in the database, and forced predictions for nicknames. Costs one credit.</td></tr><tr><td>Get Gender By Username</td><td><code>getGenderByUsername</code></td><td>Extracts a potential first name from a single username, handle or nickname and predicts its gender, returning the extracted name, predicted gender, confidence probability and country. Optionally adds country context, an AI fallback and forced predictions for low-signal handles. Costs one credit.</td></tr><tr><td>Get Remaining Credits</td><td><code>getRemainingCredits</code></td><td>Returns the number of API credits currently available on the account and the package expiration time, without performing a gender lookup. Use it to monitor quota before running bulk jobs.</td></tr><tr><td>Validate Phone Number</td><td><code>validatePhoneNumber</code></td><td>Validates and formats an international phone number, returning national, international and E.164 representations plus validity, number type (mobile, landline, VoIP and more), region, area code and location metadata. Provide an address context such as a country code when the number is not in international format.</td></tr></tbody></table>

