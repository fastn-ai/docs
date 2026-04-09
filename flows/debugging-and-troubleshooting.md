---
description: Find and fix problems in your flows using Fastn's built-in debugging tools.
---

# Debugging & Troubleshooting

When a flow does not behave the way you expect or returns wrong data, fails silently, or never triggers. Fastn gives you three tools to figure out what went wrong which includes the **Test** button, the **Logs** page, and the **Logger** step. This section covers how to use each one and lists the most common problems you will encounter.

### Tool 1: The Test button

The Test button lets you run your flow with sample data without deploying it. This is your first debugging tool, for good practice use it every time you make a change.

#### Where to find it

The **Test** button is in the top-right corner of the flow builder, next to **Deploy** and **\</> Integrate**. It has a play icon (▶) and a dropdown arrow.

<figure><img src="../.gitbook/assets/test button fastn flows.gif" alt="Animated demo showing the Test button location in the top-right corner of the flow builder"><figcaption></figcaption></figure>

#### How to use it

1. Open your flow in the builder.
2. Click **Test**.
3. A test panel will open . Enter a JSON request body that matches your trigger's input schema or simply click **Run** if you have defined input in your flow already.

#### What to look for

* **Click on any step** after a test run to see its input and output in the right panel. This tells you exactly what data entered the step and what came out.
* If a step shows a red indicator this likely means an error was detected , the right panel shows the error message.

<figure><img src="../.gitbook/assets/error fastn flowes right pop up.png" alt="Flow builder showing a failed step highlighted in red with error details and JSON output in the right panel"><figcaption></figcaption></figure>

* Compare the output of each step with what you expected. If step 3 returns unexpected data, the problem is likely in step 2's configuration (the step feeding data into step 3).

#### When the Test button does not work

| Symptom                                   | Cause                                                                         | Fix                                                                                                                                                                  |
| ----------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Test button is grayed out or unresponsive | No steps have been added yet that can be tested                               | Make sure you have at least one step beyond the trigger.                                                                                                             |
| Test produces no output                   | No **Success** or **Error** response step at the end of the flow              | Add a **Success** step (under **Flow Response**) as the last step in your flow. Without a response step, the flow executes but returns nothing.                      |
| Test runs but every step shows an error   | Input schema mismatch — the test data does not match what the trigger expects | Open the trigger step, check the **Request Schema**, and make sure your test JSON has the exact field names and types defined there. Field names are case-sensitive. |

### Tool 2: The Logs page

The Logs page shows the execution history of all your deployed flows — every time a flow ran, whether it succeeded or failed, and how long it took. This is where you investigate problems in production.

#### Where to find it

Click **Logs** in the left sidebar. It is a separate section, not inside Flows.

<figure><img src="../.gitbook/assets/logs.gif" alt="Animated demo of navigating to the Logs page from the left sidebar to view flow execution history"><figcaption></figcaption></figure>

#### What you'll see

The Logs page shows a table with these columns:

| Column               | What it tells you                                                            |
| -------------------- | ---------------------------------------------------------------------------- |
| **Flow Name**        | Which flow ran                                                               |
| **Request Time**     | When the execution started                                                   |
| **Duration (s)**     | How long the execution took in seconds                                       |
| **HTTP Status Code** | The result — 200 means success, anything else means something went wrong     |
| **tenantId**         | Which customer/tenant triggered the flow (relevant for multi-tenant widgets) |
|                      |                                                                              |

Each row also has a **View logs** link that opens the detailed execution trace.

#### How to read a log entry

Click **View logs** on any row to see the step-by-step execution:

1. Each step shows whether it passed or failed.
2. For each step, you can see the **input** (what data entered the step) and the **output** (what data came out).
3. If a step failed, the error message appears with the specific reason.

**What to look for:**

* **Find the first red step** that is where the failure started. Every red step after it may just be a consequence of the first failure.
* **Compare the output of the step before the failure** with the input the failing step expected. Mismatched field names, null values, or wrong data types are the most common causes.
* **Check the HTTP Status Code** in the list view first. A 200 means the flow completed. A 400 usually means bad input. A 401 means authentication failed. A 500 means an internal error.

### Tool 3: The Logger step

The Logger step lets you write data to the Logs at any point in your flow. Use it to inspect what data looks like between steps, especially when the Test button is not enough (e.g., for flows triggered by external webhooks or schedules that you cannot easily test manually).

#### Where to find it

In the flow builder, click the **+** button to open the step picker. Scroll down to **Flow Control**. Logger is listed alongside Custom Code, Switch, Loop, and Log Metrics.

<figure><img src="../.gitbook/assets/logger alt fastn flows.gif" alt="Animated demo of adding a Logger step from the Flow Control section in the step picker"><figcaption></figcaption></figure>

Alternatively you can search "Logger" on the right side of the canvas and drag the logger to the desired step, as shown below:

