---
description: "The UK Parliament Register of Interests lists MPs' declared financial interests. Search interests and read registers and categories."
hidden: true
---

# UK Parliament Register of Interests API

<img src="../../.gitbook/assets/connectors/lg/uk-parliament-interests.png" alt="UK Parliament Register of Interests API logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [parliament.uk](https://parliament.uk) |
| **Authentication** | No sign-in needed |
| **Slug** | `ukParliamentInterests` |

## Setup

UK Parliament Register of Interests API needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect UK Parliament Register of Interests API from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **UK Parliament Register of Interests API**.
2. Select **Connect** on the UK Parliament Register of Interests API card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. UK Parliament Register of Interests API needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use UK Parliament Register of Interests API's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Interest Category</td><td><code>getCategory</code></td><td>Return details of an interest category by ID. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>Get Register</td><td><code>getRegister</code></td><td>Return a published version of a register of interests by ID. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>Get Registered Interest</td><td><code>getInterest</code></td><td>Return the latest version of an interest which has been published. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>List Interest Categories</td><td><code>listCategories</code></td><td>Return a list of categories interests should be registered under, sorted by category number. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>List Registers</td><td><code>listRegisters</code></td><td>Return a list of published versions of registers of interests. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr><tr><td>Search Registered Interests</td><td><code>searchInterests</code></td><td>Return a list of interests that have been published on a register. Docs: https://interests-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json)</td></tr></tbody></table>

