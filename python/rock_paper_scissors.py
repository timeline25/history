import random

def play():
    user = input("Enter your choice (rock, paper, or scissors): ").lower()
    computer = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose {user}, computer chose {computer}.\n")

    if user == computer:
        return "It's a tie!"
    elif is_win(user, computer):
        return "You won!"
    else:
        return "You lost!"

def is_win(player, opponent):
    # Return true if the player wins
    # rock beats scissors, scissors beats paper, paper beats rock
    if (player == "rock" and opponent == "scissors") or \
       (player == "scissors" and opponent == "paper") or \
       (player == "paper" and opponent == "rock"):
        return True

while True:
    print(play())
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
