import random

logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        `------'                           |__/           
    """

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


user_answer = input("Do you want to play a game of black jack? 'y' or 'n' ")
loope = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if user_answer == 'y':
    loope = True


# user_total

def starting_point():
    global start
    global cpu
    start = random.choices(cards, k=2)
    cpu = random.choice(cards)
    i = 0
    for x in start:
        i = i + x
    global user_total
    user_total = i
    print(f"your first two cards are {start}, your current score is {user_total}\n")
    print(f"The computer's first card is {cpu}\n")


starting_point()


def main():
    start1 = random.choice(cards)
    cpu1 = random.choice(cards)

    start.append(start1)
    global cpu_score
    cpu_score = []
    cpu_score.append(cpu)
    cpu_score.append(cpu1)

    y = 0
    for x in start:
        y += x

    cpu_final = 0
    for x in cpu_score:
        cpu_final += x

    cpu_score.append(cpu_final)

    if (y >= 21):
        print(f'your cards {start}, your current score is {y}\n')
        print(f'Cpu fisrt card {cpu} \n')
        print(f'your final cards {start}, your final score is {y}\n')
        print(f"Computer's final final hand {cpu}, final score is {cpu_final}")
        print('you went over. you lose')
        loope = False

    else:
        print(f'your cards {start}, your current score is {y}')
        loope = True

    keep_going = True
    if cpu_final < y < 21:
        keep_going = True
        print("this condition needs to be tweaked")
    else:
        keep_going = False
        print("you lost - (disregard it needs a few tweaks here)")


while loope:

    answer = input("type 'y' to get another card or 'n' to pass ")
    if answer == 'y':
        main()
    else:
        # loope = keep_going
        # check()
        loope = False
