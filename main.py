import random


def get_ai_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def get_player_choice():
    choice = input("Enter your choice (rock/paper/scissors): ").lower()
    if choice in ["rock", "paper", "scissors"]:
        return choice
    else:
        print("Invalid choice")
        return get_player_choice()


def determine_winner(player_choice, ai_choice):
    if player_choice == ai_choice:
        return "Tie"
    elif player_choice == "rock" and ai_choice == "scissors":
        return "Player"
    elif player_choice == "paper" and ai_choice == "rock":
        return "Player"
    elif player_choice == "scissors" and ai_choice == "paper":
        return "Player"
    else:
        return "AI"


def play_game():
    player_choice = get_player_choice()
    ai_choice = get_ai_choice()
    winner = determine_winner(player_choice, ai_choice)
    print(f"You chose {player_choice} and the AI chose {ai_choice}")
    if winner == "Tie":
        print("It's a tie!")
    elif winner == "Player":
        print("You win!")
    else:
        print("The AI wins!")


play_game()
