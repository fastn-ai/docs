---
description: "SAP SuccessFactors Incentive Management - the incentive compensation product formerly sold as SAP Commissions and, before SAP acquired CallidusCloud in 2018,…"
hidden: true
---

# SAP Incentive Management (CallidusCloud Commissions)

<img src="../../.gitbook/assets/connectors/lg/sap-callidus-cloud.png" alt="SAP Incentive Management (CallidusCloud Commissions) logo">

SAP SuccessFactors Incentive Management - the incentive compensation product formerly sold as SAP Commissions and, before SAP acquired CallidusCloud in 2018, as Callidus Commissions / TrueComp. Its REST API is still served per tenant from https://&lt;tenant&gt;.callidusondemand.com (newer tenants: https://&lt;tenant&gt;.app.commissions.cloud.sap). Covers the shipped v2 API: credits, sales transactions and orders, deposits, balances, commissions, incentives, measurements, payments, participants, positions, titles, business units, users and groups, quotas, calendars and periods, customers, products, categories and classifiers, territories, variables, earning codes, event types, reasons, audit and message logs, and pipeline jobs (classify, allocate, reward, pay, compensate and pay, import, reset, purge). CallidusCloud CPQ (now SAP CPQ) and Litmos (divested 2022) are separate products needing separate connectors. No webhook API exists - poll with $filter or audit logs.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [callidusondemand.com](https://callidusondemand.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `sapCallidusCloud` |

## Use it

Add SAP Incentive Management (CallidusCloud Commissions) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.sapCallidusCloud.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Approve Calculated Data | `approveCalculatedData` | Submit a pipeline job that approves all calculated data for a period, locking the results so they can be posted and paid. |
| Create Business Unit | `createBusinessUnit` | Create a business unit under a processing unit. Business units partition the tenant's data for security and for rule scoping. |
| Create Calendar | `createCalendar` | Create a calendar with a minor and a major period type. Periods are added separately with Create Period. |
| Create Category | `createCategory` | Create an effective-dated category rule element. |
| Create Category Classifier | `createCategoryClassifier` | Assign a classifier (a product, customer or postal code) into a category on a category tree. This is how a newly synced product or customer becomes creditable in the compensation model, and it was the largest missing integration write. SAP does not publish a typed request body for any v2 write, so the field names are taken from the GetCategoryClassifier response contract. category, categoryTree and classifier are passed as JSON object strings and emitted verbatim, matching how the shipped actions pass lookup objects. |
| Create Category Tree | `createCategoryTree` | Create a category tree: the hierarchy that categories hang off. This closes a dependency gap - Create Category was already shipped but the category's owner is a category tree, and there was no way to create one. classifierClass names the object being classified, e.g. a product or a customer. SAP does not publish a typed request body for any v2 write, so the field names are taken from the GetCategoryTree response contract; the error contract states the required field is name. |
| Create Credit | `createCredit` | Create a direct transaction credit. The API accepts a JSON array so the request always posts one credit. Reference fields (position, period, creditType) are given by name or by seq. The credit period must contain the compensation date and the business units of position and transaction must be compatible. |
| Create Credit Type | `createCreditType` | Create a credit type. creditTypeId is the logical key credits reference. |
| Create Customer | `createCustomer` | Create an effective-dated customer classifier. classifierId is the logical key that sales transactions reference. |
| Create Deposit | `createDeposit` | Create a deposit against a position for a period - for example a manual bonus or draw. The deposit date must fall inside the period. |

<details>

<summary>See 194 more actions</summary>

