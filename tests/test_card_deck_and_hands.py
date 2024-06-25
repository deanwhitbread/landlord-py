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
    def test_bomb_beat_solo_hands(self):
        '''Test that the bomb card hand beats both solo hand and 
        solo chain hand.'''
        bomb_hand = [[2,2,2,2]]
        bomb_hand = self.hlpr.convert_hand_numbers_to_card_objects(bomb_hand)
        self.hand.calculate_hand_score(bomb_hand.pop())
        bomb_score = self.hand.hand_score

        solo_hand = self.hlpr.convert_hand_numbers_to_card_objects([[15]])
        self.hand.calculate_hand_score(solo_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

        solo_hand = self.hlpr.convert_hand_numbers_to_card_objects([[3,4,5,6,7,8,9,10,11,12,13,1]])
        self.hand.calculate_hand_score(solo_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

    def test_bomb_beat_pair_hands(self):
        '''Test that the bomb card hand beats both pair hand and 
        pair chain hand.'''
        bomb_hand = [[2,2,2,2]]
        bomb_hand = self.hlpr.convert_hand_numbers_to_card_objects(bomb_hand)
        self.hand.calculate_hand_score(bomb_hand.pop())
        bomb_score = self.hand.hand_score

        pair_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2]])
        self.hand.calculate_hand_score(pair_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

        pair_hand = self.hlpr.convert_hand_numbers_to_card_objects([[5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,1,1]])
        self.hand.calculate_hand_score(pair_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

    def test_bomb_beat_trio_hands(self):
        '''Test that the bomb card hand beats trio hand, trio 
        chain hand, and trio with solo hand.'''
        bomb_hand = [[2,2,2,2]]
        bomb_hand = self.hlpr.convert_hand_numbers_to_card_objects(bomb_hand)
        self.hand.calculate_hand_score(bomb_hand.pop())
        bomb_score = self.hand.hand_score

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2,2]])
        self.hand.calculate_hand_score(trio_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[9,9,9,10,10,10,11,11,11,12,12,12,13,13,13,1,1,1]])
        self.hand.calculate_hand_score(trio_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2,2,15]])
        self.hand.calculate_hand_score(trio_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2,2,1,1]])
        self.hand.calculate_hand_score(trio_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

    def test_bomb_beat_airplane_hands(self):
        '''Test that the bomb card hand beats both airplane with solo 
        hand and airplane with pair hand.'''
        bomb_hand = [[2,2,2,2]]
        bomb_hand = self.hlpr.convert_hand_numbers_to_card_objects(bomb_hand)
        self.hand.calculate_hand_score(bomb_hand[0])
        bomb_score = self.hand.hand_score

        airplane_hand = self.hlpr.convert_hand_numbers_to_card_objects([[10,10,10,11,11,11,12,12,12,13,13,13,1,1,1,5,6,7,8,9]])
        self.hand.calculate_hand_score(airplane_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

        airplane_hand = self.hlpr.convert_hand_numbers_to_card_objects([[11,11,11,12,12,12,13,13,13,1,1,1,6,6,7,7,8,8,9,9]])
        self.hand.calculate_hand_score(airplane_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

    def test_rocket_beat_solo_hands(self):
        '''Test that the rocket card hand beats both solo hand and 
        solo chain hand.'''
        rocket_hand = self.hlpr.convert_hand_numbers_to_card_objects([[14,15]])
        self.hand.calculate_hand_score(rocket_hand.pop())
        rocket_score = self.hand.hand_score

        solo_hand = self.hlpr.convert_hand_numbers_to_card_objects([[15]])
        self.hand.calculate_hand_score(solo_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

        solo_hand = self.hlpr.convert_hand_numbers_to_card_objects([[3,4,5,6,7,8,9,10,11,12,13,1]])
        self.hand.calculate_hand_score(solo_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

    def test_rocket_beat_pair_hands(self):
        '''Test that the rocket card hand beats both pair hand and 
        pair chain hand.'''
        rocket_hand = self.hlpr.convert_hand_numbers_to_card_objects([[14,15]])
        self.hand.calculate_hand_score(rocket_hand.pop())
        rocket_score = self.hand.hand_score

        pair_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2]])
        self.hand.calculate_hand_score(pair_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

        pair_hand = self.hlpr.convert_hand_numbers_to_card_objects([[5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,1,1]])
        self.hand.calculate_hand_score(pair_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

    def test_rocket_beat_trio_hands(self):
        '''Test that the rocket card hand beats trio hand, trio 
        chain hand, and trio with solo hand.'''
        rocket_hand = self.hlpr.convert_hand_numbers_to_card_objects([[14,15]])
        self.hand.calculate_hand_score(rocket_hand.pop())
        rocket_score = self.hand.hand_score

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2,2]])
        self.hand.calculate_hand_score(trio_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[9,9,9,10,10,10,11,11,11,12,12,12,13,13,13,1,1,1]])
        self.hand.calculate_hand_score(trio_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2,2,15]])
        self.hand.calculate_hand_score(trio_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2,2,1,1]])
        self.hand.calculate_hand_score(trio_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

    def test_rocket_beat_airplane_hands(self):
        '''Test that the rocket card hand beats airplane hand, airplance
        with solo hand, and airplane with pair hand.'''
        rocket_hand = self.hlpr.convert_hand_numbers_to_card_objects([[14,15]])
        self.hand.calculate_hand_score(rocket_hand.pop())
        rocket_score = self.hand.hand_score

        airplane_hand = self.hlpr.convert_hand_numbers_to_card_objects([[10,10,10,11,11,11,12,12,12,13,13,13,1,1,1,5,6,7,8,9]])
        self.hand.calculate_hand_score(airplane_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

        airplane_hand = self.hlpr.convert_hand_numbers_to_card_objects([[11,11,11,12,12,12,13,13,13,1,1,1,6,6,7,7,8,8,9,9]])
        self.hand.calculate_hand_score(airplane_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)