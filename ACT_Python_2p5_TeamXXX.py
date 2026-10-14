import random

p1_choice = input("Enter either rock, paper, or scissors: ").lower()
ai_choice = random.choice(["rock", "paper", "scissors"])
if p1_choice not in ("rock", "paper", "scissors"):
    print("invalid choice")
else:
    print(f"AI chose: {ai_choice}")
    #Tie
    if p1_choice == ai_choice:
        print("tie")
    #Rock
    elif p1_choice == "rock" and ai_choice == "scissors":
        print("You win")
    elif p1_choice == "rock" and ai_choice == "paper":
        print("You lose")
    #Scissors
    elif p1_choice == "scissors" and ai_choice == "paper":
        print("You win")
    elif p1_choice == "scissors" and ai_choice == "rock":
        print("You lose")
    #Paper
    elif p1_choice == "paper" and ai_choice == "scissors":
        print("You lose")
    elif p1_choice == "paper" and ai_choice == "rock":
        print("You win")
