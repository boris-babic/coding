
#turn rectangle into axes
def rectangulate(x, y, width, height):
     if y == 0:
          return int(x)
     elif x == width:
          return int(width + y)
     elif y == height:
          return int(width + height + width -x)
     else:
          return int(width + height + width + height - y)
def midpoints(devices):
    midpoint = int(len(devices)/2)
    for i in range(len(devices)-1):
        if  devices[i][1] == devices[i+1][1]:
            midpoint = i
            break
    return int(midpoint)


def wrap_around_access(list, index):
    if len(list) == 0:
        return None  # Handle an empty list

    # Calculate the wrapped index
    wrapped_index = index % len(list)

    # Handle negative indices
    if wrapped_index < 0:
        wrapped_index += len(list)

    # Access the element using the wrapped index
    return list[wrapped_index]


results = []
with open('y5/python/input.txt') as file:
        t = file.readline()
        for i in range(int(t)):
            #loop for each room
            h, w, n = file.readline().split()
            h, w, n = int(h), int(w), int(n)
            devices = []
            for i in range(n):
                #for each device
                x, y, c = file.readline().split()
                x, y= int(x), int(y)
                index = rectangulate(int(x), int(y), int(w), int(h))
                device = (index, c)
                devices.append(device)
            devices.sort(key=lambda x:x[0])
            midpoint = midpoints(devices)
            if len(devices)%2 == 0:
                possible = 1
                for i in range(int(len(devices)/2)):
                    right_device = wrap_around_access(devices, (midpoint+i+1))
                    left_device = wrap_around_access(devices, (midpoint-i))
                    if right_device[1] != left_device[1]:
                        possible = 0
            else:
                possible = 0
            if possible:
                results.append('pujde to')
            else:
                results.append('ajajaj')

with open('y5/python/output.txt', 'w') as file:
     for result in results:
          file.writelines(result + '\n')

