---
description: "DNSFilter is a cloud-based DNS security and content filtering platform."
hidden: true
---

# DNSFilter

DNSFilter is a cloud-based DNS security and content filtering platform. This connector wraps the DNSFilter public REST API (api.dnsfilter.com v1/v2): organizations, users, policies, networks, roaming clients (user agents), block pages, IP/MAC addresses, scheduled policies and reports, traffic reports and analytics, dashboards, billing and MSP/distributor management.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [dnsfilter.com](https://dnsfilter.com) |
| **Authentication** | Bearer token |
| **Actions** | 276 |
| **Events** | 0 |
| **Slug** | `dnsfilter` |

## Use it

Add DNSFilter from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dnsfilter.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Allowed Application To Policy | `addAllowedApplicationToPolicy` | Add a single application to a DNSFilter policy's allow list by application name. |
| Add Allowed Domain To Policy | `addAllowedDomainToPolicy` | Add a single domain to a DNSFilter policy's allow list, with a note explaining why. |
| Add Blocked Application To Policy | `addBlockedApplicationToPolicy` | Add a single application to a DNSFilter policy's block list by application name. |
| Add Blocked Category To Policy | `addBlockedCategoryToPolicy` | Add a single content category to a DNSFilter policy's block list. |
| Add Blocked Domain To Policy | `addBlockedDomainToPolicy` | Add a single domain to a DNSFilter policy's block list, with a note explaining why. |
| Add Distributor Organization SKU | `addDistributorOrganizationSku` | Add a product SKU to a sub-organization under the authenticated DNSFilter distributor. |
| Add Distributor User Membership | `addDistributorUserMembership` | Grant a distributor dashboard user membership of an organization with a role. |
| Add User To Collection | `addUserToCollection` | Add a user to a DNSFilter collection. |
| Batch Delete Domain Notes | `batchDeleteDomainNotes` | Delete the notes for several domains on a DNSFilter resource in one call. |
| Batch Update Domain Notes | `batchUpdateDomainNotes` | Update the notes for several domains on a DNSFilter resource in one call. |
| Bulk Add Allowlist Domains | `bulkAddAllowlistDomains` | Add one or more domains to the allow list of one or more DNSFilter policies. |
| Bulk Add Blocklist Domains | `bulkAddBlocklistDomains` | Add one or more domains to the block list of one or more DNSFilter policies. |
| Bulk Create Networks | `bulkCreateNetworks` | Start an asynchronous bulk creation of several DNSFilter networks. Returns a job id to poll for status. |
| Bulk Delete Networks | `bulkDeleteNetworks` | Start an asynchronous bulk deletion of DNSFilter networks by id. Returns a job id to poll for status. |
| Bulk Look Up Domains | `bulkLookupDomains` | Get the domains and DNSFilter content categories associated with each FQDN in a comma-separated list. |
| Bulk Remove Allowlist Domains | `bulkRemoveAllowlistDomains` | Remove one or more domains from the allow list of one or more DNSFilter policies. |
| Bulk Remove Blocklist Domains | `bulkRemoveBlocklistDomains` | Remove one or more domains from the block list of one or more DNSFilter policies. |
| Bulk Update Networks | `bulkUpdateNetworks` | Start an asynchronous bulk update of policy, scheduled policy and block page across several DNSFilter networks. |
| Bulk Update Organizations | `bulkUpdateOrganizations` | Update shared settings across one or more DNSFilter organizations in a single call. |
| Cancel Distributor MSP | `cancelDistributorMsp` | Cancel an MSP managed by the authenticated DNSFilter distributor. |
| Cancel Distributor Suborganization | `cancelDistributorSuborganization` | Cancel a sub-organization under the authenticated DNSFilter distributor. |
| Cancel Organization | `cancelOrganization` | Mark a DNSFilter organization as cancelled, ending its subscription. |
| Change Password | `changePassword` | Change the password of the currently authenticated DNSFilter user. |
| Check Roaming Clients For Mixed Values | `checkUserAgentsHaveMixedValues` | Check whether a selection of DNSFilter roaming clients has mixed values for the bulk-editable settings. |
| Create Agent Local User Bulk Delete | `createAgentLocalUserBulkDelete` | Start a bulk deletion job for DNSFilter agent local users selected by id or filter. |
| Create Agent Local Users CSV Export | `createAgentLocalUsersCsvExport` | Start a CSV export of DNSFilter agent local users and get the export record to poll. |
| Create API Key | `createApiKey` | Create a new DNSFilter API key for the current user. The full token value is returned only once, in the create response. |
| Create Billing Payment Method | `createBillingPaymentMethod` | Register a newly created Stripe payment method against a DNSFilter organization. |
| Create Block Page | `createBlockPage` | Create a new DNSFilter block page, the branded page shown to end users when a request is blocked. |
| Create CyberSight CSV Export | `createCyberSightCsvExport` | Start a CSV export of a DNSFilter CyberSight report over a date range. |
| Create Dashboard | `createDashboard` | Create a DNSFilter dashboard with its widget layout. |
| Create Distributor MSP | `createDistributorMsp` | Create a new MSP under the authenticated DNSFilter distributor. |
| Create Distributor Suborganization | `createDistributorSuborganization` | Create a sub-organization under an MSP managed by the authenticated DNSFilter distributor. |
| Create Distributor User | `createDistributorUser` | Create a dashboard user under the authenticated DNSFilter distributor. This sends a real invitation email. |
| Create Enterprise Connection | `createEnterpriseConnection` | Create an OIDC SSO enterprise connection for a DNSFilter organization. |
| Create IP Address | `createIpAddress` | Register a new public IP address against a DNSFilter network so traffic from it is filtered by that network's policy. |
| Create MAC Address | `createMacAddress` | Create a DNSFilter MAC address record so a specific device is filtered by its own policy. |
| Create Network | `createNetwork` | Create a new DNSFilter network (site) and attach policies, a block page and IP addresses to it. |
| Create Network Secret Key | `createNetworkSecretKey` | Create a DNSFilter network secret key used by roaming clients to join the network. |
| Create Network Subnet | `createNetworkSubnet` | Create a subnet inside a DNSFilter network so a LAN IP range gets its own policy and block page. |
| Create Networks CSV Export | `createNetworksCsvExport` | Start a CSV export of DNSFilter networks and get the export record to poll. |
| Create Organization | `createOrganization` | Create a new DNSFilter organization. Requires MSP privileges on the authenticated account. |
| Create Organization User | `createOrganizationUser` | Add a new or existing user to a DNSFilter organization. This sends a real invitation email to the address supplied. |
| Create Policy | `createPolicy` | Create a new DNSFilter filtering policy with safe-search, allow list, block list and blocked category settings. |
| Create Roaming Client Bulk Delete | `createUserAgentBulkDelete` | Start a bulk deletion job for DNSFilter roaming clients matching the given filters or ids. |
| Create Roaming Client Bulk Update | `createUserAgentBulkUpdate` | Start a bulk update job applying a changeset to DNSFilter roaming clients selected by id or filter. |
| Create Roaming Client Cleanup | `createUserAgentCleanup` | Create a DNSFilter roaming client cleanup rule that removes clients inactive for a given number of days. |
| Create Roaming Client CSV Export | `createUserAgentCsvExport` | Start a CSV export of DNSFilter roaming clients and get the export record to poll. |
| Create Scheduled Policy | `createScheduledPolicy` | Create a DNSFilter scheduled policy that rotates between filtering policies on a timetable. |
| Create Scheduled Report | `createScheduledReport` | Create a DNSFilter scheduled email report. Recipients receive real emails on the chosen frequency. |
| Create Scheduled Report Preview | `createScheduledReportPreview` | Create a DNSFilter scheduled report preview, triggering background generation of a sample report. |
| Create Trial | `createTrial` | Start a DNSFilter trial subscription for an organization on the given SKU. |
| Delete Agent Local User | `deleteAgentLocalUser` | Delete a DNSFilter agent local user by id. |
| Delete API Key | `deleteApiKey` | Permanently remove a DNSFilter API key by id. |
| Delete Block Page | `deleteBlockPage` | Delete a DNSFilter block page by id. |
| Delete Dashboard | `deleteDashboard` | Delete a DNSFilter dashboard by id. |
| Delete Domain Note | `deleteDomainNote` | Delete the note recorded against a domain on a DNSFilter resource. |
| Delete Enterprise Connection | `deleteEnterpriseConnection` | Delete a DNSFilter SSO enterprise connection by id. |
| Delete IP Address | `deleteIpAddress` | Remove a DNSFilter IP address record by id. |
| Delete MAC Address | `deleteMacAddress` | Delete a DNSFilter MAC address record by id. |
| Delete Network | `deleteNetwork` | Delete a DNSFilter network by id. |
| Delete Network Secret Key | `deleteNetworkSecretKey` | Revoke the secret key of a DNSFilter network. |
| Delete Network Subnet | `deleteNetworkSubnet` | Delete a subnet from a DNSFilter network. |
| Delete Organization | `deleteOrganization` | Delete an MSP customer organization in DNSFilter. Destructive and irreversible. |
| Delete Organization User | `deleteOrganizationUser` | Remove a user from a DNSFilter organization. The user account itself is not deleted. |
| Delete Policy | `deletePolicy` | Delete a DNSFilter filtering policy by id. |
| Delete Roaming Client | `deleteUserAgent` | Delete a DNSFilter roaming client, optionally queueing an uninstall on the device. |
| Delete Scheduled Policy | `deleteScheduledPolicy` | Delete a DNSFilter scheduled policy by id. |
| Delete Scheduled Report | `deleteScheduledReport` | Delete a DNSFilter scheduled email report by id. |
| Dequeue Roaming Client Uninstall | `dequeueUserAgentUninstall` | Cancel a queued uninstall for a DNSFilter roaming client. |
| Export Roaming Clients CSV | `exportUserAgentsCsv` | Download the DNSFilter roaming clients of an organization as CSV. |
| Get Active Agents QPS Report | `getQpsActiveAgentsReport` | Get the DNSFilter queries-per-second report broken down by active roaming clients. |
| Get Active Organizations QPS Report | `getQpsActiveOrganizationsReport` | Get the DNSFilter queries-per-second report broken down by active organizations. |
| Get Agent Local User | `getAgentLocalUser` | Get a single DNSFilter agent local user by id. |
| Get Agent Local User Bulk Delete | `getAgentLocalUserBulkDelete` | Get the status of a DNSFilter agent local user bulk delete job. |
| Get Agent Local User Bulk Delete Counts | `getAgentLocalUserBulkDeleteCounts` | Get the progress counts of a DNSFilter agent local user bulk delete job. |
| Get Agent Local User Counts | `getAgentLocalUserCounts` | Get counts of DNSFilter agent local users by policy assignment status. |
| Get Agent Local Users CSV Export | `getAgentLocalUsersCsvExport` | Get the status and download details of a DNSFilter agent local users CSV export. |
| Get API Key | `getApiKey` | Display a single DNSFilter API key by id. The secret value is not returned. |
| Get Application | `getApplication` | Get basic information for a single DNSFilter application by id. |
| Get Application Category | `getApplicationCategory` | Get basic information for a single DNSFilter application category by id. |
| Get Application Policies | `getApplicationPolicies` | Get how a specific application is allowed or blocked across the policies of an organization. |
| Get Application Requests By Agent Report | `getApplicationRequestsByAgentReport` | Get DNSFilter application request statistics broken down by roaming client. |
| Get Application Requests By Collection Report | `getApplicationRequestsByCollectionReport` | Get DNSFilter application request statistics broken down by collection. |
| Get Application Requests By Network Report | `getApplicationRequestsByNetworkReport` | Get DNSFilter application request statistics broken down by network. |
| Get Application Requests By User Report | `getApplicationRequestsByUserReport` | Get DNSFilter application request statistics broken down by end user. |
| Get Application Requests Report | `getApplicationRequestsReport` | Get total DNSFilter application request statistics for a period. |
| Get Billing Address | `getBillingAddress` | Show the billing address for the given DNSFilter organization. |
| Get Billing Information | `getBilling` | Show the basic billing information registered in Stripe for the given DNSFilter organization. |
| Get Block Page | `getBlockPage` | Get a single DNSFilter block page by id, optionally including its relationships. |
| Get Bulk Network Create Status | `getBulkCreateNetworksStatus` | Get the status of an asynchronous DNSFilter bulk network creation job. |
| Get Bulk Network Delete Status | `getBulkDeleteNetworksStatus` | Get the status of an asynchronous DNSFilter bulk network deletion job. |
| Get Bulk Network Update Status | `getBulkUpdateNetworksStatus` | Get the status of an asynchronous DNSFilter bulk network update job. |
| Get Category | `getCategory` | Get basic information for a single DNSFilter content category by id. |
| Get Category Requests By Organization Report | `getTotalCategoriesByOrganizationReport` | Get total DNSFilter requests per content category broken down by organization. |
| Get Category Stats Report | `getCategoryStatsReport` | Get DNSFilter summary statistics for specific content categories in an organization. |
| Get Client Stats Report | `getClientStatsReport` | Get DNSFilter summary client statistics for an organization over a period. |
| Get Collection User | `getCollectionUser` | Get the details of a single user within a DNSFilter collection. |
| Get Current Invoice | `getCurrentInvoice` | Get the estimated DNSFilter invoice for the upcoming month for the current user. |
| Get Current User | `getCurrentUser` | Fetch information about the currently authenticated DNSFilter user. |
| Get CyberSight CSV Export | `getCyberSightCsvExport` | Get the status and download details of a DNSFilter CyberSight CSV export. |
| Get Deployments Report | `getDeploymentsReport` | Get the count of DNSFilter deployments (networks and roaming clients) for an organization. |
| Get Distributor | `getDistributor` | Get the DNSFilter distributor record for the authenticated distributor account. |
| Get Distributor Covered Users Summary | `getDistributorCoveredUsersSummary` | Get the DNSFilter covered-users summary per organization for the authenticated distributor over a date range. |
| Get Distributor Health | `getDistributorHealth` | Health check for the DNSFilter distributor API. |
| Get Distributor MSP | `getDistributorMsp` | Get a single MSP managed by the authenticated DNSFilter distributor. |
| Get Distributor Organization | `getDistributorOrganization` | Get a single sub-organization under the authenticated DNSFilter distributor. |
| Get Distributor Usage By Organization | `getDistributorUsageByOrganization` | Get DNSFilter usage per organization for the authenticated distributor over a date range. |
| Get Distributor Usage By SKU | `getDistributorUsageBySku` | Get DNSFilter usage per product SKU for the authenticated distributor over a date range. |
| Get Distributor User | `getDistributorUser` | Get a single dashboard user under the authenticated DNSFilter distributor. |
| Get Distributor User Reset Password URL | `getDistributorUserResetPasswordUrl` | Generate a password reset URL for a distributor dashboard user without sending an email. |
| Get Domain Note | `getDomainNote` | Get the note recorded against a domain on a DNSFilter policy or other resource. |
| Get Domain Requests By Organization Report | `getTotalDomainsByOrganizationReport` | Get total DNSFilter requests per domain broken down by organization. |
| Get Domain Requests By User Report | `getTotalDomainsByUserReport` | Get total DNSFilter requests per domain broken down by end user. |
| Get Domain Stats Report | `getDomainStatsReport` | Get DNSFilter summary statistics for a specific domain or FQDN in an organization. |
| Get Enterprise Connection | `getEnterpriseConnection` | Get a single DNSFilter SSO enterprise connection by id. |
| Get Invoice | `getInvoice` | Get basic information for a single DNSFilter invoice by id. |
| Get IP Address | `getIpAddress` | Get basic information for a single DNSFilter IP address record by id. |
| Get MAC Address | `getMacAddress` | Get basic information for a single DNSFilter MAC address record by id. |
| Get My IP Address | `getMyIpAddress` | Return the public IP address DNSFilter observes for the caller. |
| Get Network | `getNetwork` | Get basic information for a single DNSFilter network by id. |
| Get Network Counts | `getNetworkCounts` | Get counts of DNSFilter networks grouped by protection status. |
| Get Network LAN IP | `getNetworkLanIp` | Get a single LAN IP record behind a DNSFilter network. |
| Get Network Subnet | `getNetworkSubnet` | Get a single subnet of a DNSFilter network. |
| Get Networks CSV Export | `getNetworksCsvExport` | Get the status and download details of a DNSFilter networks CSV export. |
| Get Networks Geo | `getNetworksGeo` | Get the geographic location information for the DNSFilter networks associated with the current user. |
| Get Organization | `getOrganization` | Get basic information for a single DNSFilter organization by id. |
| Get Organization Settings | `getOrganizationSettings` | Get the settings for one or more DNSFilter organizations. |
| Get Organization Stats Report | `getOrganizationStatsReport` | Get DNSFilter summary statistics for an organization over a period. |
| Get Organization Usage | `getOrganizationUsage` | Get DNSFilter usage metrics for an organization over a date range of at most 365 days. |
| Get Organization Usage Detailed | `getOrganizationUsageDetailed` | Get detailed DNSFilter usage metrics for an organization, with user and wifi counts resolved from the data warehouse. |
| Get Organization User | `getOrganizationUser` | Get the details and permissions of a single user within a DNSFilter organization. |
| Get Policy | `getPolicy` | Get basic information for a single DNSFilter policy by id. |
| Get Policy IP | `getPolicyIp` | Get basic information for a single DNSFilter policy IP by id. |
| Get Policy Permissive Mode | `getPolicyPermissiveMode` | Get whether permissive mode is enabled for a DNSFilter policy. |
| Get PSA Integration Redirect Link | `getPsaIntegrationRedirectLink` | Create a DNSFilter PSA integration if one does not exist and return the redirect link used to complete setup. |
| Get Queries Per Second Report | `getQpsReport` | Get the DNSFilter queries-per-second traffic report, bucketed over time and filterable by organization, network, roaming client and request disposition. |
| Get Query Logs | `getQueryLogs` | Get individual DNSFilter DNS query log entries, filterable by domain, category, policy, network, roaming client and disposition. |
| Get Roaming Client | `getUserAgent` | Get a single DNSFilter roaming client by id. |
| Get Roaming Client Bulk Delete | `getUserAgentBulkDelete` | Get the status of a DNSFilter roaming client bulk delete job. |
| Get Roaming Client Bulk Delete Counts | `getUserAgentBulkDeleteCounts` | Preview how many DNSFilter roaming clients a bulk delete filter would match. |
| Get Roaming Client Bulk Update | `getUserAgentBulkUpdate` | Get the status of a DNSFilter roaming client bulk update job. |
| Get Roaming Client Bulk Update Counts | `getUserAgentBulkUpdateCounts` | Preview how many DNSFilter roaming clients a bulk update filter would match. |
| Get Roaming Client Cleanup | `getUserAgentCleanup` | Get a DNSFilter roaming client cleanup rule and its status. |
| Get Roaming Client Counts | `getUserAgentCounts` | Get counts of DNSFilter roaming clients grouped by state. |
| Get Roaming Client CSV Export | `getUserAgentCsvExport` | Get the status and download details of a DNSFilter roaming client CSV export. |
| Get Roaming Client Uninstall PIN | `getUserAgentUninstallPin` | Get the PIN required to uninstall DNSFilter roaming clients in an organization. |
| Get Roaming Clients Report | `getRoamingClientsReport` | Get the count of DNSFilter roaming clients for an organization. |
| Get Scheduled Policy | `getScheduledPolicy` | Get a single DNSFilter scheduled policy by id. |
| Get Scheduled Report | `getScheduledReport` | Get a single DNSFilter scheduled email report by id. |
| Get Scheduled Report Preview | `getScheduledReportPreview` | Get a DNSFilter scheduled report preview and its generation status. |
| Get Threats By Organization Report | `getTotalThreatsByOrganizationReport` | Get total DNSFilter threat requests blocked over time, broken down by organization. |
| Get Threats By User Report | `getTotalThreatsByUserReport` | Get total DNSFilter threat requests blocked over time, broken down by end user. |
| Get Top Agents Report | `getTopAgentsReport` | Get the DNSFilter roaming clients that generated the most DNS traffic in a period. |
| Get Top Application Categories Report | `getTopApplicationCategoriesReport` | Get the DNSFilter application categories with the most requests in a period. |
| Get Top Categories Report | `getTopCategoriesReport` | Get the DNSFilter content categories with the most requests in a period. |
| Get Top Collections Report | `getTopCollectionsReport` | Get the DNSFilter collections that generated the most DNS traffic in a period. |
| Get Top Domains Report | `getTopDomainsReport` | Get the domains with the most DNSFilter DNS requests in a period. |
| Get Top Networks Report | `getTopNetworksReport` | Get the DNSFilter networks that generated the most DNS traffic in a period. |
| Get Top Organizations Requests Report | `getTopOrganizationsRequestsReport` | Get the organizations with the most DNSFilter DNS requests in a period. |
| Get Top Users Report | `getTopUsersReport` | Get the end users that generated the most DNSFilter DNS traffic in a period. |
| Get Total Category Requests Report | `getTotalCategoriesReport` | Get total DNSFilter requests per content category over time. |
| Get Total Domain Requests Report | `getTotalDomainsReport` | Get total DNSFilter requests per domain over time. |
| Get Total Organization Requests Report | `getTotalOrganizationsRequestsReport` | Get total DNSFilter requests for an organization over time. |
| Get Total Requests By Agent Report | `getTotalRequestsByAgentReport` | Get total DNSFilter DNS requests over time broken down by roaming client. |
| Get Total Requests By Collection Report | `getTotalRequestsByCollectionReport` | Get total DNSFilter DNS requests over time broken down by collection. |
| Get Total Requests By Geography Report | `getTotalRequestsGeoReport` | Get total DNSFilter DNS requests broken down by geographic location. |
| Get Total Requests By Organization Report | `getTotalRequestsByOrganizationReport` | Get total DNSFilter DNS requests over time broken down by organization. |
| Get Total Requests By User Report | `getTotalRequestsByUserReport` | Get total DNSFilter DNS requests over time broken down by end user. |
| Get Total Requests Report | `getTotalRequestsReport` | Get total DNSFilter DNS requests over time, bucketed and filterable by every traffic dimension. |
| Get Total Threats Report | `getTotalThreatsReport` | Get total DNSFilter threat requests blocked over time. |
| Get User | `getUser` | Get basic information for a single DNSFilter user by id. |
| Get User UI Settings | `getUserUiSettings` | Get the current DNSFilter user's dashboard UI settings. |
| Link Dashboard | `linkDashboard` | Link a public DNSFilter dashboard so it appears in the current user's dashboard list. |
| List Agent Local Users | `listAgentLocalUsers` | List the extant DNSFilter agent local users, the OS-level user accounts seen by roaming clients. |
| List AI Applications | `listAiApplications` | List the AI applications and websites DNSFilter recognizes. |
| List All Agent Local Users | `listAllAgentLocalUsers` | List all DNSFilter agent local users, including deleted ones. |
| List All Applications | `listAllApplications` | List all DNSFilter applications including deleted ones, optionally filtered by application category. |
| List All Block Pages | `listAllBlockPages` | List all DNSFilter block pages associated with the current user, including deleted ones. |
| List All Categories | `listAllCategories` | List all DNSFilter content categories including internal categories. |
| List All IP Addresses | `listAllIpAddresses` | List all DNSFilter IP addresses associated with the current user, including deleted ones. |
| List All MAC Addresses | `listAllMacAddresses` | List all DNSFilter MAC address records for the current user, including deleted ones. |
| List All MSP Networks | `listAllMspNetworks` | List all DNSFilter networks of an organization managed by the authenticated MSP, including deleted ones. |
| List All Networks | `listAllNetworks` | List all DNSFilter networks associated with the current user, including deleted ones. |
| List All Organizations | `listAllOrganizations` | List all DNSFilter organizations, including cancelled ones, with optional name, type and MSP filters. |
| List All Policies | `listAllPolicies` | List all DNSFilter filtering policies associated with the current user, including deleted ones. |
| List All Roaming Clients | `listAllUserAgents` | List all DNSFilter roaming clients including deleted ones. |
| List All Scheduled Policies | `listAllScheduledPolicies` | List all DNSFilter scheduled policies, including deleted ones. |
| List All Users | `listAllUsers` | List all DNSFilter dashboard users, including deleted ones. |
| List API Keys | `listApiKeys` | Get the list of DNSFilter API keys associated with the current user, optionally filtered by name, id, last four characters, organization or expiry state. |
| List Application Categories | `listApplicationCategories` | List the extant DNSFilter application categories used for application-level filtering. |
| List Applications | `listApplications` | List the extant DNSFilter applications that can be allowed or blocked in a policy, optionally filtered by application category. |
| List Available Dashboards | `listAvailableDashboards` | List every DNSFilter dashboard the current user could link, including public ones owned by others. |
| List Block Pages | `listBlockPages` | List the extant DNSFilter block pages associated with the current user. |
| List Categories | `listCategories` | List the extant DNSFilter content categories that can be allowed or blocked in a policy. |
| List Collection Users | `listCollectionUsers` | List the users belonging to a DNSFilter collection (a directory-synced group of end users). |
| List CyberSight Activity Types | `listCyberSightActivityTypes` | List the CyberSight report activity types available in DNSFilter. |
| List Dashboards | `listDashboards` | List the DNSFilter dashboards available to the current user, default dashboard first. |
| List Distributor Available SKUs | `listDistributorAvailableSkus` | List the DNSFilter product SKUs the authenticated distributor can provision. |
| List Enterprise Connections | `listEnterpriseConnections` | List all SSO enterprise connections configured for the given DNSFilter organization. |
| List Invoices | `listInvoices` | List the DNSFilter invoices for an organization, most recent first. |
| List IP Addresses | `listIpAddresses` | List the extant DNSFilter IP addresses (deployment sites) associated with the current user. |
| List MAC Addresses | `listMacAddresses` | List the extant DNSFilter MAC address records for one or more organizations. |
| List MSP Networks | `listMspNetworks` | List the extant DNSFilter networks of an organization managed by the authenticated MSP. |
| List Network LAN IPs | `listNetworkLanIps` | List the LAN IP addresses seen behind a DNSFilter network. |
| List Network Subnets | `listNetworkSubnets` | List the extant subnets configured on a DNSFilter network. |
| List Networks | `listNetworks` | List the extant DNSFilter networks (sites) associated with the current user. |
| List Organization Users | `listOrganizationUsers` | List the users belonging to a DNSFilter organization. |
| List Organizations | `listOrganizations` | List the DNSFilter organizations visible to the authenticated user, with pagination and search. |
| List Owned Dashboards | `listOwnedDashboards` | List the DNSFilter dashboards owned by the current user. |
| List Policies | `listPolicies` | List the extant DNSFilter filtering policies associated with the current user. |
| List Policy IPs | `listPolicyIps` | List the DNSFilter policy IP records associated with the current user. |
| List Query Protection Methods | `listQpMethods` | List the DNSFilter query protection (QP) methods dictionary. |
| List Relay Releases | `listRelayReleases` | List the available DNSFilter relay software releases. |
| List Roaming Client Releases | `listUserAgentReleases` | List the available DNSFilter roaming client software releases. |
| List Roaming Client Tags | `listUserAgentTags` | List the tags available on DNSFilter roaming clients. |
| List Roaming Clients | `listUserAgents` | List the extant DNSFilter roaming clients (user agents) installed on devices, with filtering by state, network, policy, tags and version. |
| List Scheduled Policies | `listScheduledPolicies` | List the extant DNSFilter scheduled policies, which switch filtering policies on a timetable. |
| List Scheduled Reports | `listScheduledReports` | List the DNSFilter scheduled email reports configured for an organization. |
| List Site Subnets | `listSiteSubnets` | List all DNSFilter site subnets across the networks of an organization. |
| List Users | `listUsers` | List the extant DNSFilter dashboard users visible to the authenticated account. |
| List VPN Settings State Types | `listVpnSettingsStateTypes` | List the VPN settings state types available in DNSFilter. |
| Look Up Domain | `lookupDomain` | Get all DNSFilter domain records and categories associated with a single FQDN. |
| Look Up Network By IP | `lookupNetworkByIp` | Find the DNSFilter network that owns a given public IP address. |
| Make Dashboard Private | `makeDashboardPrivate` | Make a DNSFilter dashboard private, removing access for other users. |
| Make Dashboard Public | `makeDashboardPublic` | Make a DNSFilter dashboard public to other users in the owner's organizations. |
| Promote Organization To MSP | `promoteOrganizationToMsp` | Promote the authenticated user's DNSFilter organization to an MSP on the given plan. |
| Reactivate Distributor MSP | `reactivateDistributorMsp` | Reactivate a cancelled MSP managed by the authenticated DNSFilter distributor. |
| Reactivate Distributor Suborganization | `reactivateDistributorSuborganization` | Reactivate a cancelled sub-organization under the authenticated DNSFilter distributor. |
| Remove Allowed Application From Policy | `removeAllowedApplicationFromPolicy` | Remove a single application from a DNSFilter policy's allow list. |
| Remove Allowed Domain From Policy | `removeAllowedDomainFromPolicy` | Remove a single domain from a DNSFilter policy's allow list. |
| Remove Blocked Application From Policy | `removeBlockedApplicationFromPolicy` | Remove a single application from a DNSFilter policy's block list. |
| Remove Blocked Category From Policy | `removeBlockedCategoryFromPolicy` | Remove a single content category from a DNSFilter policy's block list. |
| Remove Blocked Domain From Policy | `removeBlockedDomainFromPolicy` | Remove a single domain from a DNSFilter policy's block list. |
| Remove Distributor Organization SKU | `removeDistributorOrganizationSku` | Remove a product SKU from a sub-organization under the authenticated DNSFilter distributor. |
| Remove Distributor User Membership | `removeDistributorUserMembership` | Remove a distributor dashboard user's membership of an organization. |
| Remove User From Collection | `removeUserFromCollection` | Remove a user from a DNSFilter collection. |
| Resend Organization User Invite | `resendOrganizationUserInvite` | Resend the DNSFilter invitation email for a user in an organization. This sends a real email. |
| Revoke API Key | `revokeApiKey` | Revoke a DNSFilter API key by id so it can no longer authenticate, without deleting the record. |
| Rotate Network Secret Key | `rotateNetworkSecretKey` | Rotate the secret key of a DNSFilter network, issuing a new key and invalidating the old one. |
| Search Distributor MSPs | `searchDistributorMsps` | Search the MSPs managed by the authenticated DNSFilter distributor. |
| Search Distributor Organizations | `searchDistributorOrganizations` | Search the sub-organizations under the authenticated DNSFilter distributor. |
| Search Distributor Users | `searchDistributorUsers` | Search the dashboard users under the authenticated DNSFilter distributor. |
| Send Distributor User Reset Password Email | `sendDistributorUserResetPasswordEmail` | Send a password reset email to a distributor dashboard user. This sends a real email. |
| Suggest Domain Threat | `suggestDomainThreat` | Submit an FQDN to DNSFilter for threat re-categorization review. Note this files a real report with DNSFilter's threat team. |
| Suppress License Warning | `suppressLicenseWarning` | Suppress the DNSFilter licence warning for the current user and return the suppression date. |
| Unlink Dashboard | `unlinkDashboard` | Unlink a DNSFilter dashboard so it no longer appears in the current user's dashboard list. |
| Update Agent Local User | `updateAgentLocalUser` | Update a DNSFilter agent local user's friendly name or per-user policy overrides. |
| Update Application Policies | `updateApplicationPolicies` | Set which DNSFilter policies allow and which block a given application, in one call. |
| Update Billing Address | `updateBillingAddress` | Update the billing address for the given DNSFilter organization. |
| Update Block Page | `updateBlockPage` | Update an existing DNSFilter block page with the specified data. |
| Update Current User | `updateCurrentUser` | Update the profile attributes (first name, last name, phone) of the currently authenticated DNSFilter user. |
| Update Dashboard | `updateDashboard` | Update a DNSFilter dashboard's name, layout or visibility. |
| Update Distributor | `updateDistributor` | Update the DNSFilter distributor record for the authenticated distributor account. |
| Update Distributor MSP | `updateDistributorMsp` | Update an MSP managed by the authenticated DNSFilter distributor. |
| Update Distributor Suborganization | `updateDistributorSuborganization` | Update a sub-organization under the authenticated DNSFilter distributor. |
| Update Distributor User Membership | `updateDistributorUserMembership` | Change the role a distributor dashboard user holds in an organization. |
| Update Domain Note | `updateDomainNote` | Set the note recorded against a domain on a DNSFilter policy allow or block list. |
| Update Enterprise Connection | `updateEnterpriseConnection` | Update an existing DNSFilter enterprise (SSO) connection by id. Note: the organization's custom login URL is set via the organization's unique_id attribute (PATCH /v1/organizations), not here. |
| Update IP Address | `updateIpAddress` | Update an existing DNSFilter IP address record. |
| Update MAC Address | `updateMacAddress` | Update an existing DNSFilter MAC address record. |
| Update Network | `updateNetwork` | Update a DNSFilter network with the specified attributes. |
| Update Network LAN IP | `updateNetworkLanIp` | Rename a LAN IP record behind a DNSFilter network. |
| Update Network Subnet | `updateNetworkSubnet` | Update a subnet of a DNSFilter network. |
| Update Organization | `updateOrganization` | Update a DNSFilter organization with the specified attributes. |
| Update Organization User | `updateOrganizationUser` | Update a user's profile or permissions within a DNSFilter organization. |
| Update Policy | `updatePolicy` | Update a DNSFilter filtering policy with the specified attributes. |
| Update Policy Permissive Mode | `updatePolicyPermissiveMode` | Turn permissive mode on or off for a DNSFilter policy. |
| Update Roaming Client | `updateUserAgent` | Update a DNSFilter roaming client's name, network, policy, block page or tags. |
| Update Roaming Client Cleanup | `updateUserAgentCleanup` | Update or start a DNSFilter roaming client cleanup rule. |
| Update Roaming Client Settings | `updateUserAgentSettings` | Update both device settings and filtering client settings for a DNSFilter roaming client. |
| Update Scheduled Policy | `updateScheduledPolicy` | Update a DNSFilter scheduled policy. |
| Update Scheduled Report | `updateScheduledReport` | Update a DNSFilter scheduled email report. |
| Update User UI Settings | `updateUserUiSettings` | Update the current DNSFilter user's dashboard UI settings such as theme mode. |
| Upsert Distributor MSP SKUs | `upsertDistributorMspSkus` | Create or update the product SKUs provisioned for an MSP under the authenticated DNSFilter distributor. |
| Verify IP Address | `verifyIpAddress` | Check whether an IP address is already registered in DNSFilter before creating it. The address is sent as the Rails nested query parameter ip_address[address], which the API accepts on this GET route. |
