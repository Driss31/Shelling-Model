"""Define rules to determine the most satisfied citizen in an empty house."""
import numpy as np

from ethnic_residential_dynamics.utils.neighbors_type import count_same_color_neighbors


def most_suited_citizen(matrix: np.ndarray, i: int, j: int) -> int:
    """Return '1' or '-1' or '0' representing the citizen that would be the most satisfied."""
    count_pos_neighbors = count_same_color_neighbors(matrix=matrix, i=i, j=j, default=1)
    count_neg_neighbors = count_same_color_neighbors(
        matrix=matrix, i=i, j=j, default=-1
    )
    count_all_neighbors = count_pos_neighbors + count_neg_neighbors

    # Conditions of satisfaction
    if not count_all_neighbors:
        return 2

    if count_all_neighbors in [1, 2]:
        if not count_pos_neighbors:
            return -1
        elif not count_neg_neighbors:
            return 1
        else:
            return 0

    if count_all_neighbors in [3, 4, 5]:
        if count_pos_neighbors <= 1:
            return -1
        elif count_neg_neighbors <= 1:
            return 1
        else:
            return 0

    if count_pos_neighbors <= 2:
        return -1
    elif count_neg_neighbors <= 2:
        return 1

    return 0
