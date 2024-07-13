from card_hand import CardHand, Card
import game_rules as rules
import random 
from collections import defaultdict

class Player:
    def __init__(self):
        '''Construct a Player class with the initial stake initialised.'''
        self.set_stake_amount(60)
        self.reset()

    def play_hand(self):
        if self.get_hand() and not self.hand.play():
            self.hand.reset()
            return False

        if not self.get_hand():
            self.set_random_hand()   
        
        self.hand.calculate_hand_score(self.hand.get_hand())
        self.remove_cards(self.get_hand())
        
        return self.get_hand()

    def set_bid(self, amount: int) -> bool:
        '''Set the players' bid to the amount provided. If the bid is valid 
        but exceeds the players' total stake, the total state is returned.
        
        Args:
            amount - An integer reppresenting the amount the player is bidding. 

        Returns: True if the bid was set successfully, False otherwise. 
        '''
        if amount>3 or (amount>self.get_stake_amount() and not self.get_stake_amount()):
            return False

        if amount>self.get_stake_amount():
            self.bid = self.get_stake_amount() 
        else:
            self.bid = amount

        self.set_stake_amount(self.get_stake_amount() - self.get_bid_amount())

        return True

    def get_random_bid_amount(self) -> int:
        '''Return a random bid amount. If the bid is valid but exceeds the 
        players' total stake, the total state is returned.'''
        probabilty = random.random()
        if probabilty>0.85:
            self.set_bid(3)
        elif probabilty>0.5:
            self.set_bid(2)
        elif probabilty>0.2:
            self.set_bid(1)
        else:
            self.set_bid(0)
        
        return self.get_bid_amount()

    def get_bid_amount(self) -> int:
        '''Return the players' bid for the round.'''
        return self.bid

    def get_stake_amount(self) -> int:
        '''Return the players' total stake.'''
        return self.stake
    
    def set_stake_amount(self, amount: int):
        '''Set the players' stake to the provided amount.
        
        Args:
            amount - An integer representing the players' total stake amount. 
        '''
        self.stake = amount

    def set_cards(self, cards: list[Card]):
        '''Set the players' cards.
        
        Args:
            cards - A list of Card objects that represent the players' cards.    
        '''
        self.cards = cards

    def add_wildcards(self, wildcards: list[Card]):
        '''Add the wildcards to the players' cards.
        
        Args:
            cards - A list of Card objects that represent the players' cards.    
        '''
        self.get_cards().extend(wildcards)

    def get_cards(self) -> list[Card]:
        '''Return the players' cards.'''
        return self.cards

    def has_passed_bidding(self) -> bool:
        '''Returns True if the players bid is zero, False otherwise.'''
        return self.get_bid_amount()==0

    def get_hand(self):
        return self.hand.get_hand()

    def set_hand(self, hand):
        self.hand.select(hand)

    def set_random_hand(self, previous_hand=None):
        self.hand.set_random_hand(self.get_cards(), previous_hand)

    def remove_cards(self, hand):
        card_values_freq_map = defaultdict(int)
        for card in hand:
            card_values_freq_map[card.get_number()] += 1

        new_cards = list()
        for card in self.get_cards():
            if card.get_number() in card_values_freq_map.keys():
                if not card_values_freq_map[card.get_number()]:
                    new_cards.append(card)
                else:
                    card_values_freq_map[card.get_number()] -= 1
            else:
                new_cards.append(card)

        self.set_cards(new_cards)

    def reset(self):
        '''Resets the players' hand played, cards being held by the player,
        and their bid for the round.'''
        self.hand = CardHand()
        self.cards = None
        self.bid = None