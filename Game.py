from Cards import *
from Player import *
from os import system


def clear_board():
    system('cls')


class Game:
    nbr_player = 0
    players = []
    deck = Cards()
    default = []
    score = 0
    choice_card = 0
    index_player = 0

    def __init__(self):
        choice = int(input('How many players are you ? (min: 2 | max: 4)\n'))

        while choice < 2 or choice > 4:
            choice = int(input(f"You can't play with {choice} players. How many players are you ? (min: 2 | max: 4)\n"))

        self.nbr_player = choice
        self.set_players()
        self.distribute_cards()

        self.game_logic()

    def set_players(self):
        for x in range(self.nbr_player):
            self.players.append(Player())

    def distribute_cards(self):
        for i in range(3):
            for player in self.players:
                player.cards_player.append(self.deck.cards.pop(0))

    def game_logic(self):
        while self.score <= 50:
            clear_board()

            print(f"C'est au tour du J{(self.index_player % self.nbr_player) + 1}.\nLe score est à : {self.score}. Vos cartes : {self.players[self.index_player].cards_player}")

            self.action_player()

            self.index_player = (self.index_player + 1) % self.nbr_player

        self.end_game()

    def action_player(self):
        self.card_choice(self.players[self.index_player].cards_player)

        self.put_card()

    def card_choice(self, list_cards):
        self.choice_card = int(input("Quelle carte choisissez-vous ?"))
        while self.choice_card not in list_cards:
            self.choice_card = int(input("Choix Incorrect. Quelle carte choisissez-vous ?"))

    def put_card(self):
        self.players[self.index_player].cards_player.remove(self.choice_card)
        self.default.append(self.choice_card)

        self.players[self.index_player].cards_player.append(self.deck.cards.pop(0))

        if len(self.deck.cards) == 0:
            self.deck.cards.extend(self.default)
            self.default = []

        self.card_score()

    def card_score(self):
        card = self.choice_card
        alternative_score = 0

        if card == 1:
            alternative_score = int(input("Vous avez choisi l'AS, souhaitez-vous faire +1 (1) ou +11 (11) : "))
            while alternative_score != 1 and alternative_score != 11:
                alternative_score = int(input("Votre choix est incorrect ! Vous avez choisi l'AS, souhaitez-vous "
                                              "faire +1 (1) ou +11 (11) : "))

            card = alternative_score

        elif card == 9:
            card = 0

        elif card == 10:
            alternative_score = (input("Vous avez choisi le 10, souhaitez-vous faire +10 (+) ou -10 (-) : "))
            while alternative_score != "+" and alternative_score != "-":
                alternative_score = (input("Votre choix est incorrect ! Vous avez choisi le 10, souhaitez-vous "
                                           "faire +10 (+) ou -10 (-) : "))

            if alternative_score == "-":
                card = -10
            else:
                card = 10

        else:
            pass

        self.choice_card = card
        self.score += self.choice_card

    def end_game(self):
        print(f"Le J{self.index_player} a perdu.")
