'''
a = 10
a = a + 10

a += 10

a = 10
b = 'ahoj'
a, b = b, a
print (a)
print (b)
a, b, c, d, e, f = 'Python'
print (a, b, c, d, e, f, sep='-')

print (str(cislo1)+ cislo2)
print (cislo1, cislo2, sep='')

cislo1 = 4567
cislo2 = int(input ('zadaj cislo: '))
zvysok = cislo2 % 100
print (cislo1, zvysok, sep='')

pocet_rokov = int(input('Zadaj dlzku sporenia v rokoch: '))
urok = int(input('Zadaj rocny urok v percentach: '))
vklad = int(input ('Zadaj tvoj vklad: '))

nasobok = urok / 100 + 1
for i in range (pocet_rokov):
    vklad = vklad * nasobok
    print ('Vase uspory po {} roku pri {} percentnom uroku je {}'.format(i+1, urok, round(vklad, 2)))
'''

dlzka = 1
sirka = 0.3
vyska = 0.5
sirkaskla = 0.01
dlzkavody = dlzka - 2*sirkaskla
sirkavody = sirka - 2*sirkaskla
vyskavody = vyska - sirkaskla

hustotavody = 998
hustotaskla = 2500

objem = dlzkavody * sirkavody * vyskavody
povrch = 2* (dlzka * sirka + dlzka * vyska + sirka * vyska) - dlzka * sirka

hmotnostvody = objem * hustotavody
hmotnostskla = povrch * sirkaskla * hustotaskla
hmotnostakvaria = hmotnostskla + hmotnostvody
print (hmotnostvody)
print (hmotnostskla)
print ('Hmotnost akvaria je {}'.format(hmotnostakvaria))
