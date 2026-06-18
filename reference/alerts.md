---
description: Alert rule conditions, thresholds, and monitoring configuration.
---

# Alerts

Alerts notify you when a workflow or integration crosses a performance threshold. They are configured under **Activity → Alerts**.

### Creating an alert

Click **Create Alert**. The form has:

* **Name** (required)
* **Condition** (required) — The metric to watch
* **Threshold** (required) — The value that triggers the alert (e.g., "5" for a 5% error rate)

### Conditions

The available alert conditions are:

| Condition     | Watches                             |
| ------------- | ----------------------------------- |
| error rate    | The percentage of failed executions |
| latency p99   | 99th-percentile execution latency   |
| latency p95   | 95th-percentile execution latency   |
| latency avg   | Average execution latency           |
| throughput    | Execution volume                    |
| failure count | The number of failures              |
