---
description: Transform and Reshape Data for the Next Step.
---

# Data Mapping in Flows

You can use **Data Mapper** to reshape and transform data as it flows through your integration. Whether you're preparing inputs for an API call, structuring data for storage, or customizing outputs for downstream steps, the Data Mapper gives you full control. You can reference outputs from earlier steps, use flow variables, or inject secrets to build the exact data object you need, without writing custom code.

### Getting Started

1. Log in to [live.fastn.ai](https://live.fastn.ai) and navigate to "Flows." Select the flow type you need and name your new flow based on the task you want to perform.
2. Navigate to the side panel and from the list of available flow components, select "Data Mapper." This will allow you to reshape your data as needed for your specific flow requirements.

<figure><img src="../../../.gitbook/assets/image (466).png" alt=""><figcaption></figcaption></figure>

3. Inside the Data Mapper, define your data types such as `int`, `string`, or `boolean`. Once you've established a key for your value, you can choose to:
   * Hardcode a value directly.
   * Map it from a previous step, for example, `{{input.text}}`.
   * Concatenate values to create a new data format, like `{{input.text}}_{{another.value}}`.

{% hint style="info" %}
Make sure your defined key type aligns with your headers or input in the terminal, otherwise it will throw an error.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (467).png" alt=""><figcaption></figcaption></figure>

4.  Utilize AI-assisted suggestions in the Data Mapper for efficient schema mapping. Use the search function in the Flow data Map to quickly locate and map items:

    * Add headers to a new key you defined.
    * Incorporate an input for mapping.
    * Include a secret value that you have defined for flows in your project.
    * Assign steps to a key that navigate input from the previous steps.
    * An App Config for any environment where you wish to deploy your project.

    <figure><img src="../../../.gitbook/assets/image (468).png" alt=""><figcaption></figcaption></figure>
5. You can run the Data Mapper in a debug mode. This allows you to verify the accuracy of mapping and ensure that the data transformations meet your expectations before proceeding to deployment.

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3iSr2Tx8FvvuoLPncziH%2Fuploads%2FRldJ4cCVXZ5G0iDzR7Nl%2F20250617-1958-06.8141168.mp4?alt=media&token=dd356c3e-c382-4033-8ac4-b7e8f3513487" %}

## Defining Field Data Types

<figure><img src="../../../.gitbook/assets/image (288).png" alt=""><figcaption></figcaption></figure>

Here's an example of defining different data types as shown in the image in JSON, including nested objects and arrays:

```json
{
  "integerValue": 42,
  "floatValue": 3.14,
  "stringValue": "example",
  "booleanValue": true,
  "passwordValue": "s3cr3t",
  "decimalValue": 9.99,
  "objectValue": {
    "nestedInteger": 1,
    "nestedString": "nested"
  },
  "orderedObjectJSON": [
    {
      "order": 1,
      "description": "First item"
    },
    {
      "order": 2,
      "description": "Second item"
    }
  ],
  "Array": {
    "key": "value",
    "list": [1, 2, 3, 4]
  }
}
```

## Value Configuration Options

### **1. Advanced Action**

In the **Advanced Action** section, a variety of options are available to dynamically manipulate data:

* **Filter:** Extract specific elements from arrays or lists.

The filter function iterates through the elements and selects those matching specified criteria. The result is a new array containing only the filtered elements.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```json
Variable Name: id_filter_with_variables
Loop Over: Key
Returned Field: first
Operator: ==
Value: {{field_value}}
```

<figure><img src="../../../.gitbook/assets/image (268).png" alt=""><figcaption></figcaption></figure>

* **UUID:** Generate a unique identifier.

A UUID generates a unique identifier that is essential for ensuring data items are distinct within a dataset. This function helps in tracking and referencing specific data entries in complex data mapping scenarios.

You need to fill in the following fields;

**Example Input**

```json
Variable Name: id_UUID
Generate Type: Dynamic UUID
```

<figure><img src="../../../.gitbook/assets/image (269).png" alt=""><figcaption></figcaption></figure>

* **Array Size:** Obtain the size of an array.

Complete the following fields in the Advanced Action to map your target array.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```yaml
Variable Name: id_array_Length
Target: {{headers['x-fastn-space-tenantid']}}
```

<figure><img src="../../../.gitbook/assets/image (272).png" alt=""><figcaption></figcaption></figure>

* **Escape String:** Escape special characters in a string.

Use this advanced action to automatically escape characters like quotation marks (`"`), backslashes (`\`), and others that may interfere with parsing or formatting in downstream systems. Useful when working with JSON, code snippets, or other structured data formats that require properly escaped strings.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```yaml
Variable Name: id_substring
Substring By: Regex
Target Value: {{input}}
Regex Value: [add regex here]
```

<figure><img src="../../../.gitbook/assets/image (271).png" alt=""><figcaption></figcaption></figure>

* **Loop:** Iterate over elements to apply transformations.

Use this action when you want to iterate through elements and apply transformations to each.\
You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```yaml
Loop Over: {{input}}
Variable Index: input_index
```

<figure><img src="../../../.gitbook/assets/image (273).png" alt=""><figcaption></figcaption></figure>

* **Substring:** Extract a portion of a string.

Use this action to extract a portion of a string (e.g., first 3 characters, regex match).\
You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```yaml
Variable Name: id_substring
Substring By: Regex
Target Value: {{input}}
Regex Value: [add regex here]
```

<figure><img src="../../../.gitbook/assets/image (274).png" alt=""><figcaption></figcaption></figure>

* **Trim White Spaces:** Remove leading and trailing spaces.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```yaml
Variable Name: id_trimmed
Trim Type: All
Target Value: {{input}}
```

<figure><img src="../../../.gitbook/assets/image (275).png" alt=""><figcaption></figcaption></figure>

* **Math Expression:** Apply mathematical calculations.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```
Mathematical Operation: {{input}} + 1
Cast Variable: Integer
```

<figure><img src="../../../.gitbook/assets/image (277).png" alt=""><figcaption></figcaption></figure>

* **Conditions:** Implement logic branches based on conditions.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```
Variable Name: id_condition
Condition (1):
  Key: {{field_value}}
  Operator: ==
  Value: {{target_value}}
Return Value: {{field_value}}
```

<figure><img src="../../../.gitbook/assets/image (278).png" alt=""><figcaption></figcaption></figure>

* **Converter:** Change data types or formats.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```
Variable Name: id_filter_date_converter
Conversion Type: Data To Stamp
Source Field: {{value}}
Date Format: ISO_8601
```

<figure><img src="../../../.gitbook/assets/image (279).png" alt=""><figcaption></figcaption></figure>

* **Transcode:** Transform data encoding.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```
Variable Name: id_decoder
Transcode Type: Decode Base64
Target Value: {{value}}
```

<figure><img src="../../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

* **Hashing:** Generate a hash value.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```
Variable Name: id_hash
Algorithm Type: SHA-256
Target Value: {{value}}
```

<figure><img src="../../../.gitbook/assets/image (281).png" alt=""><figcaption></figcaption></figure>

* **Append To List:** Add an element to a list.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```
Variable Name: id_insertList
Selected List: {{target_list}}
List To Append: {{list_to_add}}
```

<figure><img src="../../../.gitbook/assets/image (282).png" alt=""><figcaption></figcaption></figure>

* **Remove From List:** Delete elements from a list.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```
Variable Name: id_removeItems
Remove By: Index
Selected List: {{target_list}}
List of Indices: [list]
```

<figure><img src="../../../.gitbook/assets/image (283).png" alt=""><figcaption></figcaption></figure>

* **Insert Item:** Place an item at a specific position.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```
Variable Name: id_insertItem
Selected List: {{target_list}}
Item: {{item_to_add}}
```

<figure><img src="../../../.gitbook/assets/image (284).png" alt=""><figcaption></figcaption></figure>

* **Remove Item:** Delete an item from a list.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```
Variable Name: id_removeItem
Selected List: {{target_list}}
Index: {{item_index}}
```

<figure><img src="../../../.gitbook/assets/image (285).png" alt=""><figcaption></figcaption></figure>

* **Date Source:** Handle and manipulate date/time values.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```
Variable Name: id_dateSource
Generate Type: Now
Target TZ: UTC +02:00
Target Format: YYYY-MM-dd HH:mm:ss.SSS Z
Operation: None
```

<figure><img src="../../../.gitbook/assets/image (286).png" alt=""><figcaption></figcaption></figure>

* **Find index:** Determine the index of an element in a list.

You need to fill in the following fields in the Advanced Action settings to map your value according to that action. **This is an example input for this Advanced Action:**

```
Variable Name: id_indexOf
Searching Type: Find First
Search In List: {{target_list}}
Target Value: {{target_field}}
Target Type: Text
```

<figure><img src="../../../.gitbook/assets/image (287).png" alt=""><figcaption></figcaption></figure>

### **2. Add Parent Key**

**Use:** Encapsulate the field under a higher-level object key to create structured output.

**Example:**

*   Original:

    ```json
    { "id": "input" }
    ```
*   With parent key `"user"` added:

    ```json
    { 
      "user": { "id": "input" } 
    }
    ```

**What Happens:**\
The field becomes part of a nested JSON structure. This is useful when APIs or schemas expect data to be wrapped inside parent keys

### **3. Set Default Value**

**Use:** Define what value should be used when the input is missing or not explicitly set.

**Options:**

*   **Null**

    * Sets the field to `null`.
    *   Example output:

        ```json
        { "id": null }
        ```

    On every run, `null` is returned unless overridden. Useful when you want to mark a value as explicitly absent.
*   **Empty**

    * Sets the field to an empty string or empty object (depending on context).
    *   Example:

        ```json
        { "id": "" }
        ```

    Ensures the field exists with an empty value. Used to clear or reset the field.
*   **Fallback Value**

    * Provides a static value if nothing else is passed.
    *   Example:

        ```json
        { "id": "default-id-001" }
        ```

    If `id` is not set, this default will be used during execution.
*   **Required (fail if missing)**

    * Enforces that a value must be present.

    If `id` is not provided at runtime, the system throws an error or blocks the workflow. Ideal for mandatory identifiers.

### **4. Import JSON**

**Use:** Load and assign structured JSON data directly to the field.

**Example:**

*   Imported JSON file:

    ```json
    {
      "id": "123",
      "type": "admin",
      "status": "active"
    }
    ```
*   Result:

    ```json
    {
      "id": {
        "id": "123",
        "type": "admin",
        "status": "active"
      }
    }
    ```

\
The field is replaced by the full JSON structure from the import. This is useful for setting default templates or pre-populated data.

## **Code View & Expression Modes**

_View or author logic in different programming languages or expression styles._

Fastn data mapper offers a feature that allows you to switch between visual and code-based views for defining field values within a flow. It supports various programming languages like JavaScript, C#, and Python Lambda.

This flexibility enables users to manage their data structure according to their preferred coding or visual style, offering a more customizable approach to editing and mapping data. Additionally, the section mentions the functionality of adding states to manage dynamic data changes, like updating counters in response to API calls, which aids in maintaining accurate and updated data flow within the application.

* **Form**\
  Visual editor for defining field values through UI components.

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3iSr2Tx8FvvuoLPncziH%2Fuploads%2Fpksa3MHeMTLAOTTp4R1x%2F20250618-0053-03.5857023.mp4?alt=media&token=60270b80-df6d-45de-af0d-812dfb68631c" %}

Switch between visual and code-based views of field logic:

* JavaScript
* C#
* Python Lambda (if applicable)

## States & Mapping

You can add states in your flow before your data mapper to fetch values from previously defined states. Every time you call an API, you may want to increment a counter or update its count.

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3iSr2Tx8FvvuoLPncziH%2Fuploads%2Fr5fYo1fLSKtTVzKALvUb%2F20250617-2332-35.5026239.mp4?alt=media&token=6e1438b3-d2f7-4be8-b04e-bac06743cf7c" %}

This can be achieved by storing the last state information and using it next time you run the flow.

For example:

*   To increment a sum:

    ```plaintext
    state.inc.sum += 1
    ```
*   To check if a state exists and perform an operation:

    ```plaintext
    if (isExist(state.inc.sum)) {
        state.inc.sum++;
    } else {
        state.inc.sum = 1; // Initialize sum if it does not exist
    }
    ```

## Mapping with different Flow Components

When you build flows in Fastn, each component can both **take mapped inputs from previous steps** and **produce outputs that can be mapped into later steps**. The style of mapping depends on the type of component you are working with. Below are examples of how mapping works for each.

### **Connectors**

You can map values from a connector step’s output into another step, or pass dynamic values from earlier steps _into_ a connector.

#### **Example (Mapping into Gmail)**

_App: Gmail_\
&#xNAN;_&#x45;ndpoint: sendMail_

<pre class="language-js"><code class="lang-js">Object Recipient = {{steps.hubspot.output.getEmail}}
<strong>Object Subject = "Welcome " + {{steps.hubspot.output.firstName}}
</strong>Message = "Thanks for signing up!"
</code></pre>

#### **Mapping from Connector**

```js
{{steps.sendMail.output.messageId}}
```

### **Database**

Database steps accept mapped values from previous steps (to build queries) and also produce query results that can be mapped downstream.

#### **Example (Mapping into a SQL query)**

```sql
Query = SELECT * FROM orders WHERE customerId = {{steps.hubspot.output.contactId}}
```

#### **Mapping from Database (query result)**

```js
{{steps.databaseQuery.output.rows[0].email}}
```

### **Data Mapper**

The Data Mapper helps you transform or restructure values before passing them further. You can map in any output from earlier steps and produce a structured object as output.

#### **Example (Mapping into a new object)**

```json
{
  "id": {{steps.hubspot.output.contactId}},
  "name": {{steps.hubspot.output.contactName}},
  "isActive": true
}
```

#### **Mapping from Data Mapper**

<pre class="language-js"><code class="lang-js"><strong>{{steps.dataMapper.output.id}}
</strong></code></pre>

### **Variables**

Variables are defined once and then can be referenced throughout the flow.

#### **Example (Defining variables)**

<pre class="language-js"><code class="lang-js"><strong>Str filePath = "https://storage.fastn.ai/file.csv"
</strong>Int retryCount = 3
</code></pre>

#### **Mapping from Variables (in another step)**

```js
{{variables.filePath}}
```

### **Switch**

Switch uses mapped values to decide which path to take. You pass outputs from earlier steps _into_ the condition, and the result determines the execution path.

#### **Example (Mapping into a Switch Condition)**

```js
Case: {{steps.orderCheck.output.status}} == "shipped"
```

#### **Mapping from Switch (Branch Name)**

```js
{{steps.switchCase.output.selectedCase}}
```

### **Loop**

Loops take a list of items as input, and each iteration produces one item that can be mapped into child steps.

**Example (Mapping into Loop)**

```js
{{steps.getContacts.output.contacts}}
```

**Mapping inside Loop (item being iterated)**

```js
{{steps.loopOverContacts.item.email}}
```

### **Download File**

The Download File step maps a file URL from earlier steps, and produces a file reference for later steps.

#### **Example (Mapping into Download File)**

```js
SourceUrl = {{steps.apiFetch.output.downloadUrl}}
DestinationName = "report.csv"
```

#### **Mapping from Download File (file path)**

```js
{{steps.downloadFile.output.filePath}}
```

### **Logger**

Logger maps in any value you want to record. Its output is usually just a confirmation, but the logs can be used for debugging.

#### **Example (Mapping into Logger)**

```js
Header = "Order Status"
Message = {{steps.orderCheck.output.status}}
```

#### **Mapping from Logger**

```js
{{steps.logger.output.confirmation}}
```

### **Converter**

Converter takes mapped input (like JSON or CSV) and converts it into another format. You map the source data in, and then downstream steps can use the converted file or object.

#### **Example (Mapping into Converter)**

```js
StepName = convertInput
ConversionType = JSON_PARQUET
Source = {{steps.apiFetch.output.jsonData}}
```

#### **Mapping from Converter (converted data reference)**

```js
{{steps.convertInput.output.filePath}}
```

### **Custom Code (JSON)**

When using JSON code, values are accessed in the handler via `params.data.input`. You can map values in by defining them as inputs, and map values out by returning them.

#### **Example (Mapping into JSON code)**

```js
const projectId = {{params.data.input.projectid}};
const apps = {{params.data.input.apps}};
```

#### **Mapping from JSON code (return object)**

```js
return { query: "INSERT INTO apps ..." }
{{steps.customJsonCode.output.query}}
```

### **Custom Code (Python Lambda)**

For Python Lambda, you access mapped values from previous steps using `params['data']['steps']`. You return a response dictionary that can be mapped downstream.

#### **Example (Mapping into Python Lambda)**

```python
product_output = params['data']['steps']['getProductStep']['output']
```

#### **Mapping from Python Lambda (returned response)**

```python
response["discounted_price"] = 90
# mapped as: {{steps.pythonLambda.output.discounted_price}}
```

### **Flow Response (Success & Error)**

Flow Response maps in values you want to return as the final output of the flow. This could be static or pulled from previous steps.

#### **Example (Mapping into Flow Response)**

```json
{
  "status": "success",
  "orderId": {{steps.createOrder.output.id}}
}
```

#### **Mapping from Flow Response**

This is the **final payload** returned to the API or chat, it does not map further but represents the end of the flow.

## Standard Error Patterns

#### **DATA\_VALIDATION\_ERROR**

This error often arises due to issues with data mapping and type conversion. Here are some corrective actions to resolve it:

1. **Incorrect Type Mapping**: Ensure you are not mapping a string to other data types such as boolean, number, decimal, or list. Strings must be mapped to string fields only.
2. **Invalid Field Naming**: Do not start mapping field names with numbers, for example, `{{4444sss.tet}}` is not valid.
3. **Default Value Check**: If a field's default value is empty, consider setting it to `null`.
4. **Value Escaping**: Properly escape values that contain special characters like `"` or `/` using the advanced action feature.
5. **Advance Action Inputs**: Review any advanced actions in the step to ensure that input values are not passing incorrect data.
