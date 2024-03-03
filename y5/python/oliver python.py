#faktorialy my ass
'''
n = int(input())
vysledok = 1
riadok = '1' # '1.2.3.4.5='
for i in range(2, n+1):
    vysledok = vysledok * i
    #riadok = riadok + '.'+ str(i)
    riadok = f'{riadok}.{i}'
riadok = riadok + '=' 
print(riadok, vysledok)
'''
'''
n = 3
n = int(input())
vysledok = 1
riadok = '1' # '1.2.3.4.5='
vojde do for loopu
i = 2
vysledok = 1 * 2 = 2
riadok = '1.2'
i = 3
vysledok = 2 * 3 = 6
riadok = '1.2.3'
i = 4
vyjdeme z for loopu
riadok = '1.2.3='
'1.2.3=' 6
'''
'''
#hod kockou my ass
import random
pocty = [0,0,0,0,0,0]
kocka = [1,2,3,4,5,6]
n=5
for i in range(n):
    hod = random.choice(kocka)
    pocty[hod-1] += 1
    print(hod)
print(pocty)
for i in range(6): #012345
    print(f'Cislo {kocka[i]} sme hodili {pocty[i]} krat')
'''
#hod mincou my ass
'''
import random
moznosti = ['rub','lice']
pocty = [0,0]



for i in range(100):
    hod=random.randint(1,2)
    pocty[hod-1] += 1

print(moznosti)
print (pocty)

for i in range(2):
    print (f'vyskyt stavu + {moznosti[i]} {pocty[i]}-krát.')

#uroky
pociatocna_suma = 500
terajsia_suma = pociatocna_suma
urok = 5/100 #lebo 5 % je 0,05
dlzka = 10
#po a)
for i in range(10):
    pociatocna_suma = pociatocna_suma * (1+urok)
print(f'Za 10 rokov sa pri {urok*100}% uroku stane z {pociatocna_suma}€ {terajsia_suma}€')
#po b)
cielova_suma = 1000
pocet_rokov = 0
while terajsia_suma < cielova_suma:
    terajsia_suma = terajsia_suma * (1+urok)
    pocet_rokov += 1
print(f'Za {pocet_rokov} rokov presiahne pociatocna suma koncovu sumu')

hladane_meno = input('meno ty pico ')
najdene_meno = 'nie'
pocet_mien = 0
with open('mena.txt') as file:
    for riadok in file:
        pocet_mien +=1
        if hladane_meno in riadok:
            najdene_meno = 'ano'


if najdene_meno == 'ano':
    print('nasiel sa ten penis')
else:
    print('zdrhol nam kokot')
print('pocet kokotov je', pocet_mien)
'''
active = True
while active:
    with open('mena.txt', 'a') as subor:
        pocet_mien = 0
        zaciatocne_pismeno = input('daj sem zaciatocne pismeno: ').upper()
        for riadok in subor:
            pocet_mien += 1
            if zaciatocne_pismeno == riadok[0].upper():
                print(riadok.strip())
        otazka = input('chcete zopakovat [y/n]')
        if otazka == 'n':
            active = False
        print('penis', file=subor)
    print('je tu tolkoto penisov: ', pocet_mien)

