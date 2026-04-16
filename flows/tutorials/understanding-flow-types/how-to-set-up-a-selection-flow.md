---
description: >-
  Learn how to build a selection flow that powers dropdown selections inside
  configuration flows, using connector actions like Google Cloud Storage Get
  Buckets as an example.
---

# How to Set Up a Selection Flow?

Selection flows in Fastn allow you to fetch dynamic data (such as lists of items, projects, or files) that can then be displayed as selectable options inside configuration flows. These are reusable across widgets or connectors wherever a dynamic selection is required.

## **1. Create a Selection Flow**

* Go to the **Widgets** section in Fastn.
* Click the arrow next to the **Add Widget** button (top-right corner).

<figure><img src="../../../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

* Select **Add Selection Flow**.
* Enter a name for your flow and click **Build**.

<figure><img src="../../../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

This will create a configuration flow that allows you to define the logic for your selection data source.

> In this guide, we’ll build a selection flow using the **Google Cloud Storage** connector and its **Get Buckets** action.

## **2. Add a Connector Action Step**

Inside your new flow, add a step and choose **Connector Action**.

This is where you define which connector and which specific endpoint will supply data to your selection flow.

1. Under **Group Type**, select **Fastn Connectors**.
   * You can also choose **Workspace Connectors** if you’ve built custom connectors in your workspace.
2. Under **Connector**, select **Google Cloud Storage**.
3. Under **Endpoint**, select **Get Buckets**.

<figure><img src="../../../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>

Your step now represents the request that will fetch a list of storage buckets from Google Cloud Storage.

{% hint style="info" %}
For any connector you choose, the available endpoints will depend on that connector’s supported actions. For example, selecting _HubSpot_ would display actions such as _Get Contacts_ or _Get Companies_.
{% endhint %}

## **3. Configure the Connector Action**

After selecting the endpoint, click **Next**.\
You’ll now see the **Connection Configuration** section.

Here you can decide how your widget or flow connects to an account:

* **Fixed Connection:** Uses a specific account that you connect here (e.g., your own Google Cloud Storage account).
* **Dynamic Connection:** Allows multiple users to connect their own accounts dynamically through widgets.

<figure><img src="../../../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

## **4. Define the Configuration Parameters**

Once your connection is set, you’ll see the **Configure** section.\
This section displays the endpoint URL and the fields you can map.

For the **Google Cloud Storage – Get Buckets** endpoint, for example, you’ll see:

<figure><img src="../../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
You can provide **static values** directly in these fields or map them to existing **input variables** for flexibility.
{% endhint %}

## **5. Test the Selection Flow**

Next, open the **Test** section.

Here you can:

* View the **Headers** and **Input** fields used in your connector request.
* See the **Tenant ID** associated with your workspace or environment.
* Run a **Test** to verify that your selection flow returns the expected data (e.g., a list of buckets).

<figure><img src="../../../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

If successful, you’ll see the response data in the output preview.

## **6. Add a Final Step**

Once you’ve confirmed the connector response, you can add any follow-up step to process or format the data.

<figure><img src="../../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

For instance, in this use case,

* Add an **Advanced Action** to transform the output.

<figure><img src="../../../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>

* Add a **Loop** step to iterate over the items returned (e.g., each bucket).

<figure><img src="../../../.gitbook/assets/image (77).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (76).png" alt=""><figcaption></figcaption></figure>

* Or simply return a **Success Message** as an object confirming completion:

> **Str "GCS buckets' fetching successful"**

This final output will serve as the data source for your selection dropdown in configuration flows.

## **7. Using the Selection Flow in Configuration Flows**

After saving, your newly created flow will appear in:

* **Workspace Selection Flows** (if created within your workspace), or
* **Community Selection Flows** (if shared publicly).

{% hint style="info" %}
You can now reference this selection flow from any configuration flow that supports **Selection Type: Mapping, Dynamic, or Custom**.
{% endhint %}

For example, in your **GCS Configuration Flow**, when you open the selection dropdown for a dynamic input, you’ll see **“GCS – Get Buckets”** listed as an available selection source.\
You can then enable **pagination**, apply **limits**, or transform the results based on your configuration.

<figure><img src="../../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

Your selection flow is now ready and can be reused across configuration flows wherever dynamic data selection is required.

#### Example Scenarios

* [x] Populate dropdowns with live data from connectors (e.g., list of buckets, projects, or files).
* [x] Handle large datasets using pagination and limit controls.
* [x] Provide a seamless experience for users to select external data dynamically from widgets.
