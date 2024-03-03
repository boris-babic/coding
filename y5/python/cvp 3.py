import random

with open('cisla_prvocisla.txt', 'w') as file:
    file.write('23' + '\n')
    file.write('14' + '\n')
    file.write('32' + '\n')
    file.write('31' + '\n')
    file.write('121' + '\n')
    file.write('3587' + '\n')
    file.write('21564' + '\n')

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

def prime_factors(n, primes):
    factors =[]
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
    return factors

def printing_function(x):
    final = f'{x}='
    factors = prime_factors(x, find_primes(x))
    for i in list(set(factors)):
        count = factors.count(i)
        if count>1:
            final += f'{i}^{count}*'
        else:
            final += f'{i}*'
    return final[:-1]
        





with open('cisla_prvocisla.txt', 'r') as file:
    with open('cisla_prvocisla1.txt', 'w') as new_file:
        file_print = []
        for row in file:
            x = int(row.strip())
            file_print.append((x, printing_function(x)))
        file_print.sort(reverse=True, key=lambda x: x[0])
        for row in file_print:
            new_file.write(row[1] +'\n')