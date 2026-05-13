---
description: >-
  In this guide, you’ll learn how to use UCL's Playground for AI Assistant to
  assign Jira tasks with natural language; no integration code needed.
---

# Connect UCL for task Assignment in Jira

{% hint style="info" %}
UCL's Playground is the overview of how your AI agent will work with integrated Connectors and Actions (Tools) through UCL.
{% endhint %}

### Connect your Jira account to UCL

For this use case, we need to connect the Jira App with the Assign Issue Action.

> You can select any app by checking the top-right box on the app and click on **Select Tools** to modify your action selection and then finalize this setup by clicking the **Confirm Action** button in the right-bottom.

<figure><img src="../../../../../.gitbook/assets/image (609).png" alt=""><figcaption></figcaption></figure>

* You need to authenticate your Jira account, after which the Jira App will appear as **Connected**.
* From Select Tools, you can enable the **Assign Issue** Action.

> ⚠️ You may need to be a Jira project admin or have the right permissions to link your account successfully.

<figure><img src="../../../../../.gitbook/assets/image (606).png" alt=""><figcaption></figcaption></figure>

You will now see Jira along with other selected apps in your dashboard.

<figure><img src="../../../../../.gitbook/assets/image (607).png" alt=""><figcaption></figcaption></figure>

### **Use UCL’s Playground to Perform Actions**

You can use the **Playground** (from the three-dot menu, top-right) in your dashboard to test all your connected apps.

<figure><img src="../../../../../.gitbook/assets/image (608).png" alt=""><figcaption></figcaption></figure>

In the AI Assistant, enter the prompt describing the action you want to perform. For example:

> _Assign "Task Name" to "User's Jira ID"_

The AI Assistant will process your request using the appropriate action in the connected app, such as updating a task in Jira.

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3iSr2Tx8FvvuoLPncziH%2Fuploads%2FeJts2Cx3QfYisXlgM8C8%2F20250602-2000-08.2595966.mp4?alt=media&token=6c46e6e6-7597-40f5-88cc-245fdae9adc0" %}

Once successful, the task ownership will be updated in your Jira workspace.

<figure><img src="../../../../../.gitbook/assets/image (366).png" alt=""><figcaption></figcaption></figure>

> This setup allows you to automate and streamline task management in Jira using natural language, making workflows faster and more efficient.
