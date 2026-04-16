---
description: >-
  Migrate files from Google Drive to Google Cloud Storage for each tenant,
  preserving folder structures, handling Google file formats, and avoiding
  duplicate uploads based on file update timestamps.
---

# Setting Up a Google Drive to GCS Migration Flow

## **1. Start the Flow**

You can start the flow by selecting **New API Request** as the trigger.

![Flow trigger step configured with New API Request as the starting point](<../../../.gitbook/assets/image (178).png>)<br>

### Initiate Your Flow Variables

When the flow starts, the following important variables are initialized:

<figure><img src="../../../.gitbook/assets/image (180).png" alt="Flow variables initialization step with MIME handling for Docs, Sheets, Slides, and Drawings"><figcaption></figcaption></figure>

{% hint style="info" %}
You also define MIME handling for Docs, Sheets, Slides, and Drawings so that Google-native files can be exported in the correct format during migration.
{% endhint %}

***

## **2. Configure Drive and GCS Settings**

### Map Get Configs

The next step maps values from your [**DriveConfigFlow** ](setting-up-a-google-drive-to-gcs-migration-widget.md#configuration-flow-drive_to_gcs)so the flow has all required tenant and bucket details.<br>

<figure><img src="../../../.gitbook/assets/image (182).png" alt="Data mapping step pulling tenant and bucket details from DriveConfigFlow"><figcaption></figcaption></figure>

### Create Bucket for Tenant

Once these values are ready, you can use the Google Cloud Storage connector to create a **bucket for the tenant** if it doesn’t already exist.

<figure><img src="../../../.gitbook/assets/image (183).png" alt="Google Cloud Storage connector step creating a bucket for the tenant"><figcaption></figcaption></figure>

***

## **3. Set the File Path Rules**

You will then hit a **Switch** step that determines how the `filePath` variable is set:

<figure><img src="../../../.gitbook/assets/image (184).png" alt="Switch step determining how the filePath variable is set"><figcaption></figcaption></figure>

* If `baseFilePath` is provided → set `filePath` = `{{var.baseFilePath}}`

<figure><img src="../../../.gitbook/assets/image (185).png" alt="Setting filePath to baseFilePath when baseFilePath is provided"><figcaption></figcaption></figure>

* If `separateFoldersForUsers` is `true` → set `filePath` per tenant/user

<figure><img src="../../../.gitbook/assets/image (186).png" alt="Setting filePath per tenant and user when separateFoldersForUsers is true"><figcaption></figcaption></figure>

* Else → set `filePath` = `"Google Drive"`

<figure><img src="../../../.gitbook/assets/image (187).png" alt="Default case setting filePath to Google Drive"><figcaption></figcaption></figure>

From here, you move into the **Loop Over Input** step.

***

## **4. Loop Over Input Items**

<figure><img src="../../../.gitbook/assets/image (188).png" alt="Loop Over Input step iterating through the list of file IDs"><figcaption></figcaption></figure>

For each item in your incoming list of file IDs:

* Use the Google Drive connector with **getFile**
  * `File ID` = `{{steps.loopOverInput.loopOverItem.value}}`
  * `param.fields` = `id,name,mimeType,modifiedTime`

<figure><img src="../../../.gitbook/assets/image (189).png" alt="Google Drive connector getFile action configured with File ID and fields parameters"><figcaption></figcaption></figure>

* Initialize `fileObject` from `loopOverItem`

<figure><img src="../../../.gitbook/assets/image (190).png" alt="Initializing fileObject variable from the loopOverItem value"><figcaption></figcaption></figure>

* Append this file object to the `files` array using the advanced action **insertItem**.

{% hint style="info" %}
You can click the three-dots next to your variable to setup or edit the advanced action selected.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (191).png" alt="Appending file object to the files array using the insertItem advanced action"><figcaption></figcaption></figure>

***

## **5. Loop Over Files**

After the Loop Over Input ends, the next step will be a loop that runs until all files are processed.

**i. Initialize Loop Counters and Variables**

<figure><img src="../../../.gitbook/assets/image (161).png" alt="Initializing loop counters and variables for file processing"><figcaption></figcaption></figure>

* **Data Mapper:** `fileLength = arrayLength(var.files)` ; total files in the queue.

<figure><img src="../../../.gitbook/assets/image (162).png" alt="Data mapper setting fileLength to the array length of the files variable"><figcaption></figcaption></figure>

#### Switch Statement

* If no files remain, exit the loop.
*   Else, set:

    * `currentFile = {{var.files[0]}}` , the file you’ll process now.

    <figure><img src="../../../.gitbook/assets/image (163).png" alt="Setting currentFile to the first item in the files array"><figcaption></figcaption></figure>

    * Remove the first item from `var.files` using `removeItem`.

<figure><img src="../../../.gitbook/assets/image (164).png" alt="Removing the first item from the files array using removeItem action"><figcaption></figcaption></figure>

**ii. Switch Statement to Check If Current File is a Folder**

<figure><img src="../../../.gitbook/assets/image (165).png" alt="Switch step checking if the current file is a folder based on mimeType"><figcaption></figcaption></figure>

*   If `currentFile.mimeType` indicates a folder:

    *   Call **Google Drive Connector** with action to **getFilesFromFolder** with:

        * `param.q = '{{var.currentFile.file.id}}' in parents`
        * `param.fields = files(id,name,mimeType,modifiedTime)`

        <figure><img src="../../../.gitbook/assets/image (166).png" alt="Google Drive connector getFilesFromFolder action with parent ID and fields parameters"><figcaption></figcaption></figure>
    * Append each returned file to `var.files` so they’re picked up in the same loop.

    <figure><img src="../../../.gitbook/assets/image (167).png" alt="Appending folder contents to the files array for processing in the loop"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (168).png" alt="Loop configuration for processing files within a folder"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (169).png" alt="Variable mapping for folder file insertion into the processing queue"><figcaption></figcaption></figure>

**Non-Folder Files**

* Build a **state key** for this file:

<figure><img src="../../../.gitbook/assets/image (170).png" alt="Building a state key for the current file to track processing status"><figcaption></figcaption></figure>

*   **Read State** for `stateKey` to check if the file is already processed or unchanged.

    <figure><img src="../../../.gitbook/assets/image (172).png" alt="Reading state for stateKey to check if the file was already processed"><figcaption></figcaption></figure>

#### iii. Switch Step to Check if Files are Updated

Next Step is a switch statement that checks if files are updated, and ends the flow if there is no update.

<figure><img src="../../../.gitbook/assets/image (173).png" alt="Switch step checking if files have been updated since last processing"><figcaption></figcaption></figure>

If the file is updated,

* Run **gettingMimeType** JS step → detect MIME type and extension.

```
function handler(params) {
  const mimeTypes = params?.data.var.mimeTypes;
  const fileMimeTypes = params?.data.var.currentFile.file.metadata?.mimeType;

  for (let i = 0; i < mimeTypes.length; i++) {
    if (mimeTypes[i].googleMimeType === fileMimeTypes) {
      return {
        mimeType: mimeTypes[i].exportableMimeTypes,
        extension: mimeTypes[i].exportablExtension
      };
    }
  }
```

* Run **preparingParams** JS step → prepare download/export URLs.

```
function handler(params) {
  const fileId = params?.data.var.currentFile.file.value;
  let fileNamePrefix = '';
  if (params?.data.input.overrideFiles === false) {
    fileNamePrefix = Date.now() + '_';
  }

  return {
    googleUrl: 'https://www.googleapis.com/drive/v3/files/' + fileId + '/export?mimeType=' + params?.data.steps.gettingMimeType.output.mimeType,
    nonGoogleUrl: 'https://www.googleapis.com/drive/v3/files/' + fileId + '?alt=media',
    fileNamePrefix
  };
}
```

* Get access token from **Fastn Connector** using the action **getConnectorToken**.

<figure><img src="../../../.gitbook/assets/image (174).png" alt="Fastn connector getConnectorToken action retrieving an access token"><figcaption></figcaption></figure>

**iv. Decide How to Download (Switch Step)**

<figure><img src="../../../.gitbook/assets/image (499).png" alt="Switch step deciding download method based on Google-native or non-Google file type"><figcaption></figcaption></figure>

*   **If Google-native file (Docs, Sheets, Slides, Drawings):**

    <figure><img src="../../../.gitbook/assets/image (500).png" alt="Configuration for downloading Google-native files like Docs, Sheets, and Slides"><figcaption></figcaption></figure>
*   **Else (non-Google file):**

    <figure><img src="../../../.gitbook/assets/image (501).png" alt="Configuration for downloading non-Google files using direct media URL"><figcaption></figcaption></figure>

**v. Download from Drive**

*   For both types of files, the variables that are initialized will connect to the flow component **Download file** where you can download these files.

    <figure><img src="../../../.gitbook/assets/image (502).png" alt="Download file flow component that downloads files from Google Drive"><figcaption></figcaption></figure>

**vi. Upload to Google Cloud Storage**

* In the next step, you will use the **Google Cloud Storage** connector with the action **uploadFileToGCS** with your target bucket and `fileName`.

<figure><img src="../../../.gitbook/assets/image (503).png" alt="Google Cloud Storage connector uploadFileToGCS action with target bucket and fileName"><figcaption></figcaption></figure>

**vii. Update File State**

* In the next step, you will use the State component to overwrite the State for StateKey depending on the updates.

<figure><img src="../../../.gitbook/assets/image (504).png" alt="State component overwriting the stateKey value after file upload"><figcaption></figcaption></figure>

* Loop picks up next `currentFile` and continues until `var.files` is empty.

***

## **6. Finish the Migration**

The loop continues until all files are processed.\
When complete, the main flow returns a success message confirming the migration.

<figure><img src="../../../.gitbook/assets/image (506).png" alt="Flow returning a success message confirming the migration is complete"><figcaption></figcaption></figure>
