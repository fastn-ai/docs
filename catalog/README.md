---
description: "1,000+ ready-made connectors for the apps your customers use, by category."
---

# Connector catalog

## What is a connector?

A **connector** is Fastn's ready-made link to one app's API, such as HubSpot, Slack or Stripe. It already knows how to talk to that app, so you don't have to write the integration code yourself. Each connector defines three things:

* **Authentication**: how a customer signs in to the app, for example OAuth 2.0 or an API key.
* **Actions**: what Fastn can do in the app, such as create a contact, send a message or list invoices. Your workflows call actions.
* **Events**: what the app can tell Fastn about, such as a new deal or a paid invoice. Events start your workflows through [triggers](../build/triggers/README.md).

A connector is the definition. When one of your customers signs in to the app through it, that creates a **connection**: their own authorized account. One connector serves all your customers, each with their own connection. See [Core concepts](../getting-started/concepts.md).

## Popular connectors

| Connector | Category | About |
| --- | --- | --- |
| <img src="../.gitbook/assets/connectors/sm/hubspot.png" alt=""> [HubSpot](crm-sales/hubspot.md) | [CRM and sales](crm-sales/README.md) | HubSpot is a CRM platform. Create, update, search and batch-manage contacts, companies, deals, tickets, products and quotes. |
| <img src="../.gitbook/assets/connectors/sm/salesforce.png" alt=""> [Salesforce](crm-sales/salesforce.md) | [CRM and sales](crm-sales/README.md) | Salesforce is a CRM platform. Create, update and query accounts, contacts, leads, opportunities, cases and other records, including in bulk. |
| <img src="../.gitbook/assets/connectors/sm/lead-connector.png" alt=""> [GoHighLevel](crm-sales/gohighlevel.md) | [CRM and sales](crm-sales/README.md) | GoHighLevel is a CRM and marketing platform for agencies. Manage contacts, conversations, opportunities, calendars, campaigns and workflows. |
| <img src="../.gitbook/assets/connectors/sm/keap.png" alt=""> [Keap](crm-sales/keap.md) | [CRM and sales](crm-sales/README.md) | Keap is a CRM and marketing automation platform. Manage contacts, companies, tags, opportunities, orders, products and subscriptions. |
| <img src="../.gitbook/assets/connectors/sm/close.png" alt=""> [Close](crm-sales/close.md) | [CRM and sales](crm-sales/README.md) | Close is a sales CRM. Manage leads, contacts, opportunities, tasks and activities, log calls, and run bulk actions and sequences. |
| <img src="../.gitbook/assets/connectors/sm/salesloft.png" alt=""> [Salesloft](crm-sales/salesloft.md) | [CRM and sales](crm-sales/README.md) | Salesloft is a sales engagement platform. Manage people, accounts, cadences, tasks, calls, emails and bulk jobs. |
| <img src="../.gitbook/assets/connectors/sm/shopify.png" alt=""> [Shopify](ecommerce/shopify.md) | [E-commerce](ecommerce/README.md) | Shopify is an e-commerce platform for online stores. Manage orders, products, customers, inventory, returns and billing charges. |
| <img src="../.gitbook/assets/connectors/sm/cin7core.png" alt=""> [Cin7 Core](ecommerce/cin7core.md) | [E-commerce](ecommerce/README.md) | Cin7 Core manages inventory, sales, purchasing and production. Create purchases, sales, production orders and accounting records. |
| <img src="../.gitbook/assets/connectors/sm/bigcommerce.png" alt=""> [BigCommerce](ecommerce/bigcommerce.md) | [E-commerce](ecommerce/README.md) | BigCommerce is an online store platform. Manage products, categories, orders, customers, carts, checkouts and themes. |
| <img src="../.gitbook/assets/connectors/sm/woocommerce.png" alt=""> [WooCommerce](ecommerce/woocommerce.md) | [E-commerce](ecommerce/README.md) | WooCommerce is an online store plugin for WordPress. Manage products, orders, customers, coupons, reviews and shipping zones. |
| <img src="../.gitbook/assets/connectors/sm/wix.png" alt=""> [Wix](ecommerce/wix.md) | [E-commerce](ecommerce/README.md) | Wix is a website builder with online stores. Manage products, categories, carts, orders, contacts, members and bookings. |
| <img src="../.gitbook/assets/connectors/sm/walmart-marketplace.png" alt=""> [Walmart Marketplace](ecommerce/walmart-marketplace.md) | [E-commerce](ecommerce/README.md) | Walmart Marketplace lets sellers sell on Walmart.com in the US. Manage orders, items, prices, inventory, returns and repricing. |
| <img src="../.gitbook/assets/connectors/sm/zendesk-support.png" alt=""> [Zendesk Support](it-service/zendesk-support.md) | [IT and service management](it-service/README.md) | Zendesk Support is a customer service and ticketing platform. Manage tickets, tags, macros, users, organizations and automations. |
| <img src="../.gitbook/assets/connectors/sm/servicenow.png" alt=""> [ServiceNow](it-service/servicenow.md) | [IT and service management](it-service/README.md) | ServiceNow is an IT service management platform. Create and manage incidents, change requests, assets, events and business rules. |
| <img src="../.gitbook/assets/connectors/sm/jira.png" alt=""> [Jira](project-management/jira.md) | [Project management](project-management/README.md) | Jira is an issue and project tracking tool. Manage issues, comments, attachments, project roles, dashboards, fields and issue types. |
| <img src="../.gitbook/assets/connectors/sm/intercom.png" alt=""> [Intercom](it-service/intercom.md) | [IT and service management](it-service/README.md) | Intercom is a customer messaging and support platform. Manage contacts, companies, conversations, tickets and help center articles. |
| <img src="../.gitbook/assets/connectors/sm/freshservice.png" alt=""> [Freshservice](it-service/freshservice.md) | [IT and service management](it-service/README.md) | Freshservice is an IT service management platform. Manage tickets, changes, assets, service catalog items, projects and alerts. |

