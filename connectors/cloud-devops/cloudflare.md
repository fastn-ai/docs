---
description: "Cloudflare API v4 (base https://api.cloudflare.com/client/v4)."
hidden: true
---

# Cloudflare

Cloudflare API v4 (base https://api.cloudflare.com/client/v4). Manage accounts, zones (CRUD + cache purge + settings), DNS records, page rules, Workers scripts, Workers KV namespaces and values, and notification webhook destinations/policies. Auth: Bearer API token. Responses use the standard {success, errors, messages, result, result_info} envelope.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [cloudflare.com](https://cloudflare.com) |
| **Authentication** | Bearer token |
| **Actions** | 48 |
| **Events** | 7 |
| **Slug** | `cloudflare` |

## Use it

Add Cloudflare from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cloudflare.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Delete KV Values | `bulkDeleteKvValues` | Delete multiple keys from a Workers KV namespace in one request (DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk). Body is a JSON array of key-name strings. |
| Bulk Write KV Values | `bulkWriteKvValues` | Write multiple key/value pairs to a Workers KV namespace in one request (PUT /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk). Body is a JSON array of {key,value} objects. |
| Create DNS Record | `createDnsRecord` | Create a DNS record (POST /zones/{zone_id}/dns_records). |
| Create KV Namespace | `createKvNamespace` | Create a Workers KV namespace (POST /accounts/{account_id}/storage/kv/namespaces). |
| Create Notification Policy | `createNotificationPolicy` | Create a notification policy linking an alert type to webhook destinations (POST /accounts/{account_id}/alerting/v3/policies). |
| Create Page Rule | `createPageRule` | Create a page rule (POST /zones/{zone_id}/pagerules). |
| Create Webhook Destination | `createWebhookDestination` | Create a notification webhook destination (POST /accounts/{account_id}/alerting/v3/destinations/webhooks). Used by the webhook config. |
| Create Zone | `createZone` | Create a zone (POST /zones). |
| Delete DNS Record | `deleteDnsRecord` | Delete a DNS record (DELETE /zones/{zone_id}/dns_records/{id}). |
| Delete KV Namespace | `deleteKvNamespace` | Delete a Workers KV namespace (DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}). |
| Delete KV Value | `deleteKvValue` | Delete a key from a KV namespace (DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}). |
| Delete Notification Policy | `deleteNotificationPolicy` | Delete a notification policy (DELETE /accounts/{account_id}/alerting/v3/policies/{policy_id}). |
| Delete Page Rule | `deletePageRule` | Delete a page rule (DELETE /zones/{zone_id}/pagerules/{id}). |
| Delete Webhook Destination | `deleteWebhookDestination` | Delete a notification webhook destination (DELETE /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhookId}). |
| Delete Worker Script | `deleteWorkerScript` | Delete a Workers script (DELETE /accounts/{account_id}/workers/scripts/{script_name}). |
| Delete Zone | `deleteZone` | Delete a zone (DELETE /zones/{zone_id}). |
| Edit Zone Setting | `editZoneSetting` | Edit a single zone setting (PATCH /zones/{zone_id}/settings/{setting_id}). |
| Get Account | `getAccount` | Get an account (GET /accounts/{account_id}). |
| Get DNS Record | `getDnsRecord` | Get a DNS record (GET /zones/{zone_id}/dns_records/{id}). |
| Get KV Namespace | `getKvNamespace` | Get a single Workers KV namespace by id (GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}). |
| Get Notification Destination Eligibility | `getNotificationEligibleDestinations` | Get which notification delivery mechanisms are eligible for the account (GET /accounts/{account_id}/alerting/v3/destinations/eligible). |
| Get Notification Policy | `getNotificationPolicy` | Get a single notification policy by id (GET /accounts/{account_id}/alerting/v3/policies/{policy_id}). |
| Get User | `getUser` | Get the current user details (GET /user). |
| Get Webhook Destination | `getWebhookDestination` | Get a single webhook notification destination by id (GET /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}). |
| Get Worker Subdomain | `getWorkerSubdomain` | Get the account's workers.dev subdomain (GET /accounts/{account_id}/workers/subdomain). |
| Get Zone | `getZone` | Get a zone (GET /zones/{zone_id}). |
| List Account Members | `listAccountMembers` | List members of an account (GET /accounts/{account_id}/members). |
| List Account Roles | `listAccountRoles` | List all roles available in an account (GET /accounts/{account_id}/roles). |
| List Accounts | `listAccounts` | List accounts (GET /accounts). |
| List API Tokens | `listApiTokens` | List account-owned API tokens (GET /accounts/{account_id}/tokens). |
| List Available Alerts | `listAvailableAlerts` | List alert types available for notification policies (GET /accounts/{account_id}/alerting/v3/available_alerts). |
| List DNS Records | `listDnsRecords` | List DNS records for a zone (GET /zones/{zone_id}/dns_records). |
| List KV Keys | `listKvKeys` | List keys in a Workers KV namespace (GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys). |
| List KV Namespaces | `listKvNamespaces` | List Workers KV namespaces (GET /accounts/{account_id}/storage/kv/namespaces). |
| List Notification Policies | `listNotificationPolicies` | List notification policies (GET /accounts/{account_id}/alerting/v3/policies). |
| List Page Rules | `listPageRules` | List page rules for a zone (GET /zones/{zone_id}/pagerules). |
| List Webhook Destinations | `listWebhookDestinations` | List notification webhook destinations (GET /accounts/{account_id}/alerting/v3/destinations/webhooks). |
| List Worker Scripts | `listWorkerScripts` | List Workers scripts for an account (GET /accounts/{account_id}/workers/scripts). |
| List Zone Settings | `listZoneSettings` | List all settings for a zone (GET /zones/{zone_id}/settings). |
| List Zones | `listZones` | List zones (GET /zones). |
| Purge Cache | `purgeCache` | Purge cached files for a zone (POST /zones/{zone_id}/purge_cache). Pass purge_everything or files/tags/hosts/prefixes. |
| Read KV Value | `readKvValue` | Read a value by key from a KV namespace (GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}). Returns the raw value. |
| Update DNS Record | `updateDnsRecord` | Overwrite a DNS record (PUT /zones/{zone_id}/dns_records/{id}). |
| Update KV Namespace | `updateKvNamespace` | Rename a Workers KV namespace (PUT /accounts/{account_id}/storage/kv/namespaces/{namespace_id}). |
| Update Notification Policy | `updateNotificationPolicy` | Update a notification policy (PUT /accounts/{account_id}/alerting/v3/policies/{policy_id}). |
| Update Zone | `updateZone` | Edit zone properties such as paused or plan (PATCH /zones/{zone_id}). |
| Verify Token | `verifyToken` | Verify the API token is valid (GET /user/tokens/verify). |
| Write KV Value | `writeKvValue` | Write a value for a key in a KV namespace (PUT /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}). Body is the raw value. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Billing Usage Alert | `billing_usage_alert` | Usage-based billing threshold reached. |
| Certificate Expiration | `zone_aop_custom_certificate_expiration_type` | A custom certificate is expiring. |
| Health Check Status | `health_check_status_notification` | A health check changed status. |
| L4 DoS Attack | `dos_attack_l4` | Network-layer DDoS attack detected. |
| L7 DoS Attack | `dos_attack_l7` | HTTP DDoS attack detected. |
| Universal SSL | `universal_ssl_event_type` | Universal SSL certificate event. |
| Workers Alert | `workers_alert` | Workers usage/error alert. |
