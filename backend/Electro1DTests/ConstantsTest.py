# @author Chase Amador
# Testing for Constants Class
# To run: python3 -m unittest backend.Electro1DTests.ConstantsTest
import unittest
from backend.Electro1D.Constants import *


class TestConstants(unittest.TestCase):

    def test_convert_colors(self):
        # Test with the provided dyeColor
        expected_rgb_color = (132, 50, 237)
        actual_rgb_color = Constants.dyeColor
        self.assertEqual(actual_rgb_color, expected_rgb_color)

    def test_gel_percents(self):
        expected_gels = [("7.5%", 7.5), ("10%", 10), ("12%", 12), ("15%", 15)]
        for i in range(0, len(Constants.gels) - 1):
            self.assertEqual(expected_gels[i], Constants.gels[i])

    def test_constants(self):
        self.assertEqual(Constants.slow, "Slow")
        self.assertEqual(Constants.moderate, "Moderate")
        self.assertEqual(Constants.fast, "Fast")
        self.assertEqual(Constants.low, .75)
        self.assertEqual(Constants.medium, 1.0)
        self.assertEqual(Constants.high, 1.5)
        self.assertEqual(Constants.highX2, 2.0)

    def test_voltage(self):
        self.assertEqual(Constants.fiftyV, "50V")
        self.assertEqual(Constants.hundredV, "100V")
        self.assertEqual(Constants.oneFiftyV, "150V")
        self.assertEqual(Constants.twoHundredV, "200V")
        for i in range(0, len(Constants.voltageList)):
            self.assertEqual(Constants.voltageList[i], str(50 + 50 * i) + "V")

    def test_std_ref(self):
        self.assertEqual(Constants.std1Ref, 0)
        self.assertEqual(Constants.std2Ref, 1)
        self.assertEqual(Constants.std3Ref, 2)
        self.assertEqual(Constants.std4Ref, 3)
        self.assertEqual(Constants.std5Ref, 4)
        self.assertEqual(Constants.std6Ref, 5)
        self.assertEqual(Constants.std7Ref, 6)
        for i in range(0, len(Constants.standardIndices) - 1):
            self.assertEqual(Constants.standardIndices[i], i)


if __name__ == '__main__':
    unittest.main()
