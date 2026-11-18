---
description: "Detrack delivery management and real-time vehicle tracking (API v2)."
hidden: true
---

# Detrack

<img src="../../.gitbook/assets/connectors/detrack.png" alt="Detrack logo" width="64">

Detrack delivery management and real-time vehicle tracking (API v2). Create, update and track delivery and collection jobs, manage vehicles/drivers, driver groups, sub-accounts, geofences, depots, routes, rate cards, invoices, exports, and account-wide job/notification/webhook settings.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [detrack.com](https://detrack.com) |
| **Authentication** | API key |
| **Slug** | `detrack` |

## Use it

Add Detrack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.detrack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Create Jobs | `bulkCreateJobs` | Create many Detrack jobs in one request. Pass an array of job objects in `data`; each takes the same fields as Create Job. Returns the array of created job records. |
| Create Contractor Group | `createContractorGroup` | Create a contractor group in Detrack, used to transfer jobs to a third-party carrier's fleet. Only `name` is required. |
| Create Geofence | `createGeofence` | Create a geofence in Detrack from a polygon of latitude/longitude points. `name` is required (Detrack answers 422 "Name cannot be blank" otherwise). Note this endpoint uses the `data` envelope while Update Geofence does not. |
| Create Group | `createGroup` | Create a driver/vehicle group in Detrack. Only `name` is required; the branding and custom-settings flags are optional per-group overrides. |
| Create Invoice | `createInvoice` | Create an invoice in Detrack. `org_group` must reference an existing organisation group - Detrack returns 422 org_group "cannot be blank" when it cannot resolve one, and an account with no organisation groups can never satisfy it (Detrack exposes no API to create organisation groups). |
| Create Job | `createJob` | Create a single Detrack delivery or collection job. `do_number` (the Delivery/Collection Order number) and `date` are the minimum; `address` is needed for routing. Leave `assign_to` empty unless you intend to dispatch the job to a real driver. Returns the created job record. |
| Create Job By ID API | `createJobIdApi` | Create a Detrack job through the /jobs id-keyed endpoint family. Equivalent to Create Job but the response is addressed by internal job id. Leave `assign_to` empty unless you intend to dispatch to a real driver. |
| Create Or Update Depot | `createDepot` | Create a Detrack depot (warehouse / dispatch origin), or update an existing one. This endpoint UPSERTS BY NAME: posting a name that already exists returns that depot's existing id with the supplied fields applied, rather than creating a duplicate. WARNING: Detrack exposes no PUT and no DELETE on depots (both return 405), so a depot created here can only be removed from the Detrack web app under Settings. Only `name` is required; supply an address to have it geocoded. |
| Create Rate Card | `createRateCard` | Create a Detrack rate card (job pricing rule). Detrack requires name, service_type, item_type, fee_structure and calculation_type; the accepted values for service_type and calculation_type are defined by the rate card add-on, which is not enabled on accounts without the entitlement. |
| Create Rate Card Chargeable | `createRateCardChargeable` | Apply a rate card to a selection of jobs, producing rate card chargeables. Detrack answers 400 bad_request "No jobs selected" when the job selection does not resolve, which is what an account without the rate card add-on receives. |

<details>

<summary>See 70 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Sub Account | `createSubAccount` | Create a sub-account user in the Detrack organisation. Detrack only accepts the role "manager" on this endpoint (any other value returns 422 role "is not included in the list"). Creating a sub-account invites the email address, so use a mailbox you control. The call is idempotent by email. |
| Create Vehicle | `createVehicle` | Create a vehicle (driver) in Detrack. `detrack_id` must be a Detrack ID that already exists for the account - Detrack answers 422 detrack_id "not found" for an unknown one, and 422 "cannot be blank" if it is omitted. |
| Create Vehicle Checklist | `createVehicleChecklist` | Create a vehicle checklist in Detrack - the inspection form drivers complete at the start or end of a shift. Only `name` is required. Checklist items and the email notification mode are part of the paid vehicle_checklist add-on and are silently ignored by this endpoint on accounts without it (profile addons.vehicle_checklist.has_addon = false), so they are deliberately not offered here. |
| Delete Contractor Group | `deleteContractorGroup` | Permanently delete a Detrack contractor group by its id. Returns 204 No Content on success. |
| Delete Geofence | `deleteGeofence` | Permanently delete a Detrack geofence by id. Returns 204 No Content on success. |
| Delete Group | `deleteGroup` | Permanently delete a Detrack driver/vehicle group by its group id. Returns 204 No Content on success. |
| Delete Invoice | `deleteInvoice` | Permanently delete a Detrack invoice by id. Returns 204 No Content on success. |
| Delete Job | `deleteJob` | Permanently delete a Detrack job by its D.O. number. Returns 204 No Content on success and 404 with code not_found if no job carries that D.O. number. |
| Delete Job By Internal ID | `deleteJobById` | Permanently delete a Detrack job addressed by its internal job id. Returns 204 No Content on success. |
| Delete Rate Card | `deleteRateCard` | Permanently delete a Detrack rate card by id. Requires the rate card add-on. |
| Delete Rate Card Chargeable | `deleteRateCardChargeable` | Permanently delete a Detrack rate card chargeable by id. Note Detrack exposes no PUT on this resource (a PUT returns 405). |
| Delete Sub Account | `deleteSubAccount` | Permanently remove a sub-account user from the Detrack organisation by id. Returns 204 No Content on success. |
| Delete Vehicle | `deleteVehicle` | Permanently delete a Detrack vehicle (driver) by its vehicle id. Returns 204 No Content on success and 404 not_found if no vehicle carries that id. |
| Delete Vehicle Checklist | `deleteVehicleChecklist` | Permanently delete a Detrack vehicle checklist by id. Returns 204 No Content on success. |
| Get Collection Settings | `getCollectionSettings` | Retrieve the Detrack collection settings - the proof-of-collection requirements, geofence radius, failure and item reject reason lists and the collection notification endpoint. The collection counterpart of Get Delivery Settings. |
| Get Contractor Group | `getContractorGroup` | Retrieve one Detrack contractor group by its id. Returns 404 not_found "Could not find the contractor group with this id" for an unknown id. |
| Get Delivery Settings | `getDeliverySettings` | Retrieve the Detrack delivery settings - what proof of delivery drivers must capture (photo, signature, recipient name, verification code), the geofence radius for a valid POD, the failure reason lists and the delivery notification endpoint. |
| Get Depot | `getDepot` | Retrieve one Detrack depot. This endpoint is keyed by depot NAME, not by id - passing an id returns 404 not_found "Depot not found". |
| Get Export | `getExport` | Retrieve one Detrack export job by id to check its status and obtain its download URL. Returns 404 not_found "Could not find export with this id" for an unknown id. |
| Get Geofence | `getGeofence` | Retrieve one Detrack geofence by id, with its polygon points and assigned drivers. Detrack returns 500 rather than 404 when the id does not exist. |
| Get Group | `getGroup` | Retrieve one Detrack driver/vehicle group by its group id, including its counts and branding overrides. |
| Get Invoice | `getInvoice` | Retrieve one Detrack invoice by id. Detrack serves invoices through its group controller, so an unknown id returns 404 not_found "Could not find group with this id". |
| Get Job | `getJob` | Retrieve one Detrack job by its Delivery/Collection Order number (D.O. number), optionally narrowed by job date and type. Returns the full job record including proof-of-delivery fields, photos, signature URLs, items and milestones. |
| Get Job By Internal ID | `getJobById` | Retrieve one Detrack job by its internal job id (the `id` field, not the D.O. number) via the /jobs id-keyed endpoint family. Returns the full job record. |
| Get Job Settings | `getJobSettings` | Retrieve the Detrack account-wide job settings - which job and item fields are enabled, the job form and table layouts, custom column headers, reason lists, retention period, date formats and POD behaviour. Around 148 settings keys. |
| Get Notification Settings | `getNotificationSettings` | Retrieve the Detrack notification settings - the sender identity used for customer emails and the SMS / WhatsApp provider credentials used for delivery notifications. |
| Get Organisation | `getOrganisation` | Retrieve one Detrack organisation by id, with its address, units of measurement, time zone and credit balance. Detrack has no POST or DELETE on this resource (both return 405). |
| Get Profile | `getProfile` | Retrieve the Detrack user profile that owns the API key, including name, email, role, country, trial end date and the organisations/organizations the user belongs to. Use it to verify the connection and discover the current organisation id. |
| Get Rate Card | `getRateCard` | Retrieve one Detrack rate card by id. Returns 404 not_found "Could not find rate card with this id" when no rate card carries that id. |
| Get Rate Card Chargeable | `getRateCardChargeable` | Retrieve one Detrack rate card chargeable by id. Returns 404 not_found "Could not find rate card with this id" for an unknown id. |
| Get Sub Account | `getSubAccount` | Retrieve one Detrack sub-account user by id, including its role, permissions, group memberships and per-user webhook configuration. |
| Get Vehicle | `getVehicle` | Retrieve one Detrack vehicle (driver) by its vehicle id, including its live position, connection status, shift window and capacity limits. |
| Get Vehicle Checklist | `getVehicleChecklist` | Retrieve one Detrack vehicle checklist by id, with its items, assigned vehicles and notification settings. |
| Get Vehicle Settings | `getVehicleSettings` | Retrieve the Detrack account-wide vehicle settings - the GPS ping interval, the route time factor used for ETA calculation and the vehicle display options on the dashboard. |
| Get Webhook Settings | `getWebhookSettings` | Retrieve the Detrack account-wide webhook configuration - the endpoint Detrack posts job events to, which job statuses fire it, the payload content type and the authentication Detrack uses when calling it. Use this to confirm a webhook subscription is registered. |
| List Contractor Groups | `listContractorGroups` | List the contractor groups in the Detrack account - the third-party carrier groups jobs can be transferred to - with their user and vehicle counts. |
| List Depots | `listDepots` | List the Detrack depots (warehouses / dispatch origins), with their geocoded address and coordinates. Detrack offers no server-side name or id filter on this endpoint (both are silently ignored and every depot is returned), so page through the results and filter client-side, or use Get Depot with the depot's name. |
| List Exports | `listExports` | List the export jobs generated from the Detrack dashboard, with their status and download URL. Exports are created from the Detrack web app, not through the API (POST/PUT/DELETE all return 405). |
| List Geofences | `listGeofences` | List the geofences defined in the Detrack account, with their polygon points and the drivers assigned to each. |
| List Groups | `listGroups` | List the driver/vehicle groups in the Detrack account, with their user, vehicle and job counts and per-group branding settings. |
| List Invoices | `listInvoices` | List the invoices Detrack holds for the account's organisation groups. Invoices belong to an organisation group, so an account with no organisation groups returns an empty list. |
| List Jobs | `listJobs` | List Detrack delivery and collection jobs, optionally filtered by date, job type, status, D.O. number, assigned vehicle or driver name. Returns a page of full job records (200+ fields each) with cursor links. Use `limit` to keep responses small. |
| List Jobs By ID API | `listJobsIdApi` | List Detrack jobs through the /jobs id-keyed endpoint family, the counterpart of List Jobs whose records are addressed by internal job id. Supports the same date, type, status and pagination filters. |
| List Organisations | `listOrganisations` | List the Detrack organisations the API key can see, with their address, units of measurement, time zone, credits and non-working days. Detrack also serves this at the US spelling /organizations - both return the same records. |
| List Rate Card Chargeables | `listRateCardChargeables` | List the rate card chargeables - the priced job charges produced by applying rate cards to jobs. |
| List Rate Cards | `listRateCards` | List the rate cards (job pricing rules) in the Detrack account. Rate cards are a paid add-on: an account without the entitlement receives 403 {"code":"forbidden"}, which matches an empty rate_cards permission list on the profile. |
| List Routes | `listRoutes` | List the Detrack planned routes for a given date. `date` is required - without it Detrack returns 422 invalid_date "date parameter is required". Set `tbc` to list routes that are still to be confirmed. |
| List Sub Accounts | `listSubAccounts` | List the sub-account users of the Detrack organisation, with their role, group memberships, permissions and per-user webhook configuration. |
| List Vehicle Checklists | `listVehicleChecklists` | List the vehicle checklists (driver pre-trip/post-trip inspection forms) configured in the Detrack account, with their items, assigned vehicles and notification settings. |
| List Vehicles | `listVehicles` | List the vehicles (drivers) in the Detrack account, with their live GPS position, speed, battery, connection status and capacity limits. Filter by name or page through the results. |
| Reattempt Job | `reattemptJob` | Schedule a reattempt of a failed Detrack job. The job must already be in the failed status, otherwise Detrack returns 422 invalid_reattempt "Job must be failed for reattempt". Send `data` as a single object (an array triggers a Detrack 500). |
| Reattempt Job By ID API | `reattemptJobIdApi` | Schedule a reattempt of a failed Detrack job through the /jobs id-keyed endpoint family. Both `id` and `date` are required - Detrack answers 422 invalid_data "Data is missing" if either is absent, and this endpoint does NOT accept a do_number. Only a job already in the failed status is found; anything else returns 404 not_found. |
| Update Collection Settings | `updateCollectionSettings` | Update the Detrack collection settings - the proof-of-collection requirements, geofence radius and the collection failure and item reject reason lists. Only the keys supplied inside `data` change. |
| Update Contractor Group | `updateContractorGroup` | Update a Detrack contractor group by its id - rename it or archive it. Only the fields supplied inside `data` change. |
| Update Delivery Settings | `updateDeliverySettings` | Update the Detrack delivery settings - tighten or relax the proof-of-delivery requirements, change the POD geofence radius, or edit the delivery failure and item reject reason lists. Only the keys supplied inside `data` change. |
| Update Geofence | `updateGeofence` | Update a Detrack geofence by id - rename it or replace its polygon. Unlike the other Detrack write endpoints this one takes the fields at the top level, NOT inside a `data` envelope (sending `data` makes Detrack return 500). |
| Update Group | `updateGroup` | Update a Detrack driver/vehicle group by its group id. Only the fields supplied inside `data` change - rename it, archive it, or adjust its branding overrides. |
| Update Invoice | `updateInvoice` | Update a Detrack invoice by id. Only the fields supplied inside `data` change. |
| Update Job | `updateJob` | Update an existing Detrack job, addressed by its D.O. number. Only the fields supplied inside `data` are changed. Setting `assign_to` dispatches the job to that vehicle's driver. |
| Update Job By Internal ID | `updateJobById` | Update a Detrack job addressed by its internal job id. Only the fields supplied inside `data` change. Setting `assign_to` dispatches the job to that vehicle's driver. |
| Update Job Settings | `updateJobSettings` | Update the Detrack account-wide job settings. Only the keys supplied inside `data` change - use it to switch collections on, change the date format, adjust the retention period, or reorder the job form and table columns. |
| Update Notification Settings | `updateNotificationSettings` | Update the Detrack notification settings - the email sender identity and the SMS / WhatsApp provider credentials. Only the keys supplied inside `data` change. Changing the SMS provider affects messages sent to real recipients. |
| Update Organisation | `updateOrganisation` | Update a Detrack organisation by id - change its address, phone number, units of measurement, time zone, default currency or non-working days. Only the fields supplied inside `data` change. |
| Update Profile | `updateProfile` | Update the Detrack user profile that owns the API key - name, mobile number, dial code, locale and country. Only the fields supplied inside `data` change. Note the time zone, default landing page, date format and units of measurement are NOT settable here (Detrack accepts them with a 200 but silently ignores them) - use Update Organisation or Update Job Settings for those. |
| Update Rate Card | `updateRateCard` | Update a Detrack rate card by id. Only the fields supplied inside `data` change. Requires the rate card add-on. |
| Update Sub Account | `updateSubAccount` | Update a Detrack sub-account user by id - change the name, group memberships, permissions or the per-user webhook endpoint. Only the fields supplied inside `data` change. |
| Update Vehicle | `updateVehicle` | Update a Detrack vehicle (driver) by its vehicle id. Only the fields supplied inside `data` change - useful for adjusting capacity, shift hours, speed limits or disabling a vehicle. |
| Update Vehicle Checklist | `updateVehicleChecklist` | Update a Detrack vehicle checklist by id - rename it, reassign vehicles or change when it is mandatory. Only the fields supplied inside `data` change. Checklist items and the email notification mode belong to the paid vehicle_checklist add-on and are silently ignored on accounts without it, so they are deliberately not offered here. |
| Update Vehicle Settings | `updateVehicleSettings` | Update the Detrack account-wide vehicle settings - the GPS ping interval, the ETA route time factor and the dashboard display options. Only the keys supplied inside `data` change. |
| Update Webhook Settings | `updateWebhookSettings` | Register, change or clear the Detrack account-wide webhook. Set `webhook_url` plus `webhook_triggers` to subscribe to job status events; send webhook_url null to unsubscribe. This is the endpoint a fastn event subscription uses to register and deregister itself. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Driver Heading To Job | `heading_to` | Fires when the driver marks that they are heading to the job. Shares the single account-wide Detrack webhook URL; routed by the job's `status` field. payloadSchema is MODELLED from the Detrack job record, not captured live. |
| Job Completed | `completed` | Fires when a job is completed, carrying the electronic proof of delivery - signature URL, photo URLs, POD timestamp and POD coordinates. Shares the single account-wide Detrack webhook URL; routed by the job's `status` field. payloadSchema is MODELLED from the Detrack job record, not captured live. |
| Job Deleted | `deleted` | Fires when a job is deleted from Detrack. Shares the single account-wide Detrack webhook URL; routed by the job's `status` field. payloadSchema is MODELLED from the Detrack job record, not captured live. |
| Job Failed | `failed` | Fires when a job fails, carrying the failure reason the driver selected. Shares the single account-wide Detrack webhook URL; routed by the job's `status` field. payloadSchema is MODELLED from the Detrack job record, not captured live. |
| Job In Progress | `dispatched` | Fires when a job moves to In Progress (dispatched). Shares the single account-wide Detrack webhook URL; routed by the job's `status` field. payloadSchema is MODELLED from the Detrack job record, not captured live. |
| Job Info Received | `info_recv` | Fires when a job enters the Info Received status - Detrack has the job details but it is not yet in progress. Detrack holds ONE account-wide webhook URL (Settings &gt; Integrations &gt; Webhook, or the Update Webhook Settings action), so every trigger on this connector shares that endpoint and is routed by the job's `status` field. payloadSchema is MODELLED from the Detrack job record returned by GET /api/v2/dn/jobs, not captured from a live delivery. |
| Job On Hold | `on_hold` | Fires when a job is put on hold. Shares the single account-wide Detrack webhook URL; routed by the job's `status` field. payloadSchema is MODELLED from the Detrack job record, not captured live. |
| Job Partially Completed | `completed_partial` | Fires when a job is partially completed - some items delivered or collected, some rejected. Shares the single account-wide Detrack webhook URL; routed by the job's `status` field. payloadSchema is MODELLED from the Detrack job record, not captured live. |
| Job Returned | `return` | Fires when a job is marked as a return. Shares the single account-wide Detrack webhook URL; routed by the job's `status` field. payloadSchema is MODELLED from the Detrack job record, not captured live. |
| Job Scheduled | `scheduled` | Fires when a job is scheduled. Shares the single account-wide Detrack webhook URL; routed by the job's `status` field. payloadSchema is MODELLED from the Detrack job record, not captured live. |
