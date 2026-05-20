---
description: >-
  Learn what the Embedded Experience is, where it's useful, and see how it works
  through a real-world Shopify example.
---

# Getting Started with Fastn’s Embedded Experience

## What is the Embedded Experience?

The **Embedded Experience** in Fastn allows you to bring your automated workflows directly into your product or platform. This gives your users a seamless, interactive way to trigger and manage workflows, without needing to log into Fastn or understand its backend logic.

It’s designed to create a **white-labeled, native experience**, helping you deliver integrations and automation as a built-in feature of your own app.

## Where Embedding Is Useful

You can embed Fastn to:

* Let customers **trigger workflows** from within your app (e.g., sync product data, send alerts, or request reports).
* Allow users to **authenticate with third-party services** (like Shopify, Slack, or Jira) without leaving your platform.
* **Display workflow status or results** using your own UI components, keeping everything in one place.



Let’s walk through a real-world scenario of using Fastn’s embedded experience.

## Example Use Case: Sync Shopify Products to Elasticsearch

Imagine you're building a platform for e-commerce merchants, and you want to offer product sync from **Shopify to Elasticsearch,** without building the integration yourself.

Here’s how you can do it using Fastn:

* **Use a Prebuilt Template**
  * Go to the **Flows** page in Fastn.
  * Click on **Templates** in the top-right corner.
  * Switch to the **Community Templates** tab and select the **Shopify** label.
  * Find the **"Activate Shopify Export"** template, click the three dots, and select **Import**.
* **Activate with a Widget**
  * Once the flow is imported, attach it to a **Widget**.
  * Embed the widget in your app using a simple `<script>` or `<iframe>`.
  * Your users can now click a button to authenticate with Shopify and instantly enable the sync—without any dev work on your side.

This embedded flow will keep Elasticsearch updated automatically whenever new products are added to Shopify.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe1zf2HAGRryfoO-sczer2ui2jGMrwYeJGmDO7A5bJC8fP7gWzFhXo-kS18Z99CKhNjG55-Dqbqbrc0NTrfMbC_TaDkfQHWGDUPLvQt3T8SOmxb3Js9zqet15pWab1hnGKO1gd3?key=aWFNWdC9I0x6b7wkwYQbDg" alt="Activate Shopify Export flow template showing the multi-step workflow for syncing Shopify products to Elasticsearch"><figcaption></figcaption></figure>

* The Activate Shopify Export flow will perform multiple actions. It will prep the Elasticsearch database by handling index creation and import our required flows such as the exporting Shopify products, updating Shopify products and searching for Shopify products in Elasticsearch. Additionally, it will create the required webhooks in fastn and Shopify allowing product updates to be sent.
* Once the flow is imported, it will show up on the Flows page. Next we are going to open the flow and update the projectId in the Variables step to match the current project id which can found in the URL as shown in the images below.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcPpJ1Yl6reT2cgjV2-gR7rb1Mp4Wp4P4sM13ejfa9IZ_BBCQq74rx9JQdunpjJ74iLzt_WMYLCGyG8YizZYBlpIMam1S4ihN-Z4RCDANAyLQSe4Fg_TgRKrTTY4Aeeyl5QwJTh?key=aWFNWdC9I0x6b7wkwYQbDg" alt="Fastn Flows page showing the imported Activate Shopify Export flow"><figcaption></figcaption></figure>

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeny3xrP7sRYcRjXza7Hi-3JHzfEUbGh1h3tTloVjmf3TPnGfbTKFT5gnAwVnDt5VR1vkn-yowjgYaWqOG1SBylX3MDyx0WbNuykg6Uccl-Q7aCtV6ykatN5MBb10ESk_kCrV7wig?key=aWFNWdC9I0x6b7wkwYQbDg" alt="Flow editor showing the Variables step with the projectId field highlighted for updating"><figcaption></figcaption></figure>

* Next we are going to deploy the flow by clicking on the Deploy button on the top right.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcjLeVTAf4FwW0tNClEDL4O-RjiIKPdfb5OfWJ48VYZuBAWiLLdW_3hVBZ4uk4PVN6luKRr9K4oGSYN20OQMka02Fiw7YEwraYS3SE5PmfribHDwrB66-WZgF2upHot9ghnhZrc0w?key=aWFNWdC9I0x6b7wkwYQbDg" alt="Flow editor with the Deploy button highlighted in the top-right corner"><figcaption></figcaption></figure>

