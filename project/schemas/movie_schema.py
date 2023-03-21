from typing import List,Optional
from models.__all_models import *
from pydantic import BaseModel
from schemas.reviews_schema import ReviewSchema

class MovieSchema(BaseModel):
    name:str
    year:int
    description:str
    awards:str
    avarage_score:int

    class Config:
      orm_mode = True


class MovieReviewSchema(MovieSchema):
    reviews:Optional[List[ReviewSchema]]
