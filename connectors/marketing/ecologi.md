---
description: "Ecologi lets businesses fund verified climate action - tree planting, carbon avoidance, permanent carbon removal and habitat restoration - directly from their…"
hidden: true
---

# Ecologi

Ecologi lets businesses fund verified climate action - tree planting, carbon avoidance, permanent carbon removal and habitat restoration - directly from their own systems. This connector covers the full Ecologi public API: the Impact API for funding each impact type, and the Reporting API for reading any Ecologi profile's cumulative impact totals.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [ecologi.com](https://ecologi.com) |
| **Authentication** | Bearer token |
| **Actions** | 11 |
| **Events** | 0 |
| **Slug** | `ecologi` |

## Use it

Add Ecologi from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ecologi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get User Carbon Avoided | `getUserCarbonOffset` | Returns the total tonnes of CO2e emissions an Ecologi profile has avoided through carbon avoidance projects, and how much of that is still pending settlement. Reads public profile data and works for any public Ecologi username. Totals refresh every 10 minutes. |
| Get User Carbon Removed | `getUserCarbonRemoval` | Returns the total tonnes of CO2e an Ecologi profile has permanently removed from the atmosphere through carbon removal projects such as biochar or enhanced rock weathering, and how much is still pending settlement. Reads public profile data and works for any public Ecologi username. |
| Get User Habitat Restored | `getUserHabitatRestoration` | Returns the total area of natural habitat an Ecologi profile has funded the restoration of, in square metres, and how much is still pending settlement. Reads public profile data and works for any public Ecologi username. |
| Get User Impact | `getUserImpact` | Returns a combined view of every impact type an Ecologi profile has funded - trees, carbon avoidance, carbon removal and habitat restoration - in a single request, together with the amounts still pending. Reads public profile data and works for any public Ecologi username. Totals refresh every 10 minutes. |
| Get User Profile | `getUserProfile` | Returns the full public Ecologi profile for a username: headline impact totals, account and subscription details, earned badges, per-project tree contributions, and the most recent impact tiles with their project and purchase source. Returns up to 100 tiles; the endpoint does not paginate. |
| Get User Trees | `getUserTrees` | Returns the total number of trees an Ecologi profile has funded, and how many of those are still pending settlement. Reads public profile data and works for any public Ecologi username. Totals refresh every 10 minutes. |
| Purchase Carbon Avoidance | `purchaseCarbonOffset` | Funds carbon avoidance credits, billed by the kilogram or the tonne, with a 1 kg (0.001 tonne) minimum. Funding may be split across several verified projects. Set Test Mode to true to validate a request and receive the expected response without being charged. This action spends real money against your Ecologi account balance when Test Mode is false. |
| Purchase Carbon Removal | `purchaseCarbonRemoval` | Funds permanent carbon removal such as biochar or enhanced rock weathering, billed by the kilogram with a 1 kg minimum. Set Test Mode to true to validate a request and receive the expected response without being charged. This action spends real money against your Ecologi account balance when Test Mode is false. |
| Purchase Habitat Restoration | `purchaseHabitatRestoration` | Funds the restoration of natural habitat such as wildflower meadow or seagrass bed, billed by the square metre with a 0.1 m2 minimum and one decimal place of precision. Set Test Mode to true to validate a request and receive the expected response without being charged. This action spends real money against your Ecologi account balance when Test Mode is false. |
| Purchase Local Trees | `purchaseLocalTrees` | Funds tree planting in a specific country, each of which has its own reforestation project and pricing. Set Test Mode to true to validate a request and receive the expected response without being charged. This action spends real money against your Ecologi account balance when Test Mode is false. |
| Purchase Trees | `purchaseTrees` | Funds the planting of 1 to 250,000 trees, which are added to your Ecologi forest as pending until your next monthly invoice is paid. Set Test Mode to true to validate a request and receive the expected response without being charged. This action spends real money against your Ecologi account balance when Test Mode is false. |
