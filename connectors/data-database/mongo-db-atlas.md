---
description: "Manage MongoDB Atlas resources through the Atlas Administration API v2 — organizations, projects, clusters, database users, IP access lists, network peering,…"
hidden: true
---

# MongoDB Atlas

<img src="../../.gitbook/assets/connectors/lg/mongo-db-atlas.png" alt="MongoDB Atlas logo">

Manage MongoDB Atlas resources through the Atlas Administration API v2 — organizations, projects, clusters, database users, IP access lists, network peering, backups, alerts, events, teams, and more.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [cloud.mongodb.com](https://cloud.mongodb.com) |
| **Authentication** | Digest auth |
| **Slug** | `mongoDbAtlas` |

## Use it

Add MongoDB Atlas from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mongoDbAtlas.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Acknowledge Alert | `acknowledgeAlert` | Acknowledges or unacknowledges one alert in the specified project. Set acknowledgedUntil to a future timestamp to acknowledge, or a past timestamp to unacknowledge. |
| Add Team Users | `addTeamUsers` | Adds one or more existing organization users to the specified team. The body is a JSON array of objects each containing a user id. |
| Create Alert Configuration | `createAlertConfiguration` | Creates one alert configuration for the specified project. Define the event type, optional matchers and threshold, and the notifications to send when the alert triggers. |
| Create Cluster | `createCluster` | Creates one cluster in the specified project. The replicationSpecs define the cloud provider, region, tier, and node count. Provisioning a dedicated tier incurs cost. |
| Create Custom Database Role | `createCustomDatabaseRole` | Creates one custom database role in the specified project. A role grants privileges (actions on resources) and can inherit other roles. |
| Create Database User | `createDatabaseUser` | Creates one database user in the specified project. The user authenticates via SCRAM password, X.509, AWS IAM, or LDAP, and is granted one or more roles. |
| Create IP Access List Entries | `createProjectIpAccessList` | Adds one or more IP access list entries to the specified project. The body is a JSON array of entry objects, each with an ipAddress, cidrBlock, or awsSecurityGroup plus an optional comment. |
| Create Network Peering Connection | `createNetworkPeeringConnection` | Creates one network peering connection in the specified project. The required body fields depend on the cloud provider (AWS, GCP, or AZURE). |
| Create Network Peering Container | `createNetworkPeeringContainer` | Creates one network peering container in the specified project. A container reserves a CIDR block for one cloud provider region. |
| Create Organization API Key | `createOrganizationApiKey` | Creates one programmatic API key for the specified organization with the given roles. The private key is returned only once. |
| Create Organization Invitation | `createOrganizationInvitation` | Invites one user to join the specified organization with the given roles. |
| Create Project | `createProject` | Creates one project (group) in the specified organization. Requires the API key to have the Organization Owner or Project Creator role. |
| Create Team | `createTeam` | Creates one team in the specified organization and adds the given users to it. |
| Create Third-Party Integration | `createThirdPartyIntegration` | Configures one third-party service integration for the specified project. The required body fields depend on the integration type — e.g. DATADOG needs apiKey and region, WEBHOOK needs url, SLACK needs apiToken. |
| Delete Alert Configuration | `deleteAlertConfiguration` | Removes one alert configuration from the specified project. |
| Delete Cloud Backup Snapshot | `deleteReplicaSetBackup` | Removes one cloud backup snapshot from one cluster in the specified project. |
| Delete Cluster | `deleteCluster` | Removes one cluster from the specified project. The cluster must have termination protection disabled. |
| Delete Custom Database Role | `deleteCustomDatabaseRole` | Removes one custom database role from the specified project. |
| Delete Database User | `deleteDatabaseUser` | Removes one database user from the specified project. |
| Delete IP Access List Entry | `deleteProjectIpAccessListEntry` | Removes one IP access list entry from the specified project, identified by its IP address or CIDR block. |
| Delete Network Peering Connection | `deleteNetworkPeeringConnection` | Removes one network peering connection from the specified project. |
| Delete Organization API Key | `deleteOrganizationApiKey` | Removes one programmatic API key from the specified organization. |
| Delete Organization Invitation | `deleteOrganizationInvitation` | Cancels one pending invitation to the specified organization. |
| Delete Project | `deleteProject` | Removes one project (group). The project must not contain any clusters. |
| Delete Team | `deleteTeam` | Removes one team from the specified organization. |
| Delete Third-Party Integration | `deleteThirdPartyIntegration` | Removes one third-party service integration from the specified project. |
| Get Alert | `getAlert` | Returns one alert that MongoDB Cloud triggered for the specified project. |
| Get Alert Configuration | `getAlertConfiguration` | Returns one alert configuration from the specified project. |
| Get Cloud Backup Schedule | `getBackupSchedule` | Returns the cloud backup schedule for one cluster in the specified project. |
| Get Cloud Backup Snapshot | `getReplicaSetBackup` | Returns one cloud backup snapshot for one cluster in the specified project. |
| Get Cluster | `getCluster` | Returns the details of one cluster in the specified project, identified by cluster name. |
| Get Custom Database Role | `getCustomDatabaseRole` | Returns one custom database role in the specified project, identified by role name. |
| Get Database User | `getDatabaseUser` | Returns one database user in the specified project, identified by authentication database and username. |
| Get IP Access List Entry | `getProjectIpAccessListEntry` | Returns one IP access list entry from the specified project, identified by its IP address or CIDR block. |
| Get Network Peering Connection | `getNetworkPeeringConnection` | Returns one network peering connection in the specified project. |
| Get Organization | `getOrganization` | Returns a single organization identified by its unique 24-hexadecimal-digit ID. |
| Get Organization API Key | `getOrganizationApiKey` | Returns one programmatic API key in the specified organization. |
| Get Organization Event | `getOrganizationEvent` | Returns one event for the specified organization, identified by its event ID. |
| Get Organization Invitation | `getOrganizationInvitation` | Returns one pending invitation to the specified organization. |
| Get Organization Settings | `getOrganizationSettings` | Returns the settings for the specified organization, including API access list and multi-factor authentication requirements. |
| Get Organization User | `getOrganizationUser` | Returns one MongoDB Cloud user who is a member of the specified organization. |
| Get Project | `getProject` | Returns the details of one project identified by its unique 24-hexadecimal-digit ID. |
| Get Project By Name | `getProjectByName` | Returns the details of one project identified by its human-readable name. |
| Get Project Event | `getProjectEvent` | Returns one event for the specified project, identified by its event ID. |
| Get Project Settings | `getProjectSettings` | Returns the settings for the specified project, such as collection of database statistics and realtime performance panel settings. |
| Get Serverless Instance | `getServerlessInstance` | Returns one serverless instance in the specified project, identified by name. |
| Get Team | `getTeam` | Returns one team in the specified organization, identified by team ID. |
| Get Team By Name | `getTeamByName` | Returns one team in the specified organization, identified by team name. |
| Get Third-Party Integration | `getThirdPartyIntegration` | Returns the configuration of one third-party service integration in the specified project. |
| List Alert Configuration Matcher Fields | `listAlertConfigMatcherFields` | Returns all field names that the matchers array in an alert configuration can use to filter the targets an alert applies to. |
| List Alert Configurations | `listAlertConfigurations` | Returns all alert configurations for the specified project. |
| List Alerts | `listAlerts` | Returns all alerts that MongoDB Cloud triggered for the specified project. |
| List Cloud Backup Snapshots | `listReplicaSetBackups` | Returns all cloud backup snapshots for one cluster (replica set) in the specified project. |
| List Clusters | `listClusters` | Returns the details of all clusters in the specified project. |
| List Clusters For All Projects | `listClustersForAllProjects` | Returns the details of all clusters in all projects to which the authenticated API key has access. |
| List Custom Database Roles | `listCustomDatabaseRoles` | Returns all custom database roles in the specified project. |
| List Database Users | `listDatabaseUsers` | Returns all database users that belong to the specified project. |
| List IP Access List Entries | `listProjectIpAccessList` | Returns all IP access list entries for the specified project. Entries control which IP addresses and CIDR blocks can connect to the project's clusters. |
| List Network Peering Connections | `listNetworkPeeringConnections` | Returns all network peering connections in the specified project for the given cloud provider. |
| List Network Peering Containers | `listNetworkPeeringContainers` | Returns all network peering containers in the specified project across all cloud providers. |
| List Organization API Keys | `listOrganizationApiKeys` | Returns all programmatic API keys that belong to the specified organization. |
| List Organization Events | `listOrganizationEvents` | Returns all events for the specified organization. Supports filtering by event type and date range. |
| List Organization Invitations | `listOrganizationInvitations` | Returns all pending invitations to the specified organization. |
| List Organization Projects | `listOrganizationProjects` | Returns all projects (groups) in the specified organization. |
| List Organization Teams | `listOrganizationTeams` | Returns all teams that belong to the specified organization. |
| List Organization Users | `listOrganizationUsers` | Returns all MongoDB Cloud users who are members of the specified organization. |
| List Organizations | `listOrganizations` | Returns all organizations to which the authenticated API key has access. |
| List Project Events | `listProjectEvents` | Returns all events for the specified project. Supports filtering by event type and date range. |
| List Project Processes | `listProjectProcesses` | Returns the details of all MongoDB processes (mongod/mongos) running in the specified project. |
| List Project Users | `listProjectUsers` | Returns all MongoDB Cloud users who are members of the specified project. |
| List Projects | `listProjects` | Returns all projects (groups) the authenticated API key can access across all organizations. |
| List Serverless Instances | `listServerlessInstances` | Returns all serverless instances in the specified project. |
| List Team Users | `listTeamUsers` | Returns all users who are members of the specified team. |
| List Third-Party Integrations | `listThirdPartyIntegrations` | Returns all active third-party service integrations configured for the specified project (e.g. Datadog, PagerDuty, Slack, Webhook). |
| Remove Organization User | `removeOrganizationUser` | Removes one user from the specified organization. Do not use the connected owner's own user ID. |
| Remove Team User | `removeTeamUser` | Removes one user from the specified team. The user remains a member of the organization. |
| Rename Team | `renameTeam` | Renames one team in the specified organization. |
| Return Project Limits | `returnProjectLimits` | Returns all limits for the specified project, such as the maximum number of clusters and database users. |
| Take Cloud Backup Snapshot | `takeSnapshot` | Takes one on-demand cloud backup snapshot of one cluster in the specified project. |
| Toggle Alert Configuration | `toggleAlertConfiguration` | Enables or disables one alert configuration in the specified project without replacing its other fields. |
| Update Alert Configuration | `updateAlertConfiguration` | Replaces one alert configuration in the specified project. This is a full replacement — include all fields you want to keep. |
| Update Cloud Backup Schedule | `updateBackupSchedule` | Updates the cloud backup schedule for one cluster in the specified project, including retention policies and reference backup time. |
| Update Cluster | `updateCluster` | Updates the configuration of one cluster in the specified project. Only the fields you provide are changed. |
| Update Custom Database Role | `updateCustomDatabaseRole` | Updates one custom database role in the specified project. Only the fields you provide are changed. |
| Update Database User | `updateDatabaseUser` | Updates one database user's password, roles, or scopes in the specified project. Only the fields you provide are changed. |
| Update Organization | `updateOrganization` | Updates one organization's name or default alert settings. Only the fields you provide are changed. |
| Update Organization API Key | `updateOrganizationApiKey` | Updates the description or roles of one programmatic API key in the specified organization. |
| Update Organization Invitation | `updateOrganizationInvitation` | Updates the roles or team memberships of one pending organization invitation. |
| Update Organization Settings | `updateOrganizationSettings` | Updates the settings for the specified organization, such as API access list and multi-factor authentication requirements. Only the fields you provide are changed. |
| Update Project | `updateProject` | Updates the name of one project (group). |
| Update Project Settings | `updateProjectSettings` | Updates the settings for the specified project. Only the fields you provide are changed. |
| Update Third-Party Integration | `updateThirdPartyIntegration` | Replaces the configuration of one third-party service integration in the specified project. Provide the full set of fields for the integration type. |
