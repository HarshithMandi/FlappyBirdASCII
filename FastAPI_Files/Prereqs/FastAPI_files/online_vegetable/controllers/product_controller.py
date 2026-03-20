from fastapi import APIRouter, Depends, HTTPException
from schemas.product_schema import ProductCreate, ProductOut
from services.product_service import ProductService
from core.dependencies import get_product_service

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=ProductOut)
def create_product(product: ProductCreate, service: ProductService = Depends(get_product_service)):
    product_id = service.create_product(product)
    return {"id": product_id, **product.dict()}

@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: str, service: ProductService = Depends(get_product_service)):
    return service.get_product_by_id(product_id)