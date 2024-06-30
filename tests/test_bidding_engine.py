import unittest
from game_engine import BiddingEngine
from game_player import Player

class BiddingEngineTestCase(unittest.TestCase):
    def setUp(self):
        self.players = [self.player1, self.player2, self.player3]
        self.engine.set_players(self.players)

    def tearDown(self):
        for player in self.players:
            player.reset()

        self.engine.reset()
    
    @classmethod
    def setUpClass(cls):
        cls.player1 = Player()
        cls.player2 = Player()
        cls.player3 = Player()
        cls.engine = BiddingEngine()

    @classmethod
    def tearDownClass(cls):
        del cls.engine
        del cls.player1
        del cls.player2
        del cls.player3

    def test_execute_bidding_round_function_returns_max_bid_and_winner_bidder(self):
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertTrue(max_bid>=0 and max_bid<=3)
        self.assertTrue(type(winner), Player)
    
    def test_execute_bidding_round_function_returns_matches_the_max_bid_with_the_winner_bidder(self):
        max_bid, winner = self.engine.execute_bidding_round()
        for player in self.players:
            if player==winner:
                self.assertEqual(player.get_bid_amount(), max_bid)
    
    def test_bidders_must_raise_bid_when_bidding_for_wildcards(self):
        self.player1.set_bid(3)
        self.player2.set_bid(3)
        self.player3.set_bid(3)
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertEqual(winner, self.player1)
        self.assertEqual(max_bid, 3)

        self.player1.set_bid(2)
        self.player2.set_bid(3)
        self.player3.set_bid(2)
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertEqual(winner, self.player2)
        self.assertEqual(max_bid, 3)

        self.player1.set_bid(3)
        self.player2.set_bid(1)
        self.player3.set_bid(3)
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertEqual(winner, self.player1)
        self.assertEqual(max_bid, 3)

        self.player1.set_bid(1)
        self.player2.set_bid(2)
        self.player3.set_bid(0)
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertEqual(winner, self.player2)
        self.assertEqual(max_bid, 2)

        self.player1.set_bid(0)
        self.player2.set_bid(1)
        self.player3.set_bid(1)
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertEqual(winner, self.player2)
        self.assertEqual(max_bid, 1)

        self.player1.set_bid(0)
        self.player2.set_bid(0)
        self.player3.set_bid(2)
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertEqual(winner, self.player3)
        self.assertEqual(max_bid, 2)
