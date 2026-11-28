---
description: "Genderize predicts details from a personal name. Predict gender, age and nationality."
hidden: true
---

# Genderize

<img src="../../.gitbook/assets/connectors/lg/genderize.png" alt="Genderize logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [genderize.io](https://genderize.io) |
| **Authentication** | API key |
| **Slug** | `genderize` |

## Setup

Your customers enter their API key for Genderize when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Genderize from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Genderize**.
2. Select **Connect** on the Genderize card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Genderize's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Predict Age</td><td><code>predictAge</code></td><td>Predicts the estimated age for a single first name or full name using Agify. Returns the estimated age in years (null when unknown) and the number of data points behind the prediction. Optionally scopes the prediction to a country with a two-letter ISO 3166-1 alpha-2 code.</td></tr><tr><td>Predict Gender</td><td><code>predictGender</code></td><td>Predicts the most likely gender for a single first name or full name using Genderize. Returns the gender (male or female, or null when unknown), a confidence probability between 0 and 1 and the number of data points behind the prediction. Optionally scopes the prediction to a country with a two-letter ISO 3166-1 alpha-2 code.</td></tr><tr><td>Predict Nationality</td><td><code>predictNationality</code></td><td>Predicts the most likely nationalities for a single last name or full name using Nationalize. Returns up to five candidate countries ordered by descending probability, each with a two-letter ISO country code and a confidence ratio, plus the number of data points behind the prediction.</td></tr></tbody></table>

