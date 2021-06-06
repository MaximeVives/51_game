import random


class Cards:
    card_pattern = [7, 8, 9, 10, 2, 3, 4, 1]
    cards = card_pattern * 4

    def __init__(self):
        random.shuffle(self.cards)


