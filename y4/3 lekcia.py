import tkinter, math
canvas = tkinter.Canvas(width= 1920, height= 1080)
canvas.pack()

pocet = 12
x_center, y_center = 400, 400
radius = 100
ray_radius = 150
ray_radius2 = 200
uhol = int(360 / pocet)
tocit = uhol /2

for i in range(0, 360, uhol):
    x1 = radius * math.cos(math.radians(i)) + x_center
    y1 = radius * math.sin(math.radians(i)) + y_center
    x2 = ray_radius * math.cos(math.radians(i + tocit)) + x_center
    y2 = ray_radius * math.sin(math.radians(i + tocit)) + y_center
    x3 = radius * math.cos(math.radians(i + tocit + tocit)) + x_center
    y3 = radius * math.sin(math.radians(i + tocit + tocit)) + y_center
    canvas.create_polygon(x1, y1, x2, y2, x3, y3)
    ray_radius, ray_radius2 = ray_radius2, ray_radius
    
canvas.create_oval(x_center - radius, y_center - radius, x_center + radius, y_center + radius, fill='yellow')
canvas.mainloop()