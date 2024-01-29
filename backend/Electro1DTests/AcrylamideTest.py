# @author Chase Amador
# Testing for Acrylamide Class
# To run: python3 -m unittest backend.Electro1DTests.AcrylamideTest
import unittest
from backend.Electro1D.Acrylamide import Acrylamide

class TestAcrylamide(unittest.TestCase):

    # Checks if the initialization of the Acrylamide object sets the properties correctly.
    def test_initialization(self):
        acrylamide_obj = Acrylamide("10.0%", 11.0)
        self.assertEqual(acrylamide_obj.percent_gel, "10.0%")
        self.assertEqual(acrylamide_obj.concentration, 11.0)
        self.assertEqual(acrylamide_obj.suppressor, 3)  # Based on the provided logic in set_suppressor method

    # Tests the get_conc method
    def test_get_conc(self):
        acrylamide_obj = Acrylamide("8.0%", 9.0)
        self.assertEqual(acrylamide_obj.get_conc(), 9.0)

    # Tests the set_suppressor method with different concentration values
    def test_set_suppressor(self):
        acrylamide_obj = Acrylamide("12.0%", 13.0)
        self.assertEqual(acrylamide_obj.suppressor, 6)

        acrylamide_obj.set_suppressor(11.0)
        self.assertEqual(acrylamide_obj.suppressor, 3)

        acrylamide_obj.set_suppressor(8.0)
        self.assertEqual(acrylamide_obj.suppressor, 2)

        acrylamide_obj.set_suppressor(5.0)
        self.assertEqual(acrylamide_obj.suppressor, 1)

        acrylamide_obj.set_suppressor(12.5)
        self.assertEqual(acrylamide_obj.suppressor, 6)

        acrylamide_obj.set_suppressor(10.5)
        self.assertEqual(acrylamide_obj.suppressor, 3)

        acrylamide_obj.set_suppressor(7.5)
        self.assertEqual(acrylamide_obj.suppressor, 1)

if __name__ == '__main__':
    unittest.main()