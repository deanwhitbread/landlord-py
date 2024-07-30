from game.core.player import Player

class BiddingEngine:
    def __init__(self):
        '''Construct a BiddingEngine object. The bidding engine handles the bidding
        between players in a round of landlord.'''
        self.reset()
    
    def execute_bidding_round(self) -> (int, Player):
        '''Simulates a round of bidding in a game of landlord. An interger
        representing the maximum bid and a Player object representing the winning
        bidder is returned.'''
        max_bid, winning_bidder = 0, None
        for player in self._get_bidding_order():
            if player.get_bid_amount() is None:
                player.set_bid(player.get_random_bid_amount())
            
            if player.get_bid_amount()>max_bid:
                max_bid = player.get_bid_amount()
                winning_bidder = player

            if player.get_bid_amount()==3:
                break

        return max_bid, winning_bidder

    def _get_bidding_order(self) -> list[Player]:
        '''Returns a list of Player objects where the players are ordered in their
        bidding order. A player bids first if they have the three of hearts card. 
        Otherwise, the list of players in the game is returned.'''
        first_bidder = None
        for player in self.get_players():
            for card in player.get_cards():
                if card.get_number()==3 and card.get_suit()=="hearts":
                    first_bidder = player
                    break 
        
        if first_bidder:
            order = [first_bidder]
            for player in self.get_players():
                if player!=first_bidder:
                    order.append(player)
            
            return order
        else:
            return self.get_players()
    
    def set_players(self, players: list[Player]):
        '''Sets the players playing the game of landlord.
        
        Args:
            players - A list of Player objects that represent the players
                    playing the game of landlord.
        '''
        self.players = players

    def get_players(self):
        '''Returns a list of Player objects that represent the players in the game.'''
        return self.players

    def reset(self):
        '''Resets the bidding engine, ready for a new round of landlord.'''
        self.players = None
