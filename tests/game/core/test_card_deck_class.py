import unittest
from game.core.deck import CardDeck

class CardDeckTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        self.deck.reset()
    
    @classmethod
    def setUpClass(cls):
        cls.deck = CardDeck()

    @classmethod
    def tearDownClass(cls):
        del cls.deck

    def test_get_card_deck_function(self):
        deck = self.deck.get_card_deck()
        self.assertEqual(len(deck), 54)

    def test_valid_add_card_to_deck_function(self):
        deck = self.deck.get_card_deck()
        self.assertEqual(len(deck), 54)
        self.deck.add_card_to_deck(10, "spades")
        self.assertEqual(len(deck), 55)
        self.deck.add_card_to_deck(7, "hearts")
        self.assertEqual(len(deck), 56)
        self.deck.add_card_to_deck(13, "clubs")
        self.assertEqual(len(deck), 57)

    def test_invalid_add_card_to_deck_function(self):
        deck = self.deck.get_card_deck()
        self.assertEqual(len(deck), 54)
        self.deck.add_card_to_deck(97, "spades")
        self.assertEqual(len(deck), 54)
        self.deck.add_card_to_deck(-10, "spades")
        self.assertEqual(len(deck), 54)

    def test_reset_function(self):
        deck = self.deck.get_card_deck()
        self.assertEqual(len(deck), 54)
        self.deck.add_card_to_deck(10, "spades")
        self.assertEqual(len(deck), 55)
        self.deck.reset()

        deck = self.deck.get_card_deck()
        self.assertEqual(len(deck), 54)

    def test_shuffle_function(self):
        deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7]
        deck += [8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12]
        deck += [13,13,13,13,14,15]
        card_deck = [card.get_number() for card in self.deck.get_card_deck()]
        self.assertTrue(deck==card_deck)
        self.deck.shuffle()
        card_deck = [card.get_number() for card in self.deck.get_card_deck()]
        self.assertFalse(deck==card_deck)

    def test_deal_function(self):
        self.deck.shuffle()
        player1, player2, player3, wildcards = self.deck.deal()
        self.assertEqual(len(player1), 17) 
        self.assertEqual(len(player2), 17) 
        self.assertEqual(len(player3), 17) 
        self.assertEqual(len(wildcards), 3) 

    def test_cannot_deal_cards_more_than_once(self):
        self.deck.shuffle()
        player1, player2, player3, wildcards = self.deck.deal()
        self.assertEqual(len(player1), 17) 
        self.assertEqual(len(player2), 17) 
        self.assertEqual(len(player3), 17) 
        self.assertEqual(len(wildcards), 3) 
        player1, player2, player3, wildcards = self.deck.deal()
        self.assertEqual(len(player1), 0) 
        self.assertEqual(len(player2), 0) 
        self.assertEqual(len(player3), 0) 
        self.assertEqual(len(wildcards), 0)

    def test_can_deal_cards_after_deck_reset(self):
        self.deck.shuffle()
        player1, player2, player3, wildcards = self.deck.deal()
        self.assertEqual(len(player1), 17) 
        self.assertEqual(len(player2), 17) 
        self.assertEqual(len(player3), 17) 
        self.assertEqual(len(wildcards), 3) 
        self.deck.reset()
        self.deck.shuffle()
        player1, player2, player3, wildcards = self.deck.deal()
        self.assertEqual(len(player1), 17) 
        self.assertEqual(len(player2), 17) 
        self.assertEqual(len(player3), 17) 
        self.assertEqual(len(wildcards), 3) 
        