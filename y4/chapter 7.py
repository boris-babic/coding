'''
active = True
cost = 0
while active == True:
    age = input('Enter your age: ')
    if  int(age) < 3:
        print('Its free for children')
    elif int(age) < 12:
        print('This ticket will cost you 10 bucks')
        cost += 10
    elif int(age) >= 12:
        print('This ticket will cost you 15 bucks')
        cost += 15
    stop = input('Is that all? ').lower()
    if stop == 'yes':
        active = False
print(f'Your total is {cost} dollars')
'''
#7-8, 7-9
orders = [
    'tuna sandwich',
    'salami sandwich',
    'egg sandwich',
    'salami sandwich',
    'salmon sandwich',
    'salami sandwich',
    'salami sandwich',
    ]
finished = []

print('Sorry we dont have salami')
while 'salami sandwich' in orders:
    orders.remove('salami sandwich') 

while orders:
    current_sandwich = orders.pop()
    finished.append(current_sandwich)
    print(f'Now im working on {current_sandwich}')
print('We have made ', *finished)