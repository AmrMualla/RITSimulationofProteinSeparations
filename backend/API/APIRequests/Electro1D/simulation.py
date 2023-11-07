from fastapi import APIRouter

router = APIRouter(
    prefix='/1DElectrophoresis',
    tags=['1D Simulation']
)


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
