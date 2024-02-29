from poker_get_deck_and_hand import get_hand, get_deck


def pick_and_draw():
    deck = get_deck()
    hand = get_hand(deck)

    input_keep_cards = input('Pick cards to keep, Type "draw" to draw again. Separate cards by commas.\n')

    if input_keep_cards:
        if input_keep_cards == 'draw':
            new_deck = [deck.remove(card) for card in deck if card in hand]
            return get_hand(new_deck)
        else:
            for card in input_keep_cards:
                pass


def validation_input_to_keep(cards_to_keep: str):
    valid_values = ['1', '2', '3', '4', '5']
    values = cards_to_keep.split(',')

    try:
        if cards_to_keep == 'draw':
            return cards_to_keep
        elif ',' not in cards_to_keep and cards_to_keep != 'draw':
            raise ValueError
        elif 'draw' in cards_to_keep and len(cards_to_keep) > 4:
            raise ValueError
        else:
            for value in values:
                if value.strip() not in valid_values:
                    raise ValueError
            return list(map(int, (cards_to_keep.split(','))))
    except ValueError:
        print('Please enter a valid value i.e. "1 - 5" separated by commas OR "draw".')


pick_and_draw()
