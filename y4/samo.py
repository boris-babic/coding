def verification(input):
    input = input.strip()
    print(get_sum(input))
    if len(input) != 19:
        return False
    elif get_sum(input)%10!=0:

        return False
    else:
        return True

def get_sum(number):
    sum = 0
    number = f'{number[:4]}{number[5:9]}{number[10:14]}{number[15:]}'
    for i in range(16):
        if i%2!=0:
            sum+= int(number[i])
        else:
            sum+= get_double(number[i])
    return sum

def get_double(number):
    number = str(int(number)*2)
    if int(number)>9:
        x = int(number[0])+int(number[1])
    else: x = number
    return int(x)


print(verification('1234-5678-9456-7506'))