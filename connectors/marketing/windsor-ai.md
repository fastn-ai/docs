---
description: "Windsor.ai is a marketing data platform that unifies data from 350+ advertising, analytics, CRM and e-commerce sources behind one API."
hidden: true
---

# Windsor.ai

<img src="../../.gitbook/assets/connectors/lg/windsor-ai.png" alt="Windsor.ai logo">

This connector covers the complete Windsor.ai Connectors API and account-management API: querying any connector (or all sources at once) with field selection, date presets, filters and account selection; discovering connectors, fields and connector options; listing and executing write actions; listing connected accounts and custom fields; connector connect-info; and generating, listing and unlinking co-user authorization links.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [windsor.ai](https://windsor.ai) |
| **Authentication** | Credentials you enter |
| **Slug** | `windsorAi` |

## Use it

Add Windsor.ai from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.windsorAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Execute Write Action</td><td><code>executeWriteAction</code></td><td>Executes one write action (e.g. pause_campaign, create_campaign, set a budget) of a data source connector against one connected account, with parameters matching the action's JSON Schema from List Write Actions. Write actions must first be enabled for the team member under Settings &gt; API Access in Windsor.ai; otherwise the API returns 403 write_actions_disabled.</td></tr><tr><td>Generate Authorization Link</td><td><code>generateAuthorizationLink</code></td><td>Generates a co-user authorization link that lets a client or teammate connect their own data sources to your Windsor.ai team without sharing credentials. Optionally restrict the link to a single data source; otherwise the user may connect any supported source.</td></tr><tr><td>Get Connector Connect Info</td><td><code>getConnectorConnectInfo</code></td><td>Describes how a data source can be connected to the Windsor.ai account: whether it uses OAuth or manual credentials, a temporary connect URL that opens the right connection screen (expires after 4 days; treat it as a secret), and the credential fields required for manual connectors. Returns 404 for an unknown connector.</td></tr><tr><td>Get Connector Data</td><td><code>getConnectorData</code></td><td>Queries the data of one connected data source (e.g. facebook, google_ads, googleanalytics4) or of every connected source at once (connector = all). Select fields, a date range or preset, a JSON filter, specific accounts and the output renderer. Returns rows of the requested fields. Fails with 400 when no account of that source is connected.</td></tr><tr><td>Get Connector Fields</td><td><code>getConnectorFields</code></td><td>Returns the fields available for a data source connector (id, name, type, description), including any custom fields configured for the account. Use connector = all to list fields across every connector with the connectors each field is available in. Fails with 400 for a source with no connected account.</td></tr><tr><td>Get Connector Options</td><td><code>getConnectorOptions</code></td><td>Returns the configuration options a data source connector supports, such as the connected accounts to choose from, report types, breakdowns or reporting levels, each with its type and allowed values. Fails with 400 for a source with no connected account.</td></tr><tr><td>List Co-User Linked Accounts</td><td><code>listCoUserLinkedAccounts</code></td><td>Lists the accounts that clients or teammates connected to your team through co-user authorization links, optionally filtered by data source or by the access token of a specific link. Available to the team owner only (co-users receive 403).</td></tr><tr><td>List Connected Accounts</td><td><code>listConnectedAccounts</code></td><td>Returns the data source accounts connected to the Windsor.ai workspace, for all data sources or for one specific source, with account name, id and status.</td></tr><tr><td>List Connectors</td><td><code>listConnectors</code></td><td>Returns the identifiers of every data source connector available through the Windsor.ai API (e.g. facebook, google_ads, googleanalytics4), including the special all connector that queries every connected source at once.</td></tr><tr><td>List Custom Fields</td><td><code>listCustomFields</code></td><td>Returns the custom fields defined in the Windsor.ai workspace, which can be referenced in data queries and enrichments across supported data sources.</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Write Actions</td><td><code>listWriteActions</code></td><td>Lists the write actions a data source connector supports (for example pause_campaign or create_campaign), each with a JSON Schema describing its parameters. Use connector = all to list the actions of every connector, each tagged with its connector.</td></tr><tr><td>Unlink Co-User Account</td><td><code>unlinkCoUserAccount</code></td><td>Removes an account that was connected through a co-user authorization link from your team, identified by its data source and account id (as returned by List Co-User Linked Accounts). OAuth-selected accounts are deselected rather than erased; other accounts are deleted and need a new authorization to reconnect. Team owner only; returns 404 when no linked account matches.</td></tr></tbody></table>

</details>
