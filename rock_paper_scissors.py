import random

def play():
    user = input("Whats your choice? (r) for rock, (p) for paper, (s) for scissors\n ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        print("Its a tie!")

    elif is_win(user, computer):
        print("You won!")
        
    else:
        print("You lost!")

# r > s, s > p, p > r
def is_win(user, computer):
    if (user == "r" and computer == "s") \
    or (user == "s" and computer == "p") \
    or (user == "p" and computer == "r"):
        return True

play()