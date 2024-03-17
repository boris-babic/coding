import tkinter, random
screen_width, screen_height = 800, 800
canvas = tkinter.Canvas(width=screen_width, height=screen_height)
canvas.pack()

og = ['jablko', 'programovanie', 'koleso', 'uloha', 'riesenie'] 
slova = og[:]
speed = 5
def word(x, y, t):
    canvas.delete('all')
    canvas.create_text(x, y, text=t)

def keypress(event):
    global slovo, displayed
    for i in range(len(slovo)):
        if event.keysym == slovo[i]:
            displayed = displayed[:i]+ event.keysym + displayed[i+1:]
    print(event.char)

def start(event):
    global slovo, x, y, displayed, game_going
    canvas.delete('all')
    game_going = True
    slova = og[:]
    slovo = slova.pop(random.randrange(len(slova)))
    displayed = '*' * len(slovo)
    x, y = random.randrange(200, screen_width-200), 50
    timer()

def timer():
    global slovo, x, y, displayed, game_going
    word(x, y, displayed)
    y +=2
    solved = True
    for char in displayed:
        if char == '*':
            solved = False
            break
    if solved:
        try:
            print(slova, slovo)
            slovo = slova.pop(random.randrange(len(slova)))
            displayed = '*' * len(slovo)
            y = 50
        except ValueError:
            game_going = False
            result = 'Game Won'
    if y + 20 > screen_height:
        game_going = False
        result = 'Game Lost'
    if game_going == True:
        canvas.after(100, timer)
    else:
        canvas.create_text(screen_width/2, screen_height/2, text=result)

canvas.bind('<Button-1>', start)
canvas.bind_all('<Key>', keypress)
canvas.mainloop()