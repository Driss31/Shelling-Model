"""Function to find unsatisfied citizens."""
from random import randint
from ethnic_residential_dynamics.utils.neighbors_type import count_same_color_neighbors, count_neighbors, most_suited_citizen
import numpy as np


def _check_satisfied_neighborhood(recursive_counter: int, stop_recursive: int, matrix_size: int) -> bool:
    """Check if there are still unsatisfied citizen."""
    return recursive_counter >= stop_recursive * (matrix_size ** 2)


def get_unsatisfied(matrix_model: np.ndarray, recursive_counter: int, stop_recursive: int):
    """Recursive function that randomly looks for an unsatisfied citizen and returns its coordinates.

    Note:
        If this function is called more than `stop_recursive` without finding any unsatisfied citizen,
        we consider that all citizens are satisfied.
    """
    matrix_size = len(matrix_model)
    while not _check_satisfied_neighborhood(recursive_counter=recursive_counter, stop_recursive=stop_recursive,
                                            matrix_size=matrix_size):

        i = randint(0, matrix_size - 1)
        j = randint(0, matrix_size - 1)
        nbr_neighbors = count_neighbors(matrix_model, i, j)
        nbr_same = count_same_color_neighbors(matrix_model, i, j)
        if matrix_model[i][j] != 1 and matrix_model[i][j] != -1:
            recursive_counter += 1
            return get_unsatisfied(matrix_model, recursive_counter, stop_recursive)
        else:
            if nbr_neighbors == 0:
                recursive_counter += 1
                return get_unsatisfied(matrix_model, recursive_counter, stop_recursive)
            # Conditions of satisfaction
            elif 0 < nbr_neighbors < 3 and nbr_same >= 1:
                recursive_counter += 1
                return get_unsatisfied(matrix_model, recursive_counter, stop_recursive)
            elif 2 < nbr_neighbors < 6 and nbr_same >= 2:
                recursive_counter += 1
                return get_unsatisfied(matrix_model, recursive_counter, stop_recursive)
            elif 5 < nbr_neighbors and nbr_same >= 3:
                recursive_counter += 1
                return get_unsatisfied(matrix_model, recursive_counter, stop_recursive)
            else:
                # Dissatisfaction
                return i, j

    return "Converge", recursive_counter


def move_to_satisfaction(matrix_model, list_empty_index, i, j):
    """Move an unsatisfied citizen to a house where he can be satisfied if found."""
    if matrix_model[i][j] == 1:
        for indexes in list_empty_index:
            if most_suited_citizen(matrix=matrix_model, i=indexes[0], j=indexes[1]) >= 0:
                matrix_model[indexes[0]][indexes[1]] = 1  # new place in the matrix
                matrix_model[i][j] = 0  # old place in the matrix
                list_empty_index.remove(indexes)
                list_empty_index.append([i, j])
                return matrix_model
        return matrix_model

    if matrix_model[i][j] == -1:
        for item in list_empty_index:
            if most_suited_citizen(matrix=matrix_model, i=item[0], j=item[1]) <= 0:
                matrix_model[item[0]][item[1]] = -1
                matrix_model[i][j] = 0
                list_empty_index.remove(item)
                list_empty_index.append([i, j])
                return matrix_model
        return matrix_model
