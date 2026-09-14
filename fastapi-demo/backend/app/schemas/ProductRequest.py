from pydantic import BaseModel
class ProductRequest(BaseModel) :
    name : str
    description : str
    price : float
    quantity : int