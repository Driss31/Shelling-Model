"""Functions to add and remove citizens."""
from random import choice, randint
from typing import Tuple

import numpy as np


def _check_if_empty_or_edge(
    matrix: np.ndarray, size_mat: int, indexes: Tuple[int, int]
) -> Tuple[int, int]:
    """Check if matrix[indexes] is not 0 or 2."""
    i, j = indexes
    while matrix[i][j] == 0 or matrix[i][j] == 2:  # if no citizen, look somewhere else
        i, j = randint(0, size_mat - 1), randint(0, size_mat - 1)
    return i, j


def remove_citizen(matrix: np.ndarray, count_remove: int) -> np.ndarray:
    """Remove randomly `count_remove` of citizens '1' and '-1' from `matrix`.

    Return the new matrix.
    """
    size_mat = len(matrix)
    for _ in range(count_remove):
        i, j = _check_if_empty_or_edge(
            matrix=matrix,
            size_mat=size_mat,
            indexes=(randint(0, size_mat - 1), randint(0, size_mat - 1)),
        )
        matrix[i][j] = 0

    return matrix


def add_citizens(matrix: np.ndarray, count_add: int) -> np.ndarray:
    """Add `count_add` citizens '1' and '-1' randomly chosen in the empty spaces (where there is 0)."""
    zeros_indexes = np.argwhere(matrix == 0)
    for _ in range(count_add):
        empty_idx = choice(range(len(zeros_indexes)))
        # Add citizen
        matrix[zeros_indexes[empty_idx][0]][
            zeros_indexes[empty_idx][1]
        ] = np.random.choice([-1, 1], 1)[0]
        zeros_indexes = np.delete(zeros_indexes, empty_idx, axis=0)

    return matrix
