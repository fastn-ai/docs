---
description: "PyPI is the official Python package index. Get project and release details, files, provenance and feeds of new and updated packages."
hidden: true
---

# PyPI

<img src="../../.gitbook/assets/connectors/lg/pypi.png" alt="PyPI logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [pypi.org](https://pypi.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `pypi` |

## Setup

PyPI needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect PyPI from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **PyPI**.
2. Select **Connect** on the PyPI card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. PyPI needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use PyPI's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get File Provenance</td><td><code>getFileProvenance</code></td><td>Get the PEP 740 provenance object (attestation bundles and Trusted Publisher identity) for one distribution file Files uploaded without attestations return 404. Docs: https://docs.pypi.org/api/integrity/</td></tr><tr><td>Get Latest Updates Feed</td><td><code>getLatestUpdatesFeed</code></td><td>Get the RSS feed of the latest releases on PyPI with project, version, description and link Docs: https://docs.pypi.org/api/feeds/</td></tr><tr><td>Get Newest Packages Feed</td><td><code>getNewestPackagesFeed</code></td><td>Get the RSS feed of the newest projects created on PyPI with name, description and link Docs: https://docs.pypi.org/api/feeds/</td></tr><tr><td>Get Package Statistics</td><td><code>getStats</code></td><td>Get PyPI storage statistics: total size of all packages in bytes and the top 100 projects by size Docs: https://docs.pypi.org/api/stats/</td></tr><tr><td>Get Project</td><td><code>getProject</code></td><td>Get a project's metadata at its latest version, its project URLs, the files of the latest release and known vulnerabilities Docs: https://docs.pypi.org/api/json/</td></tr><tr><td>Get Project Files</td><td><code>getProjectFiles</code></td><td>List every distribution file (wheels and sdists) of all releases of a project with download URLs and hashes, from the Simple Repository JSON API, PEP 691). Docs: https://docs.pypi.org/api/index-api/</td></tr><tr><td>Get Project Releases Feed</td><td><code>getProjectReleasesFeed</code></td><td>Get the RSS feed of the latest releases of one project Docs: https://docs.pypi.org/api/feeds/</td></tr><tr><td>Get Release</td><td><code>getRelease</code></td><td>Get a project's metadata, files and known vulnerabilities for one release version Docs: https://docs.pypi.org/api/json/</td></tr></tbody></table>

