import random as rd
from card import *

# Defines exception for when a card is drawn on an empty deck
class DrawError(Exception):
    pass

class Deck(object):
    def __init__(self):
        self.deck_list = []
        self.new_deck()
        
    # Resets and shuffles a new deck list
    def new_deck(self):
        self.deck_list.clear()
        for value in range(len(Card.VALUE_NAMES)):
            for suit in range(len(Card.SUIT_NAMES)):
                self.deck_list.append(Card(suit, value))
        rd.shuffle(self.deck_list)

    # Returns and removes card from deck; raises exception if deck is empty
    def draw_card(self):
        if not self.is_empty():
            return self.deck_list.pop(0)
        else:
            raise DrawError

    ######################
    # VALIDATION METHODS #
    ######################
    # Returns if deck is empty
    def is_empty(self):
        return not self.deck_list

    ##################
    # GETTER METHODS #
    ##################
    # Returns deck list
    def get_deck_list(self):
        return self.deck_list
    # Returns remaining card count in deck
    def remaining_card_count(self):
        return len(self.deck_list)
