"""neighbors_type tests."""
import numpy as np
import pytest

from ethnic_residential_dynamics.utils.neighbors_type import (
    _get_small_neighborhood,
    count_neighbors,
    count_same_color_neighbors,
)


@pytest.fixture(name="neighborhood")
def neighborhood_mock():
    """Return a matrix 10*10."""
    return np.array(
        [
            [2.0, 0.0, -1.0, 1.0, -1.0, 1.0, 0.0, 1.0, -1.0, 2.0],
            [1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, -1.0, 1.0, -1.0],
            [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0, 0.0, 1.0, -1.0, 1.0],
            [1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 0.0, -1.0],
            [-1.0, 0.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0],
            [0.0, -1.0, 1.0, -1.0, 0.0, -1.0, 0.0, -1.0, -1.0, 1.0],
            [-1.0, 1.0, 0.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 0.0],
            [-1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, -1.0, 1.0, -1.0, 1.0, 0.0, 0.0, -1.0, 1.0],
            [2.0, -1.0, 0.0, -1.0, 1.0, -1.0, 1.0, 1.0, 1.0, 2.0],
        ]
    )


def test_get_small_neighborhood_middle(neighborhood):
    """Should return [[ 1. -1.  1.], [ 1.  0.  0.]]."""
    answer = _get_small_neighborhood(matrix=neighborhood, i=3, j=4)
    np.array_equal(
        answer, np.array([[1.0, -1.0, 1.0], [-1.0, 1.0, -1.0], [1.0, -1.0, 1.0]])
    )


def test_get_small_neighborhood_edge(neighborhood):
    """Should return [[ 1. -1.  1.], [ 1.  0.  0.]]."""
    answer = _get_small_neighborhood(matrix=neighborhood, i=0, j=4)
    np.array_equal(answer, np.array([[1.0, -1.0, 1.0], [1.0, 0.0, 0.0]]))


def test_count_neighbors_middle(neighborhood):
    """Should return 6."""
    answer = count_neighbors(matrix=neighborhood, i=1, j=1)
    assert answer == 6


def test_count_neighbors_edge(neighborhood):
    """Should return 1."""
    answer = count_neighbors(matrix=neighborhood, i=0, j=0)
    assert answer == 1


def test_count_same_color_neighbors_middle(neighborhood):
    """Should retrun 4."""
    answer = count_same_color_neighbors(matrix=neighborhood, i=2, j=4)
    assert answer == 2


def test_count_same_color_neighbors_edge(neighborhood):
    """Should retrun 4."""
    answer = count_same_color_neighbors(matrix=neighborhood, i=0, j=4)
    assert answer == 0


def test_count_same_color_neighbors_default(neighborhood):
    """Should retrun 4."""
    answer = count_same_color_neighbors(matrix=neighborhood, i=2, j=4, default=1)
    assert answer == 4
