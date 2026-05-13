---
description: >-
  This guide walks you through the Redshift-to-GCS migration flow, explaining
  each step so you understand what’s happening under the hood. The flow is
  designed to take queries from Redshift, process the
---

# Setting Up a Redshift to GCS Migration Flow

## **1. Flow Trigger and Initialization**

<figure><img src="../../../../.gitbook/assets/image (507).png" alt=""><figcaption></figcaption></figure>

### **i. Trigger on API Request**

The flow starts when an **API request** is received.\
This allows external systems to trigger the migration process on demand.

### **ii. Initialize Variables**

Sets up all **required variables** for the migration.\
This ensures the flow has the correct configuration and placeholders before processing begins.

<figure><img src="../../../../.gitbook/assets/image (508).png" alt=""><figcaption></figcaption></figure>

***

## **2. Configuration Mapping**

### **Map Redshift Config**

Uses a **data mapping step** to pull Redshift connection details from the [RedshiftConfigFlow.](setting-up-an-aws-redshift-to-gcs-migration-widget.md#configuration-flow-redshift_to_gcs)\
This ensures the flow knows which database and credentials to use.

<figure><img src="../../../../.gitbook/assets/image (510).png" alt=""><figcaption></figcaption></figure>

***

## **3. Create GCS Bucket**

### **GCS Bucket Creation**

The **Google Cloud Storage connector** creates a new bucket for the tenant.\
The bucket name is based on the mapped project ID, ensuring data isolation per tenant.

<figure><img src="../../../../.gitbook/assets/image (511).png" alt=""><figcaption></figcaption></figure>

***

## **4. Loop Over Tables**

This section processes data for each table in your migration list.

<figure><img src="../../../../.gitbook/assets/image (512).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (513).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (514).png" alt=""><figcaption></figcaption></figure>

### **i. Map Query Object**

Creates a **query object** containing the SQL query and output file name for the current table.\
This tells the flow what to fetch from Redshift.

<figure><img src="../../../../.gitbook/assets/image (515).png" alt=""><figcaption></figcaption></figure>

### **ii. Insert Item to Queries Variable**

Uses the **`insertItem` advanced action** to store the query in the `queries` variable.\
This variable will later be processed in the query execution loop.

<figure><img src="../../../../.gitbook/assets/image (516).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (517).png" alt=""><figcaption></figcaption></figure>

## **5. Security Check and Query Handling**

The next step after the Loop over Tables ends is the switch statement that checks for the query.

### **Switch: Query Provided?**

**If no query is provided**: Skip security checks and go directly to the **Loop Over Queries**.

<figure><img src="../../../../.gitbook/assets/image (518).png" alt=""><figcaption></figcaption></figure>

#### **If a query is provided**: Perform a security review before running it.

#### **i. OpenAI Security Scan**

The **OpenAI connector** analyzes the provided query for potential **security risks**.\
This helps prevent unsafe or malicious SQL execution.

It has the command:

```
function handler(params) {
  content = `You are a security validator. Your only job is to analyze the provided SQL query and return whether it is secure or not. You must return a single JSON object with only one boolean field:

	{"allowed": true} if the query is secure,
	{"allowed": false} if the query has security risks such as SQL injection vulnerability, use of dynamic string concatenation, or unsafe operations.

	Return only the JSON. No other explanation, comments, or messages.
	validate this query ${params?.data.steps.getConfigs.output.query}
`
  return {
    "auth": {
      "bearerToken": "aliqui"
    },
    "body": {
      "messages": [{
        "role": "user",
        "content": content
      }],
      "model": "gpt-4"
    }
  }
}
```

#### **ii. Map Security Scan Output**

Maps the security scan results into a structured format for the next decision step.

<figure><img src="../../../../.gitbook/assets/image (519).png" alt=""><figcaption></figcaption></figure>

#### **iii. Switch: Query Safe?**

* **If unsafe**: Returns an error message and stops execution.

<figure><img src="../../../../.gitbook/assets/image (520).png" alt=""><figcaption></figcaption></figure>

* **If safe**: Proceeds to map the custom query to a variable for execution.

<figure><img src="../../../../.gitbook/assets/image (521).png" alt=""><figcaption></figcaption></figure>

#### **Store Safe Query**

Initializes the safe query variable using the `insertItem` advanced action.\
This prepares it for batch or single execution.

<figure><img src="../../../../.gitbook/assets/image (523).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (524).png" alt=""><figcaption></figcaption></figure>

## **6. Loop Over Queries**

The output from the switch statement of whether thee query is provided or not is returned to this loop. This section handles executing queries and sending results to GCS.

<figure><img src="../../../../.gitbook/assets/image (525).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (526).png" alt=""><figcaption></figcaption></figure>

**Switch: Is Batching Enabled?**

**If yes**: Executes queries in smaller chunks to handle large datasets.

### **i. Batching Path**

#### **Initialize Batch Variables**

Sets `batchLoopIndex = 0` to track paging through results.

<figure><img src="../../../../.gitbook/assets/image (527).png" alt=""><figcaption></figcaption></figure>

#### **Infinity Loop for Batches**

Repeats until all data is processed.

<figure><img src="../../../../.gitbook/assets/image (528).png" alt=""><figcaption></figcaption></figure>

#### **Inside Infinity Loop:**

<figure><img src="../../../../.gitbook/assets/image (529).png" alt=""><figcaption></figcaption></figure>

1. **Remove Semicolons (JS Code)** – Ensures queries are clean before execution.

```
function handler(params) {
  const query = params?.data.steps.loopOverQueries.loopOverItem.query;
  
  return {
    query: query.replace(/;$/, '')
  };
}
```

2. **Map Base Query with Offset** – Adds `LIMIT` and `OFFSET` for pagination.

<figure><img src="../../../../.gitbook/assets/image (530).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (531).png" alt=""><figcaption></figcaption></figure>

3. **Execute Query (AWS Redshift)** – Runs the SQL against Redshift with batching parameters.

<figure><img src="../../../../.gitbook/assets/image (532).png" alt=""><figcaption></figcaption></figure>

4. **Switch: Execution Failed?** – Returns an error if execution fails.

<figure><img src="../../../../.gitbook/assets/image (534).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (535).png" alt=""><figcaption></figcaption></figure>

5. **Increment Batch Index** – Updates the offset for the next batch.

<figure><img src="../../../../.gitbook/assets/image (536).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (537).png" alt=""><figcaption></figcaption></figure>

6. **Map Batch Results** – Formats results for GCS upload.

<figure><img src="../../../../.gitbook/assets/image (538).png" alt=""><figcaption></figcaption></figure>

7. **Switch: Results Empty?** – Ends the loop if no more data.

<figure><img src="../../../../.gitbook/assets/image (540).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (539).png" alt=""><figcaption></figcaption></figure>

8. **Upload to GCS** – Sends the batch results to the tenant’s GCS bucket.

<figure><img src="../../../../.gitbook/assets/image (541).png" alt=""><figcaption></figcaption></figure>

9. **Switch: Last Batch?** – Ends the loop if the batch is smaller than the limit else, the iteration continues.

<figure><img src="../../../../.gitbook/assets/image (542).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (543).png" alt=""><figcaption></figcaption></figure>

### **ii. Non-Batching Path**

<figure><img src="../../../../.gitbook/assets/image (544).png" alt=""><figcaption></figcaption></figure>

1. **Execute Query (AWS Redshift)** – Runs the full query without pagination.

<figure><img src="../../../../.gitbook/assets/image (545).png" alt=""><figcaption></figcaption></figure>

2. **Switch: Execution Failed?** – Returns an error if query execution fails.

<figure><img src="../../../../.gitbook/assets/image (546).png" alt=""><figcaption></figcaption></figure>

**Else: Upload Results to GCS** – Sends the complete result set to the tenant’s GCS bucket.

<figure><img src="../../../../.gitbook/assets/image (547).png" alt=""><figcaption></figcaption></figure>

***

### **7. Completion**

#### **Return Success Message**

Once all queries are processed and results are uploaded, the main flow returns a **success response**.\
This confirms that the migration is complete.

<figure><img src="../../../../.gitbook/assets/image (548).png" alt=""><figcaption></figcaption></figure>
