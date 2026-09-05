---
description: >-
  Answers to common questions about Fastn flows, debugging, data syncs,
  connector filtering, and integration best practices.
---

# FAQs

## Flow Fundamentals

<details>

<summary>What is a flow, and why do I need it?​</summary>

* In the Fastn platform, flows are sequences of steps that perform an end-to-end operations like inserting data into a database or retrieving a list of products from a Shopify store.
* Users can build flows to create APIs that give a synchronous real-time response or workflows that are executed as asynchronous jobs.
* Using a range of available actions such as connectors, loops, switches, custom code, and more, users can tailor flows for their unique applications.

</details>

<details>

<summary>How do I run a Flow?</summary>

* After a flow is created it can be run using the available `Debugger` which allows users to test the `DRAFT` version of the flow, see the output and debug any issues.
* To run the `Debugger`, users can click on the `Run Debugger` button on the top right of the canvas page.
* Once flows are tested and finalized, they can be deployed as the `LIVE` version. Users can use the `Embed this Flow` feature on the canvas page to generate code or curl commands that trigger the flow externally either as part of user applications or through API tools such as Postman.
* API keys can be generated with desired permissions to authenticate access to selective flows.
* Executed flows can be monitored in the `Logs` page which can be accessed using the navigation menu.

</details>

<details>

<summary>How do I debug a flow that is returning an error?</summary>

* A flow can be tested at any stage during its creation using the `Debugger`.
* To run the `Debugger`, users can click on the `Run Debugger` button on the top right of the canvas page.
* The `Debugger` allows users to view the end result of a flow as well as any error messages that may have been thrown in the execution of the flow.
* The step which threw the error is highlighted with a red border in the canvas page.
* The `Debug` view in the `Debugger` can offer more insight by showing users the output of each step used in the flow.
* When staged versions of flows are triggered externally using an API request, their logs and metrics are available in the `Logs` page.
* For each flow, the executed steps are highlighted along with any steps that threw an error.
* Using information gathered from these various means users can pinpoint the source of the error.

</details>

<details>

<summary>How do I integrate a flow into my application?</summary>

* Once flows are tested and finalized, they can be deployed as the `LIVE` version. Users can then use the `Embed this Flow` feature on the canvas page to generate code or curl commands that trigger the flow externally.
* The `Generate API Key` option can be used generate a new API key that is passed in the request headers to authenticate access to flows.
* The generated code in the `Embed This Flow` dialog box can then be copied into a user application in the desired format.

</details>

## Design and Best Practices

<details>

<summary>How should I filter records in API-based connectors?</summary>

Most connectors support filtering via query parameters. When filtering by fields like email, ensure values are properly URL-encoded, this includes support for plus-addresses (e.g. `user+tag@example.com`).

</details>

<details>

<summary><strong>How can I design flows for large and reliable data syncs?</strong></summary>

Split the sync into two flows:

* **Ingestion Flow**: Fetch data and store it in the Fastn database.
* **Publishing Flow**: Push stored records to the destination in smaller batches.\
  This reduces API pressure, improves reliability, and allows for easier retries and monitoring.

</details>

<details>

<summary>What are best practices for creating unique keys or identifiers?</summary>

Use expression steps or custom code to concatenate multiple fields and generate composite keys (e.g. `price_key = product_id + "_" + region`). This helps with deduplication and mapping in downstream systems.

</details>

<details>

<summary>How can I verify that all records were processed successfully?</summary>

Log synced record IDs or counts to the Fastn database to track actual progress and catch any missed or partial data, even if the flow logs report success. Additionally, you can add a [**Success Response**](../flow-setup-essentials/designing-a-flow/#flow-response-success-and-error) flow component at the end of your flow to return a confirmation payload, record count, or custom output, ensuring the flow ran as expected.

</details>

<details>

<summary>What date format should I use in filters or payloads?</summary>

Use ISO 8601 format (`yyyy-mm-dd`). If your source data is in another format (e.g. Unix timestamp), use Fastn's built-in transformations to convert it before syncing.

</details>
