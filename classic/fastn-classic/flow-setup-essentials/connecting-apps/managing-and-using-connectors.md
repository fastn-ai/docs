---
description: >-
  Learn to integrate external apps as Connectors in your Flows or make new
  Custom Connectors.
---

# Managing & Using Connectors

## Using Fastn Connectors in Flows​

You can add Connectors in your **Flows** at any required step from the right navigation bar under **Flow Connection:**

<figure><img src="../../../../.gitbook/assets/image (244).png" alt="Flow editor right sidebar showing Flow Connection panel for adding connectors to a flow step"><figcaption></figcaption></figure>

### Example: Adding a Slack Connector to Send Message to a Channel

After adding the connector as a flow component:

* Select the **Group Type** of connectors, the **Connector** i.e, Slack, and corresponding **Endpoint**. Click on **Next** to proceed.
* In the **Connect** section, login to Slack (your Connector app) using a fixed connection or allow multiple users to create connections dynamically via Widgets.
* Move to the **Configure** section to add the channel ID and message text.

{% hint style="info" %}
Channel ID and message text can be fetched from previous steps or entered as static values.
{% endhint %}

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3iSr2Tx8FvvuoLPncziH%2Fuploads%2FdgXFKW1RQEE3nUkmHaQx%2F20250704-1926-55.4506826.mp4?alt=media&token=455eab13-dae7-441a-9b31-3fd13c0490a7" %}

Save the configuration and you will see the Send Message Slack Connector in the flow:

<figure><img src="../../../../.gitbook/assets/image (245).png" alt="Flow editor showing the configured Slack Send Message connector step in the workflow"><figcaption></figcaption></figure>

## Creating a Custom Connector for your Workspace/Organization​

To manage connectors within your workspace:

* Navigate to Connectors in your workspace.
* Locate the group of connectors where you wish to add a new one.
* Click the **Add** button in the top right corner.

<figure><img src="../../../../.gitbook/assets/image (246).png" alt="Workspace connectors page with the Add button in the top right corner for creating new connectors"><figcaption></figcaption></figure>

*   Choose **Add Custom Action**. Select the type of connector to add:

    * Function
    * HTTP API
    * gRPC
    * Database

    <figure><img src="../../../../.gitbook/assets/image (247).png" alt="Add Custom Action dialog with connector type options: Function, HTTP API, gRPC, and Database"><figcaption></figcaption></figure>

### Function Connector

Selecting a Function Connector will allow you to add a function that forms the basis of your connector. You can add the code for the function and view the input and output schema in a Form, JSON or YAML format. You can test run the function from the **Test** section before creating it.

{% hint style="info" %}
You can Edit or Preview your connector function from the connectors list in your workspace connector after its creation.
{% endhint %}

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3iSr2Tx8FvvuoLPncziH%2Fuploads%2F7G5yvUnfHJr8EYX9M4RF%2F20250704-2303-37.1977765.mp4?alt=media&token=b9ab5bcf-b29f-4c68-922f-4679d5e3fd46" %}

### HTTP API Connector

Selecting an HTTP API Connector will allow you to connect with RESTful APIs over standard HTTP/HTTPS. You can add an HTTP URL and include JavaScript code to form the basis of your connector. You can define and test API calls directly in the platform, ensuring proper integration and functionality before implementation.

<figure><img src="../../../../.gitbook/assets/image (476).png" alt="HTTP API Connector setup with URL field and JavaScript code editor for defining API calls"><figcaption></figcaption></figure>

### gRPC API Connector

With the gRPC API Connector, you can connect with services that expose APIs over gRPC instead of HTTP. This feature allows for efficient communication with these services, leveraging the benefits of gRPC such as improved performance and support for multiple languages.

<figure><img src="../../../../.gitbook/assets/image (480).png" alt="gRPC API Connector configuration interface for connecting to gRPC-based services"><figcaption></figcaption></figure>

### Database Connector

You can add a connector that can integrate databases such as Postgres, Redshift, and MySQL into your workspace.

<figure><img src="../../../../.gitbook/assets/image (477).png" alt="Database Connector setup showing options for PostgreSQL, Redshift, and MySQL integration"><figcaption></figcaption></figure>
