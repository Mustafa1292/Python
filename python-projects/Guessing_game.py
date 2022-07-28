import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

EASY_lIVES = 10
HARD_LIVES = 5


def check_answer(gues, ans, turn):
    if gues > ans:
        print("Too high")
        return turn-1
    elif ans > gues:
        print("Too low")
        return turn - 1
    else:
        print(f"Nice, you got it! The answer was {ans}")
        turn = 0


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "hard":
        return HARD_LIVES
    elif level == "easy":
        return EASY_lIVES
    else:
        print("Not a valid level")


# def game():
#     print(logo)
#     set_difficulty()

def game():
    print("Welcome to the number Guessing Game!\n")
    print("I'm thinking of a number between 1 and a 100")

    answer = random.randint(1, 100)
    print(f"the random values is {answer}\n")

    turn = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"Number of attempts left {turn} ")
        guess = int(input("Make a guess: "))
        turn = check_answer(guess, answer, turn)

        if turn==0:
            print("You have run out of attempts, you lose")
            return

game()
