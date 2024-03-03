host = ['ja', 'ty', 'on']
for i in range (3):
    print (f'Cau {host[i]} pozyvam ta') 

print (f'{host[2]} nemoze prist')
del host[2]
host.append('ona')

for i in range (3):
    print (f'Cau {host[i]} pozyvam ta')

print ('Hey mam vacsi stol')
host.insert (0, 'tvoja mama')
host.append ('tvoj tatko')
n = len(host)

for i in range (5):
    print (f'Cau {host[i]} si pozvany')

print(f'Je pozvanych {n} ludi')
print('I can only invite 2 people')
host.pop(0)

locations = ['london', 'paris', 'kyiv', 'long beach', 'compton']

print(sorted(locations))
print(locations)

print(sorted(locations, reverse=True))
print(locations)
