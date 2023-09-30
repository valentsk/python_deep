import random


class Matrix:

    def __init__(self, rows: int = 2, columns: int = 2, matrix: list[list[int]] = None):
        if matrix is None:
            if rows > 1 and columns > 1:
                self.rows = rows
                self.columns = columns
                self.matrix = [[random.randint(0,100) for _ in range(columns) for _ in range(rows)]]
            else:
                raise ValueError
        else:
            if Matrix._check_matrix(matrix):
                self.rows = len(matrix)
                self.columns = len(matrix[0])
                self.matrix = matrix
            else:
                raise ValueError

    def __eq__(self, other):
        if Matrix._same(self, other):
            return all([all([self.matrix[r][c] == other.matrix[r][c]
                             for c in range(self.columns)]) for r in range(self.rows)])
        else:
            return ValueError

    def __str__(self):
        return '\n'.join(''.join([f'{x:^5}' for x in row]) for row in self.matrix) + '\n'

    def __add__(self, other):
        if Matrix._same(self, other):
            return Matrix(matrix = [[self.matrix[i][j] + other.matrix[i][j]
                                     for j in range(self.columns)] for i in range(self.rows)])
        else:
            return ValueError
    @staticmethod
    def _same(matrix1, matrix2):
        return isinstance(matrix2, Matrix) and matrix1.rows == matrix2.rows and matrix1.columns == matrix2.columns

    @staticmethod
    def _check_matrix(matrix: list[list[int]]) -> bool:
        return len(set(map(len, matrix))) == 1


a = Matrix()
b = Matrix(4, 5)
c = Matrix(matrix = [[1,2,3],[4,5,6],[7,8,9]])
d = Matrix(matrix = [[1,2,3],[4,5,6],[7,8,9]])

print(a)
print(b)
print(c)

print(c == d)
print(c is d)
print(c + d)