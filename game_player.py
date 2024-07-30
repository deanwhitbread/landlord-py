from card_hand import CardHand, Card
import random 
from collections import defaultdict
import game.rules as rules

class Player:
    def __init__(self):
        '''Construct a Player class with the initial stake initialised.'''
        self.set_stake_amount(60)
        self.reset()

    def play_hand(self, previous_hand: list[Card]=None) -> list[Card]:
        '''Returns a list of Card objects that represents the hand played by the player. 
        If the previous hand is chosen, the hand will either be the same category as the 
        previous hand, or an empty list representing the player skipping the play. 
        
        Args:
            previous_hand - A list of Card objects representing the previous hand played.
                            Default is None. 
        '''
        if self.get_hand() and not self.hand.is_valid():
            self.hand.reset()
            return False

        if not self.get_hand():
            self.set_random_hand(previous_hand)   
        
        self.hand.get_hand_score(self.hand.get_hand())
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

        # self.set_stake_amount(self.get_stake_amount() - self.get_bid_amount())

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
    
    def set_stake_amount(self, amount: int) -> None:
        '''Set the players' stake to the provided amount.
        
        Args:
            amount - An integer representing the players' total stake amount. 
        '''
        self.stake = amount

    def set_cards(self, cards: list[Card]) -> None:
        '''Set the players' cards.
        
        Args:
            cards - A list of Card objects that represent the players' cards.    
        '''
        self.cards = cards

    def add_wildcards(self, wildcards: list[Card]) -> None:
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

    def get_hand(self) -> list[Card] or None:
        '''Returns a list of Card object representing the players' hand, if a hand has been 
        set, None otherwise.'''
        return self.hand.get_hand()

    def set_hand(self, hand: list[Card]) -> None:
        '''Sets the players' hand.
        
        Args:
            hand - A collection of Card objects to set the players' hand to. 
        '''
        self.hand.set_hand(hand)

    def set_random_hand(self, previous_hand: list[Card]=None) -> None:
        '''Randomly sets the players' hand. If the previous hand is provided, the hand 
        selected will a hand in the same category, or None if no hand exists.
        
        Args:
            previous_hand - A list of Card objects that represents the last hand played. 
                            Default is None.
        '''
        self.hand.set_random_hand(self.get_cards(), previous_hand)

    def remove_cards(self, hand: list[Card]) -> None:
        '''Removes the provided cards from the players' cards.

        Args:
            hand - A list of Card objects representing the cards to be removed from the players'
                    hand. 
        '''
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