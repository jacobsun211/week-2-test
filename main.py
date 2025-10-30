from core import deck
from core import game_logic



def main():
    player = {"hand": []}
    dealer = {"hand": []}
    deck_of_cards = deck.build_standard_deck()
    deck_of_cards = deck.shuffle_by_suit(deck_of_cards)
    game_logic.run_full_game(deck_of_cards, player, dealer)

if __name__ == '__main__':
    main()

