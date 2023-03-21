from datetime import datetime
from models.__all_models import *
from pydantic import BaseModel

class ReviewSchema(BaseModel):
    
    movie_name:str
    reviewer_name:str
    review:str
    created_at:datetime = datetime.now().strftime("%H:%M:%S")
    updated_at:datetime = datetime.now().strftime("%H:%M:%S")
    reviewer_id:int
    movie_id:int

    class Config:
        orm_mode = True
