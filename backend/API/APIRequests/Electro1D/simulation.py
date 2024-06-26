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

ACCEPTED_FILE_TYPES = ['fasta', 'fas', 'fa', 'fna', 'ffn', 'faa', 'mpfa', 'frn']

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
    try:
        filetype = file.filename.split('.')[-1]
        if filetype in ACCEPTED_FILE_TYPES:
            with open("temp_data_file.faa", "w+") as temp_data_file:
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
        else:
            return_list = [
                {'name': 'unsupported file format',
                'molecularWeight': 0,
                'color': '',
                'id_num': '',
                'id_str': '',
                }
            ]
    except:
        return_list = [
            {'name': 'error',
            'molecularWeight': 0,
            'color': '',
            'id_num': '',
            'id_str': '',
            }
        ]
    finally:
        file.file.close()
        temp_data_file.close()
        os.remove("temp_data_file.faa")
    return return_list


def sort_files(file_list: list[UploadFile]):
    n = len(file_list)
    for i in range(n - 1):

        swapped = False
        for j in range(0, n - i - 1):

            if file_list[j].filename > file_list[j + 1].filename:
                swapped = True
                file_list[j], file_list[j + 1] = file_list[j + 1], file_list[j]

        if not swapped:
            return


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
    sort_files(files)
    for file in files:
        filetype = file.filename.split('.')[-1]
        if filetype in ACCEPTED_FILE_TYPES:
            well_data.append(await fileGetProteinInfo(file))
        i += 1
    return well_data
