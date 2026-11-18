---
description: "Zoho Learn is Zoho's knowledge management and online training platform."
hidden: true
---

# Zoho Learn

Zoho Learn is Zoho's knowledge management and online training platform. This connector wraps the Zoho Learn REST API v1 (learn.zoho.com/learn/api/v1): hubs and hub members, spaces and space members, manuals, chapters and articles, article export and search, courses with members, enrollment, completion, ratings and resources, lessons, learner status and discussions, question banks, course and lesson reports, and custom portal administration (invites, users, signup requests, and shared courses and manuals).

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [learn.zoho.com](https://learn.zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 73 |
| **Events** | 0 |
| **Slug** | `zohoLearn` |

## Use it

Add Zoho Learn from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoLearn.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Custom Portal User | `activateCustomPortalUser` | Activates a user in a Zoho Learn custom portal, restoring their access. |
| Add Attachment In Author Preview | `addAttachmentInAuthorPreview` | Uploads a temporary attachment for a learner answer while previewing a quiz or assignment as its author in Zoho Learn. The request is multipart/form-data. |
| Add Attachment To Learner Answer | `addAttachmentToLearnerAnswer` | Attaches a file or image to a learner's answer on a quiz or assignment in Zoho Learn. The request is multipart/form-data. |
| Add Course Rating Or Feedback | `addCourseRating` | Adds a star rating and written feedback to a course in Zoho Learn. At least one of rating or feedback must be supplied. |
| Add Members To A Course | `addCourseMembers` | Adds users to a course in Zoho Learn. Members are added as learners unless another role is given. |
| Add Or Remove User To Course In Custom Portal | `addOrRemoveUserToCourseInCustomPortal` | Adds custom portal users to a course shared with a Zoho Learn custom portal, or removes them from it. |
| Add Or Remove User To Manual In Custom Portal | `addOrRemoveUserToManualInCustomPortal` | Adds custom portal users to a manual shared with a Zoho Learn custom portal, or removes them from it. |
| Add Users To Manual | `addUsersToManual` | Adds hub users to a manual in Zoho Learn, or updates the role of users already on it. |
| Add Users To Space | `addUsersToSpace` | Adds hub users to a space in Zoho Learn, assigning each an Admin or Member role. |
| Approve Custom Portal Signup | `approveCustomPortalSignup` | Approves a pending self-signup request for a Zoho Learn custom portal. |
| Change Role Of Course Member | `changeCourseMemberRole` | Changes the role a member holds on a course in Zoho Learn. |
| Complete A Lesson | `completeLesson` | Marks a lesson within a course as completed for the connected Zoho Learn user and returns the updated course progress. |
| Complete Course | `completeCourse` | Marks a course as completed for the connected Zoho Learn user. |
| Create Article | `createArticle` | Creates an article in a Zoho Learn manual by importing a document. DOCX files may be up to 50 MB and other supported formats up to 10 MB. The request is multipart/form-data. |
| Create Chapter | `createChapter` | Creates a chapter in a Zoho Learn manual, optionally nested under an existing chapter or article. |
| Create Course | `createCourse` | Creates a course in a Zoho Learn portal. |
| Create Private Manual | `createPrivateManual` | Creates a private manual inside a space in Zoho Learn. The scope ID is the hub id returned by the Get Hub Listing action. |
| Create Question Bank | `createQuestionBank` | Creates a question bank in a Zoho Learn portal for reuse across quizzes. |
| Create Space | `createSpace` | Creates a space inside a Zoho Learn hub, optionally adding an initial set of members. |
| Create Space Manual | `createSpaceManual` | Creates a manual inside a space in Zoho Learn. The manual is visible to the members of that space. |
| Delete Attachment From Author Preview | `deleteAttachmentFromAuthorPreview` | Deletes a temporary attachment uploaded while previewing a quiz or assignment as its author in Zoho Learn. |
| Delete Attachment From Learner Answer | `deleteAttachmentFromLearnerAnswer` | Removes an attachment from a learner's answer on a quiz or assignment in Zoho Learn. |
| Delete Course Rating Or Feedback | `deleteCourseRating` | Deletes a course rating or feedback entry in Zoho Learn and returns the recalculated overall rating. |
| Delete Custom Portal Invite | `deleteCustomPortalInvite` | Withdraws a pending invitation to a Zoho Learn custom portal. |
| Delete Custom Portal User | `deleteCustomPortalUser` | Permanently removes a user from a Zoho Learn custom portal. |
| Delete Question Bank | `deleteQuestionBank` | Deletes a question bank from a Zoho Learn portal. |
| Disable Custom Portal | `disableCustomPortal` | Disables a custom portal in Zoho Learn, withdrawing access from its external users. Zoho's published documentation truncates this endpoint's path after "/di"; the path used here mirrors the documented Enable Custom Portal endpoint and should be confirmed against a live call. |
| Disable Custom Portal User | `disableCustomPortalUser` | Disables a user in a Zoho Learn custom portal, suspending their access without deleting them. |
| Edit Course Rating Or Feedback | `editCourseRating` | Updates an existing course rating or feedback entry in Zoho Learn. At least one of rating or feedback must be supplied. |
| Enable Custom Portal | `enableCustomPortal` | Enables a custom portal in Zoho Learn, making it available to its external users. |
| Enroll In A Course | `enrollInCourse` | Enrols the connected Zoho Learn user in a public or on-request course. |
| Export Article As HTML ZIP | `exportArticleAsHtmlZip` | Exports a Zoho Learn article as an HTML ZIP archive including its attachments. The response is a binary file rather than JSON. |
| Export Article As PDF | `exportArticleAsPdf` | Exports a Zoho Learn article as a PDF document. The response is a binary file rather than JSON. |
| Get All Question Banks | `getAllQuestionBanks` | Returns the question banks in a Zoho Learn portal, with optional creator filtering and sorting. |
| Get Article Information | `getArticleInformation` | Returns the details of an article in a Zoho Learn manual. |
| Get Course Data | `getCourseData` | Returns the details of a single course in a Zoho Learn portal, looked up by its course URL. |
| Get Course Listing | `getCourseListing` | Returns the courses in a Zoho Learn portal, filtered by the learner, author or explore view, with optional category, subcategory, tag and creator filters plus sorting and pagination. |
| Get Courses Shared To Custom Portal | `getCoursesSharedToCustomPortal` | Returns the courses that have been shared with a Zoho Learn custom portal, with sorting and pagination. |
| Get Custom Portal Pending Invites | `getCustomPortalPendingInvites` | Returns the invitations to a Zoho Learn custom portal that have not yet been accepted. |
| Get Custom Portal Signup Requests | `getCustomPortalSignupRequests` | Returns the pending self-signup requests for a Zoho Learn custom portal. |
| Get Custom Portal Users | `getCustomPortalUsers` | Returns the users belonging to a Zoho Learn custom portal. |
| Get Enrollment Requests | `getEnrollmentRequests` | Returns the pending enrolment requests for a course in Zoho Learn. |
| Get Hub Listing | `getHubListing` | Returns the Zoho Learn hubs (portals) the connected user belongs to. The hub URL returned here is the value used as the hub or portal identifier by most other Zoho Learn actions. |
| Get Hub Members | `getHubMembers` | Returns the members of a Zoho Learn hub, with pagination. |
| Get Lesson Discussion List | `getLessonDiscussionList` | Returns the discussion threads and replies posted against a lesson in Zoho Learn. |
| Get List Of Course Resources | `getCourseResources` | Returns the files attached as resources to a course in Zoho Learn. |
| Get Manual Information | `getManualInformation` | Returns the details of a manual in Zoho Learn. |
| Get Manuals Shared To Custom Portal | `getManualsSharedToCustomPortal` | Returns the manuals that have been shared with a Zoho Learn custom portal, with pagination. |
| Get Members In A Course | `getCourseMembers` | Returns the members of a course in Zoho Learn along with each member's role and course progress. |
| Get Question Bank | `getQuestionBank` | Returns a single question bank in a Zoho Learn portal, looked up by its question bank URL. |
| Get Quiz Lesson | `getQuizLesson` | Returns a quiz lesson within a course in Zoho Learn, including its questions. |
| Get Space Information | `getSpaceInformation` | Returns the details of a single space in a Zoho Learn hub. |
| Get Space Listing | `getSpaceListing` | Returns the spaces in a Zoho Learn hub, with optional filtering to the current user's spaces, sorting and pagination. |
| Get Space Manual Listing | `getSpaceManualListing` | Returns the manuals inside a space in Zoho Learn, with sorting and pagination. |
| Invite Custom Portal Users | `inviteCustomPortalUsers` | Invites external users to a Zoho Learn custom portal. Up to 100 email addresses can be invited in a single call. |
| Invite Users To Hub | `inviteUsersToHub` | Invites users to a Zoho Learn hub by email. Up to 100 email addresses can be invited in a single call. |
| Mark Learner As Complete | `markLearnerAsComplete` | Marks a learner's progress on a course as complete in Zoho Learn. |
| Mark Learner As Failed | `markLearnerAsFailed` | Marks a learner as having failed a course in Zoho Learn. |
| Mark Learner As In Progress | `markLearnerAsInProgress` | Marks a learner's progress on a course as in progress in Zoho Learn. |
| Reject Custom Portal Signup | `rejectCustomPortalSignup` | Rejects a pending self-signup request for a Zoho Learn custom portal. |
| Remove User From Space | `removeUserFromSpace` | Removes a member from a space in Zoho Learn. |
| Resend Custom Portal Invite | `resendCustomPortalInvite` | Resends a pending invitation to a Zoho Learn custom portal. |
| Search Articles | `searchArticles` | Searches the articles in a Zoho Learn hub by keyword, with optional filtering by author, manual or space, plus sorting and pagination. |
| Search Attachments | `searchAttachments` | Searches the attachments in a Zoho Learn hub by keyword, with optional filtering by author, manual or space, plus sorting and pagination. |
| Search Manuals | `searchManuals` | Searches the manuals in a Zoho Learn hub by keyword, with sorting and pagination. |
| Share Or Remove Manual To Custom Portal | `shareOrRemoveManualToCustomPortal` | Shares manuals with a Zoho Learn custom portal or withdraws manuals already shared with it. |
| Trash Article | `trashArticle` | Moves an article in a Zoho Learn manual to the trash. Sub-levels are trashed too when the recursive option is set, otherwise they move one level up in the content hierarchy. |
| Update Article | `updateArticle` | Updates an existing article in a Zoho Learn manual by importing a replacement document. Notification and mandatory-read reset options apply only when the article is published. The request is multipart/form-data. |
| Update Learner Status | `updateLearnerStatus` | Updates the completion percentage a learner has reached on a lesson in Zoho Learn. |
| Update Question Bank | `updateQuestionBank` | Updates an existing question bank in a Zoho Learn portal. Only the fields supplied are sent. |
| View A Course Report | `viewCourseReport` | Returns the report for a course in Zoho Learn, either per member or per lesson, with optional filtering by completion state, lesson type or specific users. |
| View A Lesson Report | `viewLessonReport` | Returns the learner report for a single lesson in Zoho Learn, with optional progress filtering, user filtering and CSV export. |
| View Course Rating Or Feedback | `viewCourseRating` | Returns the ratings and feedback recorded against a course in Zoho Learn, including the overall rating. |
