---
description: "The Go Module Mirror (proxy.golang.org), Module Index (index.golang.org) and Checksum Database (sum.golang.org) are free public services run by Google for the…"
hidden: true
---

# Go Module Mirror

<img src="../../.gitbook/assets/connectors/lg/go-module-mirror.png" alt="Go Module Mirror logo">

The Go Module Mirror (proxy.golang.org), Module Index (index.golang.org) and Checksum Database (sum.golang.org) are free public services run by Google for the Go ecosystem. List module versions, get version info, go.mod files and the latest version, follow the feed of newly published module versions, and look up go.sum checksums. No API key needed.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [proxy.golang.org](https://proxy.golang.org) |
| **Authentication** | No authentication |
| **Slug** | `goModuleMirror` |

## Use it

Add Go Module Mirror from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.goModuleMirror.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Checksum Database Latest</td><td><code>getChecksumDbLatest</code></td><td>Get the latest signed tree head of the Go checksum database (GET sum.golang.org/latest). Docs: https://go.dev/ref/mod#checksum-database</td></tr><tr><td>Get Latest Module Version</td><td><code>getModuleLatest</code></td><td>Get JSON metadata of the latest version of a module (GET proxy.golang.org/{module}/@latest). Docs: https://go.dev/ref/mod#goproxy-protocol</td></tr><tr><td>Get Module go.mod</td><td><code>getModuleGoMod</code></td><td>Get the go.mod file of one module version (GET proxy.golang.org/{module}/@v/{version}.mod). Docs: https://go.dev/ref/mod#goproxy-protocol</td></tr><tr><td>Get Module Version Info</td><td><code>getModuleVersionInfo</code></td><td>Get JSON metadata (canonical version, commit time, origin VCS/URL/hash/ref) for one module version (GET proxy.golang.org/{module}/@v/{version}.info). Docs: https://go.dev/ref/mod#goproxy-protocol</td></tr><tr><td>List Module Index</td><td><code>listModuleIndex</code></td><td>List module versions newly cached by proxy.golang.org in chronological order, as newline-delimited JSON {Path, Version, Timestamp} (GET index.golang.org/index). Docs: https://index.golang.org/</td></tr><tr><td>List Module Versions</td><td><code>listModuleVersions</code></td><td>List the known tagged versions of a module, one per line (GET proxy.golang.org/{module}/@v/list). Docs: https://go.dev/ref/mod#goproxy-protocol</td></tr><tr><td>Lookup Module Checksum</td><td><code>lookupChecksum</code></td><td>Look up the go.sum lines (module and go.mod hashes) of a module version in the Go checksum database, with the signed tree head (GET sum.golang.org/lookup/{module}@{version}). Docs: https://go.dev/ref/mod#checksum-database</td></tr></tbody></table>
