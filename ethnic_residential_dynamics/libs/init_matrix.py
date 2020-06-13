"""Function to initialize citizen matrix."""
import logging

import numpy as np

EMPTY_HOUSE = 2


def _validate_even(n: int) -> int:
    """Check if n is even."""
    if n % 2 == 0:
        logging.info(f"Matrix size given is odd: {n}. Fallback: {n+1}", fallback=n + 1)
        return n
    return n + 1


def perfect_distribution(matrix_size: int) -> np.ndarray:
    """Returns a matrix (matrix_size * matrix_size) containing alternate '1' and '-1'.

    Corners contain `2` as exceptions. matrix_size has to be even.
    """
    matrix_size = _validate_even(n=matrix_size)
    perfect_matrix = np.ones(shape=(matrix_size, matrix_size))
    for i in range(matrix_size):
        for j in range(matrix_size):
            if (i + j) % 2 == 0:
                perfect_matrix[i][j] = -1
    perfect_matrix[0][0] = perfect_matrix[0][-1] = perfect_matrix[-1][
        0
    ] = perfect_matrix[-1][-1] = EMPTY_HOUSE

    return perfect_matrix
