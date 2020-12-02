# Copyright 2020
# Jadon Schuler & Justin Baum

class Polynomials:
    """
    A polynomial will be a 0 indexed list.
    3 + 2x + 5x^2
    [3, 2, 5]
    0 + 5x + 0x^2 + 11x^3
    [0, 5, 0, 11]
    """
    @staticmethod
    def multiplication(polynomial1, polynomial2, n):
        """
        >>> Polynomials.multiplication([1,2,3],[2,5,7],3)
        [31, 30, 23]
        """
        poly1 = [polynomial1[i] if polynomial1[i] else 0 for i in range(n)]
        poly2 = [polynomial2[i] if polynomial2[i] else 0 for i in range(n)]
        result = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                result[(i+j) % n] += poly1[i] * poly2[j]
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
