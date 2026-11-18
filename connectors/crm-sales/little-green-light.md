---
description: "Little Green Light donor-management CRM for nonprofits."
hidden: true
---

# Little Green Light

Little Green Light donor-management CRM for nonprofits. Wraps the LGL REST API v1 (https://api.littlegreenlight.com/api/v1): constituents and their contact info, gifts and pledges, memberships, events and invitations, volunteer times, campaigns, funds, appeals and appeal requests, groups, relationships, notes, contact reports, categories/keywords, custom attributes, lists, mailing templates and account types. Authenticates with an LGL account API key over Bearer or HTTP Basic. Rate limit: 300 calls per 5 minutes. LGL has no outbound webhooks; poll the /search endpoints with updated_from for change detection.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [littlegreenlight.com](https://littlegreenlight.com) |
| **Authentication** | Basic auth, Bearer token |
| **Actions** | 141 |
| **Events** | 0 |
| **Slug** | `littleGreenLight` |

## Use it

Add Little Green Light from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.littleGreenLight.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Constituent Keyword | `addConstituentKeyword` | Tag a constituent with an existing keyword. The body carries only the keyword id. |
| Create Appeal | `createAppeal` | Create an appeal. Only name is required; link it to a campaign with campaign_id or campaign_name. |
| Create Appeal Request For Appeal | `createAppealRequestForAppeal` | Add an appeal request (an ask on a constituent) under an appeal. constituent_id and appeal_id are both required in the body. |
| Create Campaign | `createCampaign` | Create a fundraising campaign. Only name is required. |
| Create Category | `createCategory` | Create a category (custom field). item_type and name are required. facet_type controls the widget LGL renders (e.g. single_select, multi_select, text, date, number). |
| Create Category Keyword | `createCategoryKeyword` | Add a keyword (selectable value) to a category. category_id and name are required. |
| Create Constituent | `createConstituent` | Create a constituent (individual or organization) with its related objects. first_name, last_name and at least one email address are required by LGL. Nested arrays (email_addresses, phone_numbers, street_addresses, web_addresses, categories, groups, class_affiliations, relationships, custom_attrs) are created alongside the constituent. |
| Create Constituent Appeal Request | `createConstituentAppealRequest` | Add an appeal request (ask) to a constituent. The constituent comes from the path; appeal_id is required in the body. |
| Create Constituent Class Affiliation | `createConstituentClassAffiliation` | Add a class affiliation (class year) to a constituent. Get class_affiliation_type_id from listClassAffiliationTypes. |
| Create Constituent Contact Report | `createConstituentContactReport` | Log a contact report (call, email, meeting, mailing, proposal) against a constituent. text is required; identify the type with contact_report_type_id or contact_report_type_name, and the owner with team_member (id, email or "First Last"). |
| Create Constituent Email Address | `createConstituentEmailAddress` | Add an email address to a constituent. Set is_preferred to make it the primary address. |
| Create Constituent Gift | `createConstituentGift` | Record a gift for a constituent: donation, pledge, pledge payment, in-kind, soft credit or other. gift_type_id AND gift_type_name are both required (read them from listGiftTypes). For a pledge payment, point parent_gift_id or parent_external_id at the pledge. ack_template_name selects the acknowledgement mailing template; pass "do_not_ack" to suppress. |
| Create Constituent Group Membership | `createConstituentGroupMembership` | Add a constituent to a group. group_id is required in the body. |
| Create Constituent Invitation | `createConstituentInvitation` | Invite a constituent to an event, addressed from the constituent side. Constituent from the path, event_id required in the body. rsvp: 1 yes, 2 no, 3 maybe, 4 unknown. |
| Create Constituent Membership | `createConstituentMembership` | Add a membership to a constituent. Identify the level with membership_level_id or membership_level_name (see listMembershipLevels). |
| Create Constituent Note | `createConstituentNote` | Add a note to a constituent. text and original_date are required by LGL. |
| Create Constituent Phone Number | `createConstituentPhoneNumber` | Add a phone number to a constituent. |
| Create Constituent Relationship | `createConstituentRelationship` | Link a constituent to another constituent. related_constituent_id and relationship_type_id identify the other party and the kind of link; auto_soft_credit and also_acknowledge control gift crediting behaviour. |
| Create Constituent Street Address | `createConstituentStreetAddress` | Add a street address to a constituent. seasonal with seasonal_from/seasonal_to marks a snowbird address. |
| Create Constituent Volunteer Time | `createConstituentVolunteerTime` | Log volunteer time for a constituent. constituent_id and volunteering_category_id are required by LGL. |
| Create Constituent Web Address | `createConstituentWebAddress` | Add a web address (website, LinkedIn, Facebook) to a constituent. |
| Create Event | `createEvent` | Create an event. Only name is required. multi_attend allows a constituent to be counted for several attendances. |
| Create Event Invitation | `createEventInvitation` | Invite a constituent to an event. Event from the path, constituent_id required in the body. rsvp: 1 yes, 2 no, 3 maybe, 4 unknown. Use parent_invitation_id with is_a_guest to add an extra guest under an existing invitation. |
| Create Fund | `createFund` | Create a fund. Only name is required; campaign_id or campaign_name links it to a campaign. |
| Create Group | `createGroup` | Create a constituent group. Only name is required. |
| Create Membership Level | `createMembershipLevel` | Create a membership level. ordinal controls its position in LGL's pick lists. |
| Delete Appeal | `deleteAppeal` | Delete an appeal by LGL appeal id. Returns {api_version, result:"success"}. |
| Delete Appeal Request | `deleteAppealRequest` | Delete an appeal request by its LGL id. Returns {api_version, result:"success"}. |
| Delete Campaign | `deleteCampaign` | Delete a campaign by LGL campaign id. Returns {api_version, result:"success"}. |
| Delete Category | `deleteCategory` | Delete a category (custom field) by its LGL id. Returns {api_version, result:"success"}. |
| Delete Class Affiliation | `deleteClassAffiliation` | Delete a class affiliation by its LGL id. Returns {api_version, result:"success"}. |
| Delete Constituent | `deleteConstituent` | Delete a constituent by LGL id. Returns {api_version, result:"success"}. Destructive and not reversible through the API. |
| Delete Constituent Relationship | `deleteConstituentRelationship` | Delete a constituent relationship by its LGL id. Returns {api_version, result:"success"}. |
| Delete Contact Report | `deleteContactReport` | Delete a contact report by its LGL id. Returns {api_version, result:"success"}. |
| Delete Email Address | `deleteEmailAddress` | Delete an email address record by its LGL id. Returns {api_version, result:"success"}. |
| Delete Event | `deleteEvent` | Delete an event by LGL event id. Returns {api_version, result:"success"}. |
| Delete Fund | `deleteFund` | Delete a fund by LGL fund id. Returns {api_version, result:"success"}. |
| Delete Gift | `deleteGift` | Delete a gift by LGL gift id. Returns {api_version, result:"success"}. |
| Delete Group | `deleteGroup` | Delete a constituent group by its LGL id. Returns {api_version, result:"success"}. |
| Delete Group Membership | `deleteGroupMembership` | Remove a constituent from a group by deleting the group membership. Returns {api_version, result:"success"}. |
| Delete Invitation | `deleteInvitation` | Delete an event invitation by its LGL id. Returns {api_version, result:"success"}. |
| Delete Keyword | `deleteKeyword` | Delete a keyword by its LGL id. Pass permanent=1 to hard-delete it rather than retire it. Returns {api_version, result:"success"}. |
| Delete Membership | `deleteMembership` | Delete a membership record by its LGL id. Returns {api_version, result:"success"}. |
| Delete Membership Level | `deleteMembershipLevel` | Delete a membership level by its LGL id. Returns {api_version, result:"success"}. |
| Delete Note | `deleteNote` | Delete a note by its LGL id. Returns {api_version, result:"success"}. |
| Delete Phone Number | `deletePhoneNumber` | Delete a phone number record by its LGL id. Returns {api_version, result:"success"}. |
| Delete Street Address | `deleteStreetAddress` | Delete a street address record by its LGL id. Returns {api_version, result:"success"}. |
| Delete Volunteer Time | `deleteVolunteerTime` | Delete a volunteer time record by its LGL id. Returns {api_version, result:"success"}. |
| Delete Web Address | `deleteWebAddress` | Delete a web address record by its LGL id. Returns {api_version, result:"success"}. |
| Get Appeal | `getAppeal` | Show a single appeal by LGL appeal id. |
| Get Appeal Request | `getAppealRequest` | Show a single appeal request (ask) by its LGL id. |
| Get Campaign | `getCampaign` | Show a single campaign by LGL campaign id. |
| Get Category | `getCategory` | Show a single category (custom field) by its LGL id, including its keywords. |
| Get Class Affiliation | `getClassAffiliation` | Show a single class affiliation by its LGL id. |
| Get Constituent | `getConstituent` | Show a single constituent by LGL constituent id, including its email addresses, phone numbers, street addresses, web addresses, categories, groups and custom attributes. |
| Get Constituent Relationship | `getConstituentRelationship` | Show a single constituent relationship by its LGL id. |
| Get Contact Report | `getContactReport` | Show a single contact report by its LGL id. |
| Get Email Address | `getEmailAddress` | Show a single email address record by its LGL id. |
| Get Event | `getEvent` | Show a single event by LGL event id. |
| Get Fund | `getFund` | Show a single fund by LGL fund id. |
| Get Gift | `getGift` | Show a single gift (donation, pledge, pledge payment, in-kind or soft credit) by LGL gift id. |
| Get Group | `getGroup` | Show a single constituent group by its LGL id. |
| Get Group Membership | `getGroupMembership` | Show a single group membership by its LGL id. |
| Get Invitation | `getInvitation` | Show a single event invitation by its LGL id, including attendances and custom fields. |
| Get Keyword | `getKeyword` | Show a single keyword by its LGL id. |
| Get Membership | `getMembership` | Show a single membership record by its LGL id. |
| Get Membership Level | `getMembershipLevel` | Show a single membership level by its LGL id. |
| Get Note | `getNote` | Show a single note by its LGL id. |
| Get Phone Number | `getPhoneNumber` | Show a single phone number record by its LGL id. |
| Get Street Address | `getStreetAddress` | Show a single street address record by its LGL id. |
| Get Volunteer Time | `getVolunteerTime` | Show a single volunteer time record by its LGL id. |
| Get Web Address | `getWebAddress` | Show a single web address record by its LGL id. |
| List Appeal Requests For Appeal | `listAppealRequestsForAppeal` | Fetch the appeal requests (asks) attached to one appeal, with ask amount, status and the assigned team member. |
| List Appeals | `listAppeals` | Fetch all appeals for the account. An appeal is a specific solicitation (mailing, event push) usually under a campaign. |
| List Campaigns | `listCampaigns` | Fetch all fundraising campaigns for the account. Campaigns are the top level of the campaign &gt; fund &gt; appeal hierarchy. |
| List Categories | `listCategories` | Fetch the categories (LGL's custom fields) for the account, each with its keywords. item_type selects which record the categories belong to: Constituent (default), Gift or VolunteerTime. |
| List Category Keywords | `listCategoryKeywords` | Fetch the keywords (the selectable values) belonging to one category. |
| List Class Affiliation Types | `listClassAffiliationTypes` | Fetch the class affiliation types configured on the account (read-only). |
| List Constituent Appeal Requests | `listConstituentAppealRequests` | Fetch every appeal request (ask) recorded against one constituent. |
| List Constituent Categories | `listConstituentCategories` | Fetch the categories and selected keyword values set on one constituent. |
| List Constituent Class Affiliations | `listConstituentClassAffiliations` | Fetch the class affiliations (alumni class years) recorded for one constituent. |
| List Constituent Contact Reports | `listConstituentContactReports` | Fetch the contact reports logged against one constituent. |
| List Constituent Email Addresses | `listConstituentEmailAddresses` | Fetch the email addresses on one constituent. |
| List Constituent Gifts | `listConstituentGifts` | Fetch all gifts for one constituent. Pledges and pledge payments are gifts too (gift_type_name "Pledge" / "Pledge Payment"; a payment points at its pledge via parent_gift_id). |
| List Constituent Group Memberships | `listConstituentGroupMemberships` | Fetch the groups one constituent belongs to, with join and leave dates. |
| List Constituent Invitations | `listConstituentInvitations` | Fetch every event invitation recorded for one constituent. |
| List Constituent Memberships | `listConstituentMemberships` | Fetch the membership records for one constituent, with level, start and finish dates. |
| List Constituent Notes | `listConstituentNotes` | Fetch the notes recorded on one constituent. |
| List Constituent Phone Numbers | `listConstituentPhoneNumbers` | Fetch the phone numbers on one constituent. |
| List Constituent Relationships | `listConstituentRelationships` | Fetch the relationships (spouse, employer, board colleague) linking one constituent to others. |
| List Constituent Street Addresses | `listConstituentStreetAddresses` | Fetch the street addresses on one constituent, including seasonal address windows. |
| List Constituent Volunteer Times | `listConstituentVolunteerTimes` | Fetch the volunteer time records logged for one constituent. |
| List Constituent Web Addresses | `listConstituentWebAddresses` | Fetch the web addresses (websites, social profiles) on one constituent. |
| List Constituents | `listConstituents` | Fetch all constituents (donors, members, prospects) for the LGL account, newest LGL id first. Paginated with limit/offset; the envelope carries total_items and next_link. |
| List Contact Reports | `listContactReports` | Fetch all contact reports for the account. Contact reports are LGL's logged touchpoints and tasks (call, email, meeting, mailing, proposal). |
| List Custom Attributes | `listCustomAttributes` | Fetch the custom attributes defined on the account. item_type filters by the record they attach to (Constituent, Gift, Invitation, AppealRequest). Read-only: LGL exposes no create, update or delete for attributes. |
| List Event Invitations | `listEventInvitations` | Fetch the invitations (event attendees) for one event, with RSVP and attendance state. |
| List Events | `listEvents` | Fetch all fundraising events (galas, dinners, walks) for the account. |
| List Funds | `listFunds` | Fetch all funds for the account. A fund is the designation money is given to, optionally under a campaign. |
| List Gift Categories | `listGiftCategories` | Fetch the gift categories on the account, optionally filtered to one gift type. |
| List Gift Types | `listGiftTypes` | Fetch the gift types on the account (Gift, Pledge, Pledge Payment, In Kind, Soft Credit, Other). Both gift_type_id and gift_type_name from here are required when creating a gift. |
| List Groups | `listGroups` | Fetch the constituent groups (board, committees, volunteers) defined on the account. |
| List Lists | `listLists` | Fetch the constituent lists (saved segments, mailing lists) on the account. |
| List Mailing Templates | `listMailingTemplates` | Fetch the mailing templates on the account - this is where acknowledgement templates live (e.g. "Pledge Acknowledgment", code pledge_ack). Pass a template's name as ack_template_name on a gift to pick the acknowledgement, or "do_not_ack" to suppress it. Filter with mailing_type_id. |
| List Membership Levels | `listMembershipLevels` | Fetch the membership levels configured on the account. Use these ids when creating a membership. |
| List Notes | `listNotes` | Fetch all notes for the account. |
| List Payment Types | `listPaymentTypes` | Fetch the payment types on the account (cash, check, credit card, ...). Use these ids on gifts. |
| List Relationship Types | `listRelationshipTypes` | Fetch the relationship types configured on the account (read-only). Use these ids when creating a constituent relationship. |
| List Team Members | `listTeamMembers` | Fetch the LGL account's team members (staff users). Their ids and emails are what assigned_to and team_member fields on appeal requests, contact reports and gifts refer to. |
| List Type Values | `listTypeValues` | Fetch the values of one pick-list type by its key, e.g. contact_report_types, note_types, email_address_types, phone_number_types, street_address_types, web_address_types, event_types, appeal_types, volunteering_categories, marital_statuses. Read the available keys from listTypes. |
| List Types | `listTypes` | Fetch every pick-list type on the account with its values in one call - contact report types, note types, email/phone/street/web address types, event types, appeal types, volunteering categories, marital statuses and more. This is the lookup table behind most *_type_id fields. |
| List Volunteer Times | `listVolunteerTimes` | Fetch all volunteer time records for the account. |
| Remove Constituent Keyword | `removeConstituentKeyword` | Remove a keyword from a constituent. Deletes the tag, not the keyword itself. Returns {api_version, result:"success"}. |
| Search Constituents | `searchConstituents` | Search active constituents. The q[] value is one or more term=value pairs joined by semicolons, e.g. name=brady, eaddr=@acme.com, updated_from=2026-01-01T00:00:00Z;updated_to=2026-02-01T00:00:00Z. Terms: name, eaddr, phone_number, street, city, state, postal_code, country, keyword, updated_from, updated_to, membership_status (0 lapsed, 1 active), membership_level, membership_end_date_from, membership_end_date_to, external_id (op\|value, ops eq ne co nc bl nb), constituent_type (0 individual, 1 organization), groups, class, custom_attr (key\|op\|value), custom_attr_from, custom_attr_to, custom_attr_int. This is the endpoint to poll for change detection since LGL has no webhooks. |
| Search Contact Reports | `searchContactReports` | Search contact reports. q[] takes term=value pairs joined by semicolons. Terms: original_date_from, original_date_to, name, text, contact_report_type_id (comma separated), constituent_id (comma separated), const_keyword, updated_from, updated_to. |
| Search Gifts | `searchGifts` | Search gifts across the account. q[] takes term=value pairs joined by semicolons. Terms: date_from, date_to (YYYY-MM-DD), gift_types (op\|ids, ops in/ni), gift_amount (op\|number[\|number2], ops gte lte btw gt lt eq ne), payment_types, campaigns, funds, appeals, appeal_types, events, event_types, categories (each op\|ids with in/ni/bl), constituent_type (0 individual, 1 organization), gift_ids, external_gift_ids, created_from, created_to, updated_from, updated_to. Example: q[]=gift_amount=btw\|100\|1000. Use updated_from to poll for new and changed gifts. |
| Search Lists | `searchLists` | Search constituent lists. q[] takes term=value pairs joined by semicolons. Terms: name, list_type_id, is_favorite (true/false). Example: q[]=name=Board members. |
| Search Volunteer Times | `searchVolunteerTimes` | Search volunteer time records. q[] takes term=value pairs joined by semicolons. Terms: date_from, date_to, description, volunteering_category_id (comma separated), constituent_id (comma separated), external_id (op\|ids, ops in ni bl nb), const_keyword, updated_from, updated_to. |
| Update Appeal | `updateAppeal` | Update an appeal (PATCH, partial). name is required by LGL's schema on every update. |
| Update Appeal Request | `updateAppealRequest` | Update an appeal request (PATCH, partial). constituent_id and appeal_id are required by LGL's schema on every update. |
| Update Campaign | `updateCampaign` | Update a campaign (PATCH, partial). name is required by LGL's schema on every update. |
| Update Category | `updateCategory` | Update a category (PATCH, partial). item_type and name are required by LGL's schema on every update. |
| Update Class Affiliation | `updateClassAffiliation` | Update a class affiliation (PATCH, partial). |
| Update Constituent | `updateConstituent` | Update a constituent (PATCH, partial). Only the fields you send are changed, but sending an empty string overwrites the stored value. Nested arrays are appended unless the matching remove_previous_* flag is true, which replaces the whole set. LGL's schema also lists email_addresses as required; omit it to leave the existing addresses untouched. |
| Update Constituent Relationship | `updateConstituentRelationship` | Update a constituent relationship (PATCH, partial). |
| Update Contact Report | `updateContactReport` | Update a contact report (PATCH, partial). text is required by LGL's schema on every update. |
| Update Email Address | `updateEmailAddress` | Update an email address record (PATCH, partial). |
| Update Event | `updateEvent` | Update an event (PATCH, partial). name is required by LGL's schema on every update. |
| Update Fund | `updateFund` | Update a fund (PATCH, partial). name is required by LGL's schema on every update. |
| Update Gift | `updateGift` | Update a gift (PATCH, partial). gift_type_id and gift_type_name must both be sent, matching each other. Sending an empty string overwrites the stored value. |
| Update Group | `updateGroup` | Update a constituent group (PATCH, partial). name is required by LGL's schema on every update. |
| Update Group Membership | `updateGroupMembership` | Update a group membership (PATCH, partial) - end a membership by setting date_end and is_current false. group_id is required by LGL's schema on every update. |
| Update Invitation | `updateInvitation` | Update an event invitation (PATCH, partial) - typically to set rsvp or attended. constituent_id is required by LGL's schema on every update. |
| Update Keyword | `updateKeyword` | Update a keyword (PATCH, partial). category_id and name are required by LGL's schema on every update. |
| Update Membership | `updateMembership` | Update a membership record (PATCH, partial) - renew it by moving finish_date, or change the level. |
| Update Membership Level | `updateMembershipLevel` | Update a membership level (PATCH, partial). name is required by LGL's schema on every update. |
| Update Note | `updateNote` | Update a note (PATCH, partial). text and original_date are required by LGL's schema on every update. |
| Update Phone Number | `updatePhoneNumber` | Update a phone number record (PATCH, partial). |
| Update Street Address | `updateStreetAddress` | Update a street address record (PATCH, partial). |
| Update Volunteer Time | `updateVolunteerTime` | Update a volunteer time record (PATCH, partial). constituent_id and volunteering_category_id are required by LGL's schema on every update. |
| Update Web Address | `updateWebAddress` | Update a web address record (PATCH, partial). |
