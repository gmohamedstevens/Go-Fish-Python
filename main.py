from deck import *
from hand import *

def start_game():
    deck = Deck()
    player_hand = Hand()
    cpu_hand = Hand()
    
    for card in deck.get_deck_list():
        print(card.to_string())
    print(str(deck.remaining_card_count()) + " cards within deck.")

    player_hand.draw_from_deck(deck, 7)
    cpu_hand.draw_from_deck(deck, 7)
    
    print()
    print(str(deck.remaining_card_count()) + " cards within deck.")
    print()
    print("Player hand")
    print("============")
    player_hand.display_hand()
    print("============")
    print()
    print("CPU hand")
    print("========")
    cpu_hand.display_hand()
    print("========")
    print()
    
    try:
        for i in range(100):
            card = deck.draw_card()
            if card:
                print("Drew " + card.to_string())
    except DrawError:
        print("The deck is empty, no more cards can be drawn")
    print(str(deck.remaining_card_count())  + " cards within deck.")
    if deck.is_empty():
        print("The deck is empty.")

if __name__ == "__main__":
    start_game()
    input()
