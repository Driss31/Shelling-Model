"""Tests for unbalance_matrix functions."""
import numpy as np

from ethnic_residential_dynamics.utils.unbalance_matrix import (
    _check_if_empty_or_edge,
    add_citizens,
    remove_citizen,
)


def test_check_if_empty_or_edge():
    """Should not return indexes of zeros and coins."""
    answer = _check_if_empty_or_edge(
        matrix=np.array([[2, 1, -1, 2], [1, 0, 0, 0], [-1, 1, -1, 0], [2, -1, 1, 2]]),
        size_mat=4,
        indexes=(1, 1),
    )
    assert answer not in [(1, 1), (1, 2), (1, 3), (2, 3)]


def test_remove_citizen():
    """Should remove 15 zeros and avoid indexes of zeros and coins."""
    answer = remove_citizen(
        matrix=np.array(
            [
                [2.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 2.0],
                [1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0],
                [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0],
                [1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0],
                [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0],
                [1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0],
                [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0],
                [1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0],
                [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0],
                [2.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, 2.0],
            ]
        ),
        count_remove=15,
    )

    assert 10 * 10 - np.count_nonzero(a=answer) == 15


def test_add_citizens():
    """Should put citizen on 5 zeros from a matrix with 10 zeros."""
    answer = add_citizens(
        matrix=np.array(
            [
                [2.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 2.0],
                [1.0, 0.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0],
                [-1.0, 1.0, -1.0, 1.0, -1.0, 0.0, -1.0, 0.0, -1.0, 1.0],
                [1.0, -1.0, 1.0, 0.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0],
                [-1.0, 1.0, -1.0, 1.0, -1.0, 0.0, -1.0, 1.0, -1.0, 1.0],
                [1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, 0.0, 1.0, -1.0],
                [-1.0, 1.0, 0.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0],
                [1.0, -1.0, 1.0, 0.0, 1.0, 0.0, 1.0, -1.0, 0.0, -1.0],
                [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0],
                [2.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, 2.0],
            ]
        ),
        count_add=5,
    )

    assert 10 * 10 - np.count_nonzero(a=answer) == 5
