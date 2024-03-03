import tkinter, math
canvas = tkinter.Canvas(width = 1920, height = 1080)
canvas.pack()

number_of_rays    = 14
long_rays_radius  = 100
short_rays_radius = 80
radius_of_sun     = 60 #radius of sun without the rays, radius of "valleys"
x_of_center       = 500
y_of_center       = 500
points            = [] #here will be the points of the sun
base_angle        = 180 // number_of_rays #angle between valleys and ray.Because valleys are between rays, angle between them is 1/2
counter           = 0 #for the cycle between long and short rays
radii             = [long_rays_radius, short_rays_radius] #also to cycle between them

for angle in range(0, 360, round(360/number_of_rays)):
    counter += 1
    #we will get the coordinates of rays here
    x_coordinate = radii[counter % 2] * math.cos(math.radians(angle)) + x_of_center
    y_coordinate = radii[counter % 2] * math.sin(math.radians(angle)) + y_of_center
    point = (int(x_coordinate), int(y_coordinate)) 
    points.append(point) 

    #we will get the coordinates of "valleys" here, we add base angle so that it won't have the same angle as ray created above
    x_coordinate = radius_of_sun * math.cos(math.radians(angle + base_angle)) + x_of_center
    y_coordinate = radius_of_sun * math.sin(math.radians(angle + base_angle)) + y_of_center
    point = (int(x_coordinate), int(y_coordinate))
    points.append(point)

canvas.create_polygon(points, fill= 'yellow', width= 2, outline='orange')

canvas.mainloop()