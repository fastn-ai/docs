---
description: "Deck of Cards simulates decks of playing cards. Open and shuffle decks, draw cards and manage piles."
hidden: true
---

# Deck of Cards

<img src="../../.gitbook/assets/connectors/lg/deck-of-cards.png" alt="Deck of Cards logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [deckofcardsapi.com](https://deckofcardsapi.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `deckOfCards` |

## Setup

Deck of Cards needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Deck of Cards from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.deckOfCards.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Cards to Pile</td><td><code>addToPile</code></td><td>Add drawn cards to a named pile, creating the pile if needed Cards must have been drawn first. Does not work with multi-deck decks. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Draw Cards</td><td><code>drawCards</code></td><td>Draw cards from the top of a deck Use deck_id 'new' to create a shuffled deck and draw from it in one call. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Draw from Pile</td><td><code>drawFromPile</code></td><td>Draw cards from the top of a named pile Give cards to draw specific cards or count to draw several. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Draw from Pile Bottom</td><td><code>drawFromPileBottom</code></td><td>Draw cards from the bottom of a named pile Docs: https://deckofcardsapi.com/</td></tr><tr><td>Draw Random from Pile</td><td><code>drawFromPileRandom</code></td><td>Draw random cards from a named pile Docs: https://deckofcardsapi.com/</td></tr><tr><td>List Pile Cards</td><td><code>listPileCards</code></td><td>List the cards in a named pile and the remaining count of every pile Does not work with multi-deck decks. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Open New Deck</td><td><code>openNewDeck</code></td><td>Open a brand new unshuffled deck in order: spades, diamonds, clubs, then hearts Set jokers_enabled to add two Jokers. Returns the new deck_id. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Reshuffle Deck</td><td><code>reshuffleDeck</code></td><td>Shuffle an existing deck By default all cards return to the deck; set remaining=true to shuffle only the cards left in the main stack. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Return Cards to Deck</td><td><code>returnCardsToDeck</code></td><td>Return drawn cards to the main deck Give cards to return only those cards; otherwise all drawn cards return. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Return Pile to Deck</td><td><code>returnPileToDeck</code></td><td>Return cards from a named pile to the main deck Give cards to return only those cards; otherwise the whole pile returns. Docs: https://deckofcardsapi.com/</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Shuffle New Deck</td><td><code>shuffleNewDeck</code></td><td>Create a new shuffled deck Set deck_count for several decks, cards for a partial deck, or jokers_enabled to add two Jokers. Returns the new deck_id. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Shuffle Pile</td><td><code>shufflePile</code></td><td>Shuffle the cards in a named pile Does not work with multi-deck decks. Docs: https://deckofcardsapi.com/</td></tr></tbody></table>

</details>

## Events

Deck of Cards has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
