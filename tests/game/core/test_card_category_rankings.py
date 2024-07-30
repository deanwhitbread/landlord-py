import unittest
from tests import helpers
from game.core.hand import CardHand

class CardCategoryRankingsTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        self.hand.reset()
    
    @classmethod
    def setUpClass(cls):
        cls.hand = CardHand()
        cls.hlpr = helpers.TestHelpers()

    @classmethod
    def tearDownClass(cls):
        del cls.hand
        del cls.hlpr

    def test_bomb_beat_solo_hands(self):
        '''Test that the bomb card hand beats both solo hand and 
        solo chain hand.'''
        bomb_hand = [[2,2,2,2]]
        bomb_hand = self.hlpr.convert_hand_numbers_to_card_objects(bomb_hand)
        self.hand.get_hand_score(bomb_hand.pop())
        bomb_score = self.hand.hand_score

        solo_hand = self.hlpr.convert_hand_numbers_to_card_objects([[15]])
        self.hand.get_hand_score(solo_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

        solo_hand = self.hlpr.convert_hand_numbers_to_card_objects([[3,4,5,6,7,8,9,10,11,12,13,1]])
        self.hand.get_hand_score(solo_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

    def test_bomb_beat_pair_hands(self):
        '''Test that the bomb card hand beats both pair hand and 
        pair chain hand.'''
        bomb_hand = [[2,2,2,2]]
        bomb_hand = self.hlpr.convert_hand_numbers_to_card_objects(bomb_hand)
        self.hand.get_hand_score(bomb_hand.pop())
        bomb_score = self.hand.hand_score

        pair_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2]])
        self.hand.get_hand_score(pair_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

        pair_hand = self.hlpr.convert_hand_numbers_to_card_objects([[5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,1,1]])
        self.hand.get_hand_score(pair_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

    def test_bomb_beat_trio_hands(self):
        '''Test that the bomb card hand beats trio hand, trio 
        chain hand, and trio with solo hand.'''
        bomb_hand = [[2,2,2,2]]
        bomb_hand = self.hlpr.convert_hand_numbers_to_card_objects(bomb_hand)
        self.hand.get_hand_score(bomb_hand.pop())
        bomb_score = self.hand.hand_score

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2,2]])
        self.hand.get_hand_score(trio_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[9,9,9,10,10,10,11,11,11,12,12,12,13,13,13,1,1,1]])
        self.hand.get_hand_score(trio_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2,2,15]])
        self.hand.get_hand_score(trio_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2,2,1,1]])
        self.hand.get_hand_score(trio_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

    def test_bomb_beat_airplane_hands(self):
        '''Test that the bomb card hand beats both airplane with solo 
        hand and airplane with pair hand.'''
        bomb_hand = [[2,2,2,2]]
        bomb_hand = self.hlpr.convert_hand_numbers_to_card_objects(bomb_hand)
        self.hand.get_hand_score(bomb_hand[0])
        bomb_score = self.hand.hand_score

        airplane_hand = self.hlpr.convert_hand_numbers_to_card_objects([[10,10,10,11,11,11,12,12,12,13,13,13,1,1,1,5,6,7,8,9]])
        self.hand.get_hand_score(airplane_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

        airplane_hand = self.hlpr.convert_hand_numbers_to_card_objects([[11,11,11,12,12,12,13,13,13,1,1,1,6,6,7,7,8,8,9,9]])
        self.hand.get_hand_score(airplane_hand.pop())
        self.assertTrue(bomb_score > self.hand.hand_score)

    def test_rocket_beat_solo_hands(self):
        '''Test that the rocket card hand beats both solo hand and 
        solo chain hand.'''
        rocket_hand = self.hlpr.convert_hand_numbers_to_card_objects([[14,15]])
        self.hand.get_hand_score(rocket_hand.pop())
        rocket_score = self.hand.hand_score

        solo_hand = self.hlpr.convert_hand_numbers_to_card_objects([[15]])
        self.hand.get_hand_score(solo_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

        solo_hand = self.hlpr.convert_hand_numbers_to_card_objects([[3,4,5,6,7,8,9,10,11,12,13,1]])
        self.hand.get_hand_score(solo_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

    def test_rocket_beat_pair_hands(self):
        '''Test that the rocket card hand beats both pair hand and 
        pair chain hand.'''
        rocket_hand = self.hlpr.convert_hand_numbers_to_card_objects([[14,15]])
        self.hand.get_hand_score(rocket_hand.pop())
        rocket_score = self.hand.hand_score

        pair_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2]])
        self.hand.get_hand_score(pair_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

        pair_hand = self.hlpr.convert_hand_numbers_to_card_objects([[5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,1,1]])
        self.hand.get_hand_score(pair_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

    def test_rocket_beat_trio_hands(self):
        '''Test that the rocket card hand beats trio hand, trio 
        chain hand, and trio with solo hand.'''
        rocket_hand = self.hlpr.convert_hand_numbers_to_card_objects([[14,15]])
        self.hand.get_hand_score(rocket_hand.pop())
        rocket_score = self.hand.hand_score

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2,2]])
        self.hand.get_hand_score(trio_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[9,9,9,10,10,10,11,11,11,12,12,12,13,13,13,1,1,1]])
        self.hand.get_hand_score(trio_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2,2,15]])
        self.hand.get_hand_score(trio_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

        trio_hand = self.hlpr.convert_hand_numbers_to_card_objects([[2,2,2,1,1]])
        self.hand.get_hand_score(trio_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

    def test_rocket_beat_airplane_hands(self):
        '''Test that the rocket card hand beats airplane hand, airplance
        with solo hand, and airplane with pair hand.'''
        rocket_hand = self.hlpr.convert_hand_numbers_to_card_objects([[14,15]])
        self.hand.get_hand_score(rocket_hand.pop())
        rocket_score = self.hand.hand_score

        airplane_hand = self.hlpr.convert_hand_numbers_to_card_objects([[10,10,10,11,11,11,12,12,12,13,13,13,1,1,1,5,6,7,8,9]])
        self.hand.get_hand_score(airplane_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)

        airplane_hand = self.hlpr.convert_hand_numbers_to_card_objects([[11,11,11,12,12,12,13,13,13,1,1,1,6,6,7,7,8,8,9,9]])
        self.hand.get_hand_score(airplane_hand.pop())
        self.assertTrue(rocket_score > self.hand.hand_score)