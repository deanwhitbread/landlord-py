import unittest
from tests import helpers
import misc.constants as const
from game.core.card import Card
from game.core.deck import CardDeck
from game.core.hand import CardHand

class CardHandTestCase(unittest.TestCase):
    def setUp(self):
        self.solo_hand = [[3],[11],[2],[14],[15],[5]]

    def tearDown(self):
        self.hand.reset()
        self.deck.reset()
    
    @classmethod
    def setUpClass(cls):
        cls.hand = CardHand()
        cls.hlpr = helpers.TestHelpers()
        cls.deck = CardDeck()

    @classmethod
    def tearDownClass(cls):
        del cls.hand
        del cls.hlpr
        del cls.deck

    def test_set_hand_method_adds_any_set_of_cards_to_the_hand(self):
        '''Test the set hand method adds any set of choosen cards to the player's hand.'''
        hands = self.hlpr.get_valid_pair_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.set_hand(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_invalid_pair_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.set_hand(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_valid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.set_hand(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_invalid_trio_chain_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.set_hand(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_valid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.set_hand(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

        hands = self.hlpr.get_invalid_combination_with_pair_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)
            self.hand.set_hand(hand)
            self.assertNotEqual(len(self.hand.current_hand), 0)

    def test_set_hand_method_sets_hand_to_same_category_as_previous_hand_played(self):
        previous_hand = [[3,4,5,6,7]]
        previous_hand = self.hlpr.convert_hand_numbers_to_card_objects(previous_hand)
        previous_hand_category = self.hand.get_hand_category(previous_hand[0])
        solo_hands = [[4,5,6,7,8]]
        solo_hands = self.hlpr.convert_hand_numbers_to_card_objects(solo_hands)
        self.hand.set_hand(self.hand.get_hand(), previous_hand[0], solo_hands)
        self.assertTrue(self.hand.get_hand_category(self.hand.get_hand())==previous_hand_category)

    def test_cannot_play_empty_hand(self):
        '''Test play method disallows playing an empty hand.'''
        self.assertFalse(self.__class__.hand.is_valid())

    def test_is_valid_method(self):
        '''Test method allows a valid hand to be played.'''
        hands = self.hlpr.get_valid_trio_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.set_hand(hand)
            self.assertTrue(self.hand.is_valid())
        
        hands = self.hlpr.get_valid_bomb_card_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.set_hand(hand)
            self.assertTrue(self.hand.is_valid())

        hands = self.hlpr.get_valid_combination_with_solo_hand()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.set_hand(hand)
            self.assertTrue(self.hand.is_valid())
    
    def test_reset_method_clears_current_hand(self):
        '''Test reset method clears the player's current hand.'''
        hands = self.hlpr.get_valid_solo_card_chain_hands()
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            self.hand.set_hand(hand)
            self.assertTrue(len(self.hand.current_hand)>=5)
            self.__class__.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)

        solo_hand = self.hlpr.convert_hand_numbers_to_card_objects(self.solo_hand)
        for hand in solo_hand:
            self.hand.set_hand(hand)
            self.assertEqual(len(self.hand.current_hand), 1)
            self.__class__.hand.reset()
            self.assertEqual(len(self.hand.current_hand), 0)

    def test_set_random_hand_function_chooses_a_valid_hand_from_cards(self):
        self.deck.shuffle()
        c1, c2, c3, wildcards = self.deck.deal()
        self.hand.set_random_hand(c1)
        self.assertIsNotNone(self.hand.get_hand())
        self.assertTrue(self.hand.is_valid()) 
        self.hand.reset()

        self.hand.set_random_hand(c1+wildcards)
        self.assertIsNotNone(self.hand.get_hand())
        self.assertTrue(self.hand.is_valid()) 
        self.hand.reset()

        self.hand.set_random_hand(c2[:5])
        self.assertIsNotNone(self.hand.get_hand())
        self.assertTrue(self.hand.is_valid()) 
        self.hand.reset()

        self.hand.set_random_hand(c3[4:14])
        self.assertIsNotNone(self.hand.get_hand())
        self.assertTrue(self.hand.is_valid()) 
        self.hand.reset()

        self.hand.set_random_hand([Card(3, "hearts")])
        self.assertIsNotNone(self.hand.get_hand())
        self.assertTrue(self.hand.is_valid()) 
        self.hand.reset()

        self.hand.set_random_hand(wildcards)
        self.assertIsNotNone(self.hand.get_hand())
        self.assertTrue(self.hand.is_valid()) 
        self.hand.reset()

    def test_set_random_hand_raises_type_error_when_non_card_object_parameter_passed(self):
        with self.assertRaises(TypeError):
            card = Card(3, "hearts")
            self.hand.set_random_hand(card)

        with self.assertRaises(TypeError):
            self.hand.set_random_hand([3,3,3,4,4,4,5,5,5,6,6,6,10,10,2,2,15])

        with self.assertRaises(TypeError):
            self.hand.set_random_hand()

    def test_set_random_hand_raises_value_error_when_empty_list_is_passed(self):
        with self.assertRaises(ValueError):
            self.hand.set_random_hand(list())
    
    def test_get_card_category_function_returns_category(self):
        hands = [[11],[3,4,5,6,7,8],[8,8],[11,11,12,12,13,13],[2,2,2],[4,4,4,5,5,5,6,6,6], 
            [5,5,5,12],[10,10,10,1,1],[3,3,3,4,4,4,5,5,5,7,9,11],[12,12,12,13,13,13,1,1,10,10],
            [7,7,7,7],[14,15]]
        category = [[const.CARD_CATEGORY.SOLO],[const.CARD_CATEGORY.SOLO_CHAIN],
            [const.CARD_CATEGORY.PAIR],[const.CARD_CATEGORY.PAIR_CHAIN],
            [const.CARD_CATEGORY.TRIO],[const.CARD_CATEGORY.TRIO_CHAIN],
            [const.CARD_CATEGORY.TRIO_WITH_SOLO],[const.CARD_CATEGORY.TRIO_WITH_PAIR],
            [const.CARD_CATEGORY.AIRPLANE_WITH_SOLO],
            [const.CARD_CATEGORY.AIRPLANE_WITH_PAIR],
            [const.CARD_CATEGORY.BOMB],[const.CARD_CATEGORY.ROCKET]]

        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for i in range(len(hands)):
            hand = hands[i]
            self.assertEqual(self.hand.get_hand_category(hand), category[i].pop())

    def test_set_random_hand_function_with_category_set_returns_stronger_hand_in_the_same_category(self):
        opponent_hands = [[3,3,4,4,5,5], [5,6,7,8,9], [11,11,11,3,3], [6]] 
        opponent_hands = self.hlpr.convert_hand_numbers_to_card_objects(opponent_hands)
        player_cards = [[3,3,7,7,8,8,9,9,12,13,2], [3,3,3,4,9,10,11,12,13,13,1,15], [3,5,5,6,6,7,7,13,13,13], [3,3,3,4,4,11,2]]
        player_cards = self.hlpr.convert_hand_numbers_to_card_objects(player_cards)
        for i in range(len(opponent_hands)):
            op_hand = opponent_hands[i]
            op_hand_category = self.hand.get_hand_category(op_hand)
            self.hand.get_hand_score(op_hand)
            op_hand_score = self.hand.hand_score
            player_hand = self.hand.set_random_hand(player_cards[i], op_hand)
            player_hand_category = self.hand.get_hand_category(player_hand)
            self.assertEqual(player_hand_category, op_hand_category) 
            self.hand.get_hand_score(player_hand)
            player_hand_score = self.hand.hand_score
            self.assertTrue(player_hand_score>op_hand_score)
            self.hand.reset()

    def test_set_random_hand_function_returns_none_when_category_set_but_no_hands_in_that_category(self):
        opponent_hands = [[3,3,4,4,5,5], [5,6,7,8,9], [11,11,11,8], [6]] 
        opponent_hands = self.hlpr.convert_hand_numbers_to_card_objects(opponent_hands)
        player_cards = [[4,4,5,5,8,8,1,15], [3,4,5,6,7,8,9,13,2,2], [3,3,3,5,10,10,1,2], [3,3,4,4,5,5]]
        player_cards = self.hlpr.convert_hand_numbers_to_card_objects(player_cards)
        for i in range(len(opponent_hands)):
            player_hand = self.hand.set_random_hand(player_cards[i], opponent_hands[i])
            self.assertEqual(len(player_hand), 0) 
            self.hand.reset()

    def test_valid_get_rocket_hand_method(self):
        solo_hand = [Card(12, 'hearts'), Card(13, 'hearts'), 
                    Card(1, 'hearts'), Card(14, 'joker'), Card(15, 'joker')]
        self.hand.set_hand(self.hand._get_rocket_hand(solo_hand))
        hand = set([card.get_number() for card in self.hand.get_hand()])
        self.assertIn(14, hand)
        self.assertIn(15, hand)
        self.assertEqual(len(hand), 2)

    def test_invalid_get_rocket_hand_method(self):
        solo_hand = [Card(12, 'hearts'), Card(13, 'hearts'), Card(1, 'hearts')]
        self.hand.set_hand(self.hand._get_rocket_hand(solo_hand))
        self.assertEqual(len(self.hand.get_hand()), 0)

    def test_get_similar_cards_method_returns_array_containing_same_cards(self):
        player_cards = [[3,4,5,5,7,8,11], [7,7,7,8,8,8,10,13], [5,7,1,1,2,2,2]]
        player_cards = self.hlpr.convert_hand_numbers_to_card_objects(player_cards)
        for cards in player_cards:
            card_freq_map = self.hlpr.get_number_frequency_map(cards)
            for num, freq in card_freq_map.items():
                similar_cards = self.hand._get_similar_cards(cards, num, freq)
                self.assertTrue(all([card.get_number()==num for card in similar_cards]))
                self.assertEqual(len(similar_cards), freq)
                self.assertTrue(type(similar_cards)==list)

    def test_valid_get_trio_with_all_combination_hands_method(self):
        trio_hands = [[5,5,5,8,8,8], [3,3,3,4,4,4], [9,9,9,1,1,1]]
        pair_hands = [[3,3,4,4,7,7], [10,10,1,1,2,2], [6,6,12,12,13,13]]
        solo_hands = [[3,4,7], [10,1,2],[6,12,13]]
        trio_hands = self.hlpr.convert_hand_numbers_to_card_objects(trio_hands)
        pair_hands = self.hlpr.convert_hand_numbers_to_card_objects(pair_hands)
        solo_hands = self.hlpr.convert_hand_numbers_to_card_objects(solo_hands)
        for i in range(len(trio_hands)):
            trio, pair, solo = trio_hands[i], pair_hands[i], solo_hands[i]
            self.assertTrue(len(self.hand._get_all_trio_with_combination_hands([pair], [trio]))>0)
            self.assertTrue(len(self.hand._get_all_trio_with_combination_hands([solo], [trio]))>0)

    def test_move_high_cards_to_back_of_array_method(self):
        player_cards = [[1,7,7,8,10,13], [1,2,3,7,8,10,11]]
        player_cards = self.hlpr.convert_hand_numbers_to_card_objects(player_cards)
        for cards in player_cards:
            cards = [[card] for card in cards]
            cards = self.hand._move_high_cards_to_back_of_array(cards)
            self.assertEqual(cards[-1][0].get_number(), 1)

    def test_move_high_cards_to_back_of_array_method_remove_jokers(self):
        player_cards = [[1],[2],[5],[5],[7],[11],[12],[13],[14],[15]]
        player_cards = self.hlpr.convert_hand_numbers_to_card_objects(player_cards)
        cards = self.hand._move_high_cards_to_back_of_array(player_cards)
        self.assertEqual(cards[-1][0].get_number(), 1)

    def test_valid_get_chain_hands_method(self):
        trio_hands = [[3,3,3],[4,4,4],[7,7,7],[8,8,8],[9,9,9],[10,10,10]]
        trio_hands = self.hlpr.convert_hand_numbers_to_card_objects(trio_hands)
        chain_hands = self.hand._get_chain_hands(trio_hands, min_hands_needed=2)
        self.assertTrue(len(chain_hands)>0)

        pair_hands = [[3,3],[4,4],[5,5],[6,6],[7,7],[11,11],[12,12],[13,13]]
        pair_hands = self.hlpr.convert_hand_numbers_to_card_objects(pair_hands)
        chain_hands = self.hand._get_chain_hands(pair_hands, min_hands_needed=2)
        self.assertTrue(len(chain_hands)>0)
        
        solo_hands = [[6],[7],[8],[9],[10],[2],[14]]        
        solo_hands = self.hlpr.convert_hand_numbers_to_card_objects(solo_hands)
        chain_hands = self.hand._get_chain_hands(solo_hands, min_hands_needed=5)
        self.assertTrue(len(chain_hands)>0)

    def test_invalid_get_chain_hands_method(self):
        solo_hands = [[3],[4],[5],[7],[11],[12],[13],[15]]
        solo_hands = self.hlpr.convert_hand_numbers_to_card_objects(solo_hands)
        chain_hands = self.hand._get_chain_hands(solo_hands, min_hands_needed=5)
        self.assertEqual(len(chain_hands), 0)

    def test_get_chain_hands_method_returns_chains_same_length_as_previous_hand(self):
        solo_hands = [[4],[6],[9],[10],[11],[12],[13],[1]]
        solo_hands = self.hlpr.convert_hand_numbers_to_card_objects(solo_hands)
        chain_hands = self.hand._get_chain_hands(solo_hands, min_hands_needed=5, max_hands_needed=6)
        self.assertEqual(len(chain_hands), 1)
        self.assertEqual(len(chain_hands[0]), 6)

    def test_valid_get_chain_sequences_method(self):
        solo_hands = [[4],[6],[9],[10],[11],[12],[13],[1],[2]]
        solo_hands = self.hlpr.convert_hand_numbers_to_card_objects(solo_hands)
        sequences = self.hand._get_chain_sequences(solo_hands, min_hands_needed=5)
        for chain in sequences:
            self.assertTrue(len(chain)>=5)

        pair_hands = [[4,4],[5,5],[6,6],[9,9],[12,12]]
        pair_hands = self.hlpr.convert_hand_numbers_to_card_objects(pair_hands)
        sequences = self.hand._get_chain_sequences(pair_hands, min_hands_needed=3)
        for chain in sequences:
            self.assertTrue(len(chain)>=6)

        trio_hands = [[8,8,8],[13,13,13],[1,1,1]]
        trio_hands = self.hlpr.convert_hand_numbers_to_card_objects(trio_hands)
        sequences = self.hand._get_chain_sequences(trio_hands, min_hands_needed=2)
        for chain in sequences:
            self.assertTrue(len(chain)>=6)
    
    def test_get_chain_sequences_method_returns_sequences_same_length_as_previous_hand(self):
        previous_hand = [[3,4,5,6,7]]
        previous_hand = self.hlpr.convert_hand_numbers_to_card_objects(previous_hand)

        solo_hands = [[4],[5],[6],[7],[8],[10],[11],[12],[13],[1]]
        solo_hands = self.hlpr.convert_hand_numbers_to_card_objects(solo_hands)
        sequences = self.hand._get_chain_sequences(solo_hands, min_hands_needed=5, previous_hand=previous_hand.pop())
        self.assertEqual(len(sequences), 2)
        for chain in sequences:
            self.assertTrue(len(chain)==5)

    def test_invalid_get_chain_sequence_method(self):
        solo_hands = [[4],[6],[9],[11],[12],[13],[2]]
        solo_hands = self.hlpr.convert_hand_numbers_to_card_objects(solo_hands)
        sequences = self.hand._get_chain_sequences(solo_hands, min_hands_needed=5)
        self.assertEqual(len(sequences), 0)

    def test_valid_get_airplane_hands_method(self):
        trio_hands = [[3,3,3,4,4,4]]
        pair_hands = [[7,7],[10,10]]
        solo_hands = [[7,10,1,2]]
        trio_hands = self.hlpr.convert_hand_numbers_to_card_objects(trio_hands)
        pair_hands = self.hlpr.convert_hand_numbers_to_card_objects(pair_hands)
        solo_hands = self.hlpr.convert_hand_numbers_to_card_objects(solo_hands)
        airplane_hands = self.hand._get_airplane_hands(trio_hands, solo_hands[0], pair_hands)
        self.assertTrue(len(airplane_hands)>0)

    def test_invalid_get_airplane_hands_method(self):
        trio_hands = [[3,3,3,4,4,4]]
        pair_hands = [[3,3],[4,4]]
        solo_hands = [[3,4]]
        trio_hands = self.hlpr.convert_hand_numbers_to_card_objects(trio_hands)
        pair_hands = self.hlpr.convert_hand_numbers_to_card_objects(pair_hands)
        solo_hands = self.hlpr.convert_hand_numbers_to_card_objects(solo_hands)
        airplane_hands = self.hand._get_airplane_hands(trio_hands, solo_hands[0], pair_hands)
        self.assertEqual(len(airplane_hands), 0)

    def test_valid_get_all_pairs_method(self):
        hands = [[3,3,4,4,7,8,10,11], [5,6,8,13,13,1,1]]
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            freq_map = self.hlpr.get_number_frequency_map(hand)
            pair_hands = self.hand._get_all_pairs(hand, freq_map)
            self.assertTrue(len(pair_hands)>0)

    def test_invalid_get_all_pairs_method(self):
        hands = [[3,7,8,10,11], [5,6,8,13]]
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            freq_map = self.hlpr.get_number_frequency_map(hand)
            pair_hands = self.hand._get_all_pairs(hand, freq_map)
            self.assertTrue(len(pair_hands)==0)

    def test_valid_get_all_trios_method(self):
        hands = [[3,3,4,4,4,7,8,10,10,10,11], [5,6,6,6,8,13,13,1,1]]
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            freq_map = self.hlpr.get_number_frequency_map(hand)
            trio_hands = self.hand._get_all_trios(hand, freq_map)
            self.assertTrue(len(trio_hands)>0)

    def test_invalid_get_all_trios_method(self):
        hands = [[3,3,4,4,7,8,10,11], [5,6,8,13,13,1,1]]
        hands = self.hlpr.convert_hand_numbers_to_card_objects(hands)
        for hand in hands:
            freq_map = self.hlpr.get_number_frequency_map(hand)
            trio_hands = self.hand._get_all_trios(hand, freq_map)
            self.assertTrue(len(trio_hands)==0)
    
    def test_rocket_hand_can_be_played_at_any_time(self):
        previous_hand = [[13,13,13,2,2]] 
        cards = [[3,3,3,5,5,14,15]] 
        previous_hand = self.hlpr.convert_hand_numbers_to_card_objects(previous_hand)
        cards = self.hlpr.convert_hand_numbers_to_card_objects(cards)
        self.hand.set_random_hand(cards[0], previous_hand[0])
        hand_numbers = set([card.get_number() for card in self.hand.get_hand()])
        self.assertIn(14, hand_numbers)
        self.assertIn(15, hand_numbers)
        self.assertEqual(len(self.hand.get_hand()), 2)

    def test_bomb_hand_can_be_played_at_any_time(self):
        previous_hand = [[13,13,13,2,2]] 
        cards = [[3,3,3,3,5,5,12]] 
        previous_hand = self.hlpr.convert_hand_numbers_to_card_objects(previous_hand)
        cards = self.hlpr.convert_hand_numbers_to_card_objects(cards)
        self.hand.set_random_hand(cards[0], previous_hand[0])
        hand_numbers = set([card.get_number() for card in self.hand.get_hand()])
        self.assertIn(3, hand_numbers)
        self.assertEqual(len(self.hand.get_hand()), 4) 

    def test_can_play_higher_bomb_hand_when_previous_hand_is_a_bomb_hand(self):
        previous_hand = [[5,5,5,5]] 
        cards = [[4,4,7,7,7,7,9,10]] 
        previous_hand = self.hlpr.convert_hand_numbers_to_card_objects(previous_hand)
        cards = self.hlpr.convert_hand_numbers_to_card_objects(cards)
        self.hand.set_random_hand(cards[0], previous_hand[0])
        hand_numbers = set([card.get_number() for card in self.hand.get_hand()])
        self.assertIn(7, hand_numbers)
        self.assertEqual(len(self.hand.get_hand()), 4)  

    def test_can_play_rocket_hand_when_previous_hand_is_a_bomb_hand(self):
        previous_hand = [[2,2,2,2]] 
        cards = [[5,6,7,11,14,15]] 
        previous_hand = self.hlpr.convert_hand_numbers_to_card_objects(previous_hand)
        cards = self.hlpr.convert_hand_numbers_to_card_objects(cards)
        self.hand.set_random_hand(cards[0], previous_hand[0])
        hand_numbers = set([card.get_number() for card in self.hand.get_hand()])
        self.assertIn(14, hand_numbers)
        self.assertIn(15, hand_numbers)
        self.assertEqual(len(self.hand.get_hand()), 2)