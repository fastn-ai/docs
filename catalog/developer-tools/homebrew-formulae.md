---
description: "Homebrew is a package manager for macOS and Linux. Get formula and cask details, list all packages and read install analytics."
hidden: true
---

# Homebrew Formulae

<img src="../../.gitbook/assets/connectors/lg/homebrew-formulae.png" alt="Homebrew Formulae logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [brew.sh](https://brew.sh) |
| **Authentication** | No sign-in needed |
| **Slug** | `homebrewFormulae` |

## Setup

Homebrew Formulae needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Homebrew Formulae from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Homebrew Formulae**.
2. Select **Connect** on the Homebrew Formulae card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Homebrew Formulae needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Homebrew Formulae's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Cask</td><td><code>getCask</code></td><td>Get the metadata of one Homebrew/cask cask: names, version, download URL, artifacts, dependencies and analytics Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>Get Formula</td><td><code>getFormula</code></td><td>Get the metadata of one Homebrew/core formula: versions, URLs, bottles, dependencies, conflicts, caveats and install analytics Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List All Casks</td><td><code>listCasks</code></td><td>List metadata for every current Homebrew/cask cask Large response (about 19 MB). Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List All Formulae</td><td><code>listFormulae</code></td><td>List brew info metadata for every current Homebrew/core formula Large response (about 30 MB). Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List Analytics Events</td><td><code>listAnalytics</code></td><td>Rank all formulae by one analytics event category over 30, 90 or 365 days Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List Cask Install Analytics</td><td><code>listCaskAnalytics</code></td><td>Get install counts for every Homebrew/cask cask, grouped by cask token Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List Core Formula Analytics</td><td><code>listCoreFormulaAnalytics</code></td><td>Get analytics counts for every Homebrew/core formula grouped by formula name Docs: https://formulae.brew.sh/docs/api/</td></tr></tbody></table>

