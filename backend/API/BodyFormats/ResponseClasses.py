from fastapi import UploadFile
from pydantic import BaseModel


class ProteinInfo(BaseModel):
    """
    The content related to a protein for the
    frontend system
    """
    short_name: str
    long_name: str
    molecular_weight: int
    ncbi_index_num: str
