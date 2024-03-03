import math

print ('Zadaj strany trojuholnika')
a= float(input('Strana a='))
b= float(input('Strana b='))
c= float(input('Strana c='))
strany =  [a, b, c]
strany.sort()

a = strany [0]
b = strany [1]
c = strany [2]

x = a + b
y = a + c
z = b + c
if x > c and y > b and z >a:
    print (f'Trojuholnik so stranami {a} a {b} a {c}')
    if a**2 + b**2 == c**2:
        print ('Je to pravouhly trojuholnik')
        alfa = round(math.asin(a / c) * 180 / math.pi, 2)
        beta = 90 - alfa
        print(f'Vnutorne uhly su {alfa} stupnov a {beta} stupnov')
        
else:
    print('Toto bohuzial nie je trojuholnik')