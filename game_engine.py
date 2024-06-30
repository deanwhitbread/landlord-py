
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
        bidding_order = self._get_bidding_order()
        max_bid = 0
        winning_bidder = None
        for player in bidding_order:
            if player.get_bid_amount() is None:
                player.set_bid(player.get_random_bid_amount())
            
            if player.get_bid_amount()>max_bid:
                max_bid = player.get_bid_amount()
                winning_bidder = player

            if player.get_bid_amount()==3:
                break

        return max_bid, winning_bidder

    def _get_bidding_order(self):
        first_bidder = None
        for player in self.players:
            for card in player.cards:
                if card.get_number()==3 and card.get_suit()=="hearts":
                    first_bidder = player
                    break 
        
        if first_bidder:
            order = [first_bidder]
            for player in self.players:
                if player==first_bidder:
                    continue
                
                order.append(player)
            
            return order
        else:
            return self.players
    
    def set_players(self, players):
        self.players = players

    def reset(self):
        self.players = None