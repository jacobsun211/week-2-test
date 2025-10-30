from random import randint


def build_standard_deck():
    suits = ["H","C","D","S"]
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    deck = []
    for suite in suits:
        for rank in ranks:
            card = create_card(rank, suite)
            deck.append(card)
    return deck

def create_card(rank, suite):
    if rank == "A":
        value = 1
    elif rank == "J":
        value = 10
    elif rank == "Q":
        value = 10
    elif rank == "K":
        value = 10
    else:
        value = int(rank)
    card = {"rank":rank, "suite":suite,"value":value}
    return card

def shuffle_by_suit(deck,swaps = 5000):
    count = 0
    while count < swaps:
        i = randint(0,51)
        j = randint(0,51)
        if deck[i] == deck[j]:
            continue
        j_suite = deck[j]["suite"]
        if j_suite == "H" and j % 5 != 0:
            continue
        if j_suite == "C" and j % 3 != 0:
            continue
        if j_suite == "D" and j % 2 != 0:
            continue
        if j_suite == "S" and j % 7 != 0:
            continue
        deck[i],deck[j] = deck[j],deck[i]
        count += 1
    return deck


# deck = build_standard_deck()
# print(shuffle_by_suit(deck))