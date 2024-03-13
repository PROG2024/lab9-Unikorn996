"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
from circle import Circle


class TestCircle(unittest.TestCase):

    def setUp(self):
        """Set up."""
        self.c1 = Circle(3)
        self.c2 = Circle(4)
        self.c3 = Circle(5)

    def test_area(self):
        """Test areas."""
        self.assertEqual(self.c1.get_area(), 28.274333882308138)
        self.assertEqual(self.c2.get_area(), 50.26548245743669)
        self.assertEqual(self.c3.get_area(), 78.53981633974483)

    def test_normal_add(self):
        """Test normal cases of add_area."""
        c12 = self.c1.add_area(self.c2)
        c23 = self.c2.add_area(self.c3)
        self.assertEqual(c12.radius, 5.0)
        self.assertEqual(c23.radius, 6.4031242374328485)

    def test_illegal_case(self):
        """Test illegal cases of radii."""
        with self.assertRaises(ValueError):
            c4 = Circle(-1)

