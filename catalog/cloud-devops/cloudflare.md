---
description: "Cloudflare provides DNS, CDN and edge services. Manage zones, DNS records, page rules, key-value storage and notification policies."
hidden: true
---

# Cloudflare

<img src="../../.gitbook/assets/connectors/lg/cloudflare.png" alt="Cloudflare logo">

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [cloudflare.com](https://cloudflare.com) |
| **Authentication** | Access token |
| **Slug** | `cloudflare` |

## Setup

Your customers enter their access token for Cloudflare when they connect. Nothing else needs setting up.

## Use it

Add Cloudflare from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cloudflare.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Bulk Delete KV Values</td><td><code>bulkDeleteKvValues</code></td><td>Delete multiple keys from a Workers KV namespace in one request Body is a JSON array of key-name strings.</td></tr><tr><td>Bulk Write KV Values</td><td><code>bulkWriteKvValues</code></td><td>Write multiple key/value pairs to a Workers KV namespace in one request Body is a JSON array of {key,value} objects.</td></tr><tr><td>Create DNS Record</td><td><code>createDnsRecord</code></td><td>Create a DNS record</td></tr><tr><td>Create KV Namespace</td><td><code>createKvNamespace</code></td><td>Create a Workers KV namespace</td></tr><tr><td>Create Notification Policy</td><td><code>createNotificationPolicy</code></td><td>Create a notification policy linking an alert type to webhook destinations</td></tr><tr><td>Create Page Rule</td><td><code>createPageRule</code></td><td>Create a page rule</td></tr><tr><td>Create Webhook Destination</td><td><code>createWebhookDestination</code></td><td>Create a notification webhook destination Used by the webhook config.</td></tr><tr><td>Create Zone</td><td><code>createZone</code></td><td>Create a zone</td></tr><tr><td>Delete DNS Record</td><td><code>deleteDnsRecord</code></td><td>Delete a DNS record</td></tr><tr><td>Delete KV Namespace</td><td><code>deleteKvNamespace</code></td><td>Delete a Workers KV namespace</td></tr></tbody></table>

<details>

<summary>View 38 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete KV Value</td><td><code>deleteKvValue</code></td><td>Delete a key from a KV namespace</td></tr><tr><td>Delete Notification Policy</td><td><code>deleteNotificationPolicy</code></td><td>Delete a notification policy</td></tr><tr><td>Delete Page Rule</td><td><code>deletePageRule</code></td><td>Delete a page rule</td></tr><tr><td>Delete Webhook Destination</td><td><code>deleteWebhookDestination</code></td><td>Delete a notification webhook destination</td></tr><tr><td>Delete Worker Script</td><td><code>deleteWorkerScript</code></td><td>Delete a Workers script</td></tr><tr><td>Delete Zone</td><td><code>deleteZone</code></td><td>Delete a zone</td></tr><tr><td>Edit Zone Setting</td><td><code>editZoneSetting</code></td><td>Edit a single zone setting</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Get an account</td></tr><tr><td>Get DNS Record</td><td><code>getDnsRecord</code></td><td>Get a DNS record</td></tr><tr><td>Get KV Namespace</td><td><code>getKvNamespace</code></td><td>Get a single Workers KV namespace by id</td></tr><tr><td>Get Notification Destination Eligibility</td><td><code>getNotificationEligibleDestinations</code></td><td>Get which notification delivery mechanisms are eligible for the account</td></tr><tr><td>Get Notification Policy</td><td><code>getNotificationPolicy</code></td><td>Get a single notification policy by id</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Get the current user details</td></tr><tr><td>Get Webhook Destination</td><td><code>getWebhookDestination</code></td><td>Get a single webhook notification destination by id</td></tr><tr><td>Get Worker Subdomain</td><td><code>getWorkerSubdomain</code></td><td>Get the account's workers.dev subdomain</td></tr><tr><td>Get Zone</td><td><code>getZone</code></td><td>Get a zone</td></tr><tr><td>List Account Members</td><td><code>listAccountMembers</code></td><td>List members of an account</td></tr><tr><td>List Account Roles</td><td><code>listAccountRoles</code></td><td>List all roles available in an account</td></tr><tr><td>List Accounts</td><td><code>listAccounts</code></td><td>List accounts</td></tr><tr><td>List API Tokens</td><td><code>listApiTokens</code></td><td>List account-owned API tokens</td></tr><tr><td>List Available Alerts</td><td><code>listAvailableAlerts</code></td><td>List alert types available for notification policies</td></tr><tr><td>List DNS Records</td><td><code>listDnsRecords</code></td><td>List DNS records for a zone</td></tr><tr><td>List KV Keys</td><td><code>listKvKeys</code></td><td>List keys in a Workers KV namespace</td></tr><tr><td>List KV Namespaces</td><td><code>listKvNamespaces</code></td><td>List Workers KV namespaces</td></tr><tr><td>List Notification Policies</td><td><code>listNotificationPolicies</code></td><td>List notification policies</td></tr><tr><td>List Page Rules</td><td><code>listPageRules</code></td><td>List page rules for a zone</td></tr><tr><td>List Webhook Destinations</td><td><code>listWebhookDestinations</code></td><td>List notification webhook destinations</td></tr><tr><td>List Worker Scripts</td><td><code>listWorkerScripts</code></td><td>List Workers scripts for an account</td></tr><tr><td>List Zone Settings</td><td><code>listZoneSettings</code></td><td>List all settings for a zone</td></tr><tr><td>List Zones</td><td><code>listZones</code></td><td>List zones</td></tr><tr><td>Purge Cache</td><td><code>purgeCache</code></td><td>Purge cached files for a zone Pass purge_everything or files/tags/hosts/prefixes.</td></tr><tr><td>Read KV Value</td><td><code>readKvValue</code></td><td>Read a value by key from a KV namespace Returns the raw value.</td></tr><tr><td>Update DNS Record</td><td><code>updateDnsRecord</code></td><td>Overwrite a DNS record</td></tr><tr><td>Update KV Namespace</td><td><code>updateKvNamespace</code></td><td>Rename a Workers KV namespace</td></tr><tr><td>Update Notification Policy</td><td><code>updateNotificationPolicy</code></td><td>Update a notification policy</td></tr><tr><td>Update Zone</td><td><code>updateZone</code></td><td>Edit zone properties such as paused or plan</td></tr><tr><td>Verify Token</td><td><code>verifyToken</code></td><td>Verify the API token is valid</td></tr><tr><td>Write KV Value</td><td><code>writeKvValue</code></td><td>Write a value for a key in a KV namespace Body is the raw value.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Billing Usage Alert</td><td><code>billing_usage_alert</code></td><td>Usage-based billing threshold reached.</td></tr><tr><td>Certificate Expiration</td><td><code>zone_aop_custom_certificate_expiration_type</code></td><td>A custom certificate is expiring.</td></tr><tr><td>Health Check Status</td><td><code>health_check_status_notification</code></td><td>A health check changed status.</td></tr><tr><td>L4 DoS Attack</td><td><code>dos_attack_l4</code></td><td>Network-layer DDoS attack detected.</td></tr><tr><td>L7 DoS Attack</td><td><code>dos_attack_l7</code></td><td>HTTP DDoS attack detected.</td></tr><tr><td>Universal SSL</td><td><code>universal_ssl_event_type</code></td><td>Universal SSL certificate event.</td></tr><tr><td>Workers Alert</td><td><code>workers_alert</code></td><td>Workers usage/error alert.</td></tr></tbody></table>
