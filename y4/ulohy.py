'''
slovo = 'jablko'
a = 1
f = ''
for i in slovo:
    f += str(a) + str(i)
    a += 1
print (f)
'''
'''
x = 0
n = int(input('Zadaj cislo: '))
for i in range(n):
    x = i % 7
    print (x, end = ' ')
'''
'''
c1 = 'blue'
c2 = 'red'
for i in range (10):
    if i % 2 == 0:
        print (c1)
    else:
        print (c2) 
'''
'''
n = int(input('Zadaj pocet cisel: '))
x = 0
for i in range (n):
    x += float(input ('Zadaj cislo: '))
print('')
print('Sucet je: ', x)
print('Priemer je: ', x/n)
'''
