'''
import random
def hod_kockou():
    return (int(random.randrange(1,7)))
list = [0,0,0,0,0,0]
n = 100
for i in range(n):
    x = hod_kockou()
    list[x-1] +=1
    print(f'{list[x-1]}-krat bolo hodene cislo {x}', list)
for i in range(6):
'''
'''
import random, tkinter
import time
start = time.time()
canvas = tkinter.Canvas(width= 1200, height = 800)
canvas.pack()
def hod_kockou():
    return (int(random.randrange(1,7)))

with open('hod_kockou.txt','w') as file:
    for i in range(100000):
        file.writelines(f'{hod_kockou()} {hod_kockou()} {hod_kockou()} \n')

cube1 = []
cube2 = []
cube3 = []
with open('hod_kockou.txt') as file:
    for row in file:
        row.strip()
        throw = row.split()
        cube1.append(int(throw[0]))
        cube2.append(int(throw[1]))
        cube3.append(int(throw[2]))
sums = [0]*19
for i in range(len(cube1)):
    throw_sum = cube1[i] + cube2[i] + cube3[i]
    sums[throw_sum] +=1
print(sums)
max_value = max(sums)
x = 50
for i in range(3,len(sums)):
    canvas.create_rectangle(x, 750, x + 20, 750 - sums[i]/max_value*500, fill='orange')
    canvas.create_text(x + 10, 780, text=i)
    x += 40
print(time.time())
canvas.mainloop()
'''
'''
import random, tkinter
import time
start = time.time()
canvas = tkinter.Canvas(width= 1200, height = 800)
canvas.pack()
def hod_kockou():
    return (int(random.randrange(1,7)))

with open('hod_kockou.txt','w') as file:
    for i in range(100000):
        file.writelines(f'{hod_kockou()} {hod_kockou()} {hod_kockou()} \n')

cube1 = []
cube2 = []
cube3 = []
sums = [0]*19
with open('hod_kockou.txt') as file:
    for row in file:
        row.strip()
        throw = sum(int(x)for x in row.split())
        sums[throw] +=1

max_value = max(sums)
x = 50
for i in range(3,len(sums)):
    canvas.create_rectangle(x, 750, x + 20, 750 - sums[i]/max_value*500, fill='orange')
    canvas.create_text(x + 10, 780, text=i)
    x += 40
print(time.time() - start)
canvas.mainloop()
'''

import random

with open('priklady.txt','w') as file:
    for i in range(10):
        sign = ('+', '-')
        file.write(f'{random.randrange(100)} {random.choice(sign)} {random.randrange(100)} =  \n')

with open('priklady.txt') as file:
    new_equations = []
    for row in file:
        og = row
        row.strip()
        sum , dif = 0, 0
        if '+' in row:
            number1 = int(row[:row.find('+')].strip())
            number2 = int(row[row.find('+')+1: row.find('=')].strip())
            sum = number1 + number2
        if '-' in row:
            number1 = int(row[:row.find('-')].strip())
            number2 = int(row[row.find('-')+1: row.find('=')].strip())
            dif = number1 - number2
        if sum < 100 and dif >= 0:
            new_equations.append(og)
print(new_equations)
with open('priklady.txt', 'w') as file:  
    for equation in new_equations:
        file.write(equation)    

