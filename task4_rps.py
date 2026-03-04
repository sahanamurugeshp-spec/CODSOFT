import random

options = ["rock", "paper", "scissors"]

while True:
    user = input("Enter rock, paper, or scissors: ").lower()
    computer = random.choice(options)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")

    elif user in options:
        print("Computer wins!")

    else:
        print("Invalid input!")

    again = input("Play again? (yes/no): ")
    if again.lower() != "yes":
        break