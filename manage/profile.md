---
description: Your account and how you sign in. Organization settings live separately.
---

# Your profile

The profile row at the bottom of the left rail, or `/profile`

This page is about you, not the organization. The **Organization settings** link crosses over to [General](general.md).

### About you

Shown to your team on invitations, comments and audit entries.

| Field         | Notes                                                        |
| ------------- | -------------------------------------------------------------- |
| **First name** | Required.                                                    |
| **Last name**  | Required.                                                    |
| **Job title**  | Optional.                                                    |
| **Timezone**   | The full IANA list. Every time on screen is shown in this zone. |

{% hint style="info" %}
Your profile timezone changes how timestamps are *displayed* to you. It does not change when a [schedule trigger](../build/triggers/README.md) fires: a schedule keeps the timezone it was saved with.
{% endhint %}

### Sign in email

Your sign-in address, and where security notices go, shown with a **Verified** badge.

The address is always read-only here. The page says: *Your sign-in address is managed by your identity provider. Contact an admin to change it.*

### Security

One row, **Passkeys**: sign in with Face ID, a fingerprint or a hardware key. It reads **Not set up** until you add one, then the number registered, with **Set up** or **Add another** to register a passkey and a remove control beside each one. If a single passkey is your only way in, the page warns that losing that device would lock you out and offers **Add a second passkey**.

There is no two-factor row and no password row. Sign-in is passwordless, so there is no password to set or change.

{% hint style="info" %}
If your account is an Owner or Admin, it can change anything in the organization. A second passkey on another device keeps you from being locked out if you lose the first.
{% endhint %}

### Where you are signed in

Every active session, with its **IP** address, newest marked **Most recent**.

| Button          | Effect                                                                                     |
| --------------- | -------------------------------------------------------------------------------------------- |
| **Sign out**    | Ends that one session. It sits on each row.                                                 |
| **Everywhere**  | Ends all of them. Use if you have lost a device or think someone else has access.           |

Sign out anything you do not recognize, then check the [audit log](audit-log.md) for `auth.login` entries from the same address.

### Switching organization

The account card at the bottom of the left rail switches between organizations you belong to. Everything else in the dashboard (connectors, workflows, customers, settings) is scoped to whichever one is selected.
