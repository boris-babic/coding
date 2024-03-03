import tkinter, random, math
canvas = tkinter.Canvas(width= 700, height= 500,)
canvas.pack()

#1
x_red  = 50 #upper left corner of the first square
y_red  = 50 
side   = 100
middle_point = side/2 #for text
x_blue = x_red + side + 10 
y_blue = y_red 
#dont worry that its in multiple lines, its purely esthetic
#and doesnt change the function of the program,
#each parameter or value or tag or whatever is in its own line
canvas.create_rectangle(x_red,
                        y_red,
                        x_red + side,
                        y_red + side,
                        fill='red')
canvas.create_text(x_red + middle_point,
                   y_red + middle_point,
                   text='red',
                   font='arial 20',
                   fill='yellow')

canvas.create_rectangle(x_blue,
                        y_blue,
                        x_blue + side,
                        y_blue + side,
                        fill='blue')
canvas.create_text(x_blue + middle_point,
                   y_blue + middle_point,
                   text='blue',
                   font='arial 20',
                   fill='yellow')
#end of 1

#2
#put background='navy' into the tkinter.Canvas brackets
number_of_stars = 200
for star in range(number_of_stars):
    canvas.create_text(random.randrange(500),
                       random.randrange(500),
                       text='*',
                       font=f'arial {random.randrange(10, 21)}',
                       fill='yellow')
#end of 2

#3
x_bigger_square     = 50
y_bigger_square     = 50
side_bigger_square  = 180
side_smaller_square = 100
x_middle            = x_bigger_square + side_bigger_square/2
y_middle            = y_bigger_square + side_bigger_square/2


canvas.create_rectangle(x_bigger_square,
                        y_bigger_square,
                        x_bigger_square + side_bigger_square,
                        y_bigger_square + side_bigger_square,
                        fill='indian red')
canvas.create_rectangle(x_middle - side_smaller_square/2,
                        y_middle - side_smaller_square/2,
                        x_middle + side_smaller_square/2,
                        y_middle + side_smaller_square/2,
                        fill='light blue')
#points ABCD
canvas.create_text(x_bigger_square - 10,
                   y_bigger_square -10,
                   text='A')
canvas.create_text(x_bigger_square + side_bigger_square + 10,
                   y_bigger_square -10,
                   text='B')
canvas.create_text(x_bigger_square + side_bigger_square + 10,
                   y_bigger_square + side_bigger_square + 10,
                   text='C')
canvas.create_text(x_bigger_square - 10,
                   y_bigger_square + side_bigger_square + 10,
                   text='D')
#length of sides
canvas.create_text(x_bigger_square + side_bigger_square + 10,
                   y_middle,
                   text=side_bigger_square)
canvas.create_text(x_middle,
                   y_middle + side_smaller_square/2 - 10,
                   text=side_smaller_square)
#end of 3

#4
number_of_squares = 20
x_middle          = 250 
y_middle          = 250
side              = 20 #side je aka bude vzdialenost medzi stvorcami
red = 'red'
blue = 'blue'
yellow = 'yellow'
for current_side in reversed(range(number_of_squares)):
    current_side *= side / 2 #/2 kvoli tomu ze zacinam od stredu
    canvas.create_rectangle(x_middle - current_side,
                            y_middle - current_side,
                            x_middle + current_side,
                            y_middle + current_side,
                            fill=red)
    red, blue, yellow = blue, yellow, red
#end of 4

#5
x_side = 135
y_side = 90 

#nemecko
x_left  = 10
x_right = 10 + x_side
canvas.create_rectangle(x_left,
                        10,
                        x_right,
                        10 + y_side,
                        fill='yellow')
canvas.create_rectangle(x_left,
                        10,
                        x_right,
                        10 + y_side*2/3,
                        fill='red',
                        outline='')
canvas.create_rectangle(x_left,
                        10 ,
                        x_right,
                        10 + y_side/3,
                        fill='black')
#reverse order so we wont have a border between yellow and red,
# red will simply hide the rest of yellow

#taliansko
y_top = 10
y_bot = 10 + y_side

canvas.create_rectangle(200,y_top, 200 + x_side, y_bot, fill= 'white')
canvas.create_rectangle(200, y_top, 200 + x_side / 3, y_bot, fill='green', outline='')
canvas.create_rectangle(200 + x_side * 2 / 3, y_top, 200 + x_side , y_bot, fill='red', outline='')
#this order is once again because of outlines

#francuzsko
y_top = 150
y_bot = 150 + y_side

