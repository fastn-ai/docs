---
description: "Zoho People is an HR system. Read and add form records, leave records, attendance reports, timesheets and time logs."
hidden: true
---

# Zoho People

<img src="../../.gitbook/assets/connectors/lg/zoho-people.png" alt="Zoho People logo">

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [people.zoho.com](https://people.zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `zohoPeople` |

## Setup

Your customers sign in to Zoho People through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Zoho People from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoPeople.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Time Log</td><td><code>addTimeLog</code></td><td>Add a time log against a job in the Zoho People time tracker. Supply either the hours worked or a from and to time.</td></tr><tr><td>Get Attendance User Report</td><td><code>getAttendanceUserReport</code></td><td>Retrieve an employee's attendance report from Zoho People for a given month and year, showing worked hours per day.</td></tr><tr><td>Get Job Details</td><td><code>getJobDetails</code></td><td>Retrieve the details of a job in the Zoho People time tracker, including its project and client.</td></tr><tr><td>Get Leave Type Details</td><td><code>getLeaveTypeDetails</code></td><td>Retrieve the leave types assigned to an employee in Zoho People together with their permitted, availed and balance counts.</td></tr><tr><td>Get Timesheet</td><td><code>getTimesheet</code></td><td>Retrieve timesheets from the Zoho People time tracker for a user and date range.</td></tr><tr><td>Insert Form Record</td><td><code>insertFormRecord</code></td><td>Create a record in a Zoho People form, such as adding an employee to the employee form. Field values are supplied as a JSON object keyed by the form's field link names.</td></tr><tr><td>List Form Records</td><td><code>listFormRecords</code></td><td>Retrieve records from a Zoho People form view, optionally filtered by a search column and value or by modified time. Use view name P_EmployeeView to read employee records.</td></tr><tr><td>List Forms</td><td><code>listForms</code></td><td>Retrieve every form configured in your Zoho People account, including its display name and form link name. The form link name is required by the record actions.</td></tr><tr><td>List Leave Records</td><td><code>listLeaveRecords</code></td><td>Retrieve leave records within a date range from Zoho People, optionally filtered by employee, leave type or approval status.</td></tr><tr><td>List Time Logs</td><td><code>listTimeLogs</code></td><td>Retrieve time logs from the Zoho People time tracker for a date range, optionally filtered by user, job, project or billing status.</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Record Attendance</td><td><code>recordAttendance</code></td><td>Record an attendance check-in or check-out for an employee in Zoho People. At least one of employee ID, email address or map ID must be supplied to identify the employee.</td></tr><tr><td>Update Form Record</td><td><code>updateFormRecord</code></td><td>Update an existing record in a Zoho People form. Only the fields included in the input data are changed.</td></tr></tbody></table>

</details>

## Events

Zoho People has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
