from pydantic import BaseModel

class inputs(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float