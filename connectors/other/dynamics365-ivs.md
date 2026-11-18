---
description: "Microsoft Dynamics 365 Supply Chain Management - Inventory Visibility Service (IVS)."
hidden: true
---

# Dynamics 365 Inventory Visibility

<img src="../../.gitbook/assets/connectors/lg/dynamics365-ivs.png" alt="Dynamics 365 Inventory Visibility logo">

Microsoft Dynamics 365 Supply Chain Management - Inventory Visibility Service (IVS). Cache-backed, F&O-decoupled near-real-time inventory API for high-frequency on-hand queries (avoids F&O OData 429 throttling). Two-step auth: Azure AD client_credentials token (scope 0cdb527f-a8d1-4bf8-9436-b352c68682b2/.default) is exchanged at https://securityservice.operations365.dynamics.com/token for an IVS bearer token (1h TTL); that token calls the region-specific data plane host https://inventoryservice.{RegionShortName}-il{Island}.gateway.prod.island.powerapps.com. Covers on-hand query (indexquery/exactquery/productsearch/GET), on-hand change events + set/override, soft reservations + allocation, change schedules + ATP, external-change adjustment sync, and reservation cleanup/job-progress.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [powerapps.com](https://powerapps.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `dynamics365Ivs` |

## Use it

Add Dynamics 365 Inventory Visibility from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dynamics365Ivs.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Allocate | `allocationAllocate` | Create one allocate event - reserve on-hand stock into an allocation pool/group. Supply the full allocation body as `body`. Requires the inventory allocation feature. |
| Clean Up Reservation Data (Resync Job) | `reservationResyncJob` | Create a job to clean up historical reservation data. Body `dataSources` is an array of data source names (e.g. ["iv","pos"]); an empty array cleans all. Returns a job id usable with getJobProgress. |
| Consume Allocation | `allocationConsume` | Create one consume event - consume (draw down) stock from an allocation pool when an order ships. Supply the full body as `body`. |
| Create On-Hand Change Event | `createOnhandChange` | Post a single on-hand change (delta) event from an external system. Body: id (idempotency key), organizationId, productId, dimensions, quantities{dataSource:{measure:number}}, optional dimensionDataSource. Increments/decrements cached quantities. |
| Create On-Hand Change Events (Bulk) | `createOnhandChangeBulk` | Post up to 512 on-hand change (delta) events in one call. Body `events` is an array of change-event objects (same shape as createOnhandChange). |
| Create On-Hand Change Schedule | `createChangeSchedule` | Post one future-dated on-hand change schedule (drives ATP). Body: id, organizationId, productId, dimensions, quantitiesByDate{date:{dataSource:{measure:number}}}, optional dimensionDataSource. Date format year-month-day, within the configured schedule period. Requires the ATP / on-hand change schedule feature. |
| Create On-Hand Change Schedules (Bulk) | `createChangeScheduleBulk` | Post up to 512 future-dated on-hand change schedules. Body `schedules` is an array of change-schedule objects (same shape as createChangeSchedule). |
| Create Soft Reservation | `createReservation` | Create one soft reservation event. Body: id, organizationId, productId, dimensionDataSource, dimensions, quantity, modifier, ifCheckAvailForReserv (default true), optional quantityDataSource/quantities. Returns reservationId used to unreserve. Requires the soft reservation feature enabled. |
| Create Soft Reservations (Bulk) | `createReservationBulk` | Create multiple soft reservation events (max 512). Body `reservations` is an array of reservation objects (same shape as createReservation). |
| Get Azure AD Token (Step 1) | `getAadToken` | Step 1 of IVS auth. Fetches a Microsoft Entra (Azure AD) token via client_credentials for the IVS resource app. The returned access_token is the client_assertion for getIvsToken (Step 2). Scope is fixed to the IVS AAD app id 0cdb527f-a8d1-4bf8-9436-b352c68682b2/.default. |
| Get IVS Token (Step 2) | `getIvsToken` | Step 2 of IVS auth. Exchanges the Azure AD token (from getAadToken) at the security service for the IVS bearer access_token used on all data-plane calls. Pass aadToken = the access_token from Step 1. Context is the SCM environmentId from the connection. Token TTL ~3600s. Handles 307 redirect automatically. |
| Get Job Progress | `getJobProgress` | Get the execution progress of an IVS job (e.g. reservation resync). Pass jobId (e.g. SomeJob:xxxxxxxx-...). |
| Query Allocation | `allocationQuery` | Query allocation results - remaining/consumed quantities per allocation pool. Supply the full query body as `query`. |
| Query On-Hand (Exact Query) | `queryOnhandExact` | On-hand exact query: query precise site/location (dimension tuples) combinations to avoid the cartesian expansion of the index query. Supply full body as `query` (filters{organizationId,productId,dimensions[],values[][]}, groupByValues, returnNegative). Api-Version 1.0 or 2.0 (2.0 uses filters.keys instead of organizationId+dimensions). |
| Query On-Hand (GET) | `queryOnhandGet` | On-hand query via GET. Single-org only. Pass filter values as query params (organizationId, productId, siteId, locationId, dimension keys), plus groupBy (comma list), returnNegative, and optional ATP params (QueryATP, ATPFromDate, ATPToDate). Convenience for simple lookups; prefer queryOnhandIndex for production. |
| Query On-Hand (Index Query) | `queryOnhandIndex` | Recommended on-hand query. POST index query returning current cached on-hand quantities per data source (fno/iv/pos/@iv). Supply the full query document as `query` (filters{organizationId,productId,siteId,locationId,...}, groupByValues, returnNegative; optional QueryATP/ATPFromDate/ATPToDate, dimensionDataSource). Api-Version 1.0 = one org; pass apiVersion 2.0 + pageNumber/pageSize for multi-org paging. |
| Query On-Hand With Product Search (Exact) | `queryOnhandProductSearchExact` | Exact query enhanced with product search. Supply full body as `query` (productSearch, filters{organizationId,dimensions,values}, groupByValues, returnNegative). Requires SCM 10.0.36+ and the IVS search service. |
| Query On-Hand With Product Search (Index) | `queryOnhandProductSearchIndex` | Index query enhanced with product search. Filter/find products by ProductAttributeQuery (productFilter/attributeFilter) in addition to dimension filters. Requires SCM 10.0.36+ and the IVS search service. Supply full body as `query` (productSearch, filters, groupByValues, returnNegative). |
| Reallocate | `allocationReallocate` | Create one reallocate event - move allocated stock between allocation pools. Supply the full body as `body`. |
| Reverse Soft Reservation (Unreserve) | `unreserve` | Reverse one soft reservation by reservationId. Body: id, organizationId, productId, reservationId, dimensions, OffsetQty (units to free). Partial or full reversal depending on OffsetQty. |
| Reverse Soft Reservations (Unreserve Bulk) | `unreserveBulk` | Reverse multiple soft reservations (max 512). Body `unreserves` is an array of unreserve objects (same shape as unreserve). |
| Set / Override On-Hand Quantities (Bulk) | `setOnhandBulk` | Override (absolute set, not delta) cached on-hand quantities for the specified inventory system data source. Path requires inventorySystem (the data source name, e.g. pos). Body `records` is an array of { id, organizationId, productId, dimensions, quantities, modifiedDateTimeUTC, dimensionDataSource? }. Used for stock counts. |
| Sync External Inventory Changes (Adjustment Bulk) | `transactionAdjustmentBulk` | Sync external inventory changes through Inventory Visibility via the transaction adjustment bulk endpoint. Body `adjustments` is an array of adjustment records. Used to reconcile/sync changes that originated outside IVS. |
| Unallocate | `allocationUnallocate` | Create one unallocate event - release stock from an allocation pool. Supply the full body as `body`. |
