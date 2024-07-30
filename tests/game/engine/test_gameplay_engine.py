
import unittest
from tests import helpers 
from game.engine.gameplay import GameplayEngine
from game.landlord import LandlordGame
from game.core.player import Player

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
    
    def test_landlord_is_winner_when_is_first_player_to_have_no_cards(self):
        landlord_cards = [[5,14,15]]
        peasants_cards = [[3,4,4,6,6,6,9,10], [3,3,7,7,7,9,11]]
        landlord_cards = self.hlpr.convert_hand_numbers_to_card_objects(landlord_cards)
        peasants_cards = self.hlpr.convert_hand_numbers_to_card_objects(peasants_cards)
        p1, p2, p3 = self.game.get_players()
        p1.set_bid(3), p2.set_bid(1), p3.set_bid(2)
        p1.set_cards(landlord_cards[0]), p2.set_cards(peasants_cards[0]), p3.set_cards(peasants_cards[1])
        self.game._execute_bidding()
        order = self.gameplay.get_play_order(self.game.get_landlord(), self.game.get_peasants())
        winner, total_stake = self.gameplay.play_round(order, self.game.get_round_stake())
        self.assertEqual(winner, self.game.get_landlord())

    def test_peasants_win_if_one_peasant_has_no_cards(self):
        landlord_cards = [[3,3,4,4,7,8,9]]
        peasants_cards = [[1,1], [3,3,7,7,7,9,11,13]]
        landlord_cards = self.hlpr.convert_hand_numbers_to_card_objects(landlord_cards)
        peasants_cards = self.hlpr.convert_hand_numbers_to_card_objects(peasants_cards)
        p1, p2, p3 = self.game.get_players()
        p1.set_bid(3), p2.set_bid(1), p3.set_bid(2)
        p1.set_cards(landlord_cards[0]), p2.set_cards(peasants_cards[0]), p3.set_cards(peasants_cards[1])
        self.game._execute_bidding()
        order = self.gameplay.get_play_order(self.game.get_landlord(), self.game.get_peasants())
        winner, total_stake = self.gameplay.play_round(order, self.game.get_round_stake())
        self.assertIn(winner, self.game.get_peasants())
    
    def test_double_stake_function_returns_true_when_hand_is_a_bomb_hand(self):
        hand = [[3,3,3,3]]
        hand = self.hlpr.convert_hand_numbers_to_card_objects(hand)
        p1, p2, p3 = self.game.get_players()
        p1.set_hand(hand.pop())
        self.assertTrue(self.gameplay.double_round_stake(p1, p3))

    def test_double_stake_function_returns_true_when_hand_is_a_rocket_hand(self):
        hand = [[14,15]]
        hand = self.hlpr.convert_hand_numbers_to_card_objects(hand)
        p1, p2, p3 = self.game.get_players()
        p1.set_hand(hand.pop())
        self.assertTrue(self.gameplay.double_round_stake(p1, p3))

    def test_double_stake_function_returns_true_when_both_players_have_passed(self):
        hand = [[5,5,5,13]]
        hand = self.hlpr.convert_hand_numbers_to_card_objects(hand)
        p1, p2, p3 = self.game.get_players()
        p1.set_hand(hand.pop())
        self.assertTrue(self.gameplay.double_round_stake(p1, p1))

    def test_double_stake_function_returns_false_for_any_other_hand(self):
        hand = [[14,15]]
        hand = self.hlpr.convert_hand_numbers_to_card_objects(hand)
        p1, p2, p3 = self.game.get_players()
        p1.set_hand(hand.pop())
        self.assertTrue(self.gameplay.double_round_stake(p1, p3))

    def test_bomb_doubles_the_round_stake_when_played(self):
        landlord_cards = [[2,2,2,2]]
        peasants_cards = [[3,4,4,6,6,6,9,10], [3,3,7,7,7,9,11]]
        landlord_cards = self.hlpr.convert_hand_numbers_to_card_objects(landlord_cards)
        peasants_cards = self.hlpr.convert_hand_numbers_to_card_objects(peasants_cards)
        p1, p2, p3 = self.game.get_players()
        p1.set_bid(3), p2.set_bid(1), p3.set_bid(2)
        p1.set_cards(landlord_cards[0]), p2.set_cards(peasants_cards[0]), p3.set_cards(peasants_cards[1])
        self.game._execute_bidding()
        order = self.gameplay.get_play_order(self.game.get_landlord(), self.game.get_peasants())
        self.assertEqual(self.game.get_round_stake(), 3)
        winner, total_stake = self.gameplay.play_round(order, self.game.get_round_stake())
        self.assertEqual(total_stake, 3*2)

    def test_rocket_doubles_the_round_stake_when_played(self):
        landlord_cards = [[14,15]]
        peasants_cards = [[3,4,4,6,6,6,9,10], [3,3,7,7,7,9,11]]
        landlord_cards = self.hlpr.convert_hand_numbers_to_card_objects(landlord_cards)
        peasants_cards = self.hlpr.convert_hand_numbers_to_card_objects(peasants_cards)
        p1, p2, p3 = self.game.get_players()
        p1.set_bid(3), p2.set_bid(1), p3.set_bid(2)
        p1.set_cards(landlord_cards[0]), p2.set_cards(peasants_cards[0]), p3.set_cards(peasants_cards[1])
        self.game._execute_bidding()
        order = self.gameplay.get_play_order(self.game.get_landlord(), self.game.get_peasants())
        self.assertEqual(self.game.get_round_stake(), 3)
        winner, total_stake = self.gameplay.play_round(order, self.game.get_round_stake())
        self.assertEqual(total_stake, 3*2)

    def test_stake_doubles_when_both_players_pass(self):
        landlord_cards = [[13,2]]
        peasants_cards = [[3,4,4,6,6,6,9,10], [3,3,7,7,7,9,11]]
        landlord_cards = self.hlpr.convert_hand_numbers_to_card_objects(landlord_cards)
        peasants_cards = self.hlpr.convert_hand_numbers_to_card_objects(peasants_cards)
        p1, p2, p3 = self.game.get_players()
        p1.set_bid(3), p2.set_bid(1), p3.set_bid(2)
        p1.set_cards(landlord_cards[0]), p2.set_cards(peasants_cards[0]), p3.set_cards(peasants_cards[1])
        self.game._execute_bidding()
        order = self.gameplay.get_play_order(self.game.get_landlord(), self.game.get_peasants())
        self.assertEqual(self.game.get_round_stake(), 3)
        winner, total_stake = self.gameplay.play_round(order, self.game.get_round_stake())
        self.assertEqual(total_stake, 3*2)
