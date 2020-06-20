"""Tests for worker make_simulation."""
import os

from ethnic_residential_dynamics.processes.workers.make_simulation import simulation
from ethnic_residential_dynamics.utils.parser import get_command_line_parser

PNG = "png"


def test_simulation():
    """Should save graphs in plots/tests."""
    parser = get_command_line_parser()
    parsed = parser.parse_args(
        [
            "--plots_path",
            "plots/tests",
            "--size_population",
            "10",
            "--count_remove",
            "40",
            "--count_add",
            "20",
            "--stop_satisfaction",
            "3",
            "--stop_recursive",
            "6",
        ]
    )

    # Delete all files from directory
    filelist = [f for f in os.listdir(parsed.plots_path)]
    for f in filelist:
        os.remove(os.path.join(parsed.plots_path, f))

    # Make simulation
    simulation(args=parsed)

    plots = [
        filename for filename in os.listdir(parsed.plots_path) if filename.endswith(PNG)
    ]
    assert len(plots) > 0
