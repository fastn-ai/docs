---
description: "Connect Deck of Cards to your product with fastn."
hidden: true
---

# Deck of Cards

<img src="../../.gitbook/assets/connectors/lg/deck-of-cards.png" alt="Deck of Cards logo">

Deck of Cards is a free API that simulates decks of playing cards: create and shuffle decks (single or multiple, partial, with Jokers), draw cards, manage named piles (add, list, shuffle, draw, return) and get card images. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [deckofcardsapi.com](https://deckofcardsapi.com) |
| **Authentication** | No authentication |
| **Slug** | `deckOfCards` |

## Use it

Add Deck of Cards from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.deckOfCards.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Cards to Pile</td><td><code>addToPile</code></td><td>Add drawn cards to a named pile, creating the pile if needed (GET /api/deck/{deck_id}/pile/{pile_name}/add/). Cards must have been drawn first. Does not work with multi-deck decks. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Draw Cards</td><td><code>drawCards</code></td><td>Draw cards from the top of a deck (GET /api/deck/{deck_id}/draw/). Use deck_id 'new' to create a shuffled deck and draw from it in one call. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Draw from Pile</td><td><code>drawFromPile</code></td><td>Draw cards from the top of a named pile (GET /api/deck/{deck_id}/pile/{pile_name}/draw/). Give cards to draw specific cards or count to draw several. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Draw from Pile Bottom</td><td><code>drawFromPileBottom</code></td><td>Draw cards from the bottom of a named pile (GET /api/deck/{deck_id}/pile/{pile_name}/draw/bottom/). Docs: https://deckofcardsapi.com/</td></tr><tr><td>Draw Random from Pile</td><td><code>drawFromPileRandom</code></td><td>Draw random cards from a named pile (GET /api/deck/{deck_id}/pile/{pile_name}/draw/random/). Docs: https://deckofcardsapi.com/</td></tr><tr><td>List Pile Cards</td><td><code>listPileCards</code></td><td>List the cards in a named pile and the remaining count of every pile (GET /api/deck/{deck_id}/pile/{pile_name}/list/). Does not work with multi-deck decks. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Open New Deck</td><td><code>openNewDeck</code></td><td>Open a brand new unshuffled deck in order: spades, diamonds, clubs, then hearts (GET /api/deck/new/). Set jokers_enabled to add two Jokers. Returns the new deck_id. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Reshuffle Deck</td><td><code>reshuffleDeck</code></td><td>Shuffle an existing deck (GET /api/deck/{deck_id}/shuffle/). By default all cards return to the deck; set remaining=true to shuffle only the cards left in the main stack. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Return Cards to Deck</td><td><code>returnCardsToDeck</code></td><td>Return drawn cards to the main deck (GET /api/deck/{deck_id}/return/). Give cards to return only those cards; otherwise all drawn cards return. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Return Pile to Deck</td><td><code>returnPileToDeck</code></td><td>Return cards from a named pile to the main deck (GET /api/deck/{deck_id}/pile/{pile_name}/return/). Give cards to return only those cards; otherwise the whole pile returns. Docs: https://deckofcardsapi.com/</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Shuffle New Deck</td><td><code>shuffleNewDeck</code></td><td>Create a new shuffled deck (GET /api/deck/new/shuffle/). Set deck_count for several decks, cards for a partial deck, or jokers_enabled to add two Jokers. Returns the new deck_id. Docs: https://deckofcardsapi.com/</td></tr><tr><td>Shuffle Pile</td><td><code>shufflePile</code></td><td>Shuffle the cards in a named pile (GET /api/deck/{deck_id}/pile/{pile_name}/shuffle/). Does not work with multi-deck decks. Docs: https://deckofcardsapi.com/</td></tr></tbody></table>

</details>
