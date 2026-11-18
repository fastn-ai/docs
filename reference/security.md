---
description: How fastn protects your data and your customers' credentials, its certifications, and where to get the security documents your review needs.
---

# Security and compliance

This page is for your security, compliance and procurement reviewers. It covers how fastn keeps each of your customers' data apart, how credentials are protected, what fastn is certified for, and how to get the reports a vendor review asks for.

The full security documentation, including the audit reports, is in the [fastn Trust Center](https://trust.fastn.ai).

## Certifications and compliance

| Standard | Status |
| --- | --- |
| SOC 2 Type II | Certified |
| ISO/IEC 27001:2022 | Certified |
| GDPR | Compliant. See [Privacy](#privacy-and-your-data) below |
| PCI DSS v4.0.1 | Report available in the Trust Center |
| HIPAA | HIPAA-ready, with a [Business Associate Agreement](https://fastn.ai/hipaa-baa) for customers who need one |
| CASA Tier 2 | Listed in the Trust Center |

fastn's public endpoints score **A+** on Qualys SSL Labs, ImmuniWeb and CryptCheck.

### Get the reports

Request the SOC 2 Type II report, the ISO/IEC 27001 certificate, the PCI DSS report, the latest penetration test and vulnerability assessment, and the CAIQ self-assessment from the [Trust Center](https://trust.fastn.ai): choose **Get access** or **Ask for information**. Reports that are under NDA are shared once access is approved.

## How your customers' data is kept apart

* **Each customer is isolated.** Every one of your customers has its own connections, credentials, records and events. One customer's data never reaches another's, and the isolation is enforced by the platform, not only by convention. See [Customers and tenancy](../tutorials/developer/understanding-tenancy.md).
* **Control plane and data plane are separate.** Configuration (connectors, workflows, widgets) and the traffic that carries your customers' data run on separate planes.
* **Every request is scoped.** API calls are checked against the caller's role and the customer they act for before they reach any data.

## Credentials

* **Encrypted and customer-scoped.** When a customer connects an app, its tokens and keys are encrypted at rest and stored under that customer only.
* **Refreshed by fastn.** fastn refreshes OAuth tokens itself, so your code never handles a refresh token.
* **Never shown back.** The dashboard and API do not return a connection's raw credentials to a caller that is not explicitly allowed to read them. Granting **decrypt** on Connections or **read** on Secrets to an API key is the only way to read them, and [API keys](../manage/api-keys.md) explains why to grant it rarely.
* **Your own secrets** are encrypted the same way. See [Secrets](../manage/secrets.md).

## Access control

* **Roles.** Everyone in your organization has a role (Owner, Admin, Developer, Operator, Viewer), and the platform enforces what each can do. See [Roles](../manage/roles.md).
* **API keys** are scoped by permission, by customer, by IP address and by expiry, and can be revoked at once. See [API keys](../manage/api-keys.md).
* **Caller identity.** Turn on identity verification on a key so that a caller cannot change which customer or user it claims to act for: each request carries an HMAC your backend computes. See [Identity hash](../manage/api-keys.md#identity-hash).
* **Audit log.** Who did what, and when, across your organization. See [Audit log](../manage/audit-log.md).
* **AI agents act with permissions.** Agent and MCP tool calls run with the same permissions as the person or key behind them, and every call is logged.

## Encryption in transit

All traffic to fastn's dashboard, API and widget uses HTTPS.

## Reliability

* **99.9% uptime SLA.** The terms are in the Service-Level Agreement in the [Trust Center](https://trust.fastn.ai).
* **Monitoring and alerts** on every plan. You can also alert your own team on failures: see [Alerts](../operate/alerts.md).
* **Backups** are taken as part of fastn's data security controls, with a recovery time objective of 24 to 48 hours.

## Enterprise options

The Enterprise plan adds:

* SSO with SAML
* Data residency
* Dedicated infrastructure
* Private networking
* Self-hosting

[Contact fastn](https://fastn.ai/contact) to discuss them.

## Privacy and your data

* fastn processes personal data under its [Privacy Policy](https://fastn.ai/privacy). Vendors that process data for fastn are bound by data processing agreements.
* Under GDPR you can ask to access, correct, delete, restrict or move your data, and under the CCPA to know what is collected and to have it deleted. Send requests to [dpo@fastn.ai](mailto:dpo@fastn.ai), fastn's Data Protection Officer.
* **You can take your work with you.** Workflows are JavaScript files you can mirror to your own GitHub repository (see [Environments and GitHub](../manage/environments.md)), and connectors and actions export as JSON (see [Importing and exporting](../build/connectors/importing-and-exporting.md)).

## Billing

What you pay for, how customer connections are counted and what happens at a plan limit are on [Billing and limits](../manage/billing.md).

## Contact

* Security questions and document requests: the [Trust Center](https://trust.fastn.ai)
* Privacy requests: [dpo@fastn.ai](mailto:dpo@fastn.ai)
* Anything else: [contact@fastn.ai](mailto:contact@fastn.ai)
