---
description: "The simplest embed: an HTML iframe tag."
---

# Iframe

The simplest option: an HTML tag.

```html
<iframe
  src="https://YOUR_FASTN_HOST/api/v1/embed/iframe?token=YOUR_EMBED_TOKEN"
  style="width:100%; height:600px; border:none"
  allow="clipboard-write"
  referrerpolicy="strict-origin-when-cross-origin"
></iframe>
```

Use it for a CMS block, or anywhere you only control markup. The URL takes the token only: the customer is inside the token, named when your backend minted it, so there is no separate customer parameter to keep in step.

{% hint style="danger" %}
The snippet the dashboard generates contains a live token in the URL: the tab says so. That is fine for a first run and wrong for production: URLs end up in logs, referrers and browser history. For production, mint tokens from your backend and keep them out of the URL. The SDK exists for exactly that.
{% endhint %}
