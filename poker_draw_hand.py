from poker_get_deck_and_hand import get_hand, get_deck
from poker_hand_checker import check_drawn_hand

import random


def pick_and_draw():  # need to test
    deck = get_deck()
    hand = get_hand(deck)
    random.shuffle(hand)
    print(hand)
    check_drawn_hand(hand)
    input_cards_to_keep = input('Pick cards to discard, Type "draw" to draw all again, "keep" to keep all. Separate '
                                'cards to discard by commas.\n')
    cards_to_keep = validation_input_to_keep(input_cards_to_keep)

    if cards_to_keep:
        if cards_to_keep == 'draw':
            new_deck = [card for card in deck if card not in hand]
            print(get_hand(new_deck))
            check_drawn_hand(hand)
        elif input_cards_to_keep == 'keep':
            print(hand)
            check_drawn_hand(hand)
        else:
            list_cards_to_keep = list(map(int, (cards_to_keep.split(','))))
            for index, card in enumerate(list_cards_to_keep, start=1):
                hand.remove(hand[card - index])

            for card in range(len(list_cards_to_keep)):
                hand.append(random.choice(deck))

            print(hand)
            check_drawn_hand(hand)


def validation_input_to_keep(cards_to_keep: str):  # need to test
    valid_values = ['1', '2', '3', '4', '5']
    values = cards_to_keep.split(',')

    try:
        if cards_to_keep == 'draw' or cards_to_keep == 'keep':
            return cards_to_keep
        elif cards_to_keep in valid_values and len(cards_to_keep) == 1:
            return cards_to_keep
        elif ',' not in cards_to_keep and (cards_to_keep != 'draw' or cards_to_keep != 'keep'):
            raise ValueError
        elif ('draw' in cards_to_keep or 'keep' in cards_to_keep) and len(cards_to_keep) > 4:
            raise ValueError
        else:
            for value in values:
                if value.strip() not in valid_values:
                    raise ValueError
            return cards_to_keep
    except ValueError:
        print('Please enter a valid value i.e. "1 - 5" separated by commas, "draw" OR "keep".')


pick_and_draw()
