import unittest
from tests import helpers 
from game.core.deck import CardDeck
from game.core.player import Player

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
    
    def test_stake_does_not_decrease_when_valid_bid_submitted(self):
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.set_bid(0)
        self.assertTrue(self.player.has_passed_bidding())
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.set_bid(1)
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.set_bid(2)
        self.assertEqual(self.player.get_stake_amount(), 60)
        self.player.set_bid(3)
        self.assertEqual(self.player.get_stake_amount(), 60)
    
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
        self.assertEqual(self.player.get_stake_amount(), 1)

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
        self.assertEqual(self.player.get_stake_amount(), 2)

    def test_player_can_randomly_play_a_valid_hand(self):
        c1, c2, c3, wildcards = self.deck.deal()
        self.player.set_cards(c1)
        self.assertEqual(len(self.player.get_hand()), 0)
        self.player.set_random_hand()
        self.assertNotEqual(len(self.player.get_hand()), 0)

    def test_play_hand_function_returns_the_hand_being_played(self):
        cards = [[3,3,6,8,11,13,2,2], [3,4,5,5,5,9,13,14,15]]
        cards = self.hlpr.convert_hand_numbers_to_card_objects(cards)
        hands = [[3,3], [5,5,5,9]] 
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for i in range(len(cards)):
            self.player.set_cards(cards[i])
            self.player.set_hand(hands[i])
            self.assertEqual(self.player.play_hand(), hands[i])

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

    def test_set_random_hand_function_returns_hand_in_the_same_category_as_previous_hand(self):
        opponent_hands = [[3,3,4,4,5,5], [5,6,7,8,9], [11,11,11,8], [6]] 
        opponent_hands = self.hlpr.convert_hand_numbers_to_card_objects(opponent_hands)
        player_cards = [[3,3,7,7,8,8,9,9,12,13,2], [3,3,3,4,9,10,11,12,13,13,1,15], [3,5,5,6,6,7,7,13,13,13], [3,3,3,4,4,11,2]]
        player_cards = self.hlpr.convert_hand_numbers_to_card_objects(player_cards)
        for i in range(len(opponent_hands)):
            op_hand = opponent_hands[i]
            op_hand_category = self.player.hand.get_hand_category(op_hand)
            self.player.set_cards(player_cards[i])
            self.player.set_random_hand(op_hand)
            player_hand = self.player.get_hand()
            player_hand_category = self.player.hand.get_hand_category(player_hand)
            self.assertEqual(op_hand_category, player_hand_category)
    
    def test_set_random_hand_function_passes_when_player_does_not_have_stronger_hand(self):
        opponent_hands = [[10,10,10], [5,5,6,6,7,7],[2,2]] 
        opponent_hands = self.hlpr.convert_hand_numbers_to_card_objects(opponent_hands)
        player_cards = [[3,5,5,5,8,11,12,1,1,1,14], [3,4,4,4,4,11,12,2,2], [5,5,5,6,6,12,1,14,15]]
        player_cards = self.hlpr.convert_hand_numbers_to_card_objects(player_cards)
        for i in range(len(opponent_hands)):
            op_hand = opponent_hands[i]
            self.player.set_cards(player_cards[i])
            player_hand = self.player.set_random_hand(op_hand)
            self.assertIsNone(player_hand)

    def test_remove_cards_function_removes_cards_from_players_deck(self):
        cards = [[3,4,5,6,7,8,10,10,10,2,14,15]]
        cards = self.hlpr.convert_hand_numbers_to_card_objects(cards).pop()
        self.player.set_cards(cards)
        self.assertEqual(len(self.player.get_cards()), 12)

        hand = self.player.get_cards()[:6]
        self.player.remove_cards(hand)
        self.assertEqual(len(self.player.get_cards()), 6)
        
        hand = self.player.get_cards()[:4]
        self.player.remove_cards(hand)
        self.assertEqual(len(self.player.get_cards()), 2)

        hand = self.player.get_cards()[:2]
        self.player.remove_cards(hand)
        self.assertEqual(len(self.player.get_cards()), 0)
    
        