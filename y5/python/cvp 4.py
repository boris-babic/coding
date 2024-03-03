def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def prime_factorization(n, primes):
    factors =[]
    power_factors = []
    active = True
    i = 0
    if n in primes:
        factors = [1, n]
        active = False
    while active:
        if n % primes[i] == 0:
            factors.append(primes[i])
            n = n/primes[i]
        else:
            i+=1
        if i >len(primes)-1:
            active = False
    for i in list(set(factors)):
        count = factors.count(i)
        power_factors.append((i, count))
    return power_factors

def gcf(numbers):
    primes = find_primes(numbers[-1])
    gcf = []
    x = 1
    for prime in primes:
        min_count = 99
        for number in numbers:
            factors = prime_factorization(number, find_primes(number))
            for i, j in factors:
                if i == prime and j< min_count:
                    min_count = j
        if min_count != 99:
            gcf.append(prime ** min_count)
    for i in gcf:
        x *= i
    print(x)
        
gcf([64, 30])

    
'''
with open('gcf.txt') as file:
    with open ('gcf1.txt', 'w') as new_file:
        for row in file:
            numbers = [ int(x) for x in row.split()]
            numbers.sort()
'''