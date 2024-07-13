
import unittest
from game_engine import GameplayEngine, LandlordGame
from game_player import Player 
from tests import helpers 

class GameplayEngineTestCase(unittest.TestCase):
    def setUp(self):
        wildcards = self.game.deal_cards_to_players()
        p1, p2, p3 = self.game.get_players()
        p1.set_bid(3)
        self.game._execute_bidding()
        self.game.give_landlord_wildcards(wildcards)

    def tearDown(self):
        self.gameplay.reset()
        self.game.reset()
    
    @classmethod
    def setUpClass(cls):
        cls.gameplay = GameplayEngine()
        cls.landlord = Player()
        cls.peasant1, cls.peasant2 = Player(), Player()
        cls.game = LandlordGame([cls.landlord, cls.peasant1, cls.peasant2])
        cls.hlpr = helpers.TestHelpers()

    @classmethod
    def tearDownClass(cls):
        del cls.gameplay
        del cls.game, cls.landlord, cls.peasant1, cls.peasant2
        del cls.hlpr

    def test_landlord_player_begins_the_round(self):
        self.assertTrue(self.game._execute_bidding())
        landlord, peasants = self.game.get_landlord(), self.game.get_peasants()
        order = self.gameplay.get_play_order(landlord, peasants)
        self.assertEqual(len(order), 3)
        self.assertEqual(order[-1], self.game.get_landlord())

    def test_play_round_function_ends_with_a_winner(self):
        order = self.gameplay.get_play_order(self.game.get_landlord(), self.game.get_peasants())
        winning_player, stake = self.gameplay.play_round(order, self.game.get_landlord().get_bid_amount())
        self.assertIn(winning_player, order)
        self.assertTrue(stake>=self.game.get_landlord().get_bid_amount())
    