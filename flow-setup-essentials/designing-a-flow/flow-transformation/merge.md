---
description: Combine data from multiple branches back into a single output path.
---

# Merge

The **Merge** component combines outputs from two or more previous steps back into a single data path. Use it after branches — such as parallel connectors, loops, or switch paths — when you need to reunify data before passing it to the next step. Merge appends or joins the results so downstream steps receive one consolidated input instead of multiple separate outputs.

### **When to Use the Merge Component?**

Use the Merge component when you need to:

* Combine outputs from two or more previous steps
* Bring data back into one path after branches
* Append or merge lists into a single list for next steps

## **How to Configure the Merge Component?**

### **Step 1: Add and Name the Merge Component**

* Add the **Merge** component to your flow

<figure><img src="../../../../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

* Give it a clear and descriptive name based on what you're merging\
  \&#xNAN;_(e.g., “MergeOutputandTokens”)_

This helps in identifying the merged output in the next steps.

### **Example Use Case**

You previously had:

* A **Loop Over Webhooks** step → produced a list
* A **Slack – Generate Token** step → produced token headers

<figure><img src="../../../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

After adding the Merge step, both outputs will be taken as inputs

* Strategy selected: **Append**
* The outputs are merged into one unified list

This lets you work with one combined result rather than handling two separate values.

{% hint style="info" %}
When merging lists, ensure that **both lists follow the same format.** This ensures the merge works correctly, and you can map the merged data without issues
{% endhint %}

### **Step 2: Select the Input Lists to Merge**

You will see fields to add the inputs you want to merge:

* Enter the reference for each list you want to merge\
  e.g.:
  * `{{steps.loopOverWebhooks.output}}`
  * `{{steps.generateToken.headers}}`

<figure><img src="../../../../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

> Add or remove fields using the icons on the right, based on how many sources you are merging.

### **Step 3: Choose the Merge Strategy**

You must select how the lists should be merged. For example:

* **Append** → Appends the lists in order, combining them into one list

<figure><img src="../../../../../.gitbook/assets/image (661).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
_This means list items from the second input will be added after the first list._
{% endhint %}

### **Step 4: Set the Number of Sources**

* Specify the number of sources you are merging

> Add or remove the source fields to match this count

<figure><img src="../../../../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

### **Step 5: Add a Success Message to Display Output**

Once your merge is complete:

* Add a **Success Message** component at the end of the flow
* Output the merged value inside this step
* Run the flow to confirm it executes successfully

<figure><img src="../../../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

> This will allow you to view both merged values clearly in the final output of the flow.
