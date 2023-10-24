# @author Chase Amador
# Testing for Constants Class
# To run: python3 -m unittest backend.Electro1DTests.ConstantsTest
import unittest

class TestConstants(unittest.TestCase):

    def test_convert_color_to_rgb(self):
        # Test with the provided dyeColor
        expected_rgb_color = (132, 50, 237)
        actual_rgb_color = Constants.convert_color_to_rgb(Constants.dyeColor)
        self.assertEqual(actual_rgb_color, expected_rgb_color)

        # Test with a different color
        different_color = (255, 0, 0)  # Red
        expected_different_rgb_color = (255, 0, 0)
        actual_different_rgb_color = Constants.convert_color_to_rgb(different_color)
        self.assertEqual(actual_different_rgb_color, expected_different_rgb_color)

        # Test with black color
        black_color = (0, 0, 0)
        expected_black_rgb_color = (0, 0, 0)
        actual_black_rgb_color = Constants.convert_color_to_rgb(black_color)
        self.assertEqual(actual_black_rgb_color, expected_black_rgb_color)

        # Test with white color
        white_color = (255, 255, 255)
        expected_white_rgb_color = (255, 255, 255)
        actual_white_rgb_color = Constants.convert_color_to_rgb(white_color)
        self.assertEqual(actual_white_rgb_color, expected_white_rgb_color)

if __name__ == '__main__':
    unittest.main()
