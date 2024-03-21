# author: Beck Anderson
import os

from fastapi import APIRouter, UploadFile
from typing import Any
import random

from backend.API.BodyFormats.ResponseClasses import ProteinInfo
from backend.Electro1D import Protein

router = APIRouter(
    prefix='/1DElectrophoresis',
    tags=['1D Simulation']
)


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
                                    "molecularWeight": weight_list[i],
                                    "color": '#' + hex(random.randrange(0, 2**24))[2:],
                                    "id_num": protein_dict[seq_id][0].split('|')[1],
                                    "id_str": protein_dict[seq_id][0].split('|')[0]
                                    })
            else:
                return_list.append({"name": " ".join(protein_dict[seq_id][0].split(' ')[1:]),
                                    "molecularWeight": weight_list[i],
                                    "color": '#' + hex(random.randrange(0, 2**24))[2:],
                                    "id_num": protein_dict[seq_id][0].split('|')[0],
                                    "id_str": ''
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
