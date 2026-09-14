from fastapi import APIRouter, Depends
from app.extensions import get_db
from sqlalchemy.orm import Session
from app.schemas. ProductRequest import ProductRequest
from app.schemas.ProductResponse import ProductResponse

from app.services.ProductService import ProductService
router = APIRouter()

@router.get("/", response_model = list[ProductResponse])
def get_all_Products(db : Session = Depends(get_db)):
    return ProductService(db).get_all()
@router.get("/{id}", response_model = ProductResponse)
def get_product_by_id(id : int, db : Session = Depends(get_db)) :
    return ProductService(db).get_by_id(id)

@router.post("/", response_model = ProductResponse, status_code = 201)
def add_product(product : ProductRequest, db : Session = Depends(get_db)) :
    return ProductService(db).add_product(product)

@router.put("/{id}", response_model = ProductResponse, status_code = 200)
def update_product(id : int, product : ProductRequest, db : Session = Depends(get_db)):
    return ProductService(db).update_product(id, product)

@router.delete("/{id}", response_model = ProductResponse, status_code = 200)
def delete_product(id : int, db : Session = Depends(get_db)) :
    return ProductService(db).delete_product(id)