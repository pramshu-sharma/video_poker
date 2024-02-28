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


def get_rank_and_suite_values(hand, get_suite: bool = None, get_rank: bool = None):
    assert get_suite is None or isinstance(get_suite, bool), 'get_suite must be a boolean or None'
    assert get_rank is None or isinstance(get_rank, bool), 'get_rank must be a boolean or None'

    suites, ranks = {}, {}
    for card in hand:
        suite_val = card.split('_')[0]
        rank_val = card.split('_')[1]

        if suite_val not in suites:
            suites[suite_val] = 1
        else:
            suites[suite_val] += 1

        if rank_val not in ranks:
            ranks[rank_val] = 1
        else:
            ranks[rank_val] += 1

    if get_suite and not get_rank:
        return hand, suites
    elif get_rank and not get_suite:
        return hand, ranks
    elif get_suite and get_rank:
        return hand, suites, ranks
    else:
        return hand, None, None


def check_pair():
    hand, ranks = get_rank_and_suite_values(get_hand(), get_rank=True)
    rank_count = ranks.values()

    if 2 in rank_count and 3 not in rank_count:
        return True

    return False


def check_high_card():
    # count_dict_values = {}
    # for card in hand:
    #     value = card.split('_')[1]
    #     if value not in count_dict_values:
    #         count_dict_values[value] = 1
    #     else:
    #         count_dict_values[value] += 1
    hand, ranks = get_rank_and_suite_values(get_hand(), get_rank=True)
    rank_count = ranks.values()
    # for rank in rank_count:
    #     if rank > 1:
    #         print(hand, 'F', ranks)
    #         return False
    #     else:
    #         print(hand, 'T', ranks)
    #         return True
    if 1 in rank_count and all(rank == 1 for rank in rank_count):  # add conditional to check if straight
        return True

    return False


def check_two_pair(hand):
    count_dict_values = {}
    for card in hand:
        value = card.split('_')[1]
        if value not in count_dict_values:
            count_dict_values[value] = 1
        else:
            count_dict_values[value] += 1

    values = list(count_dict_values.values())
    if values.count(2) == 2:
        return True

    return False


def check_three_of_a_kind(hand):
    count_dict_values = {}
    for card in hand:
        value = card.split('_')[1]
        if value not in count_dict_values:
            count_dict_values[value] = 1
        else:
            count_dict_values[value] += 1

    values = count_dict_values.values()
    if 3 in values and 2 not in values:
        return True

    return False


def check_four_of_a_kind(hand):
    count_dict_values = {}
    for card in hand:
        value = card.split('_')[1]
        if value not in count_dict_values:
            count_dict_values[value] = 1
        else:
            count_dict_values[value] += 1

    values = count_dict_values.values()
    if 4 in values:
        return True

    return False


def check_full_house(hand):
    count_dict_values = {}
    for card in hand:
        value = card.split('_')[1]
        if value not in count_dict_values:
            count_dict_values[value] = 1
        else:
            count_dict_values[value] += 1

    values = count_dict_values.values()
    if 3 in values and 2 in values:
        return True

    return False


def check_flush(hand):
    count_dict_suites = {}
    for card in hand:
        suite = card.split('_')[0]
        if suite not in count_dict_suites:
            count_dict_suites[suite] = 1
        else:
            count_dict_suites[suite] += 1

    if 5 in count_dict_suites.values():
        return True

    return False


def check_straight_flush(hand):
    pass


def check_straight(hand):
    count_dict_values = {}  # need to fix
    for card in hand:
        value = card.split('_')[1]
        if value not in count_dict_values:
            count_dict_values[value] = 1
        else:
            count_dict_values[value] += 1

    values = list(count_dict_values.values())

    for value in values:
        if value > 1:
            return hand, values, 'F'

    keys = sorted(list(map(int, count_dict_values.keys())))
    if 1 in keys and all(num < 10 for num in keys):
        pass
    else:
        for key in keys:
            if key == 1:
                index_of_1 = keys.index(key)
                keys[index_of_1] = 14
    keys.sort()
    for key in range(1, len(keys)):
        if key != keys[key - 1] + 1:
            return hand, keys, 'F'

    return hand, keys, 'T'


def check_royal_flush(hand):
    royal_flush_list = [['H_1', 'H_10', 'H_11', 'H_12', 'H_13'], ['D_1', 'D_10', 'D_11', 'D_12', 'D_13'],
                        ['C_1', 'C_10', 'C_11', 'C_12', 'C_13'], ['S_1', 'S_10', 'S_11', 'S_12', 'S_13']]
    for royal_flush in royal_flush_list:
        if sorted(hand) == royal_flush:
            return True
        else:
            return False
