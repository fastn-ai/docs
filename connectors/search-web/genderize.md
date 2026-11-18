---
description: "Genderize predicts the most likely gender behind a personal name, returning a gender, a confidence probability and the number of records behind the…"
---

# Genderize

Genderize predicts the most likely gender behind a personal name, returning a gender, a confidence probability and the number of records behind the prediction, optionally scoped to a country. This connector covers the full Genderize API together with its sister Demografix services that share the same API key: Agify (predict age from a name) and Nationalize (predict nationality from a name), including single-name and batch lookups.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [genderize.io](https://genderize.io) |
| **Authentication** | Credentials you enter |
| **Actions** | 3 |
| **Events** | 0 |
| **Slug** | `genderize` |

## Use it

Add Genderize from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.genderize.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Predict Age | `predictAge` | Predicts the estimated age for a single first name or full name using Agify. Returns the estimated age in years (null when unknown) and the number of data points behind the prediction. Optionally scopes the prediction to a country with a two-letter ISO 3166-1 alpha-2 code. |
| Predict Gender | `predictGender` | Predicts the most likely gender for a single first name or full name using Genderize. Returns the gender (male or female, or null when unknown), a confidence probability between 0 and 1 and the number of data points behind the prediction. Optionally scopes the prediction to a country with a two-letter ISO 3166-1 alpha-2 code. |
| Predict Nationality | `predictNationality` | Predicts the most likely nationalities for a single last name or full name using Nationalize. Returns up to five candidate countries ordered by descending probability, each with a two-letter ISO country code and a confidence ratio, plus the number of data points behind the prediction. |
