---
description: >-
  Use this guide to build a widget in Fastn that allows users to authenticate
  with Google Drive, configure file selection, and schedule automated syncs to
  Google Cloud Storage (GCS).
---

# Setting Up a Google Drive to GCS Migration - Widget

## Setting Up Flows for the Widget

Each of these flows corresponds to an action button or event from your Google Drive widget. You can define steps inside the flow that should be triggered when the respective action occurs.

### Activation Flow

This flow will be triggered by the activation button in your widget for Google Drive. You can return a success message from flow components or add any additional steps in this flow that you want to be triggered when your connector is activated.

**Steps:**

* In this case, we simply return a static success message like:\
  `"Activation successful for {{input.source}}"`

<figure><img src="../../../.gitbook/assets/image (204).png" alt=""><figcaption></figcaption></figure>

### Deactivation Flow

This flow handles deactivation logic, such as deleting registered webhooks.

**Steps:**

* **Initialize Flow Variables:**

The deactivation flow begins with initializing the variables `webhookIds` and `tenantId`. The `webhookIds` have a value of `{{input.source}}`, while `tenantId` is obtained from the request headers as `headers['x-fastn-space-tenantid']`.

<figure><img src="../../../.gitbook/assets/image (205).png" alt=""><figcaption></figcaption></figure>

2. **Loop over Webhook IDs:**

* Use a Loop step to iterate over `webhookIds`

<figure><img src="../../../.gitbook/assets/image (206).png" alt=""><figcaption></figcaption></figure>

* Inside the loop, add a `Delete Webhook` step that deletes each of the webhooks fetched through there IDs as long as the flow runs.

<figure><img src="../../../.gitbook/assets/image (207).png" alt=""><figcaption></figcaption></figure>

3. **Return Success Message:**

* After the loop, return a success message like:\
  `"Deactivation completed for {{tenantId}}"`

### Configuration Flow (driveConfigFlow)

This flow is used to prepopulate options for user configuration in the widget, such as choosing files and sync frequency.

**Steps:**

*   **Map Data:**

    * Maps values for:

    `files`: List of available files

    <figure><img src="../../../.gitbook/assets/image (209).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
In the **mapping step**, users can click the three dots next to fields like **Files** and **Sync Frequency** to access **Configuration Field Options**.
{% endhint %}

For both **Files** and **Sync Frequency**, users can configure settings like setting a label, hiding the field in the config pop-up or based on the config Field.

<figure><img src="../../../.gitbook/assets/image (495).png" alt=""><figcaption></figcaption></figure>

In the **Selections** section for **Files**, you can:

* Enable or disable Selection
* Set the Selection Type as Custom, Static, or Dynamic
* Choose the Selector for your Widget

<figure><img src="../../../.gitbook/assets/image (496).png" alt=""><figcaption></figcaption></figure>

* **Map Schedule:**

`syncFrequency`: Frequency options (daily, hourly, etc.)

<figure><img src="../../../.gitbook/assets/image (208).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
`syncFrequency` is an object with dropdown values, left empty in the flow initially and populates dynamically.
{% endhint %}

In the **Selections** section for **Sync Frequency**, you can:

* Set the Selection Type as Custom, Static, or Dynamic
* Enable or disable Selection
* Option Items for your drop-down of Sync Frequency in the Widget with the value for each sync and its respective label

<figure><img src="../../../.gitbook/assets/image (498).png" alt=""><figcaption></figcaption></figure>

### Sync Flow Breakdown (activate)

The sync flow fetches selected files from Google Drive and migrates them to a specified Google Cloud Storage (GCS) bucket. It handles file processing, formatting, and storage while respecting user-configured preferences.

* **Initialize flow variables**

<figure><img src="../../../.gitbook/assets/image (488).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (489).png" alt=""><figcaption></figcaption></figure>

* **Switch**

In the switch statement, the Data Mapper:

* Takes values from the respective config flow
* Initializes a sync-specific variable based on flow output
* If the connector is Google Drive:
  * Calls `driveConfigFlow` for schedule info

<figure><img src="../../../.gitbook/assets/image (490).png" alt=""><figcaption></figcaption></figure>

* If Redshift:
  * Calls `RedShiftconfigflow` for schedule info

<figure><img src="../../../.gitbook/assets/image (491).png" alt=""><figcaption></figcaption></figure>

* **Initializing Flow Variables**

In the next step, variables are initialized for both Drive and Redshift mapped outputs respectively.

<figure><img src="../../../.gitbook/assets/image (202).png" alt=""><figcaption></figcaption></figure>

