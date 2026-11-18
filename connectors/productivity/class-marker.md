---
description: "ClassMarker is an online testing and quiz platform for exams, training assessments and certification."
hidden: true
---

# ClassMarker

<img src="../../.gitbook/assets/connectors/lg/class-marker.png" alt="ClassMarker logo">

ClassMarker is an online testing and quiz platform for exams, training assessments and certification. This connector covers the ClassMarker REST API v1: the group, link and exam catalogue, recent results for groups, links and individual exams, access list code management, the question bank, and test categories. Requests are authenticated with an API key plus a per-request SHA-256 signature and UNIX timestamp.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [classmarker.com](https://classmarker.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `classMarker` |

## Use it

Add ClassMarker from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.classMarker.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Access Codes | `addAccessCodes` | Add access codes to an access list, so unregistered users can be admitted to a restricted exam. The codes are sent as a JSON array; supply them pre-encoded, for example ["Code1", "Code2"]. Find the access list identifier in the ClassMarker web app under the exam's Access List settings. |
| Create Category | `createCategory` | Create a child category underneath an existing parent category. ClassMarker exposes no API to delete a category, so created categories persist until removed in the web app. |
| Create Parent Category | `createParentCategory` | Create a top-level parent category for organising question-bank questions. ClassMarker exposes no API to delete a category, so created categories persist until removed in the web app. |
| Create Question | `createQuestion` | Add a question to the account's question bank. Category and Randomise Answers are both required by the API even though the published documentation shows them as optional. The correct answer is designated inside the Answer Options object rather than by a top-level field: the API rejects correct_answer, correct_answers and answer as invalid properties. Essay questions are scored manually. ClassMarker exposes no API to delete a question, so created questions persist until archived or removed in the web app. |
| Delete Access Codes | `deleteAccessCodes` | Remove access codes from an access list, revoking admission for unregistered users holding those codes. The codes are sent as a JSON array; supply them pre-encoded, for example ["Code1", "Code2"]. |
| Get Question | `getQuestion` | Retrieve a single question from the question bank by its identifier, including its answer options, correct answer and feedback. Obtain question identifiers from List Questions. |
| List Categories | `listCategories` | List every parent category and its child categories in the account. Category identifiers are needed when creating or updating question-bank questions. |
| List Groups Links And Exams | `listGroupsLinksAndExams` | List every group, public link and exam available to the account, with the identifiers needed by the recent-results actions. Returns status ok with data, or no_results when the account has no groups or links yet. |
| List Questions | `listQuestions` | List every question in the account's question bank, with its type, category, scoring, feedback and answer options. |
| List Recent Results For All Groups | `listRecentResultsForAllGroups` | Retrieve recent exam results across every group in the account. Use Finished After Timestamp to page forward through results by completion time; ClassMarker defaults to roughly the last fourteen days when it is omitted. |
| List Recent Results For All Links | `listRecentResultsForAllLinks` | Retrieve recent exam results across every public link in the account. Use Finished After Timestamp to page forward through results by completion time; ClassMarker defaults to roughly the last fourteen days when it is omitted. |
| List Recent Results For Group Exam | `listRecentResultsForGroupExam` | Retrieve recent results for one specific exam within one specific group. Obtain the group and exam identifiers from List Groups Links And Exams. |
| List Recent Results For Link Exam | `listRecentResultsForLinkExam` | Retrieve recent results for one specific exam behind one specific public link. Obtain the link and exam identifiers from List Groups Links And Exams. |
| Update Category | `updateCategory` | Rename a child category or move it under a different parent category. Obtain the category identifier from List Categories. Note that the published documentation gives the route as /v1/category/{category_id}.json, which does not exist; the working route is /v1/categories/category/{category_id}.json. |
| Update Parent Category | `updateParentCategory` | Rename an existing parent category. Obtain the parent category identifier from List Categories. |
| Update Question | `updateQuestion` | Update an existing question in the account's question bank, including its text, type, options, category, scoring and feedback. Obtain the question identifier from List Questions. The correct answer is designated inside the Answer Options object rather than by a top-level field: the API rejects correct_answer, correct_answers and answer as invalid properties. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Exam Completed (Group) | `single_user_test_results_group` | Fires in real time when a user registered in a ClassMarker group finishes an exam, delivering the full result including score, pass/pass-mark, timings, certificate and any monitoring events. ClassMarker has NO webhook registration API, so the customer must register the fastn trigger URL by hand: log in to ClassMarker, go to My Account &gt; Webhooks / API Keys, open the Webhooks tab, click 'New Webhook +', enter a name, paste the fastn trigger URL into the endpoint field, tick the optional extras you need (Questions, responses and category results; Unique link ID for links; URL for viewing results), tick 'Verify on Save', then click 'Save Webhook Settings'. Finally assign the webhook to the group, either while assigning an exam or by editing an existing exam's settings. ClassMarker sends a probe with payload_status 'verify' on save and 'live' for real results. Payload schema modelled from ClassMarker's published sample, not from a captured delivery. |
| Exam Completed (Link) | `single_user_test_results_link` | Fires in real time when someone finishes an exam taken through a ClassMarker public link, delivering the full result including score, pass/pass-mark, timings, certificate and any monitoring events. ClassMarker has NO webhook registration API, so the customer must register the fastn trigger URL by hand: log in to ClassMarker, go to My Account &gt; Webhooks / API Keys, open the Webhooks tab, click 'New Webhook +', enter a name, paste the fastn trigger URL into the endpoint field, tick the optional extras you need (Questions, responses and category results; Unique link ID for links; URL for viewing results), tick 'Verify on Save', then click 'Save Webhook Settings'. Finally assign the webhook to the link, either while assigning an exam or by editing an existing exam's settings. ClassMarker sends a probe with payload_status 'verify' on save and 'live' for real results. Payload schema modelled from ClassMarker's published sample, not from a captured delivery. |
