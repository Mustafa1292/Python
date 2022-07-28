
import string

new_list = []
space = ""
with open("zingarelli2005.txt") as folder:
  for ciao in folder.readlines():
    new_list.append(ciao.strip())
joined = space.join(new_list)
for letter in string.ascii_uppercase:
  a = joined.count(letter)
  print(letter,'-',round(a/len(joined)*100,3),"%")


