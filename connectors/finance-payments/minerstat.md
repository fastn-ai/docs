---
description: "Minerstat is a crypto-mining intelligence platform."
hidden: true
---

# Minerstat

<img src="../../.gitbook/assets/connectors/lg/minerstat.png" alt="Minerstat logo">

Minerstat is a crypto-mining intelligence platform. This connector covers the full Minerstat Data API (v3) plus the legacy v2 contract: mineable coins with live network and market data, coin history snapshots, the hardware catalogue (ASICs, GPUs, CPUs and FPGAs) with manufacturer specs, mining algorithms with their coins and benchmarks, the mining-pool directory with fees and payout schemes, and ranked profitability opportunities.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [minerstat.com](https://minerstat.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `minerstat` |

## Use it

Add Minerstat from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.minerstat.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Algorithm</td><td><code>getAlgorithm</code></td><td>Retrieves a single mining algorithm by slug, together with the active coins mined on it and the hardware benchmarked for it.</td></tr><tr><td>Get Coin</td><td><code>getCoin</code></td><td>Retrieves a single coin by slug, returning every field from List Coins plus identity details such as website, block explorer, consensus type and supply figures.</td></tr><tr><td>Get Hardware</td><td><code>getHardware</code></td><td>Retrieves a single mining device by slug, including its identity, release information, rated power draw and the full manufacturer specification sheet.</td></tr><tr><td>Get Pool</td><td><code>getPool</code></td><td>Retrieves a single mining pool by slug, including its identity, founding year and the per-coin fees, payout schemes and minimum payouts it offers.</td></tr><tr><td>Get Profitability Ranking</td><td><code>getProfitabilityRanking</code></td><td>Returns ranked mining opportunities for a given device or hashrate, with daily coins, revenue, electricity cost, net profit and break-even electricity price. Supply either Hardware Slug (preset mode) or Hashrate together with Algorithm (manual mode). This endpoint is available only on the Minerstat Enterprise plan.</td></tr><tr><td>List Algorithms</td><td><code>listAlgorithms</code></td><td>Lists every proof-of-work mining algorithm Minerstat tracks, with its natural hashrate unit and the number of active coins that use it. Row counts are capped by the account's Minerstat plan. Unlike the other list endpoints this one does not support offset paging, so raise Limit to retrieve more algorithms.</td></tr><tr><td>List Coin History</td><td><code>listCoinHistory</code></td><td>Lists historical network snapshots (difficulty and hashrate over time) for a single coin, newest first. Each call is hard-capped at 100 points and further capped by the account's Minerstat plan.</td></tr><tr><td>List Coins</td><td><code>listCoins</code></td><td>Lists all active mineable coins with live network data, market data and freshness metadata. Optionally filter by algorithm slug or restrict the list to high-confidence coins. Row counts are capped by the account's Minerstat plan.</td></tr><tr><td>List Coins (Legacy v2)</td><td><code>listCoinsLegacy</code></td><td>Lists coins using the legacy Minerstat v2 contract: a bare JSON array with stable identifiers and -1 in place of missing values. Optionally filter by ticker list or legacy algorithm name. Retained for existing integrations; new work should use List Coins. The v2 API retires on 31 December 2026.</td></tr><tr><td>List Hardware</td><td><code>listHardware</code></td><td>Lists the mining hardware catalogue with identity, device type, rated power draw and release date. Optionally filter to a single device type. Row counts are capped by the account's Minerstat plan.</td></tr></tbody></table>

<details>

<summary>View 3 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Hardware (Legacy v2)</td><td><code>listHardwareLegacy</code></td><td>Lists mining hardware using the legacy Minerstat v2 contract: a bare JSON array carrying per-algorithm benchmarked speeds. Retained for existing integrations; new work should use List Hardware. The v2 API retires on 31 December 2026.</td></tr><tr><td>List Pools</td><td><code>listPools</code></td><td>Lists the mining-pool directory with default fees, the number of coins each pool serves and the result of the most recent liveness check. Row counts are capped by the account's Minerstat plan.</td></tr><tr><td>List Pools (Legacy v2)</td><td><code>listLegacyPools</code></td><td>Lists mining pools using the legacy Minerstat v2 contract: a bare JSON array with stable sha1 identifiers, an editorial description and a per-ticker map of pool terms. Retained for existing integrations; new work should use List Pools. The v2 API retires on 31 December 2026.</td></tr></tbody></table>

</details>
