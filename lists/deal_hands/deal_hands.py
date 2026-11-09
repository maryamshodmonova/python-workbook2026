def deal_hands(deck: list[str], num_players: int, cards_per_player: int) -> list[list[str]]:
    hands = []

    for i in range(num_players):
        start = i * cards_per_player
        end = start + cards_per_player

        hand = deck[start:end]
        hands.append(hand)

    return hands


if __name__ == "__main__":
    # Test your function
    deck = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H']

    hands = deal_hands(deck, 3, 3)

    for i, hand in enumerate(hands, 1):
        print(f"Player {i}: {hand}")
