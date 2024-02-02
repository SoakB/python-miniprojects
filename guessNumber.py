import random

def gamemode():
    mode = 0
    while mode != 1 or mode != 2 or mode !=3:
        mode = int(input("Do you want to guess a number? (1)\nWant the computer to guess your number? (2)\nOr exit? (3)\n"))
        if mode == 1:
            guess(int(input("Guess a number between 1 and ...? ")))
        elif mode == 2:
            computer_guess(int(input("Guess a number between 1 and ...? ")))
        elif mode == 3:
            break
        else:
            print("Press 1, 2 or 3!!\n")
    
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess < random_number:
            print("Sorry, guess again, too low!")
        elif guess > random_number:
            print("Sorry, guess again, too high!")
    
    print(f"Congrats! you guessed the number, {random_number}, correctly!\n")

def computer_guess(x):
    low = 1; high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low # could also be high
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"YAY!!! the computer guessed your number, {guess}, correctly!!\n")

gamemode()