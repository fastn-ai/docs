# Pipelines

A **Pipeline** defines _where_ your releases will be deployed.

You use a pipeline to send releases to environments or domains.

> You can assign multiple destinations inside a single pipeline if you want a release to propagate across several environments.

### **Creating a Pipeline**

* Go to **Settings → Deployment → Pipelines**.
* Click **Create Pipeline** (top-right).

<figure><img src="../../../../../.gitbook/assets/image (677).png" alt=""><figcaption></figcaption></figure>

* Add:
  * **Pipeline Name**
  * **Description**

<figure><img src="../../../../../.gitbook/assets/image (678).png" alt=""><figcaption></figcaption></figure>

* (Optional) Enable **Deploy to Different Domains** to deploy outside the current domain.

<figure><img src="../../../../../.gitbook/assets/image (679).png" alt=""><figcaption></figcaption></figure>

* Under **Destination**, select your primary deployment destination (e.g., UCL).
* Add additional destinations if needed.
* Click **Create Pipeline**.

### **Deploying a Release Through a Pipeline**

Once the pipeline is created:

* Click the **Deploy a Release** button.

<figure><img src="../../../../../.gitbook/assets/image (687).png" alt=""><figcaption></figcaption></figure>

* Add a **Deployment Description**.

<figure><img src="../../../../../.gitbook/assets/image (682).png" alt=""><figcaption></figcaption></figure>

* Click **Deploy**.

<figure><img src="../../../../../.gitbook/assets/image (683).png" alt=""><figcaption></figcaption></figure>

> You’ll see a confirmation indicating that the deployment is complete and that the selected release was successfully pushed to the configured destinations.
