import unittest
from game_player import Player
from tests import helpers 

class PlayerClassTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        self.player.reset()
        self.player.set_stake_amount(60)
    
    @classmethod
    def setUpClass(cls):
        cls.player = Player()
        cls.hlpr = helpers.TestHelpers()

    @classmethod
    def tearDownClass(cls):
        del cls.player 
        del cls.hlpr
    
    def test_can_submit_valid_bid(self):
        self.assertTrue(self.player.set_bid(0)) 
        self.assertTrue(self.player.set_bid(1)) 
        self.assertTrue(self.player.set_bid(2))
        self.assertTrue(self.player.set_bid(3))
    
    def test_cannot_submit_invalid_bid(self):
        self.assertFalse(self.player.set_bid(4))
        self.assertFalse(self.player.set_bid(10))
        self.assertFalse(self.player.set_bid(20))
    
    def test_stake_decreases_when_valid_bid_submitted(self):
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.set_bid(0)
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.set_bid(1)
        self.assertEqual(self.player.get_stake_amount(), 59)
        self.player.set_bid(2)
        self.assertEqual(self.player.get_stake_amount(), 57)
        self.player.set_bid(3)
        self.assertEqual(self.player.get_stake_amount(), 54)
    
    def test_stake_is_unchanged_when_invalid_bid_submitted(self):
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.set_bid(4)
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.set_bid(10)
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.set_bid(20)
        self.assertEqual(self.player.get_stake_amount(), 60)

    def test_cannot_bid_when_stake_is_empty(self):
        for _ in range(20):
            self.player.set_bid(3)

        self.assertEqual(self.player.get_stake_amount(), 0)
        self.assertTrue(self.player.set_bid(0))
        self.assertFalse(self.player.set_bid(1))
        self.assertFalse(self.player.set_bid(2))
        self.assertFalse(self.player.set_bid(3))
    
    def test_set_stake_amount_sets_the_players_total_stake(self):
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.set_stake_amount(0)
        self.assertEqual(self.player.get_stake_amount(), 0)
        self.player.set_stake_amount(35)
        self.assertEqual(self.player.get_stake_amount(), 35)

    def test_set_cards_function_gives_the_player_cards(self):
        self.assertTrue(self.player.cards==None)
        cards = [1,2,3,4,5,6,7,8,9,10,10,10,11,12,13,14,15]
        self.player.set_cards(cards)
        self.assertEqual(len(self.player.cards), 17)
        self.assertFalse(self.player.cards==None)

    def test_set_cards_function_replaces_current_cards(self):
        cards = [1,2,3,4,5,6,7,8,9,10,10,10,11,12,13,14,15]
        self.player.set_cards(cards)
        self.assertTrue(self.player.cards==cards)
        new_cards = [3,3,3,3,4,4,4,4,5,5,5,5,10,10,10,14,15]
        self.player.set_cards(new_cards)
        self.assertTrue(self.player.cards==new_cards)
        self.assertFalse(self.player.cards==cards)

    def test_get_random_bid_amount_function_returns_bid_or_skips(self):
        SKIP_BID = 0
        for _ in range(100):
            bid = self.player.get_random_bid_amount()
            self.assertTrue(bid==3 or bid==2 or bid==1 or bid==SKIP_BID)

    def test_get_random_bid_amount_function_returns_bid_that_does_not_exceed_players_stake(self):
        for _ in range(19):
            self.player.set_bid(3)

        self.assertEqual(self.player.get_stake_amount(), 3)
        bid = self.player.get_random_bid_amount()
        self.assertTrue(self.player.get_stake_amount()>=bid)
        
        self.player.set_bid(1)
        self.assertEqual(self.player.get_stake_amount(), 2)
        bid = self.player.get_random_bid_amount()
        self.assertTrue(self.player.get_stake_amount()>=bid)

        self.player.set_bid(1)
        self.assertEqual(self.player.get_stake_amount(), 1)
        bid = self.player.get_random_bid_amount()
        self.assertTrue(self.player.get_stake_amount()>=bid)

        self.player.set_bid(1)
        self.assertEqual(self.player.get_stake_amount(), 0)
        bid = self.player.get_random_bid_amount()
        self.assertTrue(self.player.get_stake_amount()>=bid)
         
        