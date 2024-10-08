#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.
    """
    mtype_e = "matrix must be a matrix (list of lists) of integers/floats"
    mlen_e = "Each row of the matrix must have the same size"
    dtype_e = "div must be a number"
    dzero_e = "division by zero"
    mempty_e = "matrix can't be empty"
    float_not_int = "cannot convert float NaN to integer"
    float_not_inf = "cannot convert float infinity to integer"

    if not isinstance(div, (int, float)):
        raise TypeError(dtype_e)
    if div == 0:
        raise ZeroDivisionError(dzero_e)

    if not isinstance(matrix, list) or matrix == [] or matrix == [[]]:
        raise ValueError(mempty_e)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(mtype_e)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(mlen_e)
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(mtype_e)
            if isinstance(num, float) and (num != num or num in [float('inf'), float('-inf')]):
                if num != num:
                    raise ValueError(float_not_int)
                else:
                    raise OverflowError(float_not_inf)
    
    # Return the divided matrix
    return [[round(num / div, 2) for num in row] for row in matrix]
