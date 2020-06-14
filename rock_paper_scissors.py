gestures = ["rock", "paper", "scissors", "lizard", "spock"]
n_rounds = 0
max_round = 5
rounds_to_win = 3
player_score = 0
cpu_score = 0
player_won = 0
player_choice = 0
cpu_choice = 0
winner = 0
draw_score = 0
i = 0

def duel(player_option, cpu_option):
    win_conditions = {
        "rock": ("scissors", "lizard"),
        "paper": ("rock", "spock"),
        "scissors": ("paper", "lizard"),
        "lizard": ("paper", "spock"),
        "spock": ("rock", "scissors")
    }
    if player_option == cpu_option:
        return 0
    elif cpu_option in win_conditions[player_option]:
        return 2
    else:
        return 1

import random
player_choice = input("Enter gesture: ")
while player_score < rounds_to_win or cpu_score < rounds_to_win:
    if player_choice in gestures: #valid gestures only.
        cpu_choice = random.choice(gestures)
        print("You choosed", player_choice, "the CPU choosed", cpu_choice)
        winner = duel(player_choice, cpu_choice) #result of battles.
        if winner == 2:
            print("You won the round!")
            player_score += 1
        elif winner == 1:
            print("You lost the round!")
            cpu_score += 1
        else:
            draw_score += 1
            print("Draw!")
        print(player_score, "x", cpu_score, " - Number of draws = ", draw_score,".")
        if player_score == rounds_to_win:
            print("You won the game!")
            break
        if cpu_score == rounds_to_win:
            print("CPU won the game!")
            break
        n_rounds += 1
        if n_rounds == max_round:
            print("Game over. Limit rounds reached!")
            break
    else:
        print("Invalid gesture!")
    player_choice = input("Enter gesture: ")