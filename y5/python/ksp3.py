
n = input()
inputs = input().split()
binnumbers = [int(x) for x in inputs]

def and_values(number1, number2):
    number1 = str(bin(int(number1)))[2:]
    number2 = str(bin(int(number2)))[2:]
    number1 = number1[::-1]
    number2 = number2[::-1]
    x = ''
    if len(number2)>len(number1):
        number1, number2 = number2, number1
    for i in range(len(number2)):
        if int(number1[i])==1 and int(number2[i]) == 1:
            x += '1'
        else:
            x += '0'
    return (int((x[::-1]), 2))

def xor_values(number1, number2):
    number1 = str(bin(int(number1)))[2:]
    number2 = str(bin(int(number2)))[2:]
    number1 = number1[::-1]
    number2 = number2[::-1]
    x = ''
    if len(number2)>len(number1):
        number1, number2 = number2, number1
        number2 += '0' *(len(number1)-len(number2)) 
    for i in range(len(number2)):
        if int(number1[i]) != int(number2[i]):
            x += '1'
        else:
            x += '0'
    return(int((x[::-1]), 2))
counter = 0
for i,j in enumerate(binnumbers):
    for k in binnumbers[i+1:]:
        if and_values(j, k)>xor_values(j, k):       
            counter += 1
print(counter)