canvas.create_rectangle(10, y_top, 10 + x_side, y_bot, fill= 'white')
canvas.create_rectangle(10, y_top, 10 + x_side / 3, y_bot, fill='blue', outline='')
canvas.create_rectangle(10 + x_side * 2 / 3, y_top, 10 + x_side , y_bot, fill='red', outline='')

#ukraina 
x_left  = 200
x_right = 200 + x_side
canvas.create_rectangle(x_left, 150, x_right, 150 + y_side, fill='blue')
canvas.create_rectangle(x_left + 1, 150 + y_side / 2, x_right, 150 + y_side, fill='yellow', outline='')
#+ 1 lebo mi to neukazovalo lavy border ale nechapem preco
#end of 5

#6
#idk why i draw it from the bottom up
height = 50
middle = 180
offset = 100 #width of the rectangle measured from the middle
base_y = 250
for colour in 'light green', 'olive', 'green', 'dark green':
    canvas.create_rectangle(middle - offset, base_y , middle + offset, base_y + height, fill=colour)
    base_y -= height
    offset -= 25
#end of 6

#7
x, y = 10, 100
d = 20
n = 16
for i in range(n):
    if y == 100: #if we are on the top we add the difference
        x1 = x + d
        y1 = y + d
        canvas.create_line(x, y, x1, y1, width= 5, fill='blue')
    else: #if we are on the bottom we subtract
        x1 = x + d
        y1 = y - d
        canvas.create_line(x, y, x1, y1, width= 5, fill='blue')
    x = x1 #set the starting point of the new line to the end of the last
    y = y1
#end of 7

#8
x, y = 70, 100
r = 50
dx, dy = 120, 60


for color in 'blue', 'yellow', 'black', 'green', 'red':
    canvas.create_oval(x - r, y - r, x + r, y + r, width=15, outline=color)
    if y == 100: #here we check if we were in the top row or the bottom, if top we move down, else we move up
        x += dx/2 #we divide it by 2 because the bottom rings are exactly in the middle
        y += dy
    else:
        x += dx/2
        y -= dy
#end of 8

#9
sum = 0
n = 9
height = 20
y = 20 #starting point
for i in range(n):
    value = random.choice((1, 2, 5, 10, 20, 50))
    canvas.create_text(125, y + height/2, text=f'{value} €')
    canvas.create_rectangle(100, y, 150, y + height)
    y += height
    sum += value
canvas.create_text(200, 100, text=f'spolu = {sum} €')
#end of 9


#10
n = 30
r = 20
for i in range(n):
    x = random.randrange(20, 480)
    y = random.randrange(20, 480)
    value = random.randrange(1, 10)
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=f'#{random.randrange(256**3):06x}')
#type of formating of the color (above)
    canvas.create_text(x, y, text=value, font='arial 30')
#end of 10

#11
input = str(input('Zadaj text: ')).upper()
x , y = 30, 100
dx , dy = 30, 30

for letter in input:
    text_color   = f'#{random.randrange(256**3):06x}'
    square_color = f'#{random.randrange(256**3):06x}'
    canvas.create_rectangle(x - dx/2, y - dx/2, x + dx/2, y + dy/2, fill= square_color)
    canvas.create_text(x, y, text=letter, font='arial 26', fill=text_color)
    x += dx
#end of 11

#12
n = 7
x = 10
max_x = 380
spacing = 5
#here ill calculate the side of the rectangle a 
#n = 380/(a + 5) 
#n(a+5) = 380
#a+5 = 380/n
a = 380/n+5
for i in range(n):
    canvas.create_rectangle(x, 20, x + a, 20 + a, fill=f'#{random.randrange(256**3):06x}')
    x += a + 5
#end of 12

#13
x, y = 50, 250
a = 280
#because its equilateral the internal angle will be 60 degrees
x1 = x + a * math.cos(math.pi/3) #60 degrees in radians is pi/3
y1 = y - a * math.sin(math.pi/3)
canvas.create_polygon(x, y, x + a, y, x1, y1, fill='blue')
#end of 13

#14
n = 20

for i in range(n):
    a = random.randrange(10, 51)
    x = random.randrange(10, 450) #x of left bottom corner of the roof
    y = random.randrange(30, 450) #y of left bottom corner of the roof

    x1 = x + a * math.cos(math.pi/3)
    y1 = y - a * math.sin(math.pi/3)
    color = f'#{random.randrange(256**3):06x}'
    canvas.create_polygon(x, y, x + a, y, x1, y1, fill=color)
    color = f'#{random.randrange(256**3):06x}'
    canvas.create_rectangle(x, y, x + a, y + a, fill=color, outline=color)
#end of 14

