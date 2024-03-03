'''
#1
def vypis_sucty(tab):
    for i in tab:
        print(sum(i), end=' ')
vypis_sucty([[1, 2, 3], [4], [5, 6]])
'''
'''
#2
def zoznam_suctov(tab):
    result = []
    for i in tab:
        result.append(sum(i))
    return result
print(zoznam_suctov([[1, 2, 3], [4], [5, 6]]))
'''
'''
#3
def pridaj_sucty(tab):
    for i in tab:
        i.append(sum(i))
    return tab
a = [[1, 2, 3], [4], [5, 6]]
print(pridaj_sucty(a))
'''
'''
#4
def preklop(matica):
    q = []
    for i in range(len(matica[0])):
        new = []
        for row in matica:
            new.append(row[i])
        q.append(new)
    print(q)
p = [[1, 2], [5, 6], [3, 4]]
preklop(p)
'''
'''
#5
def preklop_sa(matica):
    q = []
    for i in range(len(matica[0])):
        new = []
        for row in matica:
            new.append(row[i])
        q.append(new)
    matica = q
    return matica
p = [[1, 2], [5, 6], [3, 4]]
print(preklop_sa(p))
'''

#6
def zisti_dlzky(tab):
    length = len(tab[0])
    for row in tab:
        if len(row)!= length:
            return None
    return length
print(zisti_dlzky([[1, 2], [3, 4], [5, 6]]))
'''
#7
def dopln(
    tab
):
''' 