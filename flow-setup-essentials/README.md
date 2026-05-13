---
description: >-
  Flows power automation by letting you define how data should move and be
  processed across your systems.
---

# Flow Setup Essentials

## **What Are Flows?**

In Fastn, flows are sequences of steps that perform a complete operation from start to finish. These steps can include actions like API connectors, condition-based switches, loops, and even custom code. Flows power automation by letting you define how data should move and be processed across your systems.

## **Accessing Flows**

You can view and manage all your existing flows by navigating to the **Flows** section from the left-hand menu in your project workspace.

<figure><img src="../../../.gitbook/assets/image (417).png" alt="Fastn Flows page listing existing flows with the Create Flow button in the left-hand menu"><figcaption></figcaption></figure>

You can click on the **Templates** button to access the section that presents several pre-built templates that we have for different connections and actions.

Click on **Create Flow** to select a starting point for the type of flow you want to create:

<figure><img src="../../../.gitbook/assets/image (410).png" alt="Create Flow dialog showing flow type options for selecting a starting trigger"><figcaption></figcaption></figure>

## **Flow Types**

Fastn supports multiple types of flows, based on the event or trigger that starts them:

### **i. On API Request**

Kick off a flow whenever an external system makes an API call to Fastn. This is perfect for building seamless integrations between Fastn and your internal tools or external services. Whether you're triggering actions from a custom app or automating backend operations, this option gives you full control via a simple API endpoint.

#### **Use Case (Send Email via Gmail)**

Suppose you want to send an email automatically whenever an API request is made to Fastn. You can set this up by:

* **Starting Point:** Select **On API Request** as your flow trigger.
* **Add Connector:** Choose **Gmail** from the _fastn Connectors_.
* **Endpoint:** Select **sendMail**.

<figure><img src="../../../.gitbook/assets/image (583).png" alt="Flow editor with On API Request trigger connected to a Gmail sendMail connector step"><figcaption></figcaption></figure>

* **Configure Gmail Action:**
  * Subject
  * Raw Email Data
  * Recipient Email
  * Email Content

<figure><img src="../../../.gitbook/assets/image (584).png" alt="Gmail connector configuration panel with fields for subject, raw data, recipient, and email content"><figcaption></figcaption></figure>

* **Save & Test Run:** Once saved, you can send a test API request. Fastn will process it and automatically trigger the Gmail action.

> When you check the inbox for the recipient email, you’ll see the email with the subject **“Test”** and the body **“This is a test email from Fastn.ai”**.

<figure><img src="../../../.gitbook/assets/image (582).png" alt="Email inbox showing the test email sent by the Fastn Gmail flow with subject Test"><figcaption></figcaption></figure>

### **ii. On App Event**

Let your flow respond to what's happening in your favorite apps; like Salesforce, Shopify, or HubSpot. When something changes (like a new lead, order, or form submission), Fastn can jump into action automatically.

<figure><img src="../../../.gitbook/assets/image (581).png" alt="On App Event trigger configuration showing available apps like Salesforce, Shopify, and HubSpot"><figcaption></figcaption></figure>

#### **Use Case (HubSpot Contact Creation)**

When setting up your flow, you select HubSpot as the app, then choose Contact Creation as the trigger event. After connecting your HubSpot account, Fastn starts listening for new contacts.

Here’s how it works in action:

* A prospect fills out a form on your website.
* HubSpot automatically creates a new contact with their details.
* Fastn detects this new contact creation event.
* The flow can then send a welcome email, add the contact into a marketing campaign, or log the event in your database, depending on how you configure the next steps.

> This way, every new contact from HubSpot can immediately trigger downstream actions, without you having to check HubSpot manually.

### **iii. On Webhook Event**

Flows can listen for incoming webhooks and act instantly when data is received. This trigger is perfect when you want Fastn to respond to external systems in real-time; whether you're syncing customer updates, processing transactions, or handling alerts from other platforms.

#### **Use Case (Webhook → Google Docs + Slack)**

When a webhook event is triggered, Fastn creates a new document in Google Docs with the received data and then shares the link directly into a Slack channel. This way, every webhook instantly generates a record and notifies your team.

<figure><img src="../../../.gitbook/assets/image (577).png" alt="Flow editor showing a webhook trigger connected to Google Docs creation and Slack notification steps"><figcaption></figcaption></figure>

### **iv. On Schedule**

Use this trigger to run flows automatically at specific times; whether that’s every hour, once a day, once a week, or on a custom schedule you define. It’s perfect for tasks that need to happen regularly, like sending reports, syncing data, or cleaning up old records. Just set it once, and Fastn will handle it from there.

#### **Use Case (Google Sheets → appendSheet)**

Every day at midnight, the flow runs on schedule and uses **Google Sheets → appendSheet** to log a timestamp entry in a report sheet. This helps maintain a daily record without anyone having to update it manually.

<figure><img src="../../../.gitbook/assets/image (576).png" alt="Scheduled flow running daily at midnight using Google Sheets appendSheet to log timestamp entries"><figcaption></figcaption></figure>

### **v. On Chat Message**

Trigger flows based on new messages from your users. This is especially useful for chatbot interactions, support flows, or conversational interfaces where a message can kick off a series of automated actions; all while keeping the experience personal and responsive.

#### Use Case (Intercom → getContacts)

When a user types _“Get my last 5 contacts from Intercom”_ into chat, Fastn triggers the flow and calls the **Intercom → getContacts** endpoint. The chatbot then returns the details of the most recent 5 contacts directly in the conversation.

<figure><img src="../../../.gitbook/assets/image (580).png" alt="Flow editor with On Chat Message trigger connected to Intercom getContacts endpoint"><figcaption></figcaption></figure>

<div align="left"><figure><img src="../../../.gitbook/assets/image (579).png" alt="Chat interface displaying the last 5 Intercom contacts returned by the chatbot flow"><figcaption></figcaption></figure></div>
