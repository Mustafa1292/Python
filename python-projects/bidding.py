logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


#HINT: You can call clear() to clear the output in the console.

from os import system, name

print(logo)
print('Welcome to the secret aution pair')
more_user = 'yes'

users = {}

while more_user == 'yes':
    user_name = input('What is your name? ')
    user_bid = int(input('What is your bid? '))
    
    # users = [{'Name': user_name, 'Bid': user_bid}]
    users[user_name] = user_bid

    more_user = input('Are there more users "yes" or "no"? ')

    system('cls')
x = 0
person = ''

for key in users:
    price = users[key]
    
    if price > x:
        x = price
        person = [key]
        str(person)
    
print(f"The highest bid is {person}")
        