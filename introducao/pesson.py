import warnings
from pydantic import BaseModel, EmailStr, ValidationError, validator


class User(BaseModel):
    name: str
    age: int
    email: EmailStr

    @validator('email')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('Invalid email address')
        return value

def f(user: User):
    print(user.name)
    print(user.age)
    print(user.email)

try:
    user = User(name='John', age=42, email='john@example.com')
    print(user)
except ValidationError as e:
    print(f"Validation Error: {e}")
