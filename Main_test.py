import random
import time
import getpass
import os


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


class Player:

    def __init__(self, name, is_ai=False):
        self.hand = []
        self.name = name
        self.dshf = dshf

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
        cardd = random.choice(atf1.hand)
        card_index = atf1.hand.index(cardd)
        play = atf1.hand.pop(card_index)
        return play


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


dshf = shuffled()

username = getpass.getuser()
user1 = Player(f"{username}")
atf1 = Player("A.BoTI")

cur_players = [user1, atf1]


def deal_hand(size=7):
    for _ in range(size):
        for players in cur_players:
            players.draw_card()


def gamest():
    deal_hand()
    turns = [0, 1]
    chosen_turn = random.choice(turns)
    st_olor = Deck.colors
    starting_color = random.choice(st_olor)

    print(f"Starting card color is {starting_color}.")
    time.sleep(2)
    os.system('clear')
    while True:

        if len(user1.hand) == 0:
            print(f"{user1.name} wins!")
            break
        elif len(atf1.hand) == 0:
            print(f"{atf1.name} wins!")
            break

        if chosen_turn == 0:
            print(f"{user1.name} turn")
            time.sleep(3)
            os.system('clear')
            user1.display_hand()
            prompt = (
                    "Play a card (e.g. type '1' to play "
                    "the first card in your hand) "
                    "(To draw a card, type 'd'): "
                      )
            inpud = input(prompt)
            try:
                inpud = int(inpud)-1
                if 0 <= inpud < len(user1.hand):
                    plcrd = user1.hand[inpud]
                    plcrd = plcrd.strip('[]')
                    plsplit = plcrd.split()

                    card_col = plsplit[0].lower()
                    card_val = plsplit[1] if len(plsplit) > 1 else plsplit

                    card_cv = f"{card_col}"
                    card_va = f"{card_val}"

                    if card_va in ["skip", "reverse", "draw_two"]:
                        if card_va == "skip":
                            if card_cv in starting_color:
                                played = user1.play_card(card=inpud)
                                print(f"{user1.name} played: {played}")
                                print(f"Skipping {atf1.name} turn.")
                                time.sleep(2)
                                os.system('clear')
                                chosen_turn = 0
                        elif card_va == "reverse":
                            if card_cv in starting_color:
                                played = user1.play_card(card=inpud)
                                print(f"{user1.name} played: {played}")
                                print(f"Turns are reversed!")
                                time.sleep(2)
                                os.system('clear')
                                chosen_turn = (chosen_turn + 1 ) % 2
                        elif card_va == "draw_two":
                            if card_cv in starting_color:
                                played = user1.play_card(card=inpud)
                                print(f"{user1.name} played: {played}")
                                print(f"{atf1.name} is forced to draw two cards!")
                                for _ in range(2):
                                    atf1.draw_card()
                                time.sleep(2)
                                os.system('clear')
                                chosen_turn = 1
                            else:
                                print("continuing the game")
                    elif plcrd in ["WILD", "W.DRAWF"]:
                        played = user1.play_card(card=inpud)
                        color_prompt = input(
                                "Type a color "
                                "(e.g. red, green...)"
                                            )

                        if color_prompt in st_olor:
                            starting_color = color_prompt
                            print(f"The new color is {starting_color}...")
                            penalize_prompt = (
                                            f"{atf1.name} has been "
                                            "penalized four cards."
                                              )
                            if plcrd == "W.DRAWF":
                                for _ in range(4):
                                    atf1.draw_card()
                                print(penalize_prompt)
                                time.sleep(2)
                                os.system('clear')
                            print(f"{user1.name} played: {played}")
                            time.sleep(2)
                            os.system('clear')
                            chosen_turn = 1
                        else:
                            print("Invalid color, please "
                                  "input a color from [red, "
                                  "blue, green, yellow]")

                        os.system('clear')

                    elif card_cv in starting_color:
                        played = user1.play_card(card=inpud)
                        os.system('clear')
                        print(f"{user1.name} played: {played}")
                        user1.display_hand()
                        time.sleep(2)
                        os.system('clear')
                        chosen_turn = 1

                    else:
                        print(
                                "Invalid card color, "
                                f"Current color: {starting_color}"
                                )
                else:
                    print("Invalid card position.")
            except ValueError:
                if inpud in ['d', 'D']:
                    usrDrawCardPrompt = int(
                            input("You can  1-8 cards from the deck: ")
                            )
                    if 1 <= usrDrawCardPrompt <= 8:
                        temp_list = []
                        for _ in range(usrDrawCardPrompt):
                            carddrew = user1.draw_card()
                            temp_list.append(carddrew)
                        played_drawn = ', '.join(map(str, temp_list))

                        print(
                            f"Cards Drawn: {played_drawn}"
                            )
                        chosen_turn = 1
                        time.sleep(5)
                    else:
                        print("Invalid range, try again.")
                os.system('clear')
        elif chosen_turn == 1:
            print(f"{atf1.name} turn")
            time.sleep(3)
            os.system('clear')
            if len(atf1.hand) > 0:
                valid_move = False
                attempts = 0
                max_attempts = len(atf1.hand)

                while not valid_move and attempts < max_attempts:

                    played = atf1.ai_choose_card()
                    played1 = played.strip('[]')
                    playsplit = played1.split()

                    card_col2 = playsplit[0].lower()
                    card_val2 = playsplit[1] if len(playsplit) > 1 else playsplit

                    card_cvp = f"{card_col2}"
                    card_cva = f"{card_val2}"
                    if card_cva in ["skip", "reverse", "draw_two"]:
                        if card_cvp in starting_color:
                            if card_cva == "skip":
                                print(f"Skipping {user1.name}'s turn")
                                time.sleep(2)
                                os.system('clear')

                                print(f"{atf1.name} played: {played}")
                                time.sleep(2)
                                os.system('clear')
                                chosen_turn = 1
                            elif card_cva == "reverse":
                                print("Turns are reverse")
                                time.sleep(2)
                                os.system('clear')

                                print(f"{atf1.name} played: {played}")
                                time.sleep(2)
                                os.system('clear')
                                chosen_turn = (chosen_turn + 1) % 2
                            elif card_cva == "draw_two":
                                print(f"{atf1.name} played: {played}")
                                time.sleep(2)
                                os.system('clear')

                                print(f"{user1.name} is forced to draw two cards.")

                                for _ in range(2):
                                    user1.draw_card()
                                time.sleep(2)
                                os.system('clear')
                                chosen_turn = 0
                    elif card_cvp == starting_color:
                        print(f"{atf1.name} played: {played}")

                        time.sleep(3)
                        os.system('clear')
                        valid_move = True

                        # chosen_turn = 0
                    elif played1 in ["WILD", "W.DRAWF"]:
                        ai_chosecolor = random.choice(st_olor)
                        starting_color = ai_chosecolor
                        print(f"The new color is {starting_color}...")
                        if played1 == "W.DRAWF":
                            for _ in range(4):

                                user1.draw_card()
                            print(
                                    f"{user1.name} has been "
                                    "penalized four cards."
                                    )
                            time.sleep(2)
                            os.system('clear')
                        print(f"{atf1.name} played: {played}")
                        time.sleep(2)
                        os.system('clear')
                        valid_move = True
                        chosen_turn = 0

                    else:
                        print(
                                "AI Try again for the card u "
                                "picked has a color "
                                "not matching the current color"
                                )
                        atf1.hand.append(played)
                        attempts += 1
                if not valid_move:
                    print(
                            f"{atf1.name} couldn't play a "
                            "valid card and draws a new one."
                            )
                    atf1.draw_card()

                chosen_turn = 0
            else:
                print(f"{atf1.name} has no cards left!")

            time.sleep(1)
            os.system('clear')


gamest()
