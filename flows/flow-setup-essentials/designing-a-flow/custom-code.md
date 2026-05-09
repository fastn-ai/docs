---
description: >-
  Write custom logic in JavaScript, Python, or C# inside your Fastn flow.
  Handle advanced data processing that standard automation components cannot cover.
---

# Write custom code in Fastn flows

Write your own logic inside the flow using supported programming languages such as **JavaScript, Python Lambda, or C#**. This step is useful when you need more control, advanced data handling, or custom logic that cannot be achieved with standard components.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FW4LojehxvRb903r8X4XV%252Fimage.png%3Falt%3Dmedia%26token%3D35c52fa1-8758-4672-a870-f2f2d5d760ed&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=20a0254c&#x26;sv=2" alt="Custom Code component in the flow editor with language selection options"><figcaption></figcaption></figure>

**Example (C# Custom Code)**

For example, if you need to add a **Custom Code** step in your flow, you can write a function that processes the data coming from previous steps and returns the output you want to use later. In the example below, the function is written in **C#**.

It takes the flow data as input, extracts the `steps` object (which contains outputs from earlier steps), deserializes it into a dictionary, and then returns it. This allows you to handle the step data programmatically inside your flow and make it available for the next steps.

> This example shows how you can configure the **Custom Code** step in **C#**, but the same component also works with **JavaScript** or **Python Lambda**, depending on your preference.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FiI3cHs5kUxWWn0JSLuW6%252Fimage.png%3Falt%3Dmedia%26token%3Df887a3fd-02a4-4815-ae2e-959919ecf544&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=21e60540&#x26;sv=2" alt="Example C# custom code step processing flow data and deserializing step outputs"><figcaption></figcaption></figure>

{% hint style="info" %}
To make this easier, the AI agent in the top right corner provides smart suggestions about the code.
{% endhint %}