#15
width, height = 300, 200
x_middle, y_middle = width / 2, height / 2
x, y = 50, 20
canvas.create_rectangle(x, y, x + width, y + height, fill='white')
canvas.create_rectangle(x, y + y_middle, x + width, y + height, fill='red')
canvas.create_polygon(x, y, x, y + height,x + x_middle, y + y_middle, fill='navy', outline='blue')
#end of 15

#16
side = 30
spacing = 3
x, y = 10, 10
columns = 8
rows = 4
for row in range(rows):
    if row %2 == 0: #here we check if we are in an even or odd row and pick our startin colors accordingly
        color1, color2 = 'maroon', 'gold' #here we are in even row, so we start with maroon color
    else:
        color1, color2 = 'gold', 'maroon' #here we are in odd row, so we start with gold color

    for column in range(columns):
        canvas.create_rectangle(x, y, x + side, y + side, fill=color1)
        x += side + spacing
        color1, color2 = color2, color1
    y += side + spacing
    x = 10 #we move back to the begining
#end of 16

#17
x, y = 10, 10
for square in range(25):
    color = f'#{(255 - 10 * square):02x}' + '00' + f'{(10 * square):02x}'
    canvas.create_rectangle(x + 15 * square, y, x + 15 * square + 15, y + 250, fill=color, width=0)
#end of 17

#18
x, y = 300, 250
n = 7
a = 200
base_angle = 360 / n #angle between 2 points
radius = a / (2 * math.sin(math.radians(base_angle/2)))
#you can find the formula here https://www.mathopenref.com/polygonradius.html
for point in range(n):
    x1 = x + radius * math.cos(math.radians(base_angle * point))
    y1 = y + radius * math.sin(math.radians(base_angle * point))
    x2 = x + radius * math.cos(math.radians(base_angle * point + base_angle))
    y2 = y + radius * math.sin(math.radians(base_angle * point + base_angle))
    canvas.create_line(x1, y1, x2, y2, width= 3)

#end of 18

#19
x, y = 300, 250
n = 9
radius = 125
base_angle = 360 / n #angle between 2 points

for point in range(n):
    #point represents the number of the point from the origin
    #think of it as on clock - you start at 1 and then you have 2 etc
    #and that is the value of point
    x1 = x + radius * math.cos(math.radians(base_angle * point))
    y1 = y + radius * math.sin(math.radians(base_angle * point))
    #you multiply point by base angle becasue point tells you how many points you have to jump
    #and base angle tells us the angle between 2 points
    #you can see it on the clock - when you move from 3 to 6 you move 3 hours clockwise
    #the angle between 1 hour is 30 degrees so you moved 30 * 3 = 90 degrees
    x2 = x + radius * math.cos(math.radians(base_angle * point + base_angle))
    y2 = y + radius * math.sin(math.radians(base_angle * point + base_angle))
    canvas.create_line(x1, y1, x2, y2, width= 3)
    for diagonal in range(point, n):
        x3 = x + radius * math.cos(math.radians(base_angle * diagonal))
        y3 = y + radius * math.sin(math.radians(base_angle * diagonal))
        canvas.create_line(x1, y1, x3, y3)

#end of 19

#20
x, y = 350, 250
n = 12
radius = 100
small_radius = 2 * radius * math.sin(math.radians(180/(2 * n)))
#small radius is the radius of the small circles
#because the center of them and the contact points lies on the bigger circle
#you can get a regular polygon that has 2n sides that are small radius long
#formula for it is here https://www.mathopenref.com/polygonsides.html
base_angle = 360 / n
for point in range(n):
    color = f'#{random.randrange(255 ** 3):06x}'
    x1 = x + radius * math.cos(math.radians(base_angle * point))
    y1 = y + radius * math.sin(math.radians(base_angle * point))
    canvas.create_oval(x1 - small_radius,
                       y1 - small_radius,
                       x1 + small_radius,
                       y1 + small_radius,
                       fill= color)
#end of 20

#21
x, y = 30, 30
width, height = 325, 216
blue, red = '#0b4ea2', '#ee1c25'
coat_of_arms = tkinter.PhotoImage(file='sk.png')
canvas.create_rectangle(x, y, x + width, y + height, fill='white')
canvas.create_rectangle(x,
                        y + 1/3*height,
                        x + width,
                        y + 2/3*height,
                        fill=blue,
                        width = 0)
canvas.create_rectangle(x,
                        y + 2/3*height,
                        x + width,
                        y + height,
                        fill=red,
                        width = 0)
canvas.create_image(x + 100, y + 108, image=coat_of_arms)
#end of 21

canvas.mainloop()