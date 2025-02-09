import misc.constants as const
import misc.helpers as hlpr
import random
from game.core.card import Card

class CardDeck:
    def __init__(self):
        '''Construct a deck of cards where individual cards in the deck 
        are represented as Card objects.'''
        self.reset()

    def get_card_deck(self) -> list[Card]:
        '''Return a list of Card objects representing the deck of cards.'''
        return self._deck

    def add_card_to_deck(self, card_number: int, suit: str):
        '''Add a card to the deck.
        
        Args:
            card_number - A integer representing the card number. 
            suit - A string representing the suit the card belongs to. 
        '''
        if card_number<=0 or card_number>15:
            return 
            
        self.get_card_deck().append(Card(number=card_number, suit=suit))

    def shuffle(self):
        '''Randomly shuffle the card deck.'''
        random.shuffle(self.get_card_deck()) 
    
    def deal(self) -> list[Card]:
        '''Deal the cards to the three players in the game. Each player
        receives 17 cards each, with the remaining 3 cards becoming wildcards.

        Returns four lists containing Card objects, where the first three sets 
        contain players' cards, and the final set containing the wildcard deck.
        '''
        if len(self.get_card_deck())<54:
            return list(), list(), list(), list()

        player1, player2, player3 = list(), list(), list()
        for i in range(17*3):
            card = self.get_card_deck().pop()
            if i%3==0:
                player1.append(card)
            elif i%3==1:
                player2.append(card)
            else:
                player3.append(card)

        return player1, player2, player3, self.get_card_deck()
    
    def reset(self):
        '''Reset the card deck.'''
        self._deck = []
        for num in range(1, 14):
            for suit in ["hearts", "diamonds", "clubs", "spades"]:
                self.add_card_to_deck(num, suit)

        self.add_card_to_deck(14, "joker")
        self.add_card_to_deck(15, "joker")