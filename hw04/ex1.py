# Напишите функцию для транспонирования матрицы

import random


def insert_matrix(matrix, size_row, size_column):
    for i in range(size_row):
        arr = []
        for j in range(size_column):
            arr.append(random.randint(0, 9))
        matrix.append(arr)

def print_matrix(matrix, size_row, size_column):
    for i in range(size_row):
        for j in range(size_column):
            print(matrix[i][j], end=' ')
        print()

def transpon(matrix, trans_matrix, size_row, size_column):
    for i in range(size_row):
        for j in range(size_column):
            trans_matrix[j][i] = matrix[i][j]

matrix = []
size_row = 2
size_column = 4
insert_matrix(matrix, size_row, size_column)
print_matrix(matrix, size_row, size_column)
print()
trans_matrix = []
insert_matrix(trans_matrix, size_column, size_row)
transpon(matrix, trans_matrix, size_row, size_column)
print_matrix(trans_matrix, size_column, size_row)



