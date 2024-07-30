from collections import defaultdict
from game_player import Player
import game_rules as rules

class GameplayEngine:
    def __init__(self):
        '''Construct a GameplayEngine object.'''
        self.reset() 

    def play_round(self, order: list[Player], stake: int) -> (Player, int): 
        '''Plays a round of Landlord and returns the round winner and winning stake. 
        
        Args: 
            order - A list of Player objects representing the order of play, with the landlord
                    playing first, starting the round.
            stake - An integer representing the initial stake at the beginning of the round. 
        
        Returns: A tuple containing a player object in the first index that represents the winning player,
                and an integer in the second index representing the total stake won from the round. 
        '''
        previous_hand, previous_player_to_play_hand = None, None
        ptr = -1
        while len(order[ptr].get_cards())!=0:
            player = order[ptr]
            
            # check if both players skipped. 
            if previous_player_to_play_hand == player:
                previous_hand = None

            if previous_hand:
                player.set_random_hand(previous_hand)
            else:
                player.set_random_hand()
            
            if player.get_hand():
                if self.double_round_stake(player, previous_player_to_play_hand):
                    stake *= 2
                
                previous_hand, previous_player_to_play_hand = player.get_hand(), player 
                player.play_hand()
                player.hand.reset()
            else:
                # player skips
                pass

            # check is player has won
            if len(player.get_cards())==0:
                break                
            
            # choose next player
            ptr = (ptr-1)%3
        
        return previous_player_to_play_hand, stake
    
    def get_play_order(self, landlord: Player, peasants: list[Player]) -> list[Player]:
        '''Returns a list of Player objects representing the play order of the round of landlord.
        
        Args:
            landlord - A Player object that represents the landlord in a single round.
            peasants - A list of Player objects that represents the peasants in a single round.
        '''
        return peasants + [landlord]

    def double_round_stake(self, player: Player, previous_player: Player) -> bool:
        '''Returns True if the round stake should be doubled, False otherwise.
        
        Args:
            player - A Player object representing the current player who is playing a hand.
            previous_player - A Player object representing the previous player to play a hand. 
        '''
        card_number_freq = defaultdict(int)
        for card in player.get_hand():
            card_number_freq[card.get_number()] += 1

        return player==previous_player or rules.is_bomb(card_number_freq) or rules.is_rocket(card_number_freq)

    def reset(self):
        '''Resets the GameplayEngine class, resetting the landlord and peasants in the round.'''
        self.landlord = None
        self.peasants = None
    