## Browse by category

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><strong>AI and ML</strong></td><td>OpenAI, Anthropic (Claude), ChatBotKit</td><td><a href="ai-ml/README.md">ai-ml/README.md</a></td></tr>
<tr><td><strong>Developer tools</strong></td><td>GitHub, GitLab, LaunchDarkly</td><td><a href="developer-tools/README.md">developer-tools/README.md</a></td></tr>
<tr><td><strong>Search and web</strong></td><td>Apify, SearchApi, Explorium</td><td><a href="search-web/README.md">search-web/README.md</a></td></tr>
<tr><td><strong>Data and databases</strong></td><td>Snowflake, Appwrite, Databricks</td><td><a href="data-database/README.md">data-database/README.md</a></td></tr>
<tr><td><strong>Cloud and DevOps</strong></td><td>AWS S3, Confluent Cloud, Terraform Cloud</td><td><a href="cloud-devops/README.md">cloud-devops/README.md</a></td></tr>
<tr><td><strong>CRM and sales</strong></td><td>HubSpot, Salesforce, Pipeliner CRM (Coevera)</td><td><a href="crm-sales/README.md">crm-sales/README.md</a></td></tr>
<tr><td><strong>Marketing</strong></td><td>Mailchimp, DataForSEO, Sequenzy</td><td><a href="marketing/README.md">marketing/README.md</a></td></tr>
<tr><td><strong>Finance and payments</strong></td><td>Stripe, Xero, Odoo</td><td><a href="finance-payments/README.md">finance-payments/README.md</a></td></tr>
<tr><td><strong>E-commerce</strong></td><td>Cin7 Core, Shopify, Walmart Marketplace</td><td><a href="ecommerce/README.md">ecommerce/README.md</a></td></tr>
<tr><td><strong>Communication</strong></td><td>Google Gmail, Slack, Microsoft Teams</td><td><a href="communication/README.md">communication/README.md</a></td></tr>
<tr><td><strong>Social media</strong></td><td>ContentStudio, Pinterest, Mastodon</td><td><a href="social-media/README.md">social-media/README.md</a></td></tr>
<tr><td><strong>Productivity</strong></td><td>Google Sheets, Google Calendar, Google Drive</td><td><a href="productivity/README.md">productivity/README.md</a></td></tr>
<tr><td><strong>Project management</strong></td><td>Jira, Asana, Rentman</td><td><a href="project-management/README.md">project-management/README.md</a></td></tr>
<tr><td><strong>Docs and knowledge</strong></td><td>Notion, Confluence, WordPress.com</td><td><a href="docs-knowledge/README.md">docs-knowledge/README.md</a></td></tr>
<tr><td><strong>Analytics and monitoring</strong></td><td>Datadog, Kibana, Dynatrace (API token)</td><td><a href="analytics-monitoring/README.md">analytics-monitoring/README.md</a></td></tr>
<tr><td><strong>Security</strong></td><td>DNSFilter, Didit, NextDNS</td><td><a href="security/README.md">security/README.md</a></td></tr>
<tr><td><strong>IT and service management</strong></td><td>Jira, Zendesk Support, Intercom</td><td><a href="it-service/README.md">it-service/README.md</a></td></tr>
<tr><td><strong>Design</strong></td><td>Figma, Miro, Mural</td><td><a href="design/README.md">design/README.md</a></td></tr>
<tr><td><strong>Maps and location</strong></td><td>TomTom, AccuWeather, Felt</td><td><a href="maps-location/README.md">maps-location/README.md</a></td></tr>
<tr><td><strong>Entertainment and media</strong></td><td>Vimeo, College Football Data, Lichess</td><td><a href="entertainment-media/README.md">entertainment-media/README.md</a></td></tr>
<tr><td><strong>Sample and novelty APIs</strong></td><td>The Dog API, PokeAPI, The Cat API</td><td><a href="sample/README.md">sample/README.md</a></td></tr>
<tr><td><strong>Other</strong></td><td>Bonusly, Digital Humani, WaniKani</td><td><a href="other/README.md">other/README.md</a></td></tr>
</tbody></table>

## Can't find one?

Missing a connector or an action? Create it yourself by following [Create a connector](create-a-connector.md), or describe it to the Fastn agent or your AI tool and let it build the connector for you.

