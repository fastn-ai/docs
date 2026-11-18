---
description: "PostHog product analytics, feature flags, experiments, surveys, session replay, and data management."
hidden: true
---

# PostHog

<img src="../../.gitbook/assets/connectors/lg/posthog.png" alt="PostHog logo">

PostHog product analytics, feature flags, experiments, surveys, session replay, and data management. Wraps the PostHog public REST API (US cloud) plus the event capture/batch ingestion endpoints.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [posthog.com](https://posthog.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `posthog` |

## Use it

Add PostHog from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.posthog.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Capture Event | `captureEvent` | Send a single event to PostHog via the capture ingestion endpoint. Authenticates with the project write API key (phc_) passed as api_key in the body; also identifies/updates the person via distinct_id and properties. |
| Capture Event Batch | `captureBatch` | Send multiple events to PostHog in one request via the batch ingestion endpoint. Authenticates with the project write API key (phc_) in the body. |
| Create Action | `createAction` | Create a new autocapture action with matching steps. |
| Create Annotation | `createAnnotation` | Create a new annotation to mark a point in time on charts. |
| Create Cohort | `createCohort` | Create a new cohort. Provide filters for a dynamic cohort, or set is_static for a manually-managed one. |
| Create Dashboard | `createDashboard` | Create a new dashboard. |
| Create Experiment | `createExperiment` | Create a new A/B test experiment. A feature flag is created from the provided feature_flag_key. |
| Create Feature Flag | `createFeatureFlag` | Create a new feature flag with release conditions. |
| Create Insight | `createInsight` | Create a new insight from a query definition. |
| Create Organization Invite | `createOrganizationInvite` | Invite a new member to the organization by email. |
| Create Project | `createProject` | Create a new project (environment) within the organization. |
| Create Role | `createRole` | Create a new RBAC role in the organization. |
| Create Survey | `createSurvey` | Create a new survey with questions. |
| Delete Action | `deleteAction` | Delete (soft-delete) an autocapture action by ID by setting its deleted flag. |
| Delete Annotation | `deleteAnnotation` | Delete (soft-delete) an annotation by ID by setting its deleted flag. |
| Delete Cohort | `deleteCohort` | Delete a cohort by ID (soft delete via the deleted flag). |
| Delete Dashboard | `deleteDashboard` | Delete a dashboard by ID (soft delete via the deleted flag). |
| Delete Experiment | `deleteExperiment` | Delete an experiment by numeric ID (soft delete via the deleted flag). |
| Delete Feature Flag | `deleteFeatureFlag` | Delete a feature flag by numeric ID (soft delete via the deleted flag). |
| Delete Insight | `deleteInsight` | Delete an insight by numeric ID (soft delete via the deleted flag). |
| Delete Organization Invite | `deleteOrganizationInvite` | Delete (revoke) a pending organization invite by ID. |
| Delete Person Property | `deletePersonProperty` | Remove a single property from a person by their PostHog person ID (UUID). |
| Delete Project | `deleteProject` | Permanently delete a project (environment) by numeric ID. Irreversible. |
| Delete Role | `deleteRole` | Delete an RBAC role by ID. |
| Delete Survey | `deleteSurvey` | Delete a survey by its ID. |
| Get Action | `getAction` | Retrieve a single autocapture action by ID. |
| Get Annotation | `getAnnotation` | Retrieve a single annotation by ID. |
| Get Cohort | `getCohort` | Retrieve a single cohort by ID. |
| Get Current User | `getCurrentUser` | Retrieve the profile of the user that owns the personal API key. |
| Get Dashboard | `getDashboard` | Retrieve a single dashboard by ID, including its tiles. |
| Get Event | `getEvent` | Retrieve a single captured event by its UUID. |
| Get Experiment | `getExperiment` | Retrieve a single experiment by its numeric ID. |
| Get Feature Flag | `getFeatureFlag` | Retrieve a single feature flag by its numeric ID. |
| Get Insight | `getInsight` | Retrieve a single insight by its numeric ID. |
| Get My Feature Flags | `getMyFeatureFlags` | Get the feature flags and their evaluated values for the current user in the project. |
| Get Organization | `getOrganization` | Retrieve the connected organization's details. |
| Get Person | `getPerson` | Retrieve a single person by their PostHog person ID (UUID). |
| Get Project | `getProject` | Retrieve a single project (environment) by its numeric ID, including its ingestion api_token. |
| Get Property Definition | `getPropertyDefinition` | Retrieve a single property definition by its ID. |
| Get Role | `getRole` | Retrieve a single RBAC role by ID. |
| Get Survey | `getSurvey` | Retrieve a single survey by its ID. |
| List Actions | `listActions` | List autocapture actions defined in the project. |
| List Annotations | `listAnnotations` | List annotations (chart markers) defined in the project. |
| List Cohort Persons | `listCohortPersons` | List the persons that belong to a cohort by cohort ID. |
| List Cohorts | `listCohorts` | List cohorts defined in the project. |
| List Dashboards | `listDashboards` | List dashboards defined in the project. |
| List Destinations | `listHogFunctions` | List Hog Functions (destinations, transformations, and other CDP functions) in the project. Destinations are PostHog's mechanism for delivering events to external systems in real time, i.e. outbound webhooks. |
| List Event Definitions | `listEventDefinitions` | List event definitions (event names seen) in the project. |
| List Event Property Values | `listEventValues` | List the distinct values seen for a given event property key. |
| List Events | `listEvents` | List recent events captured in the project, with optional filters. |
| List Experiments | `listExperiments` | List A/B test experiments defined in the project. |
| List Feature Flags | `listFeatureFlags` | List feature flags defined in the project. |
| List Group Types | `listGroupTypes` | List the group types (e.g. company, organization) configured for the project. |
| List Groups | `listGroups` | List groups of a given group type in the project. |
| List Insights | `listInsights` | List insights defined in the project. |
| List Organization Invites | `listOrganizationInvites` | List pending member invites for the connected organization. |
| List Organization Members | `listOrganizationMembers` | List all members of the connected organization. |
| List Organizations | `listOrganizations` | List all organizations the personal API key can access. |
| List Persons | `listPersons` | List persons (users) tracked in the project, with optional search filters. |
| List Persons Activity | `listPersonsActivity` | List the activity log for person changes in the project. |
| List Projects | `listProjects` | List all projects (environments) the personal API key can access in the organization. |
| List Property Definitions | `listPropertyDefinitions` | List property definitions (event or person properties) in the project. |
| List Roles | `listRoles` | List RBAC roles defined in the organization. |
| List Session Recordings | `listSessionRecordings` | List session replay recordings in the project. |
| List Surveys | `listSurveys` | List surveys defined in the project. |
| List Users | `listUsers` | List users visible to the connected account. |
| Run Query | `runQuery` | Run a HogQL or other query node against the project's data and return the result rows. |
| Update Action | `updateAction` | Update an autocapture action's name, description, steps, or settings by ID. |
| Update Annotation | `updateAnnotation` | Update an annotation's content or date marker by ID. |
| Update Cohort | `updateCohort` | Update a cohort's name, description, or filters by ID. |
| Update Dashboard | `updateDashboard` | Update a dashboard's name, description, pinned state, or tags by ID. |
| Update Experiment | `updateExperiment` | Update an experiment's name, description, dates, or metrics by numeric ID. |
| Update Feature Flag | `updateFeatureFlag` | Update a feature flag's name, active state, or release conditions by numeric ID. |
| Update Insight | `updateInsight` | Update an insight's name, description, query, or favorited state by numeric ID. |
| Update Organization | `updateOrganization` | Update the connected organization's settings such as its name. |
| Update Person | `updatePerson` | Update a person's properties by their PostHog person ID (UUID). |
| Update Person Property | `updatePersonProperty` | Set a single property on a person by their PostHog person ID (UUID). |
| Update Project | `updateProject` | Update a project's settings such as its name. |
| Update Role | `updateRole` | Update an RBAC role's name by ID. |
| Update Survey | `updateSurvey` | Update a survey's name, description, questions, or schedule by ID. |
