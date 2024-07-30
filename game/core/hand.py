from collections import Counter, defaultdict
import random
from misc.constants import CARD_CATEGORY as CATEGORY
import game.rules as rules
from game.core.card import Card 

class CardHand:
    def __init__(self):
        '''Construct a CardHand object. A CardHand object represents a player's
        hand in a card game. 
        '''
        self.reset()

    def set_hand(self, hand: list[Card], previous_hand: list[Card]=None, valid_hands: list[Card]=None) -> None:
        '''Set the selected cards as the player's card hand. If previous_hand is given, valid_hands
        parameter is needed to set a hand of the same card category as the previous hand, if possible.
        Otherwise no hand will be set. 
        
        Args:
            hand - A list of Card objects representing the players' hand. 
            previous_hand - A list of Card objects representing the hand last played. Default is None.
            valid_hands - A collection of list of Card objects representing the availble hands the player
                        has access to. Default is None.
        '''
        if previous_hand and valid_hands:
            category = self.get_hand_category(previous_hand)
            previous_hand_score = self.get_hand_score(previous_hand)

            possible_hands = list()
            for hand in (valid_hands):
                if ((self.get_hand_category(hand)==category and self.get_hand_score(hand)>previous_hand_score) 
                            or self.get_hand_category(hand)==CATEGORY.ROCKET or self.get_hand_category(hand)==CATEGORY.BOMB):
                    possible_hands.append(hand)
            
            if len(possible_hands)>0:
                self.set_hand(random.choice(possible_hands))
        else:
            self.current_hand = hand

    def get_hand(self) -> list[Card] or None:
        '''Returns the players' hand. Default is None if no hand is set.'''
        return self.current_hand

    def is_valid(self) -> bool:
        '''Return whether the selected hand can be played. 
        
        Returns: True if the selected hand can be played, False otherwise. 
        '''
        if not self.get_hand():
            return False

        number_freq = self.get_card_number_frequency_map(self.current_hand)
        match len(self.get_hand()):
            case 1:
                return rules.is_solo(number_freq)
            case 2:
                return (rules.is_pair(number_freq) or 
                       rules.is_rocket(number_freq))
            case 3: 
                return rules.is_trio(number_freq)
            case _:
                return (rules.is_bomb(number_freq) or 
                        rules.is_combination(number_freq) or 
                        rules.is_chain(number_freq))

    def get_hand_score(self, hand: list[Card]) -> int:  
        '''Calculate the score of the player's current hand.
        
        Args:
            hand - A list of Card objects representing the players' hand.
        '''
        number_freq = self.get_card_number_frequency_map(hand)
        category = rules.get_hand_category(number_freq)
        match category:
            case CATEGORY.SOLO | CATEGORY.SOLO_CHAIN:
                self.hand_score = sum([card.get_points() for card in hand])
            case CATEGORY.PAIR | CATEGORY.PAIR_CHAIN:
                self.hand_score = sum([card.get_points() for card in hand]) * 2
            case CATEGORY.TRIO:
                self.hand_score = sum([card.get_points() for card in hand]) * 3
            case (CATEGORY.TRIO_CHAIN | CATEGORY.TRIO_WITH_SOLO | 
                    CATEGORY.TRIO_WITH_PAIR | CATEGORY.AIRPLANE_WITH_SOLO | 
                    CATEGORY.AIRPLANE_WITH_PAIR):
                self.hand_score = sum([card.get_points() for card in hand if number_freq[card.get_number()]==3]) * 3
            case CATEGORY.BOMB | CATEGORY.BOMB_WITH_SOLO | CATEGORY.BOMB_WITH_PAIR:
                self.hand_score = sum([card.get_points() for card in hand]) * 5
            case _:
                self.hand_score = sum([card.get_points() for card in hand]) * 10

        return self.hand_score

    def get_card_number_frequency_map(self, hand: list[Card]) -> Counter[int:int]:
        '''Return a hash map mapping card numbers in the hand to the frequency the numbers
        appears in the hand.
        
        Args:
            hand - A list of Card objects representing the players' hand. 
        '''
        return Counter([card.get_number() for card in hand])

    def set_random_hand(self, cards: list[Card], previous_hand: list[Card]=None) -> list[Card] or None:
        '''Chooses a random hand given the players' cards. If the previous hand is given, a card of the same
        category as the previous hand will be choosen, or no hand will be selected if there are no cards in the same
        category.

        Args:
            card - A list of Card objects representing the players' cards.
            previous_hand - A set of Card objects representing the hand previously played. Default is None. 

        Returns: A list of Card objects representing the cards chosen by the function. 
        '''
        if type(cards)==list and len(cards)==0:
            msg = "The list of Card objects is empty. The cards parameter must be a list of Card objects with at least one object."
            raise ValueError(msg)

        if cards is None or (type(cards)==list and type(cards[0])!=Card):
            card_type = type(cards[0]) if cards else None
            msg = f"The cards attribute is of type '{card_type}' when it should be a list of Card objects."
            raise TypeError(msg)

        freq_map = self.get_card_number_frequency_map(cards)
        valid_hands = list()
        solo_hands = [[card] for card in cards]
        pair_hands, trio_hands = list(), list()

        if not previous_hand:
            # possibly begin the new round with a single card. 
            PLAY_SINGLE_PROB = 0.3
            if len(cards)==1 or random.random()<PLAY_SINGLE_PROB:
                self.set_hand(random.choice(solo_hands))
                return self.get_hand()
            
        # add rocket.
        if 14 in freq_map.keys() and 15 in freq_map.keys():
            valid_hands.append(self._get_rocket_hand(cards))
        
        # add valid bomb hand and get all valid trio and pair hands.
        for num, freq in freq_map.items():
            if freq==4:
                valid_hands.append(self._get_similar_cards(cards, card_number=num, total_cards=freq))

            if freq==3:
                trio_hands.append(self._get_similar_cards(cards, card_number=num, total_cards=freq))

            if freq==2:
                pair_hands.append(self._get_similar_cards(cards, card_number=num, total_cards=freq))
        
        if pair_hands:
            valid_hands.extend(pair_hands)
        if trio_hands:
            valid_hands.extend(trio_hands)

            # add trio with solo and trio with pair combination hands.
            valid_hands.extend(self._get_all_trio_with_combination_hands(solo_hands, trio_hands))
            if pair_hands:
                valid_hands.extend(self._get_all_trio_with_combination_hands(pair_hands, trio_hands))
        
        # find chain sequences.
        trio_chain_hands = self._get_chain_sequences(trio_hands, min_hands_needed=2, previous_hand=previous_hand)
        if trio_chain_hands:
            valid_hands.extend(trio_chain_hands)

        pair_chain_hands = self._get_chain_sequences(pair_hands, min_hands_needed=3, previous_hand=previous_hand)
        if pair_chain_hands:
            valid_hands.extend(pair_chain_hands)

        solo_chain_hands = self._get_chain_sequences(solo_hands, min_hands_needed=5, previous_hand=previous_hand)
        if solo_chain_hands:
            valid_hands.extend(solo_chain_hands)

        # find airplane with single and pair combinations.
        airplane_hands = self._get_airplane_hands(trio_chain_hands, cards, pair_hands)
        if airplane_hands:
            valid_hands.extend(airplane_hands)

        
        # choose random card to play
        if previous_hand is not None:
            # set hand with same category as the previous hand.
            self.set_hand(None, previous_hand, valid_hands+solo_hands)
        else:
            if not valid_hands:
                self.set_hand(random.choice(solo_hands))
            else:
                self.set_hand(random.choice(valid_hands))

        return self.get_hand()

    def _get_rocket_hand(self, cards: list[Card]) -> list[Card]:
        '''Returns a list of Card objects containing the rocket card hand.
        
        Args:
            cards - A list of Card objects representing the players' cards. 
        '''
        return [card for card in cards if card.get_number()==14 or card.get_number()==15]

    def _get_similar_cards(self, cards: list[Card], card_number: int, total_cards: int) -> list[Card]:
        '''Returns a list of Card objects containing cards of the given number.
        
        Args:
            cards - A list of Card objects representing the players' cards.
            card_number - An integer representing the card number that should be in the list. 
            total_cards - An integer representing the total number of cards in the list. 
        '''
        similar_cards = list()
        for card in cards:
            if card.get_number()==card_number:
                similar_cards.append(card)

            if len(similar_cards)==total_cards:
                break

        return similar_cards

    def _get_all_trio_with_combination_hands(self, combination_hands: list[list[Card]], 
                                            trio_hands: list[list[Card]]) -> list[list[Card]] or None:
        '''Returns a collection of list of Card objects containing all combination hands with the trio hand category. 
        If no combination is available, None is returned. 
        
        Args:
            combination_hands - A collection of list of Card objects representing a set of non-trio card hands. 
            trio_hands - A collection of list of Card objects representing a set of trio hands.
        '''
        trio_combination_hands = list()
        for i in range(len(trio_hands)):
            for j in range(len(combination_hands)):
                if combination_hands[j][0].get_number()!=trio_hands[i][0].get_number():
                    trio_combination = trio_hands[i] + combination_hands[j]
                    trio_combination_hands.append(trio_combination)

        return trio_combination_hands

    def _move_high_cards_to_back_of_array(self, array: list[Card]) -> list[Card]:
        '''Returns a list of Card objects where the high cards (Ace and two) are either placed at the back
        of removed from the list. Method is used prior to processing chain sequences, so the number two is 
        removed from the list if present. 

        Args:
            array - A list of Card objects will be modified. 
        '''
        while array[-1][0].get_number()==14 or array[-1][0].get_number()==15:
            if array[-1][0].get_number()==15:
                array = array[:-1]

            if array[-1][0].get_number()==14:
                array = array[:-1]

        while array[0][0].get_number()==1 or array[0][0].get_number()==2:
            if array[0][0].get_number()==1:
                ace = array[0]
                array = array[1:] + [ace]

            if array[0][0].get_number()==2:
                array = array[1:]
        
        return array  

    def _get_chain_hands(self, hands_array: list[list[Card]], min_hands_needed: int, 
                        max_hands_needed: int=float('inf')) -> list[list[Card]]:
        '''Return a collection of Card objects containing all possible chain sequences. When the maximum number of 
        hands needed is provided, the function will find all hands that match that criteria. 
        
        Args:
            hands_array - A collection of Card objects containing a set of cards in the same card category. 
            min_hands_needed - An integer representing the minimum number of cards needed to fulfil a 
                            chain sequence for the card category. 
            max_hands_needed - An integer representing the maximum number of cards needed to fulfil a 
                            chain sequence for the card category. Default is positive infinity.
        '''
        if max_hands_needed<float('inf'):
            match min_hands_needed:
                case 2:
                    min_hands_needed = max_hands_needed // 3
                    if min_hands_needed<2:
                        min_hands_needed = 2
                case 3:
                    min_hands_needed = max_hands_needed // 2
                    if min_hands_needed<3:
                        min_hands_needed = 3
                case 5:
                    min_hands_needed = max_hands_needed
                    if min_hands_needed<5:
                        min_hands_needed = 5
                case _:
                    return self.get_hand()            

        # use sliding window to find all chain sequences. 
        chain_hands = list()
        sequence = [arr[0].get_number() for arr in hands_array]
        left, prev, right = 0, 0, 1
        while right<len(sequence):                
            if sequence[prev]==sequence[right]-1 or (sequence[prev]==13 and sequence[right]==1):
                prev = right
                right += 1
            else:
                left = right
                prev = right
                right += 1

            if right-left>max_hands_needed:
                left += 1
            
            if right-left>=min_hands_needed:
                chain_cards = hands_array[left:right]
                hand = [card for trio in chain_cards for card in trio]
                chain_hands.append(hand)
        
        return chain_hands

    def _get_chain_sequences(self, hands_array: list[list[Card]], min_hands_needed: int, 
                            previous_hand: list[Card]=None) -> list[list[Card]]:
        '''Returns a collection of Card objects that represent all chain sequences that satisfy the minumum 
        number of cards needed. When the previous hand is given, the minumum number of cards needed in a 
        sequence will match the number of cards in the previous hand. 

        Args:
            hands_array - A collection of Card objects containing a set of cards in the same card category. 
            previous_hand - A list of Card objects representing the previous hand played. Default is None. 
            min_hands_needed - An integer representing the minimum number of cards needed in the chain sequence. 
        '''
        max_hand_length = len(previous_hand) if previous_hand else float('inf')
        hand_sequences = list()
        if len(hands_array)>=min_hands_needed:
            hands_array.sort(key=lambda card: card[0].get_number())   
            hands_array = self._move_high_cards_to_back_of_array(hands_array)
            sequences = self._get_chain_hands(hands_array, min_hands_needed, max_hands_needed=max_hand_length)
            if sequences:
                hand_sequences.extend(sequences)

        return hand_sequences

    def _get_airplane_hands(self, trio_chain_hands: list[list[Card]], solo_hands: list[list[Card]], 
                            pair_hands: list[list[Card]]) -> list[list[Card]]:
        ''''Returns a collection of list of Card objects that represent airplane card hands. An airplane card hand 
        is a trio chain card hand with either an equal number of solo cards or an equal number of pair cards. 
        
        Args:
            trio_chain_hands - A collection of list of Card objects that represent a set of trio chain hands. 
            solo_hands - A collection of list of Card objects that represent a set of solo hands.
            pair_hands - A collection of list of Card objects that represent a set of pair hands. 
        '''
        airplane_hands = list()
        for chain in trio_chain_hands:
            trio_card_numbers = set([card.get_number() for card in chain])
            pairs_needed = len(chain) // 3
            solos_needed = len(chain) // 3
            
            combination = chain.copy()
            for pair in pair_hands:
                if pair[0].get_number() not in trio_card_numbers:
                    combination += pair
                    pairs_needed -= 1

                if not pairs_needed:
                    airplane_hands.append(combination)
                    break

            combination = chain.copy()
            for card in solo_hands:
                if card.get_number() not in trio_card_numbers and card.get_suit()!="joker":
                    combination.append(card)
                    solos_needed -= 1
                    trio_card_numbers.add(card.get_number())

                if not solos_needed:
                    airplane_hands.append(combination)
                    break
        
        return airplane_hands

    def get_hand_category(self, hand: list[Card]) -> int:
        '''Returns an interger representing the card category of the provided hand.
        
        Args:
            hand - A list of Card objects that represents a card hand.
        '''
        number_freq = defaultdict(int)
        for card in hand:
            number_freq[card.get_number()] += 1
        
        return rules.get_hand_category(number_freq)  

    def _get_all_pairs(self, cards: list[Card], freq_map: Counter[int:int]) -> list[list[Card]]:
        '''Returns a collection of lists of Card objects that represents all the available pair hands 
        in the players' cards.
        
        Args:
            cards - A list of Card objects that represents the players' current cards.
            freq_map - A Counter object that maps an integer representing the card number to an integer
                        representing the frequency of the number in the players' cards. 
        '''
        pair_hands = list()
        for key, val in freq_map.items():
            if val==2:
                pair_hands.append([card for card in cards if card.get_number()==key])

        return pair_hands

    def _get_all_trios(self, cards: list[Card], freq_map: Counter[int:int]) -> list[list[Card]]:
        '''Returns a collection of lists of Card objects that represents all the available trio hands 
        in the players' cards.

        Args:
            cards - A list of Card objects that represents the players' current cards.
            freq_map - A Counter object that maps an integer representing the card number to an integer
                        representing the frequency of the number in the players' cards. 
        '''
        trio_hands = list()
        for key, val in freq_map.items():
            if val==3:
                trio_hands.append([card for card in cards if card.get_number()==key])

        return trio_hands

    def reset(self):
        '''Clear the player's hand, removing all selected cards.'''
        self.current_hand = list()
        self.hand_score = 0
        