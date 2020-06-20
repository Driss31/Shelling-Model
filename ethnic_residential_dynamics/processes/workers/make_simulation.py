"""Worker to make simulations."""
from argparse import Namespace
from typing import Optional

import numpy as np

from ethnic_residential_dynamics.libs.init_matrix import perfect_distribution
from ethnic_residential_dynamics.libs.satisfaction import (
    get_unsatisfied,
    move_to_satisfaction,
)
from ethnic_residential_dynamics.utils.parser import get_command_line_parser
from ethnic_residential_dynamics.utils.plot_matrix import plot_citizen_matrix
from ethnic_residential_dynamics.utils.unbalance_matrix import (
    add_citizens,
    remove_citizen,
)


def simulation(args: Namespace,) -> Optional[bool]:
    """Plot neighborhood and check the convergence."""
    matrix_model = perfect_distribution(matrix_size=args.size_population)
    plot_citizen_matrix(args=args, matrix=matrix_model, index=0)

    matrix_model = remove_citizen(matrix=matrix_model, count_remove=args.count_remove)
    plot_citizen_matrix(args=args, matrix=matrix_model, index=1)

    matrix_model = add_citizens(matrix=matrix_model, count_add=args.count_add)
    plot_citizen_matrix(args=args, matrix=matrix_model, index=2)

    list_empty_spaces = np.argwhere(matrix_model == 0).tolist()

    for epoch in range(2, args.stop_satisfaction * (args.size_population ** 2) + 2):

        # Plot neighborhood
        if (epoch % 2) == 0:
            plot_citizen_matrix(args=args, matrix=matrix_model, index=epoch + 1)

        # Find an unsatisfied citizen
        unsatisfied_individual = get_unsatisfied(
            matrix_model=matrix_model,
            recursive_counter=0,
            stop_recursive=args.stop_recursive,
        )

        if unsatisfied_individual[0] == "Converge":
            plot_citizen_matrix(args=args, matrix=matrix_model, index=epoch + 1)
            print("Convergence after: ", epoch + 1, " iterations")
            return True
        else:
            matrix_model = move_to_satisfaction(
                matrix_model,
                list_empty_spaces,
                unsatisfied_individual[0],
                unsatisfied_individual[1],
            )

    print("No convergence", matrix_model)  # pragma: no cover


if __name__ == "__main__":
    simulation(args=get_command_line_parser().parse_args())

# Simulation
# n = 15
# m = 60
# p = 30
# alpha = 3
# beta = 6
