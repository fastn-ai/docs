---
description: "1,000+ ready-made connectors for the apps your customers use, by category."
---

# Connector catalog

fastn manages 1,000+ ready-made connectors, and the list grows every week.

## What is a connector?

A **connector** is fastn's ready-made link to one app's API, such as HubSpot, Slack or Stripe. It already knows how to talk to that app, so you don't have to write the integration code yourself. Each connector defines three things:

* **Authentication**: how a customer signs in to the app, for example OAuth 2.0 or an API key.
* **Actions**: what fastn can do in the app, such as create a contact, send a message or list invoices. Your workflows call actions.
* **Events**: what the app can tell fastn about, such as a new deal or a paid invoice. Events start your workflows through [triggers](../build/triggers/README.md).

A connector is the definition. When one of your customers signs in to the app through it, that creates a **connection**: their own authorized account. One connector serves all your customers, each with their own connection. See [Core concepts](../getting-started/concepts.md).

## Popular connectors

| | Connector | Category | About |
| --- | --- | --- | --- |
| <img src="../.gitbook/assets/connectors/sm/hubspot.png" alt=""> | [HubSpot](crm-sales/hubspot.md) | [CRM and sales](crm-sales/README.md) | HubSpot CRM connector — full CRUD, search and batch operations across contacts, companies, deals, tickets,… |
| <img src="../.gitbook/assets/connectors/sm/salesforce.png" alt=""> | [Salesforce](crm-sales/salesforce.md) | [CRM and sales](crm-sales/README.md) | Salesforce CRM connector for managing Accounts, Contacts, Leads, Opportunities, Cases, and Tasks via the… |
| <img src="../.gitbook/assets/connectors/sm/lead-connector.png" alt=""> | [GoHighLevel](crm-sales/lead-connector.md) | [CRM and sales](crm-sales/README.md) | GoHighLevel (HighLevel) is an all-in-one CRM, marketing-automation and agency platform. |
| <img src="../.gitbook/assets/connectors/sm/keap.png" alt=""> | [Keap](crm-sales/keap.md) | [CRM and sales](crm-sales/README.md) | Keap (formerly Infusionsoft) CRM, sales, and marketing automation platform. |
| <img src="../.gitbook/assets/connectors/sm/close.png" alt=""> | [Close](crm-sales/close.md) | [CRM and sales](crm-sales/README.md) | Close CRM connector. |
| <img src="../.gitbook/assets/connectors/sm/salesloft.png" alt=""> | [Salesloft](crm-sales/salesloft.md) | [CRM and sales](crm-sales/README.md) | Salesloft Revenue Orchestration Platform (sales engagement). |
| <img src="../.gitbook/assets/connectors/sm/shopify.png" alt=""> | [Shopify](ecommerce/shopify.md) | [E-commerce](ecommerce/README.md) | Shopify Admin REST API connector for managing orders, products, customers, inventory, discounts, shipping,… |
| <img src="../.gitbook/assets/connectors/sm/cin7core.png" alt=""> | [Cin7 Core](ecommerce/cin7core.md) | [E-commerce](ecommerce/README.md) | Cin7 Core (formerly DEAR Inventory) — cloud inventory, sales, purchasing, production and accounting… |
| <img src="../.gitbook/assets/connectors/sm/bigcommerce.png" alt=""> | [BigCommerce](ecommerce/bigcommerce.md) | [E-commerce](ecommerce/README.md) | BigCommerce REST Management API — Catalog (products, categories, brands, variants, images, modifiers),… |
| <img src="../.gitbook/assets/connectors/sm/woocommerce.png" alt=""> | [WooCommerce](ecommerce/woocommerce.md) | [E-commerce](ecommerce/README.md) | WooCommerce is the open-source e-commerce plugin for WordPress. |
| <img src="../.gitbook/assets/connectors/sm/wix.png" alt=""> | [Wix](ecommerce/wix.md) | [E-commerce](ecommerce/README.md) | Wix REST API connector (www.wixapis.com). |
| <img src="../.gitbook/assets/connectors/sm/walmart-marketplace.png" alt=""> | [Walmart Marketplace](ecommerce/walmart-marketplace.md) | [E-commerce](ecommerce/README.md) | Walmart Marketplace (US) Seller API — environment-switchable (production or sandbox). |
| <img src="../.gitbook/assets/connectors/sm/zendesk-support.png" alt=""> | [Zendesk Support](it-service/zendesk-support.md) | [IT and service management](it-service/README.md) | Zendesk Support customer service and ticketing platform. |
| <img src="../.gitbook/assets/connectors/sm/servicenow.png" alt=""> | [ServiceNow](it-service/servicenow.md) | [IT and service management](it-service/README.md) | ServiceNow ITSM platform connector. |
| <img src="../.gitbook/assets/connectors/sm/intercom.png" alt=""> | [Intercom](it-service/intercom.md) | [IT and service management](it-service/README.md) | Intercom customer messaging and support platform. |
| <img src="../.gitbook/assets/connectors/sm/freshservice.png" alt=""> | [Freshservice](it-service/freshservice.md) | [IT and service management](it-service/README.md) | Freshservice IT service management — tickets, problems, changes, releases, assets, service catalog,… |

