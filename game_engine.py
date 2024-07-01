
from game_player import Player
from card_deck import CardDeck

class LandlordGame:
    def __init__(self, players):
        self.players = players
        self.bidding_engine = BiddingEngine()
        self.deck = CardDeck()
        self.reset()

    def play(self):
        # check players have stake to bid
        for player in self.get_players():
            if player.get_stake_amount()==0:
                # a player has ran out of stake to bid, game ends. 
                return False

        # deal cards to players
        self.deck.shuffle()
        p1, p2, p3 = self.get_players()[0], self.get_players()[1], self.get_players()[2]
        p1_cards, p2_cards, p3_cards, wildcards = self.deck.deal()

        p1.set_cards(p1_cards)
        p2.set_cards(p2_cards)
        p3.set_cards(p3_cards)

        # execute the bidding round.
        if not self._execute_bidding():
            # all players have passed, new round begins
            # round ends, prepare next round.
            self.reset() 

            return False
        else:
            # play round

            # round ends, prepare next round.
            self.reset()

            return True

    def _execute_bidding(self):
        players_passing = [player.get_bid_amount()==0 for player in self.get_players()]
        if all(players_passing):
            return False 

        self.stake, self.landlord = self.bidding_engine.execute_bidding_round()
        self.peasants = [player for player in self.get_players() if player!=self.get_landlord()]

        return True

    def get_landlord(self):
        return self.landlord

    def get_peasants(self):
        return self.peasants

    def get_round_stake(self):
        return self.stake

    def get_players(self):
        return self.players

    def reset(self):
        self.landlord = None 
        self.peasants = None
        self.stake = 0 
        for player in self.players:
            player.reset()
        
        self.bidding_engine.reset()
        self.bidding_engine.set_players(self.players)
        self.deck.reset()

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