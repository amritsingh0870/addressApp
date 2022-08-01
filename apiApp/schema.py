from pydantic import BaseModel
from typing import Union

'''             Note
# Thsese are schema that are defined for request body'''


class addressDataCreate(BaseModel):
    address: str
    latitude:float
    longitude: float 
    contact : int 


class addressDataDelete(BaseModel):
    id: int


class addressDataUpdate(BaseModel):
    id:int
    address: Union[str,None]
    latitude:Union[float,None]
    longitude: Union[float,None] 
    contact : Union[int,None] 


class addressDataGet(BaseModel):
    latitude : float 
    longitude : float 