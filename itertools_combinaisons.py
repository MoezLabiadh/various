from itertools import combinations

list = ['A', 'B', 'C', 'D']

comb = combinations (list, 3)

for x, y, z in comb:
    print (x,y, z)