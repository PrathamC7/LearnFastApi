from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.Product import Product
from app.schemas.ProductRequest import ProductRequest

class ProductRepository :
    def __init__(self, db : Session):
        self.db = db
    def get_all(self) -> list[Product] :
        stmt = select(Product)
        return list(self.db.scalars(stmt).all())
    
    def get_by_id(self, id) -> Product | None:
        return self.db.get(Product, id)
    
    def add_product(self, product : ProductRequest) :
        new_product = Product(name = product.name,
                    description = product.description,
                    quantity = product.quantity,
                    price = product.price)
        self.db.add(new_product)  # prepare to insert
        self.db.commit() # actually adds to the db
        self.db.refresh(new_product) # gets the final version of the object
        return new_product
    
    def update_product(self, id : int, product : ProductRequest) :
        updatable_product = self.db.get(Product, id)
        if updatable_product is None : return None
        # updatable_product.name = product.name
        # updatable_product.description = product.description
        # updatable_product.quantity = product.quantity
        # updatable_product.price = product.price
        data = product.model_dump()
        for field, value in data.items() :
            setattr(updatable_product, field, value)
        self.db.commit()
        self.db.refresh(updatable_product)
        return updatable_product
    
    def delete_product(self, id) :
        product = self.db.get(Product, id)
        if product is None : return None
        self.db.delete(product)
        self.db.commit()
        return product