* Once the flow is deployed we are now ready to create our widget to trigger it.

### Setting up with Widget

* Go to the Connectors page, and find the Shopify connector under fastn connectors. Click on the three dots to see additional options and click on Publish.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdRNU3rmKsLSeWG1ojBo5FOMth70CYanwEWyU3CtKlP5ITeSG0ulXryAKOoMF1tYEFkmZABQPrhdbgoZ-SkV-kYRWEg1gf6RyiCILFEz6xDa06wSQ4H_gGbUMXL1dTgsIdoalTdBQ?key=aWFNWdC9I0x6b7wkwYQbDg" alt="Connectors page showing the Shopify connector with the three-dot menu open and Publish option visible"><figcaption></figcaption></figure>

* This will open the create a widget page with Shopify's info pre-filled. Next add the Activate Shopify Exports flow as an activate action as shown below and update the widget.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfiBPBSWm5YfeK0suaHhOWCK43NzWFsGdQRUTE-vi3unwalJP_vpZ1VWmF2BQ774E3O3ZwX0uxtruTyW-WZaAYwpD-H3w-6tyPg1nhUgVT_WqVmksCrGvW4ZmSOYEsecRHzN6u6?key=aWFNWdC9I0x6b7wkwYQbDg" alt="Widget editor showing Shopify info pre-filled with the Activate Shopify Exports flow added as an activate action"><figcaption></figcaption></figure>

* After the update the widget will be published. The published widget can be viewed by going to the Widgets page.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeGRIM5PF6s6pZZae1plmkgBIqBnsJfl9q-SPfrvHjWXqdWK6ysUHPdXf6pI7Ny4HEZ5bTl_9shWBQ6JamRmRmaundRQU9SNKKmnTO4z_VkXW8wSEn3zlWE2xVLLwhpaB2_9XoNHA?key=aWFNWdC9I0x6b7wkwYQbDg" alt="Widgets page displaying the published Shopify widget"><figcaption></figcaption></figure>

* Click on the Integrate button, generate a key and click preview to open the preview page and see the created widget.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdo999hGTWSYHW9BJVvE_M0h8dB1UQY8n1xSWaiedzdkSaXC2SYMyLmnUvQZ_FHIsSl3wgnzUXKeA8bg4D9zPHMcIBxZJRStBtvq0KVJjb_WDuDnaU79xVBmENPk8M8KS2Y__gTlQ?key=aWFNWdC9I0x6b7wkwYQbDg" alt="Widget preview page showing the Shopify widget with an Activate button for end users"><figcaption></figcaption></figure>

### Activating the flow

* Clicking on the Activate button will trigger the authentication of Shopify connector. Which will ask for the store name and authenticate using oauth.
* Once the authentication is successful the activate flow will be triggered.
* This step will import the required flows, which can be seen deployed in the Flows page.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXevUIzanBmXx1YK02l67IQV4o2vIRGHgQ_XdH-sxUaC2rxyXPDsE7dbFUcDhCMHHphOG1xk6gRR9e87OZ3ioSCDdCfiac_G3cNoNfOVZJWw19UbMBOfYSi8WzyuAtzbMXm18jz7gA?key=aWFNWdC9I0x6b7wkwYQbDg" alt="Flows page showing the imported Shopify flows deployed after activation, including export, update, and search flows"><figcaption></figcaption></figure>

* A webhook with the desired configurations, will be created, that can be seen on the Webhooks page

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdy8xHeol73JRs2fpGzrd6wgz5yL2SM7XDONMI_azXqJGyTtVNzLfD6q03reKaCpxIZrXRXQdkfIkV-VjtXsMsJz7fp-Ea8PT924bUsocJj1yg8lHttCSM6lUMd8yQsDqSTX8WCWw?key=aWFNWdC9I0x6b7wkwYQbDg" alt="Webhooks page displaying the auto-created webhook with Shopify product update configurations"><figcaption></figcaption></figure>

The example above demonstrates how widgets can be used to trigger multiple flows against a particular use case.

The Shopify widget can be integrated into a user's application to allow client to export data into their own Shopify accounts by using Widget to trigger authentication and connecting to their specific accounts.
