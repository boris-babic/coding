file_name = 'osemsmerovka 12x12.txt'
text = []
with open(file_name, encoding='UTF-8') as file:
    for row in file:
        text.append(row.strip())
    words = text[:text.index('')]
    table = text[text.index('')+1: -4]
    joke = text[-2]
    number_of_letters = list(text[-1])

def create_used_letters_table(table):
    used_letters_table = []
    for i in range(len(table)):
        used_letters_table_row = []
        for j in range(len(table[0])):
            used_letters_table_row.append(0)
        used_letters_table.append(used_letters_table_row)
    return used_letters_table

def check_rows(table, used_letters_table, word):
    for index, row in enumerate(table):
        if row.find(word) !=-1:
            for used_index in range(len(word)):
                used_letters_table[index][row.find(word)+used_index] = 1
        if row[::-1].find(word) !=-1:
            for used_index in range(len(word)):
                used_letters_table[index][(len(row)-row[::-1].find(word))-1-used_index] = 1
    return table, used_letters_table

def check_columns(table, used_letters_table, word):
    blank_table = []
    turned_table = []
    #creates a blank table
    for i in range(len(table[0])):
        table_row = []
        for j in range(len(table)):
            table_row.append(0)
        blank_table.append(table_row)
    #swaps each letter in the table
    for i in range(len(table)):
        for j in range(len(table[0])):
            blank_table[j][i] = table[i][j]
    #joins each row together
    for row in blank_table:
        turned_table.append(''.join(row))
    #checks the turned table
    for index, row in enumerate(turned_table):
        if row.find(word) !=-1:
            for used_index in range(len(word)):
                used_letters_table[row.find(word)+used_index][index] = 1
        if row[::-1].find(word) !=-1:
            for used_index in range(len(word)):
                used_letters_table[(len(row)-row[::-1].find(word))-1-used_index][index] = 1
    return table, used_letters_table

def check_diagonals_decreasing(table, used_letters_table, word):
    length_of_table = len(table) + len(table[0])-1
    decreasing_diagonal_table = []
    for i in range(length_of_table):
        decreasing_diagonal_table.append('')
    for i in range(len(table)):
        for j in range(len(table[0])):
            decreasing_diagonal_table[(i-j+len(table[0])-1)%length_of_table] += table[i][j]
    for index, diagonal in enumerate(decreasing_diagonal_table):
        if diagonal.find(word) !=-1:
            if index < len(table[0]):
                i = 0
                j = len(table[0])-index-1
            else:
                i = index-len(table[0])+1
                j = 0
            for used_index in range(len(word)):
                used_letters_table[i + diagonal.find(word) + used_index][j +diagonal.find(word) + used_index] = 1
        if diagonal[::-1].find(word) !=-1:
            if index < len(table[0]):
                i = 0
                j = len(table[0])-index-1
            else:
                i = index-len(table[0])+1
                j = 0
            for used_index in range(len(word)):
                used_letters_table[i + len(diagonal[::-1]) - diagonal[::-1].find(word) - used_index-1][j + len(diagonal[::-1]) - diagonal[::-1].find(word) - used_index-1] = 1

def check_diagonals_increasing(table, used_letters_table, word):
    length_of_table = len(table) + len(table[0])-1
    increasing_diagonal_table = []
    for i in range(length_of_table):
        increasing_diagonal_table.append('')
    for i in range(len(table)):
        for j in range(len(table[0])):
            increasing_diagonal_table[(i+j)%length_of_table] += table[i][j]
    for index, diagonal in enumerate(increasing_diagonal_table):
        if diagonal.find(word) != -1:

            if index < len(table[0]):
                i = 0
                j = index
            else:
                i = index-len(table[0])+1
                j = len(table[0])-1
            for used_index in range(len(word)):
                used_letters_table[i + diagonal.find(word) + used_index][j - diagonal.find(word) - used_index] = 1
        if diagonal[::-1].find(word) != -1:
            if index < len(table[0]):
                i = 0
                j = index
            else:
                i = abs(index-len(table[0]))+1
                j = len(table[0])-1
            for used_index in range(len(word)):
                used_letters_table[i+len(diagonal)-used_index - diagonal[::-1].find(word)-1][j-len(diagonal)+used_index + diagonal[::-1].find(word)+1] = 1



def print_check(table, used_letters_table):
    for i in range(len(table)):
        print(table[i], used_letters_table[i])
    print()

used_letters_table = create_used_letters_table(table)
#check_diagonals_decreasing(table, used_letters_table, 'ŤAHAČ')
#print_check(table, used_letters_table)

for word in words:
    check_rows(table, used_letters_table, word)
    check_columns(table, used_letters_table, word)
    check_diagonals_decreasing(table, used_letters_table, word)
    check_diagonals_increasing(table, used_letters_table, word)
#print_check(table, used_letters_table)
answer = ''
for i in range(len(used_letters_table)):
    for j in range(len(used_letters_table[0])):
        if used_letters_table[i][j] == 0:
            answer += table[i][j]

start_index = 0
answer_split = ''
for length in number_of_letters:
    end_index = start_index+int(length)
    answer_split += f'{answer[start_index:end_index]} '
    start_index = end_index
x = input()
print(answer_split)