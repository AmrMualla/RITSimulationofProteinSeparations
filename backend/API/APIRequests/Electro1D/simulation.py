# author: Beck Anderson

from fastapi import APIRouter

router = APIRouter(
    prefix='/1DElectrophoresis',
    tags=['1D Simulation']
)


@router.get("/standards")
async def standards():
    """
    This function will get the information for the
    standards in the simulation. This currently includes the
    names and molecular weights, but may add additional values.
    Will never remove any. :)
    :return: The data. Comes in a json format, but accessed easily.
    """
    return {'standards':
                [{'name': 'Myosin',
                  'molecular_weight': 200},
                 {'name': 'β-galactosidase',
                  'molecular_weight': 116.3},
                 {'name': 'Phosphorylase b',
                  'molecular_weight': 97.4},
                 {'name': 'Bovine Serum Albumin',
                  'molecular_weight': 66.2},
                 {'name': 'Ovalbumin',
                  'molecular_weight': 45},
                 {'name': 'Carbonic Anhydrase',
                  'molecular_weight': 31},
                 {'name': 'Soybean Trypsin Inhibitor',
                  'molecular_weight': 21.5},
                 {'name': 'Lysozyme',
                  'molecular_weight': 14.4},
                 {'name': 'Aprotinin',
                  'molecular_weight': 6.5}
                 ]
            }


@router.get("/runInfo")
async def runSimulation():
    """
    TODO: Check if get is the right way to do this
    This will send simulation data to the server and
    return accurate information for how the simulation
    should be displayed visually
    :return: visual(?) data in JSON(?) format
    """
    return {'outcome': "Simulation Data"}
