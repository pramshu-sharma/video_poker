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
    except TypeError:
        print('Please enter a valid value i.e. "1 - 5" separated by commas, "draw" OR "keep".')


def validation_bet(coins, total_coins):
    try:
        if coins < 1 or coins > 5 or coins > total_coins:
            raise ValueError
        else:
            return True
    except ValueError:
        print('Please enter a valid bet.')