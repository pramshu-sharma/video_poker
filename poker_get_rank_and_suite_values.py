
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
        return suites
    elif get_rank and not get_suite:
        return ranks
    elif get_suite and get_rank:
        return suites, ranks

