---
description: >-
  Add a step to log messages or data objects. Useful for debugging or tracking
  flow activity.
---

# Logger

The **Logger** component records messages, variable values, or object data at any point in your flow. Use it to monitor execution progress, validate logic, and troubleshoot issues by capturing real-time insights you can review in the **Logs** section of your Fastn workspace.

<figure><img src="../../../.gitbook/assets/image (660).png" alt="Logger component in the Fastn flow editor"><figcaption></figcaption></figure>

### **How does it help?**

* Monitor flow execution and debug easily
* Log key events, data points, or outcomes
* Improve visibility and traceability during automation runs

### **Where to view logs?**

All your flow logs are available in the **Logs** section, accessible from the left navigation panel inside your Fastn workspace.

<figure><img src="../../../.gitbook/assets/image (659).png" alt="Logs section in the Fastn left navigation panel"><figcaption></figcaption></figure>

This section displays a list of all your flows including the request and response logs (including start and end points).

* Any **custom Logger entries** you’ve added as part of your flow steps would be reflected here as well.

<figure><img src="../../../.gitbook/assets/Screenshot 2025-10-31 at 22.45.27.png" alt="Flow logs list showing request and response entries with custom logger entries"><figcaption></figcaption></figure>

### **Use Case**

Suppose you are processing files inside a **Loop over Templates** step, and each iteration checks a file’s processing status. You may want to log the count of:

* Skipped files
* Successfully processed files
* Failed files

#### Steps

* Add a **Logger** step **after** your loop.
* In the **Message** field, enter a summary string such as:

<figure><img src="../../../.gitbook/assets/image (51).png" alt="Logger message field with summary string for skipped, processed, and failed file counts"><figcaption></figcaption></figure>

> When your flow runs, this message will appear as a **separate log entry** in the **Logs section** of Fastn under that specific flow.

This lets you easily track loop outcomes and data processing metrics without searching through the entire flow execution trace:

<figure><img src="../../../.gitbook/assets/Screenshot 2025-10-31 at 22.45.56.png" alt="Log entry output showing loop outcome metrics in the Fastn Logs section"><figcaption></figcaption></figure>

{% hint style="info" %}
Use multiple Logger steps in key parts of your flow (e.g., before loops, after variable changes, or after conditional branches) to get detailed, structured insights during execution.
{% endhint %}
