from poker_get_deck_and_hand import get_hand
from poker_get_rank_and_suite_values import get_rank_and_suite_values


def check_pair(hand):
    ranks = get_rank_and_suite_values(hand, get_rank=True)
    rank_count = ranks.values()

    if 2 in rank_count and 3 not in rank_count:
        return True

    return False


def check_high_card(hand):
    ranks = get_rank_and_suite_values(hand, get_rank=True)
    rank_count = ranks.values()

    if 1 in rank_count and all(rank == 1 for rank in rank_count):  # add conditional to check if straight
        return True

    return False


def check_two_pair(hand):
    ranks = get_rank_and_suite_values(hand, get_rank=True)
    rank_count = list(ranks.values())

    if rank_count.count(2) == 2:
        return True

    return False


def check_three_of_a_kind(hand):
    ranks = get_rank_and_suite_values(hand, get_rank=True)
    rank_count = ranks.values()

    if 3 in rank_count and 2 not in rank_count:
        return True

    return False


def check_four_of_a_kind(hand):
    ranks = get_rank_and_suite_values(hand, get_rank=True)
    rank_count = ranks.values()

    if 4 in rank_count:
        return True

    return False


def check_full_house(hand):
    ranks = get_rank_and_suite_values(hand, get_rank=True)
    rank_count = ranks.values()

    if 3 in rank_count and 2 in rank_count:
        return True

    return False


def check_flush(hand): # add check_straight

    suites = get_rank_and_suite_values(hand, get_suite=True)
    suite_count = suites.values()

    if 5 in suite_count:
        return suite_count

    return suite_count


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

    return False
