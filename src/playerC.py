import random
from DeckC import shuffledD
from DeckC import Deck
from DeckC import deck

class Player:

    def __init__(self, name, is_ai=False):
        self.hand = []
        self.name = name
        self.dshf = shuffledD

    def play_card(self, card):
        cardply = self.hand.pop(card)

        return cardply

    def draw_card(self):
        if self.dshf:
            card = self.dshf.pop(0)
            self.hand.append(card)
            return card
        else:
            return None


    def display_hand(self):
        print(f"{self.name}'s hand: ")
        for idx, cards in enumerate(self.hand, start=1):
            print(f"({cards}) |{idx}| ")

    def ai_choose_card(self):
        from main import atf1
        cardd = random.choice(atf1.hand)
        card_index = atf1.hand.index(cardd)
        play = atf1.hand.pop(card_index)
        return play
