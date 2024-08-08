"""
Unit tests for the get_color_from_pair_number function in the misaligned module.
"""
import unittest
from misaligned import get_color_map, get_color_from_pair_number

class TestColorMap(unittest.TestCase):
    """Unit test for color map functionality."""

    def test_color_pair_and_pair_number_separately(self):
        """Test each element of the color map individually."""
        color_map, color_combinations = get_color_map()
        for i, color in enumerate(color_map):
            pair_number = i + 1
            major_color, minor_color = get_color_from_pair_number(pair_number)
            expected_color = color.split(" | ")[1:]
            expected_pair_number = int(color.split(" | ")[0])
            self.assertEqual(major_color, expected_color[0])
            self.assertEqual(minor_color, expected_color[1])
            self.assertEqual(pair_number, expected_pair_number)

        # Check the color combinations result
        self.assertEqual(color_combinations, 25)

if __name__ == '__main__':
    unittest.main()
    