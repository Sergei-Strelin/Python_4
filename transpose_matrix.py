def transpose_matrix(matrix):
    
    trans_matrix = []
    for i in range(len(matrix[0])):
        trans_matrix.append([None]*len(matrix))
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]

    return trans_matrix


def print_matrix(matrix):
    for line in matrix:
        print(line)

matrix = [[5, 4, 3, 6],
          [2, 4, 6, 2],
          [4, 9, 7, 9],
          ]

print('Исходная матрица: ')
print_matrix(matrix)

print('Транспонированная (перевёрнутая) матрица: ')
print_matrix(transpose_matrix(matrix))