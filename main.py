from example import LandlordGame
from game.core.player import Player

MAX_PLAYERS = 3

if __name__=='__main__':
    game = LandlordGame([Player() for _ in range(MAX_PLAYERS)])
    while not game.has_game_ended():        
        game.play()
    