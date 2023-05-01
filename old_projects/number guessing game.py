import random


print("welcome to the number guessing game!")
def play_game():
    level = input("You want to make it a challenge or be a bitch and take the easy way? Select 'C' or 'E'. ").lower()
    attempts = 0
    if level == "c":
        attempts = 5
        print("Guess your not a bitch after all you have 5 attempts to guess the correct number!")
    else:
        attempts = 10
        print("I knew you were a disappointment the moment you start typing...you have 10 attempts.")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    for attempt in range(attempts):
        guess = int(input("Guess the number: "))
        attempts -= 1
        if guess == number and level == "c":
            print("Congratulation you guess a number!")
            return
        elif guess == number and level == "e":
            print("Oh My Gawd! YoU ArE s0 SmArT!!")
            break
        elif guess < number:
            print(f"Too low! You got {attempts} attempts left.")
        elif guess > number:
            print(f"To high! You got {attempts} attempts left.")
        if attempts == 0:
            print(f"You lost, the number is {number} just go play rock paper scissor or something.")
            break
        
play_game()