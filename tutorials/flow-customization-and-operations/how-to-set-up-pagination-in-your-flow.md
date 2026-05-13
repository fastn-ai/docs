---
description: >-
  Fastn Flows lets you process large datasets efficiently by setting up
  pagination using parameters that control batch size and data offset.
---

# How to Set Up Pagination in your Flow?

This guide walks you through configuring your flow to fetch records in chunks (e.g., 1000 at a time) using a loop that continues until all records are retrieved.

## **Step 1: Initialize Pagination Variables**

Start your flow by adding a **Flow Variable Initializer** component to define:

<figure><img src="../../../../.gitbook/assets/image (223).png" alt=""><figcaption></figcaption></figure>

* `batchSize`: The number of records to fetch in one iteration (e.g., `1000`)
* `skipToken`: The initial offset value (set to `0`)

## **Step 2: Configure the Loop for Pagination**

In your main loop (e.g., when pulling records from Acumatica):

* Set the loop to **continue while records are returned**.
* Use the pagination variables to limit and offset your record fetch.

<figure><img src="../../../../.gitbook/assets/image (222).png" alt=""><figcaption></figcaption></figure>

Inside the loop:

* Add the **Get Records** action (e.g., from the Acumatica connector).

<figure><img src="../../../../.gitbook/assets/image (225).png" alt=""><figcaption></figcaption></figure>

* In its parameter mapping:
  * Set `top` to `{{var.batchSize}}`
  * Set `skip` (or offset) to `{{var.skipToken}}`

This setup fetches records in chunks, e.g., the first 1000, then the next 1000, and so on.

## **Step 3: Update `skipToken` After Each Iteration**

After fetching records in a loop iteration:

<figure><img src="../../../../.gitbook/assets/image (227).png" alt=""><figcaption></figcaption></figure>

* Add a **Variable Connector**
* Add the `skipToken` variable to update.
* Click the three-dot menu in the configure tab.

<figure><img src="../../../../.gitbook/assets/image (228).png" alt=""><figcaption></figcaption></figure>

* Choose **Advanced Action → Mathematical Expression**
* Set the expression as:

```handlebars
{{var.skipToken}} + {{var.batchSize}}
```

{% hint style="info" %}
Ensure both `skipToken` and `batchSize` are of type `integer` to support arithmetic operations.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (230).png" alt=""><figcaption></figcaption></figure>

This ensures:

* First iteration: `skip = 0`
* Second iteration: `skip = 1000`
* Third iteration: `skip = 2000`

...and so on.

## **Step 4: Handle Loop Exit When No More Records**

When the **Get Records** action returns an **empty list**, the loop will automatically stop.

<figure><img src="../../../../.gitbook/assets/image (231).png" alt=""><figcaption></figcaption></figure>

You can optionally add a **Filter** or a conditional **Switch** to handle this case explicitly by checking if the returned array is empty.

## **Step 5: Test the Flow with a Known Dataset**

Use a known dataset (e.g., an Acumatica table with 22,000+ records) for testing:

1.  Run the SQL count in the connected DB to validate the total:

    ```sql
    SELECT COUNT(*) FROM acumatica_custom_pricing_testtenantddp;
    ```
2. Ensure the full record count (e.g., `22,388`) is fetched in batches.

<figure><img src="../../../../.gitbook/assets/image (232).png" alt=""><figcaption></figcaption></figure>

* Check the **Logs** tab in Fastn:
  * Filter logs by tenant
  * Inspect the duration and status of each batch

<figure><img src="../../../../.gitbook/assets/image (233).png" alt=""><figcaption></figcaption></figure>

### Summary

| Parameter   | Purpose                   | Mapping                                 |
| ----------- | ------------------------- | --------------------------------------- |
| `top`       | Batch size per fetch      | `{{var.batchSize}}`                     |
| `skip`      | Offset for pagination     | `{{var.skipToken}}`                     |
| `skipToken` | Updated after every batch | `{{var.skipToken}} + {{var.batchSize}}` |

**Pagination is commonly supported by many APIs that return large datasets, including those that follow patterns like OData.** This makes the approach effective for systems such as Acumatica, Dynamics, and many others with batch data access capabilities.
