---
description: >-
  Use this guide to build a widget in Fastn that allows users to authenticate
  with RedShift, configure file selection, and schedule automated syncs to
  Google Cloud Storage (GCS).
---

# Setting Up an AWS Redshift to GCS Migration - Widget

## Setting Up Flows for the Widget

Each of these flows corresponds to an action button or event from your Redshift widget. You can define steps inside the flow that should be triggered when the respective action occurs.

### Activation Flow

This flow will be triggered by the activation button in your widget for Redshift. You can return a success message from flow components or add any additional steps in this flow that you want to be triggered when your connector is activated.

**Steps:**

* In this case, we simply return a static success message like:\
  `"Activation successful for {{input.source}}"`

<figure><img src="../../../../.gitbook/assets/image (204).png" alt=""><figcaption></figcaption></figure>

### Deactivation Flow

This flow handles deactivation logic, such as deleting registered webhooks.

**Steps:**

* **Initialize Flow Variables:**

The deactivation flow begins with initializing the variables `webhookIds` and `tenantId`. The `webhookIds` have a value of `{{input.source}}`, while `tenantId` is obtained from the request headers as `headers['x-fastn-space-tenantid']`.

<figure><img src="../../../../.gitbook/assets/image (205).png" alt=""><figcaption></figcaption></figure>

2. **Loop over Webhook IDs:**

* Use a Loop step to iterate over `webhookIds`

<figure><img src="../../../../.gitbook/assets/image (206).png" alt=""><figcaption></figcaption></figure>

* Inside the loop, add a `Delete Webhook` step

<figure><img src="../../../../.gitbook/assets/image (207).png" alt=""><figcaption></figcaption></figure>

3. **Return Success Message:**

* After loop, return a success message like:\
  `"Deactivation completed for {{tenantId}}"`

### Configuration Flow

This flow is used to prepopulate options for user configuration in the widget, such as choosing files and sync frequency.

**Steps:**

*   **Map Data:**

    * Maps values for:

    `tables`: List of available tables from Redshift storage

<figure><img src="../../../../.gitbook/assets/image (196).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
In the **mapping step**, users can click the three dots next to fields like **Tables** and **Sync Frequency** to access **Configuration Field Options**.&#x20;
{% endhint %}

For both **Tables** and **Sync Frequency**, users can configure settings like setting a label, hiding the field in the config pop-up or based on the config Field.

<figure><img src="../../../../.gitbook/assets/image (495).png" alt=""><figcaption></figcaption></figure>

In the **Selections** section for **Files**, you can:

* Enable or disable Selection
* Set the Selection Type as Custom, Static, or Dynamic
* Choose the Pagination Type and limit for your data

{% hint style="info" %}
Pagination in data storage refers to the process of dividing a large dataset into smaller, more manageable "pages" for efficient retrieval and display, particularly in web applications and APIs. You can learn more about setting up Pagination with Fastn [here](../flow-customization-and-operations/how-to-set-up-pagination-in-your-flow.md).
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (199).png" alt=""><figcaption></figcaption></figure>

* **Map Schedule:**

`syncFrequency`: Frequency options (daily, hourly, etc.)

<figure><img src="../../../../.gitbook/assets/image (208).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
`syncFrequency` is an object with dropdown values, left empty in the flow initially and populates dynamically.
{% endhint %}

In the **Selections** section for **Sync Frequency**, you can:

* Set the Selection Type as Custom, Static, or Dynamic
* Enable or disable Selection
* Option Items for your drop-down of Sync Frequency in the Widget with the value for each sync and its respective label

<figure><img src="../../../../.gitbook/assets/image (498).png" alt=""><figcaption></figcaption></figure>

### Sync Flow Breakdown&#x20;

The sync flow fetches selected data from AWS Redshift and migrates them to a specified Google Cloud Storage (GCS) bucket. It handles file processing, formatting, and storage while respecting user-configured preferences. [View complete flow breakdown](setting-up-a-google-drive-to-gcs-migration-widget.md#sync-flow-breakdown-activate)

## Widget Setup Overview

You'll create a Fastn widget with **AWS Redshift** as the dependency connector.\
The widget will support the following actions:

* **Connect:** Activates and authenticates the widget
* **Disconnect:** Deactivates the connection
* **Configure:** Allows file selection from Drive
* **Sync:** Schedules and runs the migration

<figure><img src="../../../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>

### 1. Connect Action

* **Visibility**: Pre-Auth
* **Flow Triggered**: [Activator](setting-up-an-aws-redshift-to-gcs-migration-widget.md#activation-flow)
* **Behavior**:
  * This is the first action users will see.
  * The flow prepares the widget for authentication.
  * Once activated, users authenticate their AWS account to connect.

### 2. Disconnect Action

* **Visibility**: Post-Auth
* **Flow Triggered**: [deactivate](setting-up-an-aws-redshift-to-gcs-migration-widget.md#deactivation-flow)
* **Behavior**:
  * Lets users disconnect their AWS account from the widget.
  * This action deactivates the widget and clears any saved data or context.

### 3. Configure Action

* **Visibility**: Post-Auth
* **Flow Triggered**: [redshiftConfigFlow](setting-up-an-aws-redshift-to-gcs-migration-widget.md#configuration-flow)
* **Behavior**:
  * Appears once the user has connected their AWS account.
  * Allows the user to select files or folders from their Redshift.
  * Stores this configuration for the sync process.

{% hint style="info" %}
This button is not visible Pre-Auth.
{% endhint %}

### 4. Sync Action

* **Visibility**: Post-auth and post-config
* **Flow Triggered**: [activate](setting-up-an-aws-redshift-to-gcs-migration-widget.md#sync-flow-breakdown)

The Sync Action also takes the [redshift\_to\_gcs](setting-up-a-redshift-to-gcs-migration-flow.md) flow as a source input in Payload.

```
{
  "source": "redshift_to_gcs"
}
```

* **Behavior**:
  * Starts the migration process based on the Redshift config.
  * Triggers a structured flow with logic for both Google Drive and Redshift cases.

## User Experience in the Widget

* User sees the **Connect** button → clicks to authenticate with AWS.

<figure><img src="../../../../.gitbook/assets/image (198).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (192).png" alt=""><figcaption></figcaption></figure>

* On success, **Deactivate** and **Configure** buttons appear.

<figure><img src="../../../../.gitbook/assets/image (193).png" alt=""><figcaption></figcaption></figure>

* User clicks **Configure** to:
  * Browse through AWS Redshift and select source tables and enter the relevant query.

<figure><img src="../../../../.gitbook/assets/image (194).png" alt=""><figcaption></figcaption></figure>

* User selects sync frequency from dropdown.

<figure><img src="../../../../.gitbook/assets/image (195).png" alt=""><figcaption></figcaption></figure>

* User will now be able to see the **Sync** button that can be used to start a scheduled migration to GCS.
* The **Deactivate** button allows you to disconnect your Widget.

## Final Outcome

Once set up, this Fastn widget gives your users a seamless experience to:

* Connect their AWS Redshift
* Configure what to sync
* Schedule automated migrations
* Push selected data to AWS Redshift Storage reliably
