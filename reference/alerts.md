---
description: Alert rule conditions, thresholds, and monitoring configuration.
---

# Alerts

Alert rules monitor connector and workflow performance. Managed under **Activity → Alerts**.

### Creating an alert

1. Go to **Activity → Alerts**.
2. Click **"Create Alert"**.
3. Configure:

| Field         | Required | Description                                               |
| ------------- | -------- | --------------------------------------------------------- |
| **Name**      | Yes      | Alert identifier (e.g., "High Error Rate")                |
| **Condition** | Yes      | What metric to monitor (dropdown)                         |
| **Threshold** | Yes      | Value that triggers the alert (e.g., 5 for 5% error rate) |

4. Click **Create**.

### Alert conditions

6 metric conditions available:

| Condition         | What it measures                     | Threshold example |
| ----------------- | ------------------------------------ | ----------------- |
| **error rate**    | Percentage of failed executions      | 5 = 5% error rate |
| **latency p99**   | 99th percentile execution duration   | 5000 = 5 seconds  |
| **latency p95**   | 95th percentile execution duration   | 3000 = 3 seconds  |
| **latency avg**   | Average execution duration           | 2000 = 2 seconds  |
| **throughput**    | Number of executions per time period | Varies            |
| **failure count** | Absolute number of failed executions | 10 = 10 failures  |

### Alert rules page

Under **Activity → Alerts**:

* Title: **"Alert Rules"**
* Subtitle: "Configure alert rules to monitor connector and workflow performance."
* **"Create Alert"** button
* List of configured alert rules
* Empty state: "No alert rules configured. Create your first alert."
