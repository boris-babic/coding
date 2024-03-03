import random

numbers = [f'{x:02d}' for x in range(100)]
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def make_a_code(numbers, letters):
    dictionary = {}
    for letter in letters:
        dictionary[f'{letter}'] = [numbers.pop(random.randrange(len(numbers))), numbers.pop(random.randrange(len(numbers)))]
    while numbers:
        dictionary[f'{random.choice(letters)}'].append(numbers.pop(random.randrange(len(numbers))))
    with open('y5/python/sifra.txt', 'w') as file:
        for key,value in dictionary.items():
            file.write(f'{key} {" ".join(value)}\n')
#make_a_code(numbers, letters)

def read_code(code):
    dictionary = {}
    with open(code) as file:
        for row in file:
            dictionary[f'{row.strip().split()[0]}'] = row.strip().split()[1:]
    return dictionary

def decipher(message):
    code = read_code('y5/python/sifra.txt')
    deciphered_message = ''
    for number in message.strip().split():
        for key, value in code.items():
            if number in value:
                deciphered_message += key
    return deciphered_message

def code(message):
    code = read_code('y5/python/sifra.txt')
    coded_message = ''
    for letter in list(str(message)):
        for key, value in code.items():
            if letter.upper() == key:
                coded_message += f'{str(random.choice(value))} '
    return coded_message

print(code('auto'))

