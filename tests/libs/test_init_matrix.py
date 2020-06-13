"""Tests for matrix initialization"""
import numpy as np
from numpy.testing import assert_equal

from ethnic_residential_dynamics.libs.init_matrix import (
    _validate_even,
    perfect_distribution,
)


def test_validate_even_n_even():
    """Should return same even value."""
    answer = _validate_even(n=10)
    assert answer == 10


def test_validate_even_n_odd():
    """Should return n+1 since n is odd."""
    answer = _validate_even(n=9)
    assert answer == 10


def test_perfect_distribution():
    """Should return a 6x6 perfect citizen matrix."""
    answer = perfect_distribution(matrix_size=6)
    assert_equal(
        answer,
        np.array(
            [
                [2, 1, -1, 1, -1, 2],
                [1, -1, 1, -1, 1, -1],
                [-1, 1, -1, 1, -1, 1],
                [1, -1, 1, -1, 1, -1],
                [-1, 1, -1, 1, -1, 1],
                [2, -1, 1, -1, 1, 2],
            ]
        ),
    )
