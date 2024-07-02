from card_hand import CardHand
import game_rules as rules
import random 

class Player:
    def __init__(self):
        self.set_stake_amount(60)
        self.reset()

    def set_bid(self, amount):
        if amount>3 or (amount>self.stake and not self.stake):
            return False

        if amount>self.stake:
            self.bid = self.stake 
        else:
            self.bid = amount

        self.stake -= self.bid

        return True

    def get_random_bid_amount(self):
        if random.random()>0.85:
            bid = 3
        elif random.random()>0.5:
            bid = 2
        elif random.random()>0.2:
            bid = 1
        else:
            bid = 0
        
        self.set_bid(bid)
        return self.get_bid_amount()

    def get_bid_amount(self):
        return self.bid

    def get_stake_amount(self):
        return self.stake
    
    def set_stake_amount(self, amount):
        self.stake = amount

    def set_cards(self, cards):
        self.cards = cards

    def add_wildcards(self, wildcards):
        self.cards.extend(wildcards)

    def reset(self):
        self.hand = CardHand()
        self.cards = None
        self.bid = None