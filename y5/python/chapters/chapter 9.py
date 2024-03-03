#2
'''
def zluc(zoz1, zoz2):
    list = []
    if len(zoz1) < len(zoz2):
        zoz1, zoz2 = zoz2, zoz1
    print(zoz1, zoz2)
    for i in range(len(zoz2)):
        if zoz1[i] < zoz2[i]:
            list.append(zoz1[i])
        else:
            list.append(zoz2[i])
        print(list)
    for j in range(len(zoz2)+1,len(zoz1)):
        list.append(zoz1[j])
    return listS

print(zluc([5, 6, 10], [1, 6, 7, 12]))
'''
max = 0
for i in range(1, 180):
    count = 1
    sum = 0
    if i % 7 == 0:
        count += 1
    if i % 6 == 3:
        count += 1
    if i % 2 == 0:
        count += 1
    for j in str(i):
        sum += int(j)
    if sum == 11:
        count += 1
    if count > max:
        max = count
        print(i, max)
