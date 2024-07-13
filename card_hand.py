from card_deck import Card
import game_rules as rules
from collections import Counter
import random
import game_rules as rules
from misc import constants as const

class CardHand:
    def __init__(self):
        '''Construct a CardHand object. A CardHand object represents a player's
        hand in a card game. 
        '''
        self.reset()

    def select(self, hand: list[Card]):
        '''Set the selected cards as the player's card hand.
        
        Args:
            hand - A list of Card objects representing the players' hand. 
        '''
        self.current_hand = hand

    def play(self) -> bool:
        '''Return whether the selected hand can be played. 
        
        Returns: True if the selected hand can be played, False otherwise. 
        '''
        if not self.current_hand:
            return False

        # count the frequency of the card numbers
        number_freq = self.get_card_number_frequency_map(self.current_hand)
        
        # calculate score of hand. 
        self.calculate_hand_score(self.current_hand)

        # check whether the hand is valid and can be played.
        if len(self.current_hand)==1:
            return rules.is_solo(number_freq)
        elif len(self.current_hand)==2:
            return (rules.is_pair(number_freq) or 
                rules.is_rocket(number_freq))
        elif len(self.current_hand)==3:
            return rules.is_trio(number_freq)
        else:
            return (rules.is_bomb(number_freq) or 
                rules.is_combination(number_freq) or 
                rules.is_chain(number_freq))

    def calculate_hand_score(self, hand: list[Card]):  
        '''Calculate the score of the player's current hand.
        
        Args:
            hand - A list of Card objects representing the players' hand.
        '''
        
        number_freq = self.get_card_number_frequency_map(hand)
        category = rules.get_hand_category(number_freq)
        if category==const.CARD_CATEGORY.SOLO or category==const.CARD_CATEGORY.SOLO_CHAIN:
            score = sum([card.get_points() for card in hand])
        elif category==const.CARD_CATEGORY.PAIR or category==const.CARD_CATEGORY.PAIR_CHAIN:
            score = sum([card.get_points() for card in hand]) * 2
        elif category==const.CARD_CATEGORY.TRIO:
            score = sum([card.get_points() for card in hand]) * 3
        elif (category==const.CARD_CATEGORY.TRIO_WITH_SOLO or 
            category==const.CARD_CATEGORY.TRIO_WITH_PAIR or 
            category==const.CARD_CATEGORY.TRIO_CHAIN or 
            category==const.CARD_CATEGORY.AIRPLANE_WITH_SOLO or 
            category==const.CARD_CATEGORY.AIRPLANE_WITH_PAIR):
                
                points = 0
                for card in hand:
                    if number_freq[card.get_number()]==3: 
                        points += card.get_points()

                score = points  
        elif category==const.CARD_CATEGORY.BOMB:
            score = sum([card.get_points() for card in hand]) * 5
        else:
            score = sum([card.get_points() for card in hand]) * 10
        
        self.hand_score = score

        return self.hand_score

    def get_card_number_frequency_map(self, hand: list[Card]) -> Counter[int:int]:
        '''Return a hash map mapping card numbers in the hand to the frequency the numbers
        appears in the hand.
        
        Args:
            hand - A list of Card objects representing the players' hand. 
        '''
        return Counter([card.get_number() for card in hand])

    def set_random_hand(self, cards, previous_hand=None):
        if type(cards)==list and len(cards)==0:
            raise ValueError("The list of Card objects is empty. The cards parameter must be a list of Card objects with at least one object.")
        if cards is None or (type(cards)==list and type(cards[0])!=Card):
            if cards is None:
                card_type = None
            else:
                card_type = type(cards[0])

            msg = f"The cards attribute is of type '{card_type}' when it should be a list of Card objects."
            raise TypeError(msg)

        if previous_hand:
            category = self.get_hand_category(previous_hand)
            previous_hand_score = self.calculate_hand_score(previous_hand)
        else:
            prob_play_single_card = 0.3
            if len(cards)==1 or random.random()<prob_play_single_card:
                self.select(random.choice([[card] for card in cards]))
                return self.get_hand()
            

        freq_map = self.get_card_number_frequency_map(cards)
        all_valid_hands = list()
        
        # add rocket
        rocket_set = set([14,15])
        rocket_hand = [card for card in cards if card.get_number() in rocket_set]
        if len(rocket_hand)==2:
            all_valid_hands.append(rocket_hand)
        
        trio_hands = list()
        pair_hands = list()
        solo_hands = list()
        for num, freq in freq_map.items():
            # add bomb hand
            if freq==4:
                all_valid_hands.append([card for card in cards if card.get_number()==num])

            # add trio
            if freq>=3:
                cards_needed = 3
                temp_cards = cards.copy()
                arr = list()
                while cards_needed:
                    card = temp_cards.pop()
                    if card.get_number()==num:
                        arr.append(card)
                        cards_needed -= 1

                trio_hands.append(arr)

            # add pair cards
            if freq>=2:
                cards_needed = 2
                temp_cards = cards.copy()
                arr = list()
                while cards_needed:
                    card = temp_cards.pop()
                    if card.get_number()==num:
                        arr.append(card)
                        cards_needed -= 1

                pair_hands.append(arr)
        
        # all pairs and trios to valid hands
        if pair_hands:
            all_valid_hands.extend(pair_hands)
        if trio_hands:
            all_valid_hands.extend(trio_hands)

            # add trio with solo cards
            trio_with_solo_hands = list()
            for i in range(len(trio_hands)):
                for j in range(len(cards)):
                    if cards[j].get_number()!=trio_hands[i][0].get_number():
                        trio_with_solo = trio_hands[i] + [cards[j]]
                        trio_with_solo_hands.append(trio_with_solo)
            all_valid_hands.extend(trio_with_solo_hands)

            if pair_hands:
                trio_with_pair_hands = list()
                # add all trio with pair hands
                for i in range(len(trio_hands)):
                    for j in range(len(pair_hands)):
                        if pair_hands[j][0].get_number()!=trio_hands[i][0].get_number():
                            trio_with_pair = trio_hands[i] + pair_hands[j]
                            trio_with_pair_hands.append(trio_with_pair)
                all_valid_hands.extend(trio_with_pair_hands)

        # find trio chain sequences
        trio_chain_hands = list()
        if len(trio_hands)>1:
            trio_hands.sort(key=lambda card: card[0].get_number())   
            # move ace and two pairs to the back
            while trio_hands[0][0].get_number()==1 or trio_hands[0][0].get_number()==2:
                if trio_hands[0][0].get_number()==2:
                    trio_hands = trio_hands[1:]
                else:
                    hand = trio_hands[0]
                    trio_hands = trio_hands[1:]
                    trio_hands.append(hand)      

            # sliding window to find pair chains
            sequence = [arr[0].get_number() for arr in trio_hands]
            chain_size = 1
            left, prev, right = 0, 0, 1
            while right<len(sequence):                
                if sequence[prev]==sequence[right]-1:
                    prev = right
                    right += 1
                    chain_size += 1
                else:
                    left = right
                    prev = right
                    right += 1
                    chain_size = 1

                if chain_size>=2:
                    chain_cards = trio_hands[left:right]
                    hand = [card for trio in chain_cards for card in trio]
                    trio_chain_hands.append(hand)

        # find pair chain sequences
        pair_chain_hands = list()
        if len(pair_hands)>2:
            pair_hands.sort(key=lambda card: card[0].get_number())   
            # move ace and two pairs to the back
            while pair_hands[0][0].get_number()==1 or pair_hands[0][0].get_number()==2:
                if pair_hands[0][0].get_number()==2:
                    pair_hands = pair_hands[1:]
                else:
                    hand = pair_hands[0]
                    pair_hands = pair_hands[1:]
                    pair_hands.append(hand)      

            # sliding window to find pair chains
            sequence = [arr[0].get_number() for arr in pair_hands]
            chain_size = 1
            left, prev, right = 0, 0, 1
            while right<len(sequence):                
                if sequence[prev]==sequence[right]-1:
                    prev = right
                    right += 1
                    chain_size += 1
                else:
                    left = right
                    prev = right
                    right += 1
                    chain_size = 1

                if chain_size>=3:
                    chain_cards = pair_hands[left:right]
                    hand = [card for pair in chain_cards for card in pair]
                    pair_chain_hands.append(hand)

        # sliding window to find solo chains.
        solo_chain_hands = list()
        sequence = [card.get_number() for card in cards]
        chain_size = 1
        max_chain_size = len(previous_hand) if previous_hand else float('inf')
        left, prev, right = 0, 0, 1
        while right<len(sequence):
            if sequence[prev]==sequence[right]-1:
                prev = right
                right += 1
                chain_size += 1
            else:
                left = right
                prev = right
                right += 1
                chain_size = 1

            if chain_size>max_chain_size:
                left += 1
                chain_size -= 1
            
            if chain_size>=5:
                chain_cards = cards[left:right]
                solo_chain_hands.append(chain_cards)
            
        all_valid_hands.extend(solo_chain_hands)

        # find airplane with pair combinations
        airplane_hands = list()
        if len(trio_chain_hands):
            pairs_needed = 0
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
                for card in cards:
                    if card.get_number() not in trio_card_numbers and card.get_suit()!="joker":
                        combination.append(card)
                        solos_needed -= 1
                        trio_card_numbers.add(card.get_number())

                    if not solos_needed:
                        airplane_hands.append(combination)
                        break
                    
        # add trio chain, pair chain, and valid airplane hands to all hands.
        if trio_chain_hands:
            all_valid_hands.extend(trio_chain_hands)
        if pair_chain_hands:
            all_valid_hands.extend(pair_chain_hands)
        if airplane_hands:
            all_valid_hands.extend(airplane_hands)

        # choose random card to play
        if previous_hand is not None:
            valid_hands = list()
            for hand in all_valid_hands + [[card] for card in cards]:
                hand_category_match = self.get_hand_category(hand)==category
                is_stronger_hand = self.calculate_hand_score(hand)>previous_hand_score
                # print(hand, previous_hand_score, is_stronger_hand)
                if hand_category_match and is_stronger_hand:
                    valid_hands.append(hand)
            
            if len(valid_hands)>0:
                self.select(random.choice(valid_hands))
        else:
            if not all_valid_hands:
                # only single cards left
                self.select(random.choice([[card] for card in cards]))
            else:
                self.select(random.choice(all_valid_hands))
        
        #### Player will need to remove the cards in the hand from their cards.

        return self.get_hand()

    def get_hand(self):
        return self.current_hand

    def get_hand_category(self, hand):
        number_freq = dict()
        for card in hand:
            number_freq[card.get_number()] = number_freq.get(card.get_number(), 0) + 1
        
        return rules.get_hand_category(number_freq)  

    def reset(self):
        '''Clear the player's hand, removing all selected cards.'''
        self.current_hand = list()
        self.hand_score = 0
        