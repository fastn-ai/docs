---
description: >-
  Probes live APIs to gather sample data, helps users define filter conditions
  and targets, and manages complex configuration scenarios.
---

# Configuration Agent

The Configuration Agent is a standalone agent that handles the most tedious part of integration setup — configuring how data flows between systems. Instead of manually inspecting API responses, writing filter conditions, and testing configurations, the agent probes live APIs and guides you through the setup interactively.

### What it does

1. **Probes live APIs** — Connects to the third-party app using the tenant's credentials and fetches sample data. This gives you real examples of what the data looks like — field names, data types, value formats, and edge cases.
2. **Presents sample data** — Shows you actual records from the connected app so you can make informed decisions about filtering and mapping.
3. **Helps define filter conditions** — Based on the sample data, helps you set up filters ("only sync orders where status is 'completed'", "only sync contacts with email addresses").
4. **Configures targets** — Defines where data should go and how it should be transformed — which fields map to the target system, what format conversions are needed, and what defaults to apply for missing values.
5. **Handles edge cases** — Detects configuration scenarios that could cause problems: required fields that are sometimes empty, date formats that vary between records, currency precision mismatches, enum values that don't map cleanly.

### When it's used

The Configuration Agent is called when:

* Setting up field mappings between two connectors for the first time
* A flow needs conditional logic based on real data patterns
* A tenant has complex data with edge cases (mixed date formats, optional fields, multi-currency)
* You need to debug why synced data doesn't look right in the target system

### How it works in practice

**You:** "I need to configure the Shopify-to-Xero order sync. Only completed orders, and map the line items correctly."

**Agent:** "Let me pull some sample orders from the connected Shopify account..."

_\[Agent probes the Shopify API and returns sample data]_

**Agent:** "Here are 5 recent orders. I can see that:

* Orders have 4 possible statuses: `pending`, `processing`, `completed`, `cancelled`
* Line items include `variant_id`, `title`, `quantity`, `price` — price is a string, not a number
* Shipping addresses sometimes have an empty `company` field
* Currency is CAD for this account, not USD

Based on this, I'd recommend:

* Filter: `status == 'completed'`
* Transform: convert `price` from string to number before mapping to Xero
* Default: use the customer name when `company` is empty
* Currency: map `CAD` to Xero's currency code

Want me to apply this configuration?"

> **📷 Screenshot needed:** Configuration Agent showing sample data from a live API with its analysis and recommended configuration.

> **📷 Screenshot needed:** The agent presenting filter conditions it has generated based on the sample data.

### What it detects

The agent actively looks for configuration pitfalls:

| Issue                       | What the agent does                                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Type mismatches**         | Price as string vs number, dates as Unix timestamp vs ISO format — flags and offers transform          |
| **Missing required fields** | Fields that are required in the target but sometimes empty in the source — suggests defaults           |
| **Enum mapping gaps**       | Status values in the source that don't have equivalents in the target — asks you to define the mapping |
| **Currency precision**      | Source uses 2 decimal places, target uses 4 — suggests rounding strategy                               |
| **Locale differences**      | Date formats (MM/DD vs DD/MM), number separators (comma vs period) — configures the Type Coercer       |
| **Array/nested data**       | Line items, addresses, tags that need flattening or restructuring — sets up the Field Mapper           |

### Configuration output

The Configuration Agent produces configurations that slot into Fastn's 5-level hierarchy:

* **Field mappings** — source field → CDM field → target field, with transforms
* **Filter conditions** — condition AST compatible with the Flow Router (operators: eq, neq, gt, lt, in, contains, exists)
* **Type coercion rules** — date format handling, number locale, currency precision, boolean mapping
* **Default values** — fallbacks for optional fields

These configurations are saved at the appropriate level — typically **integration** or **tenant** scope, but can be overridden at the flow level for specific cases.

### Related pages

* [**Configuring a Connector**](https://claude.ai/tutorials/saas-admin/configuring-a-connector.md) — Manual connector configuration tutorial
* [**Connector Agent**](https://claude.ai/chat/connector-agent.md) — Builds the connectors that the Configuration Agent configures
* [**Tenant Onboarding Agent**](https://claude.ai/chat/tenant-onboarding.md) — Uses the Configuration Agent's capabilities when helping tenants set up field mappings
