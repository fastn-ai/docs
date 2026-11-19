---
description: "Homebrew Formulae (formulae.brew.sh) is the free public JSON API of the Homebrew package manager."
hidden: true
---

# Homebrew Formulae

<img src="../../.gitbook/assets/connectors/lg/homebrew-formulae.png" alt="Homebrew Formulae logo">

Get metadata for any formula or cask (versions, download URLs, bottles, dependencies, caveats), list all formulae and casks, and read install, install-on-request, build-error and cask-install analytics. No API key needed.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [brew.sh](https://brew.sh) |
| **Authentication** | No authentication |
| **Slug** | `homebrewFormulae` |

## Use it

Add Homebrew Formulae from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.homebrewFormulae.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Cask</td><td><code>getCask</code></td><td>Get the metadata of one Homebrew/cask cask: names, version, download URL, artifacts, dependencies and analytics (GET /api/cask/{cask}.json). Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>Get Formula</td><td><code>getFormula</code></td><td>Get the metadata of one Homebrew/core formula: versions, URLs, bottles, dependencies, conflicts, caveats and install analytics (GET /api/formula/{formula}.json). Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List All Casks</td><td><code>listCasks</code></td><td>List metadata for every current Homebrew/cask cask (GET /api/cask.json). Large response (about 19 MB). Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List All Formulae</td><td><code>listFormulae</code></td><td>List brew info metadata for every current Homebrew/core formula (GET /api/formula.json). Large response (about 30 MB). Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List Analytics Events</td><td><code>listAnalytics</code></td><td>Rank all formulae by one analytics event category over 30, 90 or 365 days (GET /api/analytics/{category}/{days}.json). Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List Cask Install Analytics</td><td><code>listCaskAnalytics</code></td><td>Get install counts for every Homebrew/cask cask, grouped by cask token (GET /api/analytics/cask-install/homebrew-cask/{days}.json). Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List Core Formula Analytics</td><td><code>listCoreFormulaAnalytics</code></td><td>Get analytics counts for every Homebrew/core formula grouped by formula name (GET /api/analytics/{category}/homebrew-core/{days}.json). Docs: https://formulae.brew.sh/docs/api/</td></tr></tbody></table>
