from fastapi import APIRouter, UploadFile
from backend.API.BodyFormats.ResponseClasses import ProteinInfo
from backend.Electro1D.Protein import *


router = APIRouter(
    prefix='/protein',
    tags=['Protein']
)


@router.get("/{protein_name}", response_model=ProteinInfo)
async def getProteinInfo(protein_name: str):
    """
    this function
    :param protein_name: the name of the protein
    :return:
    """
    # return function that gets list of data for needed
    # protein

    # TODO: Make function, until then...
    return {
        'short_name': None,
        'long_name': None,
        'molecular_weight': None,
        'id_num': None,
        'id_str': None
    }


@router.get("/file_get", response_model=[ProteinInfo])
async def fileGetProteinInfo(protein_file: UploadFile):
    """
    This API call will process a file and return the info
    related to each of them
    :param protein_file: The file with info on proteins
    :return: a list of the protein info. Each will follow
        the ProteinINfo class information.
    """
    proteins = []
    protein = Protein()
    protein_info = parse_protein(protein_file)
    protein_mw = get_mw(protein_file)

    # split by protein

    # for each protein:
        # split by info line
        # do function that gets list of data for needed protein
        # TODO: Make function, until then...

    return [
        {
            'short_name': None,
            'long_name': None,
            'molecular_weight': protein_mw,
            'ncbi_id': protein_info[0]
        },
        {
            'short_name': None,
            'long_name': None,
            'molecular_weight': None,
            'id_num': None,
            'id_str': None
        }
    ]
