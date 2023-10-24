# @author Chase Amador
# Testing for Parameters Class
# To run: python3 -m unittest backend.Electro1DTests.ParametersTest
import unittest

# TODO MISSING MULTIPLE GUI METHOD TESTS
class TestBioClasses(unittest.TestCase):

    def test_protein(self):
        protein = Protein("TestProtein", "TestFullProtein", "TestAbbr", 100, "red")
        self.assertEqual(protein.name, "TestProtein")
        self.assertEqual(protein.full_name, "TestFullProtein")
        self.assertEqual(protein.abbr, "TestAbbr")
        self.assertEqual(protein.mw, 100)
        self.assertEqual(protein.color, "red")
        self.assertEqual(protein.speed, 0.0)
        self.assertFalse(protein.selected)
        self.assertFalse(protein.decider)

        protein.set_decider(True)
        self.assertTrue(protein.decider)

        protein.reset_decider()
        self.assertFalse(protein.decider)

    def test_acrylamide(self):
        acrylamide = Acrylamide("6%", 12.0)
        self.assertEqual(acrylamide.percent_gel, "6%")
        self.assertEqual(acrylamide.suppressor, 12.0)

    def test_electrophoresis(self):
        electrophoresis = Electrophoresis()
        self.assertEqual(electrophoresis.selected_speed, Constants.medium)
        self.assertIsNone(electrophoresis.selected_sample)
        self.assertIsNone(electrophoresis.selected_gel)
        self.assertEqual(electrophoresis.std1_ref, 0)

        gel = Acrylamide("6%", 12.0)
        electrophoresis.set_acrylamide(gel)
        self.assertEqual(electrophoresis.selected_gel, gel)

        electrophoresis.set_animation_speed(Constants.high)
        self.assertEqual(electrophoresis.selected_speed, Constants.high)

    # TODO cant test rest of methods in electrophoresis

    def test_constants(self):
        self.assertEqual(Constants.slow, "Slow")
        self.assertEqual(Constants.medium, "Moderate")
        self.assertEqual(Constants.fast, "Fast")
        self.assertEqual(Constants.low, 1.0)
        self.assertEqual(Constants.medium, 1.5)
        self.assertEqual(Constants.high, 2.0)
        self.assertEqual(Constants.highX2, 4.0)

        self.assertIsInstance(Constants.gel1, Acrylamide)
        self.assertIsInstance(Constants.gel2, Acrylamide)
        self.assertIsInstance(Constants.gel3, Acrylamide)
        self.assertIsInstance(Constants.gel4, Acrylamide)

    # TODO cant test the Parameters methods because they are all GUI related

if __name__ == '__main__':
    unittest.main()
