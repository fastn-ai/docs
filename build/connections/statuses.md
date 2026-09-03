---
description: What Active, Inactive, Expired and Failed mean, and what to do about each.
---

# Status, and what to do about each

| Status       | Meaning                                                       | Action                                                              |
| ------------ | ------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Active**   | Working.                                                      | Nothing.                                                            |
| **Inactive** | Exists but disabled.                                          | **Reconnect** from the row menu, or **Disconnect** if it is genuinely finished. |
| **Expired**  | The credential ran out and could not be refreshed.            | The customer re-authorises through your widget.                     |
| **Failed**   | The last verification call was rejected — revoked access, changed password, rotated key. | Same: the customer reconnects. |

{% hint style="info" %}
Expired and Failed connections are the most common cause of "the sync stopped working". Watch them, or set an [alert](../../operate/alerts.md) on broken connectors so you hear about it before your customer does.
{% endhint %}
