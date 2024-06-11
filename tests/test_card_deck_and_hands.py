import unittest
from card_deck import CardDeck

class CardDeckTestCase(unittest.TestCase):
    def setUp(self):
        self.card_numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
        self.suits = {"hearts", "diamonds", "clubs", "spades", "joker"}

    def tearDown(self):
        del self.card_numbers
        del self.suits 
    
    @classmethod
    def setUpClass(cls):
        cls.deck = CardDeck()

    @classmethod
    def tearDownClass(cls):
        del cls.deck

    '''
        Card Representation 
    '''
    def test_card_has_number_value(self):
        '''Test that the playing card has a number value.'''
        self.assertEqual(len(self.__class__.deck._card_stack), 54)
        for card in self.__class__.deck._card_stack:
            self.assertIn(card.get_number(), self.card_numbers)

    def test_card_has_suit(self):
        '''Test that the playing card has a single suit.'''
        self.assertEqual(len(self.__class__.deck._card_stack), 54)
        for card in self.__class__.deck._card_stack:
            self.assertIn(card.get_suit(), self.suits) 

    def test_deck_has_no_duplicate_cards(self):
        '''Test the entire deck for duplicate card value and suit.'''
        self.assertEqual(len(self.__class__.deck._card_stack), 54)

        hearts = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        diamonds = hearts.copy()
        clubs = hearts.copy()
        spades = hearts.copy()
        jokers = [14, 15]
        for card in self.__class__.deck._card_stack:
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
        self.assertEqual(len(self.__class__.deck._card_stack), 54)
        for card in self.__class__.deck._card_stack:
            self.assertTrue(card.get_points()>0)

    def test_card_ranking_follows_fibonacci_sequence(self):
        '''Test point ranking system uses fibonacci sequence.'''
        self.assertEqual(len(self.__class__.deck._card_stack), 54)

        number_points_dict = {3:1, 4:2, 5:3, 6:5, 7:8, 8:13, 9:21, 
            10:34, 11:55, 12:89, 13:144, 1:233, 2:377, 14:610, 15:987}
        for card in self.__class__.deck._card_stack:
            points = card.get_points()
            number = card.get_number()
            self.assertEqual(points, number_points_dict[number])

    def test_point_ranking_on_card_number_value(self):
        '''Test that the order of points for card numbers following the 
        order: 3,4,5,6,7,8,9,10,J,Q,K,A,2,Black Joker,Red Joker.
        '''
        self.assertEqual(len(self.__class__.deck._card_stack), 54)

        number_points_dict = {3:1, 4:2, 5:3, 6:5, 7:8, 8:13, 9:21, 
            10:34, 11:55, 12:89, 13:144, 1:233, 2:377, 14:610, 15:987}
        for card in self.__class__.deck._card_stack:
            key = card.get_number()
            points = card.get_points()
            self.assertEqual(points, number_points_dict[key])

    '''
        Card Hands
    '''
    def test_solo_card_hand(self):
        '''Test all valid solo card hands.'''
        self.fail("Test not implemented.")

    def test_valid_solo_chain_card_hand(self):
        '''Test all valid solo chain card hands.'''
        self.fail("Test not implemented.")

    def test_invalid_solo_chain_card_hand(self):
        '''Test all invalid solo chain card hands.'''
        self.fail("Test not implemented.")

    def test_valid_pair_card_hand(self):
        '''Test all valid pair card hands.'''
        self.fail("Test not implemented.")
    
    def test_invalid_pair_card_hand(self):
        '''Test all invalid pair card hands.'''
        self.fail("Test not implemented.")
    
    def test_valid_pair_chain_hand(self):
        '''Test all valid pair chain card hands.'''
        self.fail("Test not implemented.")

    def test_invalid_pair_chain_hand(self):
        '''Test all invalid pair chain hands.'''
        self.fail("Test not implemented.")

    def test_valid_trio_card_hand(self):
        '''Test all valid trio card hands.'''
        self.fail("Test not implemented.")

    def test_invalid_trio_card_hand(self):
        '''Test all invalid trio card hands.'''
        self.fail("Test not implemented.")

    def test_trio_and_solo_card_hand(self):
        '''Test all valid trio with solo card hands.'''
        self.fail("Test not implemented.")

    def test_trio_and_pair_card_hand(self):
        '''Test all valid trio with pair card hands.'''
        self.fail("Test not implemented.")

    def test_valid_trio_and_pair_chain_card_hand(self):
        '''Test all valid trio with pair chain card hands.'''
        self.fail("Test not implemented.")

    def test_invalid_trio_and_pair_chain_card_hand(self):
        '''Test all invalid trio with pair chain card hands.'''
        self.fail("Test not implemented.")

    def test_airplane_card_hand(self):
        '''Test all valid airplane chain hands.'''
        self.fail("Test not implemented.")

    def test_trio_solo_and_airplane_card_hand(self):
        '''Test all valid trio with solo and airplane card hands.'''
        self.fail("Test not implemented.")

    def test_bomb_card_hand(self):
        '''Test all valid bomb card hands.'''
        self.fail("Test not implemented.")

    def test_bomb_with_dual_solo_card_hand(self):
        '''Test all valid bomb with solo card hands.'''
        self.fail("Test not implemented.")

    def test_valid_bomb_dual_pair_card_hand(self):
        '''Test all valid bomb with dual pair card hands.'''
        self.fail("Test not implemented.")

    def test_invalid_bomb_dual_pair_card_hand(self):
        '''Test all invalid bomb with dual pair card hands.'''
        self.fail("Test not implemented.")

    def test_pair_chain_is_not_a_bomb_card_hand(self):
        '''Test that the pair chain card hand is not a bomb card hand.'''
        self.fail("Test not implemented.")

    def test_rocket_card_hand(self):
        '''Test rocked card hand.'''
        self.fail("Test not implemented.")

    def test_bomb_with_rocket_hands_card_hands(self):
        '''Test that bomb and rocket card hands cannot be played together.'''
        self.fail("Test not implemented.")

    '''
        Card Hand Ranking
    '''
    def test_ranking_for_valid_hands(self):
        '''Test the point ranking for all valid card hands.'''
        self.fail("Test not implemented.")