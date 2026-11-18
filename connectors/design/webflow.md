---
description: "Webflow Data API v2 connector — manage sites, CMS collections and items, pages, forms, assets, custom code, and site configuration via OAuth 2.0."
---

# Webflow

Webflow Data API v2 connector — manage sites, CMS collections and items, pages, forms, assets, custom code, and site configuration via OAuth 2.0.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [webflow.com](https://webflow.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 3 |
| **Events** | 0 |
| **Slug** | `webflow` |

## Use it

Add Webflow from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.webflow.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Authorized User | `getAuthorizedUser` | Retrieves the Webflow user who authorized the current access token. Useful for identifying the connected account. Requires the authorized_user:read scope. |
| Introspect Token | `introspectToken` | Retrieves information about the current authorization, including the granted scopes, rate limit, and the sites, workspaces, and users the token is authorized to access, along with details of the Webflow application. |
| List Sites | `listSites` | Lists all Webflow sites the authorized token has access to. Returns an empty list when the token is not authorized to any site. Requires the sites:read scope. |
