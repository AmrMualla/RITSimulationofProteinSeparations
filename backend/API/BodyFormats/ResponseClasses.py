from pydantic import BaseModel


class ProteinInfo(BaseModel):
    """
    The content related to a protein for the
    frontend system
    """
    name: str
    molecularWeight: float
    color: str
    id_num: str
    id_str: str
