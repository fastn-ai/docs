---
description: Your account and how you sign in. Organisation settings live separately.
---

# Your profile

**Account menu → View profile**, or `/profile`

<figure><img src="../.gitbook/assets/profile.jpg" alt="The profile page"><figcaption></figcaption></figure>

This page is about you, not the organisation. The **Organisation settings** button top-right crosses over to [Settings](README.md).

### About you

Shown to your team on invitations, comments and audit entries.

| Field         | Notes                                                        |
| ------------- | -------------------------------------------------------------- |
| **First name** | Required.                                                    |
| **Last name**  | Required.                                                    |
| **Job title**  | Optional.                                                    |
| **Timezone**   | Every time on screen is shown in this zone.                  |

{% hint style="info" %}
Your profile timezone changes how timestamps are *displayed* to you. It does not change when a [schedule trigger](../build/triggers.md) fires — a schedule keeps the timezone it was saved with.
{% endhint %}

### Sign in email

Your sign-in address, and where security notices go. It shows a **Verified** badge once confirmed.

Where sign-in is managed by an identity provider, the address is read-only and the page says so: *Your sign-in address is managed by your identity provider. Contact an admin to change it.*

### Security

| Control                       | Notes                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------ |
| **Two factor authentication** | Recommended. A code from an authenticator app, in addition to your password.        |
| **Passkeys**                  | Sign in with Face ID, a fingerprint or a hardware key.                              |
| **Password**                  | Sign-in is passwordless — magic links and passkeys. There is no password to set or change. |

An Owner or Admin sees a prompt at the top of this section, and it is worth taking seriously:

> Your account can change anything in this organisation. A password on its own is the only thing between someone else and all of it. Adding a second factor takes about a minute.

### Where you are signed in

Every active session, with its IP address and when it started, newest marked **Most recent**.

| Button                | Effect                                                                                                       |
| --------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Sign out**          | Ends that one session.                                                                                       |
| **Sign out everywhere** | Ends all of them. Use if you have lost a device or think someone else has access.                          |

Sign out anything you do not recognise, then check the [audit log](audit-log.md) for `auth.login` entries from the same address.

### Switching organisation

The account card at the bottom of the left rail switches between organisations you belong to. Everything else in the dashboard — connectors, workflows, customers, settings — is scoped to whichever one is selected.
