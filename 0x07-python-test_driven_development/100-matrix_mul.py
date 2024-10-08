#!/usr/bin/python3
"""
This module provides a function to multiply two matrices.
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices (m_a and m_b) and returns the resulting matrix.

    Args:
        m_a (list of lists of int/float): First matrix.
        m_b (list of lists of int/float): Second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers/floats.
        ValueError: If m_a or m_b is empty or the matrices cannot be multiplied.
        TypeError: If m_a or m_b contains non-numeric elements or is not rectangular.

    Returns:
        list of lists of int/float: The result of the matrix multiplication.
    """
    # Validate that m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Validate that m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check that m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Check that each element in m_a and m_b is either an integer or a float
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    # Validate that m_a and m_b are rectangular
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Validate that the matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum_product = 0
            for k in range(len(m_b)):
                sum_product += m_a[i][k] * m_b[k][j]
            row.append(sum_product)
        result.append(row)

    return result
