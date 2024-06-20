from card_deck import Card
import game_rules as rules

class CardHand:
    def __init__(self):
        '''Construct a CardHand object. A CardHand object represents a player's
        hand in a card game. 
        '''
        self.reset()

    def select(self, hand):
        '''Set the selected cards as the player's card hand.
        
        Args:
            hand - A collection of Card objects containing at least one object. 
        '''
        self.current_hand = hand

    def play(self) -> bool:
        '''Return whether the selected hand can be played. 
        
        Returns: True if the selected hand can be played, False otherwise. 
        '''
        if not self.current_hand:
            return False

        # count the frequency of the card numbers
        number_freq = dict()
        for card in self.current_hand:
            if card.get_number() in number_freq.keys():
                number_freq[card.get_number()] += 1
            else:
                number_freq[card.get_number()] = 1

        if len(self.current_hand)==1:
            return rules.is_solo(self.current_hand, number_freq)
        elif len(self.current_hand)==2:
            return (rules.is_pair(self.current_hand, number_freq) or 
                rules.is_rocket(self.current_hand))
        elif len(self.current_hand)==3:
            return rules.is_trio(self.current_hand, number_freq)
        else:
            return (rules.is_bomb(self.current_hand, number_freq) or 
                rules.is_combination(self.current_hand, number_freq) or 
                rules.is_chain(self.current_hand, number_freq))

    def reset(self):
        '''Clear the player's hand, removing all selected cards.'''
        self.current_hand = list()        
        