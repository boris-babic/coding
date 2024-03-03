'''
#priklad 1 
stav_uctu = 0 #lebo na zaciatku tam nie je nic
mesacny_vklad = int(input('Zadaj mesacny vklad: '))
urok = float(input('Zadaj urok v percentach: '))/100+1 #ak je urok 4,25 tak sa to nasobi 1,0425 
zisk = 0
for rok in range(1, 11):
    stav_uctu +=mesacny_vklad
    zisk = stav_uctu * urok - stav_uctu
    stav_uctu += zisk
    print(f'Po {rok}.rok je zisk {round(zisk, 2)} eur')
print(f'Po 10 rokoch mate na ucte {round(stav_uctu, 2)} eur')

#priklad 2 
pocet_riadkov = int(input('Zadaj pocet riadkov: '))

for riadok in range(pocet_riadkov+1):
    print(' '*(pocet_riadkov-riadok), end='')
    for poradie_znaku in range((riadok*2)-1):
        if poradie_znaku < (riadok*2-poradie_znaku):
            print(poradie_znaku+1, end='')
        else:
            print(riadok*2-poradie_znaku-1, end='')
    print()
'''
n = 9
for i in range(1, n+1):
    print(i, end='')
for i in range(8, 0, -1):
    print(i, end='')
print()
n -= 1
for i in reversed(range(1, n)):
    for j in range(1, i+2):
        print(j, end="")
    print(" " * ((n-i)*2-1), end="")
    for i in reversed(range(1, i+2)):
        print(i, end="")
    print()