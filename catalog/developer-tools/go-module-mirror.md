---
description: "The Go Module Mirror serves public Go modules. Look up module versions, go.mod files, checksums and the module index."
hidden: true
---

# Go Module Mirror

<img src="../../.gitbook/assets/connectors/lg/go-module-mirror.png" alt="Go Module Mirror logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [proxy.golang.org](https://proxy.golang.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `goModuleMirror` |

## Setup

Go Module Mirror needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Go Module Mirror from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Go Module Mirror**.
2. Select **Connect** on the Go Module Mirror card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Go Module Mirror needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Go Module Mirror's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Checksum Database Latest</td><td><code>getChecksumDbLatest</code></td><td>Get the latest signed tree head of the Go checksum database (GET sum.golang.org/latest). Docs: https://go.dev/ref/mod#checksum-database</td></tr><tr><td>Get Latest Module Version</td><td><code>getModuleLatest</code></td><td>Get JSON metadata of the latest version of a module (GET proxy.golang.org/{module}/@latest). Docs: https://go.dev/ref/mod#goproxy-protocol</td></tr><tr><td>Get Module go.mod</td><td><code>getModuleGoMod</code></td><td>Get the go.mod file of one module version (GET proxy.golang.org/{module}/@v/{version}.mod). Docs: https://go.dev/ref/mod#goproxy-protocol</td></tr><tr><td>Get Module Version Info</td><td><code>getModuleVersionInfo</code></td><td>Get JSON metadata (canonical version, commit time, origin VCS/URL/hash/ref) for one module version (GET proxy.golang.org/{module}/@v/{version}.info). Docs: https://go.dev/ref/mod#goproxy-protocol</td></tr><tr><td>List Module Index</td><td><code>listModuleIndex</code></td><td>List module versions newly cached by proxy.golang.org in chronological order, as newline-delimited JSON {Path, Version, Timestamp} (GET index.golang.org/index). Docs: https://index.golang.org/</td></tr><tr><td>List Module Versions</td><td><code>listModuleVersions</code></td><td>List the known tagged versions of a module, one per line (GET proxy.golang.org/{module}/@v/list). Docs: https://go.dev/ref/mod#goproxy-protocol</td></tr><tr><td>Lookup Module Checksum</td><td><code>lookupChecksum</code></td><td>Look up the go.sum lines (module and go.mod hashes) of a module version in the Go checksum database, with the signed tree head (GET sum.golang.org/lookup/{module}@{version}). Docs: https://go.dev/ref/mod#checksum-database</td></tr></tbody></table>

