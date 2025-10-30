from core.player_io import ask_player_action


def deal_two_each(deck,player,dealer):
    player["hand"] = deck[0:2]
    print(f"you drew a {deck[0]["rank"]} and {deck[1]["rank"]}")
    dealer["hand"] = deck[2:4]


def calculate_hand_value(hand):
    total = 0
    for card in hand:
        if card["rank"] == "A": #BONUS Ace = 1 or 11
            if total + 11 <= 21:
                total += 11
        else:
            total += card["value"]
    return total


def dealer_play(deck,dealer):
    total = calculate_hand_value(dealer["hand"])
    while total < 17:
        dealer["hand"].append(deck[0])
        deck.pop(0)
        total = calculate_hand_value(dealer["hand"])
    if total > 21:
        print(f"dealer lost since he have {total} points \nplayer wins by default")
        return False
    return True


def  run_full_game(deck,player,dealer):
    deal_two_each(deck,player,dealer)
    deck = deck[4:]
    total_player = calculate_hand_value(player["hand"])
    answer = ""
    while answer != "S":
        print(f"you have {total_player} points")
        answer = ask_player_action()
        if answer == "H":
            player["hand"].append(deck[0])
            print(f"you drew a {deck[0]["rank"]} that's plus {deck[0]["value"]} points!")
            deck.pop(0)
            total_player = calculate_hand_value(player["hand"])
            if total_player > 21:
                print(f"YOU LOSE! \n you have {total_player} points")
                return
    if dealer_play(deck,dealer):
        total_dealer = calculate_hand_value(dealer["hand"])
        print(f"player points: {total_player}\n dealer points: {total_dealer}")
        if total_player > total_dealer:
            print(" the winner is player!")
        elif total_player < total_dealer:
            print("the winner is dealer!")
        else:
            print("it's a drew!")




