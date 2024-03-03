import random
def make_a_table(path_to_file):
    with open(path_to_file, 'w') as file:
        order = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'); random.shuffle(order)
        file.write(f'  {" ".join([chr(x) for x in range(ord("A"), ord("Z")+1)])}\n')
        for value_letter in range(ord('A'), ord('Z')+1):
            file.writelines(chr(value_letter)+ ' ' + ' '.join(order)+'\n')
            order = [order[-1]] + order[:-1]
def read_table(file):
    table = []
    with open(file) as file:
        for row in file:
            table.append(row.strip().split()[1:])
    return table[1:]

def cipher(word, key, key_table):
    ciphered_word, table = '', read_table(key_table)
    for i, letter in enumerate(list(word)):
        ciphered_word += table[int(ord(letter))-int(ord('A'))][ord(str(key[int(i)%len(key)]))-ord('A')]
    return ciphered_word

def decipher(ciphered_word, key, key_table):
    deciphered_word, i, table = '', 0, read_table(key_table)
    for letter in ciphered_word:
        for index, line in enumerate(table):
            if line[ord(key[i%len(key)]) - ord('A')] == letter:                
                deciphered_word += chr(index + ord('A'))
                i += 1
                break
    return deciphered_word

print(cipher('SLOVO', 'HESLO', 'y5/python/tabulkova_sifra.txt'))
print(decipher('LGMJC', 'HESLO', 'y5/python/tabulkova_sifra.txt'))

        
