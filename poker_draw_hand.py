from poker_hand_checker import get_hand, get_deck


def pick_and_draw():
    hand = get_hand()
    print(hand)
    input_picked_cards = input('Pick cards to keep, 0 for draw all again. Separate by commas.\n')  # input validation needed
    picked_cards = list(map(int, input_picked_cards.split(',')))
    if 0 in picked_cards:
        hand = get_hand()
        print(hand)
        return hand

pick_and_draw()

