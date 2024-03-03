'''
import random
with open('besenova.txt', encoding = 'utf8') as subor:
    for riadok in subor:
        print(riadok.strip())

subor = open('novy.txt', 'w')
subor.write('jeden dva tri\n')
subor.write()

name = input('Zadaj nazov suboru: ')
subor = open(f'{name}.txt',encoding='utf8')
riadok = subor.readline()
print(riadok[2], riadok [4])


subor = open('besenova.txt', encoding='utf8')
sum = 0
length= 0
for riadok in subor:
    sum += 1
    if len(riadok)>length:
        length = len(riadok)
    print(sum, length)
subor.close()


def find(name, string):
    file = open(name, 'r', encoding='utf8')
    for row in file:
        if string in row:
            print(row)
find('D:\GBAS\python shit\maggie python.py', 'if')

file = open('suradnice.txt', 'w')
for i in range(10):
    print(random.randrange(500), file=file)
file.close()

def priemer(name):
    list = []
    with open(file=name) as file:
        for row in file:
            x = int(file.readline())
            list.append(x)
    priemer = int(sum(list))/len(list)
    print(priemer)
priemer('suradnice.txt')

import tkinter
canvas = tkinter.Canvas(width=1500, height = 800)
canvas.pack()

with open('besenova.txt', encoding='utf8') as file:
    x, y = 300, 50
    for i, riadok in enumerate(file):
        canvas.create_text(x, y, text = riadok, font='georgia 20')
        y += 40
canvas.mainloop()
'''
import tkinter, random
canvas = tkinter.Canvas(width=800, height = 800)
canvas.pack()

file = open('ciary.txt', 'w')
for i in range(5):
    file.write(f'{random.randrange(50, 750, 10)} {random.randrange(50, 750, 10)}\n')
file.write('\n')
for i in range(5):
    file.write(f'{random.randrange(50, 750, 10)} {random.randrange(50, 750, 10)}\n')
file.close()


def line_maker(file):  
    list = []
    list2= []
    with open(file) as file:
        for row in file:
            if row != '\n':
                space = row.find(' ')
                coords = int(row[:space]), int(row[space+1:])
                list.append(coords)
            else:
                list2 = list
                list = []
            print(list)
            print(list2)

        for i in range(len(list)-1):
            canvas.create_line(list[i], list[i+1])
        for i in range(len(list2)-1):
            canvas.create_line(list2[i], list2[i+1])
line_maker('ciary.txt')

canvas.mainloop()

