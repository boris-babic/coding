n= input()
a = input().strip().split()
data = [int(x) for x in a]
value = 1
for i in data:
    value = value * i
print(f'{int((value/data[0])%(10**9+7))}', end='')
for i in data[1:]:
    print(f' {int((value/data[0])%(10**9+7))}', end='')
print()
