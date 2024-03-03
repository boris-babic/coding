import tkinter
canvas= tkinter.Canvas(width=800, height= 800)
canvas.pack()

def pocet_delitelov(n):
    pocet= 0
    for i in range(1, n+1):
        if n%i == 0:
            pocet += 1
    return pocet
def prvocislo(cislo):
    if pocet_delitelov(cislo)== 2:
        return True
    return False
 
def kresli(co_kreslim,y):
    canvas.create_text(400,y, text= co_kreslim )
    
def cisla(original_cislo,kolko):
    canvas.create_text(400,400, text= original_cislo)
    pocet= 0

    while pocet < kolko:
        vacsie_cislo= original_cislo + 1
        if prvocislo(vacsie_cislo):
            kresli(vacsie_cislo,(400-(pocet+1)*25))
            pocet = pocet + 1
    pocet= 0

    while pocet < kolko:
        mensie_cislo= original_cislo - 1
        if prvocislo(mensie_cislo):
            kresli(mensie_cislo,(400+(pocet+1)*25))
            pocet = pocet + 1   
        mensie_cislo = mensie_cislo - 1 

cisla(100,3)
canvas.mainloop()

'''
import tkinter
canvas = tkinter.Canvas(width=300, height=800)
canvas.pack()
def is_prime(number):
    count = 0
    for i in range(1, number+1):
        if number % i ==0:
            count += 1
    if count <= 2:
        return True

def draw(number, y):
        canvas.create_text(150, y, text=number , font='Arial 20')

def get_numbers(start, amount):
    lower, upper = 0, 0
    ln = start
    hn = start
    count = 0
    while lower < amount:
        ln -= 1
        if is_prime(ln):
            lower += 1
            count +=1
            draw(ln, 400 - count * 25)
    draw(start, 400)
    count = 0
    while upper < amount:
        hn += 1
        if is_prime(hn):
            upper += 1
            count +=1
            draw(hn, 400 + count * 25)



    

get_numbers(100, 3)
canvas.mainloop()

#resolution of the final frame
wide=1920 
tall=1080

import tkinter, random, math
canvas = tkinter.Canvas(width= wide, height=tall)
canvas.pack()
#centre of axis of rotation
xcentre= wide / 2
ycentre= 1500

radius = math.sqrt(xcentre ** 2 + ycentre ** 2)#radius of the sky
planet_radius = ycentre - 70 #radius of planets
size = 30 #size of the planets
tree = tkinter.PhotoImage(file='strom1.png')
hours = 60 #how many photos are in the animation (for better preformance lower the number)
multiple = 360 / hours #to simplify modification of hours

def anime(angle):
    #drawing everything
    sky(angle)
    canvas.create_rectangle(0, tall - 100, wide, tall, fill='green', outline='green')#grass
    canvas.create_image(wide - 320, tall -320, image= tree)
    canvas.update()
    canvas.after(10)
    canvas.create_rectangle(0, 0, wide, tall, fill='white', outline= 'white') #refreshing the window

def sky(angle):
    #drawing the background with sun and moon on top
    background(angle)
    sun(angle)
    moon(angle)

def background(angle):
    for i in range(0, 180, 2): #2 represents how many lines will be drawn(in this case 180/2=90 lines), increase the number for better performance
        y1= ycentre + radius * math.sin(math.radians(angle * multiple + i))
        y2= ycentre + radius * math.sin(math.radians(angle * multiple - i))
        if y1 < (tall-90) or y2 < (tall-90): #for optimization (a bit)
            x1= xcentre + radius * math.cos(math.radians(angle * multiple + i))
            x2= xcentre + radius * math.cos(math.radians(angle * multiple - i))
            canvas.create_line(x1, y1, x2, y2, fill=f'#0000{(10 + i):02x}', width= 150)


def moon(angle):
    #basic stuff
    canvas.create_oval(
        xcentre + planet_radius * math.cos(math.radians(angle * multiple)) + size,
        ycentre + planet_radius * math.sin(math.radians(angle * multiple)) + size,
        xcentre + planet_radius * math.cos(math.radians(angle * multiple)) - size,
        ycentre + planet_radius * math.sin(math.radians(angle * multiple)) - size,
        fill='white',
        outline='white'
    )

def sun(angle):
    #adding 180 so its opposite of the moon
    canvas.create_oval(
        xcentre + planet_radius * math.cos(math.radians(180 + angle * multiple)) + size,
        ycentre + planet_radius * math.sin(math.radians(180 + angle * multiple)) + size,
        xcentre + planet_radius * math.cos(math.radians(180 + angle * multiple)) - size,
        ycentre + planet_radius * math.sin(math.radians(180 + angle * multiple)) - size,
        fill='yellow',
        outline='yellow'
    )
#main body
while True:
    for i in range(hours):
        anime(i)


canvas.mainloop()
'''
