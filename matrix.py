class SizeMismatchException(Exception):
    def __init__(self, message="行列のサイズが一致しません"):
        self.message = message
        super().__init__(self.message)

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if self.row != other.row or self.col != other.col:
            raise SizeMismatchException("行列のサイズが一致していません")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.col)] for i in range(self.row)]
        return Matrix(result)

    def __mul__(self, other):
        if self.col != other.row:
            raise SizeMismatchException("第1の行列の列数と第2の行列の行数が一致していません")
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(other.col)) for j in range(other.col)] for i in range(self.row)]
        return Matrix(result)

# 行列A
A = Matrix([[1, 2],
            [3, 4],
            [5, 6]])

# 行列B
B = Matrix([[7, 8, 9],
            [10, 11, 12]])

# 行列の足し算
try:
    C = A + B
    print("行列 A + B:")
    print(C)
except SizeMismatchException as e:
    print(e)

# 行列の掛け算
try:
    D = A * B
    print("行列 A * B:")
    print(D)
except SizeMismatchException as e:
    print(e)
