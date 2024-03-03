
import tkinter, math
canvas = tkinter.Canvas(width=800, height=800)
canvas.pack()
r1 = 75
r2 = 125
def clock(minutes, seconds):
    canvas.create_rectangle(175, 30, 325, 90, width=5)
    canvas.create_oval(100, 100, 400, 400, width= 5)
    canvas.create_text(250, 60, text=f'{minutes:02d}:{seconds:02d}', font='arial 20')
    canvas.create_line(250, 250,
    250 + r1 * math.cos(-math.pi/2 + math.radians(6*minutes)),
    250 + r1 * math.sin(-math.pi/2 + math.radians(6*minutes)),
    fill='red',
    width=4)
    canvas.create_line(250, 250,
    250 + r2 * math.cos(-math.pi/2 + math.radians(6*seconds)),
    250 + r2 * math.sin(-math.pi/2 + math.radians(6*seconds)),
    width=4)



start = 3
minutes = start
seconds = 0
active = True
while active:
    clock(minutes, seconds)
    canvas.update()
    canvas.after(200)
    if minutes == 0 and seconds == 0:
        canvas.create_text(250, 450, text='dobru chut')
        active=False
    else:
        canvas.create_rectangle(0, 0, 800, 800, width = 0, fill='white')
    seconds -=1
    if seconds < 0:
        seconds = 59
        minutes -= 1


canvas.mainloop()
'''
import tkinter, math

canvas= tkinter.Canvas(width=800, height= 800)
canvas.pack()
r_hod= 125
r_sek= 100
r_min= 50
j= 0
def hodiny(minuty,sekundy):
    canvas.create_oval(400-r_hod,400-r_hod,400+r_hod, 400+r_hod, width=5)
    canvas.create_rectangle(350,215,450,265)
    canvas.create_text(400,245, text= f"{minuty:02d}:{sekundy:02d}",font="Arial 20")
    global j
    x_m= 400 + r_min * math.cos(math.radians((360/60) * j))
    y_m= 400 + r_min * math.sin(math.radians((360/60) * j))
    canvas.create_line(400,400,x_m,y_m,fill="red", tag= "minutova")
    j= j+1
    for i in range(60):
        x_s= 400 + r_sek * math.cos(math.radians((360/60) * i))
        y_s= 400 + r_sek * math.sin(math.radians((360/60) * i))
        canvas.create_line(400,400,x_s,y_s, tag= "sekundova")
        canvas.update()
        canvas.after(100)
        canvas.delete("sekundova")
        
    canvas.delete("minutova")
        
start= 2
minuty= start
sekundy= 0
active= True
while active:
    hodiny(minuty,sekundy)
    canvas.update()
    canvas.after(1000)
    if minuty == 0 and sekundy == 0 :
        canvas.create_text(400,550, text= "help")
        active= False
    else:
        sekundy = sekundy-1
        if sekundy<0:
            sekundy= 59
            minuty= minuty-1
'''
