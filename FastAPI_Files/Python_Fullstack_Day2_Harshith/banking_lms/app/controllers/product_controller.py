from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.product_repository import ProductRepository
from app.schemas.product_schema import LoanProductCreate, LoanProductOut, LoanProductUpdate
from app.services.product_service import ProductService

router = APIRouter()


def get_service() -> ProductService:
    return ProductService(ProductRepository())


@router.post("", response_model=LoanProductOut)
def create_product(payload: LoanProductCreate, db: Session = Depends(get_db)):
    return get_service().create_product(db, payload)


@router.get("/{product_id}", response_model=LoanProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return get_service().get_product(db, product_id)


@router.get("", response_model=list[LoanProductOut])
def list_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_service().list_products(db, skip, limit)


@router.put("/{product_id}", response_model=LoanProductOut)
def update_product(product_id: int, payload: LoanProductUpdate, db: Session = Depends(get_db)):
    return get_service().update_product(db, product_id, payload)


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    get_service().delete_product(db, product_id)
    return {"message": "Loan product deleted"}
