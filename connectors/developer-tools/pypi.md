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

| Action | Slug | What it does |
| --- | --- | --- |
| Get File Provenance | `getFileProvenance` | Get the PEP 740 provenance object (attestation bundles and Trusted Publisher identity) for one distribution file (GET /integrity/{project}/{version}/{filename}/provenance). Files uploaded without attestations return 404. Docs: https://docs.pypi.org/api/integrity/ |
| Get Latest Updates Feed | `getLatestUpdatesFeed` | Get the RSS feed of the latest releases on PyPI with project, version, description and link (GET /rss/updates.xml). Docs: https://docs.pypi.org/api/feeds/ |
| Get Newest Packages Feed | `getNewestPackagesFeed` | Get the RSS feed of the newest projects created on PyPI with name, description and link (GET /rss/packages.xml). Docs: https://docs.pypi.org/api/feeds/ |
| Get Package Statistics | `getStats` | Get PyPI storage statistics: total size of all packages in bytes and the top 100 projects by size (GET /stats/). Docs: https://docs.pypi.org/api/stats/ |
| Get Project | `getProject` | Get a project's metadata at its latest version, its project URLs, the files of the latest release and known vulnerabilities (GET /pypi/{project}/json). Docs: https://docs.pypi.org/api/json/ |
| Get Project Files | `getProjectFiles` | List every distribution file (wheels and sdists) of all releases of a project with download URLs and hashes, from the Simple Repository JSON API (GET /simple/{project}/, PEP 691). Docs: https://docs.pypi.org/api/index-api/ |
| Get Project Releases Feed | `getProjectReleasesFeed` | Get the RSS feed of the latest releases of one project (GET /rss/project/{project}/releases.xml). Docs: https://docs.pypi.org/api/feeds/ |
| Get Release | `getRelease` | Get a project's metadata, files and known vulnerabilities for one release version (GET /pypi/{project}/{version}/json). Docs: https://docs.pypi.org/api/json/ |
