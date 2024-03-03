'''
#5-1
car = 'bmw'
print(car.lower() =='BMW'.lower())

#5-5
alien_colour = ['green', 'red', 'blue']
for i in range(3):
    if alien_colour[i] == 'green':
        print(f'You killed {alien_colour[i]} alien and you earned 5 points')
    elif alien_colour[i] == 'red':
        print(f'You killed {alien_colour[i]} alien and you earned 10 points')
    elif alien_colour[i] == 'blue':
        print(f'You killed {alien_colour[i]} alien and you earned 20 points')
#5-6
for i in range(1, 80):
    if i < 2:
        print(f'A person {i} years old is a baby')
    elif i < 4:
        print(f'A person {i} years old is a toddler')
    elif i < 13:
        print(f'A person {i} years old is a kid')
    elif i < 20:
        print(f'A person {i} years old is a teenager')
    elif i < 65:
        print(f'A person {i} years old is an adult')
    elif i >= 65:
        print(f'A person {i} years old is an elder')
'''
'''
#5-8,5-9
usernames = [
            'admin',
            'bobo', 
            'zlatan', 
            'zuzka',
            'meggy'
            ]

if usernames:
    for i in usernames:
        if i == 'admin':
            print('Hello admin, go fuck yourself')
        else:
            print(f'Hello {i}')
else:
    print('Add some users')
'''
'''
current_users = [
'Boris',
'Meggy',
'Zuzka',
'Sima',
'Tabita',
]
new_users =  [
'NinkA',
'Ema',
'Lucka',
'Sima',
'zUzka',
]
for i in range(len(current_users)):
    current_users[i]= current_users[i].lower()
for i in range(len(new_users)):
    new_users[i]= new_users[i].lower()

for i in range(len(new_users)):
    if new_users[i] in current_users:
        print(f'Meno {new_users[i]} je uz zobrane')
    else:
        print(f'Meno {new_users[i]} je k dispozicii')
'''
list = [i for i in range(1, 10)]
for i in range(1,len(list)+1):
    if   i == 1:
        print('1st')
    elif i == 2:
        print('2nd')
    elif i == 3:
        print('3rd')
    else:
        print(f'{i}th')

         