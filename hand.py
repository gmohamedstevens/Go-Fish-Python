from deck import *

# Hand contains
# Hand size

class Hand(object):
    def __init__(self):
        self.hand_list = []

    def display_hand(self):
        for card in self.hand_list:
            print(card.to_string())

    def draw_from_deck(self, deck, number_of_cards):
        try:
            for i in range(number_of_cards):
                card = deck.draw_card()
                self.add_card(card)
        except DrawError:
            print("The deck is empty, no more cards can be drawn")
        self.sort_by_value()

    def add_card(self, card):
        self.hand_list.append(card)

    def discard_card(self, number_of_cards):
        pass

    def sort_by_suit(self):
        for i in range(len(self.hand_list)):
            min_index = i
            for j in range(i+1, len(self.hand_list)):
                if self.hand_list[min_index].get_suit_int() > self.hand_list[j].get_suit_int():
                    min_index = j
            temp = self.hand_list[i]
            self.hand_list[i] = self.hand_list[min_index]
            self.hand_list[min_index] = temp

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
    
    def get_size(self):
        return len(hand_list)
    
