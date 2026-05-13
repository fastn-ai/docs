---
description: >-
  These messages appear as UI elements that show when a Flow completes
  successfully or encounters an error.
---

# How to Customize Success and Error Messages UI in Flows?

In **Flows**, you can display customized success and error messages to inform users about the outcome of a Flow execution.&#x20;

{% hint style="info" %}
By default, success and error messages are shown as text notifications, but you can extend them into a UI format using the **`userMessage`** variable.
{% endhint %}

## What is userMessage?

**`userMessage`** is a Flow variable that enables you to define a custom interface for displaying messages on screen when a Flow runs.

> You can use it in both **Success Message** and **Error Message** components to present dynamic text, headers, or UI feedback.

## When to Use?

Use `userMessage` when you want to:

* Show a UI message confirming an action (e.g., successful activation or data sync)
* Display clear, branded, or styled error messages to users
* Customize the on-screen response after an API request or connector action completes

## How to Configure?

### **Step 1: Add a Success or Error Message Component**

In your Flow, add either:

* **Success Message** component → for successful runs
* **Error Message** component → for failed runs

{% hint style="info" %}
Place this component right after your API request or as the first step after the Flow trigger.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

### **Step 2: Set User Message Variables**

You can define custom values for `userMessage`  & `userMessageHeader` .

#### Example configuration

<figure><img src="../../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

### **Step 3: Add the JSON Configuration**

Insert the following JSON code in your Flow to render the message UI dynamically:

```json
{
  "json": {
    "userMessage": "Google has been activated successfully!",
    "userMessageHeader": "Activation Succeeded"
  },
  "actions": {
    "json": {
      "action": [],
      "targetType": "object"
    },
    "json.userMessage": {
      "action": [],
      "targetType": "string"
    },
    "json.userMessageHeader": {
      "action": [],
      "targetType": "string"
    }
  }
}
```

This JSON enables the Flow to display the success UI message when executed successfully.

> You can modify the text or header based on your use case.

### Example Use Case

**Scenario:** After a new Microsoft account is activated via API.

#### **Implementation**

* Add a **Success Message** component.
* Set the `userMessage` and `userMessageHeader` values.
* Use the above JSON structure.
* Deploy the changes to live.

<figure><img src="../../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

### **Attach the Flow to the App Widget**

In the **widget** for the Google app (or any other app for your use case), add the Flow you created for activation.

<figure><img src="../../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

> Deploy the changes to live, and you will be able to see the updated UI upon activation in the **Preview** section.

This ensures the Flow runs automatically when the widget action is triggered, for example, when a user clicks **Activate** or performs an API-based operation.

<figure><img src="../../../../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

\
After successful authentication by using the **Connect** button, a UI message appears displaying:

<figure><img src="../../../../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

> **Activation Succeeded**\
> Your Google account has been activated successfully!
