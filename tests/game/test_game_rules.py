import unittest
from tests import helpers 
import misc.constants as const
import game.rules as rules

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
            self.assertTrue(rules.is_solo(number_freq))

    def test_valid_is_solo_chain_hand(self):
        '''Test the is_solo_chain_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)            
            self.assertTrue(rules.is_solo_chain(number_freq))

    def test_invalid_is_solo_chain_hand(self):
        '''Test the is_solo_chain_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_solo_card_chain_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_solo_chain(number_freq))

    def test_valid_is_pair_hand(self):
        '''Test the is_pair_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_pair_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_pair(number_freq))

    def test_invalid_is_pair_hand(self):
        '''Test the is_pair_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_pair_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_pair(number_freq))

    def test_valid_is_pair_chain_hand(self):
        '''Test the is_pair_chain_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_pair_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_pair_chain(number_freq))

    def test_invalid_is_pair_chain_hand(self):
        '''Test the is_pair_chain_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_pair_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_pair_chain(number_freq))

    def test_valid_is_trio_hand(self):
        '''Test the is_trio_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_trio_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_trio(number_freq))

    def test_invalid_is_trio_hand(self):
        '''Test the is_trio_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_trio_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_trio(number_freq))

    def test_valid_is_trio_chain_hand(self):
        '''Test the is_trio_chain_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_trio_chain(number_freq))

    def test_invalid_is_trio_chain_hand(self):
        '''Test the is_trio_chain_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_trio_chain(number_freq))

    def test_valid_is_bomb_hand(self):
        '''Test the is_bomb_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_bomb_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_bomb(number_freq))
    
    def test_invalid_is_bomb_hand(self):
        '''Test the is_bomb_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_bomb_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_bomb(number_freq))

    def test_valid_is_rocket_hand(self):
        '''Test the is_rocket_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_rocket_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_rocket(number_freq))
    
    def test_invalid_is_rocket_hand(self):
        '''Test the is_rocket_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_rocket_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_rocket(number_freq))

    def test_valid_is_chain_hand(self):
        '''Test the is_chain_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_chain(number_freq))
        
        hands = self.hlpr.get_valid_pair_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_chain(number_freq))

        hands = self.hlpr.get_valid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_chain(number_freq))

    def test_invalid_is_chain_hand(self):
        '''Test the is_chain_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_solo_card_chain_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_chain(number_freq))
        
        hands = self.hlpr.get_invalid_pair_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_chain(number_freq))

        hands = self.hlpr.get_invalid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_chain(number_freq))

    def test_valid_is_combination_hand(self):
        '''Test the is_combination_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_combination_with_solo_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_combination(number_freq)) 

        hands = self.hlpr.get_valid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_combination(number_freq)) 
    
    def test_invalid_is_combination_hand(self):
        '''Test the is_combination_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_combination_with_solo_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_combination(number_freq)) 

        hands = self.hlpr.get_invalid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_combination(number_freq)) 
    
    def test_valid_contains_solo_hand(self):
        '''Test the contains_solo_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_combination_with_solo_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.contains_solo_hand(number_freq))

    def test_invalid_contains_solo_hand(self):
        '''Test the contains_solo_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_combination_with_solo_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.contains_solo_hand(number_freq)) 

    def test_valid_contains_pair_hand(self):
        '''Test the contains_pair_hand method returns true for valid card hands.'''
        hands = self.hlpr.get_valid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.contains_pair_hand(number_freq)) 

    def test_invalid_contains_pair_hand(self):
        '''Test the contains_pair_hand method returns false for invalid card hands.'''
        hands = self.hlpr.get_invalid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.contains_pair_hand(number_freq)) 

    def test_valid_contains_trio_hand_function(self):
        hands = self.hlpr.get_valid_trio_chain_card_hand()
        hands += self.hlpr.get_valid_trio_with_solo_hands() 
        hands += self.hlpr.get_valid_trio_with_pair_hands()
        hands += self.hlpr.get_valid_airplane_with_solo_hands()
        hands += self.hlpr.get_valid_airplane_with_pair_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.contains_trio_hand(number_freq)) 

    def test_invalid_contains_trio_hand_function(self):
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands += self.hlpr.get_valid_pair_card_hand()
        hands += self.hlpr.get_valid_bomb_card_hand()
        hands += self.hlpr.get_valid_rocket_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.contains_trio_hand(number_freq)) 

    def test_valid_contains_trio_chain_hand_function(self):
        hands = self.hlpr.get_valid_trio_chain_card_hand()
        hands += self.hlpr.get_valid_airplane_with_solo_hands()
        hands += self.hlpr.get_valid_airplane_with_pair_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.contains_trio_chain_hand(number_freq)) 

    def test_invalid_contains_trio_chain_hand_function(self):
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands += self.hlpr.get_valid_pair_card_hand()
        hands += self.hlpr.get_valid_trio_with_solo_hands()
        hands += self.hlpr.get_valid_trio_with_pair_hands()
        hands += self.hlpr.get_valid_bomb_card_hand()
        hands += self.hlpr.get_valid_rocket_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.contains_trio_chain_hand(number_freq)) 

    def test_valid_is_trio_with_solo_function(self):
        hands = self.hlpr.get_valid_trio_with_solo_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_trio_with_solo(number_freq)) 

    def test_invalid_is_trio_with_solo_function(self):
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands += self.hlpr.get_valid_pair_card_hand()
        hands += self.hlpr.get_valid_bomb_card_hand()
        hands += self.hlpr.get_valid_rocket_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_trio_with_solo(number_freq)) 

    def test_valid_is_trio_with_pair_function(self):
        hands = self.hlpr.get_valid_trio_with_pair_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_trio_with_pair(number_freq)) 

    def test_invalid_is_trio_with_pair_function(self):
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands += self.hlpr.get_valid_pair_card_hand()
        hands += self.hlpr.get_valid_bomb_card_hand()
        hands += self.hlpr.get_valid_rocket_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_trio_with_pair(number_freq)) 

    def test_valid_is_airplane_with_solo_function(self):
        hands = self.hlpr.get_valid_airplane_with_solo_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_airplane_with_solo(number_freq)) 

    def test_invalid_is_airplane_with_solo_function(self):
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands += self.hlpr.get_valid_pair_card_hand()
        hands += self.hlpr.get_valid_bomb_card_hand()
        hands += self.hlpr.get_valid_rocket_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_airplane_with_solo(number_freq)) 

    def test_valid_is_airplane_with_pair_function(self):
        hands = self.hlpr.get_valid_airplane_with_pair_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_airplane_with_pair(number_freq)) 

    def test_invalid_is_airplane_with_pair_function(self):
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands += self.hlpr.get_valid_pair_card_hand()
        hands += self.hlpr.get_valid_bomb_card_hand()
        hands += self.hlpr.get_valid_rocket_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_airplane_with_pair(number_freq)) 

    def test_valid_is_bomb_with_dual_solo_function(self):
        hands = self.hlpr.get_valid_bomb_with_dual_solo_card_hand() 
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_bomb_with_dual_solo(number_freq)) 

    def test_invalid_is_bomb_with_dual_solo_function(self):
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands += self.hlpr.get_valid_pair_card_hand()
        hands += self.hlpr.get_valid_bomb_card_hand()
        hands += self.hlpr.get_valid_rocket_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_bomb_with_dual_solo(number_freq))  

    def test_valid_is_bomb_with_dual_pair_function(self):
        hands = self.hlpr.get_valid_bomb_with_dual_pair_card_hand() 
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertTrue(rules.is_bomb_with_dual_pair(number_freq))  

    def test_invalid_is_bomb_with_dual_pair_function(self):
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands += self.hlpr.get_valid_pair_card_hand()
        hands += self.hlpr.get_valid_bomb_card_hand()
        hands += self.hlpr.get_valid_rocket_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertFalse(rules.is_bomb_with_dual_pair(number_freq))  

    def test_get_hand_category_function_returns_solo_card_category_when_hand_is_a_solo_hand(self):
        hands = [[4],[8],[13],[2],[14],[15]]
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.SOLO)
        
    def test_get_hand_category_function_returns_solo_chain_card_category_when_hand_is_a_solo_chain_hand(self):
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.SOLO_CHAIN)

    def test_get_hand_category_function_returns_pair_card_category_when_hand_is_a_pair_hand(self):
        hands = self.hlpr.get_valid_pair_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.PAIR)
    
    def test_get_hand_category_function_returns_pair_chain_card_category_when_hand_is_a_pair_chain_hand(self):
        hands = self.hlpr.get_valid_pair_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.PAIR_CHAIN)

    def test_get_hand_category_function_returns_trio_card_category_when_hand_is_a_trio_hand(self):
        hands = self.hlpr.get_valid_trio_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.TRIO)

    def test_get_hand_category_function_returns_trio_with_solo_card_category_when_hand_is_a_trio_with_solo_hand(self):
        hands = self.hlpr.get_valid_trio_with_solo_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.TRIO_WITH_SOLO)

    def test_get_hand_category_function_returns_trio_with_pair_card_category_when_hand_is_a_trio_with_pair_hand(self):
        hands = self.hlpr.get_valid_trio_with_pair_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.TRIO_WITH_PAIR)

    def test_get_hand_category_function_returns_trio_chain_card_category_when_hand_is_a_trio_chain_hand(self):
        hands = self.hlpr.get_valid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.TRIO_CHAIN)

    def test_get_hand_category_function_returns_airplane_with_solo_card_category_when_hand_is_an_airplane_with_solo_hand(self):
        hands = self.hlpr.get_valid_airplane_with_solo_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.AIRPLANE_WITH_SOLO)

    def test_get_hand_category_function_returns_airplane_with_pair_card_category_when_hand_is_an_airplane_with_pair_hand(self):
        hands = self.hlpr.get_valid_airplane_with_pair_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.AIRPLANE_WITH_PAIR)

    def test_get_hand_category_function_returns_bomb_card_category_when_hand_is_a_bomb_hand(self):
        hands = self.hlpr.get_valid_bomb_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.BOMB)

    def test_get_hand_category_function_returns_bomb_with_solo_card_category_when_hand_is_a_bomb_hand(self):
        hands = self.hlpr.get_valid_bomb_with_dual_solo_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.BOMB_WITH_SOLO)

    def test_get_hand_category_function_returns_bomb_with_pair_card_category_when_hand_is_a_bomb_hand(self):
        hands = self.hlpr.get_valid_bomb_with_dual_pair_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.BOMB_WITH_PAIR)

    def test_get_hand_category_function_returns_rocket_card_category_when_hand_is_a_rocket_hand(self):
        hands = self.hlpr.get_valid_rocket_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            number_freq = self.hlpr.get_number_frequency_map(hand)
            self.assertEqual(rules.get_hand_category(number_freq), const.CARD_CATEGORY.ROCKET)
    
    def test_get_hand_category_function_raises_runtime_error_when_hand_is_in_an_unrecognised_category(self):
        hands = self.hlpr.get_hands_with_unrecognised_card_category()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            with self.assertRaises(RuntimeError):
                number_freq = self.hlpr.get_number_frequency_map(hand)
                rules.get_hand_category(number_freq)
    