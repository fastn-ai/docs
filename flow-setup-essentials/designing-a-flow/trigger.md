---
description: Initiate a flow whenever a specific event occurs in a connected app
---

# Trigger

The **Trigger** component starts your flow automatically when a specific event occurs in a connected app — such as a new message in Slack, a form submission, or a record update in a CRM. Use it when you want your automation to run in response to real-time activity rather than on a manual or scheduled basis.

<figure><img src="../../../../.gitbook/assets/image (53).png" alt="Trigger component in the Fastn flow editor canvas"><figcaption></figcaption></figure>

* You can add this component by searching for **Trigger** in your flow. Once added, you’ll first need to **select an app** from the available list or search for the required one.

<figure><img src="../../../../.gitbook/assets/image (54).png" alt="App selection panel showing available apps for the Trigger component"><figcaption></figcaption></figure>

* After selecting the app, connect and authenticate your account to enable access.

<figure><img src="../../../../.gitbook/assets/image (56).png" alt="Account authentication dialog for connecting an app to the Trigger"><figcaption></figcaption></figure>

* After saving, the Trigger will automatically listen for the selected event.

{% hint style="info" %}
Based on the selected app, a list of **Trigger events** will appear.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (62).png" alt="List of available trigger events for the selected app"><figcaption></figcaption></figure>

> In the case of Slack, when a message is posted in the specified channel, the trigger will activate and send a message from Fastn to that channel.

* Next, select the **account ID** associated with the connection, for example, _Fastn_.
* In the **Headers** section, add the required key–value pairs for authentication or configuration. Once you’ve entered all details, click **Save** to finalize this step.

<figure><img src="../../../../.gitbook/assets/image (59).png" alt="Trigger configuration panel with account ID selection and headers key-value pairs"><figcaption></figcaption></figure>

* You can choose the event that should start your flow. For example, when integrating with Slack, you can select the **Message Posted** trigger event.

<figure><img src="../../../../.gitbook/assets/image (60).png" alt="Selecting the Message Posted trigger event for Slack integration"><figcaption></figcaption></figure>

* You can test this step by clicking the **Test** button in the top right corner.

> The console will display the result, and you’ll see the message sent to your selected Slack channel.

<figure><img src="../../../../.gitbook/assets/image (61).png" alt="Test results in the console showing the Slack trigger response"><figcaption></figcaption></figure>
