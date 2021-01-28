from deck import *

# Hand contains
# Hand size

class Hand(object):
    def __init__(self):
        self.hand_list = []

    # Print the contents of the hand
    def display_hand(self):
        for card in self.hand_list:
            print(card.to_string())

    # Draw a card from the deck and add it to the hand list
    def draw_from_deck(self, deck, number_of_cards):
        try:
            for i in range(number_of_cards):
                card = deck.draw_card()
                self.add_card(card)
        except DrawError:
            print("The deck is empty, no more cards can be drawn")
        self.sort_by_value()

    # Add a card to the hand list
    def add_card(self, card):
        self.hand_list.append(card)

    def discard_card(self, number_of_cards):
        pass

    # Perform selection sort on hand list based on card suit
    def sort_by_suit(self):
        for i in range(len(self.hand_list)):
            min_index = i
            for j in range(i+1, len(self.hand_list)):
                if self.hand_list[min_index].get_suit_int() > self.hand_list[j].get_suit_int():
                    min_index = j
            temp = self.hand_list[i]
            self.hand_list[i] = self.hand_list[min_index]
            self.hand_list[min_index] = temp

    # Perform selection sort on hand list based on card value
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

    # Return size of hand list
    def get_size(self):
        return len(hand_list)
