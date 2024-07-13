import unittest
from card_hand import CardHand, Card
from card_deck import CardDeck
from tests import helpers
from misc import constants as const

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
    
    def test_get_card_category_function_returns_category(self):
        hands = [[11],[3,4,5,6,7,8],[8,8],[11,11,12,12,13,13],[2,2,2],[4,4,4,5,5,5,6,6,6], 
            [5,5,5,12],[10,10,10,1,1],[3,3,3,4,4,4,5,5,5,7,9,11],[12,12,12,13,13,13,1,1,10,10],
            [7,7,7,7],[14,15]]
        category = [[const.CARD_CATEGORY.SOLO],[const.CARD_CATEGORY.SOLO_CHAIN],
            [const.CARD_CATEGORY.PAIR],[const.CARD_CATEGORY.PAIR_CHAIN],
            [const.CARD_CATEGORY.TRIO],[const.CARD_CATEGORY.TRIO_CHAIN],
            [const.CARD_CATEGORY.TRIO_WITH_SOLO],[const.CARD_CATEGORY.TRIO_WITH_PAIR],
            [const.CARD_CATEGORY.AIRPLANE_WITH_SOLO],
            [const.CARD_CATEGORY.AIRPLANE_WITH_PAIR],
            [const.CARD_CATEGORY.BOMB],[const.CARD_CATEGORY.ROCKET]]

        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for i in range(len(hands)):
            hand = hands[i]
            self.assertEqual(self.hand.get_hand_category(hand), category[i].pop())

    def test_set_random_hand_function_with_category_set_returns_stronger_hand_in_the_same_category(self):
        opponent_hands = [[3,3,4,4,5,5], [5,6,7,8,9], [11,11,11,3,3], [6]] 
        opponent_hands = self.hlpr.convert_hand_numbers_to_card_objects(opponent_hands)
        player_cards = [[3,3,7,7,8,8,9,9,12,13,2], [3,3,3,4,9,10,11,12,13,13,1,15], [3,5,5,6,6,7,7,13,13,13], [3,3,3,4,4,11,2]]
        player_cards = self.hlpr.convert_hand_numbers_to_card_objects(player_cards)
        for i in range(len(opponent_hands)):
            op_hand = opponent_hands[i]
            op_hand_category = self.hand.get_hand_category(op_hand)
            self.hand.calculate_hand_score(op_hand)
            op_hand_score = self.hand.hand_score
            player_hand = self.hand.set_random_hand(player_cards[i], op_hand)
            player_hand_category = self.hand.get_hand_category(player_hand)
            self.assertEqual(player_hand_category, op_hand_category) 
            self.hand.calculate_hand_score(player_hand)
            player_hand_score = self.hand.hand_score
            self.assertTrue(player_hand_score>op_hand_score)
            self.hand.reset()

    def test_set_random_hand_function_returns_none_when_category_set_but_no_hands_in_that_category(self):
        opponent_hands = [[3,3,4,4,5,5], [5,6,7,8,9], [11,11,11,8], [6]] 
        opponent_hands = self.hlpr.convert_hand_numbers_to_card_objects(opponent_hands)
        player_cards = [[4,4,5,5,8,8,1,15], [3,4,5,6,7,8,9,13,2,2], [3,3,3,5,10,10,1,2], [3,3,4,4,5,5]]
        player_cards = self.hlpr.convert_hand_numbers_to_card_objects(player_cards)
        for i in range(len(opponent_hands)):
            player_hand = self.hand.set_random_hand(player_cards[i], opponent_hands[i])
            self.assertEqual(len(player_hand), 0) 
            self.hand.reset()
    