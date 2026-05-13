---
description: >-
  Use the Activation Flow template to quickly set up and test new flows,
  webhooks, and routing logic in Fastn.
---

# How to Set Up an Activation Flow?

### Overview

The **Activation Flow** is a foundational template used to automate project or tenant activation. You can use it as-is for testing or customize it for your own setup. It’s available in the **Templates** section of your workspace.

This guide provides a conceptual overview of each step so you can understand the logic and modify it as needed.

### 1. Flow Initialization

The flow begins with a **Request step**, which acts as the entry point for the activation flow. This step captures the headers and the input payload that will be passed along to the subsequent steps.

<figure><img src="../../../../.gitbook/assets/image (620).png" alt=""><figcaption></figcaption></figure>

By default, this template is designed to start on a **new API request**, but you can configure the starting point differently depending on your use case.

{% hint style="info" %}
For more details, see [Flow Types – Choosing a Starting Point](../../flow-setup-essentials/#flow-types)
{% endhint %}

### 2. Initialize Your Flow Variables

The second step is a **Variable step** named **“initiate your flow variables.”**

This sets up key reusable values such as:

* **Project ID** – identifies which project or tenant the activation applies to.
* **Organization ID** – used to associate imported templates or configurations.
* **Template and Webhook objects** – used later in the loop steps for flow creation or validation.

<figure><img src="../../../../.gitbook/assets/image (621).png" alt=""><figcaption></figcaption></figure>

> By standardizing these variables early on, the rest of the flow can reference them consistently without redefining values.

### 3. Switch Step: _Tenant Exists?_

Before moving into template and webhook loops, the flow checks if the **tenant exists**.

<figure><img src="../../../../.gitbook/assets/image (622).png" alt=""><figcaption></figcaption></figure>

* **If the tenant does not exist →** return an **error message** response immediately.
* **If a tenant exists →** continue into the next stages (looping through templates and webhooks).

This ensures the flow only proceeds when a valid project/tenant is present.

### 4. Loop Over Templates

If your setup includes templates, the flow loops through each one to check whether a corresponding flow already exists.

<figure><img src="../../../../.gitbook/assets/image (623).png" alt=""><figcaption></figcaption></figure>

#### **Inside the loop**

* **Get API step** → checks if a flow already exists.

<figure><img src="../../../../.gitbook/assets/image (624).png" alt=""><figcaption></figcaption></figure>

* If it does not exist, the flow imports it using the defined project and template IDs.

<figure><img src="../../../../.gitbook/assets/image (627).png" alt=""><figcaption></figcaption></figure>

* This ensures that all required templates for the tenant are created and deployed.

> You can omit this section entirely if your activation doesn’t require template imports.

### 5. Loop Over Webhooks

Once templates are processed, the flow iterates through **webhooks**.

<figure><img src="../../../../.gitbook/assets/image (628).png" alt=""><figcaption></figcaption></figure>

#### **Inside the loop**

* **Get Webhook step** → checks if the webhook exists.

<figure><img src="../../../../.gitbook/assets/image (633).png" alt=""><figcaption></figcaption></figure>

* **Switch step** → if the webhook does not exist, create it with schedules and routes:

<figure><img src="../../../../.gitbook/assets/image (630).png" alt=""><figcaption></figcaption></figure>

Each webhook can include:

* Schedule details (frequency, unit, flow association).

<figure><img src="../../../../.gitbook/assets/image (631).png" alt=""><figcaption></figcaption></figure>

#### **Routes configuration**

* Route configurations (headers, flow IDs, routes).

<figure><img src="../../../../.gitbook/assets/image (634).png" alt=""><figcaption></figcaption></figure>

#### **Additional configurations**

* Optional settings like auto-generated API keys, retries, and authentication.

<figure><img src="../../../../.gitbook/assets/image (635).png" alt=""><figcaption></figcaption></figure>

> If your project doesn’t use webhooks, you can remove these steps and keep only the relevant logic for your activation.

### 6. Success Response

The final step is a **Response step**, which returns a success message.

* This confirms that templates have been imported (if needed) and webhooks have been created or validated.
* You can fully customize this response.

<figure><img src="../../../../.gitbook/assets/image (632).png" alt=""><figcaption></figcaption></figure>

### When to Use This Flow?

This is a **basic activation flow** typically used in multi-tenant setups. It ensures that each tenant’s templates and webhooks are properly initialized.

You can also adapt this structure for other activation scenarios:

* Use it without templates or webhooks by removing those loops.
* Treat any flow connected through a widget’s **“activate”** function as an activation flow.

> This template helps you structure any activation process, whether for tenants, projects, or custom configurations.
