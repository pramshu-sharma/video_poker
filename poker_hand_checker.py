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

    if not check_straight(hand) and not check_flush(hand) and 1 in rank_count and all(rank == 1 for rank in rank_count):
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


def check_flush(hand):  # add check_straight

    suites = get_rank_and_suite_values(hand, get_suite=True)
    suite_count = suites.values()

    if 5 in suite_count:
        return True

    return False


def check_straight_flush(hand):
    if check_straight(hand) and check_flush(hand):
        return True

    return False


def check_straight(hand):  # need to fix
    ranks = get_rank_and_suite_values(hand, get_rank=True)
    rank_count = list(ranks.values())
    rank_values = []
    for value in ranks.keys():
        if ranks[value] > 1:
            for count in range(ranks[value]):
                rank_values.append(int(value))
        else:
            rank_values.append(int(value))

    if 2 in rank_count:
        return False

    if 1 in rank_values and all(value < 10 for value in rank_values):
        pass
    else:
        for rank in rank_values:
            if rank == 1:
                index_of_1 = rank_values.index(rank)
                rank_values[index_of_1] = 14
    rank_values.sort()
    for rank in range(1, len(rank_values)):
        if rank_values[rank] != rank_values[rank - 1] + 1:
            return False

    return True


def check_royal_flush(hand):
    royal_flush_list = [['H_1', 'H_10', 'H_11', 'H_12', 'H_13'], ['D_1', 'D_10', 'D_11', 'D_12', 'D_13'],
                        ['C_1', 'C_10', 'C_11', 'C_12', 'C_13'], ['S_1', 'S_10', 'S_11', 'S_12', 'S_13']]
    for royal_flush in royal_flush_list:
        if sorted(hand) == royal_flush:
            return True

    return False


if __name__ == '__main__':
    pass
    # hand_count = {}
    # hand_probability = []
    # count = 1
    # loop_range = 10000000
    #
    # while count <= loop_range:
    #     hand = get_hand()
    #     hand_checks = {
    #         check_pair: 'pair',
    #         check_flush: 'flush',
    #         check_two_pair: 'two_pair',
    #         check_three_of_a_kind: 'three_of_a_kind',
    #         check_four_of_a_kind: 'four_of_a_kind',
    #         check_full_house: 'full_house',
    #         check_straight: 'straight',
    #         check_straight_flush: 'straight_flush',
    #         check_high_card: 'high_card',
    #         check_royal_flush: 'royal_flush'
    #     }
    #
    #     for check_function, hand_type in hand_checks.items():
    #         hand_check = check_function(hand)
    #         if hand_check:
    #             if hand_type not in hand_count:
    #                 hand_count[hand_type] = 1
    #             else:
    #                 hand_count[hand_type] += 1
    #     count += 1
    #     if count % 100000 == 0:
    #         print(f'Hand: {count}')
    #
    # for key, value in hand_count.items():
    #     hand_probability.append((key, round(value/loop_range, 10)))
    #
    # print(hand_count)
    # print(hand_probability)
    '''
    results: {'high_card': 5012252, 'three_of_a_kind': 210465, 'pair': 4701990, 'two_pair': 476378, 'full_house': 
    14511, 'flush': 19567, 'straight': 38989, 'four_of_a_kind': 2370, 'straight_flush': 144, 'royal_flush': 11}
     
    probability: [('high_card', 0.5012252), ('three_of_a_kind', 0.0210465), ('pair', 0.470199), ('two_pair', 
    0.0476378), ('full_house', 0.0014511), ('flush', 0.0019567), ('straight', 0.0038989), ('four_of_a_kind', 
    0.000237), ('straight_flush', 1.44e-05), ('royal_flush', 1.1e-06)]
    '''