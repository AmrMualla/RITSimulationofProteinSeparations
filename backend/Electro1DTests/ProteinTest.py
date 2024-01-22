# @author Amr Mualla, Mack Leonard
# Testing for Protein Class
# To run: python3 -m unittest backend.Electro1DTests.ProteinTest
import unittest

from Bio.SeqUtils.ProtParam import ProteinAnalysis

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

    def test_get_decider(self):
        self.protein.decider = 1
        self.assertEqual(self.protein.get_decider(), 1)

    def test_set_decider(self):
        self.protein.decider = 0
        self.protein.set_decider(1)
        self.assertEqual(self.protein.get_decider(), 1)

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

    def test_parse_orchid_protein(self):
        with open("Electro1DSampleTestFiles/ls_orchid.fasta") as file:
            parsed_sequence = self.protein.parse_protein(file)
        self.assertIsInstance(parsed_sequence, dict)
    def test_get_orchid_mw(self):
        expected_mw = 5604122.421700024
        actual_mw = 0
        with open("Electro1DSampleTestFiles/ls_orchid.fasta") as file:
            mw_list = self.protein.get_mw(file)
        for item in mw_list:
            actual_mw += item
        print()
        print("Expected orchid molecular weight: ", expected_mw)
        print("Actual orchid molecular weight: ", actual_mw)
        print()
        self.assertEqual(expected_mw, actual_mw)

    def test_get_orchid_amino_acid_count(self):
        expected_amino_acid_count = {'A': 135, 'C': 136, 'D': 0, 'E': 0, 'F': 0, 'G': 160, 'H': 0, 'I': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 161, 'V': 0, 'W': 0, 'Y': 0}
        with open("Electro1DSampleTestFiles/ls_orchid.fasta") as file:
            actual_amino_acid_count = self.protein.get_amino_acid_count(file)
        self.assertIn(expected_amino_acid_count, actual_amino_acid_count)

    def test_parse_e_coliK12_protein(self):
        with open("Electro1DSampleTestFiles/e_coliK12.faa") as file:
            parsed_sequence = self.protein.parse_protein(file)
        self.assertIsInstance(parsed_sequence, dict)

    def test_get_e_coliK12_mw(self):
        expected_mw = 150560054.08059993
        actual_mw = 0
        with open("Electro1DSampleTestFiles/e_coliK12.faa") as file:
            mw_list = self.protein.get_mw(file)
        for item in mw_list:
            actual_mw += item
        print()
        print("Expected E. coli K12 molecular weight: ", expected_mw)
        print("Actual E. coli K12 molecular weight: ", actual_mw)
        print()
        self.assertEqual(expected_mw, actual_mw)

    def test_get_ecoliK12_amino_acid_cound(self):
        expected_amino_acid_count = {'A': 30, 'C': 1, 'D': 16, 'E': 12, 'F': 4, 'G': 9, 'H': 8, 'I': 12, 'K': 8, 'L': 30, 'M': 8, 'N': 5, 'P': 8, 'Q': 11, 'R': 13, 'S': 11, 'T': 17, 'V': 16, 'W': 3, 'Y': 6}
        with open("Electro1DSampleTestFiles/e_coliK12.faa") as file:
            actual_amino_acid_count = self.protein.get_amino_acid_count(file)
        self.assertIn(expected_amino_acid_count, actual_amino_acid_count)

    def test_standards_mw(self):
        expected_mw = 396728.9295000013
        actual_mw = 0
        with open("Electro1DSampleTestFiles/electrophoresis1dStandards.fasta") as file:
            mw_list = self.protein.get_mw(file)
        print(mw_list)
        for item in mw_list:
            actual_mw += item
        print()
        print("Expected standards molecular weight: ", expected_mw)
        print("Actual standards molecular weight: ", actual_mw)
        print()
        self.assertEqual(expected_mw, actual_mw)

    def test_random(self):
        with open("Electro1DSampleTestFiles/electrophoresis1dStandards.fasta") as file:
            parsed_protein = self.protein.parse_protein(file)
        for record_id in parsed_protein:
            protein = parsed_protein.get(record_id)[0].split(", ")
            print(parsed_protein)
            print(protein[0])

    def test_individual_mw(self):
        with open("Electro1DSampleTestFiles/electrophoresis1dStandards.fasta") as file:
            expected_mw_list = self.protein.get_mw(file)
        with open("Electro1DSampleTestFiles/electrophoresis1dStandards.fasta") as file:
            parsed_protein = self.protein.parse_protein(file)
        actual_mw_list = []
        for record_id in parsed_protein:
            protein = parsed_protein.get(record_id)
            sequence = ProteinAnalysis(protein[1])
            expected_individual_mw = sequence.molecular_weight()
            actual_mw_list.append(expected_individual_mw)

        print()
        print("Expected individual standard molecular weights: ", expected_mw_list)
        print("Actual individual standard molecular weights: ", actual_mw_list)
        print()
        self.assertEqual(expected_mw_list, actual_mw_list)


if __name__ == "__main__":
    unittest.main()
