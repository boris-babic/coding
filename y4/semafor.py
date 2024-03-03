import tkinter
canvas = tkinter.Canvas(width=700, height=700)
canvas.pack()
delay = 1000
def greenlight(counter):
    canvas.create_rectangle(100, 100, 250, 500, fill='black')
    canvas.create_oval(125, 125, 225, 225, fill='gray')
    canvas.create_oval(125, 250, 225, 350, fill='gray')
    canvas.create_oval(125, 375, 225, 475, fill='green')
    canvas.create_text(175, 425, text = counter, fill= 'white', font='Arial 20')
    canvas.update()
    canvas.after(delay)
def orangelight():
    canvas.create_rectangle(100, 100, 250, 500, fill='black')
    canvas.create_oval(125, 125, 225, 225, fill='gray')
    canvas.create_oval(125, 250, 225, 350, fill='orange')
    canvas.create_oval(125, 375, 225, 475, fill='gray')
    canvas.update()
    canvas.after(delay)
def redlight(counter):
    canvas.create_rectangle(100, 100, 250, 500, fill='black')
    canvas.create_oval(125, 125, 225, 225, fill='red')
    if counter == 1:
        canvas.create_oval(125, 250, 225, 350, fill='orange')
    else:
        canvas.create_oval(125, 250, 225, 350, fill='gray')
    canvas.create_oval(125, 375, 225, 475, fill='gray')
    canvas.create_text(175, 175, text = counter, fill= 'white', font='Arial 20')
    canvas.update()
    canvas.after(delay)

def light():
    while True:
        for i in reversed(range(1, 6)):
            greenlight(i)
        orangelight()
        for i in reversed(range(1, 6)):
            redlight(i)

light()
canvas.mainloop()
