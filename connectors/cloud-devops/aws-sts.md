---
description: "AWS Security Token Service (STS) Query API."
hidden: true
---

# AWS Security Token Service

<img src="../../.gitbook/assets/connectors/aws-sts.png" alt="AWS Security Token Service logo" width="64">

AWS Security Token Service (STS) Query API. Identify the caller behind the connection's credentials and mint temporary, limited-privilege credentials by assuming an IAM role, with support for session duration, external IDs, MFA, session policies and session tags. Requests are signed with AWS Signature Version 4 using the access key pair on the connection, and an optional STS session token is supported.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [aws.amazon.com](https://aws.amazon.com) |
| **Authentication** | AWS Signature V4 |
| **Slug** | `awsSts` |

## Use it

Add AWS Security Token Service from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.awsSts.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Assume Role | `assumeRole` | Returns a set of temporary security credentials (access key ID, secret access key and session token) for an IAM role, signed with the connection's own AWS credentials. The calling identity must be trusted by the role's trust policy and allowed sts:AssumeRole. Supports session duration, external ID, MFA, inline and managed session policies (up to 5 managed policy ARNs through this action), source identity and up to 5 session tags. Returns the AssumeRoleResponse envelope. |
| Assume Role With SAML | `assumeRoleWithSaml` | Returns temporary credentials for an IAM role in exchange for a SAML authentication response from an identity provider registered as a SAML provider in IAM. AWS does not require the request to be signed. The session lasts for the requested duration or until the assertion's SessionNotOnOrAfter time, whichever is shorter. Supports up to 5 managed session policy ARNs through this action. Returns the AssumeRoleWithSAMLResponse envelope. |
| Assume Role With Web Identity | `assumeRoleWithWebIdentity` | Returns temporary credentials for an IAM role in exchange for an OpenID Connect ID token or OAuth 2.0 access token from a web identity provider such as Amazon Cognito, Login with Amazon, Google, or an OIDC provider registered in IAM. AWS does not require the request to be signed, and the role's trust policy must trust the identity provider. Supports up to 5 managed session policy ARNs through this action. Returns the AssumeRoleWithWebIdentityResponse envelope. |
| Assume Root | `assumeRoot` | Returns short-term privileged root credentials for a member account in an AWS Organization, scoped to one of the AWS managed root-task policies. The connection must hold credentials of the Organizations management account or the delegated administrator for IAM, and centralized root access must be enabled in the organization. Sessions last at most 900 seconds. Returns the AssumeRootResponse envelope. |
| Decode Authorization Message | `decodeAuthorizationMessage` | Decodes the encoded authorization message that AWS services return alongside an authorization failure, revealing which policy, principal, action and resource caused the denial. Requires the sts:DecodeAuthorizationMessage permission. Returns the DecodeAuthorizationMessageResponse envelope with the decoded JSON message as a string. |
| Fastn Assume Role | `fastnAssumeRole` | Sends the same AWS STS AssumeRole request as Assume Role and returns temporary credentials for the given IAM role. The difference is the credential source: in the legacy fastn platform this operation was signed with fastn's own AWS account keys so a customer only had to trust fastn's account in the role's trust policy (usually with an external ID). Here the request is signed with whatever keys the connection holds, so to reproduce that model the connection must hold fastn-owned AWS credentials and the role must trust that account. |
| Get Access Key Info | `getAccessKeyInfo` | Returns the AWS account ID that owns a given access key ID, for long-term (AKIA) and temporary (ASIA) keys alike, without revealing anything else about the key. Useful for identifying the account behind a leaked or unknown key. Returns the GetAccessKeyInfoResponse envelope with the Account. |
| Get Caller Identity | `getCallerIdentity` | Returns details about the IAM user or role whose credentials are used to call the operation, including the AWS account ID, ARN, and user ID. No IAM permissions are required to perform this operation. |
| Get Delegated Access Token | `getDelegatedAccessToken` | Exchanges a trade-in token, issued for an AWS resource or trusted-identity-propagation flow, for temporary AWS credentials and the identity they represent. The trade-in token must be valid and unexpired at the time of the request. Returns the GetDelegatedAccessTokenResponse envelope with the Credentials and the delegated identity details. |
| Get Federation Token | `getFederationToken` | Returns temporary credentials for a federated user, signed with the IAM user credentials on the connection. The effective permissions are the intersection of the calling user's policies and the inline or managed session policies passed here, so pass at least one policy or the federated user has no permissions. Sessions last 900 to 129,600 seconds (12 hours by default). Supports up to 5 managed policy ARNs and 5 session tags through this action. Returns the GetFederationTokenResponse envelope. |

<details>

<summary>See 2 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Session Token | `getSessionToken` | Returns a set of temporary credentials for the IAM user whose long-term keys the connection holds, optionally after MFA. The temporary credentials carry the same permissions as the user except that they cannot call IAM or most STS operations. Sessions last 900 to 129,600 seconds (12 hours by default). Returns the GetSessionTokenResponse envelope with the Credentials. |
| Get Web Identity Token | `getWebIdentityToken` | Issues a short-lived JSON Web Token (JWT) signed by AWS STS that represents the calling IAM identity, for presenting to an external service that validates AWS-issued tokens. The audience populates the aud claim and up to 5 tags can be added as custom claims through this action. Tokens last 60 to 3,600 seconds (300 by default). Returns the GetWebIdentityTokenResponse envelope with the JWT. |

</details>
