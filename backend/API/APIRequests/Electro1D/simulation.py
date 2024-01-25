# author: Beck Anderson

from fastapi import APIRouter
from backend.API.BodyFormats.ResponseClasses import ProteinInfo

router = APIRouter(
    prefix='/1DElectrophoresis',
    tags=['1D Simulation']
)


@router.get("/standards", response_model=[ProteinInfo])
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


@router.get("/runInfo")
async def runSimulation():
    """
    TODO: Check if get is the right way to do this
    This will send simulation data to the server and
    return accurate information for how the simulation
    should be displayed visually
    :return: the names, weights in JSON(?) format
    """
    # return function that gets list of data for needed
    # proteins
    return {'outcome': "Simulation Data"}
