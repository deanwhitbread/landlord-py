import unittest
from game_player import Player
from tests import helpers 
from card_deck import CardDeck

class PlayerClassTestCase(unittest.TestCase):
    def setUp(self):
        self.deck.shuffle()

    def tearDown(self):
        self.player.reset()
        self.player.set_stake_amount(60)
        self.deck.reset()
    
    @classmethod
    def setUpClass(cls):
        cls.player = Player()
        cls.hlpr = helpers.TestHelpers()
        cls.deck = CardDeck()

    @classmethod
    def tearDownClass(cls):
        del cls.player 
        del cls.hlpr
        del cls.deck
    
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
        cards1, cards2, cards3, wildcards = self.deck.deal()
        self.player.set_cards(cards1)
        self.assertEqual(len(self.player.cards), 17)
        self.assertFalse(self.player.cards==None)

    def test_set_cards_function_replaces_current_cards(self):
        cards1, cards2, cards3, wildcards = self.deck.deal()
        self.player.set_cards(cards1)
        self.assertTrue(self.player.cards==cards1)
        new_cards = [3,3,3,3,4,4,4,4,5,5,5,5,10,10,10,14,15]
        self.player.set_cards(new_cards)
        self.assertTrue(self.player.cards==new_cards)
        self.assertFalse(self.player.cards==cards1)

    def test_get_random_bid_amount_function_returns_bid_or_skips(self):
        SKIP_BID = 0
        for _ in range(100):
            bid = self.player.get_random_bid_amount()
            self.assertTrue(bid==3 or bid==2 or bid==1 or bid==SKIP_BID)

    def test_get_random_bid_amount_function_returns_bid_that_does_not_exceed_players_stake(self):
        self.player.set_stake_amount(1)
        self.assertEqual(self.player.get_stake_amount(), 1)
        while True:
            bid = self.player.get_random_bid_amount()
            if bid>0:
                break
        self.assertEqual(bid, 1)
        self.assertEqual(self.player.get_bid_amount(), bid)
        self.assertEqual(self.player.get_stake_amount(), 0)

    def test_add_wildcards_function_adds_cards_to_the_players_cards(self):
        cards1, cards2, cards3, wildcards = self.deck.deal()
        self.player.set_cards(cards1)
        self.assertEqual(len(self.player.cards), 17)
        self.player.add_wildcards(wildcards)
        self.assertEqual(len(self.player.cards), 20)

    def test_bid_matches_stake_when_bid_exceeds_stake_amount_when_stake_is_low(self):
        self.player.set_stake_amount(2)
        self.assertEqual(self.player.get_stake_amount(), 2)
        self.player.set_bid(3)
        self.assertEqual(self.player.get_bid_amount(), 2)
        self.assertEqual(self.player.get_stake_amount(), 0)
        