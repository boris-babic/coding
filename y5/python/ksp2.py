z, k = input().split()
p = int(input())
list = input().split()
list = [int(x) for x in list]
list.sort()

dif = []
x = 0
for i in range(1, len(list)):
    x = list[i] -list[i-1] -1
    dif.append(x)

dif.append(int(k) - list[-1])
dif.append(list[0]-int(z))
dif.sort()
print(dif[-1])
