---
description: >-
  The Error Notification flow captures failures from other flows, allows you to
  customize the error message, and forwards alerts to destinations such as
  Slack, email, or databases.
---

# How to Customize Your Error Notification Flow?

When a flow fails, Fastn can automatically forward errors to a **notification flow**. By default, this is `fastnErrorNotification`. You can customize it to format error messages, enrich them with extra context, or forward alerts to external systems.

* In your flow, go to the **right-hand sidebar → Settings → Configuration**.

<figure><img src="../../../../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (128).png" alt=""><figcaption></figcaption></figure>

* Under **Error Notification**, toggle **Enable Error Notification**.

<figure><img src="../../../../.gitbook/assets/image (130).png" alt=""><figcaption></figcaption></figure>

* Open the **fastnErrorNotification** flow.

<figure><img src="../../../../.gitbook/assets/image (131).png" alt=""><figcaption></figcaption></figure>

* This flow starts with an **On API Request** trigger.
* Inside this flow, you can:
  * Map values from the incoming error.
  * Alter the error message.
  * Optionally, add any other steps as needed.

<figure><img src="../../../../.gitbook/assets/image (133).png" alt=""><figcaption></figcaption></figure>

* Save your changes.

**With this setup, you have control over how error messages are handled and displayed for your flow.**

