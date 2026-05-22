---
description: >-
  Learn how to configure static fields in your configuration flow, define option
  values manually, and control how they appear in your widget interface.
---

# Setting up a Configuration Flow with Static Selection Options

The **Static Configuration Flow** type is used when you want to define a fixed list of options and their corresponding values manually. These options are predefined by you and appear to the user in the form of a dropdown list.

## **Configuring a Static Selector**

In the **Options** section, go to the **Selection Type** setting and choose **Static**.

<figure><img src="../../../../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

For example, if you’re defining a variable  `syncFrequency` in your Data Mapper step, you can configure it as an **array** and manually add static options.

## **Setting Up Static Options**

After selecting **Static** as your selection type, you’ll see the same general field options available for configuration:

Each item consists of:

* **Option Label** – The name displayed in the UI (e.g., “Once a Day”).
* **Option Value** – The value stored in the backend (e.g., 24).

You can add as many static values as needed. These will appear in the configuration as a dropdown list for users to choose from.

### **Example: Sync Frequency Variable**

Let’s say you have a variable called `syncFrequency`.

* When `syncFrequency` is an **array**, you can manually define options such as:
  * Option Label: **Once a Day** → Option Value: **24**
  * Option Label: **Every Hour** → Option Value: **12**

<figure><img src="../../../../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

This will be shown to users in a dropdown list when configuring the widget.

<figure><img src="../../../../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

However, if your `syncFrequency` depends on another variable.

<figure><img src="../../../../../.gitbook/assets/image (82).png" alt=""><figcaption></figcaption></figure>

For example, if the label or value needs to be generated dynamically (like `HubSpotToCin7`), then you should define `syncFrequency` as an **object variable** and use a **Dynamic Configuration Flow** instead.

<figure><img src="../../../../../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

> Your configuration flow is now set up with **Static Selection**, allowing you to define fixed option values that appear in dropdown menus. These static variables can be used in widgets or other flows wherever consistent, predefined selections are needed.

### **When to Use Static vs. Dynamic Config Flow?**

<details>

<summary><strong>Static Configuration Flows</strong></summary>

Use when you want fixed dropdown options that don’t change (e.g., predefined sync frequencies or toggle options).

</details>

<details>

<summary><strong>Dynamic Configuration Flows</strong></summary>

Use when your options need to be fetched dynamically (e.g., pulling tables, files, or account data).

</details>
