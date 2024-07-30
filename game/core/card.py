import misc.constants as const
import misc.helpers as hlpr

class Card:
    def __init__(self, number: int, suit: str):
        '''Construct a Card object.
        
        Args:
            number - An integer representing the card number. 
            suit - A string representing the card suit. 
        '''
        self._number = number
        self._suit = suit 
        self._points = self._get_card_points_value(self.get_number()) 

    def get_number(self) -> int:
        '''Return an integer representing the card number.'''
        return self._number

    def get_suit(self) -> str:
        '''Return a string representing the suit of the card.'''
        return self._suit

    def get_points(self) -> int:
        '''Return an integer representing the value of the card.'''
        return self._points

    def _get_card_points_map(self) -> dict[int:int]:
        '''Return a hash table that maps card number keys to a number representing
        the amount of points the card represents.'''
        return hlpr.get_fibonacci_sequence_hash_map()

    def _get_card_points_value(self, card_number: int) -> int:
        '''Return an integer representing the value of the individual card.
        
        Args:
            card_number - The number of the card to return the points value for. 
        '''
        return self._get_card_points_map()[card_number]
    
    def __repr__(self):
        if self.get_number()==1 or self.get_number()>10:
            return const.SPECIAL_CARDS_MAP[self.get_number()]
        else:
            return str(self.get_number())

    def __str__(self):
        return self.__repr__()
    