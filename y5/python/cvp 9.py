import math
def readfile(file, *type):
    original = []
    with open(file, 'r') as file:
        rows =[]
        for row in file:
            original.append(row.strip())
            line = []
            x = row.strip().strip('=').split('+')
            for i in x:
                line.append(i.strip().split('/'))
            rows.append(line)
    if type:
        return rows, original
    else:
        return rows

def calculate(row):
    row_denominator = int(row[0][1])
    row_value = int(row[0][0])
    for fractions in row[1:]:
        nominator = int(fractions[0])
        denominator = int(fractions[1])
        if row_denominator != denominator:
            common = math.lcm(row_denominator, denominator)
            row_value = row_value * int(common / row_denominator)
            nominator = nominator * int(common / denominator)
            row_denominator = common
            denominator = common
            #print(row_value, row_denominator, nominator, denominator, common)
        row_value +=nominator
    return(row_value, row_denominator)

def simplify(answer):
    nominator, denominator = answer
    if nominator%denominator==0:
        return int((nominator/denominator))
    else:
        return f'{nominator}/{denominator}'

def answers(file):
    lines, original = readfile(file, 1)
    for i, row in enumerate(lines):
        answer = simplify(calculate(row))
        original[i] += str(answer)
    with open(file) as file:
        for row in original:
            print(row, file=file)
    
    
answers('zlomky.txt')

    
    