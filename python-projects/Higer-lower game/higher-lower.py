from game_data import data
import random

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },

print(logo)


# def count(turns, flag):
def correct(A, B):
    if A['follower_count'] > B['follower_count']:
        return 'A'
    else:
        return 'B'


count = 0

option_B = random.choice(data)

while count >= 0:
    option_A = option_B
    option_B = random.choice(data)

    if option_A == option_B:
        option_B = random.choice(data)

    print(f'Compare A: {option_A["name"]}, {option_A["description"]}')

    print(vs)

    print(f'Compare B: {option_B["name"]}, {option_B["description"]}')
    answer = input("Who has more followers? Type 'A' or 'B': ")

    if answer == correct(option_A, option_B):
        count += 1
    else:
        count = -1

print(f"Sorry that was wrong, Final score {count}")
