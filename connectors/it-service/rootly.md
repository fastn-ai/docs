---
description: "Rootly incident management and on-call platform."
hidden: true
---

# Rootly

Rootly incident management and on-call platform. Covers incidents, alerts, severities, teams, services, functionalities, environments, incident types, action items, retrospectives/post-mortems, workflows, schedules, escalation policies, on-call, catalogs, status pages and webhooks via the Rootly JSON:API v1 REST API.

| | |
| --- | --- |
| **Category** | [IT and service management](README.md) |
| **Website** | [rootly.com](https://rootly.com) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Actions** | 578 |
| **Events** | 33 |
| **Slug** | `rootly` |

## Use it

Add Rootly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rootly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Acknowledges an alert | `acknowledgeAlert` | Acknowledges an alert. Acknowledges a specific alert by id |
| Add subscribers to incident | `addSubscribersToIncident` | Add subscribers to incident. Add subscribers to incident |
| Assign user to incident | `assignUserToIncident` | Assign user to incident. Assign user to incident |
| Attach alerts to an incident | `attachAlert` | Attach alerts to an incident. Attach alerts to an incident from provided data |
| Bulk delete Catalog Entities | `bulkDeleteCatalogEntities` | Bulk delete Catalog Entities. Delete catalog entities by external_id list, or prune by managed_by source. Two mutually exclusive modes. |
| Bulk delete Environments | `bulkDeleteEnvironments` | Bulk delete Environments. Delete environments by external_id list, or prune by managed_by source. Two mutually exclusive modes. |
| Bulk delete Functionalities | `bulkDeleteFunctionalities` | Bulk delete Functionalities. Delete functionalities by external_id list, or prune by managed_by source. Two mutually exclusive modes. |
| Bulk delete Services | `bulkDeleteServices` | Bulk delete Services. Delete services by external_id list, or prune by managed_by source. Two mutually exclusive modes. |
| Bulk delete Teams | `bulkDeleteGroups` | Bulk delete Teams. Delete teams by external_id list, or prune by managed_by source. Two mutually exclusive modes. |
| Bulk upsert Catalog Entities | `bulkUpsertCatalogEntities` | Bulk upsert Catalog Entities. Create or update multiple catalog entities by external_id. Only attributes present in the payload are written (managed-fields semantics). Transactional: all succeed or all fail. |
| Bulk upsert Environments | `bulkUpsertEnvironments` | Bulk upsert Environments. Create or update multiple environments by external_id. Only attributes present in the payload are written (managed-fields semantics). Transactional: all succeed or all fail. Requires an API key with both create and update capability across the resource scope (team/org-scoped); record-scoped principals cannot use this endpoint (they receive 404), which also prevents the create-vs-update branch from leaking whether an external_id exists. |
| Bulk upsert Functionalities | `bulkUpsertFunctionalities` | Bulk upsert Functionalities. Create or update multiple functionalities by external_id. Only attributes present in the payload are written (managed-fields semantics). Transactional: all succeed or all fail. Requires an API key with both create and update capability across the resource scope (team/org-scoped); record-scoped principals cannot use this endpoint (they receive 404), which also prevents the create-vs-update branch from leaking whether an external_id exists. |
| Bulk upsert Services | `bulkUpsertServices` | Bulk upsert Services. Create or update multiple services by external_id. Only attributes present in the payload are written (managed-fields semantics). Transactional: all succeed or all fail. Requires an API key with both create and update capability across the resource scope (team/org-scoped); record-scoped principals cannot use this endpoint (they receive 404), which also prevents the create-vs-update branch from leaking whether an external_id exists. |
| Bulk upsert Teams | `bulkUpsertGroups` | Bulk upsert Teams. Create or update multiple teams by external_id. Only attributes present in the payload are written (managed-fields semantics). Transactional: all succeed or all fail. Requires an API key with both create and update capability across the resource scope (team/org-scoped); record-scoped principals cannot use this endpoint (they receive 404), which also prevents the create-vs-update branch from leaking whether an external_id exists. |
| Cancel an incident | `cancelIncident` | Cancel an incident. Cancel a specific incident by id |
| Create a one-time token for agent enrollment | `createPrivateAgentEnrollmentToken` | Create a one-time token for agent enrollment. Issue a one-time token valid for 24 hours. No request body is required. Requires Private Agent management permission plus the Private Agents and AI SRE features. The agent uses this token for gRPC Enroll; the agent record is created on enrollment, not by this request. The plaintext is returned only here and is not recoverable. Repeated requests issue distinct tokens; this endpoint is not idempotent. |
| Create a verified domain | `createVerifiedDomain` | Create a verified domain. |
| Create alert event | `createAlertEvent` | Create alert event. Creates a new alert event |
| Create Alert Field | `createAlertField` | Creates an alert field. Creates a new alert field from provided data |
| Create Alert Group | `createAlertGroup` | Creates an alert group. Creates a new alert group. **Note**: For enhanced functionality and future compatibility, consider using the advanced alert grouping with `conditions` field instead of the legacy `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields. |
| Create Alert Route | `createAlertRoute` | Creates an alert route. Creates a new alert route from provided data. **Note: This endpoint requires access to Advanced Alert Routing. If you're unsure whether you have access to this feature, please contact Rootly customer support.** ## Asynchronous Rule Creation For organizations with large numbers of routing rules, Rootly supports asynchronous rule processing to improve performance. When enabled, rule creation happens in the background. Asynchronous processing is also applied automatically, whether or not it is enabled for your organization, when a request carries a rule graph too large to save within the request timeout. Size is measured in total dependent records — rules plus their condition groups, conditions and destinations — and for an update it includes the rules already on the route, not just those in the payload. **Important**: Whenever rules are processed asynchronously, the rules list in the API response will not be up-to-date immediately after creation. You should ref... |
| Create Alert Urgency | `createAlertUrgency` | Creates an alert urgency. Creates a new alert urgency from provided data |
| Create Dashboard | `createDashboard` | Creates a dashboard. Creates a new dashboard from provided data |
| Create Dashboard Panel | `createDashboardPanel` | Creates a dashboard panel. Creates a new dashboard panel from provided data |
| Create edge connector | `createEdgeConnector` | Create edge connector. |
| Create edge connector action | `createEdgeConnectorAction` | Create edge connector action. |
| Create Escalation Policy | `createEscalationPolicy` | Creates an escalation policy. Creates a new escalation policy from provided data |
| Create Heartbeat | `createHeartbeat` | Creates a heartbeat. Creates a new heartbeat from provided data |
| Create meeting recording | `createMeetingRecording` | Create meeting recording. Invite a recording bot to the incident's meeting. If no previous recordings exist for the platform, a new bot is invited (session 1). If previous sessions exist, a new session is created (re-invite). The bot joins the meeting, records audio/video, and generates a transcript when the session ends. |
| Create On Call Role | `createOnCallRole` | Creates an On-Call Role. Creates a new On-Call Role from provided data |
| Create Schedule | `createSchedule` | Creates a schedule. Creates a new schedule from provided data |
| Create Schedule Rotation | `createScheduleRotation` | Creates a schedule rotation. Creates a new schedule rotation from provided data |
| Create Service | `createService` | Creates a service. Creates a new service from provided data |
| Create Team | `createTeam` | Creates a team. Creates a new team from provided data |
| Create Webhook Endpoint | `createWebhookEndpoint` | Creates a webhook endpoint. Creates a new webhook endpoint from provided data |
| Create Workflow Group | `createWorkflowGroup` | Creates a workflow group. Creates a new workflow group from provided data |
| Creates a catalog | `createCatalog` | Creates a catalog. Creates a new catalog from provided data |
| Creates a catalog checklist template | `createCatalogChecklistTemplate` | Creates a catalog checklist template. Creates a new catalog checklist template |
| Creates a Catalog Entity | `createCatalogEntity` | Creates a Catalog Entity. Creates a new Catalog Entity from provided data |
| Creates a Catalog Property | `createCauseCatalogProperty` | Creates a Catalog Property. Creates a new Catalog Property from provided data |
| Creates a Catalog Property | `createEnvironmentCatalogProperty` | Creates a Catalog Property. Creates a new Catalog Property from provided data |
| Creates a Catalog Property | `createFunctionalityCatalogProperty` | Creates a Catalog Property. Creates a new Catalog Property from provided data |
| Creates a Catalog Property | `createGroupCatalogProperty` | Creates a Catalog Property. Creates a new Catalog Property from provided data |
| Creates a Catalog Property | `createIncidentTypeCatalogProperty` | Creates a Catalog Property. Creates a new Catalog Property from provided data |
| Creates a Catalog Property | `createServiceCatalogProperty` | Creates a Catalog Property. Creates a new Catalog Property from provided data |
| Creates a Catalog Property (alias for field) | `createCatalogProperty` | Creates a Catalog Property (alias for field). Creates a new Catalog Property - returns catalog_properties type |
| Creates a cause | `createCause` | Creates a cause. Creates a new cause from provided data |
| Creates a communications group | `createCommunicationsGroup` | Creates a communications group. Creates a new communications group from provided data |
| Creates a communications stage | `createCommunicationsStage` | Creates a communications stage. Creates a new communications stage from provided data |
| Creates a communications template | `createCommunicationsTemplate` | Creates a communications template. Creates a new communications template from provided data |
| Creates a communications type | `createCommunicationsType` | Creates a communications type. Creates a new communications type from provided data |
| Creates a custom form | `createCustomForm` | Creates a custom form. Creates a new custom form from provided data |
| Creates a Form Field | `createFormField` | Creates a Form Field. Creates a new form_field from provided data |
| Creates a Form Field Placement | `createFormFieldPlacement` | Creates a Form Field Placement. Creates a new form_field_placement from provided data |
| Creates a Form Set | `createFormSet` | Creates a Form Set. Creates a new form_set from provided data |
| Creates a Form Set Condition | `createFormFieldPlacementCondition` | Creates a Form Set Condition. Creates a new form_field_placement_condition from provided data |
| Creates a Form Set Condition | `createFormSetCondition` | Creates a Form Set Condition. Creates a new form_set_condition from provided data |
| Creates a functionality | `createFunctionality` | Creates a functionality. Creates a new functionality from provided data |
| Creates a Live Call Router | `createLiveCallRouter` | Creates a Live Call Router. Creates a new Live Call Router from provided data |
| Creates a playbook | `createPlaybook` | Creates a playbook. Creates a new playbook from provided data |
| Creates a playbook task | `createPlaybookTask` | Creates a playbook task. Creates a new task from provided data |
| Creates a pulse | `createPulse` | Creates a pulse. Creates a new pulse from provided data |
| Creates a retrospective process | `createRetrospectiveProcess` | Creates a retrospective process. Creates a new retrospective process from provided data |
| Creates a retrospective process group | `createRetrospectiveProcessGroup` | Creates a retrospective process group. Creates a new retrospective process group from provided data |
| Creates a retrospective process group step | `createRetrospectiveProcessGroupStep` | Creates a retrospective process group step. Creates a new retrospective process group step from provided data |
| Creates a retrospective step | `createRetrospectiveStep` | Creates a retrospective step. Creates a new retrospective step from provided data |
| Creates a retrospective template | `createPostmortemTemplate` | Creates a retrospective template. Creates a new Retrospective Template from provided data |
| Creates a role | `createRole` | Creates a role. Creates a new role from provided data |
| Creates a schedule rotation active day | `createScheduleRotationActiveDay` | Creates a schedule rotation active day. Creates a new schedule rotation active day from provided data |
| Creates a schedule rotation user | `createScheduleRotationUser` | Creates a schedule rotation user. Creates a new schedule rotation user from provided data |
| Creates a secret | `createSecret` | Creates a secret. Creates a new secret from provided data |
| Creates a severity | `createSeverity` | Creates a severity. Creates a new severity from provided data |
| Creates a status page | `createStatusPage` | Creates a status page. Creates a new status page from provided data |
| Creates a status page announcement | `createStatusPageAnnouncement` | Creates a status page announcement. Posts an announcement to a status page and notifies its subscribers unless notify_subscribers is false |
| Creates a status page component | `createStatusPageComponent` | Creates a status page component. Creates a new status page component from provided data |
| Creates a status page component group | `createStatusPageComponentGroup` | Creates a status page component group. Creates a new status page component group from provided data |
| Creates a status page template | `createStatusPageTemplate` | Creates a status page template. Creates a new template from provided data |
| Creates a Sub-Status | `createSubStatus` | Creates a Sub-Status. Creates a new Sub-Status from provided data |
| Creates a sub-status assignment | `createIncidentSubStatus` | Creates a sub-status assignment. Creates a new sub-status assignment from provided data |
| Creates a user email address | `createUserEmailAddress` | Creates a user email address. Creates a new user email address from provided data |
| Creates a user phone number | `createUserPhoneNumber` | Creates a user phone number. Creates a new user phone number from provided data |
| Creates a workflow | `createWorkflow` | Creates a workflow. Creates a new workflow from provided data |
| Creates a workflow action item form field condition | `createWorkflowActionItemFormFieldCondition` | Creates a workflow action item form field condition. Creates a new workflow action item form field condition from provided data |
| Creates a workflow form field condition | `createWorkflowFormFieldCondition` | Creates a workflow form field condition. Creates a new workflow form field condition from provided data |
| Creates a workflow run | `createWorkflowRun` | Creates a workflow run. Creates a new workflow run from provided data |
| Creates a workflow task | `createWorkflowTask` | Creates a workflow task. Creates a new workflow task from provided data |
| Creates an alert | `createAlert` | Creates an alert. Creates a new alert from provided data |
| Creates an alert routing rule | `createAlertRoutingRule` | Creates an alert routing rule. Creates a new alert routing rule from provided data. **Note: If you are an advanced alert routing user, you should use the Alert Routes endpoint instead of this endpoint. If you don't know whether you are an advanced user, please contact Rootly customer support.** |
| Creates an alert source | `createAlertsSource` | Creates an alert source. Creates a new alert source from provided data |
| Creates an API key | `createApiKey` | Creates an API key. Creates a new API key and returns it with the plaintext token. **The token is only returned once** — store it securely, as it cannot be retrieved again. **Kinds and required fields:** - `personal` — created for the authenticated user. No additional fields required. - `team` — scoped to a team (group). Requires `group_id`. A service account is automatically created with permissions derived from group membership. - `organization` — organization-wide access. Requires owner or admin role. Optionally set `role_id` and `on_call_role_id` to control the service account's permissions. **Expiration:** All keys require an `expires_at` date set in the future (maximum 5 years). Names must be unique within their kind and scope. |
| Creates an authorization | `createAuthorization` | Creates an authorization. Creates a new authorization from provided data |
| Creates an environment | `createEnvironment` | Creates an environment. Creates a new environment from provided data |
| Creates an escalation level for an Escalation Path | `createEscalationLevelPaths` | Creates an escalation level for an Escalation Path. Creates a new escalation level from provided data |
| Creates an escalation level for an Escalation Policy | `createEscalationLevel` | Creates an escalation level for an Escalation Policy. Creates a new escalation level from provided data |
| Creates an escalation path | `createEscalationPath` | Creates an escalation path. Creates a new escalation path from provided data |
| Creates an incident | `createIncident` | Creates an incident. Creates a new incident from provided data |
| Creates an incident action item | `createIncidentActionItem` | Creates an incident action item. Creates a new action item from provided data |
| Creates an incident event | `createIncidentEvent` | Creates an incident event. Creates a new event from provided data |
| Creates an incident event functionality | `createIncidentEventFunctionality` | Creates an incident event functionality. Creates a new event functionality from provided data |
| Creates an incident event service | `createIncidentEventService` | Creates an incident event service. Creates a new event service from provided data |
| Creates an incident feedback | `createIncidentFeedback` | Creates an incident feedback. Creates a new feedback from provided data |
| Creates an incident form field selection | `createIncidentFormFieldSelection` | Creates an incident form field selection. Creates a new incident form field selection from provided data |
| Creates an incident role | `createIncidentRole` | Creates an incident role. Creates a new incident role from provided data |
| Creates an incident role task | `createIncidentRoleTask` | Creates an incident role task. Creates a new task from provided data |
| Creates an incident status page event | `createIncidentStatusPage` | Creates an incident status page event. Creates a new event from provided data |
| Creates an incident type | `createIncidentType` | Creates an incident type. Creates a new incident_type from provided data |
| Creates an incident_permission_set | `createIncidentPermissionSet` | Creates an incident_permission_set. Creates a new incident_permission_set from provided data |
| Creates an incident_permission_set_boolean | `createIncidentPermissionSetBoolean` | Creates an incident_permission_set_boolean. Creates a new incident_permission_set_boolean from provided data |
| Creates an incident_permission_set_resource | `createIncidentPermissionSetResource` | Creates an incident_permission_set_resource. Creates a new incident_permission_set_resource from provided data |
| Creates an On-Call Pay Report | `createOnCallPayReport` | Creates an On-Call Pay Report. Generates a new on-call pay report for the given date range. The report is generated asynchronously. |
| creates an override shift | `createOverrideShift` | creates an override shift. Creates a new override shift from provided data. If any existing override shifts overlap with the specified time range, they will be automatically deleted and replaced by the new override. This endpoint is idempotent: re-sending an identical override (same user and same start/end time) returns the existing override with a 200 status and does not recreate it. |
| creates an shadow configuration | `createOnCallShadow` | creates an shadow configuration. Creates a new on call shadow configuration from provided data |
| Creates an SLA | `createSLA` | Creates an SLA. Creates a new SLA from provided data |
| Creates an user notification rule | `createUserNotificationRule` | Creates an user notification rule. Creates a new user notification rule from provided data |
| Creates FormField Options | `createFormFieldOption` | Creates FormField Options. Creates a new form_field_option from provided data |
| Creates FormField Positions | `createFormFieldPosition` | Creates FormField Positions. Creates a new form field_position from provided data |
| creates shift coverage requests | `createShiftCoverageRequest` | creates shift coverage requests. Creates coverage requests for the shifts overlapping the requested time range. A range can span multiple consecutive shifts (e.g. across a handoff), so one or more coverage requests may be created; the response is always a list. A coverage request broadcasts to schedule members so someone can volunteer to cover the shift, or targets recipient_user_ids when targeted-shift-coverage is enabled. |
| Delete a catalog | `deleteCatalog` | Delete a catalog. Delete a specific catalog by id |
| Delete a catalog checklist template | `deleteCatalogChecklistTemplate` | Delete a catalog checklist template. Delete a specific catalog checklist template by id |
| Delete a Catalog Entity | `deleteCatalogEntity` | Delete a Catalog Entity. Delete a specific Catalog Entity by id |
| Delete a catalog_property | `deleteCatalogProperty` | Delete a catalog_property. Delete a specific catalog_property by id - returns catalog_properties type |
| Delete a cause | `deleteCause` | Delete a cause. Delete a specific cause by id |
| Delete a custom form | `deleteCustomForm` | Delete a custom form. Delete a specific custom form by id |
| Delete a Form Field | `deleteFormField` | Delete a Form Field. Delete a specific form_field by id |
| Delete a Form Field Placement | `deleteFormFieldPlacement` | Delete a Form Field Placement. Delete a specific form_field_placement by id |
| Delete a Form Set | `deleteFormSet` | Delete a Form Set. Delete a specific form_set by id |
| Delete a Form Set Condition | `deleteFormFieldPlacementCondition` | Delete a Form Set Condition. Delete a specific form_field_placement_condition by id |
| Delete a Form Set Condition | `deleteFormSetCondition` | Delete a Form Set Condition. Delete a specific form_set_condition by id |
| Delete a FormFieldPosition | `deleteFormFieldPosition` | Delete a FormFieldPosition. Delete a specific form_field position by id |
| Delete a functionality | `deleteFunctionality` | Delete a functionality. Delete a specific functionality by id |
| Delete a incident event | `deleteStatusPageTemplate` | Delete a incident event. Delete a specific template event by id |
| Delete a Live Call Router | `deleteLiveCallRouter` | Delete a Live Call Router. Delete a specific Live Call Router by id |
| Delete a meeting recording | `deleteMeetingRecording` | Delete a meeting recording. Delete a meeting recording. Only completed or failed recordings can be deleted. Active recordings (pending, recording, paused) must be stopped first. |
| Delete a playbook | `deletePlaybook` | Delete a playbook. Delete a specific playbook by id |
| Delete a playbook task | `deletePlaybookTask` | Delete a playbook task. Delete a specific playbook task by id |
| Delete a retrospective process | `deleteRetrospectiveProcess` | Delete a retrospective process. Delete a specific retrospective process by id |
| Delete a Retrospective Process Group | `deleteRetrospectiveProcessGroup` | Delete a Retrospective Process Group. Delete a specific Retrospective Process Group by id |
| Delete a retrospective step | `deleteRetrospectiveStep` | Delete a retrospective step. Delete a specific retrospective step by id |
| Delete a Retrospective Template | `deletePostmortemTemplate` | Delete a Retrospective Template. Delete a specific Retrospective Template by id |
| Delete a RetrospectiveProcessGroup Step | `deleteRetrospectiveProcessGroupStep` | Delete a RetrospectiveProcessGroup Step. Delete a specific RetrospectiveProcessGroup Step by id |
| Delete a role | `deleteRole` | Delete a role. Delete a specific role by id |
| Delete a schedule rotation | `deleteScheduleRotation` | Delete a schedule rotation. Delete a specific schedule rotation by id |
| Delete a schedule rotation active day | `deleteScheduleRotationActiveDay` | Delete a schedule rotation active day. Delete a specific schedule rotation active day |
| Delete a schedule rotation user | `deleteScheduleRotationUser` | Delete a schedule rotation user. Delete a specific schedule rotation user by id |
| Delete a secret | `deleteSecret` | Delete a secret. Delete a specific secret by id |
| Delete a severity | `deleteSeverity` | Delete a severity. Delete a specific severity by id |
| Delete a standalone meeting recording | `deleteStandaloneMeetingRecording` | Delete a standalone meeting recording. Delete a standalone meeting recording (not linked to an incident). Only the recording owner can delete it. Active recordings (pending, recording, paused) must be stopped first. Returns 404 for incident-linked recordings or recordings owned by another user. |
| Delete a status page | `deleteStatusPage` | Delete a status page. Delete a specific status page by id |
| Delete a status page announcement | `deleteStatusPageAnnouncement` | Delete a status page announcement. Delete a specific status page announcement by id |
| Delete a status page component | `deleteStatusPageComponent` | Delete a status page component. Delete a status page component |
| Delete a status page component group | `deleteStatusPageComponentGroup` | Delete a status page component group. Delete a status page component group together with its components |
| Delete a Sub-Status | `deleteSubStatus` | Delete a Sub-Status. Delete a specific Sub-Status by id |
| Delete a verified domain | `deleteVerifiedDomain` | Delete a verified domain. |
| Delete a workflow | `deleteWorkflow` | Delete a workflow. Delete a specific workflow by id |
| Delete a workflow action item form field condition | `deleteWorkflowActionItemFormFieldCondition` | Delete a workflow action item form field condition. Delete a specific workflow action item form field condition by id |
| Delete a workflow task | `deleteWorkflowTask` | Delete a workflow task. Delete a specific workflow task by id |
| Delete a workflow_form field condition | `deleteWorkflowFormFieldCondition` | Delete a workflow_form field condition. Delete a specific workflow form field condition by id |
| Delete AI chat session | `deleteAiChatSession` | Delete AI chat session. Permanently deletes an AI chat session and all its messages. Requires `ai.chat:write` OAuth scope or an API key. |
| Delete alert event | `deleteAlertEvent` | Delete alert event. Deletes a specific alert event. Only alert events with kind 'note' (user-created notes) can be deleted. System-generated events are immutable to maintain audit trail integrity. |
| Delete Alert Field | `deleteAlertField` | Delete an alert field. Delete a specific alert field by id |
| Delete Alert Group | `deleteAlertGroup` | Delete an alert group. Delete a specific alert group by id |
| Delete Alert Route | `deleteAlertRoute` | Delete an alert route. Delete a specific alert route by id. **Note: This endpoint requires access to Advanced Alert Routing. If you're unsure whether you have access to this feature, please contact Rootly customer support.** |
| Delete Alert Urgency | `deleteAlertUrgency` | Delete an alert urgency. Delete a specific alert urgency by id |
| Delete an alert routing rule | `deleteAlertRoutingRule` | Delete an alert routing rule. Delete a specific alert routing rule by id. **Note: If you are an advanced alert routing user, you should use the Alert Routes endpoint instead of this endpoint. If you don't know whether you are an advanced user, please contact Rootly customer support.** |
| Delete an alert source | `deleteAlertsSource` | Delete an alert source. Delete a specific alert source by id |
| Delete an authorization | `deleteAuthorization` | Delete an authorization. Delete a specific authorization by id |
| Delete an environment | `deleteEnvironment` | Delete an environment. Delete a specific environment by id |
| Delete an escalation level | `deleteEscalationLevel` | Delete an escalation level. Delete a specific escalation level by id |
| Delete an escalation path | `deleteEscalationPath` | Delete an escalation path. Delete a specific escalation path by id |
| Delete an incident | `deleteIncident` | Delete an incident. Delete a specific incident by id |
| Delete an incident action item | `deleteIncidentActionItem` | Delete an incident action item. Delete a specific incident action item by id |
| Delete an incident event | `deleteIncidentEvent` | Delete an incident event. Delete a specific incident event by id |
| Delete an incident event functionalitu | `deleteIncidentEventService` | Delete an incident event functionalitu. Delete a specific incident event service by id |
| Delete an incident event functionality | `deleteIncidentEventFunctionality` | Delete an incident event functionality. Delete a specific incident event functionality by id |
| Delete an incident form field selection | `deleteIncidentFormFieldSelection` | Delete an incident form field selection. Delete a specific incident form field selection by id |
| Delete an incident role | `deleteIncidentRole` | Delete an incident role. Delete a specific incident_role by id |
| Delete an incident role task | `deleteIncidentRoleTask` | Delete an incident role task. Delete a specific incident_role task by id |
| Delete an incident status page event | `deleteIncidentStatusPage` | Delete an incident status page event. Delete a specific incident status page event by id |
| Delete an incident type | `deleteIncidentType` | Delete an incident type. Delete a specific incident_type by id |
| Delete an incident_permission_set | `deleteIncidentPermissionSet` | Delete an incident_permission_set. Delete a specific incident_permission_set by id |
| Delete an incident_permission_set_boolean | `deleteIncidentPermissionSetBoolean` | Delete an incident_permission_set_boolean. Delete a specific incident_permission_set_boolean by id |
| Delete an incident_permission_set_resource | `deleteIncidentPermissionSetResource` | Delete an incident_permission_set_resource. Delete a specific incident_permission_set_resource by id |
| Delete an incident_sub_status | `deleteIncidentSubStatus` | Delete an incident_sub_status. Delete a specific incident_sub_status by id |
| Delete an on call shadow configuration | `deleteOnCallShadow` | Delete an on call shadow configuration. Delete a specific on call shadow configuration by id. Future shadows are hard-deleted. Active shadows (started in the past) have their end time truncated to preserve historical data. |
| Delete an override shift | `deleteOverrideShift` | Delete an override shift. Delete a specific override shift by id |
| Delete an SLA | `deleteSLA` | Delete an SLA. Delete a specific SLA by id |
| Delete an user | `deleteUser` | Delete an user. Delete a specific user by id |
| Delete an user notification rule | `deleteUserNotificationRule` | Delete an user notification rule. Delete a specific user notification rule by id |
| Delete Dashboard | `deleteDashboard` | Delete a dashboard. Delete a specific dashboard by id |
| Delete Dashboard Panel | `deleteDashboardPanel` | Delete a dashboard panel. Delete a specific dashboard panel by id |
| Delete edge connector | `deleteEdgeConnector` | Delete edge connector. |
| Delete edge connector action | `deleteEdgeConnectorAction` | Delete edge connector action. |
| Delete Escalation Policy | `deleteEscalationPolicy` | Delete an escalation policy. Delete a specific escalation policy by id |
| Delete FormField Options | `deleteFormFieldOption` | Delete FormField Options. Delete a specific form_field_option by id |
| Delete Heartbeat | `deleteHeartbeat` | Delete a heartbeat. Delete a specific heartbeat by id |
| Delete On Call Role | `deleteOnCallRole` | Delete an On-Call Role. Delete a specific On-Call Role by id |
| Delete Schedule | `deleteSchedule` | Delete a schedule. Delete a specific schedule by id |
| Delete Service | `deleteService` | Delete a service. Delete a specific service by id |
| Delete Team | `deleteTeam` | Delete a team. Delete a specific team by id |
| Delete user email address | `deleteUserEmailAddress` | Delete user email address. Deletes a user email address |
| Delete user phone number | `deleteUserPhoneNumber` | Delete user phone number. Deletes a user phone number |
| Delete video from a meeting recording | `deleteMeetingRecordingVideo` | Delete video from a meeting recording. Delete only the video file from a meeting recording. The transcript, summary, and all metadata are preserved. Only non-active recordings with an attached video can have their video deleted. |
| Delete Webhook Endpoint | `deleteWebhookEndpoint` | Delete a webhook endpoint. Delete a specific webhook endpoint by id |
| Delete Workflow Group | `deleteWorkflowGroup` | Delete a workflow_group. Delete a specific workflow group by id |
| Deletes a communications group | `deleteCommunicationsGroup` | Deletes a communications group. Deletes a communications group |
| Deletes a communications stage | `deleteCommunicationsStage` | Deletes a communications stage. Deletes a communications stage |
| Deletes a communications template | `deleteCommunicationsTemplate` | Deletes a communications template. Deletes a communications template |
| Deletes a communications type | `deleteCommunicationsType` | Deletes a communications type. Deletes a communications type |
| deletes a shift coverage request | `deleteShiftCoverageRequest` | deletes a shift coverage request. Deletes a shift coverage request. |
| Detach an incident from its parent | `detachFromParentIncident` | Detach an incident from its parent. Detach a sub-incident from its parent incident |
| Duplicates a dashboard | `duplicateDashboard` | Duplicates a dashboard. Duplicates a dashboard |
| Duplicates a dashboard panel | `duplicateDashboardPanel` | Duplicates a dashboard panel. Duplicates a dashboard panel |
| Escalates an alert | `escalateAlert` | Escalates an alert. Escalates a specific alert to the next or specified level in its escalation policy |
| Generate Live Call Router Phone Number | `generateLiveCallRouterPhoneNumber` | Generates a phone number for Live Call Router. Generates a phone number for Live Call Router |
| Get a receipt | `getReceipt` | Get a receipt. Retrieve the delivery receipt for a notification by ID, including its state and (when applicable) failure reason and referenced resource. |
| Get Alert | `getAlert` | Retrieves an alert. Retrieves a specific alert by id |
| Get Alert Event | `getAlertEvent` | Retrieve alert event. Retrieves a specific alert_event by id |
| Get Alert Field | `getAlertField` | Retrieves an alert field. Retrieves a specific alert field by id |
| Get Alert Group | `getAlertGroup` | Retrieves an alert group. Retrieves a specific alert group by id |
| Get Alert Route | `getAlertRoute` | Get an alert route. Get a specific alert route by id. **Note: This endpoint requires access to Advanced Alert Routing. If you're unsure whether you have access to this feature, please contact Rootly customer support.** ## Optional Parameters - **show_nested_ids** (query parameter): When set to `true`, the response will include IDs for all nested resources (destinations, condition_groups, conditions). This is useful when you need to reference these nested resources for updates or deletions via PATCH requests. Example: `GET /v1/alert_routes/{id}?show_nested_ids=true` |
| Get Alert Routing Rule | `getAlertRoutingRule` | Retrieves an alert routing rule. Retrieves a specific alert routing rule by id. **Note: If you are an advanced alert routing user, you should use the Alert Routes endpoint instead of this endpoint. If you don't know whether you are an advanced user, please contact Rootly customer support.** |
| Get Alert Source | `getAlertSource` | Retrieves an alert source. Retrieves a specific alert source by id |
| Get Alert Urgency | `getAlertUrgency` | Retrieves an alert urgency. Retrieves a specific alert urgency by id |
| Get API Key | `getApiKey` | Retrieves an API key. Retrieves a specific API key by its UUID. Returns key metadata including name, kind, expiration, last usage timestamp, and the grace period status — the secret token is never included. |
| Get Authorization | `getAuthorization` | Retrieves an authorization. Retrieves a specific authorization by id |
| Get Catalog | `getCatalog` | Retrieves a catalog. Retrieves a specific catalog by id |
| Get Current User | `getCurrentUser` | Get current user. Get current user |
| Get Custom Field | `getCustomField` | Retrieve a single custom field definition by its id. |
| Get Dashboard | `getDashboard` | Retrieves a dashboard. Retrieves a specific dashboard by id |
| Get Edge Connector | `getEdgeConnector` | Show edge connector. |
| Get Edge Connector Action | `getEdgeConnectorAction` | Show edge connector action. |
| Get Escalation Level | `getEscalationLevel` | Retrieves an escalation level. Retrieves a specific escalation level by id |
| Get Escalation Path | `getEscalationPath` | Retrieves an escalation path. Retrieves a specific escalation path by id |
| Get Escalation Policy | `getEscalationPolicy` | Retrieves an escalation policy. Retrieves a specific escalation policy by id |
| Get functionality incidents chart | `getFunctionalityIncidentsChart` | Get functionality incidents chart. Get functionality incidents chart |
| Get functionality uptime chart | `getFunctionalityUptimeChart` | Get functionality uptime chart. Get functionality uptime chart |
| Get Heartbeat | `getHeartbeat` | Retrieves a heartbeat. Retrieves a specific heartbeat by id |
| Get IP Ranges | `getIpRanges` | Retrieves IP ranges. Retrieves the IP ranges for rootly.com services |
| Get Live Call Router | `getLiveCallRouter` | Retrieves a Live Call Router. Retrieves a specific Live Call Router by id |
| Get Meeting Recording | `getMeetingRecording` | Get a meeting recording. Retrieve a single meeting recording session including its status, duration, speaker count, word count, and transcript summary. |
| Get On Call Shadow | `getOnCallShadow` | Retrieves an On Call Shadow configuration by ID. Retrieves a specific On Call Shadow configuration by ID |
| Get On-Call Pay Report | `getOnCallPayReport` | Retrieves an On-Call Pay Report. Retrieves a specific on-call pay report by id |
| Get On-Call Role | `getOnCallRole` | Retrieves an On-Call Role. Retrieves a specific On-Call Role by id |
| Get Override Shift | `getOverrideShift` | Retrieves an override shift. Retrieves a specific override shift by id |
| Get private agent | `getPrivateAgent` | Get private agent. Return provider inventory and last-reported health for one agent. Requires Private Agent read permission plus the Private Agents and AI SRE features. Credentials and capability schemas are never returned. |
| Get Schedule | `getSchedule` | Retrieves a schedule. Retrieves a specific schedule by id |
| Get Schedule Rotation | `getScheduleRotation` | Retrieves a schedule rotation. Retrieves a specific schedule rotation by id |
| Get Schedule Shifts | `getScheduleShifts` | Retrieves a schedule shifts. Retrieves schedule shifts |
| Get Service | `getService` | Retrieves a service. Retrieves a specific service by id |
| Get Service Incidents Chart | `getServiceIncidentsChart` | Get service incidents chart. Get service incidents chart |
| Get Service Uptime Chart | `getServiceUptimeChart` | Get service uptime chart. Get service uptime chart |
| Get Shift Coverage Request | `getShiftCoverageRequest` | retrieves a shift coverage request. Retrieves a specific shift coverage request. |
| Get Status | `getStatus` | Retrieves a Status. Retrieves a specific Status by id |
| Get Team | `getTeam` | Retrieves a team. Retrieves a specific team by id |
| Get Team Incidents Chart | `getTeamIncidentsChart` | Get team incidents chart. Get team incidents chart |
| Get User | `getUser` | Retrieves an user. Retrieves a specific user by id |
| Get Webhook Delivery | `getWebhookDelivery` | Retrieves a webhook delivery. Retrieves a specific webhook delivery by id |
| Get Webhook Endpoint | `getWebhookEndpoint` | Retrieves a webhook endpoint. Retrieves a specific webhook endpoint by id |
| Get Workflow | `getWorkflow` | Retrieves a workflow. Retrieves a specific workflow by id |
| Get Workflow Group | `getWorkflowGroup` | Retrieves a workflow group. Retrieves a specific workflow group by id |
| Get Workflow Task | `getWorkflowTask` | Retrieves a workflow task. Retrieves a specific workflow_task by id |
| Grants a team access to a status page | `createStatusPageTeam` | Grants a team access to a status page. Assigns a team to a status page. Members of the team get the chosen permission level on that page in addition to their role. Requires an owner or admin role. |
| Import a meeting recording | `importMeetingRecording` | Import a meeting recording. Import an externally captured meeting recording and attach it to an incident. Video and transcript are fetched asynchronously. The existing POST /v1/incidents/{incident_id}/meeting_recordings endpoint invites a bot — this endpoint handles recordings that were captured outside of the bot flow. |
| Leave a meeting call | `leaveMeetingRecording` | Leave a meeting call. Remove the recording bot from the meeting entirely. Unlike stop, this immediately disconnects the bot. The session will transition to analyzing and then completed once transcript processing finishes. |
| List AI chat session messages | `listAiChatSessionMessages` | List AI chat session messages. Returns the user and assistant message history for a session, paginated and chronologically ordered. Internal tool messages are filtered out. Requires `ai.chat:read` OAuth scope or an API key. |
| List AI home chat sessions | `listAiChatSessions` | List AI home chat sessions. Returns the caller's active, unbound AI home chat sessions newest-first, cursor-paginated by `before`. Requires `ai.chat:read` OAuth scope or a personal API key, and the caller must be eligible for home chat. |
| List Alert Events Feed | `listAlertEventsFeed` | List alert events across alerts. Returns a flat list of alert events across all alerts the requester can access. Designed for periodic polling: use `page[after]` with the `next_cursor` returned in the previous response to stream forward. |
| List Alert Events For Alert | `listAlertEventsForAlert` | List alert events. List alert_events |
| List Alert Fields | `listAlertFields` | List alert fields. List alert fields |
| List Alert Groups | `listAlertGroups` | List alert groups. List alert groups |
| List Alert Routes | `listAlertRoutes` | List alert routes. List all alert routes for the current team with filtering and pagination. **Note: This endpoint requires access to Advanced Alert Routing. If you're unsure whether you have access to this feature, please contact Rootly customer support.** |
| List Alert Routing Rules | `listAlertRoutingRules` | List alert routing rules. List alert routing rules. **Note: If you are an advanced alert routing user, you should use the Alert Routes endpoint instead of this endpoint. If you don't know whether you are an advanced user, please contact Rootly customer support.** |
| List Alert Sources | `listAlertSources` | List alert sources. List alert sources |
| List Alert Urgencies | `listAlertUrgencies` | List alert urgencies. List alert urgencies |
| List Alerts | `listAlerts` | List alerts. List alerts |
| List all action items for an organization | `listAllIncidentActionItems` | List all action items for an organization. List all action items for an organization |
| List API Keys | `listApiKeys` | List API keys. List API keys for the current organization. Returns key metadata including name, kind, expiration, and last usage — the secret token value is never included in the response. **API key kinds:** - `personal` — tied to a specific user, inherits that user's permissions. - `team` — scoped to one or more teams (groups), creates a service account with permissions derived from group membership. - `organization` — organization-wide, creates a service account with a configurable role and on-call role. **Automated rotation workflow:** Use `filter[expires_at][lt]` to find keys approaching expiration, then call the rotate endpoint to issue a new token before the old one expires. Combine with `filter[active]=true` to exclude already-expired keys. **Sorting:** Use the `sort` parameter with a field name (e.g., `sort=expires_at`). Prefix with `-` for descending order (e.g., `sort=-created_at`). Allowed fields: `name`, `kind`, `created_at`, `updated_at`, `expires_at`, `last_used_at`. |
| List Audit Log Entries | `listAudits` | List audits. List audits |
| List Authorizations | `listAuthorizations` | List authorizations. List authorizations |
| List catalog checklist templates | `listCatalogChecklistTemplates` | List catalog checklist templates. List catalog checklist templates |
| List Catalog Entities | `listCatalogEntities` | List Catalog Entities. List Catalog Entities |
| List catalog entity checklists | `listCatalogEntityChecklists` | List catalog entity checklists. List catalog entity checklists |
| List Catalog Properties | `listCatalogProperties` | List Catalog Properties (alias for fields). List Catalog Properties - returns catalog_properties type |
| List Catalogs | `listCatalogs` | List catalogs. List catalogs |
| List Cause Catalog Properties | `listCauseCatalogProperties` | List Catalog Properties. List Cause Catalog Properties |
| List causes | `listCauses` | List causes. List causes |
| List Custom Field Options | `listCustomFieldOptions` | List the selectable options of one custom field. |
| List Custom Fields | `listCustomFields` | List incident custom field definitions. |
| List custom forms | `listCustomForms` | List custom forms. List custom forms |
| List Dashboard Panels | `listDashboardPanels` | List dashboard panels. List dashboard panels |
| List Dashboards | `listDashboards` | List dashboards. List dashboards |
| List Edge Connector Actions | `listEdgeConnectorActions` | List edge connector actions. |
| List Edge Connectors | `listEdgeConnectors` | List edge connectors. |
| List Environment Catalog Properties | `listEnvironmentCatalogProperties` | List Catalog Properties. List Environment Catalog Properties |
| List environments | `listEnvironments` | List environments. List environments |
| List Escalation Levels | `listEscalationLevels` | List escalation levels for an Escalation Policy. List escalation levels |
| List escalation levels for an Escalation Path | `listEscalationLevelsPaths` | List escalation levels for an Escalation Path. List escalation levels |
| List Escalation Paths | `listEscalationPaths` | List escalation paths. List escalation paths |
| List Escalation Policies | `listEscalationPolicies` | List escalation policies. List escalation policies |
| List Form Field Placements | `listFormFieldPlacements` | List Form Field Placements. List form_field_placements |
| List Form Fields | `listFormFields` | List Form Fields. List form_fields |
| List Form Set Conditions | `listFormFieldPlacementConditions` | List Form Set Conditions. List form_field_placement_conditions |
| List Form Set Conditions | `listFormSetConditions` | List Form Set Conditions. List form_set_conditions |
| List Form Sets | `listFormSets` | List Form Sets. List form_sets |
| List FormField Options | `listFormFieldOptions` | List FormField Options. List form_field_options |
| List FormField Position | `listFormFieldPositions` | List FormField Position. List form field positions |
| List functionalities | `listFunctionalities` | List functionalities. List functionalities |
| List Functionality Catalog Properties | `listFunctionalityCatalogProperties` | List Catalog Properties. List Functionality Catalog Properties |
| List Heartbeats | `listHeartbeats` | List heartbeats. List heartbeats |
| List incident action items | `listIncidentActionItems` | List incident action items. List incident action items |
| List Incident alerts | `listIncidentAlerts` | List Incident alerts. List incident alerts |
| List incident event functionalities | `listIncidentEventFunctionalities` | List incident event functionalities. List incident event functionalities |
| List incident event services | `listIncidentEventServices` | List incident event services. List incident event services |
| List incident events | `listIncidentEvents` | List incident events. List incident events |
| List incident feedbacks | `listIncidentFeedbacks` | List incident feedbacks. List incident feedbacks |
| List incident form field selections | `listIncidentFormFieldSelections` | List incident form field selections. List incident form field selections |
| List incident retrospectives | `listIncidentPostMortems` | List incident retrospectives. List incident retrospectives |
| List incident role tasks | `listIncidentRoleTasks` | List incident role tasks. List incident_role tasks |
| List incident roles | `listIncidentRoles` | List incident roles. List incident roles |
| List incident status page events | `listIncidentStatusPages` | List incident status page events. List incident status page events |
| List Incident Type Catalog Properties | `listIncidentTypeCatalogProperties` | List Catalog Properties. List IncidentType Catalog Properties |
| List incident types | `listIncidentTypes` | List incident types. List incident types |
| List incident_permission_set_booleans | `listIncidentPermissionSetBooleans` | List incident_permission_set_booleans. List incident_permission_set_booleans |
| List incident_permission_set_resources | `listIncidentPermissionSetResources` | List incident_permission_set_resources. List incident_permission_set_resources |
| List incident_permission_sets | `listIncidentPermissionSets` | List incident_permission_sets. List incident_permission_sets |
| List incident_sub_statuses | `listIncidentSubStatuses` | List incident_sub_statuses. List incident_sub_statuses |
| List Incidents | `listIncidents` | List incidents. List incidents |
| List Live Call Routers | `listLiveCallRouters` | List Live Call Routers. List Live Call Routers |
| List Meeting Recordings | `listMeetingRecordings` | List all meeting recordings. List meeting recordings across the organization. Returns the current user's standalone recordings plus incident-backed recordings the user can access. Supports filtering by status, platform, and created_by. |
| List meeting recordings for an incident | `listIncidentMeetingRecordings` | List meeting recordings. List all meeting recording sessions for an incident. Returns recordings sorted by session number. Each recording represents one bot session with its own transcript, status, and metadata. |
| List On-Call Pay Reports | `listOnCallPayReports` | List On-Call Pay Reports. List on-call pay reports |
| List On-Call Roles | `listOnCallRoles` | List On-Call Roles. List On-Call Roles |
| List On-Call Shadows | `listOnCallShadows` | List On Call Shadows for Shift. List shadow shifts for schedule |
| List Override Shifts | `listOverrideShifts` | List override shifts. List override shifts |
| List playbook tasks | `listPlaybookTasks` | List playbook tasks. List playbook tasks |
| List playbooks | `listPlaybooks` | List playbooks. List playbooks |
| List private agents | `listPrivateAgents` | List private agents. List this tenant's agents, including revoked and offline agents. Inventory pages omit provider snapshots to bound database and response costs; use Get private agent for provider inventory and last-reported health. Requires Private Agent management access plus the Private Agents and AI SRE features. Credentials and capability schemas are never returned. |
| List pulses | `listPulses` | List pulses. List pulses |
| List retrospective configurations | `listRetrospectiveConfigurations` | List retrospective configurations. List retrospective configurations |
| List Retrospective Process Groups | `listRetrospectiveProcessGroups` | List Retrospective Process Groups. List Retrospective Process Groups |
| List retrospective processes | `listRetrospectiveProcesses` | List retrospective processes. List retrospective processes |
| List retrospective steps | `listRetrospectiveSteps` | List retrospective steps. List retrospective steps |
| List Retrospective Templates | `listPostmortemTemplates` | List Retrospective Templates. List Retrospective Templates |
| List RetrospectiveProcessGroup Steps | `listRetrospectiveProcessGroupSteps` | List RetrospectiveProcessGroup Steps. List RetrospectiveProcessGroup Steps |
| List roles | `listRoles` | List roles. List roles |
| List Schedule Rotation Active Days | `listScheduleRotationActiveDays` | List schedule rotation active days. List schedule rotation active days |
| List Schedule Rotation Users | `listScheduleRotationUsers` | List schedule rotation users. |
| List Schedule Rotations | `listScheduleRotations` | List schedule rotations. List schedule rotations |
| List Schedules | `listSchedules` | List schedules. List schedules |
| List secrets | `listSecrets` | List secrets. List secrets |
| List Service Catalog Properties | `listServiceCatalogProperties` | List Catalog Properties. List Service Catalog Properties |
| List Services | `listServices` | List services. List services |
| List severities | `listSeverities` | List severities. List severities |
| List Shift Coverage Requests | `listShiftCoverageRequests` | list shift coverage requests. List active shift coverage requests for a schedule. |
| List Shifts | `listShifts` | List shifts. List shifts |
| List SLAs | `listSLAs` | List SLAs. List SLAs |
| List status page announcements | `listStatusPageAnnouncements` | List status page announcements. List status page announcements |
| List status page component groups | `listStatusPageComponentGroups` | List status page component groups. List status page component groups |
| List status page components | `listStatusPageComponents` | List status page components. List status page components |
| List status page templates | `listStatusPageTemplates` | List status page templates. List status page templates |
| List status pages | `listStatusPages` | List status pages. List status pages |
| List Statuses | `listStatuses` | List Statuses. List Statuses |
| List Sub-Statuses | `listSubStatuses` | List Sub-Statuses. List Sub-Statuses |
| List Team Catalog Properties | `listTeamCatalogProperties` | List Catalog Properties. List Group Catalog Properties |
| List Teams | `listTeams` | List teams. List teams |
| List User Email Addresses | `listUserEmailAddresses` | Retrieves user email addresses. Retrieves all email addresses for the specified user |
| List User Notification Rules | `listUserNotificationRules` | List user notification rules. List user notification rules |
| List User Phone Numbers | `listUserPhoneNumbers` | Retrieves user phone numbers. Retrieves all phone numbers for the specified user |
| List Users | `listUsers` | List users. List users |
| List verified domains | `listVerifiedDomains` | List verified domains. |
| List Webhook Deliveries | `listWebhookDeliveries` | List webhook deliveries. List webhook deliveries for given endpoint |
| List Webhook Endpoints | `listWebhookEndpoints` | List webhook endpoints. List webhook endpoints |
| List Who Is On Call | `listOncalls` | List on-calls. List who is currently on-call, with support for filtering by escalation policy, schedule, and user. Returns on-call entries grouped by escalation policy level. |
| List workflow action item form field conditions | `listWorkflowActionItemFormFieldConditions` | List workflow action item form field conditions. List workflow action item form field conditions |
| List workflow form field conditions | `listWorkflowFormFieldConditions` | List workflow form field conditions. List workflow form field conditions |
| List Workflow Groups | `listWorkflowGroups` | List workflow groups. List workflow groups |
| List Workflow Runs | `listWorkflowRuns` | List workflow runs. List workflow runs |
| List Workflow Tasks | `listWorkflowTasks` | List workflow tasks. List workflow tasks |
| List Workflows | `listWorkflows` | List workflows. List workflows |
| Lists communications groups | `listCommunicationsGroups` | Lists communications groups. Lists communications groups |
| Lists communications stages | `listCommunicationsStages` | Lists communications stages. Lists communications stages |
| Lists communications templates | `listCommunicationsTemplates` | Lists communications templates. Lists communications templates |
| Lists communications types | `listCommunicationsTypes` | Lists communications types. Lists communications types |
| Lists the teams with access to a status page | `listStatusPageTeams` | Lists the teams with access to a status page. Lists the teams assigned to a status page, oldest first |
| Mark an incident as a duplicate | `markAsDuplicateIncident` | Mark an incident as a duplicate. Mark an incident as a duplicate |
| Mitigate an incident | `mitigateIncident` | Mitigate an incident. Mitigate a specific incident by id |
| Pause a meeting recording | `pauseMeetingRecording` | Pause a meeting recording. Pause an active recording session. The bot remains in the meeting but stops capturing audio/video. Use the resume endpoint to continue recording. |
| Ping a heartbeat | `pingHeartbeat` | Ping a heartbeat. Ping a specific heartbeat by id |
| Regenerate an On-Call Pay Report | `regenerateOnCallPayReport` | Regenerate an On-Call Pay Report. Triggers regeneration of an existing on-call pay report. |
| Remove assigned user from incident | `removeAssignedUserFromIncident` | Remove assigned user from incident. Remove assigned user from incident |
| Remove duplicate marking from an incident | `unmarkAsDuplicateIncident` | Remove duplicate marking from an incident. Remove the duplicate marking from an incident |
| Remove subscribers from incident | `removeSubscribersToIncident` | Remove subscribers from incident. Remove subscribers to incident |
| Removes a team's access to a status page | `deleteStatusPageTeam` | Removes a team's access to a status page. Removes a team from a status page. Its members lose the page access the assignment granted on their next request. Requires an owner or admin role. |
| Rename AI chat session | `updateAiChatSession` | Rename AI chat session. Renames an AI home chat session; a blank or null title resets to the generated title. Requires `ai.chat:write` OAuth scope or a personal API key, and the caller must be eligible for home chat. |
| Resend verification code | `resendVerificationUserPhoneNumber` | Resend verification code. Resends a verification code to the phone number. SMS sends are limited per recipient to 3 per hour and 5 per day. An application rate-limit 429 response includes Retry-After with the remaining wait in seconds. |
| Resends verification email | `resendUserEmailAddressVerification` | Resends verification email. Resends verification email for an email address |
| Resolve an incident | `resolveIncident` | Resolve an incident. Resolve a specific incident by id |
| Resolves an alert | `resolveAlert` | Resolves an alert. Resolves a specific alert by id |
| Restart an incident | `restartIncident` | Restart an incident. Restart a specific incident by id |
| Resume a meeting recording | `resumeMeetingRecording` | Resume a meeting recording. Resume a paused recording session. The bot continues capturing audio/video from the meeting. |
| Retrieves a catalog checklist template | `getCatalogChecklistTemplate` | Retrieves a catalog checklist template. Retrieves a specific catalog checklist template by id |
| Retrieves a Catalog Entity | `getCatalogEntity` | Retrieves a Catalog Entity. Retrieves a specific Catalog Entity by id |
| Retrieves a catalog entity checklist | `getCatalogEntityChecklist` | Retrieves a catalog entity checklist. Retrieves a specific catalog entity checklist by id |
| Retrieves a Catalog Property (alias for field) | `getCatalogProperty` | Retrieves a Catalog Property (alias for field). Retrieves a specific Catalog Property by id - returns catalog_properties type |
| Retrieves a cause | `getCause` | Retrieves a cause. Retrieves a specific cause by id |
| Retrieves a custom form | `getCustomForm` | Retrieves a custom form. Retrieves a specific custom form by id |
| Retrieves a dashboard panel | `getDashboardPanel` | Retrieves a dashboard panel. Retrieves a specific dashboard panel by id |
| Retrieves a Form Field | `getFormField` | Retrieves a Form Field. Retrieves a specific form_field by id |
| Retrieves a Form Field Placement | `getFormFieldPlacement` | Retrieves a Form Field Placement. Retrieves a specific form_field_placement by id |
| Retrieves a Form Set | `getFormSet` | Retrieves a Form Set. Retrieves a specific form_set by id |
| Retrieves a Form Set Condition | `getFormFieldPlacementCondition` | Retrieves a Form Set Condition. Retrieves a specific form_field_placement_condition by id |
| Retrieves a Form Set Condition | `getFormSetCondition` | Retrieves a Form Set Condition. Retrieves a specific form_set_condition by id |
| Retrieves a FormFieldPosition | `getFormFieldPosition` | Retrieves a FormFieldPosition. Retrieves a specific form field_position by id |
| Retrieves a functionality | `getFunctionality` | Retrieves a functionality. Retrieves a specific functionality by id |
| Retrieves a playbook | `getPlaybook` | Retrieves a playbook. Retrieves a specific playbook by id |
| Retrieves a playbook task | `getPlaybookTask` | Retrieves a playbook task. Retrieves a specific playbook_task by id |
| Retrieves a pulse | `getPulse` | Retrieves a pulse. Retrieves a specific pulse by id |
| Retrieves a Retrospective Configuration | `getRetrospectiveConfiguration` | Retrieves a Retrospective Configuration. Retrieves a specific retrospective_configuration by id |
| Retrieves a retrospective process | `getRetrospectiveProcess` | Retrieves a retrospective process. Retrieves a specific retrospective process by id |
| Retrieves a Retrospective Process Group | `getRetrospectiveProcessGroup` | Retrieves a Retrospective Process Group. Retrieves a specific Retrospective Process Group by id |
| Retrieves a retrospective step | `getRetrospectiveStep` | Retrieves a retrospective step. Retrieves a specific retrospective step by id |
| Retrieves a Retrospective Template | `getPostmortemTemplate` | Retrieves a Retrospective Template. Retrieves a specific Retrospective Template by id |
| Retrieves a RetrospectiveProcessGroup Step | `getRetrospectiveProcessGroupStep` | Retrieves a RetrospectiveProcessGroup Step. Retrieves a specific RetrospectiveProcessGroup Step by id |
| Retrieves a role | `getRole` | Retrieves a role. Retrieves a specific role by id |
| Retrieves a schedule rotation active day | `getScheduleRotationActiveDay` | Retrieves a schedule rotation active day. Retrieves a specific schedule rotation active day by id |
| Retrieves a schedule rotation user | `getScheduleRotationUser` | Retrieves a schedule rotation user. Retrieves a specific schedule rotation user by id |
| Retrieves a secret | `getSecret` | Retrieves a secret. Retrieve a specific secret by id |
| Retrieves a severity | `getSeverity` | Retrieves a severity. Retrieves a specific severity by id |
| Retrieves a status page | `getStatusPage` | Retrieves a status page. Retrieves a specific status page by id |
| Retrieves a status page announcement | `getStatusPageAnnouncement` | Retrieves a status page announcement. Retrieves a specific status page announcement by id |
| Retrieves a status page component | `getStatusPageComponent` | Retrieves a status page component. Retrieves a status page component |
| Retrieves a status page component group | `getStatusPageComponentGroup` | Retrieves a status page component group. Retrieves a status page component group |
| Retrieves a status page team assignment | `getStatusPageTeam` | Retrieves a status page team assignment. Retrieves a specific status page team assignment by id |
| Retrieves a status page template | `getStatusPageTemplate` | Retrieves a status page template. Retrieves a specific status_page_template by id |
| Retrieves a Sub-Status | `getSubStatus` | Retrieves a Sub-Status. Retrieves a specific Sub-Status by id |
| Retrieves a workflow action item form field condition | `getWorkflowActionItemFormFieldCondition` | Retrieves a workflow action item form field condition. Retrieves a specific workflow action item form field condition by id |
| Retrieves a workflow form field condition | `getWorkflowFormFieldCondition` | Retrieves a workflow form field condition. Retrieves a specific workflow form field condition by id |
| Retrieves an environment | `getEnvironment` | Retrieves an environment. Retrieves a specific environment by id |
| Retrieves an incident | `getIncident` | Retrieves an incident. Retrieves a specific incident by id |
| Retrieves an incident action item | `getIncidentActionItems` | Retrieves an incident action item. Retrieves a specific incident_action_item by id |
| Retrieves an incident event | `getIncidentEvents` | Retrieves an incident event. Retrieves a specific incident_event by id |
| Retrieves an incident event functionality | `getIncidentEventFunctionalities` | Retrieves an incident event functionality. Retrieves a specific incident_event_functionality by id |
| Retrieves an incident event service | `getIncidentEventServices` | Retrieves an incident event service. Retrieves a specific incident_event_service by id |
| Retrieves an incident feedback | `getIncidentFeedbacks` | Retrieves an incident feedback. Retrieves a specific incident_feedback by id |
| Retrieves an incident form field selection | `getIncidentFormFieldSelection` | Retrieves an incident form field selection. Retrieves a specific incident form field selection by id |
| Retrieves an incident retrospective | `listIncidentPostmortem` | Retrieves an incident retrospective. List incidents retrospectives |
| Retrieves an incident retrospective step | `getIncidentRetrospectiveStep` | Retrieves an incident retrospective step. Retrieves a specific incident retrospective step by id |
| Retrieves an incident role | `getIncidentRole` | Retrieves an incident role. Retrieves a specific incident_role by id |
| Retrieves an incident role task | `getIncidentRoleTask` | Retrieves an incident role task. Retrieves a specific incident_role_task by id |
| Retrieves an incident status page event | `getIncidentStatusPages` | Retrieves an incident status page event. Retrieves a specific incident_status_page_event by id |
| Retrieves an incident type | `getIncidentType` | Retrieves an incident type. Retrieves a specific incident_type by id |
| Retrieves an incident_permission_set | `getIncidentPermissionSet` | Retrieves an incident_permission_set. Retrieves a specific incident_permission_set by id |
| Retrieves an incident_permission_set_boolean | `getIncidentPermissionSetBoolean` | Retrieves an incident_permission_set_boolean. Retrieves a specific incident_permission_set_boolean by id |
| Retrieves an incident_permission_set_resource | `getIncidentPermissionSetResource` | Retrieves an incident_permission_set_resource. Retrieves a specific incident_permission_set_resource by id |
| Retrieves an SLA | `getSLA` | Retrieves an SLA. Retrieves a specific SLA by id |
| Retrieves an user notification rule | `getUserNotificationRule` | Retrieves an user notification rule. Retrieves a specific user notification rule by id |
| Retrieves FormField Options | `getFormFieldOption` | Retrieves FormField Options. Retrieves a specific form_field_option by id |
| Retrieves incident_sub_status | `getIncidentSubStatus` | Retrieves incident_sub_status. Retrieves a specific incident_sub_status by id |
| Retrieves the team's alert configuration | `getAlertConfiguration` | Retrieves the team's alert configuration. |
| Retry Webhook Delivery | `retryWebhookDelivery` | Retries a webhook delivery. Retries a webhook delivery |
| Revoke an API key | `deleteApiKey` | Revoke an API key. Revoke an API key. The key is immediately invalidated and can no longer be used for authentication. This action cannot be undone. For `team` and `organization` keys, the associated service account is also deleted. Any active sessions using this key will fail on the next request. |
| Revoke private agent | `revokePrivateAgent` | Revoke private agent. Invalidate access and refresh credentials and remove provider routing registrations. Requires Private Agent delete permission plus the Private Agents and AI SRE features. Retains the agent and invocation history. Repeated revocation is safe. An executing customer-side operation is not guaranteed to stop immediately. Use a new enrollment token to re-enroll a revoked installation. |
| Rotate an API key | `rotateApiKey` | Rotate an API key. Rotate an API key's token. Issues a new secret token and returns it — **the new token is only shown once**, so store it securely. **Self-only:** You can only rotate the API key that was used to authenticate this request. Attempting to rotate a different key returns `403 Forbidden`. **Grace period:** When enabled for your organization, the previous token remains valid after rotation, giving you time to deploy the new token without downtime. Pass `grace_period_minutes` (integer, 0–1440, default 30) to control how long the old token stays valid. Set to 0 to immediately invalidate the old token. The `grace_period_ends_at` field in the response confirms the exact time the old token will stop working. **Expiration:** Optionally provide a new `expires_at` date (ISO 8601, up to 5 years). Defaults to 90 days from now if omitted. Dates in the past are rejected. **Typical rotation workflow:** 1. Call this endpoint to get a new token (optionally with a custom `grace_period_mi... |
| Send AI chat message | `createAiChat` | Send AI chat message. Send a message to the AI assistant and receive a synchronous reply. Optionally bind the conversation to an incident or alert for context-aware responses. For eligible unbound home chat, `checkpoint_id` and `decision` confirm or cancel approval-gated writes. Responses include `confirmation` for a pending write and `checkpoint_resolved` after resume. If an action-item write needs required fields the model did not supply, no checkpoint is created and the turn completes with a plain reply linking to that incident's action-item form in the Rootly web app. The synchronous response has no `confirmation` key; only `confirmation` responses are resumable. Requires `ai.chat:write` OAuth scope or an API key. |
| Send verification code | `verifyUserPhoneNumber` | Send verification code. Sends a verification code to the phone number. SMS sends are limited per recipient to 3 per hour and 5 per day. An application rate-limit 429 response includes Retry-After with the remaining wait in seconds. |
| Sets dashboard to user default | `setDefaultDashboard` | Sets dashboard to user default. Sets dashboard to user default |
| Show a verified domain | `getVerifiedDomain` | Show a verified domain. |
| Show user email address | `showUserEmailAddress` | Show user email address. Retrieves a specific user email address |
| Show user phone number | `showUserPhoneNumber` | Show user phone number. Retrieves a specific user phone number |
| Shows a communications group | `getCommunicationsGroup` | Shows a communications group. Shows details of a communications group |
| Shows a communications stage | `getCommunicationsStage` | Shows a communications stage. Shows details of a communications stage |
| Shows a communications template | `getCommunicationsTemplate` | Shows a communications template. Shows details of a communications template |
| Shows a communications type | `getCommunicationsType` | Shows a communications type. Shows details of a communications type |
| Snoozes an alert | `snoozeAlert` | Snoozes an alert. Snoozes a specific alert by id, extending the acknowledgment timeout |
| Start a recording session | `startRecordingSession` | Start a recording session. Start a new desktop recording session. The server creates a recording record and returns a stream token the desktop client uses to send audio. No provider-specific configuration is needed from the client. |
| Stop a meeting recording | `stopMeetingRecording` | Stop a meeting recording. Stop an active or paused recording. The bot finishes processing, generates a transcript, and the session status transitions to completed. This is irreversible — to record again, create a new session. |
| Stream AI chat response (SSE) | `streamAiChat` | Stream AI chat response (SSE). Send a message and receive the AI response as a Server-Sent Events stream. Optionally bind to an incident or alert for context. For eligible unbound home chat, `checkpoint_id` and `decision` confirm or cancel approval-gated writes. Events include `confirmation_required` for pending writes and `checkpoint_resolved` before replay. If an action-item write needs required fields the model did not supply, no checkpoint is created and the turn completes with a plain reply linking to that incident's action-item form in the Rootly web app. The stream emits `done` with `status: complete` and no `confirmation_required` event; only `confirmation_required` events are resumable. `status` events carry a short progress line (`{status}`) such as the running tool's title or its progress message; they never include tool arguments or results. Requires `ai.chat:write` OAuth scope or an API key. |
| Triage an incident | `triageIncident` | Triage an incident. Set a specific incident by ID to triage state |
| Trigger an audit for a catalog checklist template | `triggerCatalogChecklistTemplate` | Trigger an audit for a catalog checklist template. Triggers an audit for all applicable entities of the checklist template |
| Update a catalog | `updateCatalog` | Update a catalog. Update a specific catalog by id |
| Update a catalog checklist template | `updateCatalogChecklistTemplate` | Update a catalog checklist template. Update a specific catalog checklist template by id |
| Update a Catalog Entity | `updateCatalogEntity` | Update a Catalog Entity. Update a specific Catalog Entity by id |
| Update a catalog_property (alias for field) | `updateCatalogProperty` | Update a catalog_property (alias for field). Update a specific catalog_property by id - returns catalog_properties type |
| Update a cause | `updateCause` | Update a cause. Update a specific cause by id |
| Update a custom form | `updateCustomForm` | Update a custom form. Update a specific custom form by id |
| Update a Form Field | `updateFormField` | Update a Form Field. Update a specific form_field by id |
| Update a Form Field Placement | `updateFormFieldPlacement` | Update a Form Field Placement. Update a specific form_field_placement by id |
| Update a Form Set | `updateFormSet` | Update a Form Set. Update a specific form_set by id |
| Update a Form Set Condition | `updateFormFieldPlacementCondition` | Update a Form Set Condition. Update a specific form_field_placement_condition by id |
| Update a Form Set Condition | `updateFormSetCondition` | Update a Form Set Condition. Update a specific form_set_condition by id |
| Update a FormFieldPosition | `updateFormFieldPosition` | Update a FormFieldPosition. Update a specific form_field position by id |
| Update a functionality | `updateFunctionality` | Update a functionality. Update a specific functionality by id |
| Update a Live Call Router | `updateLiveCallRouter` | Update a Live Call Router. Update a specific Live Call Router by id |
| Update a playbook | `updatePlaybook` | Update a playbook. Update a specific playbook by id |
| Update a playbook task | `updatePlaybookTask` | Update a playbook task. Update a specific playbook task by id |
| Update a pulse | `updatePulse` | Update a pulse. Update a specific pulse by id |
| Update a retrospective configuration | `updateRetrospectiveConfiguration` | Update a retrospective configuration. Update a specific retrospective configuration by id |
| Update a retrospective process | `updateRetrospectiveProcess` | Update a retrospective process. Updates a specific retrospective process by id |
| Update a Retrospective Process Group | `updateRetrospectiveProcessGroup` | Update a Retrospective Process Group. Update a specific Retrospective Process Group by id |
| Update a retrospective step | `updateRetrospectiveStep` | Update a retrospective step. Update a specific retrospective step by id |
| Update a Retrospective Template | `updatePostmortemTemplate` | Update a Retrospective Template. Update a specific Retrospective Template by id |
| Update a role | `updateRole` | Update a role. Update a specific role by id |
| Update a schedule rotation | `updateScheduleRotation` | Update a schedule rotation. Update a specific schedule rotation by id |
| Update a schedule rotation active day | `updateScheduleRotationActiveDay` | Update a schedule rotation active day. Update a specific schedule rotation active day by id |
| Update a secret | `updateSecret` | Update a secret. Update a specific secret by id |
| Update a severity | `updateSeverity` | Update a severity. Update a specific severity by id |
| Update a status page | `updateStatusPage` | Update a status page. Update a specific status page by id |
| Update a status page announcement | `updateStatusPageAnnouncement` | Update a status page announcement. Update a specific status page announcement by id |
| Update a status page component | `updateStatusPageComponent` | Update a status page component. Update a status page component |
| Update a status page component group | `updateStatusPageComponentGroup` | Update a status page component group. Update a status page component group |
| Update a Sub-Status | `updateSubStatus` | Update a Sub-Status. Update a specific Sub-Status by id |
| Update a user | `updateUser` | Update a user. Update a specific user by id |
| Update a workflow | `updateWorkflow` | Update a workflow. Update a specific workflow by id |
| Update a workflow action item form field condition | `updateWorkflowActionItemFormFieldCondition` | Update a workflow action item form field condition. Update a specific workflow action item form field condition by id |
| Update a workflow form field condition | `updateWorkflowFormFieldCondition` | Update a workflow form field condition. Update a specific workflow form field condition by id |
| Update a workflow task | `updateWorkflowTask` | Update a workflow task. Update a specific workflow task by id |
| Update alert | `updateAlert` | Update alert. Updates an alert |
| Update alert event | `updateAlertEvent` | Update alert event. Updates a specific alert event. Only alert events with kind 'note' (user-created notes) can be updated. System-generated events are immutable to maintain audit trail integrity. |
| Update Alert Field | `updateAlertField` | Update an alert field. Update a specific alert field by id |
| Update Alert Group | `updateAlertGroup` | Update an alert group. Update a specific alert group by id. **Note**: For enhanced functionality and future compatibility, consider using the advanced alert grouping with `conditions` field instead of the legacy `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields. |
| Update Alert Route | `updateAlertRoute` | Update an alert route. Update a specific alert route by id. **Note: This endpoint requires access to Advanced Alert Routing. If you're unsure whether you have access to this feature, please contact Rootly customer support.** ### Asynchronous Rule Creation For organizations with large numbers of routing rules, Rootly supports asynchronous rule processing to improve performance. When enabled, rule updates happen in the background. Asynchronous processing is also applied automatically, whether or not it is enabled for your organization, when a request carries a rule graph too large to save within the request timeout. Size is measured in total dependent records — rules plus their condition groups, conditions and destinations — and includes the rules already on the route, not just those in the payload, so a small payload against a large route may still be processed asynchronously. **Important**: Whenever rules are processed asynchronously, the rules list in the API response will not be u... |
| Update Alert Urgency | `updateAlertUrgency` | Update an alert urgency. Update a specific alert urgency by id |
| Update an alert route | `patchAlertRoute` | Update an alert route. Updates an alert route. **Note: This endpoint requires access to Advanced Alert Routing. If you're unsure whether you have access to this feature, please contact Rootly customer support.** |
| Update an alert routing rule | `updateAlertRoutingRule` | Update an alert routing rule. Update a specific alert routing rule by id. **Note: If you are an advanced alert routing user, you should use the Alert Routes endpoint instead of this endpoint. If you don't know whether you are an advanced user, please contact Rootly customer support.** |
| Update an alert source | `updateAlertsSource` | Update an alert source. Update a specific alert source by id |
| Update an API key | `updateApiKey` | Update an API key. Update an API key's mutable attributes: `name`, `description`, and `expires_at`. The key's `kind`, `role_id`, `on_call_role_id`, and token cannot be changed after creation. To issue a new token, use the rotate endpoint. To change the role or kind, revoke the key and create a new one. The new `expires_at` must be in the future and within 5 years. |
| Update an authorization | `updateAuthorization` | Update an authorization. Update a specific authorization by id |
| Update an environment | `updateEnvironment` | Update an environment. Update a specific environment by id |
| Update an escalation level | `updateEscalationLevel` | Update an escalation level. Update a specific escalation level by id |
| Update an escalation path | `updateEscalationPath` | Update an escalation path. Update a specific escalation path by id |
| Update an incident | `updateIncident` | Update an incident. Update a specific incident by id |
| Update an incident action item | `updateIncidentActionItem` | Update an incident action item. Update a specific incident action item by id |
| Update an incident event | `updateIncidentEvent` | Update an incident event. Update a specific incident event by id |
| Update an incident event | `updateIncidentEventFunctionality` | Update an incident event. Update a specific incident event functionality by id |
| Update an incident event | `updateIncidentEventService` | Update an incident event. Update a specific incident event service by id |
| Update an incident feedback | `updateIncidentFeedback` | Update an incident feedback. Update a specific incident feedback by id |
| Update an incident form field selection | `updateIncidentFormFieldSelection` | Update an incident form field selection. Update a specific incident form field selection by id |
| Update an incident retrospective | `updateIncidentPostmortem` | Update an incident retrospective. Update a specific incident retrospective by id. The body may be written as `content` (or its alias `smart_content`) and is sanitized to the tags the retrospective editor supports. When no `title` is sent and the body opens with an `&lt;h1&gt;`, that heading becomes the retrospective title, matching the editor. Once a retrospective has been opened in the collaborative editor that editor owns the body, and body writes are rejected with a 409. |
| Update an incident retrospective step | `updateIncidentRetrospectiveStep` | Update an incident retrospective step. Update a specific incident retrospective step by id |
| Update an incident role | `updateIncidentRole` | Update an incident role. Update a specific incident_role by id |
| Update an incident role task | `updateIncidentRoleTask` | Update an incident role task. Update a specific incident_role task by id |
| Update an incident status page event | `updateIncidentStatusPage` | Update an incident status page event. Update a specific incident status page event by id |
| Update an incident type | `updateIncidentType` | Update an incident type. Update a specific incident_type by id |
| Update an incident_permission_set | `updateIncidentPermissionSet` | Update an incident_permission_set. Update a specific incident_permission_set by id |
| Update an incident_permission_set_boolean | `updateIncidentPermissionSetBoolean` | Update an incident_permission_set_boolean. Update a specific incident_permission_set_boolean by id |
| Update an incident_permission_set_resource | `updateIncidentPermissionSetResource` | Update an incident_permission_set_resource. Update a specific incident_permission_set_resource by id |
| Update an On Call Shadow configuration | `updateOnCallShadow` | Update an On Call Shadow configuration. Update a specific on call shadow configuration by id |
| Update an On-Call Pay Report | `updateOnCallPayReport` | Update an On-Call Pay Report. Update a specific on-call pay report by id. Triggers report regeneration. |
| Update an override shift | `updateOverrideShift` | Update an override shift. Update a specific override shift by id |
| Update an SLA | `updateSLA` | Update an SLA. Update a specific SLA by id |
| Update an user notification rule | `updateUserNotificationRule` | Update an user notification rule. Update a specific user notification rule by id |
| Update Dashboard | `updateDashboard` | Update a dashboard. Update a specific dashboard by id |
| Update Dashboard Panel | `updateDashboardPanel` | Update a dashboard panel. Update a specific dashboard panel by id |
| Update edge connector | `updateEdgeConnector` | Update edge connector. |
| Update edge connector action | `updateEdgeConnectorAction` | Update edge connector action. |
| Update Escalation Policy | `updateEscalationPolicy` | Update an escalation policy. Update a specific escalation policy by id |
| Update FormField Options | `updateFormFieldOption` | Update FormField Options. Update a specific form_field_option by id |
| Update Heartbeat | `updateHeartbeat` | Update a heartbeat. Update a specific heartbeat by id |
| Update incident_sub_status | `updateIncidentSubStatus` | Update incident_sub_status. Update a specific incident_sub_status by id |
| Update On Call Role | `updateOnCallRole` | Update an On-Call Role. Update a specific On-Call Role by id |
| Update private agent metadata | `updatePrivateAgent` | Update private agent metadata. Update routing metadata or pause tool execution without disconnecting the agent. The agent UUID and provider IDs remain the execution identities. Requires Private Agent update permission. |
| Update RetrospectiveProcessGroup Step | `updateRetrospectiveProcessGroupStep` | Update RetrospectiveProcessGroup Step. Update a specific RetrospectiveProcessGroup Step by id |
| Update Schedule | `updateSchedule` | Update a schedule. Updates a specific schedule by id |
| Update schedule rotation user | `updateScheduleRotationUser` | Update schedule rotation user. Update a specific schedule rotation user by id |
| Update Service | `updateService` | Update a service. Update a specific service by id |
| Update status page template | `updateStatusPageTemplate` | Update status page template. Update a specific template event by id |
| Update Team | `updateTeam` | Update a team. Update a specific team by id |
| Update user email address | `updateUserEmailAddress` | Update user email address. Updates a user email address |
| Update user phone number | `updateUserPhoneNumber` | Update user phone number. Updates a user phone number |
| Update Webhook Endpoint | `updateWebhookEndpoint` | Update a webhook endpoint. Update a specific webhook endpoint by id |
| Update Workflow Group | `updateWorkflowGroup` | Update a workflow group. Update a specific workflow group by id |
| Updates a communications group | `updateCommunicationsGroup` | Updates a communications group. Updates a communications group |
| Updates a communications stage | `updateCommunicationsStage` | Updates a communications stage. Updates a communications stage |
| Updates a communications template | `updateCommunicationsTemplate` | Updates a communications template. Updates a communications template |
| Updates a communications type | `updateCommunicationsType` | Updates a communications type. Updates a communications type |
| Updates a status page team assignment | `updateStatusPageTeam` | Updates a status page team assignment. Changes the permission level of a team on a status page. Requires an owner or admin role. To move the grant to another team, delete it and create a new one. |
| Updates the team's alert configuration | `updateAlertConfiguration` | Updates the team's alert configuration. |
| Verifies an email address with token | `verifyUserEmailAddress` | Verifies an email address with token. Verifies an email address using a verification token |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Alert Created | `alert.created` | A new on-call alert was raised. |
| Alert Updated | `alert.updated` | An alert was acknowledged, escalated, snoozed or resolved. |
| Audit Log Entry Created | `audit_log.created` | A new audit log entry was written. |
| Incident Cancelled | `incident.cancelled` | An incident was cancelled. |
| Incident Created | `incident.created` | A new incident was declared in Rootly. |
| Incident Deleted | `incident.deleted` | An incident was deleted. |
| Incident In Triage | `incident.in_triage` | An incident moved into triage. |
| Incident Mitigated | `incident.mitigated` | An incident was mitigated. |
| Incident Resolved | `incident.resolved` | An incident was resolved. |
| Incident Timeline Event Created | `incident_event.created` | A timeline event was added to an incident. |
| Incident Timeline Event Deleted | `incident_event.deleted` | A timeline event was removed. |
| Incident Timeline Event Updated | `incident_event.updated` | A timeline event changed. |
| Incident Updated | `incident.updated` | An incident's attributes changed. |
| On-Call Shift Ended | `shift.ended` | An on-call shift ended. |
| On-Call Shift Started | `shift.started` | An on-call shift began. |
| Pulse Created | `pulse.created` | A pulse (low-signal event) was recorded. |
| Retrospective Created | `incident_post_mortem.created` | A post-mortem/retrospective was created. |
| Retrospective Deleted | `incident_post_mortem.deleted` | A post-mortem/retrospective was deleted. |
| Retrospective Published | `incident_post_mortem.published` | A post-mortem/retrospective was published. |
| Retrospective Updated | `incident_post_mortem.updated` | A post-mortem/retrospective changed. |
| Scheduled Incident Completed | `incident.scheduled.completed` | A scheduled maintenance window completed. |
| Scheduled Incident Created | `incident.scheduled.created` | A scheduled maintenance incident was created. |
| Scheduled Incident Deleted | `incident.scheduled.deleted` | A scheduled maintenance incident was deleted. |
| Scheduled Incident In Progress | `incident.scheduled.in_progress` | A scheduled maintenance window started. |
| Scheduled Incident Updated | `incident.scheduled.updated` | A scheduled maintenance incident changed. |
| Status Page Event Created | `incident_status_page_event.created` | A status page event was created for an incident. |
| Status Page Event Deleted | `incident_status_page_event.deleted` | A status page event was deleted. |
| Status Page Event Updated | `incident_status_page_event.updated` | A status page event changed. |
| Workflow Run Canceled | `genius_workflow_run.canceled` | A Rootly workflow run was canceled. |
| Workflow Run Completed | `genius_workflow_run.completed` | A Rootly workflow run completed. |
| Workflow Run Failed | `genius_workflow_run.failed` | A Rootly workflow run failed. |
| Workflow Run Queued | `genius_workflow_run.queued` | A Rootly workflow run was queued. |
| Workflow Run Started | `genius_workflow_run.started` | A Rootly workflow run started. |