<figure><img src="../.gitbook/assets/logger fastn flows.gif" alt="Animated demo of dragging a Logger step from the search panel onto the flow canvas"><figcaption></figcaption></figure>

#### How to use it

1. Click **+** below the step you want to inspect.
2. Under **Flow Control**, click **Logger**.
3. Configure what to log, map the data fields you want to inspect. For example, log the status of the output of the previous step: `{{steps.sendMessage.output.ok}}`.
4. **Save** and **Deploy** the flow.
5. When the flow runs, the logged data appears in the **Logs** page under that execution's detailed view.

> **Additional step:** You can also check if the Logger is working before deployment by testing the steps till the logger by utilizing the Test button as shown below:

<figure><img src="../.gitbook/assets/logger details .png" alt="Flow builder showing Logger step configuration and test output with LogOutput highlighted in the bottom panel"><figcaption></figcaption></figure>

#### When to use Logger vs Test

| Scenario                                                  | Use Test button                                     | Use Logger step                                                       |
| --------------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------------------------- |
| Building and iterating on a flow                          | For faster testing without deployment               | Not needed                                                            |
| Flow triggered by an external webhook (Shopify, Slack)    | No, as the trigger comes from outside               | Yes, deploy with Logger to capture live data                          |
| Scheduled flow that runs at 3 AM                          | No                                                  | Yes, inspect the logged data according to the previously ran triggers |
| Intermittent failure that only happens with specific data | Difficult as you may not know which input causes it | Yes — log the input to every run and compare                          |
| Production debugging, flow works in test but fails live   | Test does not reproduce the issue                   | Yes — add Logger to the failing step to see real production data      |

> **Important:** Remove or disable Logger steps before your flow goes into heavy production use. Each Logger step writes to the Logs database on every execution, which adds processing time and storage. Use them for debugging, then clean up accordingly.

### Common errors and how to fix them

These are the most frequently reported problems across Fastn customers, drawn from actual support cases and feedback.

#### Flow creation and setup errors

| Error                                     | What happened                                          | Fix                                                                                                                                           |
| ----------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Flow name rejected**                    | Used spaces, hyphens, or special characters            | Flow names only allow letters, numbers, and underscores. Use `daily_sync` not `daily-sync`.                                                   |
| **Test button grayed out**                | No steps added, or flow not saved                      | Add at least one step beyond the trigger, then click **Save**.                                                                                |
| **"Changes Pending" status after Deploy** | Deploy did not complete, or you edited after deploying | If you edited after deploying, click **Deploy** again. The deployed version is the one that runs in production — your working draft does not. |

#### Connector and authentication errors

| Error                                                | What happened                                                                                                                       | Fix                                                                                                                                                                                |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **401 Unauthorized during test or execution**        | API key is missing, expired, or the connector credentials have been revoked                                                         | Go to **Connectors then Credentials** in the left sidebar. Re-authenticate the connector. Then go to **\</> Integrate** and generate a new API key if calling the flow externally. |
| **Connector shows "Connected" but flow still fails** | The token expired behind the scenes, or the external service requires additional OAuth scopes                                       | Disconnect and reconnect the connector in **Connectors → Credentials**. Check if the external service (Slack, HubSpot, Shopify) has revoked or limited your access.                |
| **Multiple connections found**                       | The flow references a connector that has more than one authenticated connection, and the platform cannot determine which one to use | Specify the connection ID parameter in the Connector step configuration. Check **Connectors → Credentials** to find the correct connection ID.                                     |

#### Deployment and runtime errors

| Error                                                | What happened                                                                                   | Fix                                                                                                                                                                                                                                   |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Flow works in Test but fails when called via API** | Missing headers, wrong API key, or the deployed version is out of date                          | Click **\</> Integrate** and copy the exact cURL snippet — it includes all required headers. Make sure you have deployed after your latest changes (status should be **Live**, not **Changes Pending**).                              |
| **Flow execution times out**                         | An external API call or connector is taking too long to respond                                 | Add a timeout to the Connector step if available. Break large data processing into smaller batches using pagination. If using Custom Code, check for infinite loops.                                                                  |
| **Scheduled flow did not run**                       | Flow is not deployed, schedule is paused, or the webhook was never registered                   | Check the flow's status on the Flows list — must be **Live**. Go to **Triggers → Schedules** tab and confirm the schedule is active. If the flow uses an activation-registered webhook, confirm the activation flow ran successfully. |
| **Scheduled flow ran but produced no results**       | No new data in the external system since the last run, or the query filters are too restrictive | Add a Logger step to inspect what the Connector returns on each run. If it returns an empty array, the problem is upstream (in the source system), not in your flow.                                                                  |
| **API returns empty response**                       | No **Success** or **Error** step at the end of the flow                                         | Add a **Success** step (under **Flow Response**) as the final step. Map the data you want to return. Without this, the flow executes but the API caller receives nothing back.                                                        |
