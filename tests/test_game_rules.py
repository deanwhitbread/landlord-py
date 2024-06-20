import unittest
from tests import helpers 
import game_rules as rules

class GameRulesTestCase(unittest.TestCase):
    def setUp(self):
        self.solo_hand = [[3],[11],[2],[14],[15],[5]] 
    
    def tearDown(self):
        del self.solo_hand

    @classmethod
    def setUpClass(cls):
        cls.hlpr = helpers.TestHelpers()

    @classmethod
    def tearDownClass(cls):
        del cls.hlpr

    ''' Card Hand Tests '''
    def test_valid_is_solo_hand(self):
        '''Test the is_solo_hand method returns true for valid card hands.'''
        hands = self.solo_hand
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_solo(hand, number_freq))

    def test_valid_is_solo_chain_hand(self):
        '''Test the is_solo_chain_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)            
            self.assertTrue(rules.is_solo_chain(hand, number_freq))

    def test_invalid_is_solo_chain_hand(self):
        '''Test the is_solo_chain_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_solo_card_chain_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_solo_chain(hand, number_freq))

    def test_valid_is_pair_hand(self):
        '''Test the is_pair_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_pair_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_pair(hand, number_freq))

    def test_invalid_is_pair_hand(self):
        '''Test the is_pair_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_pair_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_pair(hand, number_freq))

    def test_valid_is_pair_chain_hand(self):
        '''Test the is_pair_chain_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_pair_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_pair_chain(hand, number_freq))

    def test_invalid_is_pair_chain_hand(self):
        '''Test the is_pair_chain_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_pair_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_pair_chain(hand, number_freq))

    def test_valid_is_trio_hand(self):
        '''Test the is_trio_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_trio_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_trio(hand, number_freq))

    def test_invalid_is_trio_hand(self):
        '''Test the is_trio_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_trio_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_trio(hand, number_freq))

    def test_valid_is_trio_chain_hand(self):
        '''Test the is_trio_chain_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_trio_chain(hand, number_freq))

    def test_invalid_is_trio_chain_hand(self):
        '''Test the is_trio_chain_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_trio_chain(hand, number_freq))

    def test_valid_is_bomb_hand(self):
        '''Test the is_bomb_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_bomb_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_bomb(hand, number_freq))
    
    def test_invalid_is_bomb_hand(self):
        '''Test the is_bomb_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_bomb_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_bomb(hand, number_freq))

    def test_valid_is_rocket_hand(self):
        '''Test the is_rocket_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_rocket_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_rocket(hand))
    
    def test_invalid_is_rocket_hand(self):
        '''Test the is_rocket_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_rocket_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_rocket(hand))

    def test_valid_is_chain_hand(self):
        '''Test the is_chain_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_chain(hand, number_freq))
        
        hands = self.hlpr.get_valid_pair_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_chain(hand, number_freq))

        hands = self.hlpr.get_valid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_chain(hand, number_freq))

    def test_invalid_is_chain_hand(self):
        '''Test the is_chain_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_solo_card_chain_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_chain(hand, number_freq))
        
        hands = self.hlpr.get_invalid_pair_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_chain(hand, number_freq))

        hands = self.hlpr.get_invalid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_chain(hand, number_freq))

    def test_valid_is_combination_hand(self):
        '''Test the is_combination_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_combination_with_solo_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_combination(hand, number_freq)) 

        hands = self.hlpr.get_valid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_combination(hand, number_freq)) 
    
    def test_invalid_is_combination_hand(self):
        '''Test the is_combination_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_combination_with_solo_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_combination(hand, number_freq)) 

        hands = self.hlpr.get_invalid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_combination(hand, number_freq)) 
    
    def test_valid_contains_solo_hand(self):
        '''Test the contains_solo_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_combination_with_solo_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.contains_solo_hand(hand, number_freq))

    def test_invalid_contains_solo_hand(self):
        '''Test the contains_solo_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_combination_with_solo_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.contains_solo_hand(hand, number_freq)) 

    def test_valid_contains_pair_hand(self):
        '''Test the contains_pair_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.contains_pair_hand(hand, number_freq)) 

    def test_invalid_contains_pair_hand(self):
        '''Test the contains_pair_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.contains_pair_hand(hand, number_freq)) 