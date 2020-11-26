from matrix import Matrix
import matrix

"""
Calculadora Sistema Ecuaciones by Rodrigo Gámez Triviño 3ºESO B

"""

values = [1, 3,
          2, 9,
          ]


def main():
    a = Matrix(values)
    print(a.m)
    print(a.n)
    print(a.rows)
    print(a.columns)
    b = a.get_transposed()
    print(b.m)
    print(b.n)
    print(b.rows)
    print(b.columns)
    print(matrix.multiplicable(a, b))
    print('\n')
    print(matrix.multiply(a, b).values)


if __name__ == '__main__':
    main()
