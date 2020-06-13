"""Code made 2 years ago. To update."""
from random import randint

from matplotlib import colors
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np


def perfect_distribution(matrix_size):
    """Returns a matrix (n * n) containing alternate '1' and '-1' except in corners where we put '2'
     we choose n even"""

    first_row = [2]  # First row of the matrix
    last_row = [2]  # Last row of the matrix
    middle_row_1 = []
    middle_row_2 = []
    #  Add alternately 1 and -1 in rows
    # First and last rows
    one_or_minus_one = 1
    for i in range(matrix_size - 2):
        first_row.append(one_or_minus_one)
        one_or_minus_one = -one_or_minus_one
        last_row.append(one_or_minus_one)
    first_row.append(2)
    last_row.append(2)

    # Middle rows
    one_or_minus_one = 1
    for i in range(matrix_size):
        middle_row_1.append(one_or_minus_one)
        one_or_minus_one = -one_or_minus_one
        middle_row_2.append(one_or_minus_one)

    # Create matrix model
    matrix_list = first_row  # List that will contain all '1', '-1' and '2'
    for i in range((matrix_size - 2) // 2):
        matrix_list += middle_row_1 + middle_row_2
    matrix_list += last_row
    matrix_model = np.reshape(
        matrix_list, (matrix_size, matrix_size)
    )  # Creating the matrix from the list

    return matrix_model


def same_neighbors(distribution_matrix, i, j):
    """For a given distribution (distribution_matrix), and for a given house (i, j), it returns the number of neighbors
     that have the same color skin"""

    same_color = 0
    size_dist_mat = len(distribution_matrix)
    if (
        i >= 1
        and j >= 1
        and distribution_matrix[i - 1][j - 1] == distribution_matrix[i][j]
    ):
        same_color += 1
    if i >= 1 and distribution_matrix[i - 1][j] == distribution_matrix[i][j]:
        same_color += 1
    if (
        i >= 1
        and j <= size_dist_mat - 2
        and distribution_matrix[i - 1][j + 1] == distribution_matrix[i][j]
    ):
        same_color += 1
    if j >= 1 and distribution_matrix[i][j - 1] == distribution_matrix[i][j]:
        same_color += 1
    if (
        j <= size_dist_mat - 2
        and distribution_matrix[i][j + 1] == distribution_matrix[i][j]
    ):
        same_color += 1
    if (
        i <= size_dist_mat - 2
        and j >= 1
        and distribution_matrix[i + 1][j - 1] == distribution_matrix[i][j]
    ):
        same_color += 1
    if (
        i <= size_dist_mat - 2
        and distribution_matrix[i + 1][j] == distribution_matrix[i][j]
    ):
        same_color += 1
    if (
        i <= size_dist_mat - 2
        and j <= size_dist_mat - 2
        and distribution_matrix[i + 1][j + 1] == distribution_matrix[i][j]
    ):
        same_color += 1

    return same_color


def remove_citizen(matrix_origin, nbr_remove):
    """ Removes randomly nbr_remove of '1' and '-1' from matrix_origin and returns the new matrix """

    new_matrix = matrix_origin.copy()
    size_mat = len(matrix_origin)
    for k in range(nbr_remove):
        i = randint(0, size_mat - 1)
        j = randint(0, size_mat - 1)
        while (
            new_matrix[i][j] == 0 or new_matrix[i][j] == 2
        ):  # if no citizen, look somewhere else
            i = randint(0, size_mat - 1)
            j = randint(0, size_mat - 1)
        new_matrix[i][j] = 0

    return new_matrix


def index_empty(matrix_model):
    """ Returns a list of empty space indexes"""

    size_mat = len(matrix_model)
    list_index = []
    for i in range(size_mat):
        for j in range(size_mat):
            if matrix_model[i][j] == 0:
                list_index.append([i, j])

    return list_index


def add_citizens(matrix_remove, nbr_add):
    """Adds nbr_add '1' and '-1' randomly chosen in the empty spaces (where there is 0)"""

    new_matrix = matrix_remove.copy()
    list_zeros = index_empty(
        matrix_remove
    )  # List containing indexes of zeros in the matrix

    for i in range(nbr_add):
        random_elt = randint(0, 9)
        new_matrix[list_zeros[random_elt][0]][
            list_zeros[random_elt][1]
        ] = np.random.choice([-1, 1], 1)[0]

    return new_matrix


def number_neighbors(matrix_model, i, j):
    """ Returns the number of neighbors matrix_model(i, j) has in the matrix_model"""

    nbr_neighbors = 0
    size_mat = len(matrix_model)
    if i >= 1 and j >= 1 and matrix_model[i - 1][j - 1] not in [0, 2]:
        nbr_neighbors += 1
    if i >= 1 and matrix_model[i - 1][j] not in [0, 2]:
        nbr_neighbors += 1
    if i >= 1 and j <= size_mat - 2 and matrix_model[i - 1][j + 1] not in [0, 2]:
        nbr_neighbors += 1
    if j >= 1 and matrix_model[i][j - 1] not in [0, 2]:
        nbr_neighbors += 1
    if j <= size_mat - 2 and matrix_model[i][j + 1] not in [0, 2]:
        nbr_neighbors += 1
    if i <= size_mat - 2 and j >= 1 and matrix_model[i + 1][j - 1] not in [0, 2]:
        nbr_neighbors += 1
    if i <= size_mat - 2 and matrix_model[i + 1][j] not in [0, 2]:
        nbr_neighbors += 1
    if (
        i <= size_mat - 2
        and j <= size_mat - 2
        and matrix_model[i + 1][j + 1] not in [0, 2]
    ):
        nbr_neighbors += 1

    return nbr_neighbors


def empty_preference(matrix_model, i, j):
    """Returns '1' or '-1' or '0' representing the citizen that would be the most satisfied in matrix_model(i, j)
    depending on the conditions of satisfaction"""

    matrix_test = matrix_model.copy()
    nbr_neighbors = number_neighbors(matrix_test, i, j)
    matrix_test[i][j] = 1
    nbr_ones = same_neighbors(matrix_test, i, j)
    matrix_test[i][j] = -1
    nbr_minus_one = same_neighbors(matrix_test, i, j)

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


def move_to_satisfaction(matrix_model, list_empty_index, i, j):
    """ For a citizen matrix_model(i, j), if we find an empty space from list_empty_index where he is satisfied, we
    change his place in matrix_model"""

    if matrix_model[i][j] == 1:
        for indexes in list_empty_index:
            if empty_preference(matrix_model, indexes[0], indexes[1]) >= 0:
                matrix_model[indexes[0]][indexes[1]] = 1  # new place in the matrix
                matrix_model[i][j] = 0  # old place in the matrix
                list_empty_index.remove(indexes)
                list_empty_index.append([i, j])
                return matrix_model
        return matrix_model

    if matrix_model[i][j] == -1:
        for item in list_empty_index:
            if empty_preference(matrix_model, item[0], item[1]) <= 0:
                matrix_model[item[0]][item[1]] = -1
                matrix_model[i][j] = 0
                list_empty_index.remove(item)
                list_empty_index.append([i, j])
                return matrix_model
        return matrix_model


def unsatisfied(matrix_model, recursive_counter, stop_recursive):
    """ Recursive function that randomly looks for an unsatisfied citizen and then returns its coordinates.
    If this function is called more than stop_recursive without finding any unsatisfied citizen, we consider that all citizens
    are satisfied"""

    size_mat = len(matrix_model)

    while recursive_counter < stop_recursive * (size_mat ** 2):  # convergence criterion

        i = randint(0, size_mat - 1)
        j = randint(0, size_mat - 1)
        nbr_neighbors = number_neighbors(matrix_model, i, j)
        nbr_same = same_neighbors(matrix_model, i, j)
        if matrix_model[i][j] != 1 and matrix_model[i][j] != -1:
            recursive_counter += 1
            return unsatisfied(matrix_model, recursive_counter, stop_recursive)
        else:
            if nbr_neighbors == 0:
                recursive_counter += 1
                return unsatisfied(matrix_model, recursive_counter, stop_recursive)
            # Conditions of satisfaction
            elif 0 < nbr_neighbors < 3 and nbr_same >= 1:
                recursive_counter += 1
                return unsatisfied(matrix_model, recursive_counter, stop_recursive)
            elif 2 < nbr_neighbors < 6 and nbr_same >= 2:
                recursive_counter += 1
                return unsatisfied(matrix_model, recursive_counter, stop_recursive)
            elif 5 < nbr_neighbors and nbr_same >= 3:
                recursive_counter += 1
                return unsatisfied(matrix_model, recursive_counter, stop_recursive)
            else:
                # Dissatisfaction
                return i, j

    return "Converge", recursive_counter


def unsatisfied2(matrix_model, stop_recursive):
    """ Calls unsatisfied function """
    c = 0
    return unsatisfied(matrix_model, c, stop_recursive)


def simulation(
    size_population, nbr_remove, number_add, stop_satisfaction, stop_recursive
):
    """ Plots the progress of the model matrix and returns the convergence """

    matrix_model = perfect_distribution(
        size_population
    )  # We create a perfect distribution
    matrix_model = remove_citizen(
        matrix_model, nbr_remove
    )  # We randomly remove some citizens
    matrix_model = add_citizens(
        matrix_model, number_add
    )  # We randomly add somme citizens in the empty spaces
    list_empty_spaces = index_empty(matrix_model)

    for i in range(stop_satisfaction * (size_population ** 2)):

        # Tracking progress after each 4 iterations
        if (i % 4) == 0:
            data = matrix_model
            plt.figure(i)
            cmap = colors.ListedColormap(["black", "white", "red"])
            plt.imshow(data, interpolation="nearest", cmap=cmap)
            red_patch = mpatches.Patch(color="red", label="Population A")
            black_patch = mpatches.Patch(color="black", label="Population B")
            white_patch = mpatches.Patch(color="white", label="Vacant homes")
            plt.legend(handles=[white_patch, red_patch, black_patch])
            plt.legend(handles=[red_patch])
            plt.legend(handles=[black_patch])
            plt.show()

        unsatisfied_individual = unsatisfied2(
            matrix_model, stop_recursive
        )  # Find an unsatisfied citizen

        if (
            unsatisfied_individual[0] == "Converge"
        ):  # If everyone is satisfied (convergence criterion)
            data = matrix_model
            plt.figure(1)
            cmap = colors.ListedColormap(["black", "white", "red"])
            plt.imshow(data, interpolation="nearest", cmap=cmap)
            red_patch = mpatches.Patch(color="red", label="Population A")
            black_patch = mpatches.Patch(color="black", label="Population B")
            white_patch = mpatches.Patch(color="white", label="Vacant homes")
            plt.legend(handles=[white_patch, red_patch, black_patch])
            plt.show()
            plt.figure(2)
            plt.pcolor(np.flipud(data))
            print("Convergence after: ", i + 1, " iterations")
            return matrix_model
        else:
            matrix_model = move_to_satisfaction(
                matrix_model,
                list_empty_spaces,
                unsatisfied_individual[0],
                unsatisfied_individual[1],
            )

    return "No convergence", matrix_model


# Simulation
n = 10
m = 40
p = 15
alpha = 3
beta = 6

# matrix_solution = simulation(n, m, p, alpha, beta)
# print(matrix_solution)
