
from game_player import Player
from card_deck import CardDeck

class LandlordGame:
    def __init__(self, players):
        '''Construct a Landlord Game object.
        
        Args:
            players - A list of Player objects that represent the players
                    in the game.
        '''
        self.players = players
        self.bidding_engine = BiddingEngine()
        self.deck = CardDeck()

    def play(self) -> bool:
        '''Play a round of Landlord. True is returned if a round can be
        played, False otherwise.'''
        if self.has_game_ended():
            return False

        wildcards = self.deal_cards_to_players()

        if self.all_players_passed_during_bidding():
            self.reset() 

            return False
        else:
            # execute the bidding round
            self._execute_bidding()

            # reveal wildcards to all players at the end of bidding 
            print(wildcards)

            # add cards to the landlords cards.
            self.give_landlord_wildcards(wildcards)

            # play round

            # round ends, prepare next round.
            self.reset()

            return True

    def _execute_bidding(self) -> bool:
        '''Simulates the bidding between players in the game. Returns True if
        the players have submitted a bid, False if all players have skipped bidding.'''
        if self.all_players_passed_during_bidding():
            return False

        p1, p2, p3 = self.get_players()
        game_players = [p1, p2, p3]
        self.stake, self.landlord = self.bidding_engine.execute_bidding_round()
        self.peasants = [player for player in game_players if player!=self.get_landlord()]

        return True

    def get_landlord(self) -> Player:
        '''Returns a Player object representing the player who is the landlord in the round.'''
        return self.landlord

    def get_peasants(self) -> list[Player]:
        '''Returns a list of Player objects representing the player who are peasants in the round.'''
        return self.peasants

    def get_round_stake(self) -> int:
        '''Returns an integer representing the current round's stake.'''
        return self.stake

    def get_players(self) -> Player:
        '''Returns three Player objects.'''
        return self.players[0], self.players[1], self.players[2]

    def give_landlord_wildcards(self, wildcards: list[Card]):
        '''Adds the wildcards to the landlord players' cards.
        
        Args:
            wildcards - A list of Card objects representing the round's wildcards.
        '''
        self.get_landlord().add_wildcards(wildcards)

    def has_game_ended(self) -> bool:
        '''Returns True if there is a player that has no more stake to bid, False otherwise.'''
        for player in self.get_players():
            if player.get_stake_amount()==0:
                return True
        
        return False

    def all_players_passed_during_bidding(self) -> bool:
        '''Returns True if all players have skipped bidding, False otherwise.'''
        p1, p2, p3 = self.get_players()
        return all([p1.has_passed_bidding(), p2.has_passed_bidding(), p3.has_passed_bidding()])

    def deal_cards_to_players(self) -> list[Card]:
        '''Deals the deck of cards to the players in the game. Returns a list of Card objects
        that represents the remaining wildcards after the cards have been dealt to players.'''
        self.deck.shuffle()
        p1, p2, p3 = self.get_players()
        c1, c2, c3, wildcards = self.deck.deal()

        p1.set_cards(c1)
        p2.set_cards(c2)
        p3.set_cards(c3)

        return wildcards

    def reset(self):
        '''Resets the round in a game of landlord.'''
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