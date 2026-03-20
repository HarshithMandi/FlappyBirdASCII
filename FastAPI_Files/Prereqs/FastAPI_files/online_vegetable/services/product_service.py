from repositories.product_repository import ProductRepository
from models.product import Product
from schemas.product_schema import ProductCreate

class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    async def create_product(self, product_data: ProductCreate) -> str:
        product = Product(**product_data.dict())
        return await self.repo.create(product)

    async def get_product(self, id: str):
        return await self.repo.get_by_id(id)

    async def get_product_by_id(self, product_id: str):
        return await self.get_product(product_id)