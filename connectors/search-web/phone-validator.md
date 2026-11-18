---
description: "Phone Validator (phonevalidator.com) worldwide phone number validation API."
---

# Phone Validator

Phone Validator (phonevalidator.com) worldwide phone number validation API. Returns line type (cell, landline, VOIP, toll-free), carrier, location, country and fake-number detection for any phone number. Authentication uses an API key passed in the query string.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [phonevalidator.com](https://phonevalidator.com) |
| **Authentication** | API key |
| **Actions** | 4 |
| **Events** | 0 |
| **Slug** | `phoneValidator` |

## Use it

Add Phone Validator from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.phoneValidator.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Validate Phone Number | `validatePhoneNumber` | Look up a phone number worldwide using Phone Validator API v4 (the current version). Set type=basic for line type, carrier, location, country and fake-number detection, or type=fake for a stand-alone fake-number check. The HTTP status is always 200 - read the StatusCode field in the body: "200" means OK, "501" bad request, "502" account not active, "503" unauthorized, "504" insufficient funds, "500" unexpected error or access denied. The test number 7029270000 is free and is not billed. |
| Validate Phone Number (API v1) | `validatePhoneNumberV1` | Look up a U.S. or Canadian phone number using the original Phone Validator API v1. Superseded by v2 on 2020-07-10 but kept online indefinitely for existing integrations; new work should use Validate Phone Number (v4). v1 offers the basic, detail (area code prefix status and wireless flag) and deactivation lookups, combined with a comma-separated type. The HTTP status is always 200 - read the StatusCode field in the body. The test number 7029270000 is free and is not billed. |
| Validate Phone Number (API v2) | `validatePhoneNumberV2` | Look up a U.S. or Canadian phone number using Phone Validator API v2. Superseded by v3 on 2021-11-24 but kept online indefinitely for existing integrations; new work should use Validate Phone Number (v4). v2 is the only generation besides v1 that offers the detail (ported) and deactivation lookups. Combine lookups by passing a comma-separated type, e.g. basic,detail,deactivation. The HTTP status is always 200 - read the StatusCode field in the body. The test number 7029270000 is free and is not billed. |
| Validate Phone Number (API v3) | `validatePhoneNumberV3` | Look up a U.S. or Canadian phone number using Phone Validator API v3. Superseded by v4 on 2026-03-18 but kept online indefinitely for existing integrations; use Validate Phone Number (v4) for new work and for numbers outside the U.S. and Canada. Set type=basic for line type, carrier, location and fake-number information, or type=fake for a stand-alone fake-number check. The HTTP status is always 200 - read the StatusCode field in the body. The test number 7029270000 is free and is not billed. |
