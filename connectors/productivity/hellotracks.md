---
description: "Hellotracks field-workforce management: jobs and dispatch, places, zones, members/workers, real-time locate, GPS tracks, forms, reports, API keys and webhooks."
hidden: true
---

# Hellotracks

Hellotracks field-workforce management: jobs and dispatch, places, zones, members/workers, real-time locate, GPS tracks, forms, reports, API keys and webhooks. Wraps both the Hellotracks REST API (/v1) and the legacy JSON-RPC-style /api surface.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [hellotracks.com](https://hellotracks.com) |
| **Authentication** | API key |
| **Actions** | 47 |
| **Events** | 12 |
| **Slug** | `hellotracks` |

## Use it

Add Hellotracks from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.hellotracks.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Job | `archiveJob` | Archives a job by id so it no longer appears in active schedules but stays recoverable. Returns the archived job in data.items. |
| Archive Jobs In Bulk (Legacy API) | `legacyArchiveJobs` | Archives one or many jobs at once by id. Archived jobs leave the active schedule but stay recoverable with Restore Jobs In Bulk. Returns status 0 on success. |
| Auto-assign Jobs | `legacyAutoAssignJobs` | Automatically assign jobs to workers. Docs: https://api-docs.hellotracks.com/api-reference/endpoint/autoassign (POST https://api.hellotracks.com/api/autoassign). |
| Create API Key | `createApiKey` | Mints a new Hellotracks API key for the account. SECURITY WARNING: the response contains data.plainTextKey, the full secret key in clear text, and it is shown only once. Treat the whole response as a secret, never log it, and revoke the key with Delete API Key or Revoke API Key when it is no longer needed. |
| Create Job | `createJob` | Creates a job. If externalId matches an existing job, Hellotracks treats it as a dedupe key and updates that job instead. Assigning a job by assigneeUsername may push a notification to that member's Hellotracks mobile app. |
| Create Jobs In Bulk (Legacy API) | `legacyCreateJobs` | Creates one or many jobs in a single call through the legacy /api surface, with the full internal job field set (destination coordinates, time windows, contact details, custom fields, required skills). Set sendRouteChange to notify affected workers of a route change. Returns status 0 and the created jobs. |
| Create Member | `createMember` | Adds a member (worker, dispatcher or admin) to the Hellotracks organization. WARNING: if password is omitted, Hellotracks sends a real invitation to the new member by email (when the username is an email address) or by SMS (when a phone number is given). |
| Create Member | `legacyCreateMember` | Add a new member. Without a password the member is invited by email/SMS. Docs: https://api-docs.hellotracks.com/api-reference/endpoint/createaccount (POST https://api.hellotracks.com/api/createaccount). |
| Create Place | `createPlace` | Creates a place (a fixed site such as a customer location, warehouse or office) with an address, geofence radius and optional team assignment. Returns the created place including its generated id. |
| Create Place | `legacyCreatePlace` | Create a place (location/site). Docs: https://api-docs.hellotracks.com/api-reference/endpoint/createplace (POST https://api.hellotracks.com/api/createplace). |
| Create Report | `legacyCreateReport` | Generate a report file (returns a download URL). Docs: https://api-docs.hellotracks.com/api-reference/endpoint/createreport (POST https://api.hellotracks.com/api/createreport). |
| Delete API Key | `deleteApiKey` | Permanently deletes an API key by its key id (the public prefix shown by List API Keys). Returns the remaining keys. Never pass the id of the key this connection authenticates with - that would break every action in this connector. |
| Delete Job | `deleteJob` | Permanently deletes a job by id. This cannot be undone - use Archive Job instead when the job should stay recoverable. Returns the deleted job in data.items. |
| Delete Jobs In Bulk (Legacy API) | `legacyDeleteJobs` | Permanently deletes one or many jobs by id. This cannot be undone - prefer Archive Jobs In Bulk to keep the data. Only administrators and company owners may delete jobs. Set notify to false to delete without alerting assigned workers. |
| Delete Member | `deleteMember` | Removes a member from the Hellotracks organization by UID. DANGEROUS: deleting the member that owns the API key, or the organization's only administrator, permanently locks the account out of the API. Never pass the UID returned by Get Authenticated Account. |
| Delete Member | `legacyDeleteMember` | Deactivate (delete) one or more members. Docs: https://api-docs.hellotracks.com/api-reference/endpoint/deleteaccount (POST https://api.hellotracks.com/api/deleteaccount). |
| Distribute Jobs | `legacyDistributeJobs` | Split many jobs into a number of regions/clusters. Docs: https://api-docs.hellotracks.com/api-reference/endpoint/distributejobs (POST https://api.hellotracks.com/api/distributejobs). |
| Edit Jobs In Bulk (Legacy API) | `legacyEditJobs` | Updates one or many existing jobs through the legacy /api surface. jobs is an OBJECT keyed by job id, each value holding only the fields to change - an array is silently ignored and returns status 0 with no change. Use worker (a username) or receiverUid to assign a job, or receiverUid "" to unassign. The notify flag controls whether the assigned worker's device is alerted; leave it false to change jobs silently. |
| Edit Member | `legacyEditMember` | Update properties of a member (identify by account or uid). Docs: https://api-docs.hellotracks.com/api-reference/endpoint/editaccount (POST https://api.hellotracks.com/api/editaccount). |
| Edit Place | `legacyEditPlace` | Update one place (uid) or several (uids) with the same changes. Docs: https://api-docs.hellotracks.com/api-reference/endpoint/editplace (POST https://api.hellotracks.com/api/editplace). |
| Get Authenticated Account | `authWhoami` | Validates the Hellotracks API key and returns the account it belongs to, including the account id, type (company or person), username, display name and email. Use this to test a connection. |
| Get Company | `getCompany` | Returns the Hellotracks company profile and its organization-wide settings, including the worker permission flags, the base address and the team configuration. |
| Get Company | `legacyGetCompany` | Retrieve company settings and team configuration. Docs: https://api-docs.hellotracks.com/api-reference/endpoint/getcompany (POST https://api.hellotracks.com/api/getcompany). |
| Get Job By ID | `getJob` | Retrieves a single job by its Hellotracks job id. Returns data.items with one job object containing title, address, date, progress, assignee, contact and time window. |
| Get Member By ID | `getMember` | Retrieves a single organization member by their Hellotracks member UID. Returns data.items with the matching member, or an empty array when the UID does not exist. |
| Get Members | `legacyGetMembers` | Retrieve members of your organization (all visible members when uids is omitted). Docs: https://api-docs.hellotracks.com/api-reference/endpoint/getaccounts (POST https://api.hellotracks.com/api/getaccounts). |
| Get Place By ID | `getPlace` | Retrieves a single place by its Hellotracks place id. Returns data.items with the place's name, full address, geofence radius, coordinates and team assignment. |
| Get Places | `legacyGetPlaces` | Retrieve places. Docs: https://api-docs.hellotracks.com/api-reference/endpoint/getplaces (POST https://api.hellotracks.com/api/getplaces). |
| Get Tracks | `legacyGetTracks` | Historical GPS tracks and mileage for members. Docs: https://api-docs.hellotracks.com/api-reference/endpoint/gettracks (POST https://api.hellotracks.com/api/gettracks). |
| Get Webhook Configuration | `getWebhookConfiguration` | Returns the callback URL currently registered for each Hellotracks webhook event (job_created, job_updated, job_completed, job_archived, job_deleted, job_checked, place_checked, clock_in_out and alert_triggered), plus whether custom callback headers are set and their names. Secret header values are never returned. |
| List API Keys | `listApiKeys` | Lists the API keys of the Hellotracks account as metadata only: key id (the public prefix), type, active flag, label, source, creator and the created, expiry and last-used timestamps. The secret part of a key is never returned by this endpoint. |
| List Jobs | `listJobs` | Lists jobs in the Hellotracks organization with optional filters for creation time, update time, progress state, external id and assignee. Returns data.items, an array of job objects. Use createdSince or updatedSince (epoch milliseconds) to poll for new or changed jobs. |
| List Members | `listMembers` | Lists or searches members (workers, dispatchers and admins) of the Hellotracks organization. Returns data.items with each member's id, username, email and display name. Use query for an exact or partial match on email, username, name or UID. |
| List Places | `listPlaces` | Lists the places (customer sites, warehouses, offices and other fixed locations) defined for the Hellotracks organization. Returns data.items with each place's id, name, address, radius and geo location. |
| List Timesheets | `listTimesheets` | Returns clock-in and clock-out time entries for the organization together with a summary of total tracked seconds, entry count, open entries and the number of members involved. Restrict the report with the from and until dates. |
| List Zones | `listZones` | Lists the geographic zones (territories) defined for the Hellotracks organization. Zones are used for zone-based auto-assignment of jobs to workers. Returns data.items. |
| Locate Members In Real Time (Legacy API) | `legacyLocate` | Returns the current real-time GPS position, heading, speed, accuracy and device state of members in the organization. This is live location data about real people - handle the response as personal data. |
| Restore Archived Job | `restoreJob` | Restores a previously archived job by id so it returns to the active schedule. Returns the restored job in data.items. |
| Restore Jobs In Bulk (Legacy API) | `legacyRestoreJobs` | Restores one or many previously archived jobs by id so they return to the active schedule. Returns status 0 on success. |
| Revoke API Key | `revokeApiKey` | Revokes an API key by key id so it stops authenticating, while keeping its record in the key list. Never pass the id of the key this connection authenticates with. |
| Route Optimization | `legacyOptimizeRoute` | Optimize the job route of one worker for a day. Docs: https://api-docs.hellotracks.com/api-reference/endpoint/optimizeroute (POST https://api.hellotracks.com/api/optimizeroute). |
| Search Jobs (Legacy API) | `legacyGetJobs` | Searches jobs through the legacy Hellotracks /api surface, which exposes the full internal job record (dispatcher, assignee history, check timestamps, custom fields) that the /v1 job object omits. Filter by id, ids, day, worker, team, order id, progress flags and a sort block. Note: this surface always answers HTTP 200 - check the status field in the body, where 0 means success. |
| Set Webhook Configuration | `setWebhookConfiguration` | Registers or clears the callback URL for one or more Hellotracks webhook events. Send a webhooks object keyed by event name, each with a url and optional custom headers. To UNSUBSCRIBE an event you must send BOTH url "" and headers {} - sending url "" alone leaves the previous URL and headers registered, and url null stores the literal string "null". Returns the full webhook configuration after the change. |
| Update Company Settings | `updateCompany` | Updates the company display name and the organization-wide worker permission flags that control whether workers may create or edit jobs and whether the Hellotracks assistant is enabled. Returns the full updated company object. |
| Update Job | `updateJob` | Updates an existing job. Send the Hellotracks job id in the body together with only the fields to change. Setting assigneeUsername dispatches the job and may push a notification to that member's mobile app. |
| Update Member | `updateMember` | Updates an existing organization member identified by UID in the path. Send only the fields to change. Changing role or password affects the member's access immediately. |
| Update Place | `updatePlace` | Updates an existing place identified by id in the path. Send only the fields to change, such as a new name, address, geofence radius or team assignment. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Alert Triggered | `alerttriggered` | Fires when an alert configuration triggers. Registered under the alert_triggered webhook key. The id field carries the alert instance id. |
| Job Archived | `jobarchived` | Fires when a job is archived. Registered under the job_archived webhook key. |
| Job Checked In | `jobcheckin` | Fires when a worker checks in at a job. Registered under the job_checked webhook key, which also delivers Job Checked Out. |
| Job Checked Out | `jobcheckout` | Fires when a worker checks out of a job. Registered under the job_checked webhook key, which also delivers Job Checked In. |
| Job Completed | `jobcompleted` | Fires when a job is marked completed, either successfully or as failed. Registered under the job_completed webhook key. |
| Job Created | `jobcreated` | Fires when a job is newly created in Hellotracks. Registered under the job_created webhook key. Delivered as a form POST carrying account, id (the job id), data (a JSON string holding the compact job), action and reason. |
| Job Deleted | `jobdeleted` | Fires when a job is deleted. Registered under the job_deleted webhook key. |
| Job Updated | `jobupdated` | Fires when an existing job is updated. Registered under the job_updated webhook key. |
| Place Checked In | `placecheckin` | Fires when a member automatically checks in at a place geofence. Registered under the place_checked webhook key. |
| Place Checked Out | `placecheckout` | Fires when a member automatically checks out of a place geofence. Registered under the place_checked webhook key. |
| Worker Clocked In | `clockin` | Fires when a worker turns tracking on, which Hellotracks treats as a clock-in. Registered under the clock_in_out webhook key. The id field carries the member UID, the timestamp and the action. |
| Worker Clocked Out | `clockout` | Fires when a worker turns tracking off, which Hellotracks treats as a clock-out. Registered under the clock_in_out webhook key. |
