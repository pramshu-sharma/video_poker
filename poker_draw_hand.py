from poker_get_deck_and_hand import get_hand, get_deck

import random


def pick_and_draw():  # need to fix
    deck = get_deck()
    hand = get_hand(deck)
    print(hand)
    input_cards_to_keep = input('Pick cards to keep, Type "draw" to draw all again, "keep" to keep all. Separate '
                                'cards by commas.\n')
    cards_to_keep = validation_input_to_keep(input_cards_to_keep)

    if cards_to_keep:
        if cards_to_keep == 'draw':
            new_deck = [card for card in deck if card not in hand]
            print(get_hand(new_deck))
        elif input_cards_to_keep == 'keep':
            print(hand)
        else:
            list_cards_to_keep = list(map(int,(cards_to_keep.split(','))))
            for card_index in list_cards_to_keep:
                deck.remove(hand[int(card_index) - 1])
                hand.remove(hand[int(card_index) - 1])

            for new_card in range(1, 5 - len(hand)):
                hand.append(random.choice(deck))
            print(hand)


def validation_input_to_keep(cards_to_keep: str): # need to fix
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
