'''
#8-3
def make_shirt(size = 'Extra large', text = 'Who is in paris?'):
    print(f'You have ordered {size.lower()} sized T-shirt with text: {text.lower()}')

make_shirt('Medium', 'I love python')
make_shirt(size= 'Large', text='I hate python')
make_shirt()

#8-7
def make_album(name, title, number=None):
    if number:
        album = {
            'Artists name: '               : name,
            'Title of the album: '         : title,
            'Number of songs on the album' : number,
        }
    else:
        album = {
            'Artists name: '       : name,
            'Title of the album: ' : title,
        }
    return album

active = True
while active:
    name = input('Gimme the name of the author: ')
    title = input('Gimme the title: ')
    answer = input('Do you know the number of songs? If you want to quit press q ').lower()
    if answer == 'yes':
        number = input('How many then ')
        print(make_album(name, title, number))
    elif answer == 'no':
        print(make_album(name, title))
    elif answer == 'q':
        active = False
#8-8
def send_messages(messages):
    while messages:
        current = messages.pop()
        print(current)
        sent_messages.append(current)

messages = ['Hello there', 'Whos in paris', 'What da dog doing']
sent_messages = []
send_messages(messages)

print(messages, sent_messages)

#8-12
def make_sandwich(*items):
    print(f'You have ordered {items} on your sandwich')
    for i in items:
        print(f'Adding {i} on your sandwich')

make_sandwich('cheese')
make_sandwich('tomato', 'tuna')
make_sandwich('salmon', 'bacon', 'olives')
8-13
def build_profile(first, last, **user):
    user['first name'] = first
    user['last name']  = last
    return user

me = build_profile('Boris', 'Babic', looking ='hot', job = 'F1 driver', )
print(me)
'''
#8-14
def make_car(manufacturer, model, **parameters):
    parameters['Manufacturer'] = manufacturer
    parameters['Model name'] = model
    return parameters
my_car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(my_car)  