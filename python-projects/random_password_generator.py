# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

x = []

for i in range(0, nr_letters):
    #x = x + random.choice(letters)
    x.append(random.choice(letters))
    #print(random.choice(letters))
for i in range(0, nr_numbers):
    #x = x + random.choice(numbers)
    x.append(random.choice(numbers))
    #print(random.choice(numbers))
for i in range(0, nr_symbols):
    #x = x + random.choice(symbols)
    x.append(random.choice(symbols))
    #print(random.choice(symbols))

random.shuffle(x)


#print(x)
z = ""
for i in x:
    z += i
print(f"\Your password is {z}")

