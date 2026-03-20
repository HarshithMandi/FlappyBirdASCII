from fastapi import APIRouter, Depends, HTTPException
from schemas.product_schema import ProductCreate, ProductOut
from services.product_service import ProductService
from core.dependencies import get_product_service

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=ProductOut)
async def create_product(product: ProductCreate, service: ProductService = Depends(get_product_service)):
    product_id = await service.create_product(product)
    return {"id": product_id, **product.dict()}

@router.get("/{product_id}", response_model=ProductOut)
async def get_product(product_id: str, service: ProductService = Depends(get_product_service)):
    product = await service.get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product