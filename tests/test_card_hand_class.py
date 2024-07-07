import unittest
from card_hand import CardHand, Card
from card_deck import CardDeck
from tests import helpers

class CardHandTestCase(unittest.TestCase):
    def setUp(self):
        self.solo_hand = [[3],[11],[2],[14],[15],[5]]

    def tearDown(self):
        self.hand.reset()
        self.deck.reset()
    
    @classmethod
    def setUpClass(cls):
        cls.hand = CardHand()
        cls.hlpr = helpers.TestHelpers()
        cls.deck = CardDeck()

    @classmethod
    def tearDownClass(cls):
        del cls.hand
        del cls.hlpr
        del cls.deck

    def test_select_method_adds_any_set_of_cards_to_the_hand(self):
        '''Test the select method adds any set of choosen cards to the player's hand.'''
        hands = self.hlpr.get_valid_pair_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.select(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_invalid_pair_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.select(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_valid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.select(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_invalid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.select(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_valid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.select(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_invalid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.select(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

    def test_cannot_play_empty_hand(self):
        '''Test play method disallows playing an empty hand.'''
        self.assertFalse(self.__class__.hand.play())

    def test_play_method(self):
        '''Test play method allows a valid hand to be played.'''
        hands = self.hlpr.get_valid_trio_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.select(hand)
            self.assertTrue(self.hand.play())
        
        hands = self.hlpr.get_valid_bomb_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.select(hand)
            self.assertTrue(self.hand.play())

        hands = self.hlpr.get_valid_combination_with_solo_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.select(hand)
            self.assertTrue(self.hand.play())
    
    def test_reset_method_clears_current_hand(self):
        '''Test reset method clears the player's current hand.'''
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.select(hand)
            self.assertTrue(len(self.hand.current_hand)>=5)
            self.__class__.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)

        solo_hand = self.hlpr.convert_hand_numbers_to_card_objects(self.solo_hand)
        for hand in solo_hand:
            self.hand.select(hand)
            self.assertEqual(len(self.hand.current_hand), 1)
            self.__class__.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)

    def test_set_random_hand_function_chooses_a_valid_hand_from_cards(self):
        self.deck.shuffle()
        c1, c2, c3, wildcards = self.deck.deal()
        self.hand.set_random_hand(c1)
        self.assertIsNotNone(self.hand.get_hand())
        self.assertTrue(self.hand.play()) 
        self.hand.reset()

        self.hand.set_random_hand(c1+wildcards)
        self.assertIsNotNone(self.hand.get_hand())
        self.assertTrue(self.hand.play()) 
        self.hand.reset()

        self.hand.set_random_hand(c2[:5])
        self.assertIsNotNone(self.hand.get_hand())
        self.assertTrue(self.hand.play()) 
        self.hand.reset()

        self.hand.set_random_hand(c3[4:14])
        self.assertIsNotNone(self.hand.get_hand())
        self.assertTrue(self.hand.play()) 
        self.hand.reset()

        self.hand.set_random_hand([Card(3, "hearts")])
        self.assertIsNotNone(self.hand.get_hand())
        self.assertTrue(self.hand.play()) 
        self.hand.reset()

        self.hand.set_random_hand(wildcards)
        self.assertIsNotNone(self.hand.get_hand())
        self.assertTrue(self.hand.play()) 
        self.hand.reset()

    def test_set_random_hand_raises_type_error_when_non_card_object_parameter_passed(self):
        with self.assertRaises(TypeError):
            card = Card(3, "hearts")
            self.hand.set_random_hand(card)

        with self.assertRaises(TypeError):
            self.hand.set_random_hand([3,3,3,4,4,4,5,5,5,6,6,6,10,10,2,2,15])

        with self.assertRaises(TypeError):
            self.hand.set_random_hand()

    def test_set_random_hand_raises_value_error_when_empty_list_is_passed(self):
        with self.assertRaises(ValueError):
            self.hand.set_random_hand(list())
    