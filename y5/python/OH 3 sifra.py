import random

def read_table(table_file_name):
    dictionary = {}
    with open(table_file_name) as table:
        for row in table:
            dictionary[f'{row.strip().split()[0][0]}'] = row.strip().split()[1:]
    return dictionary

def write_to_file(list, file_directory):
    with open(f'{file_directory}', 'w', encoding='UTF-8') as file:
        for line in list:
            file.write(line)

def cipher(file_name, table):
    new_file = []
    with open(f'{file_name}', encoding='UTF-8') as file:
        for row in file:
            new_row = ''
            for string in row:
                found = False
                for keys, items in table.items():
                    if string.upper() in keys:
                        new_row += f'{random.choice(items)}'
                        found = True
                if not found:
                    new_row += string
            new_file.append(row)
            new_file.append('     \n')
            new_file.append(new_row)
            new_file.append('     \n')           
    write_to_file(new_file, file_name)

def decipher(file_name, table):
    new_file = []
    with open(f'{file_name}', encoding='UTF-8') as file:
        for row in file:
            new_row = ''
            number = ''
            for string in row:
                if string not in '0123456789':
                    new_row += string
                    number =''
                elif len(number) < 2 :
                    number += string
                if len(number) == 2:
                    for key, value in table.items():
                        if number in value:
                            new_row += key
                    number = ''
            new_file.append(row)
            new_file.append('    \n')
            new_file.append(new_row)
            new_file.append('    \n')
    write_to_file(new_file, file_name)

#netusim preco to nedava enter medzi poslednymi dvoma riadkami but it iiiz wot it iiiz
cipher('y5/python/sifruj.txt', read_table('y5/python/homofona.txt'))
decipher('y5/python/desifruj.txt', read_table('y5/python/homofona.txt'))

