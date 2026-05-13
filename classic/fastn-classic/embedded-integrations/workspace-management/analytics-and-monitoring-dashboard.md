---
description: Track Every Integration. Optimize Every Flow.
---

# Analytics & Monitoring Dashboard

Fastn offers two powerful dashboards that provide complete visibility into your integration environment: the **Overview Dashboard** and the **Connectors Dashboard**.\
Together, they help you **monitor**, **troubleshoot**, and **optimize** integrations with precision and confidence.

## **Overview Dashboard**

### **Stay in Control with Actionable Insights**

The **Overview Dashboard** gives you a high-level snapshot of your system’s performance and activity across all tenants. It helps you track latency, errors, flow executions, and connector activity over time.

<figure><img src="../../../../.gitbook/assets/image (646).png" alt=""><figcaption></figcaption></figure>

### **Key Metrics**

These metrics provide a quick understanding of your integration health and flow behavior.

<table data-header-hidden><thead><tr><th></th><th width="470"></th><th></th></tr></thead><tbody><tr><td><strong>Metric</strong></td><td><strong>What It Means</strong></td><td><strong>Example Value</strong></td></tr><tr><td><strong>Flows</strong></td><td>Total number of flows configured or executed in your workspace. Helps gauge how many automations are active.</td><td><code>7</code></td></tr><tr><td><strong>Requests</strong></td><td>Total number of requests processed across all flows. Indicates system workload.</td><td><code>26</code></td></tr><tr><td><strong>Latency</strong></td><td>Average time taken for requests to complete, shown in milliseconds. Helps you identify potential slowdowns.</td><td><code>23 ms</code></td></tr><tr><td><strong>Errors</strong></td><td>Total count of failed requests or executions. Key indicator for debugging and reliability tracking.</td><td><code>2</code></td></tr></tbody></table>

### **Visual Analytics**

1. **Request Trends (Last 7 Days)**\
   Track how many requests were processed daily (Sun–Sat) to spot usage peaks or downtime periods.
2. **Error Trends (Last 7 Days)**\
   Visualize when and how often errors occur to identify problematic flows or connectors.

<figure><img src="../../../../.gitbook/assets/image (647).png" alt=""><figcaption></figcaption></figure>

* **Latency Trends (P50, P90, P99)**\
  Measure and compare request latency percentiles to detect performance degradation or API bottlenecks.
  * **P50:** Median latency
  * **P90:** 90th percentile (upper threshold of normal performance)
  * **P99:** 99th percentile (outlier or worst-case latency)

<figure><img src="../../../../.gitbook/assets/image (648).png" alt=""><figcaption></figcaption></figure>

*   **Flow Activity (Last 7 Days)**\
    Monitor which flows have been triggered and how frequently they run.<br>

    <figure><img src="../../../../.gitbook/assets/image (649).png" alt=""><figcaption></figcaption></figure>
* **Connector Usage (Last 7 Days)**\
  View which connectors were used within the period and how often.

<figure><img src="../../../../.gitbook/assets/image (650).png" alt=""><figcaption></figcaption></figure>

### **Filtering Options**

* **Tenant Filter:** Analyze performance for specific tenants or across all tenants.

<figure><img src="../../../../.gitbook/assets/image (651).png" alt=""><figcaption></figcaption></figure>

* **Flow Filter:** Drill down into individual flows to isolate latency, error trends, or request spikes.

<figure><img src="../../../../.gitbook/assets/image (652).png" alt=""><figcaption></figcaption></figure>

## **Connectors Dashboard**

### **Monitor Connector Health Across Tenants**

The **Connectors Dashboard** provides a detailed view of connector usage, success rates, and tenant-level activity. It helps you detect integration failures, analyze performance patterns, and assess data flow across your Fastn environment.

<figure><img src="../../../../.gitbook/assets/image (653).png" alt=""><figcaption></figcaption></figure>

> Tool usage statistics reflect **tenant-level activity**. Workspace-specific data is not displayed.

### **Key Metrics**

The **Key Metrics** panel offers a consolidated snapshot of system performance, connector engagement, and tenant activity.\
Each metric helps you understand different aspects of integration health.

<table data-header-hidden><thead><tr><th></th><th width="496"></th><th></th></tr></thead><tbody><tr><td><strong>Metric</strong></td><td><strong>What It Means</strong></td><td><strong>Example Value</strong></td></tr><tr><td><strong>Active Tenants</strong></td><td>Number and percentage of tenants with active connections. Tracks platform-wide adoption and deployment coverage.</td><td><code>1/1 (100%)</code></td></tr><tr><td><strong>Active Connectors</strong></td><td>Number of connectors in use compared to the total available. Indicates utilization and engagement level.</td><td><code>2/5 (40%)</code></td></tr><tr><td><strong>Tenant Request Success Rate</strong></td><td>Percentage of successful API requests made by tenants. A low rate may indicate connection or configuration issues.</td><td><code>85.0% (17/20)</code></td></tr><tr><td><strong>Connection Success Rate</strong></td><td>Percentage of successful connection attempts. Highlights authentication stability and connector reliability.</td><td><code>100%</code></td></tr><tr><td><strong>Average API Latency</strong></td><td>Average duration (in milliseconds) for API calls to complete. Useful for identifying performance delays.</td><td><code>550 ms</code></td></tr><tr><td><strong>Average Workflows Latency</strong></td><td>Average execution time for flows involving connectors. Helps measure workflow efficiency.</td><td><code>50 ms</code></td></tr><tr><td><strong>Average Queue Time</strong></td><td>Time requests spend waiting before execution. Longer queues may signal system load or throttling.</td><td><code>50 ms</code></td></tr><tr><td><strong>Total Data Transfer</strong></td><td>Total data volume transmitted across connectors, useful for tracking bandwidth or transfer-heavy use cases.</td><td><code>2.73 KB</code></td></tr></tbody></table>

### **Tenant Usage Summary**

Gives per-tenant visibility into connection activity and data flow metrics.

<figure><img src="../../../../.gitbook/assets/image (654).png" alt=""><figcaption></figcaption></figure>

You can **sort results** by number of connections, error count, or total data transferred.

### **Most Used Connectors**

Displays connectors with the highest number of connected accounts or the most frequent usage.

<figure><img src="../../../../.gitbook/assets/image (655).png" alt=""><figcaption></figcaption></figure>

### **Connector Error Rate**

Shows connectors with the highest error percentage over the selected period.

### **Action Usage Analytics**

Visualize connector-level action performance and system activity over time.\
The graph plots total action usage per day (e.g., Sep 9–Oct 9), highlighting activity spikes and usage frequency.

<figure><img src="../../../../.gitbook/assets/image (656).png" alt=""><figcaption></figcaption></figure>

### **App Breakdown (Current Month)**

<figure><img src="../../../../.gitbook/assets/image (657).png" alt=""><figcaption></figcaption></figure>

#### **Data Refresh Frequency**

All metrics and charts in both dashboards are **automatically refreshed** to reflect the **latest performance over the past 7 days**, ensuring you always see real-time operational insights.

#### **Summary**

* **Overview Dashboard:** Gives a high-level snapshot of your flows, requests, latency, and error patterns.
* **Connectors Dashboard:** Provides detailed analytics on connector health, tenant usage, and action-level performance.

Together, they enable you to **stay proactive**, **identify issues early**, and **optimize performance** across your entire Fastn environment.
