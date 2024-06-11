
class Card:
    def __init__(self, number, suit, points):
        self._number = number
        self._suit = suit 
        self._points = points 

    def get_number(self):
        return self._number

    def get_suit(self):
        return self._suit

    def get_points(self):
        return self._points

class CardDeck:
    def __init__(self):
        self._card_stack = []
        number_points_dict = {3:1, 4:2, 5:3, 6:5, 7:8, 8:13, 9:21, 
            10:34, 11:55, 12:89, 13:144, 1:233, 2:377, 14:610, 15:987}

        for n in range(1, 14):
            for suit in ["hearts", "diamonds", "clubs", "spades"]:
                points = number_points_dict[n]
                card = Card(n, suit, points)
                self._card_stack.append(card)

        self._card_stack.append(Card(14, "joker", 610))
        self._card_stack.append(Card(15, "joker", 987))