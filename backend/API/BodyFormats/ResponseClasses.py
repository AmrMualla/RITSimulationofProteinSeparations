from pydantic import BaseModel


class ProteinInfo(BaseModel):
    """
    The content related to a protein for the
    frontend system
    """
    name: str
    molecular_weight: int
    ncbi_link: str
