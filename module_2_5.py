def get_matrix (n, m, value):
    matrix = []
    for x in range(n):
        row = [value] * m
        matrix.append(row)
    return matrix

#для читабельности
def print_matrix(matrix):
    for row in matrix:
        print(row)


result1 = get_matrix(2,2,10)
result2 = get_matrix(3,5,42)
result3 = get_matrix(4,2,13)

print_matrix(result1)
print('')
print_matrix(result2)
print('')
print_matrix(result3)