import random

number = input()
input = input()
order = input.replace(' ', '')
list =[i for i in order]
active = True
copy = list
while True:
    random.shuffle(copy)
    if copy != list:
        break
    if number == 1:
        break
if copy == list:
    print('Janka bude frflat')
else:
    print(*copy)