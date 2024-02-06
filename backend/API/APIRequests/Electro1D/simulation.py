# author: Beck Anderson
import os
import shutil

from fastapi import APIRouter, File, UploadFile
from typing import List

from backend.API.BodyFormats.ResponseClasses import ProteinInfo
from backend.Electro1D import Protein

router = APIRouter(
    prefix='/1DElectrophoresis',
    tags=['1D Simulation']
)


@router.get("/standards", response_model=List[ProteinInfo])
async def standards():
    """
    This function will get the information for the
    standards in the simulation. This currently includes the
    names, ncbi index number, and molecular weight, but may add additional values.
    Will never remove any. :)
    :return: The data. Comes in a json format, but accessed easily.
    """
    return {'standards':
                [{'short_name': 'Myosin',
                  'long_name': '',
                  'molecular_weight': 200,
                  'ncbi_index_num': 0},
                 {'short_name': 'β-galactosidase',
                  'long_name': '',
                  'molecular_weight': 116.3,
                  'ncbi_index_num': 0},
                 {'short_name': 'Phosphorylase b',
                  'long_name': '',
                  'molecular_weight': 97.4,
                  'ncbi_index_num': 0},
                 {'short_name': 'Bovine Serum Albumin',
                  'long_name': '',
                  'molecular_weight': 66.2,
                  'ncbi_index_num': 0},
                 {'short_name': 'Ovalbumin',
                  'long_name': '',
                  'molecular_weight': 45,
                  'ncbi_index_num': 0},
                 {'short_name': 'Carbonic Anhydrase',
                  'long_name': '',
                  'molecular_weight': 31,
                  'ncbi_index_num': 0},
                 {'short_name': 'Soybean Trypsin Inhibitor',
                  'long_name': '',
                  'molecular_weight': 21.5,
                  'ncbi_index_num': 0},
                 {'short_name': 'Lysozyme',
                  'long_name': '',
                  'molecular_weight': 14.4,
                  'ncbi_index_num': 0},
                 {'short_name': 'Aprotinin',
                  'long_name': '',
                  'molecular_weight': 6.5,
                  'ncbi_index_num': 0}
                 ]
            }


@router.post("/ProteinInfo/File")
async def fileGetProteinInfo(file: UploadFile, acrylamide: float, voltage: float):
    """
    This call will take a file contianing
    :return:
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
            return_list.append({'name': " ".join(protein_dict[seq_id][0].split(' ')[1:]),
                                'molecular_weight': weight_list[i],
                                'decent_speed': acrylamide * voltage * weight_list[i],
                                'ncbi_link': 'https://www.ncbi.nlm.nih.gov/protein/'+protein_dict[seq_id][0].split('|')[1]
                                })
            i += 1
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        temp_data_file.close()
        os.remove("temp_data_file.faa")
    return {"results": return_list}


@router.post("/BatchFileProtein/Batch", response_model=List[List[ProteinInfo]])
async def batchFileGetProteinInfo():
    """
    Temp
    :return:
    """
    return {'outcome': "Batch File Protein info"}
