from numpy import dot, linalg

class Matrix:
    def __init__(self, matrix=None):
        if matrix != None:
            self.matrix = matrix
        else:
            self.matrix = []
    
    @property
    def rows(self):
        return len(self.matrix)

    @property
    def cols(self):
        return len(self.matrix[0])
            
    @property
    def order(self):        
        order = "{}x{}".format(self.rows, self.cols)
        return order
    
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix: list | tuple):
        for i, x in enumerate(matrix[0:-1]):
            if len(x) != len(matrix[i+1]):
                raise Exception("Matrix is formatted incorrectly")
        self._matrix = matrix
        
    def __repr__(self):
        matrix_repr = """["""
        for x in self.matrix:
            to_add = "\n  "
            for y in x:
                to_add += " {}".format(str(y))
            matrix_repr += to_add
        matrix_repr += "\n]"
        return matrix_repr

    def __add__(self, other):
        if self.order != other.order:
            raise ArithmeticError("Can't add matricies of differering orders")
        
        new_matrix = []
        for _ in range(len(self.matrix)):
            new_matrix.append([])
        for i, x in enumerate(self.matrix):
            for j, y in enumerate(x):
                new_matrix[i].append(int(self.matrix[i][j]) + int(other.matrix[i][j]))
        return Matrix(new_matrix)

    def __sub__(self, other):
        if self.order != other.order:
            raise ArithmeticError("Can't subtract matricies of differering orders")
        
        new_matrix = []
        for _ in range(len(self.matrix)):
            new_matrix.append([])
        for i, x in enumerate(self.matrix):
            for j, y in enumerate(x):
                new_matrix[i].append(int(self.matrix[i][j]) - int(other.matrix[i][j]))
        return Matrix(new_matrix)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ArithmeticError("Can't multiply matricies, incorrect orders")

        new_matrix = dot(self.matrix, other.matrix).tolist()
        return Matrix(new_matrix)
    
    def __truediv__(self, other):
        """Note, there is no 'division' regarding matricies. Instead, one matrix is multiplied by the
        inverse of the other"""
        if self.rows != self.cols or other.rows != other.cols:
            raise ArithmeticError("Can't divide non-square matricies")
        
        if linalg.det(other.matrix) == 0:
            # if det == 0, then cant inverse
            raise ArithmeticError("Can't invert matrix {}".format(other))
        
        inverse = Matrix(linalg.inv(other.matrix).tolist())
        return self * inverse
            


            

# m1 = Matrix()
# m1.matrix = [[1,1,1],[1,1,1],[1,1,1]]

# m2 = Matrix()
# m2.matrix = [[2,3,5],[5,9,7],[8,12,10]]

# print((m1+m2).matrix)
# print(type(m1+m2))

# print((m1-m2).matrix)
# print(type(m1-m2))

# print(m1/m2)