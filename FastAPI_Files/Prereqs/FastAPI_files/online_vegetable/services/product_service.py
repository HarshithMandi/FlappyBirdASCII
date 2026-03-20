from repositories.product_repository import ProductRepository
from models.product import Product
from schemas.product_schema import ProductCreate

class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo
    def create_product(self, product_data: ProductCreate):
        product = Product(**product_data.dict())
        return self.repo.create(product)
    def get_product(self, id: str):
        return self.repo.get_by_id(id)