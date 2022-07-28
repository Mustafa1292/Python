

def helper(first, second):
    result = []
    for a in first:
        for b in second:
            result.append(a+b)

    return result

def helper2(num,look_up):
    result = [""]
    for x in num:
        result = helper(result, list(look_up[x]))
    return result

words = []
with open("words.txt") as file:
    for word in file.readlines():
        word = word.strip()
        if len(word) == 3 or len(word) == 4:
            words.append(word)

key_pad = {'0': ['O'],'1': ['I', 'L'],'2': ['A', 'B', 'C'],'3': ['D', 'E', 'F'],'4': ['G', 'H', 'I'],'5': ['J', 'K', 'L'],'6': ['M', 'N', 'O'], '7': ['P', 'Q', 'R', 'S'],'8': ['T', 'U', 'V'], '9': ['W', 'X', 'Y', 'Z']}

response = "Y"
while response.upper() == 'Y':
    phone_number = input("Please enter a phone number: ")
     #7phone = "223-5653"
    number = ""
    for letter in phone_number:
        if letter.isdigit():
                number += letter
    digit = number[:3]
    result3 = helper2(digit, key_pad)

    digit2 = number[3:]
    result4 = helper2(digit2, key_pad)

    print("Results include...")
    for a in result3:
        for b in result4:
            if a in words and b in words:
                print("{}-{}".format(a, b))

    response = input("Try another (Y/N)? ")

print("Good Bye!")