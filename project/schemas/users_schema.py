from typing import Optional,List
from pydantic import BaseModel,EmailStr
from models.__all_models import *
from datetime import datetime
from schemas.reviews_schema import ReviewSchema

class UserSchemaBase(BaseModel):
    username:str
    name:str
    surname:str
    email:EmailStr
    password:str
    created_at:datetime = datetime.now().strftime("%H:%M:%S")
    uid:str

    class Config:
        orm_mode = True

class UserAdmSchema(UserSchemaBase):
    permission = 1


class UserManagerSchema(UserSchemaBase):
    permission = 2


class UserCommumSchema(UserSchemaBase):
    permission = 3


class UserSchemaUp(UserSchemaBase):
    username:Optional[str]
    name:Optional[str]
    surname:Optional[str]
    email:Optional[EmailStr]
    password:Optional[str]

class UserSchemaReview(UserSchemaBase):
    reviews:Optional[List[ReviewSchema]]
