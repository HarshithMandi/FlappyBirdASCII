from pydantic import BaseModel, ValidationError, StrictInt


class User(BaseModel):
    name: str
    age: StrictInt
    email:str

try:
    user= User(name="Harshith",age=22,email="harshith.mandi@gmail.com")
    print(user.dict())
except ValidationError as e:
    print("ValidationError:",e)