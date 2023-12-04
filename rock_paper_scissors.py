#importing the random module
import random

#\u0332 is used to underline the contents that precedes it
print()
print("\u0332".join("ROCK VS PAPER VS SCISSOR"))
print()

# user guide to rules of game
print('The rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper covers rock; Paper wins \n"
      + "Rock vs Scissors -> Rock smashes scissors; Rock wins \n"
      + "Paper vs Scissors -> Scissors cut paper; Scissor wins \n")
print()

# taking user input as the preferred action
user = input("Enter a choice - rock, paper or scissors: ")
possible_actions = ["rock", "paper", "scissors"]
computer = random.choice(possible_actions)
print(f"\nYou chose {user}, computer chose {computer}\n")

# comparing the actions and displaying the result
if user == computer:
    print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose :(")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose :(")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose :(")
