# Cricket Score Analysis System

import numpy as np
import json

players = {}

# Function to add player score
def add_score():
    name = input("Enter player name: ")
    score = int(input("Enter score: "))

    if name not in players:
        players[name] = []

    players[name].append(score)
    print(f"Score added for {name}.\n")


# Function to calculate batting average
def batting_average():
    name = input("Enter player name: ")

    if name in players:
        scores = np.array(players[name])
        average = np.mean(scores)
        print(f"{name}'s Batting Average: {average:.2f}\n")
    else:
        print("Player not found.\n")


# Function to display highest scorer
def highest_scorer():
    highest = 0
    best_player = ""

    for player, scores in players.items():
        total = sum(scores)
        if total > highest:
            highest = total
            best_player = player

    if best_player:
        print(f"Highest Scorer: {best_player} with {highest} runs.\n")
    else:
        print("No data available.\n")


# Function to generate match summary
def match_summary():
    print("\n--- Match Summary ---")

    for player, scores in players.items():
        print(f"{player}: Scores = {scores}, Total = {sum(scores)}")

    print()


# Function to search player statistics
def search_player():
    name = input("Enter player name: ")

    if name in players:
        print(f"\nPlayer: {name}")
        print(f"Scores: {players[name]}")
        print(f"Total Runs: {sum(players[name])}")
        print(f"Matches Played: {len(players[name])}")
        print()
    else:
        print("Player not found.\n")


# Function to save score history to file
def save_history():
    with open("score_history.json", "w") as file:
        json.dump(players, file)

    print("Score history saved successfully.\n")


# Main Menu
while True:
    print("===== Cricket Score Analysis System =====")
    print("1. Add Player Score")
    print("2. Calculate Batting Average")
    print("3. Display Highest Scorer")
    print("4. Generate Match Summary")
    print("5. Search Player Statistics")
    print("6. Save Score History")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_score()

    elif choice == '2':
        batting_average()

    elif choice == '3':
        highest_scorer()

    elif choice == '4':
        match_summary()

    elif choice == '5':
        search_player()

    elif choice == '6':
        save_history()

    elif choice == '7':
        print("Exiting Program...")
        break

    else:
        print("Invalid choice. Try again.\n")