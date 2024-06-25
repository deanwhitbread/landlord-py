from card_deck import Card
import game_rules as rules
from collections import Counter

class CardHand:
    def __init__(self):
        '''Construct a CardHand object. A CardHand object represents a player's
        hand in a card game. 
        '''
        self.reset()

    def select(self, hand: list[Card]):
        '''Set the selected cards as the player's card hand.
        
        Args:
            hand - A list of Card objects representing the players' hand. 
        '''
        self.current_hand = hand

    def play(self) -> bool:
        '''Return whether the selected hand can be played. 
        
        Returns: True if the selected hand can be played, False otherwise. 
        '''
        if not self.current_hand:
            return False

        # count the frequency of the card numbers
        number_freq = self.get_card_number_frequency_map(self.current_hand)
        
        # calculate score of hand. 
        self.calculate_hand_score(self.current_hand)

        # check whether the hand is valid and can be played.
        if len(self.current_hand)==1:
            return rules.is_solo(number_freq)
        elif len(self.current_hand)==2:
            return (rules.is_pair(number_freq) or 
                rules.is_rocket(number_freq))
        elif len(self.current_hand)==3:
            return rules.is_trio(number_freq)
        else:
            return (rules.is_bomb(number_freq) or 
                rules.is_combination(number_freq) or 
                rules.is_chain(number_freq))

    def reset(self):
        '''Clear the player's hand, removing all selected cards.'''
        self.current_hand = list()
        self.hand_score = 0

    def calculate_hand_score(self, hand: list[Card]):  
        '''Calculate the score of the player's current hand.
        
        Args:
            hand - A list of Card objects representing the players' hand.
        '''
        number_freq = self.get_card_number_frequency_map(hand)
        multiplier = 2 if rules.is_bomb(number_freq) or rules.is_rocket(number_freq) else 1

        self.hand_score = int(sum(card.get_points() for card in hand) * multiplier)

    def get_card_number_frequency_map(self, hand: list[Card]) -> Counter[int:int]:
        '''Return a hash map mapping card numbers in the hand to the frequency the numbers
        appears in the hand.
        
        Args:
            hand - A list of Card objects representing the players' hand. 
        '''
        return Counter([card.get_number() for card in hand])
        