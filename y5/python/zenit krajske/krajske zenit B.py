rows, columns = map(int, input().split())
characters = input().split()
output = ""

for column in range(columns):
    numbers = input()
    for number in numbers:
        if number == '.':
            output += number
        else:
            output += characters[(int(number) - 1) % 9]
    
    if column != columns - 1:
        output += "\n"

print(output)
