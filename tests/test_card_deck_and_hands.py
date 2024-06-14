import unittest
from card_deck import CardDeck, Card
from card_hand import CardHand 

class CardDeckTestCase(unittest.TestCase):
    def setUp(self):
        self.card_numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
        self.suits = {"hearts", "diamonds", "clubs", "spades", "joker"}
        self.number_points_dict = {3:1, 4:2, 5:3, 6:5, 7:8, 8:13, 9:21, 
            10:34, 11:55, 12:89, 13:144, 1:233, 2:377, 14:610, 15:987}

    def tearDown(self):
        del self.card_numbers
        del self.suits 
        self.__class__.hand.reset()
    
    @classmethod
    def setUpClass(cls):
        cls.deck = CardDeck()
        cls.hand = CardHand()

    @classmethod
    def tearDownClass(cls):
        del cls.deck
        del cls.hand

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

        for card in self.__class__.deck._card_stack:
            points = card.get_points()
            number = card.get_number()
            self.assertEqual(points, self.number_points_dict[number])

    def test_point_ranking_on_card_number_value(self):
        '''Test that the order of points for card numbers following the 
        order: 3,4,5,6,7,8,9,10,J,Q,K,A,2,Black Joker,Red Joker.
        '''
        self.assertEqual(len(self.__class__.deck._card_stack), 54)

        
        for card in self.__class__.deck._card_stack:
            key = card.get_number()
            points = card.get_points()
            self.assertEqual(points, self.number_points_dict[key])

    '''
        Card Hands
    '''
    def test_solo_card_hand(self):
        '''Test all valid solo card hands.'''
        hands = [[1],[2],[3],[4],[5],[6],[7],[8],[9],
            [10],[11],[12],[13],[14],[15]]
        
        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_valid_solo_chain_card_hand(self):
        '''Test all valid solo chain card hands.'''
        hands = [[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9], 
            [6,7,8,9,10],[7,8,9,10,11],[8,9,10,11,12],
            [9,10,11,12,13],[10,11,12,13,1]]

        hands = self._convert_hand_numbers_to_card_objects(hands)
        
        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_can_solo_chain_at_least_five_cards(self):
        '''Test that solo chain is at least 5 consecutive cards.'''
        hands = [[7,8,9,10,11],[3,4,5,6,7,8],[5,6,7,8,9,10], 
            [7,8,9,10,11,12,13,1],[3,4,5,6,7,8,9,10,11,12,13,1]]

        hands = self._convert_hand_numbers_to_card_objects(hands)
        
        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_invalid_solo_chain_card_hand(self):
        '''Test all invalid solo chain card hands.'''
        hands = [[3,4,5,6],[5,6,7,8],[9,10,11,12],[11,12,13,1,2], 
            [12,13,1,2,14],[13,1,2,14,15],[1,2,3,4,5],[2,3,4,5,6], 
            [3,4,6,7,8],[7,8,10,12,1]]

        hands = self._convert_hand_numbers_to_card_objects(hands)
        
        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertFalse(self.__class__.hand.play())

    def test_valid_pair_card_hand(self):
        '''Test all valid pair card hands.'''
        hands = [[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],
            [11,11],[12,12],[13,13],[1,1],[2,2]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())
    
    def test_invalid_pair_card_hand(self):
        '''Test all invalid pair card hands.'''
        hands = [[4,1],[1,4],[10,5],[3,4],[8,7]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertFalse(self.__class__.hand.play())
    
    def test_valid_pair_chain_hand(self):
        '''Test all valid pair chain card hands.'''
        hands = [[3,3,4,4,5,5],[4,4,5,5,6,6],[5,5,6,6,7,7],[6,6,7,7,8,8],
            [7,7,8,8,9,9],[8,8,9,9,10,10],[9,9,10,10,11],[10,10,11,11,12,12],
            [11,11,12,13,13],[12,12,13,13,1,1]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_can_pair_chain_at_least_three_pairs(self):
        '''Test that the pair chain is at least three consecutive pairs.'''
        hands = [[6,6,7,7,8,8],[4,4,5,5,6,6,7,7,8,8,9,9],[10,10,11,11,12,12,13,13],
            [5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,1,1]]

        hands = self._convert_hand_numbers_to_card_objects(hands)
        
        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_invalid_pair_chain_hand(self):
        '''Test all invalid pair chain hands.'''
        hands = [[5,5,7,7],[8,8,9,9,10,10],[1,1,2,2,14,14],[2,2,14,14,15,15],
            [6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,1,1,2,2],[2,2,3,3]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertFalse(self.__class__.hand.play())

    def test_valid_trio_card_hand(self):
        '''Test all valid trio card hands.'''
        hands = [[3,3,3],[4,4,4],[5,5,5],[6,6,6],[7,7,7],[8,8,8],[9,9,9],
            [10,10,10],[11,11,11],[12,12,12],[13,13,13],[1,1,1],[2,2,2]]

        hands = self._convert_hand_numbers_to_card_objects(hands)
        
        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_invalid_trio_card_hand(self):
        '''Test all invalid trio card hands.'''
        hands= [[3,4,5],[6,6,9],[10,10,1]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertFalse(self.__class__.hand.play())

    def test_trio_and_solo_card_hand(self):
        '''Test all valid trio with solo card hands.'''
        hands = [[3,3,3,6],[7,7,7,3],[6,6,6,1],[1,1,1,4],[2,2,2,3],
            [2,2,2,14], [2,2,2,15],[11,11,11,1]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_trio_and_pair_card_hand(self):
        '''Test all valid trio with pair card hands.'''
        hands = [[3,3,3,4,4],[7,7,7,10,10],[1,1,1,3,3],[2,2,2,7,7]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_valid_trio_and_pair_chain_card_hand(self):
        '''Test all valid trio with pair chain card hands.'''
        hands = [[3,3,3,4,4,4,5,5,6,6],[7,7,7,8,8,8,9,9,9,1,1,3,3,4,4],
            [11,11,11,12,12,12,13,13,13,1,1,1,5,5,4,4,3,3,9,9], [1,1,1,6,6]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_invalid_trio_and_pair_chain_card_hand(self):
        '''Test all invalid trio with pair chain card hands.'''
        hands = [[2,2,2,14,15],[3,3,3,4,4,4,8,8],[6,6,6,7,7,7,3,3,10,11],
            [1,1,1,2,2,2,5,5,8,8]]
        
        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertFalse(self.__class__.hand.play())

    def test_valid_airplane_card_hand(self):
        '''Test all valid airplane chain hands.'''
        hands = [[3,3,3,4,4,4],[4,4,4,5,5,5],[6,6,6,7,7,7],[8,8,8,9,9,9],
            [10,10,10,11,11,11],[11,11,11,12,12,12],[13,13,13,1,1,1]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_invalid_airplane_card_hand(self):
        '''Test all invalid airplane chain hands.'''
        hands = [[2,2,2,3,3,3], [1,1,1,2,2,2]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertFalse(self.__class__.hand.play())

    def test_valid_trio_solo_and_airplane_card_hand(self):
        '''Test all valid trio with solo and airplane card hands.'''
        hands = [[3,3,3,4,4,4,7,11], [10,10,10,11,11,11,3,4], 
            [10,10,10,11,11,11,12,12,12,13,13,13,1,1,1,3,15,6,7,2]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_invalid_trio_solo_and_airplane_card_hand(self):
        '''Test all invalid trio with solo and airplane card hands.'''
        hands = [[2,2,2,3,3,3,4,4,4,8,4,6],[1,1,1,2,2,2,5,6],
            [4,4,4,5,5,5,7,7,8,8]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertFalse(self.__class__.hand.play())

    def test_bomb_card_hand(self):
        '''Test all valid bomb card hands.'''
        hands = [[3,3,3,3], [5,5,5,5], [2,2,2,2], [7,7,7,7]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_valid_bomb_with_dual_solo_card_hand(self):
        '''Test all valid bomb with solo card hands.'''
        hands = [[12,12,12,12,5,4],[9,9,9,9,14,6]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_invalid_bomb_with_dual_solo_card_hand(self):
        '''Test all invalid bomb with solo card hands.'''
        hands = [[10,10,10,10,2], [5,5,5,5,14,15]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertFalse(self.__class__.hand.play())

    def test_valid_bomb_dual_pair_card_hand(self):
        '''Test all valid bomb with dual pair card hands.'''
        hands = [[5,5,5,5,13,13,1,1], [7,7,7,7,12,12,8,8]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertTrue(self.__class__.hand.play())

    def test_invalid_bomb_dual_pair_card_hand(self):
        '''Test all invalid bomb with dual pair card hands.'''
        hands = [[5,5,5,5,6,6,6,6], [12,12,12,12,3,3,3,3],
            [3,3,3,3,13,13,13,13]]

        hands = self._convert_hand_numbers_to_card_objects(hands)

        for hand in hands:
            self.__class__.hand.select(hand)
            self.assertFalse(self.__class__.hand.play())

    def test_rocket_card_hand(self):
        '''Test rocked card hand.'''
        hand = [15,14]
        for i in range(len(hand)):
            hand[i] = self._create_card_object_for_card_number(hand[i])

        self.__class__.hand.select(hand)
        self.assertTrue(self.__class__.hand.play())

    def _create_card_object_for_card_number(self, number, suit="joker"):
        '''Create a Card object using the card number provided.
        
        Args: 
            number - An integer representing the card number.
            suit - A string representing the card suit. Default is joker.

        Returns: A Card object. 
        '''
        return Card(number=number, 
            suit=suit, 
            points=self.number_points_dict[number])

    def _convert_hand_numbers_to_card_objects(self, hands, suit="hearts"):
        '''Helper function to convert the numbers in the hand to card objects.
        
        Args:
            hands - A 2-dimensional list containing a list of integers. 
            suit - The suit of all the cards. Default is hearts. 
        
        Returns: A 2-dimensional list containing a list of Card objects.
        '''
        for i in range(len(hands)):
            for j in range(len(hands[i])):
                hands[i][j] = self._create_card_object_for_card_number(hands[i][j], suit)
        
        return hands

    '''
        Card Hand Ranking
    '''
    def test_ranking_for_valid_hands(self):
        '''Test the point ranking for all valid card hands.'''
        self.fail("Test not implemented.")