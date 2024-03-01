from poker_get_deck_and_hand import get_rank_and_suite_values


def check_pair(hand):
    ranks = get_rank_and_suite_values(hand, get_rank=True)
    rank_count = ranks.values()
    return 2 in rank_count and 3 not in rank_count


def check_two_pair(hand):
    ranks = get_rank_and_suite_values(hand, get_rank=True)
    rank_count = list(ranks.values())
    return rank_count.count(2) == 2


def check_three_of_a_kind(hand):
    ranks = get_rank_and_suite_values(hand, get_rank=True)
    rank_count = ranks.values()
    return 3 in rank_count and 2 not in rank_count


def check_four_of_a_kind(hand):
    ranks = get_rank_and_suite_values(hand, get_rank=True)
    rank_count = ranks.values()
    return 4 in rank_count


def check_full_house(hand):
    ranks = get_rank_and_suite_values(hand, get_rank=True)
    rank_count = ranks.values()
    return 3 in rank_count and 2 in rank_count


def check_flush(hand):  # add check_straight
    suites = get_rank_and_suite_values(hand, get_suite=True)
    suite_count = suites.values()
    return 5 in suite_count


def check_straight_flush(hand):
    return check_straight(hand) and check_flush(hand)


def check_royal_flush(hand):
    royal_flush_list = [['H_1', 'H_10', 'H_11', 'H_12', 'H_13'], ['D_1', 'D_10', 'D_11', 'D_12', 'D_13'],
                        ['C_1', 'C_10', 'C_11', 'C_12', 'C_13'], ['S_1', 'S_10', 'S_11', 'S_12', 'S_13']]
    return sorted(hand) in royal_flush_list


def check_high_card(hand):
    ranks = get_rank_and_suite_values(hand, get_rank=True)
    rank_count = ranks.values()
    if check_straight(hand) or check_flush(hand):
        return False
    return 1 in rank_count and all(rank == 1 for rank in rank_count)


def check_straight(hand):
    ranks = get_rank_and_suite_values(hand, get_rank=True)

    if 2 in ranks.values():
        return False

    rank_values = []
    for value in ranks.keys():
        if ranks[value] > 1:
            for count in range(ranks[value]):
                rank_values.append(int(value))
        else:
            rank_values.append(int(value))

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


def check_drawn_hand(hand):
    hand_types = {
        'High Card': check_high_card(hand),
        'Pair': check_pair(hand),
        'Two Pair': check_two_pair(hand),
        'Three Of A Kind': check_three_of_a_kind(hand),
        'Straight': check_straight(hand),
        'Flush': check_flush(hand),
        'Full House': check_full_house(hand),
        'Four Of A Kind': check_four_of_a_kind(hand),
        'Straight Flush': check_straight_flush(hand),
        'Royal Flush': check_royal_flush(hand)
    }

    for key, value in hand_types.items():
        if value:
            print(key)
            break


