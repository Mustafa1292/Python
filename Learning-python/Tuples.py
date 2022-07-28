
result ={}
for perimeter in range (1,2019):
  for a in range(1,perimeter//3):
    for b in range(a+1, perimeter//2):
      c = perimeter - a - b
      if (a*b)%12 == 0 and a**2 + b**2 == c**2:
        if perimeter not in result:
          result[perimeter] = []
        result[perimeter].append((a,b,c))
lens = []
lens2 = []
for x in result.keys():
 #lens will store which perimeter has a max number.
 lens.append(len(result[x]))
 #lens2 will store the actual perimeter
 lens2.append(x)

#Q stores which perimeter has the most amount of pythagorean triples 
Q = lens.index(max(lens))
p = result[lens2[Q]]
 

print('The perimeter of', lens2[Q] ,'gives a maximum number of', lens[Q] ,'triangles. The triangles are:')
for p in p:
  print(p)