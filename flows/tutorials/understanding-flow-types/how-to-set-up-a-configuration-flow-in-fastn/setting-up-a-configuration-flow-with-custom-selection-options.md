---
description: >-
  Learn how to create a custom file picker inside a configuration flow, set file
  type restrictions, and dynamically map selected files or folders to your
  widget fields.
---

# Setting up a Configuration Flow with Custom Selection Options

If you want to create a file picker with a more flexible and dynamic interface, use a **Custom Configuration Flow** as your **Selection Type**.

With **Custom Configuration Flows**, you can design any kind of configuration flow, adding your own fields, layouts, and UI elements. This makes it ideal for cases where you need more control over the interface and logic than standard dropdown selectors can provide.

### Configure Custom Selector

* In the **Options** section, choose the **Custom** Selector type.
* Select a file picker:
  * Google Drive File Picker
  * Dropbox File Picker
  * Microsoft OneDrive File Picker

<figure><img src="../../../../.gitbook/assets/image (95).png" alt=""><figcaption></figcaption></figure>

### **Using Custom Flow for Advanced File Picker**

> In this case, we’re using a **Custom Flow** to build a **File Picker**, because the UI is more customizable and allows you to define the exact structure and behavior you need. You can add any fields, apply your own design, and adjust the flow dynamically to fit your use case.

### Add File Type Restrictions

* After choosing your file picker, click the **File Types (+) icon**.
* Add file types (e.g., `.csv`, `.xlsx`, `.pdf`, `.jpg`).
* Save your settings.

<figure><img src="../../../../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This ensures the widget will only accept the file types you’ve defined.
{% endhint %}

### Map Output to a Field

If you have a widget field (e.g., **files**), map the file picker output to it. The selected files will be stored in this field, and the restrictions will enforce allowed file types.

<figure><img src="../../../../.gitbook/assets/image (104).png" alt=""><figcaption></figcaption></figure>

> **Result:** The widget can now collect files from users while respecting the restrictions you set.
