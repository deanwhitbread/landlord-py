from card_hand import CardHand

class Player:
    def __init__(self):
        self.reset()

    def bid(self, amount):
        if amount>3 or amount>self.stake:
            return False 
        
        self.stake -= amount

        return True

    def get_stake_amount(self):
        return self.stake

    def reset(self):
        self.stake = 60
        self.hand = CardHand()