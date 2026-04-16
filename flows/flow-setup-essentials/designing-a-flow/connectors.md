---
description: >-
  Link your Fastn flow to external services and APIs like Slack and HubSpot.
  Configure prebuilt connectors to automate data exchange across 250+ apps.
---

# Connectors

The **Connectors** component links your flow to external services and APIs — such as Slack, HubSpot, or Google Sheets — enabling seamless data exchange. Use it whenever your flow needs to read from, write to, or trigger actions in a third-party application. Fastn provides 250+ prebuilt connectors, each with ready-to-use endpoints you can configure without writing code.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FzauUXKipsL4hupiUXRoK%252Fimage.png%3Falt%3Dmedia%26token%3D9155202f-7760-40a5-a0f8-a45514ff964e&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=cd9ae17&#x26;sv=2" alt="Connector component in the Fastn flow editor for linking external services"><figcaption></figcaption></figure>

When you add a connector step, you'll go through:

* **Select:** Choose the **group type** (Fastn Connector or Custom Connector) → then select the **app**.
* **Endpoint:** Pick the task you want to automate (e.g., `sendMessage`, `getContacts`).
* **Connect:** Authenticate by connecting your account.

For example, for the Google Cloud Storage Connector, a selected endpoint can be createBucket.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FkNAc16eApX7KPQ0mhVTb%252Fimage.png%3Falt%3Dmedia%26token%3Deeabd94a-ef02-484a-94d0-2f7d9abaa11c&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=5d777ac3&#x26;sv=2" alt="Google Cloud Storage connector with createBucket endpoint selected"><figcaption></figcaption></figure>

* **Configure:** Fill in the required fields or map from previous steps.

In this example,

### **Google Cloud Storage - Create Bucket**

This connector action lets you create a new storage bucket in your Google Cloud project. You can map variables or outputs from previous steps into its configuration.

#### **Params mapped in configuration**

```
param.project      = {{var.googleProjectId}}
body.storageClass  = STANDARD
body.name          = {{var.bucketName}}
body.location      = US
```

* `param.project` is mapped from a variable that holds your GCP project ID (`googleProjectId`).
* `body.name` is dynamically mapped from a variable `bucketName` ; allowing each flow run to create a bucket with a unique name.
* `body.storageClass` and `body.location` are fixed values here (`STANDARD`, `US`) but could also be mapped from variables or other steps.

{% hint style="info" %}
The configuration parameters can be static values or mapped from previous steps as shown in this example.
{% endhint %}

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FE30zP394Xj9AeCyLoLB2%252Fimage.png%3Falt%3Dmedia%26token%3D3804cbc5-8092-4294-8b0f-fc21e3bff922&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=c776ceec&#x26;sv=2" alt="Connector configuration panel with mapped parameters for Google Cloud Storage createBucket"><figcaption></figcaption></figure>
