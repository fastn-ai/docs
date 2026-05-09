---
description: >-
  Repeat actions in your Fastn flow using loop components. Iterate over data,
  run fixed repetitions, or use while conditions for workflow automation.
---

# Repeat actions with Loop in Fastn flows

The **Loop** component repeats a set of actions multiple times within your flow. Use it when you need to iterate over a list of items (such as processing each record from an API response), run a block a fixed number of times, or keep executing while a condition remains true. Fastn supports three loop types: **Loop N times**, **Loop over data**, and **While loop**.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FHp6qLW5glBYyiRkSSOoJ%252Fimage.png%3Falt%3Dmedia%26token%3D8a0aaea8-cbdc-44f4-97cb-74ec3d4b808a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=909a8e72&#x26;sv=2" alt="Loop component with loop type selection and data mapping options"><figcaption></figcaption></figure>

> You can select the Loop Type and the Data you want to loop over, mapping it from previous flow steps.

* **Loop N times**: Run a block a fixed number of times.
* **Loop over data**: Iterate through each item in a list.
* **While loop**: Keep looping as long as a condition is true.

Use **End Loop** to mark where the loop finishes.

In the example shown, the **Loop Type** is set to _Loop over data,_ and the **Loop Data** field is mapped from a previous step:

```
{{steps.sendMessage.output.message.blocks}}
```

This means the loop will go through each `block` inside the `message` output from the `sendMessage` step, allowing you to process every block one by one.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FoOe0bAvfenYGPkENLvTj%252Fimage.png%3Falt%3Dmedia%26token%3Dd5e58cec-56b6-463e-9952-e659c4317f8d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=2ac136ef&#x26;sv=2" alt="Loop configured to iterate over sendMessage output blocks from a previous step"><figcaption></figcaption></figure>
