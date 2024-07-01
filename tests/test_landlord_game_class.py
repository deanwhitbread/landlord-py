import unittest
from game_engine import LandlordGame
from game_player import Player
from card_deck import CardDeck

class LandlordGameTestCase(unittest.TestCase):
    def setUp(self):
        self.deck.shuffle()
        p1_cards, p2_cards, p3_cards, self.wildcards = self.deck.deal()
        self.player1.set_cards(p1_cards)
        self.player2.set_cards(p2_cards)
        self.player3.set_cards(p3_cards)

    def tearDown(self):
        self.game.reset()
        self.deck.reset()
        del self.wildcards
    
    @classmethod
    def setUpClass(cls):
        cls.player1 = Player()
        cls.player2 = Player()
        cls.player3 = Player()

        players = [cls.player1, cls.player2, cls.player3]
        cls.game = LandlordGame(players)
        cls.deck = CardDeck()

    @classmethod
    def tearDownClass(cls):
        del cls.game
        del cls.player1
        del cls.player2
        del cls.player3
        del cls.deck

    def test_winning_bidding_player_becomes_landlord(self):
        self.assertIsNone(self.game.get_landlord())
        self.assertTrue(self.game._execute_bidding())
        self.assertIsNotNone(self.game.get_landlord())
        self.assertNotIn(self.game.get_landlord(), self.game.get_peasants())

    def test_losing_bidding_players_becomes_peasants(self):
        self.assertIsNone(self.game.get_peasants())
        self.assertTrue(self.game._execute_bidding())
        self.assertIsNotNone(self.game.get_peasants())
        self.assertEqual(len(self.game.get_peasants()), 2)
        self.assertNotIn(self.game.get_landlord(), self.game.get_peasants())
    
    def test_round_restarts_if_all_players_pass_on_bidding(self):
        player1, player2, player3 = self.game.get_players()[0], self.game.get_players()[1], self.game.get_players()[2] 
        player1.set_bid(0)
        player2.set_bid(0)
        player3.set_bid(0)
        self.assertFalse(self.game._execute_bidding())

    def test_winning_bid_amount_is_in_the_round_pot(self):
        self.assertEqual(self.game.get_round_stake(), 0)
        self.assertTrue(self.game._execute_bidding())
        self.assertNotEqual(self.game.get_round_stake(), 0)
    
    def test_round_pot_resets_after_round_ends(self):
        self.assertEqual(self.game.get_round_stake(), 0)
        self.assertTrue(self.game.play())
        self.assertEqual(self.game.get_round_stake(), 0)

    def test_game_ends_when_one_players_stake_reaches_zero(self):
        player1 = self.game.get_players()[0]        
        player1.set_stake_amount(0)
        self.assertEqual(player1.get_stake_amount(), 0)
        self.assertFalse(self.game.play())
        player1.set_stake_amount(60)
        self.assertEqual(player1.get_stake_amount(), 60)
