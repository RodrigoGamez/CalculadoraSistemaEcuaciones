from matrix import Matrix
import matrix

"""
Calculadora Sistema Ecuaciones by Rodrigo Gámez Triviño 3ºESO B

"""

values = [1, 3,
          2, 9,
          ]

c_v = [1, 1,
       1, 1
       ]


def main():
    a = Matrix(values)
    c = Matrix(c_v)
    print(a.m)
    print(a.n)
    print(a.rows)
    print(a.columns)
    b = a.transposed()
    print(b.m)
    print(b.n)
    print(b.rows)
    print(b.columns)
    print(matrix.same_dimension(a, b))
    print('\n')
    print(matrix.multiply(a, 2).values)
    print(matrix.add(a, c.negative()).values)


if __name__ == '__main__':
    main()
