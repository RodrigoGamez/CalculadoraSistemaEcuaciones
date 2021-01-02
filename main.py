"""
Calculadora Sistema Ecuaciones by Rodrigo Gámez Triviño 3ºESO B

"""
from copy import deepcopy
from matrix import *
import matrix


a = [2, 2,
     -3, 0
     ]

c_v = [1, 1,
       1, 1
       ]


def equation_input():
    n = int(input('How many rows has the matrix?:'))
    m = int(input('How many columns has the matrix?:'))

    raw_rows = []
    for i in range(0, n):
        raw_rows.append(input('Write the {} row:'
                              .format(i + 1)))

    unknowns = []
    rows = []
    strdigit = ''
    space = False
    for raw_row in raw_rows:
        row = []
        for char in raw_row:
            if char.isalpha() or char.isspace():
                if space:
                    unknowns.append(char)
                    row.append(int(strdigit))
                    strdigit = ''
                    space = False
                else:
                    pass
            elif char.isdigit():
                space = True
                strdigit += char
            elif char == '-':
                strdigit += char
            else:
                pass
        rows.append(row)

    values = []
    for row in rows:
        for value in row:
            values.append(value)

    return Matrix(values, n, m), unknowns


def gauss_method(matrix_system):
    """Use gauss method to triangulate a system of equations"""
    new_matrix = deepcopy(matrix_system)
    new_matrix.rows.reverse()
    for index in range(0, matrix_system.m - 2):
        for index_row in range(0, matrix_system.n - 1 - index):
            row = new_matrix.rows[index_row]
            next_row = new_matrix.rows[index_row + 1]
            k = row[index] / next_row[index]
            new_row = matrix.add(row, matrix.multiply_row(next_row, -k))
            new_matrix.update_row(index_row, new_row)
            new_matrix.rows.reverse()
    return new_matrix


def inverse_matrix_gauss(matr):
    """Use gauss method to get the inverse of a matrix"""
    new_matrix = deepcopy(matr)
    if new_matrix.n == new_matrix.m:
        for step in range(0, new_matrix.n):
            for row in new_matrix.rows:
                if new_matrix.rows.index(row) == step:
                    row.append(1)
                else:
                    row.append(0)

        new_matrix = gauss_method(new_matrix)
        print(new_matrix.rows)
                
    else:
        print('the inverse cannot be calculated')


def main():
    print(a)
    inverse_matrix_gauss(Matrix(a))


if __name__ == '__main__':
    main()
