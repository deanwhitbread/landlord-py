
from game_player import Player

class LandlordGame:
    def __init__(self):
        pass

    def play(self):
        pass

    def reset(self):
        pass 

class BiddingEngine:
    def __init__(self):
        self.reset()
    
    def execute_bidding_round(self):
        max_bid = 0
        winning_bidder = None
        for player in self.players:
            if player.get_bid_amount() is None:
                player.set_bid(player.get_random_bid_amount())
            
            if player.get_bid_amount()>max_bid:
                max_bid = player.get_bid_amount()
                winning_bidder = player

            if player.get_bid_amount()==3:
                break

        return max_bid, winning_bidder
    
    def set_players(self, players):
        self.players = players

    def reset(self):
        self.players = None