'''
#1
def sucin(zoznam):
    result = 1
    for i in zoznam:
        result *= i
    return result
sucin(list(range(1, 11)))
'''
'''
#2
def mocniny(n):
    return list(x**2 for x in range(1, n+1))
print(mocniny(7))
'''
'''
#3
def len_parne(zoznam):
    new = []
    for i in zoznam:
        if i % 2==0:
            new.append(i)
    return new
print(len_parne([2, 5, 7, 10, 13, 19, 21, 24]))
'''
'''
#4
def spoj(zoznam):
    char = ''
    for slovo in zoznam:
        char = char + slovo + ' '
    char.strip()
    return char
slova = ['nepi', 'Jano', 'nepi', 'vodu']
print(spoj(slova))
'''
'''
#5
def zisti(zoznam):
    count = 0
    for i in zoznam:
        if type(i) == int and not i%7:
            count +=1
    return count
print('pocet =', zisti([4, 7.0, 14, '7', 0]))
'''
'''
#6
def zoznam2(n, value1, value2):
    return [value1, value2] *int(n/2)
print(zoznam2(10, 7, 'w'))
'''
'''
#7
def na_parnych(zoznam):
    return zoznam[::2]
print(na_parnych(list('programovanie')))
'''
'''
#8
def zostupne(zoznam):
    for i in range(len(zoznam)-1):
        if zoznam[i] < zoznam[i+1]:
            return False
        else:
            return True
print(zostupne([1, 2, 3]))
'''
'''
#9
def vyrob1(zoznam):
    return [x+1 if not x %2 else x for x in zoznam]
print(vyrob1([3, 5, 6, 8, 9, 10, 11, 13]))
'''
'''
#10
zoz1 = [1, 2.2, ['a', 'b'], 'tri', 4, '']
def vyrob2(zoznam):
    novy = []
    for i in zoznam:
        if type(i) == str:
            novy.append(i)
    return novy
print(vyrob2(zoz1))
'''
'''
#11
def zoznam_cifier(cislo):
    return [list(str(cislo))]
print(zoznam_cifier(123456789))
'''
'''
#12
def gener(a, b, c=1):
    return [x for x in range(a, b, c)]
'''
'''
#13
def cele(zoznam):
    new = []
    for i in zoznam:
        new.append(int(i))
    return new
print(cele([3.14, -7.0, 0.99]))
'''
'''
#14
def vymen(zoznam):
    return zoznam[::-1]
print(vymen(['ahoj', '123']))
'''
#15 is the same
'''
#16
def vyhod(zoznam, hodnota):
    for i in zoznam:
        if i == hodnota:
            zoznam.remove(i)
    return zoznam
print(vyhod([37, 'hello', -7, 3.14, 'hello', 2], 'hello'))
'''
#17 is the same
'''
#18
def zo_suboru(meno_suboru):
    new = []
    with open(meno_suboru) as file:
        for row in file:
            if ' ' in row:
                x = [row[:row.find(' ')].strip(), row[row.find(' ')+1:].strip()]
                new.append(x)
            else:
                new.append(row.strip())
    return new
print(zo_suboru('python/subor.txt'))
'''
'''
#19
def do_suboru(meno_suboru, zoznam):
    with open(meno_suboru, 'w') as file:
        for i in zoznam:
            if type(i) == int:
                file.writelines(str(i))
            else:
                for j in i:
                    file.write(str(j))
                    file.write(' ')
            file.write('\n')
xy = [[100, 200], 300, 400, [500, 600]]
do_suboru('subor19.txt', xy)
'''
'''
#20
def krat2(zoznam):
    return [x*2 for x in zoznam]
print(krat2([5, 3.14, [1, 2], -4, 'ab']))
'''
'''
#21
def zdvoj(zoznam):
    for i,j in enumerate(zoznam[:]):
        print(i, j)
        zoznam.insert(i-1, j)
        print(i, j)
zdvoj([1, 'Python', 2, 'Java', 3, 'C#'])
'''
'''
#22
def uprac(zoznam):
    zoznam.sort()
    for i,j in enumerate(zoznam):
        if j ==2:
            x = zoznam.pop(i)
            zoznam.insert(0, j)
    return zoznam
print(uprac([2, 2, 0, 0, 0, 1]))
'''

#23
import random
def nahodny_zoznam(n, vyber):
    return [random.choice(vyber) for i in range(n)]
print(nahodny_zoznam(8, [7, 'red', None]))

