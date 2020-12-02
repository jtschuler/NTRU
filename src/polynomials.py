"""
Copyright 2020
Jadon Schuler & Justin Baum
Polynomial Utility Functions
polynomials.py
"""

"""
A polynomial will be a 0 indexed list.
3 + 2x + 5x^2
[3, 2, 5]
0 + 5x + 0x^2 + 11x^3
[0, 5, 0, 11]
"""

import utils
from sympy import Matrix

# pylint: disable=invalid-name

def normalize(polynomial1, polynomial2):
    l = max(len(polynomial1), len(polynomial2))
    poly1 = [polynomial1[i] if polynomial1[i] else 0 for i in range(l)]
    poly2 = [polynomial2[i] if polynomial2[i] else 0 for i in range(l)]
    return (poly1, poly2)

def multiplication(polynomial1, polynomial2, modulus):
    """
    Convolution product
    >>> multiplication([1,2,3],[2,5,7],3)
    [31, 30, 23]
    """
    (poly1, poly2) = normalize(polynomial1, polynomial2)
    l = len(poly1)
    result = [0 for i in range(l)]
    for i in range(l):
        for j in range(l):
            index = (i+j) % l 
            result[index] += poly1[i] * poly2[j]
            #result[index] %= modulus
    return result

def addition(polynomial1, polynomial2, modulus):
    """
    >>> addition([1,2,3], [2,5,7], 3)
    [3, 7, 10]
    """
    poly1 = [polynomial1[i] if polynomial1[i] else 0 for i in range(modulus)]
    poly2 = [polynomial2[i] if polynomial2[i] else 0 for i in range(modulus)]
    return [poly1[i] + poly2[i] for i in range(modulus)]

def subtraction(polynomial1, polynomial2, modulus):
    """
    >>> subtraction([1,2,3], [0,1,2], 3)
    [1, 1, 1]
    """
    l = max(len(polynomial1), len(polynomial2))
    poly1 = [polynomial1[i] if polynomial1[i] else 0 for i in range(l)]
    poly2 = [polynomial2[i] if polynomial2[i] else 0 for i in range(l)]
    return [poly1[i] - poly2[i] for i in range(l)]

def trim(poly_):
    """
    >>> trim([1,2,3,4,0,0,6,0,0,0])
    [1, 2, 3, 4, 0, 0, 6]
    """
    poly = [i for i in poly_]
    while len(poly) > 0 and poly[-1] == 0:
        poly = poly[:-1]
    return poly

def degree(poly):
    """
    >>> degree([1,2,3,0,0,0])
    2
    >>> degree([1,2,3,5,0,0,0,1,2,3,4,5,0,0])
    11
    """
    return len(trim(poly)) - 1

def leading_coefficient(poly):
    """
    >>> leading_coefficient([1,2,3,0,0,0])
    3
    >>> leading_coefficient([1,2,3,5,0,0,0,1,2,3,4,5,0,0])
    5
    """
    return trim(poly)[-1]

def getnullmatrix(polynomial, N):
    """
    >>> getnullmatrix([-1,1,1], 5)
    [[-1, 0, 0, 1, 1, 1], [1, -1, 0, 0, 1, 0], [1, 1, -1, 0, 0, 0], [0, 1, 1, -1, 0, 0], [0, 0, 1, 1, -1, 0]]
    """
    """
    Linear Algebra
    [a,b,c] * [d,e,f] (mod p/q) = 1
    [
    ad + bf + ce = 1, 
    ae + db + fc = 0, 
    af + dc + be = 0
    ]
        2f, 1d, 3e, 1
        3f, 2d, 1e, 0
        1f, 3d, 2e, 0
    [f[2,1,3], d[3,2,1], e[1,3,2],[1,0,0]] solve for f d e (mod p)
    [
[-1,  0,  0,  1,  1, 1],
[ 1, -1,  0,  0,  1, 0],
[ 1,  1, -1,  0,  0, 0],
[ 0,  1,  1, -1,  0, 0],
[ 0,  0,  1,  1, -1, 0]]
    """
    d = degree(polynomial)
    matrix = [[0 for _ in range(N+1)] for _ in range(N)]
    matrix[0][N] = 1
    for i in range(N):
        for j in range(d+1):
            matrix[(i+j) % N][i] = polynomial[j]
    return matrix

def getnullvector(polynomial, modulus : int, N):
    """
    >>> getnullvector([-1,1,1], 16, 5)
    [10, 9, 3, 12, 15]
    >>> getnullvector([-1,1,1], 3, 5)
    [2, 0, 2, 2, 1]
    """
    matrix = Matrix(getnullmatrix(polynomial, N))
    solution = (-matrix.nullspace()[0])[:-1]
    for i in range(len(solution)):
        if solution[i].q != 1:
            solution = [solution[i]*solution[i].q for i in range(len(solution))]
        break
    magic_number = sum(solution)
    m = utils.multiplicative_inverse(magic_number, modulus)
    solution = list(map(lambda x: (m*(x % modulus)) , solution))
    solution = list(map(lambda x: x % modulus, solution))
    return solution

def getinverse(polynomial, modulus : int, N):
    """
    >>> getinverse([-1,1,1], 16, 5)
    [10, 9, 3, 12, 15]
    >>> getinverse([-1,1,1], 3, 5)
    [2, 0, 2, 2, 1]
    """
    d = degree(polynomial)
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(d+1):
            matrix[(i+j) % N][i] = polynomial[j]

    matrix = Matrix(matrix)
    det = matrix.det()

    # We can remove this since there will always be a solution lol
    # Just a sanity check
    if det == 0:
        print('singular matrix')
        exit()

    matrix_inv = matrix.inv() * det * utils.multiplicative_inverse(det, modulus)

    v = [0 for _ in range(N)]
    v[0] = 1
    v = Matrix(v)

    result = matrix_inv * v
    inverse = [result[i] % modulus for i in range(len(result))]

    return inverse




if __name__ == "__main__":
    import doctest
    doctest.testmod()
