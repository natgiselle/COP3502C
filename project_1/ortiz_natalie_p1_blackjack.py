# Natalie Ortiz
# COP3502C Project 1: Blackjack
# 02/12/2026

import p1_random as p1
rng = p1.P1Random()

blackjack_rounds = 0
completed_rounds = 0
player_win = 0
player_hand = 0
dealer_win = 0
tied_rounds = 0
actively_playing = True

while actively_playing:
    # new game loop
    blackjack_rounds+=1
    print(f"START GAME #{blackjack_rounds}")
    print()
    player_hand = 0

    # outputs [1, 13] therefore it is different from when using range function with loops!!
    card = rng.next_int(13) + 1 

    if card == 1:
        player_hand += 1
        print(f"Your card is a ACE!")
    elif 2 <= card <= 10:
        player_hand+= card
        print(f"Your card is a {card}!")
    elif card == 11:
        player_hand += 10
        print(f"Your card is a JACK!")
    elif card == 12:
        player_hand += 10
        print(f"Your card is a QUEEN!")
    elif card == 13:
        player_hand += 10
        print(f"Your card is a KING!")

    print(f"Your hand is: {player_hand}")
    print()
    # loops until the player is done playing
    while True:
        blackjack_menu = '1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit'
        player_option = int(input(blackjack_menu + "\n\nChoose an option: "))
        print()
        if player_option == 1:
            card = rng.next_int(13) + 1
            if card == 1:
                player_hand += 1
                print(f"Your card is a ACE!")
            elif 2 <= card <= 10:
                player_hand+= card
                print(f"Your card is a {card}!")
            elif card == 11:
                player_hand += 10
                print(f"Your card is a JACK!")
            elif card == 12:
                player_hand += 10
                print(f"Your card is a QUEEN!")
            elif card == 13:
                player_hand += 10
                print(f"Your card is a KING!")

            print(f"Your hand is: {player_hand}")
            print()

            if player_hand == 21:
                player_win += 1
                completed_rounds += 1
                print("BLACKJACK! You win!")
                print()
                break
            elif player_hand > 21:
                dealer_win += 1
                completed_rounds += 1
                print("You exceeded 21! You lose.")
                print()
                break

        elif player_option == 2:
            # the dealer is playing
            dealer_hand = rng.next_int(11) + 16
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            print()
            
            if dealer_hand > 21:
                player_win += 1
                completed_rounds += 1
                print("You win!")
                print()
                break
            elif dealer_hand > player_hand:
                dealer_win += 1
                completed_rounds += 1
                print("Dealer wins!")
                print()
                break
            elif dealer_hand == player_hand:
                tied_rounds += 1
                completed_rounds += 1
                print("It's a tie! No one wins!")
                print()
                break
            else:
                player_win += 1
                completed_rounds += 1
                print("You win!")
                print()
                break

        elif player_option == 3:
            # prints all the saved data from games played up until this option gets selected
            print(f"Number of Player wins: {player_win}")
            print(f"Number of Dealer wins: {dealer_win}")
            print(f"Number of tie games: {tied_rounds}")
            print(f"Total # of games played is: {completed_rounds}")

            if completed_rounds == 0:
                player_win_percentage = 0
            else:
                player_win_percentage = (player_win / completed_rounds) * 100
            print(f"Percentage of Player wins: {round(player_win_percentage, 1)}%")
            print()

            # DOES NOT PRINT OUT ANY GOODBYE MESSAGE!
        elif player_option == 4:
            actively_playing = False
            break
        else:
            print("Invalid input!")
            print()
            print("Please enter an integer value between 1 and 4.")