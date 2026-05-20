---
description: >-
  In this guide, you’ll learn how to connect a UCL deployment to Cursor and use
  its AI assistant to retrieve summary from Notion for a specific meeting; all
  without writing any integration code.
---

# Connect UCL to Cursor and access data from Notion

### **Connect your Notion account to UCL**

* You need to authenticate your Notion account, after which the Notion App will appear as **Connected**.

<figure><img src="../../../../../.gitbook/assets/image (610).png" alt=""><figcaption></figcaption></figure>

* From **Select Tools**, you can enable all or any specific **Actions**.

<figure><img src="../../../../../.gitbook/assets/image (611).png" alt=""><figcaption></figcaption></figure>

### **Connect Cursor to UCL**

* Download and install the latest version of [Cursor](https://cursor.com) on your desktop.
* Open Cursor and navigate to **Settings** in the top-right corner.
* Next, in the **MCP** section, click **Add Custom MCP**; this opens a file named `mcp.json`.

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3iSr2Tx8FvvuoLPncziH%2Fuploads%2F12FdzVQ8dHx7PHwKgg0e%2F20250921-0514-43.4793583.mp4?alt=media&token=2a1903b6-557c-4c8f-8829-df51a58362bc" %}

* From your UCL dashboard, you can navigate to the **Embed** section from the top navigation bar and select **Cursor** from the list of clients available to access the step-by-step embedding guide for Cursor with UCL.

{% hint style="info" %}
You can select and follow the guide for any client of your choice from the embed page to integrate it with UCL.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/image (616).png" alt=""><figcaption></figcaption></figure>

* In the **Open Setting and Add MCP Server** step, you will see the Cursor command code, which you can copy for your workspace and paste it into Cursor.

{% hint style="info" %}
Checking the **Multi Tenant** option will enable you to embed connectors and actions for multiple users \[users].
{% endhint %}

```json
{
  "mcpServers": {
    "fastn": {
      "transport": "streamable_http",
      "url": "https://mcp.ucl.dev/shttp/space_id={}&tenant_id=test-tenant&auth_token=customAuthToken"
    }
  }
}

```

* Paste this configuration into the `mcp.json` file in Cursor and **save** it.

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3iSr2Tx8FvvuoLPncziH%2Fuploads%2F12PRrTiqdrEWHXqUagPy%2F20250921-0520-33.9852515.mp4?alt=media&token=a7c91d6c-e059-45dd-83b3-93fc0e31d7a2" %}

* You should now see the UCL Server listed as connected in Cursor. Under the tools label in Cursor, you can view all the enabled actions available with your connectors in UCL.

<figure><img src="../../../../../.gitbook/assets/image (612).png" alt=""><figcaption></figcaption></figure>

### **Use Cursor to Fetch Meeting Summary from Notion**

* In Cursor, click **Toggle AI Pane** from the top-right corner to open the assistant.

<figure><img src="../../../../../.gitbook/assets/image (614).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Make sure you’ve selected an **agent;** it's not auto-set.
{% endhint %}

*   In the assistant, it will ask for your Notion database ID after you have given a command like:

    ```
    Fetch summary from Notion for the meeting titled "Meeting Name"
    ```
* The assistant will use the **"Get Tasks"** or a relevant action to retrieve notes.
* The meeting summary should appear directly in your AI plane, ready for review or further processing.

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3iSr2Tx8FvvuoLPncziH%2Fuploads%2Fln6CvLH9MXpQ58c5A8Qw%2F20250618-2103-01.6498607.mp4?alt=media&token=9d4a650a-4d6f-4cc1-bc2a-83a10b8eebe8" %}
