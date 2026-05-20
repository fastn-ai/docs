---
description: >-
  Learn how to build and configure interactive widgets in Fastn to connect apps,
  control actions, and deploy them seamlessly for end-users.
---

# Building and Configuring Widgets in Fastn

Widgets are the user-facing building blocks of Fastn's embedded integration experience. Each widget represents a single connector (such as Slack, HubSpot, or PostgreSQL) and exposes actions that your end-users trigger from inside your application. The following sections cover every part of the widget editor so you can configure widgets precisely.

## 1. Add a new widget

<figure><img src="../../../.gitbook/assets/widgets.gif" alt=""><figcaption></figcaption></figure>

1. Click **Widgets** in the left sidebar to open the Widgets page.
2. Click the **Add Widget** button at the top-right corner.
3.  Choose whether to publish the widget **with or without a connector**.

    * **With a connector/Publish Connector** — the widget is linked to a specific connector and can manage authentication and actions for that service.

    <figure><img src="../../../.gitbook/assets/widget - with connector.gif" alt=""><figcaption></figcaption></figure>

    * **Without a connector** — creates a standalone widget you can attach flows to without tying it to a single connector.

    <figure><img src="../../../.gitbook/assets/widget- without connector.gif" alt=""><figcaption></figcaption></figure>
4. **Search and select** the connector the widget should handle.

{% hint style="info" %}
You can pick from **Fastn's built-in connectors** or connectors from **your own workspace**.
{% endhint %}

## 2. Configure widget settings

After you create a widget, the widget editor opens. It contains the following fields.

<figure><img src="../../../.gitbook/assets/widget editor.png" alt=""><figcaption></figcaption></figure>

### Name and branding

These fields control how the widget appears to end-users in the embedded integration hub.

| Field               | Description                                                                                                                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name** (required) | Display name shown to end-users (for example, "Google Drive" or "HubSpot CRM").                                                                                                                |
| **Images**          | Connector icon or logo URLs displayed on the widget card. You can add multiple images and assign each a theme variant (for example, Default, Light, Dark) using the dropdown next to each URL. |
| **Description**     | Short summary of what the integration does. Appears below the widget name in the hub.                                                                                                          |

### Settings

The **Settings** panel on the right side of the widget editor contains the following toggles and buttons:

#### Enable for specific tenants

Toggle this to restrict which tenants can see the widget. When enabled, click **Add tenants** to select the tenant IDs that should have access. All other tenants will not see the widget. Leave this toggle off to make the widget available to every tenant.

#### Enable Widget history Logs

Toggle this to show history logs within the widget. When enabled, end-users can view a log of past actions and events for the integration.

#### Disable

Toggle **Disable** to hide the widget from end-users without deleting it. When disabled, the widget does not appear in the integration hub. Select a **Data Flow Label** from the dropdown to categorize the widget. Disabled widgets remain fully configured — turn off the toggle to restore visibility.

#### Enable Multi Connection

Toggle this to allow multiple connections for different tenants. When enabled, each tenant can establish their own independent connection to the external service through this widget.

The Settings panel also includes:

* **Add metrics** — configure metrics that display on the widget card (for example, sync counts or status indicators).
* **Localization** — configure localized content for the widget.

### Set dependency connectors

If your widget relies on one or more external services for authentication, specify them under **Dependency Connectors**. A dependency connector represents a service your end-users must authenticate with before the widget's actions can run.

<figure><img src="../../../.gitbook/assets/dependency connector.gif" alt=""><figcaption></figcaption></figure>

For each dependency connector you add, configure the following:

| Field           | Description                                                                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**        | Connector display name (for example, "Slack").                                                                                                                |
| **Image URL**   | Icon URL for the connector.                                                                                                                                   |
| **Description** | Brief description of what this connector enables.                                                                                                             |
| **Primary**     | Mark one connector as **Primary** when the widget has multiple dependencies. The primary connector determines the main authentication prompt users see first. |

#### Auth attributes

Click the **Auth Attributes** link on a dependency connector to open the **Custom Auth Attributes** dialog. This dialog lets you configure how end-users authenticate with the external service.

**Default Auth Method** — select the primary authentication method from the dropdown:

| Method              | When to use                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------- |
| **OAuth** (default) | The connector supports OAuth 2.0/2.1. Fastn handles the full token lifecycle.                                 |
| **Custom Input**    | The connector requires custom fields your end-user fills in (for example, a workspace URL plus an API token). |
| **API Key**         | Authentication uses a single API key passed in a header.                                                      |
| **Bearer Token**    | Authentication uses a bearer token in the `Authorization` header.                                             |
| **Basic Auth**      | Authentication uses a username and password combination.                                                      |

**Allow switching auth method** — enable this toggle to let end-users switch between authentication methods (for example, choosing between OAuth and API key).

