
from itertools import cycle
from itertools import product


def get_deck():
    suits = 'CDHS'
    values = '234567890JQKA'
    deck = product(values, suits)
    return ([''. join(c) for c in deck])


deck = get_deck()
print(len(deck))
print(deck[:7])


def deal():

    deck = get_deck()
    hands = [[], [], [], []]
    players = cycle(hands)
    for card in deck:
        player = next(players)
        player . append(card)
    return (hands)

hands = deal ()
hand1 = sorted ( hands [0])
print(hand1)
