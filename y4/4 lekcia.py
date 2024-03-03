number = int(input('Gimme a number: '))
factor = 1
factors = []

while True:
    if not number % factor:
        factors.append(factor)
    factor += 1
    if factor > number:
        break

print(factors)
