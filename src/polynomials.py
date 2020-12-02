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

def multiplication(polynomial1, polynomial2, modulus):
    """
    Convolution product
    >>> multiplication([1,2,3],[2,5,7],3)
    [31, 30, 23]
    """
    poly1 = [polynomial1[i] if polynomial1[i] else 0 for i in range(modulus)]
    poly2 = [polynomial2[i] if polynomial2[i] else 0 for i in range(modulus)]
    result = [0 for i in range(modulus)]
    for i in range(modulus):
        for j in range(modulus):
            index = (i+j) % modulus
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
    poly1 = [polynomial1[i] if polynomial1[i] else 0 for i in range(modulus)]
    poly2 = [polynomial2[i] if polynomial2[i] else 0 for i in range(modulus)]
    return [poly1[i] - poly2[i] for i in range(modulus)]

def trim(poly_):
    """
    >>> trim([1,2,3,4,0,0,6,0,0,0])
    [1, 2, 3, 4, 0, 0, 6]
    """
    poly = [i for i in poly_]
    while poly[-1] == 0:
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

def division(polynomial1, polynomial2, modulus):
    """
    """
    poly1 = trim(polynomial1)
    poly2 = trim(polynomial2)
    # 0 polynomial
    q = [0 for _ in polynomial1]
    # deep copy of polynomial 1
    r = [i for i in polynomial1]
    d = degree(polynomial1)
    c = polynomial2[-1]
    while degree(r) >= d:
        
    


def inverse(polynomial, modulus):
    """
    >>> pass
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
    """
    pass




if __name__ == "__main__":
    import doctest
    doctest.testmod()
