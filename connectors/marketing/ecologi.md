---
description: "Ecologi lets businesses fund verified climate action - tree planting, carbon avoidance, permanent carbon removal and habitat restoration - directly from their…"
hidden: true
---

# Ecologi

<img src="../../.gitbook/assets/connectors/lg/ecologi.png" alt="Ecologi logo">

Ecologi lets businesses fund verified climate action - tree planting, carbon avoidance, permanent carbon removal and habitat restoration - directly from their own systems. This connector covers the full Ecologi public API: the Impact API for funding each impact type, and the Reporting API for reading any Ecologi profile's cumulative impact totals.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [ecologi.com](https://ecologi.com) |
| **Authentication** | Bearer token |
| **Slug** | `ecologi` |

## Use it

Add Ecologi from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ecologi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get User Carbon Avoided</td><td><code>getUserCarbonOffset</code></td><td>Returns the total tonnes of CO2e emissions an Ecologi profile has avoided through carbon avoidance projects, and how much of that is still pending settlement. Reads public profile data and works for any public Ecologi username. Totals refresh every 10 minutes.</td></tr><tr><td>Get User Carbon Removed</td><td><code>getUserCarbonRemoval</code></td><td>Returns the total tonnes of CO2e an Ecologi profile has permanently removed from the atmosphere through carbon removal projects such as biochar or enhanced rock weathering, and how much is still pending settlement. Reads public profile data and works for any public Ecologi username.</td></tr><tr><td>Get User Habitat Restored</td><td><code>getUserHabitatRestoration</code></td><td>Returns the total area of natural habitat an Ecologi profile has funded the restoration of, in square metres, and how much is still pending settlement. Reads public profile data and works for any public Ecologi username.</td></tr><tr><td>Get User Impact</td><td><code>getUserImpact</code></td><td>Returns a combined view of every impact type an Ecologi profile has funded - trees, carbon avoidance, carbon removal and habitat restoration - in a single request, together with the amounts still pending. Reads public profile data and works for any public Ecologi username. Totals refresh every 10 minutes.</td></tr><tr><td>Get User Profile</td><td><code>getUserProfile</code></td><td>Returns the full public Ecologi profile for a username: headline impact totals, account and subscription details, earned badges, per-project tree contributions, and the most recent impact tiles with their project and purchase source. Returns up to 100 tiles; the endpoint does not paginate.</td></tr><tr><td>Get User Trees</td><td><code>getUserTrees</code></td><td>Returns the total number of trees an Ecologi profile has funded, and how many of those are still pending settlement. Reads public profile data and works for any public Ecologi username. Totals refresh every 10 minutes.</td></tr><tr><td>Purchase Carbon Avoidance</td><td><code>purchaseCarbonOffset</code></td><td>Funds carbon avoidance credits, billed by the kilogram or the tonne, with a 1 kg (0.001 tonne) minimum. Funding may be split across several verified projects. Set Test Mode to true to validate a request and receive the expected response without being charged. This action spends real money against your Ecologi account balance when Test Mode is false.</td></tr><tr><td>Purchase Carbon Removal</td><td><code>purchaseCarbonRemoval</code></td><td>Funds permanent carbon removal such as biochar or enhanced rock weathering, billed by the kilogram with a 1 kg minimum. Set Test Mode to true to validate a request and receive the expected response without being charged. This action spends real money against your Ecologi account balance when Test Mode is false.</td></tr><tr><td>Purchase Habitat Restoration</td><td><code>purchaseHabitatRestoration</code></td><td>Funds the restoration of natural habitat such as wildflower meadow or seagrass bed, billed by the square metre with a 0.1 m2 minimum and one decimal place of precision. Set Test Mode to true to validate a request and receive the expected response without being charged. This action spends real money against your Ecologi account balance when Test Mode is false.</td></tr><tr><td>Purchase Local Trees</td><td><code>purchaseLocalTrees</code></td><td>Funds tree planting in a specific country, each of which has its own reforestation project and pricing. Set Test Mode to true to validate a request and receive the expected response without being charged. This action spends real money against your Ecologi account balance when Test Mode is false.</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Purchase Trees</td><td><code>purchaseTrees</code></td><td>Funds the planting of 1 to 250,000 trees, which are added to your Ecologi forest as pending until your next monthly invoice is paid. Set Test Mode to true to validate a request and receive the expected response without being charged. This action spends real money against your Ecologi account balance when Test Mode is false.</td></tr></tbody></table>

</details>
