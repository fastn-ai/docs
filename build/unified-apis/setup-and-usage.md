---
description: Set up a Unified API in fastn, copy its request, authenticate with your admin API key, and run it against your customers' connections.
---

# How to Set Up and Use fastn's Unified API

## 1. Log in to fastn

Go to [app.fastn.dev](https://app.fastn.dev/) and log in to your fastn account.

## 2. Open Unified API

From the dashboard, navigate to **Integrations → Unified API**.

<figure><img src="../../.gitbook/assets/unified-api-setup-integrations.webp" alt="The fastn dashboard on the Connectors page, with arrows pointing to Integrations in the sidebar and to the Unified APIs tab at the top"><figcaption></figcaption></figure>

## 3. Select a Unified API

Choose the Unified API you want to use. For this guide, we'll use **Project Management** as an example.

<figure><img src="../../.gitbook/assets/unified-api-setup-project-management.webp" alt="The Project Management Unified API: the Ticket entity, its providers (Asana, ClickUp, Jira, Linear, Monday.com, Notion, ServiceNow and Trello) with their connection status, and the API section listing GET List, GET Get and POST Create endpoints, each with a Copy curl button"><figcaption></figcaption></figure>

Click **Project Management** to view the available endpoints and their request details.

## 4. Copy the API Request

Navigate to the endpoint you want to use. For example, to create a ticket, select the **POST Ticketing** endpoint.

At the bottom of the endpoint details, click **Copy cURL Request**. Use the copied request as the starting point for your integration.

<figure><img src="../../.gitbook/assets/unified-api-setup-copy-curl.webp" alt="The API section of the Project Management Unified API, with the Copy curl buttons for the List, Get and Create endpoints highlighted"><figcaption></figcaption></figure>

The request will look similar to this:

```bash
curl --location --request POST \
  'https://api.fastn.dev/api/v1/unified/project_management/ticketing' \
  --header 'Authorization: Bearer YOUR_FASTN_ADMIN_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "title": "...",
    "description": "...",
    "due_date": "...",
    "assignee_id": "...",
    "project_id": "...",
    "status": "...",
    "cloud_id": "...",
    "name": "...",
    "priority": "...",
    "ticket_type": "...",
    "collections": "...",
    "tags": [],
    "parent_ticket": "...",
    "creator": "..."
  }'
```

Replace the placeholder values with the appropriate values for your request. The fields required and supported depend on the endpoint and the connected project management application.

## 5. Generate Your fastn Admin API Key

To authenticate your requests, you'll need a **fastn API key**. This key is your admin API Key.

Follow the [fastn API Keys documentation](../../manage/api-keys.md) to create your admin API key.

Replace `YOUR_FASTN_ADMIN_API_KEY` in the cURL request with your actual key.

Keep this key secure. Do not expose it in frontend code or public repositories.

## 6. Make Requests Using Your Customers' Connections

If your SaaS application needs to execute Unified API requests on behalf of your customers, include the `x-org-id` header in the request.

Your **admin API key authenticates your SaaS application with fastn**, while the `x-org-id` header identifies your customer whose connections should be used for the request.

Add the following header:

```bash
--header 'x-org-id: YOUR_CUSTOMER_ORG_ID'
```

Use the **same organization ID discussed in the** [**fastn embedding guide**](../../embed/embedding/README.md). This is the organization ID you already use when setting up the embedded fastn experience.

Make sure the customer has connected and authorized the relevant application in fastn before sending requests that rely on that connection.

## 7. You're Ready to Make API Requests

Once you have your fastn admin API key and have configured the appropriate `x-org-id` header, you can start making requests through fastn's Unified API.

You can follow the same process for other Unified APIs and endpoints, using the cURL request provided in the fastn dashboard as your starting point.
