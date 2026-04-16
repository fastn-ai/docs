---
description: >-
  Connectors are used to seamlessly integrate data from various data sources and
  APIs into your created flows.
---

# Connector Types & Setup

## Connectors in Fastn

Connectors in the **Fastn** platform enable you to integrate and interact with external systems such as APIs, databases, or custom logic. They act as bridges that bring external data into your flows or send processed data out.

## Using Connectors

Connectors are components that simplify the process of integrating third-party services. Once added to a flow, they can perform operations like fetching data, transforming it, or saving it to an external system. Each connector includes input and output schemas to ensure data consistency throughout your flow.

## **Types of Connectors**

In **Fastn**, connectors let your flows interact with external apps, APIs, and data sources. They act as bridges between Fastn and the outside world, enabling powerful automations across tools and services.

Fastn supports three main types of connectors:

## **i. Community Connectors**

These are prebuilt, ready-to-use connectors that let you integrate popular apps like **Slack, Google Docs, Notion, Salesforce, HubSpot**, and many more; with **140+ supported apps and counting**.

Community connectors make it easy to connect to tools your team already uses, so you can trigger flows, pull in data, or take actions in those apps without writing any custom code.

### Example: Using a Google Doc and Slack Connector

To create a Google Doc and send it to a specific Slack channel, utilize the **Google Docs Connector** with **Create Doc Endpoint** to generate your document and then use the **Slack Connector** with **Send Message Endpoint** to send it directly to your selected channel. This process requires no coding, streamlining document sharing within your workflows.

<figure><img src="../../../.gitbook/assets/image (243).png" alt="Flow editor with Google Docs Create Doc connector followed by Slack Send Message connector"><figcaption></figcaption></figure>

## ii. Workspace Connectors

Workspace connectors let you create custom connector groups tailored to your project. Each group can contain multiple individual connectors of different types — Function, HTTP API, gRPC, or Database — giving you full control over how your flows interact with external services.

{% hint style="info" %}
You can also use the **Build with AI** button to leverage AI to assist in creating custom connector groups. Provide a description of the service you want to connect to, and Fastn generates the connector group structure for you.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (249).png" alt="Workspace Connectors page with Add Connector button and Build with AI option"><figcaption></figcaption></figure>

### Before you begin

* You have an active Fastn workspace.
* You have the necessary permissions to manage connectors in the workspace.
* If connecting to an external service, you have the service's API credentials or OAuth configuration details ready.

### Step 1: Create a connector group

A connector group acts as a container for related connectors — for example, a "Payment Service" group might hold connectors for creating charges, listing invoices, and issuing refunds.

1. Navigate to **Connectors** in your workspace.
2. Click the **Add Connector** button in the top right corner.
3. Fill in the connector group details:

<figure><img src="../../../.gitbook/assets/image (252).png" alt="Add Connector Group form with fields for name, image URL, description, documentation link, and resource type"><figcaption></figcaption></figure>

| Field                  | Required | Description                                                                                                                                                     |
| ---------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**               | Yes      | A unique name for the connector group (e.g., "Stripe" or "Internal Billing API").                                                                               |
| **Image URL**          | No       | A URL to an icon or logo that visually represents the connector group.                                                                                          |
| **Description**        | No       | A brief summary of the group's purpose and the services it connects to.                                                                                         |
| **Documentation Link** | No       | A link to external documentation for the underlying API or service.                                                                                             |
| **Resource Type**      | Yes      | Select **EXTERNAL** for third-party services or **INTERNAL** for services hosted within your own infrastructure.                                                |
| **Enable Activation**  | No       | Toggle this on to require authentication when connecting. Enabling this reveals [authentication configuration options](setting-up-connector-authentication.md). |

4. Click **Save** to create the group.

{% hint style="info" %}
Enable **Activation** if the service requires credentials. This reveals authentication options including OAuth, Basic Auth, API Key, Bearer Token, and Custom Input. See [Setting up connector authentication](setting-up-connector-authentication.md) for detailed configuration steps.
{% endhint %}

### Step 2: Add individual connectors to the group

After creating a connector group, add individual connectors that represent specific actions or endpoints.

1. Open the connector group you created.
2. Click the **Add** button in the top right corner.
3. Select **Add Custom Action**.
4. Choose one of the four connector types:

<figure><img src="../../../.gitbook/assets/image (247).png" alt="Add Custom Action dialog with connector type options: Function, HTTP API, gRPC, and Database"><figcaption></figcaption></figure>

#### Function connector

Use a Function connector to define custom logic with code. This is ideal for data transformations, calculations, or any operation that does not require an external API call.

