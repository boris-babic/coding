'''
n = 5
x = 0

x = n * (n+1)/2

print()

for i in range(n):
    for j in range(n-i):
        print(int(x), end = ' ')
        x -= 1
    print()
'''
