---
description: >-
  Condense large documents, chat logs, or articles into short, readable outputs
  while maintaining key context and intent.
---

# Summarization Chain

The Summarization Chain component transforms long pieces of text into concise, meaningful summaries using customizable AI processing.

<figure><img src="../../../../.gitbook/assets/image (47).png" alt="Summarization Chain component in the Fastn flow editor"><figcaption></figcaption></figure>

* To configure this component, start by selecting an AI model, for example, ChatGPT or Gemini.

<figure><img src="../../../../.gitbook/assets/image (52).png" alt="AI model selection dropdown showing ChatGPT and Gemini options"><figcaption></figcaption></figure>

* Once you connect your account for the chosen provider, you can select the specific model you want to use for the summarization process.

<figure><img src="../../../../.gitbook/assets/image (44).png" alt="Account connection and specific model selection for the summarization provider"><figcaption></figcaption></figure>

Next, define your chunking strategy.

{% hint style="info" %}
This determines how the input text will be divided before processing, allowing the model to handle longer content efficiently.
{% endhint %}

* You’ll then specify the characters per chunk, such as 1000, which sets the size of each text segment. Additionally, you can configure chunk overlap characters, for example, 200, to maintain context across adjacent chunks.

<figure><img src="../../../../.gitbook/assets/image (46).png" alt="Chunking strategy settings with characters per chunk and chunk overlap configuration"><figcaption></figcaption></figure>

* After setting these options, paste your input text in the provided field. Once done, click Save in the top-right corner to add the Summarization Chain step to your flow.

<figure><img src="../../../../.gitbook/assets/image (48).png" alt="Input text field and Save button for the Summarization Chain step"><figcaption></figcaption></figure>

* You can test this step by clicking the Test button in the top-right corner.

> The summarized output will appear in the console, showing how your text was condensed by the selected model.

<figure><img src="../../../../.gitbook/assets/image (49).png" alt="Console test output showing the summarized text result"><figcaption></figcaption></figure>

* The summarized output can then be used as input for other steps in your flow, or you can connect it with other components to further process or store the summarized data.

> You can also use this step to summarize text received dynamically from other sources, such as connectors, variables, or AI actions, before passing it to the next stage in your automation.
