from itertools import groupby
from itertools import cycle
from itertools import product


def get_deck():
    suits = 'CDHS'
    values = '234567890JQKA'
    deck = product(values, suits)
    return ([''.join(c) for c in deck])


def deal():
    deck = get_deck()
    hands = [[], [], [], []]
    players = cycle(hands)
    for card in deck:
        player = next(players)
        player.append(card)
    return (hands)


hands = deal()


def first(x): return (x[0])


for rank, group in groupby(hands, first):
    print(f"{rank} { list(group)}")
