from game.core.card import Card

class TestHelpers:
    def __init__(self):
        self.card_numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
        self.suits = {"hearts", "diamonds", "clubs", "spades", "joker"}
        self.number_points_dict = {3:1, 4:2, 5:3, 6:5, 7:8, 8:13, 9:21, 
            10:34, 11:55, 12:89, 13:144, 1:233, 2:377, 14:610, 15:987}

    
    def get_number_frequency_map(self, hand):
        '''Return a hash map from card numbers to frequency of number appearing 
        in hand.

        Args:
            hand - A list of Card objects.

        Returns: A integer to interger hash map representing card number-frequency pairs. 
        '''
        number_freq = dict()
        for card in hand:
            key = card.get_number()
            if key in number_freq.keys():
                number_freq[key] += 1
            else:
                number_freq[key] = 1
        
        return number_freq

    '''
        Card Hand Getters
    '''
    def get_valid_solo_card_chain_hands(self):
        '''Returns a 2-dimensional list of integers representing the valid
        solo chain card hands.'''
        return [[3,4,5,6,7],
            [4,5,6,7,8],
            [8,9,10,11,12],
            [9,10,11,12,13,1], 
            [3,4,5,6,7,8,9,10,11,12,13,1],
            [5,6,7,8,9,10,11,12],
            [7,8,9,10,11,12,13],
            [10,11,12,13,1]] 

    def get_invalid_solo_card_chain_hands(self): 
        '''Returns a 2-dimensional list of integers representing the invalid
        solo chain card hands.'''
        return [[3,4,5,6],
            [3,4,5,6,2],
            [12,13,1,2,14],
            [11,12,13,1,2,14,15], 
            [5,6,8,9,10],
            [9,10,11,12,1],
            [4,6,8,10,12],
            [4,5,6,7,8,9,10,11,12,13,1,2]]

    def get_valid_pair_card_hand(self):
        '''Returns a 2-dimensional list of integers representing the valid
        pair card hands.'''
        return [[3,3],
            [6,6], 
            [1,1],
            [2,2]]

    def get_invalid_pair_card_hand(self):
        '''Returns a 2-dimensional list of integers representing the invalid
        pair card hands.'''
        return [[3,4],
            [5,7],
            [11,12],
            [2,15],
            [10],
            [1]]

    def get_valid_pair_chain_card_hand(self):
        '''Returns a 2-dimensional list of integers representing the valid
        pair chain card hands.'''
        return [[3,3,4,4,5,5],
            [6,6,7,7,8,8],
            [12,12,13,13,1,1],
            [8,8,9,9,10,10],
            [10,10,11,11,12,12,13,13,1,1],
            [7,7,8,8,9,9,10,10], 
            [5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,1,1],
            [4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13]] 

    def get_invalid_pair_chain_card_hand(self):
        '''Returns a 2-dimensional list of integers representing the invalid
        pair chain card hands.'''
        return [[3,3,4,4],
            [10,10,11,11],
            [5,6,6,7,7,8,8],
            [7,7,8,8,9,10,10],
            [11,11,12,13,13,1,1],
            [3,3,5,5,7,7],
            [3,3,4,4,2,2],
            [8,8,10,10,12,12],
            [13,13,1,1,2,2],
            [1,1,2,2,14,15],
            [4,4,6,6,8,8,10,10,12,12],
            [12,12,13,13,1,1,2,2],
            [13,13,1,1,2,2,14,15],
            [4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,1,1],
            [11,11,12,12,1,1]]

    def get_valid_trio_card_hand(self):
        '''Returns a 2-dimensional list of integers representing the valid
        trio card hands.'''
        return [[3,3,3],
            [2,2,2],
            [7,7,7],
            [12,12,12]] 

    def get_invalid_trio_card_hand(self):
        '''Returns a 2-dimensional list of integers representing the invalid
        trio card hands.'''
        return [[3,3,4],
            [6,6,9],
            [10,10,1],
            [2,14,15]]

    def get_valid_trio_chain_card_hand(self):
        '''Returns a 2-dimensional list of integers representing the valid
        trio chain card hands.'''
        return [[3,3,3,4,4,4],
            [10,10,10,11,11,11,12,12,12,13,13,13],
            [7,7,7,8,8,8],
            [13,13,13,1,1,1],
            [8,8,8,9,9,9,10,10,10,11,11,11,12,12,12,13,13,13],
            [9,9,9,10,10,10,11,11,11,12,12,12,13,13,13,1,1,1]] 

    def get_invalid_trio_chain_card_hand(self):
        '''Returns a 2-dimensional list of integers representing the invalid
        trio chain card hands.'''
        return [[3,3,4,4],
            [11,11,12,12],
            [3,3,4,4,4],
            [3,3,4,4,4,5,5,5,6,6,6],
            [7,7,7,8,8],
            [7,7,7,8,8,8,9,9],
            [3,3,3,5,5,5,7,7,7],
            [2,2,2,3,3,3,4,4,4],
            [8,8,8,9,9,9,10,10,10,11,11,11,12,12,12,13,13,13,1,1,1],
            [12,12,12,1,1,1]]

    def get_valid_bomb_card_hand(self):
        '''Returns a 2-dimensional list of integers representing the valid
        bomb card hands.'''
        return [[3,3,3,3],
            [2,2,2,2],
            [11,11,11,11]] 

    def get_invalid_bomb_card_hand(self):
        '''Returns a 2-dimensional list of integers representing the invalid
        bomb card hands.'''
        return [[3,3,3,5], 
            [7,7,7,13],
            [5,6,6,6],
            [7,7,7],
            [12,12,12]]

    def get_valid_rocket_card_hand(self):
        '''Returns a 2-dimensional list of integers representing the valid
        rocket card hands.'''
        return [[14,15], [15,14]] 

    def get_invalid_rocket_card_hand(self):
        '''Returns a 2-dimensional list of integers representing the invalid
        rocket card hands.'''
        return [[5,14], [15,6], [14,13], [9,15]]

    def get_valid_combination_with_solo_hand(self):
        '''Returns a 2-dimensional list of integers representing valid
        combination hands containing solo card hand.'''
        return [[3,3,3,7],         # trio with solo hand
            [8,8,8,13],
            [1,1,1,3],
            [2,2,2,11],
            [5,5,5,14],
            [2,2,2,3],
            [3,3,3,4,4,4,7,11],    # airplane with solo hand for each trio
            [12,12,12,13,13,13,3,4],
            [4,4,4,5,5,5,6,6,6,7,7,7,11,13,1,2],
            [10,10,10,11,11,11,12,12,12,13,13,13,1,1,1,3,4,5,6,7],
            [3,3,3,3,7,9],         # bomb with dual solo hand
            [10,10,10,10,3,4],
            [2,2,2,2,8,12]]

    def get_invalid_combination_with_solo_hand(self):
        '''Returns a 2-dimensional list of integers representing invalid
        combination hands containing solo card hand.'''
        return [[3,3,3,3],          # trio with solo hand
            [11,11,11,11],
            [2,2,2,2],
            [2,2,5],
            [7,7,12],
            [3,3,3,4,4,4,7,7],      # airplane with solo hand for each trio
            [6,6,6,7,7,7,8,8,8,10,14,15],
            [8,8,8,9,9,9,10,10,10,1,1,3],
            [2,2,2,3,3,3,8,12],
            [3,3,3,3,14,15],        # bomb with dual solo hand
            [7,7,7,7,14,15]]
    
    def get_valid_combination_with_pair_hand(self):
        '''Returns a 2-dimensional list of integers representing valid
        combination hands containing pair card hand.'''
        return [[3,3,3,7,7],          # trio with pair hand
            [6,6,6,9,9],
            [2,2,2,1,1],
            [2,2,2,3,3],
            [3,3,3,4,4,4,1,1,2,2],    # airplane with pair hand for each  trio
            [6,6,6,7,7,7,8,8,8,12,12,13,13,1,1],
            [11,11,11,12,12,12,13,13,13,1,1,1,9,9,10,10,2,2,14,15],
            [3,3,3,3,6,6,11,11],      # bomb with dual pair hand
            [8,8,8,8,4,4,1,1],
            [2,2,2,2,5,5,14,15]]

    def get_invalid_combination_with_pair_hand(self):
        '''Returns a 2-dimensional list of integers representing invalid
        combination hands containing pair card hand.'''
        return [[3,3,3,6,9],             # trio with pair hand
            [7,7,7,12,13],
            [2,2,2,4,4,5,5],
            [3,3,3,4,4,4,1,1],           # airplane with pair hand for each trio
            [8,8,8,9,9,9,10,10,10,4,4,6,6],
            [10,10,10,11,11,11,4,4,7,7,12,12],
            [2,2,2,3,3,3,7,7,12,12],
            [3,3,3,3,14,15,11],         # bomb with dual pair hand
            [7,7,7,7,4,4],
            [2,2,2,2,4,4,5,5,9,9]]

    def get_valid_trio_with_solo_hands(self):
        return [[3,3,3,9], 
            [6,6,6,9], 
            [4,4,4,2], 
            [2,2,2,13], 
            [12,12,12,2], 
            [1,1,1,14]] 
    
    def get_valid_trio_with_pair_hands(self):
        return [[5,5,5,8,8], 
            [10,10,10,2,2], 
            [1,1,2,2,2], 
            [7,7,7,12,12], 
            [13,13,1,1,1]] 
    
    def get_valid_airplane_with_solo_hands(self):
        return [[3,3,3,4,4,4,8,11], 
            [5,5,5,6,6,6,7,7,7,10,13,1], 
            [12,12,12,13,13,13,1,1,1,5,9,14],
            [10,10,10,11,11,11,12,12,12,13,13,13,1,1,1,6,4,3,8,2]] 

    def get_valid_airplane_with_pair_hands(self):
        return [[3,3,3,4,4,4,8,8,11,11], 
            [5,5,5,6,6,6,7,7,7,10,10,13,13,1,1], 
            [12,12,12,13,13,13,1,1,1,5,5,7,7,9,9],
            [11,11,11,12,12,12,13,13,13,1,1,1,6,6,4,4,3,3,2,2]]

    def get_hands_with_unrecognised_card_category(self):
        return [[3,3,3,4,4,4,4], 
            [7,7,2,2,2,2], 
            [10,10,2],
            [4,4,4,4,14,15]] 

    def get_valid_bomb_with_dual_solo_card_hand(self):
        return [[5,5,5,5,7,8], 
            [10,10,10,10,3,12], 
            [2,2,2,2,9,14], 
            [7,7,7,7,12,1]] 

    def get_valid_bomb_with_dual_pair_card_hand(self):
        return [[3,3,3,3,6,6,10,10], 
            [7,7,7,7,4,4,2,2], 
            [13,13,13,13,6,6,8,8], 
            [1,1,1,1,13,13,2,2]]
        
    '''
        Integer to Card object converter
    '''
    def _create_card_object_for_card_number(self, number, suit="joker"):
        '''Create a Card object using the provided card number.
        
        Args: 
            number - An integer representing the card number.
            suit - A string representing the card suit. Default is joker.

        Returns: A Card object. 
        '''
        return Card(number=number, suit=suit)

    def convert_hand_numbers_to_card_objects(self, hands, suit="hearts"):
        '''Helper function to convert the card numbers in the hand to Card objects.
        
        Args:
            hands - A 2-dimensional list containing a list of integers. 
            suit - The suit of all the cards. Default is hearts. 
        
        Returns: A 2-dimensional list containing a list of Card objects.
        '''
        for i in range(len(hands)):
            for j in range(len(hands[i])):
                hands[i][j] = self._create_card_object_for_card_number(hands[i][j], suit)
        
        return hands
