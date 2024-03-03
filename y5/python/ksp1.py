n = int(input())
pencils = []
for i in range(int(n)):
    x = input()
    pencils.append(int(x))


if n<3:
    max = 0
else:
    pencils.sort()
    max_length = int(pencils[-2])-1
    list_of_steps = pencils[:-2]
    if max_length < len(list_of_steps):
        max = max_length
    else:
        max = len(list_of_steps)

print(max)