"""Tests for parser."""
import unittest

from ethnic_residential_dynamics.utils.parser import get_command_line_parser


class ParserTest(unittest.TestCase):
    """Class to test parser."""

    def setUp(self):
        """Set up a parser."""
        self.parser = get_command_line_parser()

    def test_get_command_line_parser(self):
        """Should return a parser with given arguments."""
        parsed = self.parser.parse_args(["--plots_path", "plots"])
        self.assertEqual(parsed.plots_path, "plots")
