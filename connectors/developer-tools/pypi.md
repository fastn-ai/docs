---
description: "PyPI, the Python Package Index, is the official package registry for Python."
hidden: true
---

# PyPI

<img src="../../.gitbook/assets/connectors/lg/pypi.png" alt="PyPI logo">

PyPI, the Python Package Index, is the official package registry for Python. Get project and release metadata, files and known vulnerabilities, the PEP 691 simple index, file provenance (PEP 740 attestations), storage statistics and RSS feeds of new projects and releases. Public read APIs need no API key; send a descriptive User-Agent.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [pypi.org](https://pypi.org) |
| **Authentication** | No authentication |
| **Slug** | `pypi` |

## Use it

Add PyPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pypi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get File Provenance</td><td><code>getFileProvenance</code></td><td>Get the PEP 740 provenance object (attestation bundles and Trusted Publisher identity) for one distribution file (GET /integrity/{project}/{version}/{filename}/provenance). Files uploaded without attestations return 404. Docs: https://docs.pypi.org/api/integrity/</td></tr><tr><td>Get Latest Updates Feed</td><td><code>getLatestUpdatesFeed</code></td><td>Get the RSS feed of the latest releases on PyPI with project, version, description and link (GET /rss/updates.xml). Docs: https://docs.pypi.org/api/feeds/</td></tr><tr><td>Get Newest Packages Feed</td><td><code>getNewestPackagesFeed</code></td><td>Get the RSS feed of the newest projects created on PyPI with name, description and link (GET /rss/packages.xml). Docs: https://docs.pypi.org/api/feeds/</td></tr><tr><td>Get Package Statistics</td><td><code>getStats</code></td><td>Get PyPI storage statistics: total size of all packages in bytes and the top 100 projects by size (GET /stats/). Docs: https://docs.pypi.org/api/stats/</td></tr><tr><td>Get Project</td><td><code>getProject</code></td><td>Get a project's metadata at its latest version, its project URLs, the files of the latest release and known vulnerabilities (GET /pypi/{project}/json). Docs: https://docs.pypi.org/api/json/</td></tr><tr><td>Get Project Files</td><td><code>getProjectFiles</code></td><td>List every distribution file (wheels and sdists) of all releases of a project with download URLs and hashes, from the Simple Repository JSON API (GET /simple/{project}/, PEP 691). Docs: https://docs.pypi.org/api/index-api/</td></tr><tr><td>Get Project Releases Feed</td><td><code>getProjectReleasesFeed</code></td><td>Get the RSS feed of the latest releases of one project (GET /rss/project/{project}/releases.xml). Docs: https://docs.pypi.org/api/feeds/</td></tr><tr><td>Get Release</td><td><code>getRelease</code></td><td>Get a project's metadata, files and known vulnerabilities for one release version (GET /pypi/{project}/{version}/json). Docs: https://docs.pypi.org/api/json/</td></tr></tbody></table>
