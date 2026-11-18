---
description: "SimpleKPI is a KPI tracking and dashboard platform."
hidden: true
---

# SimpleKPI

<img src="../../.gitbook/assets/connectors/lg/simplekpi.png" alt="SimpleKPI logo">

SimpleKPI is a KPI tracking and dashboard platform. This connector covers the complete SimpleKPI AI REST API (api.simplekpi.com/v1): KPIs and KPI categories with their KPIs, KPI units, the frequency and icon lookups, breakdown items, KPI entries (single upsert, batch upsert, read, update, delete), the aggregated actuals-and-targets report and the read-only users list.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [simplekpi.com](https://simplekpi.com) |
| **Authentication** | Bearer token |
| **Slug** | `simplekpi` |

## Use it

Add SimpleKPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.simplekpi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Or Update KPI Entries In Bulk | `addOrUpdateKpiEntriesInBulk` | Upserts many KPI entries in one request (the endpoint for nightly syncs). Rows are resolved individually: rejected rows are counted in rows_rejected while the rest are written, and the call returns 200 even when every row was rejected, so check the counts. Requires the entries:write scope. |
| Add Or Update KPI Entry | `addOrUpdateKpiEntry` | Upserts a KPI entry identified by kpi_id, source_id and entry_date: 201 means a new entry was created, 200 that an existing one was changed, and a 200 with stored:false means the request was valid but actual, target and notes were all empty. Use the setActual, setTarget and setNotes flags to control which values are written. Requires the entries:write scope. |
| Create Breakdown Item | `createBreakdownItem` | Adds an item to an existing breakdown (breakdowns themselves are created in the app) and returns it as stored. A duplicate name returns 409. Requires the breakdownitems:write scope. |
| Create KPI | `createKpi` | Creates a KPI on the account and returns it as stored, including its new id. Send a real icon_id and unit_id from the KPI Icons and KPI Units lookups, since omitted ids are rejected. Requires the kpis:write scope. |
| Create KPI Category | `createKpiCategory` | Creates a KPI category and returns it as stored. A duplicate name returns 409. Requires the kpis:write scope. |
| Create KPI In Category | `createKpiInCategory` | Creates a KPI inside the category named in the path (the category comes from the URL) and returns it as stored. Send a real icon_id and unit_id from the lookups. Requires the kpis:write scope. |
| Create KPI Unit | `createKpiUnit` | Creates a KPI unit that controls how values are entered and displayed. A duplicate name returns 409. Requires the kpis:write scope. |
| Delete Breakdown Item | `deleteBreakdownItem` | Deletes a breakdown item outright; archive it instead if you still want its history. Returns 204 with no body. Requires the breakdownitems:write scope. |
| Delete KPI | `deleteKpiById` | Deletes a KPI together with every entry recorded against it. This cannot be undone. Returns 204 with no body. Requires the kpis:write scope. |
| Delete KPI Category | `deleteKpiCategory` | Deletes an empty KPI category. Move or delete its KPIs first, otherwise the call returns 400. Returns 204 with no body. Requires the kpis:write scope. |

<details>

<summary>See 28 more actions</summary>

* **Delete KPI Entry** `deleteKpiEntry`: Deletes a KPI entry. Returns 204 with no body. Requires the entries:write scope.
* **Delete KPI In Category** `deleteKpiInCategory`: Deletes a KPI reached through its category, together with its entries. Returns 204 with no body. Requires the kpis:write scope.
* **Delete KPI Unit** `deleteKpiUnit`: Deletes a KPI unit that is no longer assigned to any KPI (reassign those KPIs first). Returns 204 with no body. Requires the kpis:write scope.
* **Get Breakdown Item** `getBreakdownItem`: Returns a single breakdown item by id. Requires the breakdownitems:read scope.
* **Get Data Entries Report** `getDataEntriesReport`: Returns actuals and targets for a set of KPIs over a date range, aggregated to each KPI's own frequency and aggregate function, one row per KPI, breakdown source and period. Requires the entries:read scope.
* **Get KPI** `getKpi`: Returns a single KPI by id. Requires the kpis:read scope.
* **Get KPI Category** `getKpiCategory`: Returns a single KPI category by id. Requires the kpis:read scope.
* **Get KPI Entry** `getKpiEntry`: Returns a single KPI entry by id. Requires the entries:read scope.
* **Get KPI Frequency** `getKpiFrequency`: Returns one data-entry frequency by its case-sensitive code (D, W, M, Q or Y). Requires the kpis:read scope.
* **Get KPI Icon** `getKpiIcon`: Returns one KPI icon by id. Requires the kpis:read scope.
* **Get KPI In Category** `getKpiInCategory`: Returns a KPI reached through its category. Returns 404 if the KPI exists but sits in a different category. Requires the kpis:read scope.
* **Get KPI Unit** `getKpiUnit`: Returns one KPI unit by id. Requires the kpis:read scope.
* **Get User** `getUser`: Returns one user on the account by id (read-only). Requires the users:read scope.
* **List Breakdown Items** `listBreakdownItems`: Lists the breakdown items (the parts a KPI can be broken down by, such as people, teams, products or regions) as a plain array, including combined sets with a null breakdown_id. Requires the breakdownitems:read scope.
* **List KPI Categories** `listKpiCategories`: Lists the KPI categories on the account as a plain array. Requires the kpis:read scope.
* **List KPI Entries** `listKpiEntries`: Lists KPI entries (actual and target values recorded against KPIs by date) as a plain array, filtered by user, KPI, breakdown source and date range. Requires the entries:read scope.
* **List KPI Frequencies** `listKpiFrequencies`: Returns the read-only lookup of data-entry frequencies (the codes accepted as frequency_id on a KPI) as a plain array. Requires the kpis:read scope.
* **List KPI Icons** `listKpiIcons`: Returns the read-only lookup of icons a KPI can be given (the ids accepted as icon_id) as a plain array. Icons are shared across all accounts. Requires the kpis:read scope.
* **List KPI Units** `listKpiUnits`: Lists the account's KPI units (how values are typed in and displayed: currency, percentage, plain number) as a plain array. Requires the kpis:read scope.
* **List KPIs** `listKpis`: Lists the KPIs on the account as a plain array. Page through with page and rows until a short page is returned. Requires the kpis:read scope.
* **List KPIs In Category** `listKpisInCategory`: Lists the KPIs inside one KPI category as a plain array. Requires the kpis:read scope.
* **List Users** `listUsers`: Lists the people on the account as a plain array (read-only; users are managed in the app). Use a user's id or email to attribute KPI entries. Requires the users:read scope.
* **Update Breakdown Item** `updateBreakdownItem`: Replaces a breakdown item (full replacement, not a patch). is_system is ignored on update. A duplicate name returns 409. Requires the breakdownitems:write scope.
* **Update KPI** `updateKpi`: Replaces a KPI. This is a full replacement, not a patch: any field left out is reset to its default, so read the KPI first and send it back changed. Requires the kpis:write scope.
* **Update KPI Category** `updateKpiCategory`: Replaces a KPI category (full replacement, not a patch). A duplicate name returns 409. Requires the kpis:write scope.
* **Update KPI Entry** `updateKpiEntry`: Changes the KPI entry named in the path. Use the setActual, setTarget and setNotes flags to choose which values are written. Requires the entries:write scope.
* **Update KPI In Category** `updateKpiInCategory`: Replaces a KPI reached through its category (full replacement, not a patch: omitted fields reset to defaults). Requires the kpis:write scope.
* **Update KPI Unit** `updateKpiUnit`: Replaces a KPI unit (full replacement, not a patch). A duplicate name returns 409. Requires the kpis:write scope.

</details>
