matrix = [
    [12,6,31,16,18],
    [13,10,18,32,6],
    [32,21,40,22,26],
    [8,13,24,41,19],
]
def row_extreme(row):
    extremum = 9999
    extremum_index = 0
    for index, value in enumerate(row):
        if value < extremum:
            extremum = value
            extremum_index = index
    return (extremum, extremum_index)

def transform(matrix):
    new = []
    for i in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][i])
        new.append(new_row)
    return new

def find_local(matrix):
    row, column, special_value = 0, 0, 0 
    transformed = transform(matrix)
    for row_index, row in enumerate(matrix):
        value, index = row_extreme(row)
        if value == max(transformed[index]):
            return (value, index, row_index)
        
print(find_local(matrix))