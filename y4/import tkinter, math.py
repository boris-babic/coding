import tkinter, math
canvas = tkinter.Canvas(width= 1200, height= 700)
canvas.pack()

side = 70
def triangle(x, y, counter):
    canvas.create_polygon(x - side/2, y - math.sqrt(3)/4*side,
                          x + side/2, y - math.sqrt(3)/4*side,
                          x, y + math.sqrt(3)/4*side,
                          fill='red',)
    canvas.create_text(x, y, text=counter)
def sumtriangle(x, y, row, column):
    canvas.create_polygon(x - side/2, y + math.sqrt(3)/4*side,
                          x + side/2, y + math.sqrt(3)/4*side,
                          x, y - math.sqrt(3)/4*side,
                          fill='blue',)
    canvas.create_text(x, y, text=counter)
n = 10
y = side
counter = 0
for i in range(1,n+1):
    counter += i

base = counter
for i in range(n):
    x = side + i*side/2 + 50
    for j in range(n-i):
        triangle(x, y, counter)
        x += side
        counter -=1
    x = side + i*side/2 + 50 + side/2
    for k in range(n-i-1):
        sumtriangle(x, y, i, j)
        x += side
    y += math.sqrt(3)/2*side

base -(n +  + j)









canvas.mainloop()
