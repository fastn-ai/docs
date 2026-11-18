---
description: "Cloutly is a customer review and online reputation management platform."
hidden: true
---

# Cloutly

<img src="../../.gitbook/assets/connectors/lg/cloutly.png" alt="Cloutly logo">

Cloutly is a customer review and online reputation management platform. This connector wraps the Cloutly public REST API (https://app.cloutly.com/api/v1 and /api/v2) to list the businesses/locations connected to a Cloutly account, pull reviews aggregated from Google, Facebook, Trustpilot and other sources, check API health and key scopes, and send review invites to customers. Authenticated with a long-lived API key sent in the x-api-key header.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [cloutly.com](https://cloutly.com) |
| **Authentication** | API key |
| **Slug** | `cloutly` |

## Use it

Add Cloutly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cloutly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check API Health | `checkApiHealth` | Health check for the Cloutly REST API v1. Sends GET /api/v1/ping with your API key and returns the plain-text body "OK" when the key authenticates and the API is reachable. Use this to verify a newly created Cloutly connection before running any other action. Takes no input. |
| Get API Key Scopes | `getApiKeyScopes` | Returns the API versions your Cloutly API key is entitled to, e.g. {"scopes":["v1","v2"]}. This is the v2 health endpoint (GET /api/v2/ping) and doubles as a scope-introspection call: if "v2" is absent from the list, the v2 endpoints of this connector will be refused. Takes no input. |
| List Businesses | `listBusinesses` | Lists every business (location) connected to your Cloutly account, with its connected review sources, aggregate star rating and total review count. Use this first to obtain the businessId required by List Reviews and Send Review Invite. Returns a JSON array under "items"; an empty array means no business has been connected in the Cloutly console yet. Takes no input. |
| List Businesses (API v2) | `listBusinessesV2` | Lists the businesses connected to your Cloutly account using the v2 API surface (GET /api/v2/businesses). Requires the "v2" scope on your API key - check it with Get API Key Scopes. Returns the same business records as List Businesses under "items"; kept as a separate action because v2 may add fields that v1 does not return. Takes no input. |
| List Reviews | `listReviews` | Lists reviews aggregated by Cloutly from every connected source (Google, Facebook, Trustpilot and others), newest first by default. Supports filtering by source, by business and by widget visibility, plus limit/offset paging and sort direction. Returns the total match count and the review records, including author, rating, text, status, the business reply if any, and whether the review can still be replied to. PRIVACY: review records contain reviewer names, email addresses and phone numbers - real end-customer personal data. |
| Send Review Invite | `sendReviewInvite` | Creates a contact in a Cloutly business campaign and sends that person a review invite. WARNING - THIS CONTACTS A REAL CUSTOMER AND CONSUMES ACCOUNT CREDIT: the invite is delivered by email and/or SMS, immediately when inviteDelayDays is omitted. Supply at least one of email or phoneNumber. businessId comes from List Businesses; campaignId is optional and falls back to the business default campaign. Returns the created contact and the account's remaining SMS allowance. |
