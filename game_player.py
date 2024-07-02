from card_hand import CardHand
import game_rules as rules
import random 

class Player:
    def __init__(self):
        self.set_stake_amount(60)
        self.reset()

    def set_bid(self, amount):
        if amount>3 or (amount>self.get_stake_amount() and not self.get_stake_amount()):
            return False

        if amount>self.get_stake_amount():
            self.bid = self.get_stake_amount() 
        else:
            self.bid = amount

        self.set_stake_amount(self.get_stake_amount() - self.get_bid_amount())

        return True

    def get_random_bid_amount(self):
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

    def get_cards(self):
        return self.cards

    def reset(self):
        self.hand = CardHand()
        self.cards = None
        self.bid = None