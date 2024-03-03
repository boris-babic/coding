n, k = input().split()
n, k = int(n), int(k)
ice_creams = [int(x) for x in input().split()]
for i in range(n-k+1):
    maximum = max(ice_creams[i:i+k])
    print(maximum,end = ' ')