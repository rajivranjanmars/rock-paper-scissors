import random

score= 0
exit = False
while exit == False:
    options=["rock","paper","scissors"]
    user_input =input("Enter your choice: rock, paper or scissors: ")
    computer_choice = random.choice(options)
    if user_input =="exit":
        print("Goodbye")
        print("Final score is", score)
        exit = True

    elif user_input == computer_choice:
        print("It's a tie!")
        print("score is", score)
    elif user_input == "rock":
        if computer_choice == "scissors":
            print("You win!")
            score = score +1
            print("score is", score)
        else:
            print("You lose!")
            score = score -1
            print("score is", score)
    elif user_input == "paper":
        if computer_choice == "rock":
            print("You win!")
            score = score +1
            print("score is", score)
        else:
            print("You lose!")
            score = score -1
            print("score is", score)
    elif user_input == "scissors":
        if computer_choice == "paper":
            print("You win!")
            score = score +1
            print("score is", score)
        else:
            print("You lose!")
            score = score -1
            print("score is", score)
    else:   
        print("Invalid input")
        print("score is", score)
    