---
description: >-
  Add conditional branching logic to your Fastn flows. Use the Switch component
  to route automation paths based on specific data conditions.
---

# Add conditional logic with Switch in Fastn

Create conditional logic to control the flow of actions based on specific criteria. Switches enable your automation to choose different paths based on specific conditions.

For example, "if your input equals a certain value, do action X; otherwise, do action Y." This makes your flows flexible and able to handle different situations automatically.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FFz98Nmxur6aD9xNZwr8P%252Fimage.png%3Falt%3Dmedia%26token%3D662a8fb7-ce05-4f75-9ada-e1d536d1fda6&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b680b591&#x26;sv=2" alt="Switch component configuration with conditional cases and routing paths"><figcaption></figcaption></figure>

{% hint style="info" %}
You can add a number of cases and conditions as per your choice for the switch statement.
{% endhint %}

#### **Use Case: Add Conditional Logic to Control Flow Paths**

Use the **Switch** component to introduce decision-making within your flow. It evaluates defined conditions and routes execution through different paths based on the criteria you set. This enables your automation to adapt dynamically to different data states or outcomes.

```
Case1: status = Str "shipped" → Action = NotifyCustomer  
Case2: status = Str "pending" → Action = SendReminder
```

**How does it help?**

* Introduce branching logic to handle multiple scenarios
* Automatically trigger different actions based on conditions
* Simplify complex decision-making within a single flow
