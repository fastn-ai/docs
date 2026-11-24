# Docs backlog: screenshots and checks
Moved out of the published pages on 2026-11-04 so readers no longer see writer notes. Not published (not in SUMMARY.md).

## tutorials/developer/generating-embed-tokens.md
- line 54: > **VERIFY:** The Embed tab UI shows the token request with only `Authorization: Bearer YOUR_API_KEY` and references a `YOUR_CUSTOMER_ID` parameter, while the hands-on integration used a body of `{ endOrgId, userEmail, userName }` and read the token from `data.token`. Confirm the exact request body and response shape against the current API before publishing - the UI snippet and the hands-on resul
- line 66: > **VERIFY:** The refresh endpoint exists (confirmed on the platform). Confirm its exact request and response shape, and whether the SDK (when it ships) handles auto-refresh automatically.

## tutorials/end-user/connecting-apps-via-widget.md
- line 23: > **Screenshot:** Example of an embedded widget as it appears inside a SaaS product - showing the integration hub with available app icons and connect buttons.
- line 80: > **Screenshot:** Widget showing a connected app with the Disconnect button visible.

## tutorials/saas-admin/building-your-widget.md
- line 163: Shows performance metrics for the customer's integrations with a time-range selector (7 days / 30 days / 90 days). \[VERIFY: what specific KPI cards appear here? Events processed, sync success rate, active connections, error count?]

## tutorials/saas-admin/configuring-a-connector.md
- line 31: > **Screenshot:** Create Connector dialog with all fields filled in.
- line 41: > **Screenshot:** Connector Agent page with the chat input and quick-start prompts.
- line 60: > **Screenshot:** Auth Methods dropdown showing all 6 options.

## tutorials/saas-admin/configuring-a-workflow-in-code.md
- line 17: > **Screenshot:** Full workflow editor showing all three panels - Configuration (left), Code (center), Test (right).
- line 149: > **Screenshot:** Test panel with sample input JSON and the output result after running.
- line 173: > **Screenshot:** Workflows table showing the newly created workflow with active status.

## tutorials/saas-admin/creating-a-workflow-via-ai.md
- line 25: > **Screenshot:** Standalone Workflow Builder page showing the chat input, quick-start prompts, and the left sidebar with builder info and tasks.

## tutorials/saas-admin/managing-customers.md
- line 68: > **Screenshot:** Customize Customer Limits interface showing per-customer quota overrides.
- line 78: > **Screenshot:** Activity → Executions filtered to show a specific customer's workflow runs.

## tutorials/saas-admin/roles-and-permissions-setup.md
- line 22: > **Screenshot:** Settings → ADVANCED → Roles showing the 6 built-in roles with permission counts.
- line 48: > **Screenshot:** Role detail view for "Admin" showing the permission categories with checkboxes - Connectors 6/6, Connections 6/6, Workflows 7/7, Agents 5/5, Tools 5/5.
- line 61: > **Screenshot:** Settings → People showing the role badge on a user and the filter dropdowns.
- line 79: > **Screenshot:** Create Custom Role form or the "Duplicate as Custom" button on a built-in role.
- line 95: > **Screenshot:** Audit Log showing entries with timestamp, user, action, resource, and outcome columns.

## tutorials/saas-admin/setting-up-triggers.md
- line 19: > **Screenshot:** Triggers page showing the three tabs and the Add Trigger type selection panel.
- line 83: > **Screenshot:** Scheduler trigger configuration showing the preset buttons (Interval, Daily, Weekly, Monthly, Custom) and the interval settings.
- line 109: > **Screenshot:** App Event trigger configuration showing the Connector dropdown, Connection dropdown, and the event list with event names, WEBHOOK badges, and subscription status.

## tutorials/saas-admin/setting-up-your-organization.md
- line 32: > **Screenshot:** Settings → General showing Organization Name, Timezone, Domain & Access Control, and the Company Research Report card with the "View research report" button.

## tutorials/saas-admin/configuring-a-connector.md
- > &#x20;**GIF needed:** Using Build with AI - entering a connector name, watching it discover the API and build actions.

## tutorials/saas-admin/managing-customers.md
- > &#x20;**Screenshot:** Operate → Customers showing the Create customer button and the creation form.
- > &#x20;**Screenshot:** Customer list showing created customers with their IDs.

## tutorials/saas-admin/configuring-a-connector.md
- > **GIF:** Adding a connection - clicking Connect on a connector card, completing OAuth, seeing the connected state.
