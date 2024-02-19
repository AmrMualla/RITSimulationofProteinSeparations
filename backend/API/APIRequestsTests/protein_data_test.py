import unittest
import requests


class ProteinDataTest(unittest.TestCase):
    def test_get_standards_api(self):
        response = requests.get('http://127.0.0.1:8000/1DElectrophoresis/standards?acrylamide=7.5&voltage=50')
        if response.status_code == 200:
            self.assertEqual(response.json(),[
                                              {
                                                "name": "D Chain D, Beta-galactosidase",
                                                "molecular_weight": 116062,
                                                "descent_speed": 1899.2587687983403,
                                                "ncbi_link": "https://www.ncbi.nlm.nih.gov/protein/6X1Q"
                                              },
                                              {
                                                "name": "A Chain A, GLYCOGEN PHOSPHORYLASE B",
                                                "molecular_weight": 97158,
                                                "descent_speed": 1870.3044623481403,
                                                "ncbi_link": "https://www.ncbi.nlm.nih.gov/protein/2PRI"
                                              },
                                              {
                                                "name": "B Chain B, Serum albumin",
                                                "molecular_weight": 66463,
                                                "descent_speed": 1808.4674776966513,
                                                "ncbi_link": "https://www.ncbi.nlm.nih.gov/protein/4F5S"
                                              },
                                              {
                                                "name": "Ovalbumin [Gallus gallus]",
                                                "molecular_weight": 43772,
                                                "descent_speed": 1740.4486464562715,
                                                "ncbi_link": "https://www.ncbi.nlm.nih.gov/protein/AAA68882.1"
                                              },
                                              {
                                                "name": "Carbonic anhydrase 2 [Mus musculus]",
                                                "molecular_weight": 29003,
                                                "descent_speed": 1673.416095971503,
                                                "ncbi_link": "https://www.ncbi.nlm.nih.gov/protein/NP_001344263.1"
                                              },
                                              {
                                                "name": "Pancreatic trypsin inhibitor [Musca domestica]",
                                                "molecular_weight": 22709,
                                                "descent_speed": 1633.5742538653608,
                                                "ncbi_link": "https://www.ncbi.nlm.nih.gov/protein/AFP63821.1"
                                              },
                                              {
                                                "name": "LYS_OSTED",
                                                "molecular_weight": 14918,
                                                "descent_speed": 1565.1414760559667,
                                                "ncbi_link": "https://www.ncbi.nlm.nih.gov/protein/Q6L6Q5.1"
                                              },
                                              {
                                                "name": "aprotinin [synthetic construct]",
                                                "molecular_weight": 6618,
                                                "descent_speed": 1432.772536058938,
                                                "ncbi_link": "https://www.ncbi.nlm.nih.gov/protein/CAA01755.1"
                                              }
                                            ])
        else:
            return False

    def test_file_get_protein_info(self):
        response = requests.post('http://127.0.0.1:8000/1DElectrophoresis/ProteinInfo/File?acrylamide=7.5&voltage=50')
        print(response.json())

    def test_batch_file_get_protein_info(self):
        response = requests.post('http://127.0.0.1:8000/1DElectrophoresis/BatchFileProtein/Batch?acrylamide=7.5&voltage=50')
        print(response.json())



if __name__ == '__main__':
    unittest.main()
