from poker_get_deck_and_hand import get_hand, get_deck
from poker_hand_checker import check_drawn_hand
from poker_input_validation import validation_input_to_keep

import random

payouts = {
    'High Card': 0,
    'Pair': 1,
    'Two Pair': 2,
    'Three Of A Kind': 3,
    'Straight': 4,
    'Flush': 6,
    'Full House': 9,
    'Four Of A Kind': 25,
    'Straight Flush': 50,
    'Royal Flush': 250
}


def pick_and_draw():
    deck = get_deck()
    hand = get_hand(deck)
    random.shuffle(hand)
    print(f'Current Hand: {hand} ({check_drawn_hand(hand)})')
    input_cards_to_keep = input('Pick cards to discard, Type "draw" to draw all again, "keep" to keep all. Separate '
                                'cards to discard by commas.\n')
    cards_to_keep = validation_input_to_keep(input_cards_to_keep)

    if cards_to_keep:
        if cards_to_keep == 'draw':
            new_deck = [card for card in deck if card not in hand]
            return get_hand(new_deck), check_drawn_hand(hand)

        elif input_cards_to_keep == 'keep':
            return hand, check_drawn_hand(hand)
        else:
            list_cards_to_keep = list(map(int, (cards_to_keep.split(','))))
            for index, card in enumerate(list_cards_to_keep, start=1):
                hand.remove(hand[card - index])

            for card in range(len(list_cards_to_keep)):
                hand.append(random.choice(deck))

            return hand, check_drawn_hand(hand)


def bet(total_chips):
    print(f'Total_Chips: {total_chips}')
    bet_chips = int(input('Please input your bet: '))
    if bet_chips > total_chips or bet_chips < 1 or bet_chips > 5:
        print('Enter a valid bet.')
    else:
        total_chips -= bet_chips
        hand, hand_type = pick_and_draw()
        chips_payout = 0

        for hand_types, payout in payouts.items():
            if hand_type == hand_types:
                chips_payout = bet_chips * payout

        total_chips += chips_payout
        print(f'Final Hand: {hand} ({hand_type})')
        print(total_chips)
        return total_chips


def game_loop(chips):
    while chips > 0:
        chips = bet(chips)


if __name__ == '__main__':
    try:
        game_chips = int(input('Enter chips to play with: '))
        game_loop(game_chips)
    except ValueError:
        print('Enter a valid value.')
