import unittest
from game.core.player import Player
from landlord import LandlordGame

class LandlordGameTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        self.game.reset()
    
    @classmethod
    def setUpClass(cls):
        cls.player1 = Player()
        cls.player2 = Player()
        cls.player3 = Player()

        players = [cls.player1, cls.player2, cls.player3]
        cls.game = LandlordGame(players)

    @classmethod
    def tearDownClass(cls):
        del cls.game
        del cls.player1
        del cls.player2
        del cls.player3

    def test_round_pot_resets_after_round_ends(self):
        self.assertEqual(self.game.get_round_stake(), 0)
        self.player1.set_bid(1), self.player2.set_bid(0), self.player3.set_bid(0)
        self.assertTrue(self.game.play())
        self.assertEqual(self.game.get_round_stake(), 0)
    