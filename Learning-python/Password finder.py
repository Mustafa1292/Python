#passwords the ones in the list
#Password is what mine is
def binary_search(passwords, password):
  counter = 0
  middle = len(passwords)//2
  first = 0
  last = len(passwords)-1
  #if the middle of password(passwords) is my password end the program 
 
  while first <= last:
    counter +=1

    if (passwords[middle] == password):
       print("Binary Search: Password found after {} steps.\nPassword found! You should change your password! " .format(counter)) 
       return True
    else:
      if passwords[middle] < password:
        first = middle+1 
      else:
        last = middle - 1 
      
        
      middle = (first+last) // 2
   
  while first >= last:
    counter +=1
    if first > last:
      print('Binary Search: Password NOT found after {} steps'.format(counter))
      break

  return False


def linear_search(passwords,password):
  counter = 0
  for i in range(len(passwords)):
    counter +=1
    if passwords[i] == password:
      print("Linear search: Password found after {} steps".format(counter))
      return True 
  print("Linear search: Password NOT found after {} steps".format(counter))
  return False  

      

passwords = []
with open ("passwords_short.txt") as file:
  for line in file.readlines():
    passwords.append(line.strip())
    
print('Reading password data ... Complete! ')
user_password = input("Please enter the password to search for: ")
linear_search(passwords,user_password)
binary_search(passwords,user_password)