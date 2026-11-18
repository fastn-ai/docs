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
| <img src="../.gitbook/assets/connectors/google-gmail.png" alt="" width="32"> | [Google Gmail](other/google-gmail.md) | [Other](other/README.md) | Google Gmail API connector for managing emails, drafts, labels, threads, history, attachments, settings, and… |
| <img src="../.gitbook/assets/connectors/slack.png" alt="" width="32"> | [Slack](communication/slack.md) | [Communication](communication/README.md) | Connect to Slack to send messages, manage channels, interact with users, and automate workflows directly in… |
| <img src="../.gitbook/assets/connectors/hubspot.png" alt="" width="32"> | [HubSpot](crm-sales/hubspot.md) | [CRM and sales](crm-sales/README.md) | HubSpot CRM connector — full CRUD, search and batch operations across contacts, companies, deals, tickets,… |
| <img src="../.gitbook/assets/connectors/salesforce.png" alt="" width="32"> | [Salesforce](crm-sales/salesforce.md) | [CRM and sales](crm-sales/README.md) | Salesforce CRM connector for managing Accounts, Contacts, Leads, Opportunities, Cases, and Tasks via the… |
| <img src="../.gitbook/assets/connectors/cin7core.jpg" alt="" width="32"> | [Cin7 Core](ecommerce/cin7core.md) | [E-commerce](ecommerce/README.md) | Cin7 Core (formerly DEAR Inventory) — cloud inventory, sales, purchasing, production and accounting… |
| <img src="../.gitbook/assets/connectors/google-sheets.png" alt="" width="32"> | [Google Sheets](productivity/google-sheets.md) | [Productivity](productivity/README.md) | Read, write, and manage Google Sheets spreadsheets via the Sheets API v4. |
| <img src="../.gitbook/assets/connectors/shopify.png" alt="" width="32"> | [Shopify](ecommerce/shopify.md) | [E-commerce](ecommerce/README.md) | Shopify Admin REST API connector for managing orders, products, customers, inventory, discounts, shipping,… |
| <img src="../.gitbook/assets/connectors/stripe.png" alt="" width="32"> | [Stripe](finance-payments/stripe.md) | [Finance and payments](finance-payments/README.md) | Stripe API (base https://api.stripe.com). |
| <img src="../.gitbook/assets/connectors/notion.ico" alt="" width="32"> | [Notion](docs-knowledge/notion.md) | [Docs and knowledge](docs-knowledge/README.md) | Notion REST API connector for managing pages, databases, blocks, users, comments, and search across a Notion… |
| <img src="../.gitbook/assets/connectors/jira.png" alt="" width="32"> | [Jira](project-management/jira.md) | [Project management](project-management/README.md) | Atlassian Jira Cloud connector — Issues (CRUD, JQL search, transitions, bulk ops, comments, worklogs,… |
| <img src="../.gitbook/assets/connectors/zendesk-support.png" alt="" width="32"> | [Zendesk Support](it-service/zendesk-support.md) | [IT and service management](it-service/README.md) | Zendesk Support customer service and ticketing platform. |
| <img src="../.gitbook/assets/connectors/microsoft-teams.png" alt="" width="32"> | [Microsoft Teams](communication/microsoft-teams.md) | [Communication](communication/README.md) | Microsoft Teams via Microsoft Graph API v1.0 — manage teams, channels, channel messages, replies, chats,… |
| <img src="../.gitbook/assets/connectors/xero.png" alt="" width="32"> | [Xero](finance-payments/xero.md) | [Finance and payments](finance-payments/README.md) | Xero Accounting API connector. |
| <img src="../.gitbook/assets/connectors/openai.png" alt="" width="32"> | [OpenAI](ai-ml/openai.md) | [AI and ML](ai-ml/README.md) | OpenAI API connector — chat completions, responses, embeddings, models, files, images, audio, moderations,… |
| <img src="../.gitbook/assets/connectors/google-calendar.svg" alt="" width="32"> | [Google Calendar](productivity/google-calendar.md) | [Productivity](productivity/README.md) | Google Calendar API v3 connector — manage calendars, events, ACLs, free/busy queries, and push notification… |
| <img src="../.gitbook/assets/connectors/microsoft-outlook-mail.svg" alt="" width="32"> | [Microsoft Outlook Mail](communication/microsoft-outlook-mail.md) | [Communication](communication/README.md) | Microsoft Outlook Mail via Microsoft Graph v1.0 (https://graph.microsoft.com/v1.0). |

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

