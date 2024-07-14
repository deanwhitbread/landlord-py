import unittest
from card_deck import CardDeck, Card
from card_hand import CardHand 
from tests import helpers
from misc import constants as const

class CardDeckTestCase(unittest.TestCase):
    def setUp(self):
        self.solo_hand = [[3],[11],[2],[14],[15],[5]]

    def tearDown(self):
        self.__class__.hand.reset()
        self.__class__.deck.reset()
        del self.solo_hand
    
    @classmethod
    def setUpClass(cls):
        cls.deck = CardDeck()
        cls.hand = CardHand()
        cls.hlpr = helpers.TestHelpers()

    @classmethod
    def tearDownClass(cls):
        del cls.deck
        del cls.hand
        del cls.hlpr

    '''
        Tests for Card class
    '''
    def test_card_has_number_value(self):
        '''Test that the playing card has a number value.'''
        self.assertEqual(len(self.__class__.deck._deck), 54)
        for card in self.__class__.deck.get_card_deck():
            self.assertIn(card.get_number(), self.hlpr.card_numbers)

    def test_card_has_suit(self):
        '''Test that the playing card has a single suit.'''
        self.assertEqual(len(self.__class__.deck.get_card_deck()), 54)
        for card in self.__class__.deck.get_card_deck():
            self.assertIn(card.get_suit(), self.hlpr.suits) 

    def test_deck_has_no_duplicate_cards(self):
        '''Test the entire deck for duplicate card value and suit.'''
        self.assertEqual(len(self.__class__.deck.get_card_deck()), 54)

        hearts = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        diamonds = hearts.copy()
        clubs = hearts.copy()
        spades = hearts.copy()
        jokers = [14, 15]
        for card in self.__class__.deck.get_card_deck():
            suit = card.get_suit()
            number = card.get_number()

            if suit == "hearts":
                hearts[number-1] = True
            elif suit == "diamonds":
                diamonds[number-1] = True
            elif suit == "clubs":
                clubs[number-1] = True
            elif suit == "spades":
                spades[number-1] = True
            elif suit == "joker":
                jokers[number-14] = True
            else:
                self.fail("Unrecognised suit.")
        
        self.assertTrue(all(hearts) and all(diamonds) and all(clubs) and 
            all(spades) and all(jokers))
    
    def test_card_has_points(self):
        '''Test playing card has a point value assoicated to it.'''
        self.assertEqual(len(self.__class__.deck.get_card_deck()), 54)
        for card in self.__class__.deck.get_card_deck():
            self.assertTrue(card.get_points()>0)

    def test_card_ranking_follows_fibonacci_sequence(self):
        '''Test point ranking system uses fibonacci sequence.'''
        self.assertEqual(len(self.__class__.deck.get_card_deck()), 54)
        for card in self.__class__.deck.get_card_deck():
            points = card.get_points()
            number = card.get_number()
            self.assertEqual(points, card._get_card_points_value(number))

    def test_point_ranking_on_card_number_value(self):
        '''Test that the order of points for card numbers following the 
        order: 3,4,5,6,7,8,9,10,J,Q,K,A,2,Black Joker,Red Joker.
        '''
        self.assertEqual(len(self.__class__.deck.get_card_deck()), 54)
        for card in self.__class__.deck.get_card_deck():
            key = card.get_number()
            points = card.get_points()
            self.assertEqual(points, card._get_card_points_value(key))

    def test_card_string_representation(self):
        '''Test the string representation of the card.'''
        card = Card(3, "hearts")
        self.assertEqual(str(card), str(3))

        card = Card(7, "clubs")
        self.assertEqual(str(card), str(7))

        card = Card(1, "hearts")
        self.assertEqual(str(card), const.ACE_REPR)

        card = Card(11, "spades")
        self.assertEqual(str(card), const.JACK_REPR)

        card = Card(12, "clubs")
        self.assertEqual(str(card), const.QUEEN_REPR)

        card = Card(13, "diamonds")
        self.assertEqual(str(card), const.KING_REPR)

        card = Card(14, "joker")
        self.assertEqual(str(card), const.BLACK_JOKER_REPR)

        card = Card(15, "joker")
        self.assertEqual(str(card), const.RED_JOKER_REPR)
    
    '''
        Tests for CardDeck class.
    '''
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
        