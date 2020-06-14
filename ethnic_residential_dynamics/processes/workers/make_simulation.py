"""Worker to make simulations."""
from argparse import Namespace

import numpy as np

# from ethnic_residential_dynamics.utils.parser import get_command_line_parser
from ethnic_residential_dynamics.libs.init_matrix import perfect_distribution
from ethnic_residential_dynamics.libs.satisfaction import (
    get_unsatisfied,
    move_to_satisfaction,
)
from ethnic_residential_dynamics.utils.plot_matrix import plot_citizen_matrix
from ethnic_residential_dynamics.utils.unbalance_matrix import (
    add_citizens,
    remove_citizen,
)


def simulation(
    args: Namespace,
    size_population: int,
    count_remove: int,
    count_add: int,
    stop_satisfaction: int,
    stop_recursive: int,
):
    """Plot neighborhood and check the convergence."""
    matrix_model = perfect_distribution(matrix_size=size_population)
    matrix_model = remove_citizen(matrix=matrix_model, count_remove=count_remove)
    matrix_model = add_citizens(matrix=matrix_model, count_add=count_add)
    list_empty_spaces = np.argwhere(matrix_model == 0).tolist()

    for epoch in range(stop_satisfaction * (size_population ** 2)):

        # Plot neighborhood
        if (epoch % 4) == 0:
            plot_citizen_matrix(args=args, matrix=matrix_model, index=epoch)

        # Find an unsatisfied citizen
        unsatisfied_individual = get_unsatisfied(
            matrix_model=matrix_model,
            recursive_counter=0,
            stop_recursive=stop_recursive,
        )

        if unsatisfied_individual[0] == "Converge":
            plot_citizen_matrix(args=args, matrix=matrix_model, index=epoch)
            print("Convergence after: ", epoch + 1, " iterations")
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

# matrix_solution = simulation(
#     args=get_command_line_parser().parse_args(),
#     size_population=n,
#     count_remove=m,
#     count_add=p,
#     stop_satisfaction=alpha,
#     stop_recursive=beta,
# )
