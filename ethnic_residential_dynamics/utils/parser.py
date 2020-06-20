"""Parser to get input arguments."""
from argparse import ArgumentParser


def get_command_line_parser() -> ArgumentParser:
    """Standard command line parser."""
    parser = ArgumentParser()
    parser.add_argument(
        "--plots_path", help="Path to save plots.", type=str, required=True
    )
    parser.add_argument(
        "--size_population", help="Size of matrix.", type=int, required=True
    )
    parser.add_argument(
        "--count_remove", help="Number of citizens to remove.", type=int, required=True
    )
    parser.add_argument(
        "--count_add", help="Number of citizens to remove.", type=int, required=True
    )
    parser.add_argument(
        "--stop_satisfaction",
        help="Number of times to multiply matrix size to get max epochs.",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--stop_recursive", help="Integer to stop recursivity.", type=int, required=True
    )
    return parser