* Else:
  * Ends the flow
* **Parse Sync Frequency**

<figure><img src="../../../.gitbook/assets/image (200).png" alt=""><figcaption></figcaption></figure>

* A JavaScript step (`parseSyncFrequency`) extracts and formats frequency info

```
function handler(params) {
  const frequencyString = params.data.var.configs.syncFrequency.value;
  const [rate, ...unitParts] = frequencyString.split(" ");
  const unitTime = unitParts.join(" ");

  return {
    rate: rate,
    unitTime: unitTime.trim()
  };
}
```

* **Switch**
  * If tenant doesn’t exist → return error
  * Else → proceed to Loop Over Templates

<figure><img src="../../../.gitbook/assets/image (492).png" alt=""><figcaption></figcaption></figure>

* **Loop Over Templates**
  * Fetches APIs for each project ID involved

<figure><img src="../../../.gitbook/assets/image (493).png" alt=""><figcaption></figcaption></figure>

* **Loop Over Webhooks**
  * If webhooks exist:
    * Fetch scheduler values
  * If not:
    * Create webhooks using:
      * `projectID` in headers
      * `unitRate` and `unitTime` from `parseSyncFrequency`

<figure><img src="../../../.gitbook/assets/image (494).png" alt=""><figcaption></figcaption></figure>

* The flow returns **Success Message** after successful execution.

## Widget Setup Overview

You'll create a Fastn widget with **Google Drive** as the dependency connector.\
The widget will support the following actions:

* **Connect:** Activates and authenticates the widget
* **Disconnect:** Deactivates the connection
* **Configure:** Allows file selection from Drive
* **Sync:** Schedules and runs the migration

<figure><img src="../../../.gitbook/assets/image (486).png" alt=""><figcaption></figcaption></figure>

### 1. Connect Action

* **Visibility**: Pre-Auth
* **Flow Triggered**: [Activator](setting-up-a-google-drive-to-gcs-migration-widget.md#activation-flow)
* **Behavior**:
  * This is the first action users will see.
  * The flow prepares the widget for authentication.
  * Once activated, users authenticate their Google account to connect.

### 2. Disconnect Action

* **Visibility**: Post-Auth
* **Flow Triggered**: [deactivate](setting-up-a-google-drive-to-gcs-migration-widget.md#deactivation-flow)
* **Behavior**:
  * Lets users disconnect their Google Drive from the widget.
  * This action deactivates the widget and clears any saved data or context.

### 3. Configure Action

* **Visibility**: Post-Auth
* **Flow Triggered**: [driveConfigFlow](setting-up-a-google-drive-to-gcs-migration-widget.md#configuration-flow-driveconfigflow)
* **Behavior**:
  * Appears once the user has connected their Google account.
  * Allows the user to select files or folders from their Drive.
  * Stores this configuration for the sync process.

{% hint style="info" %}
This button is not visible Pre-Auth.
{% endhint %}

### 4. Sync Action

* **Visibility**: Post-auth and post-config
* **Flow Triggered**: [activate](setting-up-a-google-drive-to-gcs-migration-widget.md#sync-flow-breakdown-activate)

The Sync Action also takes the [drive\_to\_gcs](setting-up-a-google-drive-to-gcs-migration-flow.md) flow as a source input in Payload.

```
{
  "source": "drive_to_gcs"
}
```

* **Behavior**:
  * Starts the migration process based on the Drive config.
  * Triggers a structured flow with logic for both Google Drive and Redshift cases.

## User Experience in the Widget

* User sees the **Connect** button → clicks to authenticate with Google

<figure><img src="../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

* On success, **Disconnect** and **Configure** buttons appear.

<figure><img src="../../../.gitbook/assets/image (3) (2).png" alt=""><figcaption></figcaption></figure>

* User clicks **Configure** to:
  * Browse through Google Drive and select source files.

<figure><img src="../../../.gitbook/assets/image (104).png" alt=""><figcaption></figcaption></figure>

* User selects sync frequency from the dropdown.

<figure><img src="../../../.gitbook/assets/image (5) (2).png" alt=""><figcaption></figcaption></figure>

* User will now be able to see the **Sync** button, which you can use to start a scheduled migration to GCS.

<figure><img src="../../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

* The **Disconnect** button allows you to disconnect your Widget.

## Final Outcome

Once set up, this Fastn widget gives your users a seamless experience to:

* Connect their Google Drive
* Configure what to sync
* Schedule automated migrations
* Push selected data to Google Cloud Storage reliably
