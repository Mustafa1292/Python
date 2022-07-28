import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

cpu = [rock, paper, scissors]

cpu = random.choice(cpu)


user = input("Choose R, P, S: ")

print(f"{user} + \n  {cpu}\n")

if user == "R":
    print(rock)
elif user == "S":
    print(scissors)
elif user == "P":
    print(paper)
else:
    print("invalid")

if user == "R" and cpu == paper: 
    print("CPU wins")
elif user == "S" and cpu == paper:
    print("you win")
elif user == "R" and cpu == scissors:
    print("You win")
elif user == "P" and cpu == scissors:
    print("Cpu wins")
elif user == "P" and cpu == rock:
    print("you win")
elif user == "R" and cpu == rock:
    print("Draw")
elif user == "S" and cpu == scissors:
    print("Draw")
elif user == "P" and cpu == paper:
    print("Draw")
