"""
Unit tests for the size function in the tshirts module.
"""
import unittest
from tshirts import size

class TestSize(unittest.TestCase):
    """Unit tests for the size function."""

    def test_size_s(self):
        """Test size function for size S."""
        self.assertEqual(size(38), 'S')

    def test_size_m(self):
        """Test size function for size M."""
        self.assertEqual(size(42), 'M')

    def test_size_l(self):
        """Test size function for size L."""
        self.assertEqual(size(40), 'L')

if __name__ == '__main__':
    unittest.main()
