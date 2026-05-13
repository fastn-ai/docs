---
description: >-
  Manage how your flow runs and looks with the Settings sidebar, where you can
  configure execution, validation, security, and visuals.
---

# Flow Settings

When working inside any **Flow** in Fastn, you can adjust its behavior and appearance through the **Settings** option available in the **right-hand sidebar**.

<figure><img src="../../../../.gitbook/assets/image (553).png" alt="Flow editor with the Settings option highlighted in the right-hand sidebar"><figcaption></figcaption></figure>

The Settings panel has two main subsections: **Configuration** and **Visuals**.

<figure><img src="../../../../.gitbook/assets/image (134).png" alt="Settings panel showing Configuration and Visuals subsections"><figcaption></figcaption></figure>

## 1. Configuration

The **Configuration** section controls how your flow runs and how it handles security, validation, and errors.

### **Flow Type**

You must choose how the flow should execute:

#### **🔹 API (Real-Time Sync API)**

* Executes instantly and returns a real-time response.
* Used for synchronous tasks where the result is needed immediately.

#### **🔹 Workflow (Async Workflow Job)**

<figure><img src="../../../../.gitbook/assets/image (135).png" alt="Workflow flow type settings with memory limit, CPU limit, priority, and timeout options"><figcaption></figcaption></figure>

* Executes in the background without blocking the request.
* Suitable for asynchronous or heavy jobs.
* When you select **Workflow**, additional options appear:
  * **Memory Limit** – Maximum memory allocation (e.g., 2 GB).
  * **CPU Limit** – Maximum processing power allocated (e.g., 1 vCPU).
  * **Priority** – Determines how quickly the workflow is executed (Low/Medium/High).
  * **Timeout (min)** – Maximum duration before the workflow stops.

When Workflow is selected, a new **Trigger** section appears in the **left sidebar**, where you can define how the workflow is initiated:

<figure><img src="../../../../.gitbook/assets/image (140).png" alt="Trigger section in left sidebar with Manual, Event, and Schedule workflow initiation options"><figcaption></figcaption></figure>

* **Manual** – Run the workflow manually.
* **Event** – Triggered by an event.
* **Schedule** – Triggered at scheduled intervals.

### **Validation & Multi-Tenancy**

<figure><img src="../../../../.gitbook/assets/image (136).png" alt="Validation and Multi-Tenancy settings with Enable Validation and Enforce Multi-Tenancy toggles"><figcaption></figcaption></figure>

* **Enable Validation** – Enforce schema validation for flow input.
* **Enforce Multi-Tenancy** – Require the `x-fastn-space-tenantid` header to ensure the flow only accesses resources for the specified tenant.

### **Authentication**

<figure><img src="../../../../.gitbook/assets/image (137).png" alt="Authentication settings with Enable Custom Authentication toggle for Authorization header support"><figcaption></figcaption></figure>

* **Enable Custom Authentication** – Allow access with an `Authorization` header instead of `x-fastn-api-key`.
* Uses the **fastnCustomAuth** flow for validation.
* You can customize this authentication flow as needed. [Learn More](../../tutorials/flow-customization-and-operations/how-to-customize-your-authentication-flow.md)

### **Error Notification**

<figure><img src="../../../../.gitbook/assets/image (138).png" alt="Error Notification settings with toggle to forward errors to a notification flow like Slack"><figcaption></figcaption></figure>

* **Enable Error Notification** – Forward errors to a notification flow (e.g., sending alerts to Slack).
* You can customize this with the **fastnErrorNotification** flow. [Learn More](../../tutorials/flow-customization-and-operations/how-to-customize-your-error-notification-flow.md)

## 2. Visuals

The **Visuals** section customizes the flow editor interface.

<figure><img src="../../../../.gitbook/assets/image (139).png" alt="Visuals settings with toggles for Side Action Panel, Flow MiniMap, and Dark Mode"><figcaption></figcaption></figure>

* **Enable Side Action Panel** – Displays a quick-access panel for drag-and-drop actions.
* **Enable Flow MiniMap** – Adds a minimap to navigate large or complex flows.
* **Activate Dark Mode** – Switches the editor to dark theme.
