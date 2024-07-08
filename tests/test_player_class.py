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
        self.assertTrue(self.player.has_passed_bidding())
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
        self.player.set_stake_amount(0)
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
        self.assertIsNone(self.player.get_cards())
        cards1, cards2, cards3, wildcards = self.deck.deal()
        self.player.set_cards(cards1)
        self.assertEqual(len(self.player.get_cards()), 17)
        self.assertIsNotNone(self.player.get_cards())

    def test_set_cards_function_replaces_current_cards(self):
        cards1, cards2, cards3, wildcards = self.deck.deal()
        self.player.set_cards(cards1)
        self.assertEqual(self.player.get_cards(), cards1)
        self.player.set_cards(cards2)
        self.assertEqual(self.player.get_cards(), cards2)
        self.assertNotEqual(self.player.get_cards(), cards1)

    def test_get_random_bid_amount_function_returns_bid_or_skips(self):
        SKIP_BID = 0
        for _ in range(100):
            bid = self.player.get_random_bid_amount()
            self.assertTrue(bid==3 or bid==2 or bid==1 or bid==SKIP_BID)

    def test_get_random_bid_amount_function_returns_bid_that_does_not_exceed_players_stake(self):
        self.player.set_stake_amount(1)
        self.assertEqual(self.player.get_stake_amount(), 1)
        bid = self.player.get_random_bid_amount()
        while bid==0:
            bid = self.player.get_random_bid_amount()
        self.assertEqual(bid, 1)
        self.assertEqual(self.player.get_bid_amount(), bid)
        self.assertEqual(self.player.get_stake_amount(), 0)

    def test_add_wildcards_function_adds_cards_to_the_players_cards(self):
        cards1, cards2, cards3, wildcards = self.deck.deal()
        self.player.set_cards(cards1)
        self.assertEqual(len(self.player.get_cards()), 17)
        self.player.add_wildcards(wildcards)
        self.assertEqual(len(self.player.get_cards()), 20)

    def test_bid_matches_stake_when_bid_exceeds_stake_amount_when_stake_is_low(self):
        self.player.set_stake_amount(2)
        self.assertEqual(self.player.get_stake_amount(), 2)
        self.player.set_bid(3)
        self.assertEqual(self.player.get_bid_amount(), 2)
        self.assertEqual(self.player.get_stake_amount(), 0)

    def test_player_can_randomly_play_a_valid_hand(self):
        c1, c2, c3, wildcards = self.deck.deal()
        self.player.set_cards(c1)
        self.assertEqual(len(self.player.get_hand()), 0)
        self.player.set_random_hand()
        self.assertNotEqual(len(self.player.get_hand()), 0)

    def test_play_hand_function_returns_the_hand_being_played(self):
        hands = [[3,3], [5,5,5,9]] 
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.player.set_hand(hand)
            self.assertEqual(self.player.play_hand(), hand)

    def test_play_hand_function_choses_random_hand_when_no_hand_set(self):
        c1, c2, c3, wildcards = self.deck.deal()
        self.player.set_cards(c1)
        self.assertEqual(len(self.player.get_hand()), 0)
        self.player.set_random_hand()
        self.player.play_hand()
        self.assertNotEqual(len(self.player.get_hand()), 0)
    
    def test_player_cannot_play_an_invalid_hand(self):
        hands = [[1,2,3,4,5,6,7], [13,13,13,1,1,1,2,2,2], [4,4,4,4,14,15], 
            [5,5,5,13,14]] 
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.player.set_hand(hand)
            self.assertEqual(len(self.player.get_hand()), len(hand))
            self.assertFalse(self.player.play_hand())
            self.assertEqual(len(self.player.get_hand()), 0)

    def test_get_hand_returns_the_players_choosen_hand(self):
        hand = [11,11,12,12,13,13]
        self.player.set_hand(hand) 
        self.assertTrue(self.player.get_hand(), hand)

    def test_get_hand_is_empty_when_player_has_not_chosen_hand(self):
        self.assertEqual(len(self.player.get_hand()), 0)
        