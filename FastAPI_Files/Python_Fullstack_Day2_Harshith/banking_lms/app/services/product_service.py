from sqlalchemy.orm import Session

from app.exceptions.custom_exceptions import NotFoundError
from app.models.loan_product import LoanProduct
from app.repositories.product_repository import ProductRepository
from app.schemas.product_schema import LoanProductCreate, LoanProductUpdate


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create_product(self, db: Session, payload: LoanProductCreate) -> LoanProduct:
        product = LoanProduct(**payload.model_dump())
        with db.begin():
            return self.repository.create(db, product)

    def get_product(self, db: Session, product_id: int) -> LoanProduct:
        product = self.repository.get(db, product_id)
        if not product:
            raise NotFoundError("Loan product not found")
        return product

    def list_products(self, db: Session, skip: int, limit: int) -> list[LoanProduct]:
        return self.repository.list(db, skip, limit)

    def update_product(self, db: Session, product_id: int, payload: LoanProductUpdate) -> LoanProduct:
        product = self.get_product(db, product_id)
        update_data = payload.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(product, field, value)
        with db.begin():
            return self.repository.update(db, product)

    def delete_product(self, db: Session, product_id: int) -> None:
        product = self.get_product(db, product_id)
        with db.begin():
            self.repository.delete(db, product)
