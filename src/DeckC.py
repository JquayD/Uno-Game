import random


class Deck:
    colors = ["red", "blue", "green", "yellow"]
    actions = ["skip", "reverse", "draw_two"]
    specials = ["WILD", "W.DRAWF"]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, color, action, special, numb):
        self.color = color
        self.action = action
        self.special = special
        self.numb = numb
        self.dk_d = deck()


def deck():
    cards = []

    for color in Deck.colors:
        for numb in Deck.numbers:
            if numb == Deck.numbers[0]:
                crd_o = f"[{color} {numb}]"
                cards.append(crd_o)
            else:
                for _ in range(2):
                    crd = f"[{color} {numb}]"
                    cards.append(crd)

    for color in Deck.colors:
        for action in Deck.actions:
            for _ in range(2):
                crd_a = f"[{color} {action}]"
                cards.append(crd_a)

    for color in Deck.specials:
        for _ in range(4):
            crd_w = f"[{color}]"
            cards.append(crd_w)

    return cards


def shuffled():
    dkd = deck()
    random.shuffle(dkd)

    return dkd

shuffledD = shuffled()
