# -*- encoding: utf-8 -*-

# Карты
# Демонстрирует сочетание объектов


class Card(object):
    """Одна игральная карта."""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS =["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand(object):
    """Рука: набор карт на руках у одного игрока."""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
            else:
                rep = "<пусто>"
            return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

# основная часть
card1 = Card(rank="A", suit="c")
print "Вывожу на экран объект-карту:"
print card1
card2 = Card(rank="2", suit="c")
card3 = Card(rank="3", suit="c")
card4 = Card(rank="4", suit="c")
card5 = Card(rank="5", suit="c")
print "\nВывожу еще четыре карты:"
print card2
print card3
print card4
print card5
