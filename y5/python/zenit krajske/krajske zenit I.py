n = int(input())
menus = []
for i in range(n):
    menus.append([int(x) for x in input().strip().split()])
maximum = []
for i in range(n):
    for j in range(i+1, n):
        difference = sum(abs(menus[i][k] - menus[j][k]) for k in range(4))
        maximum.append(difference)
print(max(maximum))

