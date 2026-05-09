---
description: Restrict the number of records processed or passed forward in the flow.
---

# Limit records in Fastn flows

The **Limit** component restricts how many items from a list pass forward to the next step in your flow. Use it when a connector returns more records than you need — for example, keeping only the first five collaborators from a Zendesk ticket or the ten most recent orders from Salesforce. Place it immediately after any step that outputs a list to control the volume of data your downstream steps process.

{% hint style="info" %}
This is especially useful when you only want to process a subset of records instead of the full list.
{% endhint %}

### **Use Case Example**

Suppose you are building a flow where you fetch a Zendesk ticket and want to notify only a limited number of collaborators about an update. Zendesk’s **Get Ticket** action returns a list of `collaborator_ids`, but you may only want to process the first 5 collaborators.

This is where **Limit** helps.\
You can narrow the list, e.g., to the first 5 collaborator IDs, before sending them to further steps such as **email**, **Slack**, or additional logic.

### **How does the Limit feature work?**

* After your connector step (for example, **Zendesk → Get Ticket**), add the **Limit** step from the **Transformation Actions** section.

<figure><img src="../../../../.gitbook/assets/image (662).png" alt=""><figcaption></figcaption></figure>

* In the **List** field, provide the list you want to limit.\
  For example, if you're retrieving ticket details from Zendesk, you can use:\
  `{{steps.getTicket.output.ticket.collaborator_ids}}`

<figure><img src="../../../../.gitbook/assets/image (663).png" alt=""><figcaption></figcaption></figure>

* In **Max Items**, enter the maximum number of items you want to allow through.\
  **Example:** `5`

<figure><img src="../../../../.gitbook/assets/image (664).png" alt=""><figcaption></figcaption></figure>

*   Choose the **starting direction** for the limit:

    * **From First Item**
    * **From Last Item**

    This defines whether the limit applies from the beginning or end of the list.

<figure><img src="../../../../.gitbook/assets/image (665).png" alt=""><figcaption></figcaption></figure>

* Click **Save** in the top-right corner to apply the configuration.

<figure><img src="../../../../.gitbook/assets/image (666).png" alt=""><figcaption></figcaption></figure>

* To test the step, use the **Dashboard** button in the top-right corner.

<figure><img src="../../../../.gitbook/assets/image (668).png" alt=""><figcaption></figcaption></figure>