1. Enter a name for the connector.
2. Write your function code in the editor.
3. Define the input and output schemas. You can switch between **Form**, **JSON**, and **YAML** views.
4. Use the **Test** section to validate your function with sample input before saving.
5. Click **Create** to add the connector.

{% hint style="info" %}
After creation, you can edit or preview your function from the connectors list in your workspace.
{% endhint %}

#### HTTP API connector

Use an HTTP API connector to integrate with RESTful APIs over standard HTTP/HTTPS.

1. Enter a name for the connector.
2. Provide the **HTTP URL** for the API endpoint.
3. Add JavaScript code to define the request logic — headers, request body, and response handling.
4. Define input and output schemas.
5. Test the API call to verify the response.
6. Click **Create** to add the connector.

<figure><img src="../../../.gitbook/assets/image (476).png" alt="HTTP API Connector setup with URL field and JavaScript code editor for defining API calls"><figcaption></figcaption></figure>

#### gRPC connector

Use a gRPC connector to communicate with services that expose APIs over gRPC instead of HTTP. This is useful for high-performance, low-latency service-to-service communication.

1. Enter a name for the connector.
2. Configure the gRPC service endpoint and method details.
3. Define input and output schemas matching your protobuf definitions.
4. Click **Create** to add the connector.

<figure><img src="../../../.gitbook/assets/image (480).png" alt="gRPC API Connector configuration interface for connecting to gRPC-based services"><figcaption></figcaption></figure>

#### Database connector

Use a Database connector to integrate directly with PostgreSQL, Redshift, or MySQL databases.

1. Enter a name for the connector.
2. Select the database type (**PostgreSQL**, **Redshift**, or **MySQL**).
3. Provide the connection details (host, port, database name, credentials).
4. Define your query or operation.
5. Click **Create** to add the connector.

<figure><img src="../../../.gitbook/assets/image (477).png" alt="Database Connector setup showing options for PostgreSQL, Redshift, and MySQL integration"><figcaption></figcaption></figure>

### Step 3: Configure authentication (optional)

If your connector group has **Enable Activation** turned on, configure the authentication method that matches your external service.

Fastn supports five authentication types:

| Authentication type | Use when                                                                                |
| ------------------- | --------------------------------------------------------------------------------------- |
| **OAuth**           | The service supports an OAuth login screen (e.g., Google, Microsoft, Slack).            |
| **Basic Auth**      | The service requires a username and password.                                           |
| **API Key**         | The service authenticates via an API key in headers or query parameters.                |
| **Bearer Token**    | The service requires a bearer token in the `Authorization` header.                      |
| **Custom Input**    | The service requires custom credential fields (e.g., API key + secret key with expiry). |

For detailed setup instructions for each type, see [Setting up connector authentication](setting-up-connector-authentication.md).

### Step 4: Test and verify

Before using your connector in a flow:

1. Open the connector from the group list.
2. Use the **Test** section (available for Function and HTTP API types) to run the connector with sample input.
3. Verify the output matches your expectations.
4. If the connector requires authentication, confirm that the connection succeeds with valid credentials.

### Step 5: Manage connectors

Once your connector group is set up, you can manage individual connectors and share them across your workspace.

<figure><img src="../../../.gitbook/assets/image (253).png" alt="List of individual connectors within a workspace connector group"><figcaption><p>List of connectors in a connector group</p></figcaption></figure>

**Export and import connectors**

You can export connectors from one workspace and import them into another. You can also download the corresponding **OpenAPI file** for your connector group.

<figure><img src="../../../.gitbook/assets/image (254).png" alt="Connector options menu showing export, import, and download OpenAPI file actions"><figcaption></figcaption></figure>

To access these options, click the menu icon on the connector group and select:

* **Export** — download the connector configuration as a file.
* **Import** — upload a previously exported connector configuration.
* **Download OpenAPI File** — generate and download the OpenAPI specification for the connector group.

### Using workspace connectors in flows

After creating your workspace connectors, use them in flows like any other connector:

1. Open the flow editor and add a connector step.
2. Select **Custom Connector** as the group type.
3. Select your workspace connector group and the specific endpoint.
4. Configure the connection (fixed or dynamic) and fill in the required parameters.

For more details on adding connectors to flows, see [Managing & using connectors](managing-and-using-connectors.md).

## iii. Organization Connectors

These connectors can be defined at the organization level, allowing any member within the organization to access and utilize the connections provided. This allows for streamlined organization and application of connections across various parts of the organization.

<figure><img src="../../../.gitbook/assets/image (242).png" alt="Organization Connectors page showing shared connectors available to all organization members"><figcaption></figcaption></figure>

{% hint style="info" %}
Similar to Workspace connectors, you can define group connectors and then manage different categories of connectors within them.
{% endhint %}
