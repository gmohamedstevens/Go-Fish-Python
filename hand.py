from deck import *
from card import *

# Hand contains

class Hand(object):
    def __init__(self):
        self.hand_list = []

    # Print the contents of the hand
    def display_hand(self):
        for card in self.hand_list:
            print(card.to_string())

    # Draw a card from the deck and add it to the hand
    def draw_from_deck(self, deck, number_of_cards):
        try:
            for i in range(number_of_cards):
                card = deck.draw_card()
                self.add_card(card)
        except DrawError:
            print("The deck is empty, no more cards can be drawn")
        self.sort_by_value()

    # Add a card to the hand
    def add_card(self, card):
        self.hand_list.append(card)

    def has_card(self, suit, value):
        pass

    # Discard all cards of a specified value
    def discard_by_value(self, value):
        for index in range(len(self.hand_list)-1 , -1, -1):
            card = self.hand_list[index]
            if card.get_value_int() == value:
                self.hand_list.remove(card)

    # Returns the card count of a specified value in the hand
    def count_by_value(self, value):
        count = 0
        for card in self.hand_list:
            if card.get_value_int() == value:
                count += 1
        return count

    # Returns if a four of a kind of the secified value exists in the hand
    def four_of_a_kind_exists(self, value):
        if self.count_by_value(value) == 4:
            return True
        else:
            return False

    # Perform selection sort on hand on card suit
    def sort_by_suit(self):
        for i in range(len(self.hand_list)):
            min_index = i
            for j in range(i+1, len(self.hand_list)):
                if self.hand_list[min_index].get_suit_int() > self.hand_list[j].get_suit_int():
                    min_index = j
            temp = self.hand_list[i]
            self.hand_list[i] = self.hand_list[min_index]
            self.hand_list[min_index] = temp

    # Perform selection sort on hand based on card value
    def sort_by_value(self):
        for i in range(len(self.hand_list)):
            min_index = i
            for j in range(i+1, len(self.hand_list)):
                if self.hand_list[min_index].get_value_int() > self.hand_list[j].get_value_int():
                    min_index = j
            temp = self.hand_list[i]
            self.hand_list[i] = self.hand_list[min_index]
            self.hand_list[min_index] = temp


    ##################
    # GETTER METHODS #
    ##################

    # Return size of hand
    def get_size(self):
        return len(hand_list)