* **Create Earning Code** `createEarningCode`: Create an earning code that deposits and payments can be classified with.
* **Create Earning Group** `createEarningGroup`: Create an earning group that deposits, balances and payments accumulate into.
* **Create Event Type** `createEventType`: Create an event type that sales transactions can be classified with.
* **Create Fixed Value** `createFixedValue`: Create a fixed value: a named plan constant such as a rate, threshold or target, referenced by compensation rules. Fixed values were list-only before this. Note that value and unitTypeSeq are flat here, unlike credits where money is a nested Value object. SAP does not publish a typed request body for any v2 write, so the field names are taken from the GetFixedValue response contract; the error contract states the required field is name.
* **Create Group** `createGroup`: Create a user group. The group carries the permission policy applied to its members.
* **Create Participant** `createParticipant`: Create a participant (payee). payeeId is the logical key and must be unique. Participants are effective dated - effectiveStartDate and effectiveEndDate define the first version. userId links the participant to the tenant user that signs in to the portal.
* **Create Period** `createPeriod`: Create a period on a calendar. The period type must be one of the calendar's minor or major period types and the dates must not overlap an existing period of that type.
* **Create Position** `createPosition`: Create a position. name plus the effective dates form the logical key. The payee, title and processing unit are given by name or by seq; the title supplies the compensation plan unless the position overrides it.
* **Create Position Group** `createPositionGroup`: Create an effective-dated position group that pipeline runs can target.
* **Create Position Relation** `createPositionRelation`: Link a child position to a parent position for an effective period, forming the rollup hierarchy. The relation type decides how credit rolls up.
* **Create Processing Unit** `createProcessingUnit`: Create a processing unit. Business units, positions and pipeline runs can then be scoped to it.
* **Create Product** `createProduct`: Create an effective-dated product classifier. classifierId is the logical key that sales transactions reference through productId.
* **Create Quota** `createQuota`: Create a quota definition against a calendar. The quota holds no numbers itself - per-position targets are loaded separately against its periods.
* **Create Reason** `createReason`: Create a reason code for manual credits, deposits and adjustments.
* **Create Sales Order** `createSalesOrder`: Create a sales order header. Create the order before posting its sales transaction lines. orderId must be unique within the tenant.
* **Create Sales Transaction** `createSalesTransaction`: Create a sales transaction line against an existing sales order. Numeric fields are sent as value objects with a unit type; lineNumber and sublineNumber use the tenant's numeric unit type (NUMBER by default - change it if your tenant renamed it). The sales order must already exist.
* **Create Territory** `createTerritory`: Create an effective-dated territory rule element. The selection expression itself is normally authored in the tenant's rule designer afterwards.
* **Create Title** `createTitle`: Create an effective-dated title. Assign the compensation plan to the title so that every position holding it inherits the plan.
* **Create User** `createUser`: Create a tenant user. id is the login name and must be unique. Grant permissions by adding the user to a group afterwards.
* **Create Variable** `createVariable`: Create a plan variable. Variables were list-only before this. referenceClassType selects the underlying variable kind, e.g. com.callidus.fixedvalue.FixedValue, and is what distinguishes a variable from the fixedValueVariables, rateTableVariables, lookUpTableVariables and territoryVariables endpoints, which share this same schema. SAP does not publish a typed request body for any v2 write, so the field names are taken from the GetVariable response contract; the error contract states the required field is name.
* **Delete Calendar** `deleteCalendar`: Delete a calendar by its calendarSeq. Fails while periods, quotas or pipeline runs reference it.
* **Delete Category** `deleteCategory`: Delete a category by its ruleElementSeq. Fails while rules or category trees reference it.
* **Delete Credit Type** `deleteCreditType`: Delete a credit type by its dataTypeSeq. Fails while credits still reference it.
* **Delete Customer** `deleteCustomer`: Delete a customer by its classifierSeq. Fails while transactions or category trees still reference it.
* **Delete Fixed Value** `deleteFixedValue`: Delete one or more fixed values. The id path segment accepts a comma-separated list of fixed value IDs.
* **Delete Group** `deleteGroup`: Delete a user group by its groupSeq. Fails while users are still members.
* **Delete Participant** `deleteParticipant`: Delete a participant by payeeSeq. Fails with a referred-by error while positions, credits or payments still reference the participant.
* **Delete Period** `deletePeriod`: Delete a period by its periodSeq. Fails while credits, payments or pipeline runs reference it.
* **Delete Position** `deletePosition`: Delete a position by its seq. Fails with a referred-by error while credits, quotas, position relations or payments still reference it.
* **Delete Position Group** `deletePositionGroup`: Delete a position group by its seq.
* **Delete Position Relation** `deletePositionRelation`: Delete a position relation by its seq, breaking that link in the rollup hierarchy.
* **Delete Product** `deleteProduct`: Delete a product by its classifierSeq. Fails while transactions or category trees still reference it.
* **Delete Quota** `deleteQuota`: Delete a quota by its quotaSeq. Fails while plan rules still reference it.
* **Delete Sales Order** `deleteSalesOrder`: Delete a sales order by salesOrderSeq. Fails while transaction lines still reference it.
* **Delete Sales Transaction** `deleteSalesTransaction`: Delete a sales transaction line by salesTransactionSeq. Fails if the line has already been processed into credits that were not reset.
* **Delete Scheduled Pipeline Run** `deletePipelineRun`: Delete a scheduled pipeline job that has not started yet, by its pipelineRunSeq.
* **Delete Territory** `deleteTerritory`: Delete a territory by its ruleElementSeq. Fails while rules still reference it.
* **Delete Title** `deleteTitle`: Delete a title by its seq. Fails while positions still hold the title.
* **Delete User** `deleteUser`: Delete a tenant user by its userSeq. Fails while participants still reference the user id.
* **Delete Variable** `deleteVariable`: Delete one or more plan variables. The id path segment accepts a comma-separated list of variable IDs, per the SAP parameter description "List of Variable's IDs (separated by comma)".
* **Download Audit Logs** `downloadAuditLogs`: Download audit logs for a date range as a CSV file. The range may not exceed three days. The response is text/csv rather than JSON, so treat the body as raw text.
* **Download Message Logs** `downloadMessageLogs`: Download message logs for a date range as a CSV file. The response is text/csv rather than JSON, so treat the body as raw text.
* **Get Applied Deposit** `getAppliedDeposit`: Read one applied deposit by its seq.
* **Get Audit Log** `getAuditLog`: Read one audit log entry by its seq.
* **Get Balance** `getBalance`: Read one balance record by its balanceSeq.
* **Get Business Unit** `getBusinessUnit`: Read one business unit by its businessUnitSeq.
* **Get Calendar** `getCalendar`: Read one calendar by its calendarSeq, including its period list.
* **Get Category** `getCategory`: Read one category by its ruleElementSeq.
* **Get Category Classifier** `getCategoryClassifier`: Read a single category classifier assignment by id. List Category Classifiers was already shipped; this is the by-id read.
* **Get Category Tree** `getCategoryTree`: Read one category tree by its categoryTreeSeq.
* **Get Commission** `getCommission`: Read one commission result by its commissionSeq.
* **Get Contract** `getContract`: Read one producer contract by its contractSeq.
* **Get Credit** `getCredit`: Read every attribute of one credit by its creditSeq, including custom detail fields.
* **Get Credit Type** `getCreditType`: Read one credit type by its dataTypeSeq.
* **Get Customer** `getCustomer`: Read one customer by its classifierSeq, including custom detail fields.
* **Get Deposit** `getDeposit`: Read one deposit by its depositSeq.
* **Get Event Type** `getEventType`: Read one event type by its dataTypeSeq.
* **Get Fixed Value** `getFixedValue`: Read one fixed value by its ruleElementSeq.
* **Get Group** `getGroup`: Read one user group by its groupSeq.
* **Get Incentive** `getIncentive`: Read one incentive result by its incentiveSeq.
* **Get Measurement** `getMeasurement`: Read one measurement by its measurementSeq.
* **Get Message** `getMessage`: Read one processing message by its seq.
* **Get Message Log** `getMessageLog`: Read one message log entry by its seq.
* **Get Participant** `getParticipant`: Read one participant by payeeSeq, including custom detail fields.
* **Get Payment** `getPayment`: Read one payment record by its paymentSeq.
* **Get Payment Summary** `getPaymentSummary`: Read one payment summary by its seq.
* **Get Period** `getPeriod`: Read one period by its periodSeq.
* **Get Period Type** `getPeriodType`: Read one period type by its periodTypeSeq.
* **Get Pipeline Run Messages** `getPipelineMessages`: Retrieve the error and warning messages produced by a pipeline job. Use this to diagnose a run that finished with numErrors greater than zero.
* **Get Pipeline Run Positions** `getPipelinePositions`: List the positions that a completed pipeline job actually processed. Useful for confirming the scope of a positions-mode run.
* **Get Pipeline Run Status** `getPipelineStatus`: Retrieve the status of a pipeline job. Poll this after submitting a run until state is Done; status then says whether it succeeded, and numErrors and numWarnings summarise the messages.
* **Get Position** `getPosition`: Read one position by its ruleElementOwnerSeq, including its variable assignments and custom detail fields.
* **Get Position Group** `getPositionGroup`: Read one position group by its positionGroupSeq.
* **Get Position Relation** `getPositionRelation`: Read one position relation by its positionRelationSeq.
* **Get Postal Code** `getPostalCode`: Read one postal code classifier by its classifierSeq.
* **Get Primary Measurement** `getPrimaryMeasurement`: Read one primary measurement by its seq.
* **Get Processing Unit** `getProcessingUnit`: Read one processing unit by its processingUnitSeq.
* **Get Producer** `getProducer`: Read one producer by its producerSeq, including custom detail fields.
* **Get Product** `getProduct`: Read one product by its classifierSeq, including custom detail fields.
* **Get Quota** `getQuota`: Read one quota definition by its quotaSeq.
* **Get Quota Values For Positions** `getQuotaValues`: Return the quota values held by one or more positions for a given quota. Pass the position sequences as a comma separated list.
* **Get Sales Order** `getSalesOrder`: Read one sales order by its salesOrderSeq, including custom detail fields.
* **Get Sales Transaction** `getSalesTransaction`: Read one sales transaction line by its salesTransactionSeq, including custom detail fields and transaction assignments.
* **Get Secondary Measurement** `getSecondaryMeasurement`: Read one secondary measurement by its seq.
* **Get Territory** `getTerritory`: Read one territory by its ruleElementSeq, including its rule definition.
* **Get Title** `getTitle`: Read one title by its seq, including its plan and variable assignments.
* **Get User** `getUser`: Read one tenant user by its userSeq.
* **Get Variable** `getVariable`: Read one plan variable by its ruleElementSeq.
* **List Applied Deposits** `listAppliedDeposits`: List applied deposits - the records showing which deposits were consumed against which payments during the pay stage. Read-only.
* **List Appointment Lines** `listAppointmentLines`: List appointment lines - the per-line-of-authority detail rows under a producer appointment.
* **List Appointment Types** `listAppointmentTypes`: List appointment types available to producer appointments.
* **List Appointments** `listAppointments`: List appointments - the carrier appointments held by a producer in the Producer Management module.
* **List Audit Logs** `listAuditLogs`: List audit log entries - who changed which object and when. This is the main polling seam for change detection, since the API publishes no webhooks.
* **List Balances** `listBalances`: List balances - the carried-forward outstanding amounts per position, earning group and period. Read-only.
* **List Business Units** `listBusinessUnits`: List business units - the data partitions that scope which records a user and a rule can see. Almost every object carries a businessUnits list.
* **List Calendars** `listCalendars`: List calendars. A calendar defines the major and minor period types (for example quarter and month) and owns the periods that pipeline runs are executed for.
* **List Categories** `listCategories`: List categories - the effective-dated rule elements that classify transactions into groupings a plan rule can select on.
* **List Category Classifiers** `listCategoryClassifiers`: List category classifier links - the rows that place a customer, product or other classifier inside a category.
* **List Category Trees** `listCategoryTrees`: List category trees - the hierarchies that organise classifiers such as customers, products and postal codes into a selectable structure.
* **List Commissions** `listCommissions`: List commission results - the output of commission rules for a position and period, before they are rolled into a deposit or payment. Read-only.
* **List Continuing Education** `listContinuingEducation`: List continuing education records - the training credits a producer has completed towards license renewal.
* **List Contract Types** `listContractTypes`: List contract types available to producer contracts.
* **List Contracts** `listContracts`: List contracts - the effective-dated agreements held by producers in the Producer Management module.
* **List Credit Types** `listCreditTypes`: List credit types - the classifications (for example Direct, Indirect, Overlay) that every credit carries.
* **List Credits** `listCredits`: List credits. A credit is the result of a credit rule attributing a sales transaction to a position or payee. Returns standard and custom detail fields. Paginate with top (max 100) and skip, or follow the next link in the response.
* **List Customers** `listCustomers`: List customers - the effective-dated customer classifier used by territory and credit rules to decide who a transaction belongs to.
* **List Deposits** `listDeposits`: List deposits - amounts placed into a position's earning group for a period, such as a draw, a bonus or a manual adjustment that bypasses the credit and commission rules.
* **List Earning Codes** `listEarningCodes`: List earning codes - the payroll-facing classification carried by deposits and payments, for example Commission, Bonus or Draw.
* **List Earning Group Codes** `listEarningGroupCodes`: List earning group codes - the mapping rows that say which earning codes belong to which earning group.
* **List Earning Groups** `listEarningGroups`: List earning groups - the buckets that deposits, balances and payments are accumulated into before payout.
* **List Event Types** `listEventTypes`: List event types - the classification every sales transaction carries, for example Booking, Invoice or Cancellation. Credit rules select on it.
* **List Fixed Value Types** `listFixedValueTypes`: List fixed value types - the tenant-defined data types a fixed value variable can hold.
* **List Fixed Value Variables** `listFixedValueVariables`: List fixed value variables - plan variables whose assigned value is a constant, such as a target incentive percentage.
* **List Fixed Values** `listFixedValues`: List fixed values - the constants assigned to fixed value variables for a position or title over an effective period. Read-only.
* **List Generic Classifier Types** `listGenericClassifierTypes`: List generic classifier types - the tenant-defined classifier dimensions available to classification rules. Read-only.
* **List Generic Classifiers** `listGenericClassifiers`: List generic classifiers - the tenant-defined classification dimensions beyond customer, product and postal code.
* **List Global Field Names** `listGlobalFieldNames`: List global field names - the tenant's labels for the generic attribute, number, date and boolean custom fields carried by most objects.
* **List Groups** `listGroups`: List user groups - the permission policies users are assigned to.
* **List Incentives** `listIncentives`: List incentive results - the output of incentive rules for a position and period. Read-only.
* **List Jurisdictions** `listJurisdictions`: List jurisdictions - the regulatory territories (states, provinces) that producer licenses and appointments are issued in.
* **List License Lines** `listLicenseLines`: List license lines - the per-line-of-authority detail rows under a producer license.
* **List License Types** `listLicenseTypes`: List license types available to producer licenses.
* **List Licenses** `listLicenses`: List licenses - the regulatory licenses held by producers in the Producer Management module.
* **List Lines Of Authority** `listLineOfAuthorities`: List lines of authority - the regulated product lines a producer license or appointment can cover.
* **List Lookup Table Variables** `listLookUpTableVariables`: List lookup table variables - plan variables that resolve a value from a multi-dimensional lookup table.
* **List Measurements** `listMeasurements`: List measurements - the aggregated attainment figures a plan rule computed for a position and period, such as total revenue or units against quota. Read-only.
* **List Message Logs** `listMessageLogs`: List message log entries - the persisted system log of processing messages. Read-only.
* **List Messages** `listMessages`: List processing messages raised by rules and pipeline stages. Read-only.
* **List Participant Versions** `listParticipantVersions`: List every effective-dated version of one participant, optionally narrowed to versions overlapping a date range.
* **List Participants** `listParticipants`: List participants (payees) - the people who earn incentives. Participants are effective dated, so a person can have several versions; this returns the version effective today unless a filter narrows it.
* **List Payment Mappings** `listPaymentMappings`: List payment mappings - the rules that copy an attribute from a source table onto the payment record, used to carry extra fields into payroll extracts.
* **List Payment Summaries** `listPaymentSummaries`: List payment summaries - the aggregated per-position, per-period payable totals used for payroll extracts. Read-only.
* **List Payments** `listPayments`: List payment records produced by the pay stage - the per-position, per-period amounts that go to payroll. Read-only.
* **List Period Types** `listPeriodTypes`: List period types - the granularities (month, quarter, year and any custom ones) a calendar can be built from. Read-only.
* **List Periods** `listPeriods`: List periods. Every pipeline run is submitted for a period of a calendar, so this is usually the first call in a compensation run - filter by calendar name and period name to find the periodSeq.
* **List Position Groups** `listPositionGroups`: List position groups - named sets of positions used to scope a pipeline run to part of the organisation.
* **List Position Relation Types** `listPositionRelationTypes`: List position relation types - the classifications (for example Reports To, Overlay) available when linking positions.
* **List Position Relations** `listPositionRelations`: List position relations - the effective-dated parent/child links that build the rollup hierarchy used by manager and team credit rules.
* **List Position Versions** `listPositionVersions`: List every effective-dated version of one position, optionally narrowed to a date range. Use this to see when a position changed hands or changed title.
* **List Positions** `listPositions`: List positions - the effective-dated slots in the sales organisation that a participant is assigned to and that compensation plans attach to. Credits, quotas and payments all hang off a position, not directly off a person.
* **List Postal Codes** `listPostalCodes`: List postal code classifiers - the effective-dated geography records territory rules select on.
* **List Primary Measurements** `listPrimaryMeasurements`: List primary measurements - the measurement rows that feed the main attainment calculation. Read-only.
* **List Processing Units** `listProcessingUnits`: List processing units - the top-level partitions a pipeline run can be scoped to when multi-tenant processing is enabled.
* **List Producer Address Types** `listProducerAddressTypes`: List producer address types - the classifications (for example Business, Mailing) available to producer addresses.
* **List Producer Addresses** `listProducerAddresses`: List producer addresses - the effective-dated address records attached to producers in the Producer Management module.
* **List Producer Types** `listProducerTypes`: List producer types - the classifications available to producers in the Producer Management module.
* **List Producers** `listProducers`: List producers - the insurance-industry equivalent of a participant, used by the licensed Producer Management module. Only populated on tenants that licence that module.
* **List Products** `listProducts`: List products - the effective-dated product classifier with cost and price, used by classification rules to route transactions to the right credit rule.
* **List Quotas** `listQuotas`: List quotas - the effective-dated targets attached to a calendar that plan rules measure attainment against.
* **List Rate Table Variables** `listRateTableVariables`: List rate table variables - plan variables that resolve to a commission rate table, typically a tiered attainment schedule.
* **List Reasons** `listReasons`: List reason codes - the justifications attached to manual credits, deposits and adjustments.
* **List Sales Orders** `listSalesOrders`: List sales orders. A sales order is the header that groups sales transaction lines and carries the external order id.
* **List Sales Transactions** `listSalesTransactions`: List sales transaction lines - the raw revenue events that credit rules run against. Each line belongs to a sales order and carries a value, a compensation date and an event type. Use a small top value when expanding references; large pages are slow on this resource.
* **List Secondary Measurements** `listSecondaryMeasurements`: List secondary measurements - the supporting measurement rows used by modifier and multiplier rules. Read-only.
* **List Status Codes** `listStatusCodes`: List status codes - the workflow states available to approval and producer processes.
* **List Territories** `listTerritories`: List territories - the effective-dated rule elements whose definition decides which transactions belong to which position.
* **List Territory Variables** `listTerritoryVariables`: List territory variables - the plan variables whose value is a territory, assigned per position or title.
* **List Titles** `listTitles`: List titles - effective-dated job titles that carry a compensation plan and its variable assignments. Positions inherit their plan from their title.
* **List Users** `listUsers`: List tenant users - the login accounts for the sales portal and the API, with their group memberships and business unit access lists.
* **List Variables** `listVariables`: List plan variables - the named inputs a compensation rule reads, assigned to positions and titles through variable assignments.
* **Purge Approved Data** `purgeApprovedData`: Submit a pipeline job that resets and purges all approved data produced by successful runs for a period. Destructive - the results have to be recalculated afterwards.
* **Reset From Classify** `resetFromClassify`: Submit a pipeline job that resets all results from the classification stage forward for a period, so the period can be recalculated from scratch.
* **Reset From Validate** `resetFromValidate`: Submit a pipeline job that validates and resets staged import data for a period. Pass the batch name to reset only the rows imported under that batch.
* **Run Import Pipeline** `runImportPipeline`: Submit an Import pipeline job that moves a named batch out of the stage tables into live data. stageTypeSeq picks the import stage: Validate 21673573206720533, Transfer 21673573206720534, ValidateAndTransfer 21673573206720536, ValidateAndTransferIfAllValid 21673573206720537, TransferIfAllValid 21673573206720535. module is one of TransactionalData, OrganizationData, ClassificationData, PlanRelatedData.
* **Run Pipeline** `runPipeline`: Submit a PipelineRun job for one period and return the created pipeline run. stageTypeSeq picks the stage: Classify 21673573206720515, Allocate 21673573206720516, Reward 21673573206720518, Pay 21673573206720519, Compensate 21673573206720530, Summarize 21673573206720531, CompensateAndPay 21673573206720532, ResetFromClassify 21673573206720514, Purge 21673573206720573. Poll Get Pipeline Status until state is Done. Use runMode full or incremental for the whole organisation, positions to target a subset.
* **Update Business Unit** `updateBusinessUnit`: Update a business unit by its businessUnitSeq.
* **Update Calendar** `updateCalendar`: Update a calendar by its calendarSeq.
* **Update Category** `updateCategory`: Update a compensation category by ruleElementSeq. Create, delete and list categories were already shipped; update was not. Effective dates are deliberately not sent: SAP rejects version changes on an update. owner is the category tree the category belongs to, passed as a JSON object string and emitted verbatim. SAP does not publish a typed request body for any v2 write, so the field names are taken from the GetCategory response contract.
* **Update Category Classifier** `updateCategoryClassifier`: Update an existing category classifier assignment by categoryClassifiersSeq, for example to move a product into a different category. SAP does not publish a typed request body for any v2 write, so the field names are taken from the GetCategoryClassifier response contract.
* **Update Credit** `updateCredit`: Update the hold, roll and comment attributes of an existing credit. The value of a credit cannot be changed here - it can only be modified by an adjustment.
* **Update Credit Type** `updateCreditType`: Update a credit type's description. Keyed by the logical id creditTypeId, not a sequence - SAP answers Not_Found "Resource not found for logical key" when it does not exist. Create and list were already shipped; update was not.
* **Update Customer** `updateCustomer`: Update a customer by its classifierSeq - name, description and address fields.
* **Update Deposit** `updateDeposit`: Update a deposit by its depositSeq - change the hold flag, release date or comments.
* **Update Earning Code** `updateEarningCode`: Update an earning code's description. Keyed by the logical id earningCodeId. Create and list were already shipped; update was not.
* **Update Earning Group** `updateEarningGroup`: Update an earning group's description. Keyed by the logical id earningGroupId. Create and list were already shipped; update was not.
* **Update Event Type** `updateEventType`: Update an event type's description. Keyed by the logical id eventTypeId. Create and list were already shipped; update was not.
* **Update Fixed Value** `updateFixedValue`: Update a fixed value by ruleElementOwnerSeq. Effective dates are deliberately not sent: SAP rejects version changes on an update, so date changes go through the fixed value's versions endpoint. SAP does not publish a typed request body for any v2 write, so the field names are taken from the GetFixedValue response contract.
* **Update Group** `updateGroup`: Update a user group by its groupSeq.
* **Update Participant** `updateParticipant`: Update an existing participant by payeeSeq. To change a field only from a given date onwards, create a new version with Create Participant Version instead.
* **Update Period** `updatePeriod`: Update a period by its periodSeq. Changing dates on a period that already has processed results normally requires a reset first.
* **Update Pipeline Run** `updatePipelineRun`: Act on a running or completed pipeline run - cancel it or restart it. Returns the action that was performed or an error message.
* **Update Position** `updatePosition`: Update an existing position by its seq - reassign the payee, change the title or edit the description. Use Create Position Version to change a field only from a future date.
* **Update Position Group** `updatePositionGroup`: Update a position group by its seq.
* **Update Position Relation** `updatePositionRelation`: Update a position relation by its seq, for example to repoint it at a different parent position.
* **Update Processing Unit** `updateProcessingUnit`: Update a processing unit's description. Keyed by the logical id name. Create and list were already shipped; update was not.
* **Update Product** `updateProduct`: Update a product by its classifierSeq, including its cost and price value objects.
* **Update Quota** `updateQuota`: Update a quota definition by its quotaSeq.
* **Update Reason** `updateReason`: Update a reason code's description. Keyed by the logical id reasonId. Create and list were already shipped; update was not.
* **Update Sales Order** `updateSalesOrder`: Update a sales order header by salesOrderSeq, for example to correct the external order id.
* **Update Sales Transaction** `updateSalesTransaction`: Update an existing sales transaction line by salesTransactionSeq. Changes the amount, compensation date, runnable flag and comments. Re-run the classify and later pipeline stages afterwards for the change to reach credits.
* **Update Territory** `updateTerritory`: Update a territory by ruleElementSeq. Create, delete, get and list territories were already shipped; update was not. Unlike the other updates, SAP's error contract for this endpoint names effective start date and effective end date as required, so both are sent. SAP does not publish a typed request body for any v2 write, so the field names are taken from the GetTerritory response contract.
* **Update Title** `updateTitle`: Update an existing title by its seq.
* **Update User** `updateUser`: Update a tenant user by its userSeq.
* **Update Variable** `updateVariable`: Update a plan variable by ruleElementSeq. Effective dates are deliberately not sent: SAP answers Change_EffectiveDates "Update doesn't allow to change versions", so date changes go through the variable's versions endpoint instead. SAP does not publish a typed request body for any v2 write, so the field names are taken from the GetVariable response contract.

</details>
