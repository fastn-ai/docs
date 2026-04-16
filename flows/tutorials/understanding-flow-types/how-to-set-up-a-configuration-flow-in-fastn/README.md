---
description: >-
  Learn how to create and manage configuration flows in Fastn. Configure fields,
  apply selection logic (static, dynamic, custom, mapping), and add field-level
  validation for user inputs.
---

# How to Set Up a Configuration Flow in Fastn?

Configuration flows define how data, fields, and user inputs are structured and connected inside your widgets. They help you build configurable interfaces that pass values dynamically between user inputs and connected apps or flows.

With configuration flows, you can:

* [x] Create reusable configuration interfaces for widgets or other flows.
* [x] Define and manage variables that drive your integrations.
* [x] Add logic for static, dynamic, custom, or mapping-based selections.
* [x] Apply validation to enforce input formats and required fields.

## **Creating a Configuration Flow**

To create a configuration flow:

* Go to the **Widgets** section in Fastn.
* Click the arrow next to the **Add Widget** button (top-right corner).
* Select **Add Configuration Flow**.

<figure><img src="../../../../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>

* Enter a name for your configuration flow and click **Build**.

<figure><img src="../../../../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

This creates a configuration flow that allows you to add steps, such as data mapping and field selectors.

This opens the flow builder, where you can start adding steps such as:

* **Data Mapping** to define fields and variables.
* **Connectors or Actions** to link with external tools.
* **Advanced Controls**, like conditions, transformations, and loops.

Once your flow is created, you can define how users will interact with it through field configuration.

## **Adding and Configuring Fields**

* Inside the flow, add a **Data Mapping Step**.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FdGeE774kq2pgzRfmE0ir%252Fimage.png%3Falt%3Dmedia%26token%3D3608aa43-11f0-4354-a60d-31ff05a57bc3&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=c281760f&#x26;sv=2" alt=""><figcaption></figcaption></figure>

The **Data Mapper** defines the variables and parameters that will be dynamically passed into your target app or flow.

* Click the three dots on this step to access options:
  * **Advanced Action**
  * **Add Parent Key**
  * **Set Default Value**
  * **Options**

The **Options** setting lets you configure fields that support **labels, selectors, and values**.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FqDOYeDNf0Jn9ao93oT0U%252Fimage.png%3Falt%3Dmedia%26token%3Dbd4dc861-d5ed-4586-9a05-fd9103d94a4f&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=e365a327&#x26;sv=2" alt=""><figcaption></figcaption></figure>

* Configure the following sections:

### **General Section** <a href="#general-section" id="general-section"></a>

Define how this field behaves and appears in the configuration pop-up:

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FN0BFXkUwTyWFFXT7x55W%252Fimage.png%3Falt%3Dmedia%26token%3D13916a4d-ddd5-4944-ad62-d96fec7653cf&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=cfd70b9f&#x26;sv=2" alt=""><figcaption></figcaption></figure>

* **Label** – Sets the display name in the widget UI.
* **Disable this field** – Prevents user edits.
* **Mark as new ID field** – Assigns a unique identifier for the configuration.
* **Hide this field in configuration pop-up** – Keeps advanced fields hidden from the user.
* **Hide Based on config field** – Control a field’s visibility based on another field’s value, by defining a key, operation, and value condition that determines when the field should appear or stay hidden.

<figure><img src="../../../../.gitbook/assets/image (658).png" alt=""><figcaption></figcaption></figure>

### **Selections Section** <a href="#selections-section" id="selections-section"></a>

This is where you make the configuration dynamic:

## **Selecting a Field Type**

Every field supports **Selections**, which define how users choose or input values.\
You can choose one of four **Selection Types**, each suited to different use cases.

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="image">Cover image</th><th data-hidden data-type="content-ref"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Static Selection</strong></td><td>Define fixed, predefined options that users can pick directly from a dropdown.</td><td><a href="../../../../.gitbook/assets/Screenshot 2025-10-16 232357.png">Screenshot 2025-10-16 232357.png</a></td><td><a href="setting-up-a-configuration-flow-with-static-selection-options.md">setting-up-a-configuration-flow-with-static-selection-options.md</a></td><td><a href="setting-up-a-configuration-flow-with-static-selection-options.md">setting-up-a-configuration-flow-with-static-selection-options.md</a></td></tr><tr><td><strong>Dynamic Selection</strong></td><td>Fetch real-time data from connected flows or APIs to populate your fields dynamically.</td><td><a href="../../../../.gitbook/assets/Screenshot 2025-10-16 232457.png">Screenshot 2025-10-16 232457.png</a></td><td></td><td><a href="setting-up-a-configuration-flow-with-dynamic-selection-options.md">setting-up-a-configuration-flow-with-dynamic-selection-options.md</a></td></tr><tr><td><strong>Custom Selection</strong></td><td>Design fully tailored configuration experiences like file pickers or advanced selectors.</td><td><a href="../../../../.gitbook/assets/Screenshot 2025-10-16 232656.png">Screenshot 2025-10-16 232656.png</a></td><td></td><td><a href="setting-up-a-configuration-flow-with-custom-selection-options.md">setting-up-a-configuration-flow-with-custom-selection-options.md</a></td></tr><tr><td><strong>Mapping Selection</strong></td><td>Map fields and values between source and destination flows for seamless data alignment.</td><td><a href="../../../../.gitbook/assets/Screenshot 2025-10-16 232812.png">Screenshot 2025-10-16 232812.png</a></td><td></td><td><a href="setting-up-a-configuration-flow-with-mapping-selection-options.md">setting-up-a-configuration-flow-with-mapping-selection-options.md</a></td></tr></tbody></table>

Each selection type has its own setup flow and example.\
You can learn more in the following guides:

### **Adding Field-Level Validation**

You can also add validation to ensure users provide correct data before saving their configurations.\
For example, you can:

* [x] Require fields to be filled.
* [x] Enforce URL or email formats.
* [x] Display custom error messages for invalid input.

Learn more about how to add field validation here:<br>

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="image">Cover image</th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Fields Level Validation in Configuration Flows</strong></td><td>Add rules to verify user input and ensure data accuracy in configuration fields.</td><td><a href="../../../../.gitbook/assets/Screenshot 2025-10-16 232116.png">Screenshot 2025-10-16 232116.png</a></td><td><a href="setting-up-field-level-validation-in-configuration-flows.md">setting-up-field-level-validation-in-configuration-flows.md</a></td></tr></tbody></table>

## **Using Configuration Flows in Widgets**

Once configured, your flow can be attached to any widget:

* The widget automatically renders the fields you’ve defined.
* Static, dynamic, or mapped options appear in dropdowns or pickers.
* Any validation rules are enforced before submission.

> This enables your widgets to provide users with rich, reliable, and interactive configuration experiences, powered by your underlying flow logic.

### **Next Steps**

{% stepper %}
{% step %}
Explore each configuration type in detail.
{% endstep %}

{% step %}
Combine mapping and validation for complex use cases.
{% endstep %}

{% step %}
Reuse your configuration flows across multiple widgets to maintain consistency.
{% endstep %}
{% endstepper %}
