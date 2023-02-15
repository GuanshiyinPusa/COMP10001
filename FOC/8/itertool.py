from itertools import product


def get_deck():

    # Create a list of 52 cards .
    suits = 'CDHS '
    values = '234567890 JQKA '
    deck = product(values, suits)
    return ([''. join(c) for c in deck])

print(get_deck())