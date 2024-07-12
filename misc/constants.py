
JACK_REPR = "J"
QUEEN_REPR = "Q"
KING_REPR = "K"
ACE_REPR = "A"
RED_JOKER_REPR = "RJ"
BLACK_JOKER_REPR = "BJ"

SPECIAL_CARDS_MAP = {1:ACE_REPR, 11:JACK_REPR, 12:QUEEN_REPR, 
    13:KING_REPR, 14:BLACK_JOKER_REPR, 15:RED_JOKER_REPR}

class CARD_CATEGORY: 
    SOLO = 0
    SOLO_CHAIN = 1 
    PAIR = 2
    PAIR_CHAIN = 3 
    TRIO = 4
    TRIO_CHAIN = 5
    TRIO_WITH_SOLO = 6 
    TRIO_WITH_PAIR = 7
    AIRPLANE_WITH_SOLO = 8 
    AIRPLANE_WITH_PAIR = 9
    BOMB = 10
    ROCKET = 11