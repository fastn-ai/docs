---
description: UCL lets you easily build your own custom tool groups using natural language.
---

# Creating a Custom Tool

### **Step 1: Start from UCL Setup**

* Go to the **Connect** section in your UCL Workspace.

<figure><img src="../../../.gitbook/assets/image (575).png" alt=""><figcaption></figcaption></figure>

* Click **“Define a Custom App”** to launch the **App Builder Assistant** chat.

<figure><img src="../../../.gitbook/assets/image (573).png" alt=""><figcaption></figcaption></figure>

### **Step 2: Create a Tool via Prompt**

Type a natural language prompt like:

> _“Create a tool for Google Cloud Storage.”_

The assistant may detect existing tooland ask where to add this app. For example:

> _Would you like to add the Google Cloud Storage tool under one of these, or shall I create a new group (e.g., “GoogleCloudStorage” with OAuth2 authentication)?_

You respond:

> _“Create a new group.”_

<figure><img src="../../../.gitbook/assets/image (214).png" alt=""><figcaption></figcaption></figure>

ℹ️ **Want to add to an existing tool instead?**\
Click **“Add to Existing Tool”** and select the tool you'd like to edit or extend with new toolkits.

<figure><img src="../../../.gitbook/assets/image (220).png" alt=""><figcaption></figcaption></figure>

### **Step 3: Confirm OAuth2 Authentication Setup**

The assistant will suggest an OAuth2 setup for the new tool:

```json
{
  "baseUrl": "https://accounts.google.com/o/oauth2/auth",
  "clientId": "",
  "secret": "",
  "params": {
    "scope": "https://www.googleapis.com/auth/devstorage.read_write",
    "response_type": "code",
    "access_type": "offline",
    "prompt": "consent"
  },
  "requiredAttributes": [],
  "tenantId": "default",
  "authorization": {
    "oauthGrantType": "authCodeGrantWithGrantType",
    "accessTokenUrl": "https://oauth2.googleapis.com/token",
    "refreshTokenGrantType": "refreshTokenWithAccessType"
  }
}
```

Confirm when prompted:

> _“Yes.”_

The assistant will respond:

> _“The ‘GoogleCloudStorage’ group is ready.”_

<figure><img src="../../../.gitbook/assets/image (215).png" alt=""><figcaption></figcaption></figure>

### **Step 4: Add Actions to the Tool**

The assistant will suggest actions to expose:

> _Which GCS operation would you like to expose first as a tool? For example:_

* `listBuckets`
* `getBucketMetadata`
* `createBucket`
* `deleteBucket`
* `listObjects`
* `uploadObject`
* `downloadObject`
* `deleteObject`

You can respond:

> _“Add createBucket and listObjects.”_

You’ll then receive:

> _The tools “createBucket” and “listObjects” have been created successfully in the “GoogleCloudStorage” group. You can now use them in your workflows._

<figure><img src="../../../.gitbook/assets/image (217).png" alt=""><figcaption></figcaption></figure>

### **Step 5: Finalize Setup in the Tools Section**

* Navigate to the **Tools** section in your UCL project.
* Under **Workspace Tools**, find the newly created **GoogleCloudStorage** group.

<figure><img src="../../../.gitbook/assets/image (210).png" alt=""><figcaption></figcaption></figure>

* Click the **three dots menu** > **Edit**, and fill in the `clientId` and `secret` using your Google Cloud credentials.
* Save the configuration.

<figure><img src="../../../.gitbook/assets/image (212).png" alt=""><figcaption></figcaption></figure>

### **Step 6: Connect and Test with AI Agent**

* Now go back to the **Setup** section.
* Search for your **GoogleCloudStorage** tool group and **Connect** the app by authenticating your Google account.

<figure><img src="../../../.gitbook/assets/image (219).png" alt=""><figcaption></figcaption></figure>

* Once connected, select any of the added actions (like `createBucket` or `listObjects`).

<figure><img src="../../../.gitbook/assets/image (218).png" alt=""><figcaption></figcaption></figure>

*   Use the AI Agent to test your tool with a natural command:

    > _“Create a bucket in my Google Cloud Storage.”_

#### Additional Prompt Ideas for creating Custom Tool

* “Create a tool for a fitness tracking app like Strava.”
* “Build a tool that pulls ticket data from our in-house Jira instance.”
* “Set up a custom tool for a REST API with POST and GET methods.”
