---
description: >-
  In the Fastn platform, workspaces are used to organize your created flows,
  workflows, webhooks, widgets etc.
---

# Workspace Management

## Getting Started with Workspaces in Fastn

* Multiple users can collaborate on a single workspace with role-based access assigned by the workspace **Admin**.
* When you first log in to [**Fastn**](https://live.fastn.ai/app), a workspace titled "My Workspace" is created by default. After selecting your workspace, you'll be directed to the next page to set up your integrations.

{% hint style="info" %}
If you have more than one workspace, you will be provided with an option to choose your respective.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (19) (1).png" alt=""><figcaption></figcaption></figure>

* You can create any new desired workspace with a unique Space ID by using the **Create Workspace** button on [live.fastn.ai/app](https://live.fastn.ai/app)

<figure><img src="../../../../.gitbook/assets/image (460).png" alt=""><figcaption></figcaption></figure>

## Workspace Settings[​](https://docs.fastn.ai/docs/workspace-management#workspace-settings)

* Create or delete API keys with desired permissions to use when calling flows externally.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXc-U0b-bGceNyDUzs263hsqHM9e00M8a7k2xKiyqJvx1YcMrJWJvZdnt90CRYajjkb2qbBNvOL1qMiz7nhj6_YdENawMQ32kTbK0lzSH7TKYyK05bCxCrrsR07sVRG-Q9bs-oPWxQ?key=wOmYrIP-94JypD1X6n-sVQ" alt=""><figcaption></figcaption></figure>

* Manage secrets that can be utilized across different flows.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeKsjsazl7dhlvmEF5ETdEx8yfyNVyKbz9Uirf92XdeX6ZMrqoLbwWSHlkvtTW0Lysi2WNQGHcB3LZ73JdG1o-KJXuKaTyroY8NZDy6YQhcSCE3TkGQ6SCkyLEfO_FrJNU3nVeAhg?key=wOmYrIP-94JypD1X6n-sVQ" alt=""><figcaption></figcaption></figure>

* Collaborate with others by inviting them to your managed workspaces. With RBAC (role based access control) give users in your workspace the desired permissions.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXf0EphznrN0wkjcjCKIkiWX-cUQYHQpEkCGB9kHy9HLCDXu9IQX-DPkqC2AplIJKESQ6OnGxQN2FSMW8rhzefC374dNBPiWB1eilaeXC5BkLIwxtLwQshn1oGNBgrqTP6JnUQXO?key=wOmYrIP-94JypD1X6n-sVQ" alt=""><figcaption></figcaption></figure>

* Manage deployment environments. Multiple versions of created flows can be deployed across different environments.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdH00YO0IrO4RwgnRmfeAb8yLIK-SNLGZbYIheeDSdFG57QNL_8jGlk4pgpcayW4RoCLvbPxkkD8AVwGVyq3od9zpi-AZKqxUn3mjTuNCTgMvPOd8pRhOjXImuFmVh7OU_X298yEw?key=wOmYrIP-94JypD1X6n-sVQ" alt=""><figcaption></figcaption></figure>

* With different environments, different configurations can be assigned and used in flows through variables.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdm4by-gVUoBzNXnSbn1C66m85l4M3cEQ_PiW9MWswvB6LTwANgQhcyVYnhPddIrth2LIo9x22SRzbZ0ek1oXLeWgt2Ss1_AaFbz2FMQ2-wss67JMX1hWdia7tNlU-Bs5Tq_OeO?key=wOmYrIP-94JypD1X6n-sVQ" alt=""><figcaption></figcaption></figure>

* Models created as input and output schema for different flows can also be managed in the workspace settings.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXf1hHC_elyTZzIz8cPWyXCG2B8V1Qgwbu_gpjIghgSkc_hyGwfnkLnAK6FvokENn5ZbQp066O2nbMMF9xZZbh16eKQoWErdORFI8_WO1r_fWxO0-edsLKh84LUgNLiW6537bnA8xA?key=wOmYrIP-94JypD1X6n-sVQ" alt=""><figcaption></figcaption></figure>

## Managing Tenants in Fastn

Fastn supports **multi-tenant architecture**, making it easy to build and manage flows for different clients, teams, or environments — all within a single workspace.

### What is a Tenant?

A **tenant** represents an isolated environment for a particular user within your workspace. It helps separate data, configurations, credentials, and workflows for different customers, business units, or systems. Fastn’s built-in multi-tenancy ensures complete **data isolation and secure execution** for each tenant.

<figure><img src="../../../../.gitbook/assets/image (323).png" alt=""><figcaption></figcaption></figure>

### How to Manage Tenants

You can manage all your tenants from the **Tenants** section in the left sidebar.

#### Creating a Tenant

1. Click the **"Create Tenant"** button in the top right.
2. Enter a unique name for your tenant.
3. Once created, the tenant will appear in the list with options to **edit** or **delete**.

#### Creating a Tenant Secret

1. Click on an existing tenant in the list.
2. Select **‘Create Secret’** to add credentials like API keys or tokens.
3. These secrets are securely scoped to the tenant, ensuring access is restricted to flows running within that tenant's context.

Learn more about multi-tenancy in Fastn:

{% embed url="https://docs.fastn.ai/multitenancy" %}
