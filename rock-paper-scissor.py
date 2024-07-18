import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "player"
    else:
        return "computer"

def play_game(rounds):
    player_score = 0
    computer_score = 0

    for _ in range(rounds):
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(player_choice, computer_choice)
        if winner == "player":
            player_score += 1
            print("You win this round!")
        elif winner == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("This round is a tie!")

        print(f"Current Score -> Player: {player_score}, Computer: {computer_score}\n")

    if player_score > computer_score:
        print("You win the game!")
    elif computer_score > player_score:
        print("Computer wins the game!")
    else:
        print("The game is a tie!")


rounds = int(input("Enter the number of rounds: "))
play_game(rounds)