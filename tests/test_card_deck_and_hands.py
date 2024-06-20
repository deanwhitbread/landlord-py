import unittest
from card_deck import CardDeck, Card
from card_hand import CardHand 
from tests import helpers

class CardDeckTestCase(unittest.TestCase):
    def setUp(self):
        self.solo_hand = [[3],[11],[2],[14],[15],[5]] 

    def tearDown(self):
        self.__class__.hand.reset()
        del self.solo_hand
    
    @classmethod
    def setUpClass(cls):
        cls.deck = CardDeck()
        cls.hand = CardHand()
        cls.hlpr = helpers.TestHelpers()

    @classmethod
    def tearDownClass(cls):
        del cls.deck
        del cls.hand
        del cls.hlpr

    '''
        Tests for Card class
    '''
    def test_card_has_number_value(self):
        '''Test that the playing card has a number value.'''
        self.assertEqual(len(self.__class__.deck._card_stack), 54)
        for card in self.__class__.deck._card_stack:
            self.assertIn(card.get_number(), self.hlpr.card_numbers)

    def test_card_has_suit(self):
        '''Test that the playing card has a single suit.'''
        self.assertEqual(len(self.__class__.deck._card_stack), 54)
        for card in self.__class__.deck._card_stack:
            self.assertIn(card.get_suit(), self.hlpr.suits) 

    def test_deck_has_no_duplicate_cards(self):
        '''Test the entire deck for duplicate card value and suit.'''
        self.assertEqual(len(self.__class__.deck._card_stack), 54)

        hearts = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        diamonds = hearts.copy()
        clubs = hearts.copy()
        spades = hearts.copy()
        jokers = [14, 15]
        for card in self.__class__.deck._card_stack:
            suit = card.get_suit()
            number = card.get_number()

            if suit == "hearts":
                hearts[number-1] = True
            elif suit == "diamonds":
                diamonds[number-1] = True
            elif suit == "clubs":
                clubs[number-1] = True
            elif suit == "spades":
                spades[number-1] = True
            elif suit == "joker":
                jokers[number-14] = True
            else:
                self.fail("Unrecognised suit.")
        
        self.assertTrue(all(hearts) and all(diamonds) and all(clubs) and 
            all(spades) and all(jokers))
    
    def test_card_has_points(self):
        '''Test playing card has a point value assoicated to it.'''
        self.assertEqual(len(self.__class__.deck._card_stack), 54)
        for card in self.__class__.deck._card_stack:
            self.assertTrue(card.get_points()>0)

    def test_card_ranking_follows_fibonacci_sequence(self):
        '''Test point ranking system uses fibonacci sequence.'''
        self.assertEqual(len(self.__class__.deck._card_stack), 54)

        for card in self.__class__.deck._card_stack:
            points = card.get_points()
            number = card.get_number()
            self.assertEqual(points, self.hlpr.number_points_dict[number])

    def test_point_ranking_on_card_number_value(self):
        '''Test that the order of points for card numbers following the 
        order: 3,4,5,6,7,8,9,10,J,Q,K,A,2,Black Joker,Red Joker.
        '''
        self.assertEqual(len(self.__class__.deck._card_stack), 54)

        
        for card in self.__class__.deck._card_stack:
            key = card.get_number()
            points = card.get_points()
            self.assertEqual(points, self.hlpr.number_points_dict[key])

    '''
        Tests for CardHand class.
    '''
    def test_select_method_adds_any_set_of_cards_to_the_hand(self):
        '''Test the select method adds any set of choosen cards to the player's hand.'''
        hands = self.hlpr.get_valid_pair_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.__class__.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.select(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_invalid_pair_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.__class__.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.select(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_valid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.__class__.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.select(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_invalid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.__class__.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.select(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_valid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.__class__.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.select(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_invalid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.__class__.hand.reset()
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

    '''
        Card Hand Ranking
    '''
    def test_ranking_for_valid_hands(self):
        '''Test the point ranking for all valid card hands.'''
        best_solo_hand = [self.hlpr._create_card_object_for_card_number(15, "joker")]
        self.hand.calculate_hand_score(best_solo_hand)
        best_solo_hand_score = self.hand.hand_score
        
        best_pair_hand = [self.hlpr._create_card_object_for_card_number(2)] * 2
        self.hand.calculate_hand_score(best_pair_hand)
        best_pair_hand_score = self.hand.hand_score

        best_trio_hand = [self.hlpr._create_card_object_for_card_number(2)] * 3
        self.hand.calculate_hand_score(best_trio_hand)
        best_trio_hand_score = self.hand.hand_score

        best_bomb_hand = [self.hlpr._create_card_object_for_card_number(2)] * 4
        self.hand.calculate_hand_score(best_bomb_hand)
        best_bomb_hand_score = self.hand.hand_score
        
        best_rocket_hand = [self.hlpr._create_card_object_for_card_number(14, "joker"), 
            self.hlpr._create_card_object_for_card_number(15, "joker")]
        self.hand.calculate_hand_score(best_rocket_hand)
        best_rocket_hand_score = self.hand.hand_score

        self.assertTrue(best_solo_hand_score<
            best_pair_hand_score<
            best_trio_hand_score<
            best_bomb_hand_score<
            best_rocket_hand_score)