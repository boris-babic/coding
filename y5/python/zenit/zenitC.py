n = int(input())
list = list(map(int,(input().split())))
suma = sum(list)
for i in range(n):
    print(suma-list[i])