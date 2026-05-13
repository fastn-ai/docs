---
description: >-
  Learn how to configure a mapping selection in your configuration flow, link
  source and destination flows, and control editable fields for your final
  widget setup.
---

# Setting up a Configuration Flow with Mapping Selection Options

Mapping flows allow you to link and transform data between different variables or connectors. They’re used to define how input fields map to target fields, enabling precise control over data relationships in your configuration.

## Setting Up the Mapping Configuration

In the **Selections** section, select Mapping from the list as your **Selection Type**.

<figure><img src="../../../../../.gitbook/assets/image (93).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This enables you to map data between flows by linking a **Source Flow** and a **Destination Flow**.
{% endhint %}

* **Enable Selection** – Toggles whether selection is active for this field.
* **Set this field as independent?** – Determines if the field functions independently from other mappings.
* **Selection Type** – Should be set to **Mapping** for this configuration.

<figure><img src="../../../../../.gitbook/assets/image (94).png" alt=""><figcaption></figcaption></figure>

### **Mapping**

* **Select Source Flow** – Choose the flow you want to pull data from.\
  You can select from:
  * **Community Selection Flows** – Predefined public flows.
  * **Workspace Selection Flows** – Your workspace-specific flows.
* **Select Destination Flow** – Choose the target flow where the mapping will apply.\
  The same community and workspace flow lists will appear for destination selection.

### **Editable Options**

* **Keys are Editable** – Allows editing of field keys from the source flow during mapping.
* **Add Fields** – Enables adding new fields to the destination flow during mapping.

Once configured, click **Save**.

### **Map Output to Widget Fields**

After you’ve selected your source and destination flows, the mapped values will automatically become available in your widget fields.

> Depending on your setup, editable keys and added fields will appear directly in the widget section, allowing further customization.
