"""Parser to get input arguments."""
from argparse import ArgumentParser


def get_command_line_parser() -> ArgumentParser:
    """Standard command line parser."""
    parser = ArgumentParser()
    parser.add_argument("--plots_path", help="Path to save plots.", required=True)

    return parser
