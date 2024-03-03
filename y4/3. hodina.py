'''
slovo = input ('Zadaj slovo:')
n = int(input ('Zadaj n:'))
for i in reversed(range(n)):
    print ('.' * i + slovo)
'''
'''
slovo = input ('Zadaj slovo:')
n = int(input ('Zadaj n:'))
for i in range(n):
    print ((slovo+' ') * (i+1))
'''
od = int(input('od'))
do = int(input('do'))
all = ''
for i in range(od, do+1):
    all += str(i)+' '+str(i**2)+' '+str(i**3)+'\n'    

print (all,)