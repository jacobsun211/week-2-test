
def ask_player_action():
    answer = input("please choose \n\nH to drew a card \nS to stand down ")
    if answer != "S" and answer != "H":
        ask_player_action()
    return answer
