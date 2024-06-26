import unittest
from game_player import Player

class PlayerClassTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        self.player.reset()
    
    @classmethod
    def setUpClass(cls):
        cls.player = Player()

    @classmethod
    def tearDownClass(cls):
        del cls.player 
    
    def test_can_submit_valid_bid(self):
        self.assertTrue(self.player.bid(0)) 
        self.assertTrue(self.player.bid(1)) 
        self.assertTrue(self.player.bid(2))
        self.assertTrue(self.player.bid(3))
    
    def test_cannot_submit_invalid_bid(self):
        self.assertFalse(self.player.bid(4))
        self.assertFalse(self.player.bid(10))
        self.assertFalse(self.player.bid(20))
    
    def test_stake_decreases_when_valid_bid_submitted(self):
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.bid(0)
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.bid(1)
        self.assertEqual(self.player.get_stake_amount(), 59)
        self.player.bid(2)
        self.assertEqual(self.player.get_stake_amount(), 57)
        self.player.bid(3)
        self.assertEqual(self.player.get_stake_amount(), 54)
    
    def test_stake_is_unchanged_when_invalid_bid_submitted(self):
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.bid(4)
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.bid(10)
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.bid(20)
        self.assertEqual(self.player.get_stake_amount(), 60)

    def test_cannot_bid_when_stake_is_empty(self):
        for _ in range(20):
            self.player.bid(3)

        self.assertEqual(self.player.get_stake_amount(), 0)
        self.assertTrue(self.player.bid(0))
        self.assertFalse(self.player.bid(1))
        self.assertFalse(self.player.bid(2))
        self.assertFalse(self.player.bid(3))
    