from math import sqrt


class Matrix:
    """ This class do matrix things"""

    def __init__(self, value_list, number_of_rows=None, number_of_columns=None):
        """
        When you want to define a square matrix you can leave blank
        row and column parameters

        n is the number of rows while m is the number of columns
        """
        self.values = value_list
        self.m = number_of_columns
        self.n = number_of_rows
        self.rows = []
        self.columns = []

        # If rows and columns isn't given the matrix will be square
        if not (self.m and self.n):
            self.m = int(sqrt(len(self.values)))
            self.n = int(sqrt(len(self.values)))

        self.create_columns_rows()

    def create_columns_rows(self):
        """
        This function create two lists that contains the rows and columns
        separately

        When the row has less numbers than the length we add a new num
        and when there are enough numbers it throw the row to self.rows
        """
        row = []
        for value in self.values:
            if len(row) < self.m:
                row.append(value)
            else:
                self.rows.append(row)
                row = [value]
        self.rows.append(row)

        """
        When the column has less numbers than the length we add a new num
        and when there are enough numbers it throw the row to self.columns
        """
        column = []
        for index in range(0, self.m):
            for row in self.rows:
                if len(column) < self.n:
                    column.append(row[index])
                else:
                    self.columns.append(column)
                    column = [row[index]]
            self.columns.append(column)

    def update_values(self, values):
        self.values = values
        self.create_columns_rows()

    def update_row(self, index, new_row):
        values = []
        if len(new_row) == self.m:
            self.rows[index] = new_row
            for row in self.rows:
                for value in row:
                    values.append(value)
            self.update_values(values)

    def transposed(self):
        """Change the columns for the rows and vice versa"""
        values = []
        for column in self.columns:
            for index in range(0, len(column)):
                values.append(column[index])
        return Matrix(values, self.m, self.n)

    def negative(self):
        """return the matrix multiplied by -1"""
        return multiply(self, -1)


def same_dimension(matrix_a, matrix_b):
    """Check if two matrix are can be multiplied"""
    if matrix_a.n == matrix_b.m:
        return True
    else:
        return False


def multiply(matrix_a, matrix_b):
    """Multiply two matrix if is possible"""
    values = []
    value = 0
    # If there's two matrix, then multiply them usually
    if type(matrix_a) and type(matrix_b) == Matrix:
        if same_dimension(matrix_a, matrix_b):
            for row in matrix_a.rows:
                for column in matrix_b.columns:
                    for index in range(0, matrix_a.m):
                        value += row[index] * column[index]
                    values.append(value)
                    value = 0

        return Matrix(values, matrix_a.n, matrix_b.m)
    # If there's a matrix and a number, check witch is the
    # number and then multiply them
    else:
        if type(matrix_a) == Matrix:
            number = matrix_b
            matrix = matrix_a
        else:
            number = matrix_a
            matrix = matrix_b

        for row in matrix.rows:
            for index in range(0, len(row)):
                values.append(row[index] * number)

        return Matrix(values, matrix.n, matrix.m)


def multiply_row(row, number):
    new_row = []
    for value in row:
        new_row.append(value * number)
    return new_row


def add(matrix_a, matrix_b):
    """Add two matrix if it's possible"""
    values = []
    if same_dimension(matrix_a, matrix_b):
        for index in range(0, len(matrix_a.values)):
            values.append(matrix_a.values[index] + matrix_b.values[index])
        return Matrix(values, matrix_a.n, matrix_a.m)
    else:
        return False
