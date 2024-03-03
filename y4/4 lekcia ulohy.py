
#2
number = 37
number1 = number
factors= []
primes = []
active = True

for i in range(2, number + 1):
    d = 0
    for j in range(1, i + 1):
        if i % j == 0:
            d += 1
    if d <= 2:
        primes.append(i)
y = 0
primes.append('')
print(primes)
while active:
    if primes[y]:
        factor = primes[y]
        if number1 % factor == 0:
            factors.append(factor)
            number1 = number1 / factor
        else:
            y +=1
    else:
        active = False
print(str(number), '=', end=' ')
print(*factors, sep=' * ')
#end of 2


#9
import tkinter, random
canvas = tkinter.Canvas(width=700, height= 700)
canvas.pack()

number_of_rows = 10
k = 21
for row in range(number_of_rows):
    y = 20 + row * 30
    x = 20
    value = 0
    while value < k:
        text = random.randrange(1, 5)
        value += text
        canvas.create_oval(x - 10, y-10, x + 10, y + 10)
        canvas.create_text(x, y, text=text, font='Arial 10')
        x += 25
    if value == k:
        canvas.create_text(x + 50, y, text='Hura', font='Arial 25', fill='green')
    else:
        canvas.create_text(x + 50, y, text='Skoda', font='Arial 25', fill='red')
canvas.mainloop()
#end of 9

#11
import tkinter, random
canvas = tkinter.Canvas(width=700, height= 700)
canvas.pack()

n = 10
    
for i in range(n):
    x = random.randrange(100, 600)
    y = random.randrange(100, 600)
    if i == 0:
        max_x = x
        min_x = x
        max_y = y
        min_y = y
    if x > max_x:
        max_x = x
    elif x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    elif y < min_y:
        min_y = y
    canvas.create_oval(x - 5, y -5, x + 5, y + 5, fill='red')
canvas.create_rectangle(min_x, min_y, max_x, max_y, outline='blue', tags='stvorec')


canvas.mainloop()
#end of 11
