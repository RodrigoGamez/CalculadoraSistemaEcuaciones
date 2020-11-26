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
        """
        row = []
        for index in range(0, len(self.values) + 1):
            """
            When the row has less numbers than the length it adds a new num
            and when there are enough numbers it throw the row to self.rows
            """
            # Make the rows
            if len(row) < self.m:
                row.append(self.values[index])
            else:
                self.rows.append(row)
                # the try-except block is here for don't lose any row
                try:
                    row = [self.values[index]]
                except IndexError:
                    pass

        column = []
        for index in range(0, len(self.rows[0]) + 1):
            # get an index to go through each row
            if len(column) < self.n:
                for r in range(0, len(self.rows)):
                    # get each row numbers and take the correct
                    cache = self.rows[r]
                    column.append(cache[index])
            else:
                self.columns.append(column)
                column = []
                # the try-except block is here for don't lose any column
                try:
                    for r in range(0, len(self.rows)):
                        cache = self.rows[r]
                        column.append(cache[index])
                except IndexError:
                    pass

    def get_transposed(self):
        """Change the columns for the rows and vice versa"""
        values = []
        for column in self.columns:
            for index in range(0, len(column)):
                values.append(column[index])
        return Matrix(values, self.m, self.n)


def multiplicable(matrix_a, matrix_b):
    """Check if two matrix are can be multiplied"""
    if matrix_a.n == matrix_b.m:
        return True


def multiply(matrix_a, matrix_b):
    """Multiply two matrix if is possible"""
    values = []
    value = 0
    for index_row in range(0, matrix_a.n):
        for index_column in range(0, matrix_b.m):
            for index_number in range(0, matrix_a.m):
                row = matrix_a.rows[index_row]
                column = matrix_b.columns[index_column]
                value += row[index_number] * column[index_number]
            values.append(value)
            value = 0

    return Matrix(values, matrix_a.n, matrix_b.m)

# uwu owo
