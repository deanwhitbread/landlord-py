import unittest
from game.engine.bidding import BiddingEngine
from game_player import Player
from card_deck import CardDeck

class BiddingEngineTestCase(unittest.TestCase):
    def setUp(self):
        self.players = [self.player1, self.player2, self.player3]
        self.engine.set_players(self.players)
        self.deck.shuffle()
        c1, c2, c3, self.wildcards = self.deck.deal()
        self.player1.set_cards(c1)
        self.player2.set_cards(c2)
        self.player3.set_cards(c3)

    def tearDown(self):
        for player in self.players:
            player.reset()

        self.engine.reset()
        self.deck.reset()
        del self.wildcards
    
    @classmethod
    def setUpClass(cls):
        cls.player1 = Player()
        cls.player2 = Player()
        cls.player3 = Player()
        cls.engine = BiddingEngine()
        cls.deck = CardDeck()

    @classmethod
    def tearDownClass(cls):
        del cls.engine
        del cls.player1
        del cls.player2
        del cls.player3
        del cls.deck

    def test_execute_bidding_round_function_returns_max_bid_and_winner_bidder(self):
        self.player1.set_bid(3)
        self.player2.set_bid(2)
        self.player3.set_bid(1)
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertTrue(max_bid>=0 and max_bid<=3)
        self.assertTrue(type(winner), Player)
        self.assertIn(winner, self.engine.get_players())
    
    def test_execute_bidding_round_function_returns_matches_the_max_bid_with_the_winner_bidder(self):
        max_bid, winner = self.engine.execute_bidding_round()
        for player in self.engine.get_players():
            if player==winner:
                self.assertEqual(player.get_bid_amount(), max_bid)
    
    def test_bidders_must_raise_bid_when_bidding_for_wildcards(self):
        player1, player2, player3 = self.engine._get_bidding_order()
        player1.set_bid(3)
        player2.set_bid(3)
        player3.set_bid(3)
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertEqual(winner, player1)
        self.assertEqual(max_bid, 3)

        player1.set_bid(2)
        player2.set_bid(3)
        player3.set_bid(2)
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertEqual(winner, player2)
        self.assertEqual(max_bid, 3)

        player1.set_bid(3)
        player2.set_bid(1)
        player3.set_bid(3)
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertEqual(winner, player1)
        self.assertEqual(max_bid, 3)

        player1.set_bid(1)
        player2.set_bid(2)
        player3.set_bid(0)
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertEqual(winner, player2)
        self.assertEqual(max_bid, 2)

        player1.set_bid(0)
        player2.set_bid(1)
        player3.set_bid(1)
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertEqual(winner, player2)
        self.assertEqual(max_bid, 1)

        player1.set_bid(0)
        player2.set_bid(0)
        player3.set_bid(2)
        max_bid, winner = self.engine.execute_bidding_round()
        self.assertEqual(winner, player3)
        self.assertEqual(max_bid, 2)

    def test_first_bidder_is_the_player_with_the_three_of_hearts(self):
        first_bidder = None 
        for player in self.engine.get_players():
            for card in player.get_cards():
                if card.get_number()==3 and card.get_suit()=="hearts":
                    first_bidder = player
                    break 

        if not first_bidder:
            for i in range(len(self.wildcards)):
                card = self.wildcards[i]
                if card.get_number()==3 and card.get_suit()=="hearts":
                    self.player1.get_cards()[0], self.wildcards[i] = self.wildcards[i], self.player1.get_cards()[0]
                    first_bidder = self.player1
        
        order = self.engine._get_bidding_order()
        self.assertEqual(first_bidder, order[0])