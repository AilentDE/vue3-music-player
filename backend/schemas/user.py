from pydantic import BaseModel, EmailStr, constr, conint
from enum import Enum

class CountryEnum(str, Enum):
    USA = 'USA'
    Mexico = 'Mexico'
    Germany = 'Germany'

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    age: conint(ge=18)
    country: CountryEnum
    tos: bool