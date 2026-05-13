---
description: >-
  Learn how to preview, authenticate, and embed Fastn widgets into your apps
  using iframe or React, with options for custom auth, filtering, and connector
  overrides.
---

# Previewing and Integrating Widgets

## Previewing Widgets

* On the **Widgets** page, click the **Integrate** button.
* Click **Preview**.

<figure><img src="../../../../.gitbook/assets/image (156).png" alt="Widgets page with the Integrate button highlighted for accessing preview and embedding options"><figcaption></figcaption></figure>

*   The **Preview** button opens the widget preview in a new browser tab.\
    You can change the default `tenantId` by updating the query parameters in the URL.

    > ⚠️ The preview page always shows the **DRAFT** version of the widget.\
    > Use the `env` query parameter if you want to preview a widget that has been deployed to another environment.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfv8JkgWWaW-bIZ6w-8-cHKoo69F_owSA6DHC4JZoBQxunAB5tvwILvbXr1Kmd9l5d5zUoFx8Bjc8fVLMaXOUyERCELO-rJ4EmSYS2XgtEcPR4pUgvllB4OlEIezSh5y_n9vQxgjQ?key=U8WaqUSZtzeWDdAYuCG_tQ" alt="Widget preview page opened in a new browser tab showing the draft version of the widget"><figcaption></figcaption></figure>

## Setting up Custom Authentication

*   A custom authentication flow can be created to validate user tokens whenever the widget is loaded.

    **To enable custom authentication:**

    1. On the **Widgets** page, click **Integrate**.
    2. Go to the **Settings** tab.
    3. Enable **Custom Authentication** and click **Save**.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe80L20L4kXYOPA9MpmtvxKHtG45_HmlUCQvbzAyr7_a9uWBrQ0vC8kTF4smVkZOlm4JPdb4nSnGnHGe-yy0lEOqIjMn-RLZ55Y0GpTes-K1jmFWUt-KCSjP70XnmyPFH_GVoNUUQ?key=U8WaqUSZtzeWDdAYuCG_tQ" alt="Integrate settings tab with the Custom Authentication toggle enabled"><figcaption></figcaption></figure>

<br>

* Once saved, a flow called `fastnCustomAuth` is automatically imported into your workspace and can be customized as needed.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeBIaF46uTlS2ZvEUDUIfTwhX992eTNMO-leuFgmP44dAhYiJ4Xer9mrngkvon4SKbogQxKVjcrFTlpvz9jc5d4hYkCyTOAYXc-eiU9bWq29ae9ZcbDaVR0VRVvFRHYGcbx5jUs7g?key=U8WaqUSZtzeWDdAYuCG_tQ" alt="Fastn flow editor showing the auto-imported fastnCustomAuth flow for custom token validation"><figcaption></figcaption></figure>

By default, this flow uses a Fastn user token, but you can update it with your own logic or API calls to validate the token.

> ✅ When custom authentication is enabled, the `customAuth=true` parameter must be included in the widget URL.\
> This applies to both preview and iframe integration and ignores any `apiKey` passed in the URL.

If authentication succeeds, the widget loads normally. If it fails, an error message is displayed.

<figure><img src="../../../../.gitbook/assets/image (157).png" alt="Widget displaying an authentication error message when custom auth validation fails"><figcaption></figcaption></figure>

## Integrating Widgets in Your App

### Iframe Integration

* In the **Widgets** page, click **Integrate**.

<figure><img src="../../../../.gitbook/assets/image (158).png" alt="Widgets page showing the Integrate button for accessing iframe embedding options"><figcaption></figcaption></figure>

* Select **Iframe** to generate the React or HTML code snippet.
* Copy and paste the code into your React application.

Update the configuration values in the snippet:

```javascript
projectId: "<PROJECT_ID>", // Workspace ID where the widget is configured
tenantId: "<TENANT_ID>",   // Tenant/end user identifier
authToken: "<AUTH_TOKEN>"  // Token used in the custom auth flow
```

You can customize the default widget styling by clicking the **Styling** tab, making changes, and pressing **Save**.<br>

<figure><img src="../../../../.gitbook/assets/image (159).png" alt="Integrate panel showing the Styling tab with customizable widget appearance options"><figcaption></figcaption></figure>

