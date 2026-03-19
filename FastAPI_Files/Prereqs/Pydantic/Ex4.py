from pydantic import BaseModel, ValidationError, field_validator

class Employee(BaseModel):
    salary: float
    @field_validator('salary')
    @classmethod
    def check_salary(cls,value):
        if value<=10000:
            raise ValueError("salary too low")
        return value

try:
    emp= Employee(salary=19000)
    print("Valid Employee created")
    print(emp)
except ValidationError as e:
    print(e)

