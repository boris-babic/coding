'''
x = 'aaa'
y = 'bbb'
z = 'ccc'

for i in x, y, z:
    for j in x, y, z:
        print (i, j)
'''
'''
n = 5

for i in range(1, n+1):
    for j in range (n):
        print(i+j*n, '', end='')
    print('')
'''
'''
for n in range (1, 11):
    y = n
    x = n
    for i in range (int(n-1), 0, -1):
        x = str(x) + '*' + str(i)
        y = y*i
    print(str(n) + '! = ', x, '=', y)
'''
n = 5

for i in range (n+1, 1, -1):
    print(' '*(n-i+1), end = '')
    for j in range(1,i):
        print (j, end =' ')
    print('')

