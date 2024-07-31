from game.interface.simulation import SimulationInterface

class LandlordGame(SimulationInterface):
    def __init__(self, players):
        '''Construct a Landlord Game object.
        
        Args:
            players - A list of Player objects that represent the players
                    in the game.
        '''
        super().__init__(players)

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
            if not self._execute_bidding():
                self.reset() 

                return False
            
            # reveal wildcards to all players at the end of bidding 
            print(wildcards)

            # add cards to the landlords cards.
            self.give_landlord_wildcards(wildcards)

            # play round
            # get play order
            order = self.gameplay_engine.get_play_order(self.get_landlord(), self.get_peasants())
            winner, total_stake = self.gameplay_engine.play_round(order, self.get_round_stake())
            self.update_players_stake(winner, total_stake)

            # round ends, prepare next round.
            self.reset()

            return True
    