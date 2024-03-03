'''
n = '5'
pile = list('6232213')
count = 0
recent = pile
max = 0
special = list(set(pile))
special.sort()
for i in special:
    for j in special:
        count = 0
        for k in pile:
            if k == i or k == j:
                count +=1 
            else:
                count = 0
            if count > max:
                max = count
print(max)

'''
n = input()
pile = input().strip().split()

unique_elements = set(pile)
max_count = 0

for i in unique_elements:
    for j in unique_elements:
        if i == j:
            continue

        count = 0
        dp = [0] * len(pile)

        for idx, k in enumerate(pile):
            if k == i or k == j:
                count += 1
            else:
                count = 0

            dp[idx] = count

        max_count = max(max_count, max(dp))

print(max_count)
