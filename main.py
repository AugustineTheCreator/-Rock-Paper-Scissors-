import random

print("Winning Rules of the R P scissors game as follows: \n"
                                +"Rock vs Paper->Paper wins \n"
                                +"Rock vs scissors->Rock wins \n"
                                +"Paper vs scissors->scissors wins \n")

while True:
    choices = ["R", "P", "S"]
    
    player = None
    while player not in choices:
        player = input("Enter a choice (R for rock, P for paper, S for scissors): ").upper()
        if player not in choices:
            print("That's not a valid play. Check your option!\n")
        else:
            continue

    computer_action = random.choice(choices)
    print(f"\nPlayer ({player}) : CPU ({computer_action}).\n")

    if player == computer_action:
        print(f"Both players selected {player}. It's a tie!")
    elif player == "R":
        if computer_action == "S":
            print("Rock smashes Scissors! You win!")
        else:
            print("Paper covers Rock! You lose.")
    elif player == "P":
        if computer_action == "R":
            print("Paper covers Rock! You win!")
        else:
            print("Scissors cuts Paper! You lose.")
    elif player == "S":
        if computer_action == "P":
            print("Scissors cuts Paper! You win!")
        else:
            print("Rock smashes Scissors! You lose.")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again.lower() != "y":
        break
print("\nBye!")