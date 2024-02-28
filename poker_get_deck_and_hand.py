import random


def get_deck():
    suits = ['H', 'D', 'C', 'S']
    ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

    deck = []

    for suit in suits:
        for rank in ranks:
            card = suit + '_' + rank
            deck.append(card)

    return deck


def get_hand():
    deck = get_deck()
    hand = []
    for card in range(5):
        hand_card = random.choice(deck)
        deck.remove(hand_card)
        hand.append(hand_card)

    return sorted(hand)
