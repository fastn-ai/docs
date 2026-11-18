---
description: "Deck of Cards is a free API that simulates decks of playing cards: create and shuffle decks (single or multiple, partial, with Jokers), draw cards, manage…"
hidden: true
---

# Deck of Cards

<img src="../../.gitbook/assets/connectors/deck-of-cards.png" alt="Deck of Cards logo" width="64">

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

| Action | Slug | What it does |
| --- | --- | --- |
| Add Cards to Pile | `addToPile` | Add drawn cards to a named pile, creating the pile if needed (GET /api/deck/{deck_id}/pile/{pile_name}/add/). Cards must have been drawn first. Does not work with multi-deck decks. Docs: https://deckofcardsapi.com/ |
| Draw Cards | `drawCards` | Draw cards from the top of a deck (GET /api/deck/{deck_id}/draw/). Use deck_id 'new' to create a shuffled deck and draw from it in one call. Docs: https://deckofcardsapi.com/ |
| Draw from Pile | `drawFromPile` | Draw cards from the top of a named pile (GET /api/deck/{deck_id}/pile/{pile_name}/draw/). Give cards to draw specific cards or count to draw several. Docs: https://deckofcardsapi.com/ |
| Draw from Pile Bottom | `drawFromPileBottom` | Draw cards from the bottom of a named pile (GET /api/deck/{deck_id}/pile/{pile_name}/draw/bottom/). Docs: https://deckofcardsapi.com/ |
| Draw Random from Pile | `drawFromPileRandom` | Draw random cards from a named pile (GET /api/deck/{deck_id}/pile/{pile_name}/draw/random/). Docs: https://deckofcardsapi.com/ |
| List Pile Cards | `listPileCards` | List the cards in a named pile and the remaining count of every pile (GET /api/deck/{deck_id}/pile/{pile_name}/list/). Does not work with multi-deck decks. Docs: https://deckofcardsapi.com/ |
| Open New Deck | `openNewDeck` | Open a brand new unshuffled deck in order: spades, diamonds, clubs, then hearts (GET /api/deck/new/). Set jokers_enabled to add two Jokers. Returns the new deck_id. Docs: https://deckofcardsapi.com/ |
| Reshuffle Deck | `reshuffleDeck` | Shuffle an existing deck (GET /api/deck/{deck_id}/shuffle/). By default all cards return to the deck; set remaining=true to shuffle only the cards left in the main stack. Docs: https://deckofcardsapi.com/ |
| Return Cards to Deck | `returnCardsToDeck` | Return drawn cards to the main deck (GET /api/deck/{deck_id}/return/). Give cards to return only those cards; otherwise all drawn cards return. Docs: https://deckofcardsapi.com/ |
| Return Pile to Deck | `returnPileToDeck` | Return cards from a named pile to the main deck (GET /api/deck/{deck_id}/pile/{pile_name}/return/). Give cards to return only those cards; otherwise the whole pile returns. Docs: https://deckofcardsapi.com/ |

<details>

<summary>See 2 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Shuffle New Deck | `shuffleNewDeck` | Create a new shuffled deck (GET /api/deck/new/shuffle/). Set deck_count for several decks, cards for a partial deck, or jokers_enabled to add two Jokers. Returns the new deck_id. Docs: https://deckofcardsapi.com/ |
| Shuffle Pile | `shufflePile` | Shuffle the cards in a named pile (GET /api/deck/{deck_id}/pile/{pile_name}/shuffle/). Does not work with multi-deck decks. Docs: https://deckofcardsapi.com/ |

</details>
