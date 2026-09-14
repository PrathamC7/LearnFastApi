from sqlalchemy.orm import Session
from app.repositories.ProductRepository import ProductRepository
from app.schemas.ProductRequest import ProductRequest
from fastapi import HTTPException

class ProductService :
    def __init__(self, db : Session):
        self.repository = ProductRepository(db)
        
    def get_all(self) :
        return self.repository.get_all()
    
    def get_by_id(self, id) :
        product = self.repository.get_by_id(id)
        if product is None :
            raise HTTPException(
                status_code=400,
                detail=f"No product found with id {id}"
            )
        return product
    
    def add_product(self, product : ProductRequest) :
        try :
            return self.repository.add_product(product)
        except Exception as e :
            raise HTTPException(status_code=400, detail="Something went wrong")
    
    def update_product(self, id:int, product: ProductRequest) :
        updatable_product = self.repository.update_product(id, product)
        if updatable_product is None :
            raise HTTPException(status_code=404,
                                detail=f"No product found with product id {id}")
        return updatable_product
    
    def delete_product(self, id: int):
        delete_product = self.repository.delete_product(id)
        if delete_product is None :
            raise HTTPException(status_code=404,
                                detail = f"Product not found for id {id}")
        return delete_product