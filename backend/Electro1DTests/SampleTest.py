# @author Chase Amador
# Testing for Sample Class
# To run: python3 -m unittest backend.Electro1DTests.SampleTest
import unittest
from backend.Electro1D.Sample import *


# TODO MISSING 1 GUI METHOD TEST
class TestSample(unittest.TestCase):

    def setUp(self):
        self.sample_obj = Sample()

    def test_initialization(self):
        self.assertEqual(self.sample_obj.samp_x, 0)
        self.assertEqual(self.sample_obj.samp_y, 0)
        self.assertEqual(self.sample_obj.max_y, 0)
        self.assertEqual(self.sample_obj.samp_width, 0)
        self.assertEqual(self.sample_obj.samp_height, 0)
        self.assertEqual(self.sample_obj.fill_counter, 0)
        self.assertEqual(self.sample_obj.fill_ratio, 0)
        self.assertFalse(self.sample_obj.change_on)
        self.assertFalse(self.sample_obj.fill_switch)
        self.assertFalse(self.sample_obj.empty_switch)

    def test_reset(self):
        self.sample_obj.reset()
        self.assertEqual(self.sample_obj.samp_x, 0)
        self.assertEqual(self.sample_obj.samp_y, 0)
        self.assertEqual(self.sample_obj.max_y, 0)
        self.assertEqual(self.sample_obj.samp_width, 0)
        self.assertEqual(self.sample_obj.samp_height, 0)
        self.assertEqual(self.sample_obj.fill_counter, 0)
        self.assertEqual(self.sample_obj.fill_ratio, 0)
        self.assertFalse(self.sample_obj.change_on)
        self.assertFalse(self.sample_obj.fill_switch)
        self.assertFalse(self.sample_obj.empty_switch)

    def test_set_x_position(self):
        self.sample_obj.set_x_position(5)
        self.assertEqual(self.sample_obj.samp_x, 5)
        self.sample_obj.set_x_position(5.5)
        self.assertEqual(self.sample_obj.samp_x, 5.5)

    def test_set_y_position(self):
        self.sample_obj.set_y_position(10)
        self.assertEqual(self.sample_obj.samp_y, 10)
        self.sample_obj.set_y_position(10.5)
        self.assertEqual(self.sample_obj.samp_y, 10.5)

    def test_set_max_y(self):
        self.sample_obj.set_max_y(15)
        self.assertEqual(self.sample_obj.max_y, 15)
        self.sample_obj.set_max_y(15.5)
        self.assertEqual(self.sample_obj.max_y, 15.5)

    def test_set_width(self):
        self.sample_obj.set_width(3)
        self.assertEqual(self.sample_obj.samp_width, 3)
        self.sample_obj.set_width(3.5)
        self.assertEqual(self.sample_obj.samp_width, 3.5)

    def test_draw_switch(self):
        self.sample_obj.draw_switch(True)
        self.assertTrue(self.sample_obj.change_on)

        self.sample_obj.draw_switch(False)
        self.assertFalse(self.sample_obj.change_on)

    def test_empty(self):
        self.sample_obj.empty()
        self.assertFalse(self.sample_obj.fill_switch)
        self.assertTrue(self.sample_obj.empty_switch)

if __name__ == '__main__':
    unittest.main()
