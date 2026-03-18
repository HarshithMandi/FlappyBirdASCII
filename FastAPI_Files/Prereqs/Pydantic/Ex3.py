from pydantic import BaseModel, ValidationError, Field

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)
    stock: int= Field(..., gt=0)

try:
    product= Product(name="Laptop",price=50000,stock=10)
    print(product)
    print(product.model_dump())

except ValidationError as e:
    print("Validation error:", e)

try:
    product= Product(name="TV",price=-200000,stock=-9)
    print(product.dict())
except ValidationError as e:
    print("error: ", e)
