with open('text.txt', encoding='UTF-8') as file:
    text = []
    for row in file:
        text.append(row)
def decoding(text, password):
    table = {}
    with open('tabulka.txt') as file:
        for row in file:
            x = row.strip().split()
            table[f'{x[0]}'] = x[1:]
    coded_message, index = '', 0
    for row in text:
        for letter in row.upper():
            if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                for i, j in enumerate(table[password[index % len(password)].upper()]):
                    if j == letter:
                        coded_message += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i]
                index += 1
            else:
                coded_message += letter
    return coded_message
print(decoding(text, 'covid'))