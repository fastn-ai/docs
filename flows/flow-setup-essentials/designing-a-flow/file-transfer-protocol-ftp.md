---
description: Transfer files between systems using FTP, FTPS, or SFTP connections.
---

# File Transfer Protocol (FTP)

The **File Transfer Protocol** component lets you upload, download, list, delete, or rename files on remote servers directly from your flow. Use it when your automation needs to exchange files with external systems over FTP, FTPS, or SFTP — for example, uploading reports to a partner's server or downloading data feeds for processing.

<figure><img src="../../../.gitbook/assets/image (28).png" alt="File Transfer Protocol component in the Fastn flow editor"><figcaption></figcaption></figure>

### **How to Configure?**

* **Select Connection Type**\
  Choose the connection mode based on your use case: **FTP**, **FTPS**, or **SFTP**.

<figure><img src="../../../.gitbook/assets/image (29).png" alt="Connection type selection dropdown with FTP, FTPS, and SFTP options"><figcaption></figcaption></figure>

* **Connect or Create Account**
  * You can **connect an existing FTP/FTPS/SFTP account** if already configured.
  * Or, enable the **Manual** toggle to create your own credentials.

<figure><img src="../../../.gitbook/assets/image (33).png" alt="FTP account connection panel with option to connect existing or create manual credentials"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (32).png" alt="Manual credentials form for creating a new FTP connection"><figcaption></figcaption></figure>

* **Select Operation**\
  Choose what you want the component to do:
  * **Upload** a file to the remote server
  * **Download** a file from the remote server
  * **List** files in a directory
  * **Delete** a file from the server
  * **Rename** a file
* **Set File Path**\
  Specify the target **path** for the file or directory where the operation should be performed.

<figure><img src="../../../.gitbook/assets/image (34).png" alt="FTP operation selection and file path configuration fields"><figcaption></figcaption></figure>

* **Run the Flow**\
  Save and run the flow. The selected file operation will execute automatically.

<figure><img src="../../../.gitbook/assets/image (35).png" alt="Flow execution results after running the FTP file operation"><figcaption></figcaption></figure>

### **How It Helps?**

* Transfer files securely across systems using **FTP**, **FTPS**, or **SFTP**.
* Perform multiple operations like **upload, download, or list** files in one flow.
* Enable **manual credentials** for flexible setup when predefined accounts aren’t available.
* Works seamlessly in **tenant-based environments**, each tenant’s FTP account is isolated and managed securely.
* Solves the limitation where FTP connections cannot list files directly by adding a **List operation** for better file visibility.
