'''
import tkinter
canvas = tkinter.Canvas(width=825, height= 100)
canvas.pack()

x=''
list=[]
with open('picture.txt') as picture:
    for row in picture:
        newrow = row.strip('\n')
        counter = 0
        rowlist=[]
        for num in newrow:
            x += num
            if counter !=5:
                counter +=1
            else:
                x = '#' + x
                rowlist.append(x)
                counter = 0
                x =''
        list.append(rowlist)

y = 0

for j in list:
    x = 0
    for k in j:
        canvas.create_rectangle(x, y, x, y, fill=k, width=0)
        x +=1
    y +=1


y=0
with open('picture.txt') as picture:
    for row in picture:
        for i in range(len(row.strip())//6):
            canvas.create_rectangle(i, y, i, y, fill=f'#{row[i*6:i*6+6]}', outline='')
        y+=1
canvas.mainloop()

import random
file = open('numbers.txt', 'w')
for i in range(20):
    x= random.randrange(2)
    file.write(f'{2*random.randrange(1,101)+x} {2*random.randrange(1,101)+x+1}\n')
file.close()
'''
def gcf(a, b):
    if b>a:
        a,b = b,a
    remainder=1
    while remainder:
        remainder = a % b
        a, b = b, remainder
    return a
with open('numbers.txt') as file:
    for row in file:
        a, b = int(row[:row.find(' ')]), int(row[row.find(' ')+1:].strip())
        print(a, b, gcf(a,b))