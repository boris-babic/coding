import math 

n = 9
list = [[1, 1], [3, 2], [2, 3], [4, 9], [5, 6], [7, 8], [6, 7], [8, 5], [9, 4]]
'''
for i in range(n): #vstup do programu
    northside, southside = input().split()
    bridge = [northside, southside]
    list.append(bridge)
'''
list.sort()

for i in range(n):
    prve = [x[0] for x in list]
    druhe = [x[1] for x in list]
print(list)
print(prve, druhe)

cena = []
for prvok in prve:
    x = druhe.index(prvok) - prve.index(prvok)
    print(prvok, x)
    cena.append(x)
print(cena)

for i in range(n):
    for j in range(n):
        if len(cela)< j+iand cena[j]<=cena[j+i]:
            print(j+1, j+i+1, 'yes')
        else:
            print(j+1, j+i+1, 'no')