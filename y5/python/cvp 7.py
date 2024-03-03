a = [[3,1],[2,1],[1,0]]
b = [[1,0,2], [-1,3,1]]



def make_matrix(width):
    result = []
    for i in range(width):
        result.append([0]*width)
    return result

def convert(old):
    matrix = []
    for i in range(len(old[0])):
        row = []
        for j in range(len(old)):
            row.append(old[j][i])
        matrix.append(row)
    return matrix

def multiply(a, b):
    width = max(len(a), len(b))
    second_length = min(len(a[0]),len(b[0]))
    result = make_matrix(width)
    new_b = convert(b)
    for i in range(width):
        for j in range(width):
            x = 0
            for k in range(second_length):
                x += a[i][k]*new_b[j][k]
            result[i][j] = x
    return result
print(multiply(a,b))