"""Tests for adequate citizen."""
import numpy as np
import pytest

from ethnic_residential_dynamics.libs.fit import most_suited_citizen


@pytest.fixture(name="empty_neighborhood")
def neighborhood_mock():
    """Return a matrix 10*10."""
    return np.array(
        [
            [2.0, 0.0, -1.0, -1.0, -1.0, 0.0, -1.0, -1.0, 0.0, 2.0],
            [0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0, 1.0, -1.0, 1.0, 0.0, 0.0, 0.0, -1.0],
            [0.0, -1.0, 0.0, 1.0, 0.0, -1.0, 0.0, 0.0, 1.0, 0.0],
            [-1.0, 0.0, 0.0, 0.0, -1.0, 0.0, -1.0, 1.0, -1.0, 1.0],
            [1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 1.0, -1.0],
            [0.0, 0.0, 0.0, -1.0, -1.0, -1.0, 0.0, 0.0, 1.0, 0.0],
            [-1.0, -1.0, 0.0, 0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 1.0],
            [0.0, 0.0, -1.0, -1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0],
            [2.0, 0.0, 1.0, -1.0, -1.0, -1.0, 1.0, 0.0, 0.0, 2.0],
        ]
    )


def test_most_suited_citizen_no_citizen(empty_neighborhood):
    """Should return 2."""
    answer = most_suited_citizen(matrix=empty_neighborhood, i=1, j=0)
    assert answer == 2


def test_most_suited_citizen_0(empty_neighborhood):
    """Should return 1."""
    answer = most_suited_citizen(matrix=empty_neighborhood, i=2, j=7)
    assert answer == 1


def test_most_suited_citizen_1(empty_neighborhood):
    """Should return 1."""
    answer = most_suited_citizen(matrix=empty_neighborhood, i=4, j=3)
    assert answer == 0


def test_most_suited_citizen_2(empty_neighborhood):
    """Should return -1."""
    answer = most_suited_citizen(matrix=empty_neighborhood, i=9, j=8)
    assert answer == -1


def test_most_suited_citizen_3(neighborhood):
    """Should return 1."""
    answer = most_suited_citizen(matrix=neighborhood, i=0, j=0)
    assert answer == 1


def test_most_suited_citizen_4(empty_neighborhood):
    """Should return -1."""
    answer = most_suited_citizen(matrix=empty_neighborhood, i=1, j=1)
    assert answer == -1


def test_most_suited_citizen_6(empty_neighborhood):
    """Should return 0."""
    answer = most_suited_citizen(matrix=empty_neighborhood, i=3, j=2)
    assert answer == 0


def test_most_suited_citizen_7(empty_neighborhood):
    """Should return -1."""
    answer = most_suited_citizen(
        matrix=np.array([[-1, -1, -1], [-1, 0, -1], [-1, -1, -1]]), i=1, j=1
    )
    assert answer == -1


def test_most_suited_citizen_8(neighborhood):
    """Should return 1 as most satisfied citizen in empty house in middle."""
    answer = most_suited_citizen(matrix=neighborhood, i=8, j=7)
    assert answer == 1


def test_most_suited_citizen_9(empty_neighborhood):
    """Should return 0."""
    answer = most_suited_citizen(matrix=empty_neighborhood, i=3, j=4)
    assert answer == 0
