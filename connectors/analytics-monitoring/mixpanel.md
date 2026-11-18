---
description: "Mixpanel product analytics — Query API (segmentation, funnels, retention, insights, activity stream, profiles), Lexicon schemas, annotations, cohorts, service…"
hidden: true
---

# Mixpanel

Mixpanel product analytics — Query API (segmentation, funnels, retention, insights, activity stream, profiles), Lexicon schemas, annotations, cohorts, service accounts, data pipelines, GDPR data deletion, and event/profile/group ingestion.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [mixpanel.com](https://mixpanel.com) |
| **Authentication** | Basic auth |
| **Actions** | 50 |
| **Events** | 0 |
| **Slug** | `mixpanel` |

## Use it

Add Mixpanel from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mixpanel.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activity Stream Query | `activityStream` | Return the chronological event activity stream for one or more users over a date range (Query API). |
| Append to List Property | `appendToListProperty` | Append values to list properties on a Mixpanel user profile ($append). Each value is added to the end of the list. |
| Average Segmentation Query | `segmentationAverage` | Average a numeric expression of an event over time, optionally segmented (Query API, maintenance mode). |
| Batch Update Groups | `batchUpdateGroups` | Update up to 200 Mixpanel group profiles in one request. Provide the raw JSON array of group update objects (each with $token, $group_key, $group_id and an operator such as $set). |
| Batch Update Profiles | `batchUpdateProfiles` | Update up to 2000 Mixpanel user profiles in one request. Provide the raw JSON array of profile update objects (each with $token, $distinct_id and an operator such as $set). |
| Cancel Data Deletion Task | `cancelDataDeletion` | Cancel a pending GDPR/CCPA data-deletion task by task ID. Requires OAuth/Service Account authorization. |
| Create Annotation | `createAnnotation` | Create a dated annotation in the project. Requires a Service Account credential. |
| Create Data Deletion Task | `createDataDeletion` | Create a GDPR/CCPA data-deletion task for the given distinct IDs. Requires OAuth/Service Account authorization. |
| Create Identity | `createIdentity` | Associate an anonymous ID with an identified user ID by sending a $identify event to the ingestion API (Original ID Merge). $anon_id must be a UUID v4 not already merged. |
| Create Service Account | `createServiceAccount` | Create a new service account in an organization with a role and optional expiry. Requires an owner/admin Service Account credential. |
| Delete Annotation | `deleteAnnotation` | Delete an annotation by ID. Requires a Service Account credential. |
| Delete Group | `deleteGroup` | Permanently delete a Mixpanel group profile ($delete), identified by group_key and group_id. |
| Delete Profile | `deleteProfile` | Permanently delete a Mixpanel user profile ($delete). This removes the profile but not the user's past events. |
| Delete Schema | `deleteSchema` | Delete a Lexicon schema by entity type and name. Requires a Service Account credential. |
| Delete Service Account | `deleteServiceAccount` | Delete a service account by ID within an organization. Requires an owner/admin Service Account credential. |
| Frequency Query | `retentionFrequency` | Query how often users perform an event within a time unit (addiction/frequency report, Query API). |
| Funnels Query | `funnelsQuery` | Query conversion data for a saved funnel over a date range (Query API, maintenance mode). |
| Get Annotation | `getAnnotation` | Get a single annotation by ID. Requires a Service Account credential. |
| Get Data Deletion Task | `getDataDeletion` | Get the status of a GDPR/CCPA data-deletion task by task ID. Requires OAuth/Service Account authorization. |
| Get Pipeline Status | `getPipelineStatus` | Get the status of a data pipeline (warehouse export) by name, including succeeded/retried/canceled jobs. |
| Get Schema | `getSchema` | Get a single Lexicon schema by entity type and name. Requires a Service Account credential. |
| Get Service Account | `getServiceAccount` | Get a service account by ID within an organization. Requires an owner/admin Service Account credential. |
| Import Event | `importEvent` | Import a historical event into Mixpanel via the /import endpoint (authenticated, supports events older than 5 days). Requires $insert_id for deduplication. |
| Increment Profile Property | `incrementProfileProperty` | Increment numeric properties on a Mixpanel user profile ($add). Each value is added to the current value. |
| Insights Query | `insights` | Fetch the computed data for a saved Insights report by its bookmark ID (Query API). |
| List Annotations | `listAnnotations` | List all annotations in the project. Requires a Service Account credential. |
| List Cohorts | `listCohorts` | List all saved cohorts in the project with their id, name, and member count (Query API). |
| List Saved Funnels | `listSavedFunnels` | List the saved funnels (funnel_id and name) defined in the Mixpanel project. |
| List Schemas | `listSchemas` | List all Lexicon data-dictionary schemas defined in the project. Requires a Service Account credential. |
| List Schemas For Entity | `listSchemasForEntity` | List Lexicon schemas for a specific entity type (event, user, group, or lookup). Requires a Service Account credential. |
| List Service Accounts | `listServiceAccounts` | List all service accounts in an organization. Requires an owner/admin Service Account credential. |
| Numeric Segmentation Query | `segmentationNumeric` | Bucket a numeric property of an event into ranges over time (Query API, maintenance mode). |
| Query Profiles | `queryProfiles` | Query stored user profiles by filter expression or distinct IDs, with pagination (Query API /engage). |
| Remove from Group List Property | `removeFromGroupListProperty` | Remove values from list properties on a Mixpanel group profile ($remove). |
| Remove from List Property | `removeFromListProperty` | Remove values from list properties on a Mixpanel user profile ($remove). Each value is removed from the property's list. |
| Retention Query | `retention` | Query cohort retention: how many users returned to perform an event after a born event (Query API). |
| Segmentation Query | `segmentation` | Query event counts over time, optionally segmented by a property and filtered by an expression (Query API, maintenance mode). |
| Set Group Properties | `setGroupProperties` | Set properties on a Mixpanel group profile ($set). The group is identified by group_key and group_id. |
| Set Group Properties Once | `setGroupPropertiesOnce` | Set properties on a Mixpanel group profile only if not already set ($set_once). |
| Set Profile Properties | `setProfileProperties` | Set properties on a Mixpanel user profile ($set). Overwrites existing values for the given properties. |
| Set Profile Properties Once | `setProfilePropertiesOnce` | Set properties on a Mixpanel user profile only if they are not already set ($set_once). Existing values are preserved. |
| Sum Segmentation Query | `segmentationSum` | Sum a numeric expression of an event over time, optionally segmented (Query API, maintenance mode). |
| Top Events | `topEvents` | Return today's top events by volume with percent change (Query API). |
| Track Event | `trackEvent` | Send a single event to Mixpanel via the ingestion API. The project token identifies the project; distinct_id identifies the user. |
| Union to Group List Property | `unionGroupListProperty` | Merge lists of values into list properties on a Mixpanel group profile ($union). Duplicates are ignored. |
| Union to List Property | `unionProfileListProperty` | Merge lists of values into list properties on a Mixpanel user profile ($union). Duplicate values are ignored. |
| Unset Group Properties | `unsetGroupProperties` | Remove the named properties from a Mixpanel group profile ($unset). |
| Unset Profile Properties | `unsetProfileProperties` | Permanently remove the named properties from a Mixpanel user profile ($unset). |
| Update Annotation | `updateAnnotation` | Update an annotation's date and/or description by ID. Requires a Service Account credential. |
| Upsert Schema | `upsertSchema` | Create or update a Lexicon schema for an entity by name. Requires a Service Account credential. |
