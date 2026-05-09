---
description: >-
  Transform and map data between flow steps in Fastn. Route outputs from
  connectors, variables, and secrets into the format your next step needs.
---

# Map and transform data in Fastn flows

The **Data Mapper** component lets you reshape and route data between flow steps. You can map outputs from previous steps, variables, or secrets into a new object structure that downstream steps require. Unlike the [Converter](converter.md), which changes data formats (for example, JSON to CSV), the Data Mapper restructures fields within the same format — renaming keys, combining values, or extracting nested properties.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FF1LauqCeDl6OOpO41GRJ%252Fimage.png%3Falt%3Dmedia%26token%3D15f5d337-2d04-4794-90a7-453cbd9bc77a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=fedb4a83&#x26;sv=2" alt="Data Mapper component in the Fastn flow editor"><figcaption></figcaption></figure>

For example,

This example mapping step titled "**Content"** can be used when you need to map data (usually text) from a previous step and ensure it's passed forward as a string.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252F8nGknZE7unentydDeBCl%252Fimage.png%3Falt%3Dmedia%26token%3Dbce2e596-2949-49e5-82b4-3e9930c3102c&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=f69f828b&#x26;sv=2" alt="Content mapping step with res field mapped from ChatGPT connector output"><figcaption></figcaption></figure>

### **Params mapped in configuration**

```
res = steps.chatGPT.output.choices[0].message.content
```

* Here, `res` is the variable inside the Content step.
* It is mapped directly from the **ChatGPT connector's** output: `steps.chatGPT.output.choices[0].message.content`.
* The mapped value must always resolve to a **string** type, since Content steps are designed to pass textual data forward.

### **Example**

* Pass the response from ChatGPT as plain text into another step (e.g., a database insert, a file generator, or a Slack notification).

To make this easier, the **AI agent** in the top-right corner offers smart suggestions for mapping your data. It helps you quickly pull values from previous steps or any flow data. You can simply drag and drop items like **Headers**, **Inputs**, **Steps**, **Secrets**, or **App Config** into the field you want to configure; making your mappings faster, more accurate, and less manual.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FeoYmFKjkgqK2Dn76s20S%252Fimage.png%3Falt%3Dmedia%26token%3D18001675-117e-4cc7-9953-9525af8ba7c3&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=c464291e&#x26;sv=2" alt="AI agent suggestions panel with drag-and-drop mapping for headers, inputs, steps, and secrets"><figcaption></figcaption></figure>

You can map values either in JSON, JavaScript, C#, Form, or Python Lambda.

### **Example JSON Mapping**

```
{
  "json": {
    "res": "{{data.steps.chatGPT.output.choices[0].message.content}}"
  },
  "actions": {
    "json": {
      "action": [],
      "targetType": "object"
    },
    "json.res": {
      "action": [],
      "targetType": "object"
    }
  }
}
```

> You can learn more about Data Mapping in Flows [here](https://docs.fastn.ai/building-flows/flow-setup-essentials/data-mapping-in-flows).
