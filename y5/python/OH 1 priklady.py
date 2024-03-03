import random

with open('priklady.txt','w') as file:
    for i in range(10):
        sign = ('+', '-')
        file.write(f'{random.randrange(100)} {random.choice(sign)} {random.randrange(100)} =  \n')

with open('priklady.txt') as file:
    new_equations = []
    for row in file:
        og = row
        row.strip()
        sum , dif = 0, 0
        if '+' in row:
            number1 = int(row[:row.find('+')].strip())
            number2 = int(row[row.find('+')+1: row.find('=')].strip())
            sum = number1 + number2
        if '-' in row:
            number1 = int(row[:row.find('-')].strip())
            number2 = int(row[row.find('-')+1: row.find('=')].strip())
            dif = number1 - number2
        if sum < 100 and dif >= 0:
            new_equations.append(og)
print(new_equations)
with open('priklady.txt', 'w') as file:  
    for equation in new_equations:
        file.write(equation)    

