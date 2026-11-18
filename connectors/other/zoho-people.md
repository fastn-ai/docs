---
description: "Zoho People is Zoho's HR management system."
hidden: true
---

# Zoho People

<img src="../../.gitbook/assets/connectors/zoho-people.png" alt="Zoho People logo" width="64">

Zoho People is Zoho's HR management system. This connector wraps the Zoho People REST API (people.zoho.com): forms and form records including employee data, leave tracking (leave records, leave types and balances), attendance check-in and check-out with attendance reports, and the time tracker module covering clients, projects, jobs, time logs and timesheets. OAuth 2.0 authorization code auth via the shared Zoho API Console app.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [people.zoho.com](https://people.zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `zohoPeople` |

## Use it

Add Zoho People from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoPeople.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Time Log | `addTimeLog` | Add a time log against a job in the Zoho People time tracker. Supply either the hours worked or a from and to time. |
| Get Attendance User Report | `getAttendanceUserReport` | Retrieve an employee's attendance report from Zoho People for a given month and year, showing worked hours per day. |
| Get Job Details | `getJobDetails` | Retrieve the details of a job in the Zoho People time tracker, including its project and client. |
| Get Leave Type Details | `getLeaveTypeDetails` | Retrieve the leave types assigned to an employee in Zoho People together with their permitted, availed and balance counts. |
| Get Timesheet | `getTimesheet` | Retrieve timesheets from the Zoho People time tracker for a user and date range. |
| Insert Form Record | `insertFormRecord` | Create a record in a Zoho People form, such as adding an employee to the employee form. Field values are supplied as a JSON object keyed by the form's field link names. |
| List Form Records | `listFormRecords` | Retrieve records from a Zoho People form view, optionally filtered by a search column and value or by modified time. Use view name P_EmployeeView to read employee records. |
| List Forms | `listForms` | Retrieve every form configured in your Zoho People account, including its display name and form link name. The form link name is required by the record actions. |
| List Leave Records | `listLeaveRecords` | Retrieve leave records within a date range from Zoho People, optionally filtered by employee, leave type or approval status. |
| List Time Logs | `listTimeLogs` | Retrieve time logs from the Zoho People time tracker for a date range, optionally filtered by user, job, project or billing status. |

<details>

<summary>See 2 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Record Attendance | `recordAttendance` | Record an attendance check-in or check-out for an employee in Zoho People. At least one of employee ID, email address or map ID must be supplied to identify the employee. |
| Update Form Record | `updateFormRecord` | Update an existing record in a Zoho People form. Only the fields included in the input data are changed. |

</details>
