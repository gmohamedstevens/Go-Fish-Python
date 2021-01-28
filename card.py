# Defines a card class
class Card(object):
    
    SUIT_NAMES = ["Clubs", "Hearts", "Diamonds", "Spades"]
    VALUE_NAMES =["Ace", "2", "3", "4", "5",
    "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def to_string(self):
        return Card.VALUE_NAMES[self.value] + " of " + Card.SUIT_NAMES[self.suit]

    def get_value_int(self):
        return self.value
    
    def get_suit_int(self):
        return self.suit
