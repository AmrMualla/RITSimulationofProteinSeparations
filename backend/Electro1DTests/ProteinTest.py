# @author Amr Mualla
# Testing for Protein Class
# To run: python3 -m unittest src.Electro1DTests.ProteinTest
import unittest
from backend.Electro1D.Protein import Protein

class TestProtein(unittest.TestCase):

    def setUp(self):
        self.protein = Protein()

    def test_default_values(self):
        self.assertEqual(self.protein.name, "notSet")
        self.assertEqual(self.protein.full_name, "notSet")
        self.assertEqual(self.protein.abbr, "notSet")
        self.assertEqual(self.protein.mw, 0)
        self.assertEqual(self.protein.color, (0, 0, 255))

    def test_set_start_position(self):
        self.protein.set_start_position(10, 20)
        self.assertEqual(self.protein.x1, 10)
        self.assertEqual(self.protein.y1, 20)
        self.assertEqual(self.protein.start_y, 20)
        self.assertEqual(self.protein.y1_float, 20.0)

    def test_reset_decider(self):
        self.protein.decider = 5
        self.protein.counter = 3
        self.protein.reset_decider()
        self.assertEqual(self.protein.decider, 1)
        self.assertEqual(self.protein.counter, 1)

    def test_incr_position(self):
        self.protein.y1_float = 10.0
        self.protein.speed = 1.0
        self.protein.incr_position()
        self.assertEqual(self.protein.y1_float, 11.0)
        self.assertEqual(self.protein.y1, 11)

    def test_match_position(self):
        self.protein.x1 = 10
        self.protein.y1 = 10
        self.protein.width = 5
        self.protein.height = 5
        self.assertTrue(self.protein.match_position(11, 11))
        self.assertFalse(self.protein.match_position(20, 20))

    def test_set_width(self):
        self.protein.set_width(10)
        self.assertEqual(self.protein.width, 10)

    def test_set_concentration(self):
        self.protein.set_concentration(5)
        self.assertEqual(self.protein.concentration, 5)

    def test_match_plot_position(self):
        self.protein.plot_x_pos = 10
        self.protein.plot_y_pos = 10
        self.assertTrue(self.protein.match_plot_position(11, 11))
        self.assertFalse(self.protein.match_plot_position(20, 20))

    def test_get_distance(self):
        self.protein.y1 = 15
        self.protein.start_y = 10
        self.protein.scale_factor = 2
        self.assertEqual(self.protein.get_distance(), 10.0)


if __name__ == "__main__":
    unittest.main()
