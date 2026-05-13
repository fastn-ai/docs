---
description: >-
  Power your flows with intelligence; choose between full agent logic or quick
  single-step actions.
---

# AI Agent & AI Action in Flows

* When you log in through [live.fastn.ai](https://live.fastn.ai) into your Fastn account, navigate to **Flows** and create a new flow by clicking on **Create Flow.**

<figure><img src="../../../../.gitbook/assets/image (297).png" alt="Fastn Flows page with the Create Flow button"><figcaption></figcaption></figure>

## Building your AI Agent On Chat Request

* Select the starting point for your flow. For example, if you want to build your AI agent in **Fastn** through chat message, select **On Chat message**, name your flow, and click on **Build** to start.

<figure><img src="../../../../.gitbook/assets/image (260).png" alt="Flow starting point selection with On Chat message option highlighted"><figcaption></figcaption></figure>

* Click on the **"+"** symbol within your Flow canvas.
* In the component search bar, type **“AI Agent”** and select it.
* In the AI model section, select an AI model of your choice.
* Next, from the **model dropdown**, choose the AI model best suited for your use case (e.g., **Gemini 2.0**).
* Under the **Prompt** section, define the input the agent should use, for example:\
  `{{input.chatInput}}`
* Adjust your **Session ID**, **Memory Table Name,** and **Memory Content Limit** as required.
* Click **Save** to confirm your configuration.

{% hint style="info" %}
The Fastn AI Agent is in the beta category and under trial.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (261).png" alt="AI Agent configuration panel with model selection, prompt input, and memory settings"><figcaption></figcaption></figure>

* You will now need to get into the loop of your connected AI Agent to select your apps to connect and set up necessary actions.
* Select your desired app by searching for it in the **Connector** and connecting your account.

### Example Use Case: Fetching Your Contacts From Intercom

* Select the **Intercom** Connector and endpoint **Get Contacts** in this case, and click **Next.**

<figure><img src="../../../../.gitbook/assets/image (153).png" alt="Intercom connector selected with Get Contacts endpoint"><figcaption></figcaption></figure>

* In the next **Connect** section, connect your Intercom account to **Fastn**. Configure your action in the next step, and you will then see the Get Contacts action connected in your Flow.

<figure><img src="../../../../.gitbook/assets/image (152).png" alt="Get Contacts action connected in the AI Agent flow canvas"><figcaption></figcaption></figure>

{% hint style="info" %}
Inside each connected tool, you can add or delete individual parameters and map them to input values that are static or defined automatically by the model, as shown below. You can learn more about data mapping from [data-mapping-in-flows.md](data-mapping-in-flows.md "mention")
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (155).png" alt="Tool parameter configuration with mapped input values inside the connected connector"><figcaption></figcaption></figure>

* Go to the **Chat** option in the top-right corner of the screen.

<figure><img src="../../../../.gitbook/assets/image (151).png" alt="Chat option button in the top-right corner of the flow editor screen"><figcaption></figcaption></figure>

* Type the prompt you want to execute.

```
“Get my last 5 contacts from Intercom”
```

* The chatbot will process your request. You’ll receive the result showing the contacts along with details such as when each contact was created.

<figure><img src="../../../../.gitbook/assets/image (149).png" alt="Chat response showing retrieved Intercom contacts with creation date details"><figcaption></figcaption></figure>

## AI Action

AI Action is your tool in Fastn to trigger action in your connected apps based on a single prompt without any model selection or complex flows.

### Building your AI Action on API Request

* Select the starting point for your flow. For example, if you want to trigger any task in **Fastn** through an API request for seamless system integration, select **On API Request**, name your flow, and click on **Build** to start.

<figure><img src="../../../../.gitbook/assets/image (236).png" alt="Flow starting point selection with On API Request option highlighted"><figcaption></figcaption></figure>

* Inside the flow search and add the AI Action flow component.

<figure><img src="../../../../.gitbook/assets/image (235).png" alt="Adding the AI Action component from the flow component search bar"><figcaption></figcaption></figure>

* In the AI Action connector, click on **Add Actions** to select relevant apps for connection and to update the necessary actions \[functionalities] for your task.

<figure><img src="../../../../.gitbook/assets/image (237).png" alt="AI Action connector panel with Add Actions button for selecting apps"><figcaption></figcaption></figure>

### Example Use Case: Sending a Message to your Slack Channel

* Search for the Slack Connector and enable the Send Message Action after authenticating your Slack account.

{% hint style="info" %}
Your connector will appear as **Connected** after successful authentication.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (238).png" alt="Slack connector with Send Message action enabled and account connected"><figcaption></figcaption></figure>

* You can now write a simple prompt with the message you want to send with the Channel Name e.g,

```
"Send a message test to Slack Channel ai_testing"
```

* Click **Save** and test run your flow by clicking **Test** from the top-right corner.

{% hint style="info" %}
You can deploy the flow to any of your selected environments to go LIVE.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (239).png" alt="AI Action flow with prompt configuration and Test button in the top-right corner"><figcaption></figcaption></figure>

* You will now see your flow ran successfully and the message would be sent to the respective Slack channel.

<figure><img src="../../../../.gitbook/assets/image (241).png" alt="Successful flow execution result showing the Slack message was sent"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (240).png" alt="Slack channel displaying the test message sent by the AI Action flow"><figcaption></figcaption></figure>
