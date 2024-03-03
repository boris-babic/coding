n = int(input())
letters = []
for i in range(n):
    word = input()
    for j, k in enumerate(word):
        letter = (i, j, k)
        letters.append(letter)

print(letters)

def next_step(x, y, direction):
    if direction == 1:
        value = (x, y-1)
    if direction == 2:
        value = (x+1, y-1)
    if direction == 3:
        value = (x+1, y)
    if direction == 4:
        value = (x+1, y+1)
    if direction == 5:
        value = (x, y+1)
    if direction == 6:
        value = (x-1, y+1)
    if direction == 7:
        value = (x-1, y)
    if direction == 8:
        value = (x-1, y-1)
    return value

for x, y, letter in letters:
    if letter == 'Z':
        for direction in range(1, 9):
            next_x, next_y = next_step(x, y, direction)
            result = list(filter(lambda a:a[0]==next_x and a[1]==next_y, letters))
            if result[2] == 'E':
                print('jes')