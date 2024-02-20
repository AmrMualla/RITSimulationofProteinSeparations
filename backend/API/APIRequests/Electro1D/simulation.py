# author: Beck Anderson
import os

from fastapi import APIRouter, UploadFile
from typing import Any

from backend.API.BodyFormats.ResponseClasses import ProteinInfo
from backend.Electro1D import Protein

router = APIRouter(
    prefix='/1DElectrophoresis',
    tags=['1D Simulation']
)


@router.get("/standards", response_model=list[ProteinInfo])
async def standards() -> Any:
    """
    This function will get the information for the
    standards in the simulation. This currently includes the
    names, ncbi index number, and molecular weight, but may add additional values.
    Will never remove any. :)

    NOTE: we still need to analyze the data to
    :return: The data. Comes in a json format, but accessed easily.
    """
    return [{'name': 'D Chain D, Beta-galactosidase',
             'molecular_weight': 116062,
             'ncbi_link': 'https://www.ncbi.nlm.nih.gov/protein/6X1Q'},
            {'name': 'A Chain A, GLYCOGEN PHOSPHORYLASE B',
             'molecular_weight': 97158,
             'ncbi_link': 'https://www.ncbi.nlm.nih.gov/protein/2PRI'},
            {'name': 'B Chain B, Serum albumin',
             'molecular_weight': 66463,
             'ncbi_link': 'https://www.ncbi.nlm.nih.gov/protein/4F5S'},
            {'name': 'Ovalbumin [Gallus gallus]',
             'molecular_weight': 43772,
             'ncbi_link': 'https://www.ncbi.nlm.nih.gov/protein/AAA68882.1'},
            {'name': 'Carbonic anhydrase 2 [Mus musculus]',
             'molecular_weight': 29003,
             'ncbi_link': 'https://www.ncbi.nlm.nih.gov/protein/NP_001344263.1'},
            {'name': 'Pancreatic trypsin inhibitor [Musca domestica]',
             'molecular_weight': 22709,
             'ncbi_link': 'https://www.ncbi.nlm.nih.gov/protein/AFP63821.1'},
            {'name': 'LYS_OSTED',
             'molecular_weight': 14918,
             'ncbi_link': 'https://www.ncbi.nlm.nih.gov/protein/Q6L6Q5.1'},
            {'name': 'aprotinin [synthetic construct]',
             'molecular_weight': 6618,
             'ncbi_link': 'https://www.ncbi.nlm.nih.gov/protein/CAA01755.1'}
            ]


@router.post("/ProteinInfo/File", response_model=list[ProteinInfo])
async def fileGetProteinInfo(file: UploadFile) -> Any:
    """
    This call will take a file (in the fasta format) and parse
    the information, returning a list of proteins ready for
    the electrophoresis bands

    :return: the data in a list. Each element will be in the
        ProteinInfo format, including name, molecular weight,
        descent speed, and the link to their NCBI page.
    """
    protein = Protein
    return_list = []
    temp_data_file = open("temp_data_file.faa", "w+")
    try:
        content = file.file.read().decode("utf-8")
        temp_data_file.write(content)

        protein_dict = protein.parse_protein("temp_data_file.faa")
        weight_list = protein.get_mw("temp_data_file.faa")
        i = 0
        for seq_id in protein_dict.keys():
            if len(protein_dict[seq_id][0].split('|')) > 0:
                return_list.append({"name": " ".join(protein_dict[seq_id][0].split(' ')[1:]),
                                    "molecular_weight": weight_list[i],
                                    "ncbi_link": "https://www.ncbi.nlm.nih.gov/protein/" +
                                                 protein_dict[seq_id][0].split('|')[1]
                                    })
            else:
                return_list.append({"name": " ".join(protein_dict[seq_id][0].split(' ')[1:]),
                                    "molecular_weight": weight_list[i],
                                    "ncbi_link": "https://www.ncbi.nlm.nih.gov/protein/" +
                                                 protein_dict[seq_id][0].split('|')[0]
                                    })
            i += 1
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        temp_data_file.close()
        os.remove("temp_data_file.faa")
    return return_list


@router.post("/BatchFileProtein/Batch", response_model=list[list[ProteinInfo]])
async def batchFileGetProteinInfo(files: list[UploadFile]) -> Any:
    """
    This function will take a batch of files (in the fasta format),
    and parse the information, returning a dictionary of wells,
    each of which hold the list of protein bands for that well
    :return: a dictionary containing lists of proteins
    """
    well_data = []
    i = 0
    for file in files:
        well_data.append(await fileGetProteinInfo(file))
        i += 1
    return well_data
