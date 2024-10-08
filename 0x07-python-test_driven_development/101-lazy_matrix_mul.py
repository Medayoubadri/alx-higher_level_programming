#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy's matmul function.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        A new matrix which is the product of m_a and m_b.
    """
    return np.matmul(m_a, m_b)
