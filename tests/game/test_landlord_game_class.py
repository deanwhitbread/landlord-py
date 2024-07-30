import unittest
from game_player import Player
from tests import helpers
from game.engine.gameplay import GameplayEngine
from game.landlord import LandlordGame
from game.core.deck import CardDeck

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
        self.gameplay.reset()
        for player in self.game.get_players():
            player.set_stake_amount(60)
    
    @classmethod
    def setUpClass(cls):
        cls.player1 = Player()
        cls.player2 = Player()
        cls.player3 = Player()

        players = [cls.player1, cls.player2, cls.player3]
        cls.game = LandlordGame(players)
        cls.deck = CardDeck()
        cls.hlpr = helpers.TestHelpers()
        cls.gameplay = GameplayEngine()

    @classmethod
    def tearDownClass(cls):
        del cls.game
        del cls.player1
        del cls.player2
        del cls.player3
        del cls.deck
        del cls.hlpr
        del cls.gameplay

    def test_winning_bidding_player_becomes_landlord(self):
        self.assertIsNone(self.game.get_landlord())
        self.assertTrue(self.game._execute_bidding())
        self.assertIsNotNone(self.game.get_landlord())
        self.assertNotIn(self.game.get_landlord(), self.game.get_peasants())

    def test_losing_bidding_players_becomes_peasants(self):
        self.player1.set_bid(3)
        self.player2.set_bid(2)
        self.player3.set_bid(1)
        self.assertIsNone(self.game.get_peasants())
        self.assertTrue(self.game._execute_bidding())
        self.assertIsNotNone(self.game.get_peasants())
        self.assertEqual(len(self.game.get_peasants()), 2)
        self.assertNotIn(self.game.get_landlord(), self.game.get_peasants())
    
    def test_round_restarts_if_all_players_pass_on_bidding(self):
        self.player1.set_bid(0)
        self.player2.set_bid(0)
        self.player3.set_bid(0)
        self.assertTrue(self.game.all_players_passed_during_bidding())
        self.assertFalse(self.game.has_game_ended())

    def test_winning_bid_amount_is_in_the_round_pot(self):
        self.assertEqual(self.game.get_round_stake(), 0)
        self.assertTrue(self.game._execute_bidding())
        self.assertNotEqual(self.game.get_round_stake(), 0)
    
    def test_round_pot_resets_after_round_ends(self):
        self.assertEqual(self.game.get_round_stake(), 0)
        self.player1.set_bid(1)
        self.player2.set_bid(0)
        self.player3.set_bid(0)
        self.assertTrue(self.game.play())
        self.assertEqual(self.game.get_round_stake(), 0)

    def test_game_ends_when_one_players_stake_reaches_zero(self):
        self.player1.set_stake_amount(0)
        self.assertEqual(self.player1.get_stake_amount(), 0)
        self.assertTrue(self.game.has_game_ended())
        self.player1.set_stake_amount(60)
        self.assertEqual(self.player1.get_stake_amount(), 60)

    def test_landlord_receives_the_wildcards_after_bidding_ends(self):
        self.player1.set_bid(3)
        self.player2.set_bid(2)
        self.player3.set_bid(2)
        self.assertTrue(self.game._execute_bidding())
        self.assertEqual(self.game.get_landlord(), self.player1)
        self.assertTrue(len(self.game.get_landlord().get_cards()), 17)
        self.game.give_landlord_wildcards(self.wildcards)
        self.assertTrue(len(self.game.get_landlord().get_cards()), 20)
        for player in self.game.get_peasants():
            self.assertTrue(len(player.get_cards()), 17)

    def test_has_game_ended_returns_false_when_players_have_stake_remaining(self):
        self.assertFalse(self.game.has_game_ended())

    def test_landlord_receives_round_stake_when_they_win_and_peasants_pay(self):
        p1, p2, p3 = self.game.get_players()
        p1_stake, p2_stake, p3_stake = p1.get_stake_amount(), p2.get_stake_amount(), p3.get_stake_amount()

        landlord_cards = [[5,2]]
        peasants_cards = [[3,4,4,6,6,6,9,10], [3,3,7,7,7,9,11]]
        landlord_cards = self.hlpr.convert_hand_numbers_to_card_objects(landlord_cards)
        peasants_cards = self.hlpr.convert_hand_numbers_to_card_objects(peasants_cards)
        p1.set_cards(landlord_cards[0]), p2.set_cards(peasants_cards[0]), p3.set_cards(peasants_cards[1])        
        p1.set_bid(3), p2.set_bid(2), p3.set_bid(1) 
        self.game._execute_bidding()
        self.assertTrue(self.game.get_landlord()==p1)

        order = self.gameplay.get_play_order(self.game.get_landlord(), self.game.get_peasants())
        winner, total_stake = self.gameplay.play_round(order, self.game.get_round_stake())
        self.game.update_players_stake(winner, total_stake)

        self.assertTrue(p1.get_stake_amount()>=p1_stake + (self.game.get_round_stake()*2))
        self.assertTrue(p2.get_stake_amount()<=p2_stake - self.game.get_round_stake())
        self.assertTrue(p3.get_stake_amount()<=p3_stake - self.game.get_round_stake())
    
    def test_peasants_recieve_round_stake_when_they_win_and_landlord_pays(self):
        p1, p2, p3 = self.game.get_players()
        p1_stake, p2_stake, p3_stake = p1.get_stake_amount(), p2.get_stake_amount(), p3.get_stake_amount()

        landlord_cards = [[3,4,8,11]]
        peasants_cards = [[14], [3,3,7,7,7,9,11,13]]
        landlord_cards = self.hlpr.convert_hand_numbers_to_card_objects(landlord_cards)
        peasants_cards = self.hlpr.convert_hand_numbers_to_card_objects(peasants_cards)
        p1.set_cards(landlord_cards[0]), p2.set_cards(peasants_cards[0]), p3.set_cards(peasants_cards[1])        
        p1.set_bid(3), p2.set_bid(2), p3.set_bid(1) 
        self.game._execute_bidding()
        self.assertTrue(self.game.get_landlord()==p1)

        order = self.gameplay.get_play_order(self.game.get_landlord(), self.game.get_peasants())
        winner, total_stake = self.gameplay.play_round(order, self.game.get_round_stake())
        self.game.update_players_stake(winner, total_stake)

        self.assertTrue(p1.get_stake_amount()<=p1_stake - (self.game.get_round_stake()*2))
        self.assertTrue(p2.get_stake_amount()>=p2_stake + self.game.get_round_stake())
        self.assertTrue(p3.get_stake_amount()>=p3_stake + self.game.get_round_stake())