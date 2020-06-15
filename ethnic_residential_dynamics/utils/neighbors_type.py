"""Functions to count same neighbors and neighbors in general."""
import numpy as np

CLOSE_NEIGHBOURHOOD = 3
MAP_ALL_CITIZEN = {
    -1: 1,
    0: 0,
    1: 1,
    2: 0,
}


def _get_small_neighborhood(matrix: np.ndarray, i: int, j: int) -> np.ndarray:
    """Return 3*3 matrix where matrix[i, j] is the center."""
    limit_inf_i, limit_inf_j = max(0, i - 1), max(0, j - 1)
    limit_sup_i = min(limit_inf_i + CLOSE_NEIGHBOURHOOD, i + CLOSE_NEIGHBOURHOOD - 1)
    limit_sup_j = min(limit_inf_j + CLOSE_NEIGHBOURHOOD, j + CLOSE_NEIGHBOURHOOD - 1)

    return matrix[limit_inf_i:limit_sup_i, limit_inf_j:limit_sup_j].flatten()


def count_neighbors(matrix: np.ndarray, i: int, j: int) -> int:
    """Return the number of neighbors."""
    res = _get_small_neighborhood(matrix=matrix, i=i, j=j)
    return sum([MAP_ALL_CITIZEN[x] for x in res]) - MAP_ALL_CITIZEN[matrix[i, j]]


def count_same_color_neighbors(
    matrix: np.ndarray, i: int, j: int, default: int = None
) -> int:
    """Return the number of neighbors that have the same color skin."""
    res = _get_small_neighborhood(matrix=matrix, i=i, j=j)
    map_numbers = {key: 0 for key in MAP_ALL_CITIZEN}
    if default:
        map_numbers[default] = 1
    else:
        map_numbers[matrix[i, j]] = 1
    return sum([map_numbers[x] for x in res]) - map_numbers[matrix[i, j]]