## Browse by category

Every other connector is in its category, the most used first. Your workspace may also have connectors of your own, which are not listed here.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><strong>AI and ML</strong></td><td>OpenAI, Anthropic (Claude), ChatBotKit</td><td><a href="ai-ml/README.md">ai-ml/README.md</a></td></tr>
<tr><td><strong>Developer tools</strong></td><td>GitHub, GitLab, Appwrite</td><td><a href="developer-tools/README.md">developer-tools/README.md</a></td></tr>
<tr><td><strong>Search and web</strong></td><td>Didit, Apify, SearchApi</td><td><a href="search-web/README.md">search-web/README.md</a></td></tr>
<tr><td><strong>Data and databases</strong></td><td>Snowflake, Databricks, Confluent Cloud</td><td><a href="data-database/README.md">data-database/README.md</a></td></tr>
<tr><td><strong>Cloud and DevOps</strong></td><td>AWS S3, DNSFilter, Terraform Cloud</td><td><a href="cloud-devops/README.md">cloud-devops/README.md</a></td></tr>
<tr><td><strong>CRM and sales</strong></td><td>HubSpot, Salesforce, Pipeliner CRM (Coevera)</td><td><a href="crm-sales/README.md">crm-sales/README.md</a></td></tr>
<tr><td><strong>Marketing</strong></td><td>Mailchimp, DataForSEO, Sequenzy</td><td><a href="marketing/README.md">marketing/README.md</a></td></tr>
<tr><td><strong>Finance and payments</strong></td><td>Stripe, Xero, Moneybird</td><td><a href="finance-payments/README.md">finance-payments/README.md</a></td></tr>
<tr><td><strong>E-commerce</strong></td><td>Cin7 Core, Shopify, Walmart Marketplace</td><td><a href="ecommerce/README.md">ecommerce/README.md</a></td></tr>
<tr><td><strong>Communication</strong></td><td>Slack, Microsoft Teams, Microsoft Outlook Mail</td><td><a href="communication/README.md">communication/README.md</a></td></tr>
<tr><td><strong>Social media</strong></td><td>ContentStudio, Pinterest, Mastodon</td><td><a href="social-media/README.md">social-media/README.md</a></td></tr>
<tr><td><strong>Productivity</strong></td><td>Google Sheets, Google Calendar, Google Drive</td><td><a href="productivity/README.md">productivity/README.md</a></td></tr>
<tr><td><strong>Project management</strong></td><td>Jira, Asana, Rentman</td><td><a href="project-management/README.md">project-management/README.md</a></td></tr>
<tr><td><strong>Docs and knowledge</strong></td><td>Notion, Confluence, WordPress.com</td><td><a href="docs-knowledge/README.md">docs-knowledge/README.md</a></td></tr>
<tr><td><strong>Analytics and monitoring</strong></td><td>Datadog, Kibana, Dynatrace</td><td><a href="analytics-monitoring/README.md">analytics-monitoring/README.md</a></td></tr>
<tr><td><strong>IT and service management</strong></td><td>Zendesk Support, Intercom, ServiceNow</td><td><a href="it-service/README.md">it-service/README.md</a></td></tr>
<tr><td><strong>Design</strong></td><td>Figma, Miro, Mural</td><td><a href="design/README.md">design/README.md</a></td></tr>
<tr><td><strong>Maps and location</strong></td><td>TomTom, AccuWeather, Felt</td><td><a href="maps-location/README.md">maps-location/README.md</a></td></tr>
<tr><td><strong>Entertainment and media</strong></td><td>Sanity, Contentful, Vimeo</td><td><a href="entertainment-media/README.md">entertainment-media/README.md</a></td></tr>
<tr><td><strong>Other</strong></td><td>Google Gmail, Odoo, ManageEngine ServiceDesk Plus</td><td><a href="other/README.md">other/README.md</a></td></tr>
</tbody></table>

## Can't find one?

Search the docs with **Ctrl+K** (**Cmd+K** on a Mac). Missing a connector or an action? Describe it to **Build with AI**, which can create it for you: see [Create a connector](../build/connectors/creating-a-connector.md).

