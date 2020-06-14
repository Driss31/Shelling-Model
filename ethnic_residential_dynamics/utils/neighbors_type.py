"""Functions to count same neighbors and neighbors in general."""
import numpy as np


def count_neighbors(matrix: np.ndarray, i: int, j: int) -> int:
    """Return the number of neighbors matrix_model(i, j) has."""
    nbr_neighbors = 0
    size_mat = len(matrix)
    if i >= 1 and j >= 1 and matrix[i - 1][j - 1] not in [0, 2]:
        nbr_neighbors += 1
    if i >= 1 and matrix[i - 1][j] not in [0, 2]:
        nbr_neighbors += 1
    if i >= 1 and j <= size_mat - 2 and matrix[i - 1][j + 1] not in [0, 2]:
        nbr_neighbors += 1
    if j >= 1 and matrix[i][j - 1] not in [0, 2]:
        nbr_neighbors += 1
    if j <= size_mat - 2 and matrix[i][j + 1] not in [0, 2]:
        nbr_neighbors += 1
    if i <= size_mat - 2 and j >= 1 and matrix[i + 1][j - 1] not in [0, 2]:
        nbr_neighbors += 1
    if i <= size_mat - 2 and matrix[i + 1][j] not in [0, 2]:
        nbr_neighbors += 1
    if i <= size_mat - 2 and j <= size_mat - 2 and matrix[i + 1][j + 1] not in [0, 2]:
        nbr_neighbors += 1

    return nbr_neighbors


def count_same_color_neighbors(matrix: np.ndarray, i: int, j: int) -> int:
    """Returns the number of neighbors that have the same color skin."""
    same_color = 0
    size_dist_mat = len(matrix)
    if i >= 1 and j >= 1 and matrix[i - 1][j - 1] == matrix[i][j]:
        same_color += 1
    if i >= 1 and matrix[i - 1][j] == matrix[i][j]:
        same_color += 1
    if i >= 1 and j <= size_dist_mat - 2 and matrix[i - 1][j + 1] == matrix[i][j]:
        same_color += 1
    if j >= 1 and matrix[i][j - 1] == matrix[i][j]:
        same_color += 1
    if j <= size_dist_mat - 2 and matrix[i][j + 1] == matrix[i][j]:
        same_color += 1
    if i <= size_dist_mat - 2 and j >= 1 and matrix[i + 1][j - 1] == matrix[i][j]:
        same_color += 1
    if i <= size_dist_mat - 2 and matrix[i + 1][j] == matrix[i][j]:
        same_color += 1
    if (
        i <= size_dist_mat - 2
        and j <= size_dist_mat - 2
        and matrix[i + 1][j + 1] == matrix[i][j]
    ):
        same_color += 1

    return same_color


def most_suited_citizen(matrix: np.ndarray, i: int, j: int):
    """Return '1' or '-1' or '0' representing the citizen that would be the most satisfied."""
    matrix_test = matrix.copy()
    nbr_neighbors = count_neighbors(matrix_test, i, j)
    matrix_test[i][j] = 1
    nbr_ones = count_same_color_neighbors(matrix_test, i, j)
    matrix_test[i][j] = -1
    nbr_minus_one = count_same_color_neighbors(matrix_test, i, j)

    # Conditions of satisfaction
    if nbr_neighbors == 0:
        return 2
    if nbr_neighbors == 1 or nbr_neighbors == 2:
        if nbr_ones == 0:
            return -1
        elif nbr_minus_one == 0:
            return 1
        else:
            return 0
    if 3 <= nbr_neighbors <= 5:
        if nbr_ones <= 1:
            return -1
        elif nbr_minus_one <= 1:
            return 1
        else:
            return 0
    if 6 <= nbr_neighbors <= 8:
        if nbr_ones <= 2:
            return -1
        elif nbr_minus_one <= 2:
            return 1
        else:
            return 0
