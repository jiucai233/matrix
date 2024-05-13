class SizeMismatchException(Exception):
    def __init__(self, message="行列のサイズが一致しません"):
        self.message = message
        super().__init__(self.message)

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])

    def __str__(self):
        return str(self.matrix)

    def __add__(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError("Matrices must have the same dimensions for addition")

        result_matrix = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for row in range(self.row):
            for col in range(self.col):
                result_matrix[row][col] = self.matrix[row][col] + other.matrix[row][col]
        return Matrix(result_matrix)

    def __sub__(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError("Matrices must have the same dimensions for subtraction")

        result_matrix = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for row in range(self.row):
            for col in range(self.col):
                result_matrix[row][col] = self.matrix[row][col] - other.matrix[row][col]
        return Matrix(result_matrix)

    def __mul__(self, other):
        if self.col != other.row:
            raise ValueError("Matrices must have compatible dimensions for multiplication")

        result_matrix = [[0 for _ in range(other.col)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(other.col):
                for k in range(self.col):
                    result_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result_matrix)

# Example usage
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[3, 4], [5, 6]])
C = Matrix([[3,4],[5,6],[1,2]])
D = Matrix([[3,4,5],[5,6,7]])
print(A)
print(A + B)  
print(A * D) 
try:
    print(A + C)
except Exception as e:
    print(e)

try:
    print(A * C)
except Exception as e:
    print(e)
