"""
Calculadora Sistema Ecuaciones by Rodrigo Gámez Triviño 3ºESO B

"""
from copy import deepcopy
from matrix import Matrix
import matrix


values = [1, 1, -2, 9,
          2, 1, 4, 4,
          2, -1, 6, -1,
          ]

c_v = [1, 1,
       1, 1
       ]


def equation_input():
    n = int(input('How many rows has the matrix?:'))
    m = int(input('How many columns has the matrix?:'))

    raw_rows = []
    for i in range(1, n + 1):
        raw_rows.append(input('Write the {} row. at the end write a dot:'
                              .format(i)))

    unknowns = []
    rows = []
    strnum = ''
    for raw_row in raw_rows:
        row = []
        for char in raw_row:
            if char.isdigit():
                strnum += char
            elif char.isalpha():
                unknowns.append(char)
                row.append(int(strnum))
                strnum = ''
            elif char == '-' or '+' and not '=':
                strnum += char
            elif char == '.':
                row.append(int(strnum))
                strnum = ''
        rows.append(row)

    values = []
    for row in rows:
        for value in row:
            values.append(value)

    return Matrix(values, n, m), unknowns


def gauss_method(system):
    """Use gauss method to triangulate a system of equations"""
    new_matrix = deepcopy(system)
    new_matrix.rows.reverse()
    for index in range(0, system.m - 2):
        for index_row in range(0, system.n - 1 - index):
            row = new_matrix.rows[index_row]
            next_row = new_matrix.rows[index_row + 1]
            k = row[index] / next_row[index]
            new_row = matrix.add(row, matrix.multiply_row(next_row, -k))
            new_matrix.update_row(index_row, new_row)
    return new_matrix


def main():
    a, unknowns = equation_input()
    print(a.rows)
    a = gauss_method(a)

    print(a.rows)


if __name__ == '__main__':
    main()