The dialog includes a JSON editor where you can override the default OAuth attributes. These values are merged with the connector's default settings:

```json
{
  "clientId": "",
  "clientSecret": "",
  "params": {
    "scope": ""
  }
}
```

{% hint style="warning" %}
When using custom OAuth credentials, add `https://oauth.live.fastn.ai` as the **Redirect URL** in your developer app for the external service.
{% endhint %}

## 3. Add actions to the widget

Actions are the buttons your end-users interact with on the widget card. Each action triggers a Fastn flow and controls a specific part of the integration lifecycle.

Click **"Add"** under **Actions** to create a new action row.

<figure><img src="../../../.gitbook/assets/actions for widgets.gif" alt=""><figcaption></figcaption></figure>

### Actions table reference

Each action row has four columns:

| Column              | Description                                                                                                                                                     |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name** (required) | The button label end-users see (for example, "Connect", "Disconnect", "Configure", "Sync").                                                                     |
| **Flow**            | The Fastn flow that runs when the user clicks this action. Select an existing flow from the dropdown.                                                           |
| **Visibility**      | Controls **when** this action button appears to the user. See [Action visibility](building-and-configuring-widgets-in-fastn.md#action-visibility) for details.  |
| **Action**          | Defines **what category** of lifecycle event this action represents. See [Action types](building-and-configuring-widgets-in-fastn.md#action-types) for details. |

Click the expand arrow (chevron) on an action row to reveal additional settings, including the **Flow Payload** — an optional JSON object passed to the flow at runtime. See [Flow payload](building-and-configuring-widgets-in-fastn.md#flow-payload) for details.

{% hint style="info" %}
You can use the built-in **Activate**, **Deactivate**, and **Configure** flow templates instead of creating flows from scratch. Go to the **Flows** section and click **Templates** to import them.
{% endhint %}

### Action visibility

Visibility determines at which stage of the user journey an action button appears on the widget. Choose the option that matches the user's current authentication and configuration state.

| Visibility                     | Button appears when                                                             | Typical use case                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Always**                     | The button is visible **regardless** of authentication or configuration state.  | Informational actions, help links, or actions that handle their own auth checks.                    |
| **Pre-Auth**                   | The user has **not yet authenticated** with the dependency connector.           | A "Connect" button that initiates the OAuth flow.                                                   |
| **Post-Auth**                  | The user **has authenticated** (regardless of configuration state).             | "Disconnect" or "Configure" buttons that only make sense after the user is connected.               |
| **Post-Auth & Configured**     | The user **has authenticated and completed configuration**.                     | A "Sync" or "Run" button that requires both a live connection and saved settings.                   |
| **Pre-Auth & Configured**      | The user has **not yet authenticated** but **has completed configuration**.     | Actions that need configuration before auth (for example, selecting a workspace before connecting). |
| **Post-Auth & Not Configured** | The user **has authenticated** but has **not yet completed configuration**.     | A "Configure" button shown right after first connection, hidden once settings are saved.            |
| **Pre-Auth & Not Configured**  | The user has **not yet authenticated** and has **not completed configuration**. | A first-time setup button visible only in the initial unconfigured, unauthenticated state.          |

#### Choosing the right visibility

Use the decision tree below to select the correct visibility for each action:

```
Should the button always be visible?
├── Yes → Always
└── No
    ├── Should it show BEFORE or AFTER auth?
    │   ├── Before auth (Pre-Auth)
    │   │   └── Does configuration state matter?
    │   │       ├── No → Pre-Auth
    │   │       ├── Only if configured → Pre-Auth & Configured
    │   │       └── Only if not configured → Pre-Auth & Not Configured
    │   └── After auth (Post-Auth)
    │       └── Does configuration state matter?
    │           ├── No → Post-Auth
    │           ├── Only if configured → Post-Auth & Configured
    │           └── Only if not configured → Post-Auth & Not Configured
```

**Example — a migration widget with four actions:**

| Action     | Visibility                 | Why                                                                                      |
| ---------- | -------------------------- | ---------------------------------------------------------------------------------------- |
| Connect    | Pre-Auth                   | Users must see this before they authenticate. It initiates the OAuth flow.               |
| Disconnect | Post-Auth                  | Only relevant after the user has an active connection.                                   |
| Configure  | Post-Auth & Not Configured | Appears right after the user connects, hidden once configuration is saved.               |
| Sync       | Post-Auth & Configured     | Requires both an authenticated connection and completed configuration before it can run. |

### Action types

The action type tells Fastn what lifecycle event the action represents. This controls how the platform tracks connector state and determines which built-in behaviors apply.

| Action type         | What it does                                                                                                                                                                                             | When to use                                                                                                                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Activation**      | Transitions the integration into an **active** state. The platform marks the connector as connected and updates the widget UI accordingly (for example, switching the card to an "active" visual state). | For your primary "Connect" or "Activate" action — the action that establishes the integration.                                                                                                                                                                                                           |
| **Configuration**   | Opens a **form or input dialog** defined by the linked configuration flow. Does not change the connector's active/inactive state.                                                                        | For "Configure" or "Settings" actions that let users customize integration behavior (for example, selecting sync frequency, choosing folders, or mapping fields).                                                                                                                                        |
| **Deactivation**    | Transitions the integration into an **inactive** state. The platform marks the connector as disconnected, clears session data, and resets the widget UI to its pre-auth state.                           | For "Disconnect" or "Deactivate" actions that tear down the integration.                                                                                                                                                                                                                                 |
| **Multi Connector** | Handles actions that span **multiple dependency connectors** at once. Allows the flow to interact with several connected services in a single action.                                                    | For actions that require coordinating across multiple connectors (for example, syncing data between two services simultaneously). See [Managing multiple app connections together](../../../tutorials/flow-customization-and-operations/how-to-manage-multiple-app-connections-together.md) for details. |
| **None**            | Runs the linked flow **without affecting** the connector's lifecycle state. No activation, deactivation, or configuration behavior is triggered.                                                         | For custom actions that run a flow but do not change the widget's connection state (for example, a "Sync Now" or "Test Connection" button).                                                                                                                                                              |

{% hint style="info" %}
Each widget typically has **one Activation action**, **one Deactivation action**, and **one or more Configuration actions**. Use **Multi Connector** when the widget bundles multiple services, and **None** for utility actions that do not change connector state.
{% endhint %}

#### Built-in flow templates

Fastn provides pre-built flow templates for each action type. Import them from the **Templates** section in Flows:

**Activate flow** — runs when the user triggers an Activation action. It prepares the connector, initiates authentication, and marks the integration as active.

<figure><img src="../../../.gitbook/assets/image (257).png" alt="Activate flow template in the Fastn flow editor for enabling a connected app integration"><figcaption></figcaption></figure>

**Deactivate flow** — runs when the user triggers a Deactivation action. It cleans up resources, revokes tokens if needed, and marks the integration as inactive.

<figure><img src="../../../.gitbook/assets/image (256).png" alt="Deactivate flow template in the Fastn flow editor for disabling a connected app integration"><figcaption></figcaption></figure>

**Configure flow** — runs when the user triggers a Configuration action. It renders a form based on the fields you define in the flow and stores the user's selections.

<figure><img src="../../../.gitbook/assets/image (258).png" alt="Configure flow template in the Fastn flow editor for managing connected app settings"><figcaption></figcaption></figure>

{% hint style="info" %}
Configuration flows must also be linked in **Settings > Configurations** for the widget to display configuration options. See [How to set up a configuration flow](../../../tutorials/understanding-flow-types/how-to-set-up-a-configuration-flow-in-fastn/) for details.
{% endhint %}

### Flow payload

The **Flow Payload** field accepts a JSON object that is passed to the action's flow at runtime. Use it to provide static parameters, source references, or context the flow needs to execute correctly.

For example, a Sync action that triggers a migration flow might include:

```json
{
  "source": "drive_to_gcs"
}
```

This tells the flow which migration pipeline to run without hardcoding it inside the flow definition. You can include any valid JSON — the payload is forwarded as-is to the flow's input.

## 4. Deploy to live

After you complete all actions and configurations:

* Click the **Deploy to LIVE** button at the bottom to deploy the widget to your selected environment. This deploys all connected flows to your live environment and makes the widget available to end-users.
* Open **Preview** from the **Integrate** section on the **Widgets** page to verify how the widget appears to end-users.

<figure><img src="../../../.gitbook/assets/deploy to live + preview.gif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Preview always shows the **DRAFT** version of the widget. Use the `env` query parameter to preview a specific deployed environment.
{% endhint %}

## Next steps

* [Previewing and integrating widgets](previewing-and-integrating-widgets.md) — embed widgets via iframe or the headless React package
* [How to set up an activation flow](../../../tutorials/understanding-flow-types/how-to-set-up-an-activation-flow.md) — build a custom activation flow from scratch
* [How to set up a configuration flow](../../../tutorials/understanding-flow-types/how-to-set-up-a-configuration-flow-in-fastn/) — define form fields for widget configuration
* [Fixed vs dynamic connections](../../../flow-setup-essentials/connecting-apps/fixed-vs-dynamic-connections.md) — understand when widgets are required for tenant authentication
* [Setting up a Google Drive to GCS migration widget](../../../tutorials/data-migrations/setting-up-a-google-drive-to-gcs-migration-widget.md) — end-to-end example with Pre-Auth, Post-Auth, and Post-Auth & Configured visibility
