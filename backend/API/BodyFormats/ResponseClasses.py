from pydantic import BaseModel


class ProteinInfo(BaseModel):
    """
    The content related to a protein for the
    frontend system
    """
    name: str
    molecular_weight: int
    descent_speed: float
    ncbi_link: str
