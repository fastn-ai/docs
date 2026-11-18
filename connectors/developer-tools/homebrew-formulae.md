---
description: "Homebrew Formulae (formulae.brew.sh) is the free public JSON API of the Homebrew package manager."
hidden: true
---

# Homebrew Formulae

<img src="../../.gitbook/assets/connectors/homebrew-formulae.png" alt="Homebrew Formulae logo" width="64">

Homebrew Formulae (formulae.brew.sh) is the free public JSON API of the Homebrew package manager. Get metadata for any formula or cask (versions, download URLs, bottles, dependencies, caveats), list all formulae and casks, and read install, install-on-request, build-error and cask-install analytics. No API key needed.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [brew.sh](https://brew.sh) |
| **Authentication** | No authentication |
| **Slug** | `homebrewFormulae` |

## Use it

Add Homebrew Formulae from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.homebrewFormulae.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Cask | `getCask` | Get the metadata of one Homebrew/cask cask: names, version, download URL, artifacts, dependencies and analytics (GET /api/cask/{cask}.json). Docs: https://formulae.brew.sh/docs/api/ |
| Get Formula | `getFormula` | Get the metadata of one Homebrew/core formula: versions, URLs, bottles, dependencies, conflicts, caveats and install analytics (GET /api/formula/{formula}.json). Docs: https://formulae.brew.sh/docs/api/ |
| List All Casks | `listCasks` | List metadata for every current Homebrew/cask cask (GET /api/cask.json). Large response (about 19 MB). Docs: https://formulae.brew.sh/docs/api/ |
| List All Formulae | `listFormulae` | List brew info metadata for every current Homebrew/core formula (GET /api/formula.json). Large response (about 30 MB). Docs: https://formulae.brew.sh/docs/api/ |
| List Analytics Events | `listAnalytics` | Rank all formulae by one analytics event category over 30, 90 or 365 days (GET /api/analytics/{category}/{days}.json). Docs: https://formulae.brew.sh/docs/api/ |
| List Cask Install Analytics | `listCaskAnalytics` | Get install counts for every Homebrew/cask cask, grouped by cask token (GET /api/analytics/cask-install/homebrew-cask/{days}.json). Docs: https://formulae.brew.sh/docs/api/ |
| List Core Formula Analytics | `listCoreFormulaAnalytics` | Get analytics counts for every Homebrew/core formula grouped by formula name (GET /api/analytics/{category}/homebrew-core/{days}.json). Docs: https://formulae.brew.sh/docs/api/ |