### Headless React Package

The iframe approach uses Fastn’s UI and offers limited flexibility.\
For full customization, Fastn provides a **headless React package** that exposes the APIs and lets you build your own UI.

* Package: [https://www.npmjs.com/package/@fastn-ai/react-core](https://www.npmjs.com/package/@fastn-ai/react-core)
* Example App: [https://github.com/fastnai/react-core-client](https://github.com/fastnai/react-core-client)
* Live Demo: [https://react-core-client.pages.dev](https://react-core-client.pages.dev)

## Overriding Widget Connector Auth Attributes

* You can override the default auth attributes used by a widget’s dependency connector.

#### **Steps**

1. On the **Widgets** page, click the widget name to open its configuration.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXd3qrEfJaR-1ZsNirL-rSHFxsi4hyuXWIYjoqouwHpj_rjkwGN-VdKnJiYaq9gKfw8GVDBacl99JXRtdHFAtO18Dy6WaSSpeLj3TFZ6D30Rl8NuLcgi9_q4qJBIDmSMvmuU-nXYMg?key=U8WaqUSZtzeWDdAYuCG_tQ" alt=""><figcaption></figcaption></figure>

2. Under **Dependency Connectors**, click **Auth Attributes** for the connector you want to override.

<figure><img src="../../../../.gitbook/assets/image (160).png" alt=""><figcaption></figcaption></figure>

3. Enter the auth attribute overrides as JSON.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe3zVeNZOsdU0y5TXIy2ZqC0DAXza3v6N71AcU5VLvcUx6tPK2pnrq4Osk88cCZNONtMQnd98p1SsjX7qaugGy2zyCkdXpVuykslFPscyIGN4haTNtGmSt-Ntcbg9qYA1WWEcmb?key=U8WaqUSZtzeWDdAYuCG_tQ" alt=""><figcaption></figcaption></figure>

#### **Example (Slack)**

```json
{
  "clientId": "<CLIENT_ID>",
  "clientSecret": "<CLIENT_SECRET>",
  "params": {
    "scope": "app_mentions:read,channels:history,channels:join,channels:manage,channels:read,chat:write.customize,chat:write.public,chat:write,files:read,files:write,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,links:write,mpim:history,mpim:read,mpim:write,pins:read,pins:write,reactions:read,reactions:write,reminders:read,reminders:write,team:read,usergroups:read,usergroups:write,users:read,users:write,users.profile:read,users:read.email"
  }
}
```

Click **Done**, then **Update** to save.

> From this point forward, the override credentials will be used every time a tenant uses the Slack widget.

## Filtering Widgets

Fastn allows you to dynamically show or hide widgets or actions based on tenant-specific logic.

**To enable filtering:**

1. Go to **Integrate** → **Settings**.
2. Enable **Widgets Filter**.

This will import a flow called `fastnWidgetsFilter` into your workspace.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe80L20L4kXYOPA9MpmtvxKHtG45_HmlUCQvbzAyr7_a9uWBrQ0vC8kTF4smVkZOlm4JPdb4nSnGnHGe-yy0lEOqIjMn-RLZ55Y0GpTes-K1jmFWUt-KCSjP70XnmyPFH_GVoNUUQ?key=U8WaqUSZtzeWDdAYuCG_tQ" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Every time the widget page loads, the widget list is sent to this flow for processing.
{% endhint %}

### **Example Input**

```json
"widgets": [
  {
    "id": "_knexa_c9085d88-85d0-4436-82c6-4e42d6aba4c6",
    "name": "Slack",
    "hidden": false,
    "disable": false,
    "subscribed": true,
    "hideActions": [],
    "disableMessage": "",
    "subscriptionUrl": "",
    "hideActionsByName": []
  }
]
```

You can then update these configurations in the flow to reflect business logic (e.g., hide widgets for specific tenants).

### **Example Output**

```json
"widgets": [
  {
    "id": "_knexa_c9085d88-85d0-4436-82c6-4e42d6aba4c6",
    "name": "Slack",
    "hidden": true,
    "disable": false,
    "subscribed": false,
    "hideActions": [],
    "disableMessage": "",
    "subscriptionUrl": "",
    "hideActionsByName": []
  }
]
```
