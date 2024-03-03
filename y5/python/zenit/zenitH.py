n, m, l = map(int, input().split())
pattern = list(map(int, input().split()))


used = [False] * (n * m)
valid = True
 
for i in range(l):
    used[pattern[i] - 1] = True
    for j in range(i + 1, l):
        if pattern[i] > pattern[j]:
            valid = False
            break
    if not valid:
        break

if valid and all(used):
    print("Ano")
else:
    print("Nie")