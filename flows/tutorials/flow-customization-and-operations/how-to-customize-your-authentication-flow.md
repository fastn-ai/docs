---
description: >-
  The Custom Auth flow lets you validate incoming requests, check tokens, and
  return user details and you can customize it to match your own authentication
  logic.
---

# How to Customize your Authentication Flow?

## 1. Enable Custom Auth in Settings

* Go to the **right-hand sidebar → Settings → Configuration**.
* Under **Custom Auth**, toggle **Enable Custom Authentication**.
* Save your changes.

<figure><img src="../../../.gitbook/assets/image (549).png" alt=""><figcaption></figcaption></figure>

## 2. Open the Custom Auth Flow

* Navigate to the **fastnCustomAuth** flow.
* This flow always begins with an **On API Request** trigger.

<figure><img src="../../../.gitbook/assets/image (550).png" alt=""><figcaption></figcaption></figure>

## 3. Initialize Flow Variables

* Add variables such as `baseURL` and `APIKey`.
* These can be predefined defaults for your flow, but you can alter them if needed.

<figure><img src="../../../.gitbook/assets/image (551).png" alt=""><figcaption></figcaption></figure>

## 4. Apply Token Validation (Switch Step)

* At this stage, the flow checks the Authorization header against the predefined Fastn secret (`fastn_mcp_client_api_key`).

<figure><img src="../../../.gitbook/assets/image (552).png" alt=""><figcaption></figcaption></figure>

*   **Condition 1:** If `headers.authorization` **equals**

    ```
    Bearer {{secrets.fastn_mcp_client_api_key}}
    ```

    → **Pass**.
*   **Condition 2:** If `headers.authorization` **equals**

    ```
    {{secrets.fastn_mcp_client_api_key}}
    ```

    → **Pass**.

**When one of the conditions matches:**

* The flow returns a **user object** that contains:
  * `tenantId`
  * `role`
  * `expiresIn`
* All inside a success response.

<figure><img src="../../../.gitbook/assets/image (121).png" alt=""><figcaption></figcaption></figure>

**When no conditions match:**

* The flow continues to the **Logger** step for tracking request headers.

<figure><img src="../../../.gitbook/assets/image (120).png" alt=""><figcaption></figcaption></figure>

## 5. Handle Logs and External Checks

* **Logger Step** → capture the request headers.

<figure><img src="../../../.gitbook/assets/image (122).png" alt=""><figcaption></figcaption></figure>

* **GET Request (HTTP API)** → check if the user exists externally.

<figure><img src="../../../.gitbook/assets/image (123).png" alt=""><figcaption></figcaption></figure>

* **Final Switch Step**

<figure><img src="../../../.gitbook/assets/image (124).png" alt=""><figcaption></figcaption></figure>

* If user exists → return user details.

<figure><img src="../../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* If not → return error and unauthorized.

<figure><img src="../../../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

## 6. Save and Customize

* Save the flow once configured.
* You can customize the logic to match your own authentication provider, add extra validation rules, or enrich the returned user object.

> With this setup, you decide exactly how requests are authenticated and what user details are returned.
