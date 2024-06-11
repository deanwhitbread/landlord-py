import unittest
from card_deck import CardDeck

class CardDeckTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deck = CardDeck()

    @classmethod
    def tearDownClass(cls):
        del cls.deck

    '''
        Card Representation 
    '''
    def test_card_has_number_value(self):
        '''Test that the playing card has a number value.'''
        pass

    def test_card_has_suit(self):
        '''Test that the playing card has a single suit.'''
        pass 

    def test_deck_has_no_duplicate_cards(self):
        '''Test the entire deck for duplicate card value and suit.'''
        pass
    
    def test_card_has_points(self):
        '''Test playing card has a point value assoicated to it.'''
        pass 

    def test_card_ranking_follows_fibonacci_sequence(self):
        '''Test point ranking system uses fibonacci sequence.'''
        pass

    def test_point_ranking_on_card_number_value(self):
        '''Test that the order of points for card numbers following the 
        order: 3,4,5,6,7,8,9,10,J,Q,K,A,2,Black Joker,Red Joker.
        '''
        pass 

    '''
        Card Hands
    '''
    def test_solo_card_hand(self):
        '''Test all valid solo card hands.'''
        pass 

    def test_valid_solo_chain_card_hand(self):
        '''Test all valid solo chain card hands.'''
        pass

    def test_invalid_solo_chain_card_hand(self):
        '''Test all invalid solo chain card hands.'''
        pass

    def test_valid_pair_card_hand(self):
        '''Test all valid pair card hands.'''
        pass 
    
    def test_invalid_pair_card_hand(self):
        '''Test all invalid pair card hands.'''
        pass 
    
    def test_valid_pair_chain_hand(self):
        '''Test all valid pair chain card hands.'''
        pass 

    def test_invalid_pair_chain_hand(self):
        '''Test all invalid pair chain hands.'''
        pass 

    def test_valid_trio_card_hand(self):
        '''Test all valid trio card hands.'''
        pass 

    def test_invalid_trio_card_hand(self):
        '''Test all invalid trio card hands.'''
        pass 

    def test_trio_and_solo_card_hand(self):
        '''Test all valid trio with solo card hands.'''
        pass 

    def test_trio_and_pair_card_hand(self):
        '''Test all valid trio with pair card hands.'''
        pass 

    def test_valid_trio_and_pair_chain_card_hand(self):
        '''Test all valid trio with pair chain card hands.'''
        pass 

    def test_invalid_trio_and_pair_chain_card_hand(self):
        '''Test all invalid trio with pair chain card hands.'''
        pass 

    def test_airplane_card_hand(self):
        '''Test all valid airplane chain hands.'''
        pass 

    def test_trio_solo_and_airplane_card_hand(self):
        '''Test all valid trio with solo and airplane card hands.'''
        pass 

    def test_bomb_card_hand(self):
        '''Test all valid bomb card hands.'''
        pass 

    def test_bomb_with_dual_solo_card_hand(self):
        '''Test all valid bomb with solo card hands.'''
        pass 

    def test_valid_bomb_dual_pair_card_hand(self):
        '''Test all valid bomb with dual pair card hands.'''
        pass 

    def test_invalid_bomb_dual_pair_card_hand(self):
        '''Test all invalid bomb with dual pair card hands.'''
        pass 

    def test_pair_chain_is_not_a_bomb_card_hand(self):
        '''Test that the pair chain card hand is not a bomb card hand.'''
        pass

    def test_rocket_card_hand(self):
        '''Test rocked card hand.'''
        pass

    def test_bomb_with_rocket_hands_card_hands(self):
        '''Test that bomb and rocket card hands cannot be played together.'''
        pass

    '''
        Card Hand Ranking
    '''
    def test_ranking_for_valid_hands(self):
        '''Test the point ranking for all valid card hands.'''
        pass