############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the Dealer.


from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(deck) :
    score = 0
    for card in deck :
        score += card
    return score

def remove_excess_aces(deck) :
    deck_copy = deck
    
    while calculate_score(deck_copy) > 21 and 11 in deck_copy :
        deck_copy[deck_copy.index(11)] = 1

    return deck_copy
    
def blackjack():
    clear()
    
    ai_deck = []
    player_deck = []
    continue_blackjack = True
    player_bj = False
    ai_bj = False
    
    ai_deck.append(random.choice(cards))
    ai_deck.append(random.choice(cards))
    ai_deck = remove_excess_aces(ai_deck)

    if calculate_score(ai_deck) == 21 :
        ai_bj = True
        continue_blackjack = False
    
    player_deck.append(random.choice(cards))
    player_deck.append(random.choice(cards))
    player_deck = remove_excess_aces(player_deck)

    if calculate_score(player_deck) == 21 :
        player_bj = True
        continue_blackjack = False
    
    print(logo)
    while continue_blackjack :
        print("\n========================================")
        print(f"\nThe Dealer cards are: [x , {ai_deck[1]}]")
        print(f"Your cards are: {player_deck}, with a score of {calculate_score(player_deck)}.\n")

        decision = input("To draw another card, type 'y', to pass type 'n': ")

        if decision == 'y' :
            player_deck.append(random.choice(cards))
            player_deck = remove_excess_aces(player_deck)
            if calculate_score(player_deck) >= 21 :
                continue_blackjack = False
        elif decision == 'n' :
            while calculate_score(ai_deck) < 17 :
                ai_deck.append(random.choice(cards))
                ai_deck = remove_excess_aces(ai_deck)
            continue_blackjack = False
        else:
            print("Wrong value!\n")
            return 1

    
    while calculate_score(ai_deck) < 17 and not player_bj:
        ai_deck.append(random.choice(cards))
        ai_deck = remove_excess_aces(ai_deck)

    print("\n========================================")
    print(f"\nThe Dealer cards are: {ai_deck}, with a score of {calculate_score(ai_deck)}.\n")
    print(f"Your cards are: {player_deck}, with a score of {calculate_score(player_deck)}.\n")

    if player_bj :
        print("You got Blackjack!")
    if ai_bj :
        print("The Dealer got Blackjack!")
    
    if calculate_score(player_deck) > 21 :
        print("You lost by exceeding score of 21!\n")
    elif calculate_score(ai_deck) > 21 :
        print("The Dealer exceeded score of 21, you won! Congratulations!\n")
    elif calculate_score(player_deck) > calculate_score(ai_deck) :
        print("You won! Congratulations!\n")
    elif calculate_score(player_deck) == calculate_score(ai_deck) :
        print("It's a draw!\n")
    else:
        print("You lost!\n")

    print("\n========================================")
    next_game = input("To play another round of Blackjack, type 'y': ")
    if next_game == 'y' :
        blackjack()
    else:
        return 0

blackjack()



