'''
import tkinter, random
canvas = tkinter.Canvas(background='black', width= 515, height= 400)
canvas.pack()
hz = ['32', '64', '128', '256', '512', '1k', '2k', '4k', '8k', '16k']
green_max = 150
yellow_max = 250
#hore 20 do 350
def column (x, y, height):
    canvas.create_rectangle(x + 20, y, x + 50, y - height, fill = 'green', width=0)
    if height > green_max:
        canvas.create_rectangle(x + 20, y - green_max, x + 50, y - height, fill = 'yellow', width=0)
    if height > yellow_max:
        canvas.create_rectangle(x + 20, y - yellow_max, x + 50, y - height, fill = 'red', width=0)
while True:
    for i,j in enumerate(hz):
        column(i * 50, 370, random.randrange(30, 350))
        canvas.create_text(i * 50 + 35, 390, text=j, fill='green')
    canvas.update()
    canvas.after(100)
    canvas.delete('all')
canvas.mainloop()
'''
import tkinter, random
canvas = tkinter.Canvas(width= 515, height= 400)
canvas.pack()
'''
words = ['PYTHON','Tuple','Keys','Strip','Shuffhe','Close','Input',]


with open("tajnicka.txt", 'w', encoding='UTF8') as file:
    for i in words:
        file.writelines(i + '\n')
'''
with open("tajnicka.txt", encoding='UTF8') as file:
    words = [x.strip() for x in file]
def square(x, y, a, letter = ' '):
    canvas.create_rectangle(x, y, x+a, y+a)
    canvas.create_text(x + a/2, y + a/2, text= str(letter))

for word in words:
    for 
canvas.mainloop()
