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

## Use it

Add Homebrew Formulae from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.homebrewFormulae.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Cask</td><td><code>getCask</code></td><td>Get the metadata of one Homebrew/cask cask: names, version, download URL, artifacts, dependencies and analytics Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>Get Formula</td><td><code>getFormula</code></td><td>Get the metadata of one Homebrew/core formula: versions, URLs, bottles, dependencies, conflicts, caveats and install analytics Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List All Casks</td><td><code>listCasks</code></td><td>List metadata for every current Homebrew/cask cask Large response (about 19 MB). Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List All Formulae</td><td><code>listFormulae</code></td><td>List brew info metadata for every current Homebrew/core formula Large response (about 30 MB). Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List Analytics Events</td><td><code>listAnalytics</code></td><td>Rank all formulae by one analytics event category over 30, 90 or 365 days Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List Cask Install Analytics</td><td><code>listCaskAnalytics</code></td><td>Get install counts for every Homebrew/cask cask, grouped by cask token Docs: https://formulae.brew.sh/docs/api/</td></tr><tr><td>List Core Formula Analytics</td><td><code>listCoreFormulaAnalytics</code></td><td>Get analytics counts for every Homebrew/core formula grouped by formula name Docs: https://formulae.brew.sh/docs/api/</td></tr></tbody></table>

## Events

Homebrew Formulae has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
