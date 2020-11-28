"""
Calculadora Sistema Ecuaciones by Rodrigo Gámez Triviño 3ºESO B

"""
from matrix import Matrix
import matrix


values = [1, 1, -2, 9,
          2, -1, 4, 4,
          2, -1, 6, -1,
          ]

c_v = [1, 1,
       1, 1
       ]


def gauss_method(system):
    """Use gauss method to resolve a system of equations"""
    for index in range(0, system.m - 2):
        for index_row in range(0, system.n - 1 - index):
            row = system.rows[index_row]
            next_row = system.rows[index_row + 1]
            k = row[index] / next_row[index]
            new_row = matrix.add(row, matrix.multiply_row(next_row, -k))
            system.update_row(index_row, new_row)
    print(system.rows)


def main():
    a = Matrix(values, 3, 4)
    c = Matrix(c_v)

    gauss_method(a)


if __name__ == '__main__':
    main()
