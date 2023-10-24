# @author Chase Amador
# Testing for Pipette Class
# To run: python3 -m unittest backend.Electro1DTests.PipetteTest
import unittest

class TestPipette(unittest.TestCase):

    def setUp(self):
        self.pipette_obj = Pipette()

    def test_initialization(self):
        self.assertEqual(self.pipette_obj.gap, 6)
        self.assertEqual(self.pipette_obj.speed, 2.0)
        self.assertEqual(self.pipette_obj.pipette_coords_x, [0, 0, 0, 0])
        self.assertEqual(self.pipette_obj.pipette_coords_y, [0, 0, 0, 0])
        self.assertEqual(self.pipette_obj.pipette_coords_y_f, [0, 0, 0, 0])
        self.assertEqual(self.pipette_obj.empty_tip, 4)
        self.assertIsInstance(self.pipette_obj.sample, Sample)
        self.assertFalse(self.pipette_obj.dropped)
        self.assertFalse(self.pipette_obj.emptied)
        self.assertFalse(self.pipette_obj.has_sample)
        self.assertFalse(self.pipette_obj.retracted)

    def test_set_sample_depth(self):
        self.pipette_obj.set_sample_depth(10)
        self.assertEqual(self.pipette_obj.sample_depth, 10)

    def test_incr_position(self):
        self.assertTrue(self.pipette_obj.incr_position())
        self.assertFalse(self.pipette_obj.dropped)
        self.assertFalse(self.pipette_obj.emptied)
        self.assertFalse(self.pipette_obj.retracted)

    def test_fill_well(self):
        # Assuming fill_well method modifies the internal state, test for side effects
        self.pipette_obj.fill_well(None)
        self.assertFalse(self.pipette_obj.dropped)
        self.assertFalse(self.pipette_obj.emptied)
        self.assertFalse(self.pipette_obj.retracted)

    def test_set_sample(self):
        new_sample = Sample()
        self.pipette_obj.set_sample(new_sample)
        self.assertEqual(self.pipette_obj.sample, new_sample)

    def test_reset_flags(self):
        self.pipette_obj.reset_flags()
        self.assertFalse(self.pipette_obj.dropped)
        self.assertFalse(self.pipette_obj.emptied)
        self.assertFalse(self.pipette_obj.has_sample)
        self.assertFalse(self.pipette_obj.retracted)

    def test_set_start_x_position(self):
        self.pipette_obj.set_start_x_position(5)
        self.assertEqual(self.pipette_obj.x1, 5)
        self.assertEqual(self.pipette_obj.y1, 0)
        self.assertEqual(self.pipette_obj.y1_float, 0.0)
        self.assertEqual(self.pipette_obj.pipette_coords_x, [1, 3, 7, 9])
        self.assertEqual(self.pipette_obj.pipette_coords_y, [0, 0, 0, 0])
        self.assertEqual(self.pipette_obj.pipette_coords_y_f, [0, 0, 0, 0])

    def test_set_max_y_position(self):
        self.pipette_obj.set_max_y_position(20)
        self.assertEqual(self.pipette_obj.max_y_position, 14)
        self.assertEqual(self.pipette_obj.well_bottom, 20)

if __name__ == '__main__':
    unittest.main()
